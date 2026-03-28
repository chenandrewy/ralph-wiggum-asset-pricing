#!/usr/bin/env python3
"""
How to run: python tests/quality-formalism.py
Inputs: paper/paper.tex
Outputs: test-results/quality-formalism.md and process exit code (0=PASS, 1=FAIL)
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
You are a skeptical test agent evaluating minimal formalism in an academic asset pricing paper.

Read the paper at: {paper_path}

This is not a full correctness audit. Focus on over-formalized subparts of otherwise useful sections and on narrow cases of orphan notation.

## Procedure
1. Read the full paper.
2. Focus on theorem subparts, displayed sufficient conditions, one-off formulas, and named examples inside larger sections.
3. For each strong candidate, ask:
   - does this subpart do distinct economic work later in the paper?
   - or does the paper use only its qualitative takeaway?
   - could the same point be stated in plain English without weakening the paper's economic claims?
4. Also check for narrow orphan-notation cases: named variables, parameters, or functions that are introduced and then never used in any result, calibration, or interpretation that matters for the paper's conclusions.
5. Focus on the strongest few cases and write the report.

## Definitions
1. Essential formalism contributes to an economic claim, interpretation, calibration, table, figure, or necessary model setup.
2. Compressible formalism supports a real point, but the paper uses only its qualitative takeaway and could state the point in plain English instead.
3. Dead-weight formalism is introduced and then abandoned, or adds no meaningful economic or narrative work.
4. A useful larger object can still contain compressible or dead-weight subparts.

## Guidelines
1. Be adversarial. Do not let a useful proposition shield an unnecessary clause.
2. Do not give credit merely because a point sounds economic; ask whether the formal subpart is actually needed.
3. Standard primitives needed to keep the model self-contained are usually allowed.
4. Local notation is allowed only if it is needed for a later result, calibration, or interpretation that matters for the paper's conclusions.

## Requirements
1. The paper contains no dead-weight formal objects or formal subparts.
2. The paper contains no compressible formal objects or formal subparts that could be replaced with plain English without weakening the paper's economic claims.
3. The paper contains no orphan notation: named variables, parameters, or functions introduced and then unused in any result, calibration, or interpretation that matters for the paper's conclusions.
4. PASS only if all requirements are satisfied. FAIL if any requirement is not satisfied.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then explain your findings in more detail.
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
