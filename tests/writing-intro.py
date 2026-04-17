#!/usr/bin/env python3
"""
How to run: python tests/writing-intro.py
Inputs: spec/paper-spec.md, paper/paper.tex
Outputs: test-results/writing-intro.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test

AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    preflight = require_paths(
        context,
        context.repo_root / "spec/paper-spec.md",
        context.repo_root / "paper/paper.tex",
    )
    if preflight is not None:
        return preflight

    prompt = f"""
Use parallel subagents to answer the following questions about `paper/paper.tex`:

1. Are the main arguments from `spec/paper-spec.md` clear, even to a reader who is just skimming the Introduction?
2. Does the introduction flow well?
3. Are all promised or implied analyses in Introduction actually fulfilled in the analysis sections? 

For questions 1 and 2, pass the subagent *only* the Introduction text. For question 3, pass the full test.

All subagents should evaluate as PASS/FALL.

Assemble their feedback. PASS the paper if all subagents PASS.

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
