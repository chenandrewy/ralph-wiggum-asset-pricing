#!/usr/bin/env python3
"""
How to run: python dev/qf/qf-subparts.py
Inputs: paper/paper.tex
Outputs: dev/qf-results/qf-subparts.md and process exit code (0=PASS, 1=FAIL)
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
You are a skeptical test agent focused on over-formalized subparts of results.

Read the paper at: {paper_path}

## Procedure
1. Read the full paper.
2. Focus on theorem subparts, displayed sufficient conditions, and named examples inside larger sections that may hide inside otherwise useful objects.
3. For each strong candidate, ask:
   - does this subpart do distinct economic work?
   - or is it just extra algebraic precision around a point the paper could state informally?
4. Identify the strongest few cases.
5. Write the report.

## Definitions
1. A useful larger object can still contain compressible or dead-weight subparts.
2. A subpart is compressible if the paper uses only its qualitative takeaway.
3. A subpart is dead weight if the paper never uses it beyond its own local statement or proof.

## Guidelines
1. Be adversarial. Do not let a useful proposition shield an unnecessary clause.
2. Prefer the strongest examples over broad summaries.
3. Standard primitives are not the target of this test.

## Requirements
1. The paper contains no clear dead-weight formal subparts.
2. The paper contains no compressible formal subparts.
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
