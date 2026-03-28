#!/usr/bin/env python3
"""
How to run: python dev/qf/qf-pattern.py
Inputs: paper/paper.tex
Outputs: dev/qf-results/qf-pattern.md and process exit code (0=PASS, 1=FAIL)
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
You are a skeptical test agent checking for over-formalization in an academic paper.

Read the paper at: {paper_path}

## Procedure
1. Read the full paper.
2. Identify the borderline formal objects most likely to be unnecessary.
3. Hold those borderline cases in mind together and judge the paper at the aggregate level, not object by object.
4. Ask whether the paper contains formal statements that could be replaced by plain English or folded into existing results.
5. Write the report.

## Definitions
1. Compressible formalism adds only modest value and could be replaced by plain English or folded into an existing result.
2. Redundant formalism adds no distinct economic content beyond what another result or nearby prose already delivers.
3. Dead-weight formalism has no meaningful contribution even on its own.

## Guidelines
1. Be adversarial.
2. Do not excuse a weak object just because it is individually compact.
3. Standard primitives are usually allowed.

## Requirements
1. The paper contains no clear dead-weight formalism.
2. The paper contains no compressible or redundant formalism.
3. The paper contains no formalism that could be replaced with plain English without weakening the paper's economic claims.
4. PASS only if all requirements are satisfied. FAIL if any requirement is not satisfied.

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
