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
You are a skeptical test agent evaluating whether an academic asset pricing paper achieves good theory style and stays intentionally limited in scope.

Read the paper at: {paper_path}

## Procedure
1. Read the full paper.
2. **Theory style audit (Requirement 8a).** This is the most important part. Focus on theorem subparts, displayed sufficient conditions, one-off formulas, and named examples inside larger sections. For each strong candidate, ask:
   - does this subpart do distinct economic work later in the paper?
   - or does the paper use only its qualitative takeaway?
   - could the same point be stated in plain English without weakening the paper's economic claims?
   Also check for orphan notation: named variables, parameters, or functions introduced and then never used in any result, calibration, or interpretation that matters for the paper's conclusions.
3. **Scope audit (Requirements 8b–8d).** Check whether the paper stays compact:
   - *Empirical content (8b):* should be very limited — ideally a single introductory figure using CRSP data. Scrutinize any additional empirical content, but a small justified addition is not an automatic failure.
   - *Testable predictions (8c):* a handful of direct implications of the main model is fine; a laundry list of auxiliary predictions is not.
   - *Quantitative material (8d):* rough numbers for illustration are fine; systematic calibration or estimation is not.
4. Focus on the strongest few cases per category and write the report.

## Definitions (for the theory style audit)
1. Essential formalism contributes to an economic claim, interpretation, calibration, table, figure, or necessary model setup.
2. Compressible formalism supports a real point, but the paper uses only its qualitative takeaway and could state the point in plain English instead.
3. Dead-weight formalism is introduced and then abandoned, or adds no meaningful economic or narrative work.
4. A useful larger object can still contain compressible or dead-weight subparts.

## Guidelines
1. Be adversarial. Do not let a useful proposition shield an unnecessary clause.
2. Do not give credit merely because a point sounds economic; ask whether the formal subpart is actually needed.
3. Standard primitives needed to keep the model self-contained are usually allowed.
4. Local notation is allowed only if it is needed for a later result, calibration, or interpretation that matters for the paper's conclusions.
5. The overall standard is elegance and economy: a compact theoretical contribution, not a comprehensive treatment.

## Requirements
1. **(8a — Theory style)** The paper contains no dead-weight formal objects or formal subparts.
2. **(8a — Theory style)** The paper contains no compressible formal objects or formal subparts that could be replaced with plain English without weakening the paper's economic claims.
3. **(8a — Theory style)** The paper contains no orphan notation: named variables, parameters, or functions introduced and then unused in any result, calibration, or interpretation that matters for the paper's conclusions.
4. **(8a — Theory style)** The paper avoids pompous or ceremonial formalism and avoids auxiliary formal detours that do not advance the main argument.
5. **(8b — Empirical scope)** The empirical content is very limited and serves only to motivate the theory.
6. **(8c — Testable predictions)** The paper does not try to generate a broad menu of novel testable predictions beyond the model's main arguments.
7. **(8d — Quantitative material)** Any quantitative parameterizations remain illustrative rather than becoming a calibration or estimation exercise.
8. PASS only if all requirements are satisfied. FAIL if any requirement is not satisfied.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then for each requirement (8a through 8d), state whether it passes or fails with a brief explanation.
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
