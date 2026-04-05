#!/usr/bin/env python3
"""
How to run: python tests/theory-clarity.py
Inputs: paper/paper.tex
Outputs: test-results/theory-clarity.md and process exit code (0=PASS, 1=FAIL)
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
You are evaluating the clarity of model descriptions in `paper/paper.tex`.

## Procedure
1. Read `paper/paper.tex`.
2. Identify every section that contains model definitions (e.g., the main model section, each extension subsection).
3. For each model section, launch a subagent IN PARALLEL with the following prompt (filling in the section name):

   Read the [section name] of `paper/paper.tex`. Evaluate the clarity of the model descriptions.

   Evaluate the following questions as PASS/FAIL:
   1. Are model assumptions presented in distinct model-setup blocks?
   2. Are critical equations presented in display math, and in the main text?
   3. Are critical assumptions stated at the start of a paragraph?

4. Read all subagent reports.
5. PASS only if every section passes all three questions. FAIL if any section fails any question.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then per-section findings from each subagent.
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
