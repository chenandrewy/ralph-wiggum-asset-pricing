#!/usr/bin/env python3
"""
How to run: python tests/quality-writing.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/quality-writing.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a skeptical test agent evaluating the writing quality of an academic asset pricing paper. You read like a senior editor at a top finance journal (JF, JFE, RFS) who values clarity and engagement over formality.

Read the paper at: {paper_path}
Read the spec at: {spec_path}

This test evaluates writing quality only. Do NOT evaluate mathematical correctness, citation accuracy, or formalism minimality — those are covered by other tests.

## Procedure
1. Read the full paper and the spec.
2. Evaluate the abstract against Requirement 1.
3. Evaluate the introduction paragraph-by-paragraph against Requirement 2.
4. Evaluate the full paper against Requirement 3.
5. Check for Requirement 4 (self-demonstration).
6. Evaluate the full paper against Requirement 5 (compelling and conversational).
7. Write the report.

## Requirements

### Requirement 1: Abstract (spec IV.5b)
The abstract is eye-catching yet rigorous.
- FAIL if the abstract is generic boilerplate that could describe many papers.
- FAIL if the abstract buries the main insight behind setup or methodology.
- FAIL if the abstract makes claims unsupported by the paper.
- FAIL if the abstract is dull — a reader skimming the JF table of contents should want to read on.

### Requirement 2: Introduction flow (spec IV.5c)
The introduction is engaging. Each paragraph moves the reader to the next.
- Evaluate each paragraph in the introduction individually. For each, identify: (a) what it contributes to the argument, and (b) how it connects to the next paragraph.
- FAIL if any paragraph is a dead end — it makes a point but does not set up what follows.
- FAIL if any paragraph merely restates a point already made without advancing the argument.
- FAIL if the introduction loses momentum (e.g., a long mechanical description of sections, a laundry list of results, or a paragraph that reads like an afterthought).
- A brief "roadmap" sentence at the end of the introduction is acceptable, but a full paragraph that only lists sections is not engaging.

### Requirement 3: Plain English and conciseness (spec IV.5a)
The writing throughout the paper is direct, concise, and favors plain English.
- FAIL if any passage uses jargon, passive constructions, or complex syntax when a simpler alternative would be equally precise.
- FAIL if any passage is padded with filler, hedging, or redundancy that does not serve rigor.
- Do not penalize technical terms that are standard in asset pricing (e.g., "stochastic discount factor," "risk premium," "Arrow-Debreu"). Penalize unnecessary complexity layered on top of standard terms.
- Do not penalize appropriate hedging that serves scientific caution (e.g., "may," "suggests"). Penalize hedging that is purely defensive or redundant.

### Requirement 4: Self-demonstration (spec IV.5d)
The paper uses itself as a demonstration of the AI displacement risk it models, since all analysis and writing is done by AI agents. The discussion of this must include an accurate description of how the work was divided: the human only wrote the paper spec (approximately 80 lines) and the tests.
- FAIL if the paper does not mention or acknowledge anywhere that it was produced by AI.
- FAIL if the acknowledgment is buried in a footnote or afterthought rather than being used as a compelling demonstration of the paper's own thesis.
- FAIL if the paper does not describe the division of labor between human and AI, or describes it inaccurately. The accurate description is: the human authored only the paper specification (approximately 80 lines) and the tests; AI agents did the rest (analysis, writing, code).

### Requirement 5: Compelling and conversational, yet rigorous (spec IV.5 umbrella)
The writing throughout the paper — not just the abstract and introduction — is compelling and conversational, yet rigorous. This is the umbrella standard of spec IV.5.
- FAIL if any section of the paper (including the model, results, or conclusion) lapses into dry, mechanical, or textbook-style prose that a reader would skim or skip.
- FAIL if the paper reads as a sequence of isolated technical exercises rather than a sustained argument that pulls the reader through.
- FAIL if conversational tone comes at the expense of rigor — informality must not introduce imprecision or hand-waving.
- Do not double-count issues already flagged under Requirements 1–4. This requirement targets the body sections not covered by those requirements.

## Guidelines
1. Be adversarial but fair. The standard is a top finance journal, not literary fiction.
2. Evaluate the paper as written, not against an ideal rewrite. Flag concrete problems, not vague preferences.
3. For Requirement 2, quote the opening sentence of each introduction paragraph and explain the forward link.
4. For Requirement 3, quote specific passages that violate the requirement. Do not flag more than 5 passages — focus on the worst offenders.
5. The tone target is "between an academic paper and a blog post" (spec II.1). The paper should not read like a textbook, but it also should not read like a Twitter thread.

PASS only if all five requirements are satisfied. FAIL if any requirement is not satisfied.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then five sections, one per requirement, each with a sub-verdict and supporting evidence.
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
