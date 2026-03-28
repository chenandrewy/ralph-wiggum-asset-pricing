#!/usr/bin/env python3
"""
How to run: python dev/qf/qf-redundancy.py
Inputs: paper/paper.tex
Outputs: dev/qf-results/qf-redundancy.md and process exit code (0=PASS, 1=FAIL)
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
You are a skeptical test agent checking for redundant formalism in an academic paper.

Read the paper at: {paper_path}

## Procedure
1. Read the full paper.
2. Identify formal objects that may duplicate work already done by another result, equation, or nearby prose.
3. For each candidate, state:
   - the economic point it makes,
   - where else that same point is already made,
   - whether the separate formal object is still justified.
4. Focus on the strongest few redundancy candidates.
5. Write the report.

## Definitions
1. Redundant formalism is formalism whose economic content is already delivered elsewhere in the paper.
2. Compressible formalism may add emphasis, but not enough to justify a separate formal statement.
3. Dead-weight formalism has no meaningful independent contribution.

## Guidelines
1. Be adversarial. Surface-level economic relevance is not enough.
2. A result can be redundant even if it is true and discussed later.
3. Standard primitives are usually allowed.

## Requirements
1. The paper contains no clear dead-weight formalism.
2. The paper contains no redundant or compressible formalism.
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
