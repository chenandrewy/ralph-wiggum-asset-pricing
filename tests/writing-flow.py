#!/usr/bin/env python3
"""
How to run: python tests/writing-flow.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/writing-flow.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    preflight = require_paths(context, paper_path)
    if preflight is not None:
        return preflight

    prompt = f"""
Evaluate the flow of the writing in {paper_path}. Be critical. Help make the paper really compelling. Evaluate the following requirements as PASS/FAIL.

## Requirements

1. Does every paragraph convince the reader to move to the next paragraph?
2. Are all paragraphs logically connected?
3. Are the dynamics and rhythm of the writing utilized effectively?
4. Is the tone conversational and inviting?

PASS only if all requirements are met.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Describe your findings in detail.
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
