#!/usr/bin/env python3
"""
How to run: python tests/writing-intuition.py
Inputs: paper/paper.tex
Outputs: test-results/writing-intuition.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test

AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    preflight = require_paths(context, context.repo_root / "paper/paper.tex")
    if preflight is not None:
        return preflight

    prompt = f"""
Read `paper/paper.tex`. Examine how the paper discusses the propositions and key formulas. Do all of these discussions explain the intuition in terms of the mathematical objects used in the respective propositions and formulas? Yes or no?

If yes, PASS. If no, FAIL.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then describe your findings in detail.
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
