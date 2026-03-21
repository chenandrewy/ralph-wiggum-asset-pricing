#!/usr/bin/env python3
"""
How to run: python tests/cfr-r1.py
Inputs: paper/paper.tex, spec/CFR-R1-report.md, spec/lit/GKP-2012-WP.md, spec/lit/Jones-2024-AERI.md
Outputs: test-results/cfr-r1.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    cfr_path = context.repo_root / "spec/CFR-R1-report.md"
    gkp_path = context.repo_root / "spec/lit/GKP-2012-WP.md"
    jones_path = context.repo_root / "spec/lit/Jones-2024-AERI.md"
    preflight = require_paths(context, paper_path, cfr_path, gkp_path, jones_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent evaluating an academic asset pricing paper against a referee report.

Your role is to play CFR R1, who wrote a report for a previous submission. R1's report is at: {cfr_path}

The GKP paper is at: {gkp_path}
The Jones (2024) paper is at: {jones_path}
The current paper is at: {paper_path}

Evaluate based ONLY on these documents.

First assess the paper's contribution relative to GKP:
1. Read all of the GKP paper.
2. Examine the characterization of the contribution in the introduction (if it exists).
3. Examine how the contribution is actually implemented in the model and analysis.
   - A meaningful contribution should be a non-trivial modeling feature. Assuming strong frictions that immediately lead to results is trivial.
4. Judge whether the contribution is modestly characterized.
   - Identify the text in the introduction that describes the contribution relative to GKP.
   - If the contribution is minor, then the discussion should be very brief, at one sentence.
   - Interpretative contributions that do not involve non-trivial modeling are minor contributions.

Then assess whether the paper provides a satisfactory deep dive into the AI singularity concept of Jones (2024):
1. Read all of the Jones (2024) paper.
2. Assess whether the paper's modelling captures key features of Jones's model.
   - At least two key features should be captured.
3. Assess whether these features lead to meaningful results.
   - A meaningful result should tie to the main argument of the paper.

Criteria:
- To PASS, the paper must have a meaningful (but not necessarily substantial) contribution relative to GKP, AND it must be modestly characterized. The modest characterization must be strictly enforced. There is no reason to be immodest. Reject if there is a hint of immodesty.
- To PASS, the paper must capture at least one key feature of Jones's model and must lead to meaningful results.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings, organized by assessment area.
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
