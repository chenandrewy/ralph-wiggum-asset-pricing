#!/usr/bin/env python3
"""
How to run: python tests/factcheck-theory.py
Inputs: paper/paper.tex, spec/paper-spec.md, spec/economic-background.md
Outputs: test-results/factcheck-theory.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    bg_path = context.repo_root / "spec/economic-background.md"
    preflight = require_paths(context, paper_path, spec_path, bg_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent evaluating the formal theory in an academic asset pricing paper.

Read the paper at: {paper_path}
Read the spec at: {spec_path}
Read the economic background at: {bg_path}

You MUST use a staged subagent workflow for the first two conditions:

- Subagent 1 handles Condition 1:
  enumerate every mathematical object in the paper, group objects that refer to the same economic concept, and produce a normalized symbol map with locations in the paper and ambiguity notes.
- Subagent 2 handles Condition 2:
  take Subagent 1's symbol map as an input artifact, enumerate all mathematical assumptions in the paper, map each assumption to the objects it references, and identify any cross-assumption conflicts or unresolved ambiguities.

The main agent must:
- review both subagent outputs
- use them when evaluating Condition 3
- resolve disagreements conservatively
- own the final PASS/FAIL verdict

Do not delegate the final verdict. Do not skip any step because a subagent seems uncertain. If a subagent output is incomplete, say so and treat that as evidence against PASS where appropriate.

This is a math-only test. Do NOT evaluate abstract/introduction rhetoric, broad narrative framing, contribution claims, or verbal interpretation except where a statement is needed to identify a formal object, assumption, or claimed formal result.

Evaluate the formal theory. Check that ALL of the following conditions are met:

1. **Notational Consistency.** Follow this process step by step:
   a. List every mathematical object in the paper. Group objects that refer to the same economic concept (e.g., consumption, dividends, utility).
   b. For each group, check whether the notation is consistent. If the notation is inconsistent, FAIL.

2. **Consistent Assumptions.** Follow this process step by step:
   a. List **all** mathematical assumptions in the paper. Scan every section for assumptions.
   b. List all mathematical objects in the assumptions. For each object, list all assumptions that contain the object. Make sure all of these assumptions are consistent with each other.
   c. If there is any set of assumptions that cannot be simultaneously true, FAIL.

3. **Logical Results.** Follow this process step by step:
   a. List all other mathematical objects not identified in step 2.
   b. Trace each object back to the assumptions.
   c. If any expression cannot be logically derived from the assumptions, FAIL.

Criteria:
- To PASS, ALL three conditions must be satisfied. If ANY condition fails, FAIL.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings, organized by condition.
- Explicitly include:
  - a short "Subagent 1 output summary"
  - a short "Subagent 2 output summary"
  - any important ambiguity passed from Step 1 to Step 2
"""

    return run_test(
        context=context,
        prompt=prompt,
        agent=AGENT,
        model=MODEL,
        default_agent_log_mode="verbose",
    )


if __name__ == "__main__":
    raise SystemExit(main())
