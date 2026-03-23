#!/usr/bin/env python3
"""
How to run: python tests/factcheck-interpretation.py
Inputs: paper/paper.tex, spec/paper-spec.md, spec/asset-pricing-background.md, code/*, data/*
Outputs: test-results/factcheck-interpretation.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    bg_path = context.repo_root / "spec/asset-pricing-background.md"
    code_dir = context.repo_root / "code"
    data_dir = context.repo_root / "data"
    preflight = require_paths(context, paper_path, spec_path, bg_path, code_dir, data_dir)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent reviewing the interpretation and verbal claims of an academic asset pricing paper.

Read the paper at: {paper_path}
Read the paper spec at: {spec_path}
Read the asset pricing background at: {bg_path}
Inspect supporting local materials under: {code_dir} and {data_dir}

This is an interpretation-only test. Do NOT perform a full derivation audit, notation audit, or assumption-consistency audit except insofar as an obvious formal flaw makes a verbal claim unsupported.

Procedure:
1. Extract the paper's central verbal claims, starting with the abstract and introduction, then the conclusion and theory-discussion sections.
2. For each claim, identify the exact evidence the paper uses to support it, such as propositions, comparative statics, calibrations, quantitative objects, code outputs, or exhibits.
3. Classify each claim as directly supported, partially supported, unsupported, or contradicted.
4. Flag claims that are stronger, broader, more general, or more causal than the paper's own evidence justifies.
5. Distinguish clearly between:
   - claims that are unsupported because the underlying theory/evidence is currently missing or broken
   - claims that remain overstated even if the underlying theory were taken at face value

Criteria:
- PASS only if the paper's central verbal claims are supported by the paper's own theory and supporting materials, and are stated at an appropriate level of strength.
- FAIL if any major claim is unsupported, contradicted, or materially overstated.

Guidelines:
- Focus on interpretation, scope, and evidentiary proportionality, not copyediting.
- Use the paper's own definitions and the asset pricing background when interpreting terms.
- Be strict about whether the abstract, introduction, conclusion, and theory discussion match the actual support the paper provides.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings, organized by claim.
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
