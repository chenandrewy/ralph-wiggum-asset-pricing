#!/usr/bin/env python3
"""
How to run: python tests/quality-deadweight.py
Inputs: paper/paper.tex
Outputs: test-results/quality-deadweight.md and process exit code (0=PASS, 1=FAIL)
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
Audit `paper/paper.tex` for unnecessary formalism. Check every formal object, subpart, and prose mechanism.

- Is any formalism introduced and then abandoned, or does it add no meaningful economic or narrative work? A useful larger object can still contain dead-weight subparts.
- Could any formal object's qualitative takeaway be stated in plain English without weakening the paper's economic claims?
- Are any variables, parameters, or functions introduced and then unused in any result, calibration, or interpretation that matters for the paper's conclusions?
- Is any formalism pompous or ceremonial? Are there auxiliary formal detours that do not advance the main argument?

PASS only if none of the above problems are found. FAIL if any are found.

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
