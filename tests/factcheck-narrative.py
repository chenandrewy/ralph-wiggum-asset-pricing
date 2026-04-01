#!/usr/bin/env python3
"""
How to run: python tests/factcheck-narrative.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/factcheck-narrative.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test

AGENT = "claude"
MODEL = "claude-opus-4-6"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent reviewing an academic asset pricing paper for the correctness of its verbal narrative.

Read the paper at: {paper_path}
Read the spec at: {spec_path}

This is a narrative-only test. Do NOT evaluate mathematical derivations, notational consistency, or formal correctness---those are covered by other tests. Focus on whether each section's verbal claims are internally fulfilled and mutually consistent.

## Procedure
1. Read the full paper.
2. For each section and subsection, extract:
   a. The **contract**: what does the title, opening sentence, or framing promise this section will deliver? (e.g., "calibrate X," "derive Y," "show Z")
   b. The **deliverables**: what does the section actually contain? (e.g., an equation linking X to model parameters, a qualitative paragraph, a numerical result)
3. For each section, check:
   a. **Fulfillment**: Does the section deliver what its contract promises? A section titled "The value of X" that only states an empirical fact without connecting it to the model has an unfulfilled contract. A section that claims to "calibrate" must produce a mapping from data to model parameters, not merely cite a number.
   b. **Internal references**: When the section says "as shown in Section Y" or "using the calibration from Section Y," does Section Y actually contain the referenced content?
   c. **Claim strength**: Are verbal claims (e.g., "this implies," "it follows," "we show") supported by the results actually present in the paper? Flag claims that are stronger than the evidence.
4. Across the full paper, check:
   a. **Narrative consistency**: Do sections tell a coherent story, or do later sections rely on deliverables that earlier sections promised but did not provide?
   b. **Abstract/Introduction alignment**: Are the central claims in the Abstract and Introduction supported by what the body sections actually deliver?

## Requirements
1. Every section fulfills the contract implied by its title and opening framing.
2. Every internal cross-reference points to content that actually exists in the referenced section.
3. No verbal claim is stronger than the evidence the paper provides.
4. The Abstract and Introduction claims are supported by the body.

## Guidelines
1. Be strict about fulfillment. A section that promises a calibration must contain a calibration, not just cite an empirical number. A section that promises to "derive" something must contain a derivation, not just state a result.
2. Do not penalize a section for being short or qualitative---penalize it only if it promises more than it delivers.
3. Do not evaluate whether the paper's arguments are *persuasive* or *novel*---only whether the paper delivers what it says it will.
4. Do not evaluate mathematical correctness. Focus on the verbal layer.
5. A paragraph that is internally coherent but disconnected from what the section title promises is a failure, not a pass.

## Output
Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then, for each section/subsection:
  - **Contract**: what it promises
  - **Deliverables**: what it contains
  - **Status**: FULFILLED or UNFULFILLED, with explanation
- Then a summary of cross-reference and claim-strength findings.
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
