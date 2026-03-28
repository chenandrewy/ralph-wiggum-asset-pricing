#!/usr/bin/env python3
"""
How to run: python tests/factcheck-bysection.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/factcheck-bysection.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

import re
from pathlib import Path

from _test_helpers import build_test_context, fail_test, require_paths, run_test


AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"

SECTION_RE = re.compile(r"\\section\{(.+?)\}")


def parse_sections(tex_path: Path) -> list[tuple[str, int, int]]:
    """Parse \\section boundaries from paper.tex.

    Returns list of (name, start_line, end_line).
    """
    lines = tex_path.read_text(encoding="utf-8").splitlines()
    headers: list[tuple[str, int]] = []
    for i, line in enumerate(lines, 1):
        m = SECTION_RE.search(line)
        if m:
            headers.append((m.group(1), i))

    # Find the end of content (before \printbibliography or \end{document}).
    last_line = len(lines)
    for i, line in enumerate(lines, 1):
        if line.strip().startswith(r"\printbibliography") or line.strip().startswith(r"\end{document}"):
            last_line = i - 1
            break

    sections = []
    for idx, (name, start) in enumerate(headers):
        end = headers[idx + 1][1] - 1 if idx + 1 < len(headers) else last_line
        sections.append((name, start, end))
    return sections


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"

    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    sections = parse_sections(paper_path)
    if not sections:
        return fail_test(context, "no \\section{} headers found in paper.tex")

    section_list = "\n".join(
        f"  - {name}: lines {start}–{end}" for name, start, end in sections
    )

    prompt = f"""
You are a strict fact-checking agent. Your job is to check every line of an academic asset pricing paper for accuracy, section by section.

## Inputs

- Full paper: {paper_path}
- Paper spec: {spec_path}

The paper has these sections:
{section_list}

## Workflow

Spawn one subagent per section. Each subagent checks its assigned lines. Run all subagents in parallel.

Each subagent should follow this procedure for its assigned line range:

Go through the assigned lines line by line. Extract every distinct claim. A single sentence often contains multiple claims — extract and check each one separately.

Claim types:
- DEFINITION: introduces notation or a concept
- ASSUMPTION: states a parameter value or modeling choice
- ARITHMETIC: a number derived from parameters or formulas
- VERBAL: a qualitative statement about results
- REFERENCE: cites another paper or section for a specific fact
- FIGURE/TABLE: asserts something about the content of an exhibit

How to verify each type:
- ARITHMETIC: recompute using the formulas in the paper and the stated parameters.
- VERBAL: check whether the tables, figures, and formulas actually support the claim at the stated strength.
- ASSUMPTION: check whether the stated values match what the tables actually use.
- REFERENCE: read the referenced section and confirm it actually contains the claimed content.
- FIGURE/TABLE: read the underlying file (e.g. PDF/PNG in paper/figures/) to verify.

Critical rule — no circular verification:
When a claim cites a specific section for a number (e.g. "Section X shows Y = 5.1%"), you must verify two things independently: (1) that the referenced section actually states or derives that number, and (2) that you can reproduce the number from the derivation in that section. Do not verify a number solely by checking that it is consistent with other numbers in the same paragraph.

## After all subagents complete

Review all subagent outputs. Then write the combined report.

Write your report to: {context.report_path}

The report must be a clean, human-readable markdown file:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then, for each section, a line-by-line outline:

## [Section Name] (lines N–M)
- **Line N** — section header
- **Line N** [ARITHMETIC] ERROR — claims X but recomputation gives Y
  - detail of the error
- **Line N** [VERBAL] OK — supported by Table 2
- **Line N** [REFERENCE] ERROR — cites Section X for Y, but Section X does not contain Y
...

## Criteria
- PASS if all arithmetic is correct, all verbal claims are supported, and no claim is materially wrong.
- FAIL if any arithmetic error, unsupported claim, or material inaccuracy is found.
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
