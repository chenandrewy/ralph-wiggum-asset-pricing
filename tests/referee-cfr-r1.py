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
EFFORT = "medium"


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
You are a constructive referee at a top finance journal.
You do NOT accept or reject this paper. You provide suggestions to help the author improve it.

A prior referee (CFR R1) raised two concerns about an earlier draft. That report is at:
  {cfr_path}

You are NOT that referee. Use their concerns as a guide for where to focus, but write your own assessment of the current draft. 

Read all of these documents before writing your report:
- The current paper: {paper_path}
- The CFR R1 report: {cfr_path}
- The GKP paper: {gkp_path}
- The Jones (2024) paper: {jones_path}

Limit your report to at most three concrete, actionable suggestions. 

Write your report to: {report_path}
The report must be a clean, human-readable markdown file with this exact format:
- Line 1: # {referee_id}
- Line 2: REFEREE — followed by the current date
- Then: ## Summary (one paragraph overall assessment)
- Then: ## Suggestions (numbered list of concrete improvements)
"""

    return run_referee(
        script_file=__file__,
        prompt=prompt,
        agent=AGENT,
        model=MODEL,
        default_agent_effort=EFFORT,
        default_agent_log_mode="verbose",
    )


if __name__ == "__main__":
    raise SystemExit(main())
