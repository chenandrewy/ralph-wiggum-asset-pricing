#!/usr/bin/env python3
"""
How to run: python tests/theory-correctness.py
Inputs: paper/paper.tex, spec/paper-spec.md, spec/asset-pricing-background.md
Outputs: test-results/theory-correctness.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, load_agent_model, require_paths, run_test


def main() -> int:
    context = build_test_context(__file__)
    AGENT, MODEL = load_agent_model()

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    bg_path = context.repo_root / "spec/asset-pricing-background.md"
    preflight = require_paths(context, paper_path, spec_path, bg_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent evaluating the economic theory in an academic asset pricing paper.

Read the paper at: {paper_path}
Read the spec at: {spec_path}
Read the asset pricing background at: {bg_path}

Evaluate the economic theory. Check that ALL of the following conditions are met:

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

4. **Interpretations.** Follow this process step by step:
   a. For each paragraph, identify the key verbal economic claims. Make a list of all claims.
      - Key claims are related to the economic theory proposed in the paper. Exclude claims used for motivation.
   b. For each claim, check whether the claim is supported by the formal theory. If not, FAIL.

Criteria:
- To PASS, ALL four conditions must be satisfied. If ANY condition fails, FAIL.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings, organized by condition.
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
