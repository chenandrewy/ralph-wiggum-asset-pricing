#!/usr/bin/env python3
"""
How to run: python tests/quality-gkp-cites.py
Inputs: paper/paper.tex, spec/paper-spec.md, spec/lit/GKP-2012-WP.md
Outputs: test-results/quality-gkp-cites.md and process exit code (0=PASS, 1=FAIL)
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
    gkp_wp_path = context.repo_root / "spec/lit/GKP-2012-WP.md"
    preflight = require_paths(context, paper_path, spec_path, gkp_wp_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a skeptical test agent evaluating whether an academic asset pricing paper cites GKP (Garleanu, Kogan & Panageas 2012) in a way that is sensitive, cautious, and modest.

Read these files:
- Paper: {paper_path}
- Paper spec: {spec_path}
- GKP working paper: {gkp_wp_path}

## Context

The paper builds directly on GKP's displacement risk framework. The paper spec (Quality Requirement 7) states: "The paper is sensitive, cautious, and modest in how it cites GKP." The spec also defines the intended contribution relative to GKP in section I.6.

"Sensitive" means two things: (a) do not diminish GKP's contribution — give them full credit for what they did, and (b) be respectful and collegial in tone, as these are prominent living researchers who may read the paper.

"Cautious" means: do not overstate what GKP say; do not put words in their mouth; do not attribute interpretations to GKP that are actually the paper's own.

"Modest" means: acknowledge that the core displacement-risk insight is GKP's; do not oversell the paper's contribution relative to GKP.

## Procedure
1. Read the full paper, the paper spec (especially sections I.6 and IV.7), and the GKP working paper.
2. Identify every passage in the paper that references GKP — by citation, by name, or by clear allusion to their model.
3. For each passage, evaluate against the requirements below by comparing what the paper says with what GKP actually wrote.
4. Pay special attention to: (a) how the paper characterizes GKP's discussion of intergenerational transfers, bequests, gifts, and government debt; (b) whether interpretations from other papers are attributed to GKP or correctly to the paper's own analysis; (c) how the paper characterizes the analogy between AI owners and GKP's unborn cohorts; (d) whether the paper's description of its own contribution is consistent with the modesty called for in the spec.
5. Write the report.

## Judgment standard

Evaluate from the perspective of a skeptical referee who has read GKP carefully and is already worried about overlap. If you identify a passage that is materially loose, minimizing, or stronger than the GKP source text, it fails. Do not excuse issues as "minor imprecision," "fair paraphrase," or "generous reading" unless you explain why a skeptical referee would not object. The paper's self-protective language elsewhere (e.g., "builds directly on," "we deliberately keep our characterization modest") does not compensate for loose passages — evaluate each passage on its own merits.

## Requirements
1. The paper accurately represents GKP's ideas. It does not put words in GKP's mouth, attribute the paper's own interpretations to GKP, or claim exact equivalence when the connection to GKP is an analogy. Specific fail conditions:
   - FAIL if the paper characterizes GKP's mechanism as mere inability to buy private AI capital without making clear that GKP's key mechanism is failure of intergenerational risk sharing because unborn cohorts cannot trade.
   - FAIL if the paper says GKP "raise in a footnote" or "note in passing" a point, unless the report confirms this wording is textually precise and not minimizing.
   - FAIL if the paper presents AI owners and GKP's future cohorts as exact counterparts rather than an analogy.
2. When the paper connects GKP's ideas to concepts from other papers, those connections are clearly attributed to the paper's own interpretation rather than to GKP.
3. The paper characterizes GKP's contribution graciously and the overall tone toward GKP is respectful and collegial. It treats its own contribution as merely building on GKP's core insights.
4. No passage mentioning GKP is awkward, defensive, or over-explaining. If the paper preemptively denies a criticism no one has made, or hedges a modeling choice with unprompted reassurances about the relationship to GKP, that passage fails.

PASS only if all requirements are met. Otherwise, FAIL.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then list every passage in the paper that mentions GKP (by citation, name, or paragraph title). For each passage, quote it, give the line number, characterize what it does (e.g., credits GKP, draws an analogy, describes a difference, claims contribution), and note whether it passes or fails any requirement.
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
