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
You are a strict but lightweight test agent evaluating minimal formalism in an academic asset pricing paper.

Read the paper at: {paper_path}

This is not a full correctness audit. Scan for clear unnecessary formalism; do not inspect every equation mechanically.

## Procedure
1. Read the full paper.
2. Identify candidate formal objects: displayed equations, propositions/corollaries/remarks, explicit algebraic conditions, and parametric examples with extra notation or parameters.
3. For the most important candidates, assess whether they carry real economic or narrative work later in the paper.
4. Write the report.

## Definitions
1. Formalism counts as essential only if it contributes to an economic claim, interpretation, calibration, table, figure, or necessary model setup.
2. Formalism counts as dead weight if it is introduced and then abandoned, or if it supports only other formal objects that do not themselves carry economic or narrative work.
3. It is not enough that an equation feeds a proposition if that proposition is never used to make an economic point.

## Guidelines
1. Do not flag standard primitives needed to keep the model self-contained, such as preferences, Euler equations, stochastic discount factors, and basic equilibrium definitions.
2. Do not flag an object as dead weight merely because it is used once, if that use matters for a real economic claim or quantitative takeaway.
3. Prefer compressible over dead weight when an object has real economic use but appears more formal than necessary.

## Requirements
1. The paper contains no clear dead-weight formal objects.
2. The paper does not contain a clear repeated pattern of compressible formalism large enough to violate minimal-formalism expectations.

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
