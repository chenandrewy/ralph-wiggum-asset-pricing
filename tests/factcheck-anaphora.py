#!/usr/bin/env python3
"""
How to run: python tests/factcheck-anaphora.py
Inputs: paper/paper.tex
Outputs: test-results/factcheck-anaphora.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

import re
from pathlib import Path

from _test_helpers import build_test_context, fail_test, require_paths, run_test


AGENT = "claude"
MODEL = "opus"

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

    preflight = require_paths(context, paper_path)
    if preflight is not None:
        return preflight

    sections = parse_sections(paper_path)
    if not sections:
        return fail_test(context, "no \\section{} headers found in paper.tex")

    section_list = "\n".join(
        f"  - {name}: lines {start}–{end}" for name, start, end in sections
    )

    prompt = f"""
You are a strict test agent checking an academic asset pricing paper for anaphora resolution errors.

## Input

Paper: {paper_path}

The paper has these sections:
{section_list}

## Procedure

Spawn one subagent per section. Each subagent checks its assigned lines. Run all subagents in parallel.

Each subagent should check for anaphora resolution problems in its assigned lines: any place where a demonstrative ("this", "that", "these", "such") near a cross-reference (\\ref, \\eqref) could resolve to a different meaning than what the referenced target actually contains. Look for cases where the prose and the target describe different mechanisms despite sharing vocabulary.

After all subagents complete, review their outputs and write the combined report. Take the subagents' findings as given; do not re-evaluate their judgements.

## Requirements

- Every demonstrative near a cross-reference resolves to a meaning that matches what the target actually contains.

Write your report to: {context.report_path}

The report must be a clean, human-readable markdown file:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then your findings.
"""

    return run_test(
        context=context,
        prompt=prompt,
        agent=AGENT,
        model=MODEL,
        default_agent_log_mode="verbose",
    )


if __name__ == "__main__":
    raise SystemExit(main())
