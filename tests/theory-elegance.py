#!/usr/bin/env python3
"""
How to run: python tests/theory-elegance.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/theory-elegance.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, load_agent_model, require_paths, run_test


def main() -> int:
    context = build_test_context(__file__)
    AGENT, MODEL = load_agent_model()

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent evaluating whether an academic asset pricing theory paper's model is elegant and concise.

Read the paper at: {paper_path}
Read the spec at: {spec_path}

The spec requires: "Keep mathematical notation to a minimum. The goal is to make the main argument elegantly."
The spec also requires: "Remove text and math that do not add value."

Evaluate the economic theory. Check that ALL of the following conditions are met:

1. **Conciseness.** Follow this process step by step:
   a. List every numbered equation and every named mathematical object (variables, parameters, functions) introduced in the paper.
   b. For each equation, trace it forward: which later equation or result depends on it? If an equation is never used in a derivation, proposition, calibration, or interpretation, flag it as unnecessary.
   c. For each parameter or variable, check whether it appears in at least one result that matters for the paper's conclusions. If it does not, flag it as unnecessary.
   d. Check whether any result could be stated with fewer mathematical objects. Flag redundant notation (e.g., two symbols for the same concept, intermediate expressions that could be skipped).

Criteria:
- To PASS, there must be no unnecessary equations, no unnecessary parameters, and no redundant notation. The model must be as simple as possible for the argument being made.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings.
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
