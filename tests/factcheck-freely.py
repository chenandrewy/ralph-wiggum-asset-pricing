#!/usr/bin/env python3
"""
How to run: python tests/factcheck-freely.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/factcheck-freely.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test

AGENT = "claude"
MODEL = "claude-opus-4-6"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""

## Procedure

1. Launch a Claude Opus subagent with the following prompt: "Review the paper. Look for flaws."
2. Review the subagent's output and judge whether the requirements are met.

## Requirements
1. There are no factually incorrect statements in the paper.
2. There are no logical inconsistencies in the paper.

PASS only if all requirements are met. Otherwise FAIL.

## Output
Write your report to: {context.report_path}
Use this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence summarizing the overall finding
- Then explain in more detail.
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
