#!/usr/bin/env python3
"""
How to run: python dev/qf/qf-plain-english.py
Inputs: paper/paper.tex
Outputs: dev/qf-results/qf-plain-english.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _qf_helpers import build_test_context, require_paths, run_test

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
You are a skeptical test agent checking whether the paper over-formalizes points that could be stated in plain English.

Read the paper at: {paper_path}

## Procedure
1. Read the full paper.
2. Identify the formal objects most likely to be replaceable by plain English: theorem subparts, displayed conditions, one-off formulas, and illustrative parametric examples.
3. For each candidate, ask: could the paper make the same economic point just as well in one or two sentences of plain English?
4. Focus on the strongest few examples, not every equation.
5. Write the report.

## Definitions
1. Essential formalism cannot be replaced by plain English without losing a later economic claim, quantitative takeaway, or necessary model setup.
2. Compressible formalism supports a real economic point, but the formal statement is more than the paper needs; plain English would do.
3. Dead-weight formalism is neither needed formally nor needed substantively.

## Guidelines
1. Be adversarial. Do not give credit just because an object sounds economic.
2. Standard primitives are usually allowed.
3. A formal object may be compressible even if it is true and even if it is mentioned later.

## Requirements
1. The paper contains no clear dead-weight formalism.
2. The paper contains no formalism that could be replaced with plain English without weakening the paper's economic claims.
3. PASS only if all requirements are satisfied. FAIL if any requirement is not satisfied.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then explain the main findings briefly.
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
