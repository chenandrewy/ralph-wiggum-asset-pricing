#!/usr/bin/env python3
"""
How to run: python tests/quality-ext-messaging.py
Inputs: paper/paper.tex
Outputs: test-results/quality-ext-messaging.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

import re
from pathlib import Path

from _test_helpers import build_test_context, fail_test, require_paths, run_test

AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"

SUBSECTION_RE = re.compile(r"\\subsection\{(.+?)\}")


def _is_comment(line: str) -> bool:
    """True if the line is a LaTeX comment (first non-space char is %)."""
    return line.lstrip().startswith("%")


def parse_extensions_subsections(tex_path: Path) -> list[tuple[str, int, int]]:
    """Parse the Extensions section into its intro paragraph and subsections.

    Returns list of (name, start_line, end_line).  Skips commented-out lines
    when detecting structure so that old headings left in comments do not
    create phantom parts.
    """
    lines = tex_path.read_text(encoding="utf-8").splitlines()

    # Find \section{Extensions}
    ext_start = None
    for i, line in enumerate(lines, 1):
        if not _is_comment(line) and r"\section{Extensions}" in line:
            ext_start = i
            break
    if ext_start is None:
        return []

    # Find the next \section after Extensions (or end of content).
    ext_end = len(lines)
    for i, line in enumerate(lines[ext_start:], ext_start + 1):
        if _is_comment(line):
            continue
        stripped = line.strip()
        if stripped.startswith(r"\section{") and "Extensions" not in stripped:
            ext_end = i - 1
            break
        if stripped.startswith(r"\printbibliography") or stripped.startswith(r"\end{document}"):
            ext_end = i - 1
            break

    # Find subsections within the Extensions section.
    subsections: list[tuple[str, int]] = []
    for i, line in enumerate(lines[ext_start - 1 : ext_end], ext_start):
        if _is_comment(line):
            continue
        m = SUBSECTION_RE.search(line)
        if m:
            subsections.append((m.group(1), i))

    # Build ranges: intro paragraph, then each subsection.
    result = []
    if subsections:
        result.append(("Extensions introduction", ext_start, subsections[0][1] - 1))
        for idx, (name, start) in enumerate(subsections):
            end = subsections[idx + 1][1] - 1 if idx + 1 < len(subsections) else ext_end
            result.append((name, start, end))
    else:
        result.append(("Extensions (full)", ext_start, ext_end))

    return result


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    preflight = require_paths(context, paper_path)
    if preflight is not None:
        return preflight

    subsections = parse_extensions_subsections(paper_path)
    if not subsections:
        return fail_test(context, "no Extensions section found in paper.tex")

    subsection_list = "\n".join(
        f"  - {name}: lines {start}–{end}" for name, start, end in subsections
    )

    prompt = f"""
You are evaluating the extensions section of an academic asset pricing paper for economic messaging clarity.

## Input
- Paper: {paper_path}

The extensions section has these parts:
{subsection_list}

## Procedure
1. Spawn one subagent per part listed above. Run all subagents in parallel. Each subagent reads `{paper_path}` and evaluates its assigned lines.
2. Each subagent should answer this question about its assigned lines:

   "Evaluate this part of the extensions section for economic messaging. We want these messages to be crystal clear. No reader should have to double-check the text to see what the idea was. All readers should know from the introductory paragraph what the main messages are. Does this part make the economic message(s) clear? Yes or no?"

   The subagent should:
   - State what it believes the economic message(s) of the part are.
   - Evaluate whether those messages are explicitly and clearly stated in the text, or whether the reader must infer them.
   - Return YES or NO with a short explanation.

3. After all subagents complete, review their outputs.
4. Write the combined report. PASS only if every part gets YES. FAIL if any part gets NO.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then, for each part:

## [Part Name] (lines N–M)
- **Subagent verdict:** YES or NO
- **Economic message(s) identified:** ...
- **Assessment:** ...
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
