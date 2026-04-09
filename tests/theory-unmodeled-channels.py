#!/usr/bin/env python3
"""
How to run: python tests/theory-unmodeled-channels.py
Inputs: paper/paper.tex
Outputs: test-results/theory-unmodeled-channels.md and process exit code (0=PASS, 1=FAIL)
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
## Econ Theory Background

No economic model can capture everything. There are often important economic channels that are not
explicitly captured. But if a channel is missing, the paper should be cautious in how it discusses the
channel.

## Task
Read `paper/paper.tex`. List the economic channels it discusses, and assess whether the channels are
explicitly modeled. Then examine how the modeling is discussed.

Assess: Is the paper consistently cautious about channels that it does not explicitly capture? Yes or
No.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Further details on your findings
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
