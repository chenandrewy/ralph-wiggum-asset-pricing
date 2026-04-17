#!/usr/bin/env python3
# How to run: python3 finalization/build-final.py
# Inputs: paper/paper.tex, finalization/inputs/*, finalization/templates/*
# Outputs: finalization/output-anon/paper.tex, finalization/output-named/paper.tex,
#     plus local bibliography and exhibit dependencies in each output folder
from __future__ import annotations

import pathlib
import re
import shutil
import tomllib


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
FINALIZATION_DIR = REPO_ROOT / "finalization"
INPUTS_DIR = FINALIZATION_DIR / "inputs"
OUTPUT_ANON_DIR = FINALIZATION_DIR / "output-anon"
OUTPUT_NAMED_DIR = FINALIZATION_DIR / "output-named"
TEMPLATES_DIR = FINALIZATION_DIR / "templates"
PAPER_PATH = REPO_ROOT / "paper" / "paper.tex"
REFERENCES_PATH = REPO_ROOT / "paper" / "references.bib"
EXHIBIT_PATHS = [
    REPO_ROOT / "paper" / "exhibits" / "fig-ai-valuations.pdf",
    REPO_ROOT / "paper" / "exhibits" / "fig-extension-panels.pdf",
    REPO_ROOT / "paper" / "exhibits" / "table-pd-ratios.tex",
]


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


def render_inline_markdown_tex(text: str, monochrome: bool = False) -> str:
    tokens: dict[str, str] = {}

    def stash(prefix: str, value: str) -> str:
        token = f"@@{prefix}{len(tokens)}@@"
        tokens[token] = value
        return token

    def render_link(label: str, target: str) -> str:
        return stash(
            "LINK",
            (
                (
                    rf"\hyperref[{target[1:]}]{{{tex_escape(label)}}}"
                    if target.startswith("#")
                    else rf"\href{{{target}}}{{{tex_escape(label)}}}"
                )
                if monochrome
                else (
                    rf"\hyperref[{target[1:]}]{{\textcolor{{blue}}{{{tex_escape(label)}}}}}"
                    if target.startswith("#")
                    else rf"\href{{{target}}}{{\textcolor{{blue}}{{{tex_escape(label)}}}}}"
                )
            ),
        )

    text = re.sub(
        r"\[(.*?)\]\((.*?)\)",
        lambda m: render_link(m.group(1), m.group(2)),
        text,
    )
    text = re.sub(
        r"\((.*?)\)\[(.*?)\]",
        lambda m: render_link(m.group(1), m.group(2)),
        text,
    )
    text = re.sub(
        r"`(.*?)`",
        lambda m: stash(
            "CODE",
            rf"\texttt{{{tex_escape(m.group(1))}}}"
            if monochrome
            else rf"\colorbox{{gray!10}}{{\textcolor{{red!70!black}}{{{tex_escape(m.group(1))}}}}}",
        ),
        text,
    )
    text = re.sub(
        r"\*\*(.+?)\*\*",
        lambda m: stash("BOLD", rf"\textbf{{{tex_escape(m.group(1))}}}"),
        text,
    )
    text = re.sub(
        r"__(.+?)__",
        lambda m: stash("BOLD", rf"\textbf{{{tex_escape(m.group(1))}}}"),
        text,
    )
    text = re.sub(
        r"(?<!\*)\*(?![\s*])(.+?)(?<![\s*])\*(?!\*)",
        lambda m: stash("ITALIC", rf"\textit{{{tex_escape(m.group(1))}}}"),
        text,
    )

    rendered = tex_escape(text)

    for token, value in tokens.items():
        rendered = rendered.replace(tex_escape(token), value)
    return rendered


def render_markdown_heading(line: str, monochrome: bool = False) -> str | None:
    match = re.match(r"^(#{1,3})\s+(.*)$", line.strip())
    if match is None:
        return None

    hashes = match.group(1)
    heading_text = render_inline_markdown_tex(match.group(2).strip(), monochrome=monochrome)
    size = r"\Large" if len(hashes) == 1 else r"\large"
    color_prefix = "" if monochrome else r"\textcolor{red!70!black}{"
    color_suffix = "" if monochrome else "}"
    marker_text = "" if monochrome else hashes.replace("#", r"\#") + " "
    return (
        r"\par"
        "\n"
        rf"{{{size}\bfseries {color_prefix}{marker_text}{heading_text}{color_suffix}}}"
        "\n"
        r"\par"
    )


def render_markdown_paragraph(lines: list[str], monochrome: bool = False) -> str:
    parts = [line.strip() for line in lines if line.strip()]
    return render_inline_markdown_tex(" ".join(parts), monochrome=monochrome)


def render_markdown_blockquote(lines: list[str], monochrome: bool = False) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in lines:
        stripped = line.strip()
        content = stripped[1:].lstrip() if stripped.startswith(">") else stripped
        if not content:
            if current:
                paragraphs.append(render_markdown_paragraph(current, monochrome=monochrome))
                current = []
            continue
        current.append(content)
    if current:
        paragraphs.append(render_markdown_paragraph(current, monochrome=monochrome))

    body = "\n".join(paragraphs)
    line_color = "black!55" if monochrome else "blue!45!black"
    return (
        "\\begin{tcolorbox}["
        "enhanced,"
        "breakable,"
        "colback=white,"
        "boxrule=0pt,"
        "frame hidden,"
        "sharp corners,"
        "left=0.9em,right=0em,"
        "top=0.15em,bottom=0.15em,"
        "before skip=0.75\\baselineskip,"
        "after skip=0.6\\baselineskip,"
        f"borderline west={{2pt}}{{0pt}}{{{line_color}}}"
        "]\n"
        "\\setlength{\\parskip}{0.3em}\n"
        f"{body}\n"
        "\\end{tcolorbox}"
    )


def render_fenced_block_line_tex(text: str) -> str:
    tokens: dict[str, str] = {}

    def stash(value: str) -> str:
        token = f"@@FENCELINK{len(tokens)}@@"
        tokens[token] = value
        return token

    def render_link(label: str, target: str) -> str:
        if target.startswith("#"):
            return stash(
                rf"\hyperref[{target[1:]}]{{\textcolor{{blue}}{{{tex_escape(label)}}}}}"
            )
        return stash(rf"\href{{{target}}}{{\textcolor{{blue}}{{{tex_escape(label)}}}}}")

    text = re.sub(
        r"\[(.*?)\]\((.*?)\)",
        lambda m: render_link(m.group(1), m.group(2)),
        text,
    )
    rendered = tex_escape(text)
    for token, value in tokens.items():
        rendered = rendered.replace(tex_escape(token), value)
    return rendered


def render_preface_fenced_block(lines: list[str]) -> str:
    body = "\n".join(render_fenced_block_line_tex(raw_line) for raw_line in lines)
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


def split_markdown_table_row(row: str) -> list[str]:
    stripped = row.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def is_markdown_table_separator(line: str) -> bool:
    cells = split_markdown_table_row(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell) is not None for cell in cells)


def is_markdown_table_start(lines: list[str], index: int, base_indent: int) -> bool:
    if index + 1 >= len(lines):
        return False
    first_line = lines[index]
    second_line = lines[index + 1]
    if not first_line.strip() or not second_line.strip():
        return False

    first_indent = count_leading_spaces(first_line)
    second_indent = count_leading_spaces(second_line)
    if first_indent != base_indent or second_indent != base_indent:
        return False

    first_stripped = first_line[first_indent:]
    second_stripped = second_line[second_indent:]
    if "|" not in first_stripped or "|" not in second_stripped:
        return False

    header_cells = split_markdown_table_row(first_stripped)
    separator_cells = split_markdown_table_row(second_stripped)
    if len(header_cells) < 2 or len(header_cells) != len(separator_cells):
        return False
    return is_markdown_table_separator(second_stripped)


def render_markdown_table(lines: list[str], start: int, base_indent: int, monochrome: bool = False) -> tuple[str, int]:
    header_cells = split_markdown_table_row(lines[start][base_indent:])

    body_rows: list[list[str]] = []
    index = start + 2
    while index < len(lines):
        raw_line = lines[index]
        if not raw_line.strip():
            break
        indent = count_leading_spaces(raw_line)
        if indent != base_indent:
            break
        stripped = raw_line[indent:]
        if "|" not in stripped:
            break
        cells = split_markdown_table_row(stripped)
        if len(cells) != len(header_cells) or is_markdown_table_separator(stripped):
            break
        body_rows.append(cells)
        index += 1

    alignment = "l" * len(header_cells)

    def render_row(cells: list[str]) -> str:
        rendered_cells = [render_inline_markdown_tex(cell, monochrome=monochrome) for cell in cells]
        return " & ".join(rendered_cells) + r" \\"

    rendered_lines = [
        r"\begin{center}",
        r"\small",
        rf"\begin{{tabular}}{{{alignment}}}",
        r"\toprule",
        render_row(header_cells),
        r"\midrule",
        *[render_row(row) for row in body_rows],
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{center}",
    ]
    return "\n".join(rendered_lines), index


def render_markdown_list(
    lines: list[str],
    start: int,
    indent: int,
    first_level: bool = False,
    monochrome: bool = False,
) -> tuple[str, int]:
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
        item_label = ""
        if not ordered:
            label_match = re.match(r"((?:\d+|[a-z]|[ivxlcdm]+)\.)\s+(.*)$", item_text)
            if label_match is not None:
                item_label = f"[{tex_escape(label_match.group(1))}]"
                item_text = label_match.group(2)
        item_parts = [render_inline_markdown_tex(item_text, monochrome=monochrome)]
        index += 1

        child_start = index
        while index < len(lines):
            probe = lines[index]
            if not probe.strip():
                index += 1
                continue

            probe_indent = count_leading_spaces(probe)
            if probe_indent < indent or probe_indent == indent:
                break
            index += 1

        child_lines = lines[child_start:index]
        child_nonblank = [line for line in child_lines if line.strip()]
        if child_nonblank:
            child_indent = min(count_leading_spaces(line) for line in child_nonblank)
            child_body, consumed = render_markdown_blocks(child_lines, 0, child_indent, monochrome=monochrome)
            if consumed != len(child_lines):
                raise ValueError("failed to consume nested preface list block")
            if child_body.strip():
                item_parts.append(child_body.strip())

        items.append("\\item" + item_label + " " + "\n".join(item_parts))

    body = "\n".join(items)
    return (
        ("\\vspace{-2ex}\n" if first_level else "")
        + "\\begin{"
        + env
        + "}\n"
        + "\\setlength{\\itemsep}{0.15em}\n"
        + "\\setlength{\\parskip}{0pt}\n"
        + body
        + "\n\\end{"
        + env
        + "}\n"
        + ("\\vspace{-2ex}" if first_level else "")
    ), index


def render_markdown_blocks(
    lines: list[str],
    start: int = 0,
    base_indent: int = 0,
    monochrome: bool = False,
) -> tuple[str, int]:
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
        heading = render_markdown_heading(stripped, monochrome=monochrome)
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
            rendered_list, index = render_markdown_list(
                lines,
                index,
                indent,
                first_level=(base_indent == 0),
                monochrome=monochrome,
            )
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
            parts.append(render_markdown_blockquote(quote_lines, monochrome=monochrome))
            continue

        if indent == base_indent and is_markdown_table_start(lines, index, base_indent):
            rendered_table, index = render_markdown_table(lines, index, base_indent, monochrome=monochrome)
            parts.append(rendered_table)
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
                render_markdown_heading(probe_stripped, monochrome=monochrome) is not None
                or re.match(r"(?:\d+\.\s+|[-*]\s+)", probe_stripped)
                or probe_stripped.startswith(">")
                or is_markdown_table_start(lines, index, base_indent)
            ):
                break

            paragraph_lines.append(probe[probe_indent:].strip())
            index += 1
        parts.append(render_markdown_paragraph(paragraph_lines, monochrome=monochrome))

    return "\n\n".join(parts), index


def markdown_preface_to_tex(text: str) -> str:
    """Render a narrow markdown subset for the boxed preface."""
    if not text.strip():
        return "This preface has not been provided yet."

    rendered, consumed = render_markdown_blocks(text.splitlines())
    if consumed != len(text.splitlines()):
        raise ValueError("failed to consume preface markdown")
    return rendered.strip()


def build_preface_tex(preface_markdown: str) -> str:
    return render_template(
        TEMPLATES_DIR / "preface.tex.j2",
        {"preface_body": markdown_preface_to_tex(preface_markdown)},
    )


def inject_preface(tex_source: str, preface_tex: str) -> str:
    intro_matches = list(re.finditer(r"\n\\section\{Introduction\}", tex_source))
    if len(intro_matches) != 1:
        raise ValueError("expected exactly one introduction section in paper.tex")

    intro_start = intro_matches[0].start()
    before_intro = tex_source[:intro_start]
    after_intro = tex_source[intro_start:]

    placeholder_pattern = re.compile(
        r"\n\\section\*\{Preface[^}]*\}\s*\n(?:\\vspace\{[^}]*\}\s*\n)?",
        re.DOTALL,
    )
    before_intro = placeholder_pattern.sub("\n", before_intro, count=1)

    return before_intro + "\n\\vspace{1.0em}\n" + preface_tex + after_intro


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
        "\\usepackage[most]{tcolorbox}",
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
    return updated


def write_output_bundle(bundle_dir: pathlib.Path, tex_source: str) -> None:
    bundle_dir.mkdir(parents=True, exist_ok=True)
    exhibits_dir = bundle_dir / "exhibits"
    exhibits_dir.mkdir(parents=True, exist_ok=True)

    (bundle_dir / "paper.tex").write_text(tex_source + "\n", encoding="utf-8")
    shutil.copy2(REFERENCES_PATH, bundle_dir / REFERENCES_PATH.name)
    for exhibit_path in EXHIBIT_PATHS:
        shutil.copy2(exhibit_path, exhibits_dir / exhibit_path.name)


def main() -> None:
    author_info = load_toml(INPUTS_DIR / "author-info.toml")
    preface_markdown = (INPUTS_DIR / "preface.md").read_text(encoding="utf-8")
    appendix_tex = (INPUTS_DIR / "additional-appendix.tex").read_text(encoding="utf-8")
    acknowledgments_path = INPUTS_DIR / "acknowledgments.md"
    acknowledgments_markdown = acknowledgments_path.read_text(encoding="utf-8") if acknowledgments_path.exists() else ""
    canonical_tex = PAPER_PATH.read_text(encoding="utf-8")

    preface_tex = build_preface_tex(preface_markdown)
    acknowledgments_tex = build_acknowledgments_tex(acknowledgments_markdown)

    shared_tex = inject_appendix(inject_preface(canonical_tex, preface_tex), appendix_tex)
    anonymous_tex = build_variant(shared_tex, author_info, acknowledgments_tex, named=False)
    named_tex = build_variant(shared_tex, author_info, acknowledgments_tex, named=True)

    write_output_bundle(OUTPUT_ANON_DIR, anonymous_tex)
    write_output_bundle(OUTPUT_NAMED_DIR, named_tex)


if __name__ == "__main__":
    main()
