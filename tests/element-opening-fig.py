#!/usr/bin/env python3
"""
How to run: python tests/element-opening-fig.py
Inputs: paper/paper.tex, spec/paper-spec.md, ralph-garage/page-images/page-*.png
Outputs: test-results/element-opening-fig.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

import re

from _test_helpers import (
    build_test_context,
    fail_test,
    require_page_images,
    require_paths,
    run_test,
)


AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def _extract_introduction_block(tex: str) -> str | None:
    intro_match = re.search(r"\\section\{Introduction\}", tex)
    if intro_match is None:
        return None

    rest = tex[intro_match.end():]
    next_section = re.search(r"\n\\section\{", rest)
    if next_section is None:
        return rest
    return rest[:next_section.start()]


def _extract_figure_blocks(tex: str) -> list[str]:
    return re.findall(r"\\begin\{figure\}.*?\\end\{figure\}", tex, flags=re.DOTALL)


def _extract_include_paths(block: str) -> list[str]:
    return re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", block)


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    page_images_dir = context.repo_root / "ralph-garage/page-images"

    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    page_image_check = require_page_images(context, page_images_dir)
    if page_image_check is not None:
        return page_image_check

    paper_tex = paper_path.read_text(encoding="utf-8")
    intro_block = _extract_introduction_block(paper_tex)
    if intro_block is None:
        return fail_test(context, "paper is missing an Introduction section")

    figure_blocks = _extract_figure_blocks(intro_block)
    if not figure_blocks:
        return fail_test(context, "Introduction contains no figure environment")

    intro_figure_paths = []
    for block in figure_blocks:
        include_paths = _extract_include_paths(block)
        exhibit_paths = [path for path in include_paths if path.startswith("exhibits/")]
        if exhibit_paths:
            intro_figure_paths.extend(exhibit_paths)

    if not intro_figure_paths:
        return fail_test(context, "Introduction figure is not sourced from paper/exhibits/")

    figure_block = "\n".join(f"- {path}" for path in intro_figure_paths)

    prompt = f"""
You are a strict element test agent evaluating the paper's opening figure.

Read:
- paper: {paper_path}
- spec: {spec_path}
- rendered page images directory: {page_images_dir}

The Introduction contains the following figure(s) sourced from `paper/exhibits/`:
{figure_block}

Check whether the paper has a strong opening figure.

## Requirements
1. The Introduction figure is empirical, not theoretical.
2. It compares AI and non-AI public-stock valuations.
3. It supports the intro's motivating claim.
4. It is clear and publication-quality.

## Guidelines
1. Be strict. Presence alone is not enough.
2. Fail if the figure is vague, visually weak, or substantively off-target.
3. CRSP is ideal, but not a hard requirement.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then brief findings.
"""

    return run_test(
        context=context,
        prompt=prompt,
        agent=AGENT,
        model=MODEL,
        default_agent_effort=EFFORT,
        default_agent_log_mode="verbose",
    )


if __name__ == "__main__":
    raise SystemExit(main())
