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


def count_leading_spaces(text: str) -> int:
    return len(text) - len(text.lstrip(" "))


def render_inline_preface_tex(text: str) -> str:
    tokens: dict[str, str] = {}

    def stash(prefix: str, value: str) -> str:
        token = f"@@{prefix}{len(tokens)}@@"
        tokens[token] = value
        return token

    text = re.sub(
        r"\[(.*?)\]\((.*?)\)",
        lambda m: stash("LINK", rf"\href{{{m.group(2)}}}{{\textcolor{{blue}}{{{tex_escape(m.group(1))}}}}}"),
        text,
    )
    text = re.sub(
        r"`(.*?)`",
        lambda m: stash("CODE", rf"\colorbox{{gray!10}}{{\textcolor{{red!70!black}}{{{tex_escape(m.group(1))}}}}}"),
        text,
    )

    rendered = tex_escape(text)
    rendered = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", rendered)
    rendered = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\\textit{\1}", rendered)

    for token, value in tokens.items():
        rendered = rendered.replace(tex_escape(token), value)
    return rendered


def render_preface_heading(line: str) -> str | None:
    match = re.match(r"^(#{1,3})\s+(.*)$", line.strip())
    if match is None:
        return None

    hashes = match.group(1)
    heading_text = render_inline_preface_tex(match.group(2).strip())
    size = r"\Large" if len(hashes) == 1 else r"\normalsize"
    escaped_marker = hashes.replace("#", r"\#")
    return (
        r"\par"
        "\n"
        rf"{{{size}\bfseries\textcolor{{red!70!black}}{{{escaped_marker} {heading_text}}}}}"
        "\n"
        r"\par"
    )


def render_preface_paragraph(lines: list[str]) -> str:
    parts = [line.strip() for line in lines if line.strip()]
    return render_inline_preface_tex(" ".join(parts)) + r"\par"


def render_preface_blockquote(lines: list[str]) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in lines:
        stripped = line.strip()
        content = stripped[1:].lstrip() if stripped.startswith(">") else stripped
        if not content:
            if current:
                paragraphs.append(render_preface_paragraph(current))
                current = []
            continue
        current.append(content)
    if current:
        paragraphs.append(render_preface_paragraph(current))

    body = "\n".join(paragraphs)
    return (
        "\\begin{quote}\n"
        "\\setlength{\\parskip}{0.3em}\n"
        f"{body}\n"
        "\\end{quote}"
    )


def render_preface_fenced_block(lines: list[str]) -> str:
    body = "\n".join(tex_escape(raw_line) for raw_line in lines)
    return (
        "\\begin{mdframed}["
        "backgroundcolor=gray!10,"
        "linewidth=0.6pt,"
        "linecolor=gray!70,"
        "roundcorner=2pt,"
        "innerleftmargin=0.6em,"
        "innerrightmargin=0.6em,"
        "innertopmargin=0.5\\baselineskip,"
        "innerbottommargin=0.5\\baselineskip"
        "]\n"
        "\\begingroup\n"
        "\\small\n"
        "\\setlength{\\parindent}{0pt}\n"
        "\\setlength{\\parskip}{0pt}\n"
        "\\begin{alltt}\n"
        f"{body}\n"
        "\\end{alltt}\n"
        "\\endgroup\n"
        "\\end{mdframed}"
    )


def render_preface_list(lines: list[str], start: int, indent: int) -> tuple[str, int]:
    first_content = lines[start][indent:]
    ordered = re.match(r"\d+\.\s+", first_content) is not None
    marker_pattern = r"\d+\.\s+" if ordered else r"[-*]\s+"
    env = "enumerate" if ordered else "itemize"

    items: list[str] = []
    index = start
    while index < len(lines):
        raw_line = lines[index]
        if not raw_line.strip():
            index += 1
            continue

        current_indent = count_leading_spaces(raw_line)
        stripped = raw_line[current_indent:]
        if current_indent < indent:
            break
        if current_indent != indent or re.match(marker_pattern, stripped) is None:
            break

        item_text = re.sub(marker_pattern, "", stripped, count=1)
        item_parts = [render_inline_preface_tex(item_text)]
        index += 1

        child_start = index
        while index < len(lines):
            probe = lines[index]
            if not probe.strip():
                index += 1
                continue

            probe_indent = count_leading_spaces(probe)
            probe_stripped = probe[probe_indent:]
            if probe_indent < indent:
                break
            if probe_indent == indent:
                break
            index += 1

        child_lines = lines[child_start:index]
        child_nonblank = [line for line in child_lines if line.strip()]
        if child_nonblank:
            child_indent = min(count_leading_spaces(line) for line in child_nonblank)
            child_body, consumed = render_preface_blocks(child_lines, 0, child_indent)
            if consumed != len(child_lines):
                raise ValueError("failed to consume nested preface list block")
            if child_body.strip():
                item_parts.append(child_body.strip())

        items.append("\\item " + "\n".join(item_parts))

    body = "\n".join(items)
    return (
        "\\begin{"
        + env
        + "}\n"
        + "\\setlength{\\itemsep}{0.15em}\n"
        + "\\setlength{\\parskip}{0pt}\n"
        + body
        + "\n\\end{"
        + env
        + "}"
    ), index


def render_preface_blocks(lines: list[str], start: int = 0, base_indent: int = 0) -> tuple[str, int]:
    parts: list[str] = []
    index = start
    while index < len(lines):
        raw_line = lines[index]
        if not raw_line.strip():
            index += 1
            continue

        indent = count_leading_spaces(raw_line)
        if indent < base_indent:
            break

        stripped = raw_line[indent:]
        heading = render_preface_heading(stripped)
        if indent == base_indent and heading is not None:
            parts.append(heading)
            index += 1
            continue

        if indent == base_indent and stripped.startswith("```"):
            fence_lines: list[str] = []
            index += 1
            while index < len(lines):
                probe = lines[index]
                probe_indent = count_leading_spaces(probe)
                probe_stripped = probe[probe_indent:]
                if probe_indent == base_indent and probe_stripped.startswith("```"):
                    index += 1
                    break
                fence_lines.append(probe[base_indent:] if probe.startswith(" " * base_indent) else probe)
                index += 1
            else:
                raise ValueError("unterminated fenced block in preface markdown")

            parts.append(render_preface_fenced_block(fence_lines))
            continue

        if indent == base_indent and re.match(r"(?:\d+\.\s+|[-*]\s+)", stripped):
            rendered_list, index = render_preface_list(lines, index, indent)
            parts.append(rendered_list)
            continue

        if indent == base_indent and stripped.startswith(">"):
            quote_lines: list[str] = []
            while index < len(lines):
                probe = lines[index]
                if not probe.strip():
                    quote_lines.append(probe)
                    index += 1
                    continue

                probe_indent = count_leading_spaces(probe)
                probe_stripped = probe[probe_indent:]
                if probe_indent != base_indent or not probe_stripped.startswith(">"):
                    break
                quote_lines.append(probe)
                index += 1
            parts.append(render_preface_blockquote(quote_lines))
            continue

        paragraph_lines = [stripped]
        index += 1
        while index < len(lines):
            probe = lines[index]
            if not probe.strip():
                break

            probe_indent = count_leading_spaces(probe)
            probe_stripped = probe[probe_indent:]
            if probe_indent < base_indent:
                break
            if probe_indent == base_indent and (
                render_preface_heading(probe_stripped) is not None
                or re.match(r"(?:\d+\.\s+|[-*]\s+)", probe_stripped)
                or probe_stripped.startswith(">")
            ):
                break

            paragraph_lines.append(probe[probe_indent:].strip())
            index += 1
        parts.append(render_preface_paragraph(paragraph_lines))

    return "\n\n".join(parts), index


def markdown_preface_to_tex(text: str) -> str:
    """Render a narrow markdown subset for the boxed preface."""
    if not text.strip():
        return "This preface has not been provided yet."

    rendered, consumed = render_preface_blocks(text.splitlines())
    if consumed != len(text.splitlines()):
        raise ValueError("failed to consume preface markdown")
    return rendered.strip()


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
        "\\usepackage{alltt}",
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
