#!/usr/bin/env bash
# How to run: bash finalization/build-final.sh
# Inputs: paper/paper.tex, paper/references.bib, paper/exhibits/*, finalization/inputs/*
# Outputs: finalization/output/preface.tex, finalization/output/acknowledgments.tex,
#     finalization/output/final-appendix.tex,
#     finalization/output/paper-anonymous.tex, finalization/output/paper-named.tex,
#     finalization/output/paper-anonymous.pdf, finalization/output/paper-named.pdf
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FINAL_DIR="$REPO_ROOT/finalization"
OUTPUT_DIR="$FINAL_DIR/output"
BUILD_LOG="$OUTPUT_DIR/.latex-build.log"

mkdir -p "$OUTPUT_DIR"

python3 - <<'PY'
from __future__ import annotations

import pathlib
import re
import tomllib


REPO_ROOT = pathlib.Path.cwd()
FINALIZATION_DIR = REPO_ROOT / "finalization"
INPUTS_DIR = FINALIZATION_DIR / "inputs"
OUTPUT_DIR = FINALIZATION_DIR / "output"
TEMPLATES_DIR = FINALIZATION_DIR / "templates"
PAPER_PATH = REPO_ROOT / "paper" / "paper.tex"


def load_toml(path: pathlib.Path) -> dict[str, object]:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def render_template(path: pathlib.Path, replacements: dict[str, str]) -> str:
    text = path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace(f"{{{{ {key} }}}}", value)
    return text


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def markdown_preface_to_tex(text: str) -> str:
    """Render the preface markdown using the Prompts-to-Paper readme-appendix style.

    Supports: headings (#, ##, ...), links [text](url), inline code `x`.
    Minimally escapes &, %, _, $ so authored literals survive. Other LaTeX
    metacharacters (\\, {, }, #) are left untouched so injected commands work,
    matching Prompts-to-Paper's trade-off.
    """
    if not text.strip():
        return "This preface has not been provided yet."

    # Minimal escape first (do NOT touch \, {, }, #)
    for char, repl in (("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("$", r"\$")):
        text = text.replace(char, repl)

    # Promote markdown headings to larger colored lines (before escaping #)
    def render_heading(match: re.Match[str]) -> str:
        hashes = match.group(1)
        heading_text = match.group(2).strip()
        size = r"\Large" if len(hashes) == 1 else r"\normalsize"
        escaped_marker = hashes.replace("#", r"\#")
        return (
            r"\par"
            "\n"
            rf"{{{size}\bfseries\textcolor{{red!70!black}}{{{escaped_marker} {heading_text}}}}}"
            "\n"
            r"\par"
        )

    text = re.sub(
        r"^(#{1,3})\s+(.*)$",
        render_heading,
        text,
        flags=re.MULTILINE,
    )

    # Escape remaining #
    text = re.sub(r"(?<!\\)#", r"\\#", text)

    # Markdown links -> colored \href
    text = re.sub(
        r"\[(.*?)\]\((.*?)\)",
        r"\\href{\2}{\\textcolor{blue}{\1}}",
        text,
    )

    # Inline code -> colorbox
    text = re.sub(
        r"`(.*?)`",
        r"\\colorbox{gray!10}{\\textcolor{red!70!black}{\1}}",
        text,
    )

    return text.strip()


def read_section(markdown_path: pathlib.Path, heading: str) -> str:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    start = None
    heading_level = heading.count("#")
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index + 1
            break
    if start is None:
        raise ValueError(f"could not find heading {heading!r} in {markdown_path}")

    collected: list[str] = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith("#") and stripped.count("#") <= heading_level:
            break
        collected.append(line)
    return "\n".join(collected).strip()


def extract_prompt_block(script_path: pathlib.Path) -> str:
    source = script_path.read_text(encoding="utf-8")
    match = re.search(r'prompt\s*=\s*f?("""|\'\'\')\n?(.*?)(?:\1)', source, re.DOTALL)
    if match is None:
        raise ValueError(f"could not extract prompt block from {script_path}")
    prompt = match.group(2).strip()
    if prompt.startswith("\\\n"):
        prompt = prompt[2:]
    elif prompt == "\\":
        prompt = ""
    return prompt.strip()


def format_preformatted_tex(body: str) -> str:
    lines: list[str] = []
    for raw_line in body.splitlines():
        if not raw_line.strip():
            lines.append(r"\vspace{0.4em}")
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        prefix = f"\\hspace*{{{0.5 * indent:.1f}em}}" if indent else ""
        lines.append(prefix + tex_escape(raw_line.lstrip(" ")) + r"\\")
    return "\n".join(lines)


def build_verbatim_block(title: str, body: str) -> str:
    return (
        f"\\subsection{{{tex_escape(title)}}}\n"
        "\\begingroup\n"
        "\\ttfamily\n"
        "\\small\n"
        "\\setlength{\\parindent}{0pt}\n"
        "\\setlength{\\parskip}{0.25em}\n"
        f"{format_preformatted_tex(body.strip())}\n"
        "\\endgroup\n"
    )


def build_appendix_tex(manifest: dict[str, object]) -> str:
    parts: list[str] = []

    for section in manifest.get("spec_sections", []):
        item = dict(section)
        path = REPO_ROOT / str(item["path"])
        heading = str(item["heading"])
        title = str(item["title"])
        parts.append(build_verbatim_block(title, read_section(path, heading)))

    for prompt_file in manifest.get("prompt_files", []):
        item = dict(prompt_file)
        path = REPO_ROOT / str(item["path"])
        title = str(item["title"])
        parts.append(build_verbatim_block(title, extract_prompt_block(path)))

    return render_template(
        TEMPLATES_DIR / "appendix.tex.j2",
        {
            "appendix_title": tex_escape(str(manifest.get("title", "Transparency Appendix"))),
            "appendix_body": "\n".join(parts).strip(),
        },
    )


def build_preface_tex(preface_markdown: str) -> str:
    return render_template(
        TEMPLATES_DIR / "preface.tex.j2",
        {"preface_body": markdown_preface_to_tex(preface_markdown)},
    )


def inject_preface(tex_source: str, preface_tex: str) -> str:
    pattern = re.compile(
        r"\n\\section\*\{Preface[^}]*\}\s*\n(?:\\vspace\{[^}]*\}\s*\n)?(.*?)(\n\\section\{Introduction\})",
        re.DOTALL,
    )
    match = pattern.search(tex_source)
    if match is None:
        raise ValueError("could not locate preface block in paper.tex")
    return (
        tex_source[:match.start()]
        + "\n\\vspace{1.0em}\n"
        + preface_tex
        + "\n"
        + match.group(2)
        + tex_source[match.end():]
    )


def inject_appendix(tex_source: str, appendix_tex: str) -> str:
    marker = "\\printbibliography"
    replacement = appendix_tex + "\n\n" + marker
    if marker not in tex_source:
        raise ValueError("could not locate bibliography marker in paper.tex")
    return tex_source.replace(marker, replacement, 1)


def inject_final_packages(tex_source: str) -> str:
    packages = [
        "\\usepackage{xcolor}",
        "\\usepackage{mdframed}",
        "\\usepackage{hyperref}",
    ]
    to_add = [pkg for pkg in packages if pkg not in tex_source]
    if not to_add:
        return tex_source

    marker = "\\title{"
    if marker not in tex_source:
        raise ValueError("could not locate package insertion point in paper.tex")
    replacement = "\n".join(to_add) + "\n\n" + marker
    return tex_source.replace(marker, replacement, 1)


def rewrite_paths_for_output(tex_source: str) -> str:
    updated = tex_source.replace(r"\addbibresource{references.bib}", r"\addbibresource{../../paper/references.bib}")
    updated = updated.replace("{exhibits/", "{../../paper/exhibits/")
    return updated


def build_acknowledgments_tex(markdown: str) -> str:
    """Render acknowledgments markdown to a single TeX blob for a \\thanks footnote.

    Collapses paragraphs with \\par, minimally escapes &, %, _, $, #. Leaves
    braces and backslashes alone so authors can embed small LaTeX commands.
    """
    paragraphs = [block.strip() for block in re.split(r"\n\s*\n", markdown.strip()) if block.strip()]
    if not paragraphs:
        return ""

    def escape(text: str) -> str:
        for char, repl in (("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("$", r"\$"), ("#", r"\#")):
            text = text.replace(char, repl)
        return text

    return r"\par ".join(escape(p) for p in paragraphs)


def set_named_metadata(tex_source: str, author_info: dict[str, object], acknowledgments_tex: str) -> str:
    name = str(author_info.get("name", "")).strip()
    affiliation = str(author_info.get("affiliation", "")).strip()
    email = str(author_info.get("email", "")).strip()
    date = str(author_info.get("date", "")).strip()

    author_lines = [tex_escape(name)] if name else []
    if affiliation:
        author_lines.append(tex_escape(affiliation))
    if email:
        author_lines.append(r"\texttt{" + tex_escape(email) + "}")
    author_tex = r" \\ ".join(author_lines)

    updated = re.sub(
        r"\\author\{.*?\}",
        lambda _: f"\\author{{{author_tex}}}",
        tex_source,
        count=1,
        flags=re.DOTALL,
    )
    updated = re.sub(
        r"\\date\{.*?\}",
        lambda _: f"\\date{{{tex_escape(date)}}}",
        updated,
        count=1,
        flags=re.DOTALL,
    )

    if acknowledgments_tex:
        updated = re.sub(
            r"\\title\{(.*?)\}",
            lambda m: f"\\title{{{m.group(1)}\\thanks{{{acknowledgments_tex}}}}}",
            updated,
            count=1,
            flags=re.DOTALL,
        )

    return updated


def build_variant(
    tex_source: str,
    author_info: dict[str, object],
    acknowledgments_tex: str,
    named: bool,
) -> str:
    updated = inject_final_packages(tex_source)
    if named:
        updated = set_named_metadata(updated, author_info, acknowledgments_tex)
    return rewrite_paths_for_output(updated)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = load_toml(INPUTS_DIR / "appendix-manifest.toml")
    author_info = load_toml(INPUTS_DIR / "author-info.toml")
    preface_markdown = (INPUTS_DIR / "preface.md").read_text(encoding="utf-8")
    acknowledgments_path = INPUTS_DIR / "acknowledgments.md"
    acknowledgments_markdown = (
        acknowledgments_path.read_text(encoding="utf-8") if acknowledgments_path.exists() else ""
    )
    canonical_tex = PAPER_PATH.read_text(encoding="utf-8")

    preface_tex = build_preface_tex(preface_markdown)
    appendix_tex = build_appendix_tex(manifest)
    acknowledgments_tex = build_acknowledgments_tex(acknowledgments_markdown)

    shared_tex = inject_appendix(inject_preface(canonical_tex, preface_tex), appendix_tex)
    anonymous_tex = build_variant(shared_tex, author_info, acknowledgments_tex, named=False)
    named_tex = build_variant(shared_tex, author_info, acknowledgments_tex, named=True)

    (OUTPUT_DIR / "preface.tex").write_text(preface_tex + "\n", encoding="utf-8")
    (OUTPUT_DIR / "acknowledgments.tex").write_text(acknowledgments_tex + "\n", encoding="utf-8")
    (OUTPUT_DIR / "final-appendix.tex").write_text(appendix_tex + "\n", encoding="utf-8")
    (OUTPUT_DIR / "paper-anonymous.tex").write_text(anonymous_tex + "\n", encoding="utf-8")
    (OUTPUT_DIR / "paper-named.tex").write_text(named_tex + "\n", encoding="utf-8")


main()
PY

run_quiet() {
    local label="$1"
    shift

    if ! "$@" >>"$BUILD_LOG" 2>&1; then
        echo "ERROR: $label failed. See $BUILD_LOG" >&2
        tail -n 40 "$BUILD_LOG" >&2
        exit 1
    fi
}

compile_tex() {
    local tex_file="$1"
    local base_name="$2"

    (
        cd "$OUTPUT_DIR"
        run_quiet "pdflatex pass 1 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
        run_quiet "biber ($base_name)" biber --output-safechars "$base_name"
        run_quiet "pdflatex pass 2 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
        run_quiet "pdflatex pass 3 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
    )
}

: > "$BUILD_LOG"

compile_tex "paper-anonymous.tex" "paper-anonymous"
compile_tex "paper-named.tex" "paper-named"

echo "[build-final] built finalization/output/paper-anonymous.pdf"
echo "[build-final] built finalization/output/paper-named.pdf"
