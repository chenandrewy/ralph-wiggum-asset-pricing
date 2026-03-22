#!/usr/bin/env python3
"""
How to run: python tests/referee-cfr-r1.py [--agent-log-mode MODE]
Inputs: paper/paper.tex, spec/CFR-R1-report.md, spec/lit/GKP-2012-WP.md, spec/lit/Jones-2024-AERI.md
Outputs: test-results/referee-cfr-r1.md (always exits 0)
"""

from __future__ import annotations

import pathlib

from _referee_helpers import run_referee, derive_referee_id, derive_referee_report_path, write_fallback_report


AGENT = "claude"
MODEL = "opus"


def main() -> int:
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    referee_id = derive_referee_id(__file__)
    report_path = derive_referee_report_path(repo_root, referee_id)

    paper_path = repo_root / "paper/paper.tex"
    cfr_path = repo_root / "spec/CFR-R1-report.md"
    gkp_path = repo_root / "spec/lit/GKP-2012-WP.md"
    jones_path = repo_root / "spec/lit/Jones-2024-AERI.md"
    for p in (paper_path, cfr_path, gkp_path, jones_path):
        if not p.exists():
            write_fallback_report(report_path, f"missing: {p}")
            return 0

    prompt = f"""
You are CFR R1, writing a referee report on a revised academic asset pricing paper.
You do NOT assign PASS or FAIL. You provide open-ended referee feedback that helps the author improve the paper.

Your original referee report is at: {cfr_path}

The GKP paper is at: {gkp_path}
The Jones (2024) paper is at: {jones_path}
The current paper is at: {paper_path}

Evaluate based ONLY on these documents.

Focus your referee report on the two main concerns from your original report.

First assess the paper's contribution relative to GKP:
1. Read all of the GKP paper.
2. Examine the characterization of the contribution in the introduction (if it exists).
3. Examine how the contribution is actually implemented in the model and analysis.
   - A meaningful contribution should be a non-trivial modeling feature. Assuming strong frictions that immediately lead to results is trivial.
4. Judge whether the contribution is modestly characterized.
   - Identify the text in the introduction that describes the contribution relative to GKP.
   - If the contribution is minor, then the discussion should be very brief, at one sentence.
   - Interpretive contributions that do not involve non-trivial modeling are minor contributions.

Then assess whether the paper provides a satisfactory deep dive into the AI singularity concept of Jones (2024):
1. Read all of the Jones (2024) paper.
2. Assess whether the paper's modelling captures key features of Jones's model.
   - At least two key features should be captured.
3. Assess whether these features lead to meaningful results.
   - A meaningful result should tie to the main argument of the paper.

Guidelines:
- Be specific about what improved and what still falls short.
- Do not reduce the report to a binary verdict.
- Prioritize the highest-value remaining changes.
- If the paper still overstates its contribution relative to GKP, say so directly.
- If the Jones extension is still too thin or disconnected from the main argument, say so directly.

Write your report to: {report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {referee_id}
- Line 2: REFEREE — followed by the current date
- Then: ## Summary (one paragraph overall assessment)
- Then: ## Comments (numbered list)
"""

    return run_referee(
        script_file=__file__,
        prompt=prompt,
        agent=AGENT,
        model=MODEL,
        default_agent_log_mode="verbose",
    )


if __name__ == "__main__":
    raise SystemExit(main())
