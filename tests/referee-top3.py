#!/usr/bin/env python3
"""
How to run: python tests/referee-top3.py [--agent-log-mode MODE]
Inputs: paper/paper.tex, spec/paper-spec.md, ralph-garage/page-images/page-*.png, test-results/
Outputs: test-results/referee-top3.md (always exits 0)
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
    spec_path = repo_root / "spec/paper-spec.md"
    images_dir = repo_root / "ralph-garage/page-images"
    test_results_dir = repo_root / "test-results"

    for p in (paper_path, spec_path):
        if not p.exists():
            write_fallback_report(report_path, f"missing: {p}")
            return 0

    prompt = f"""
You are a referee at a top finance journal (Journal of Finance, JFE, RFS).
You do NOT accept or reject this paper. You provide constructive feedback to help the authors improve it.

Read:
- The paper source: {paper_path}
- The paper specification: {spec_path}
- Page images of the compiled paper in: {images_dir}
- Test results from the latest test run: {test_results_dir}

Your task:
1. Read the full paper carefully.
2. Inspect all exhibits using the page images.
3. Read the test results. Consider which tests passed and which failed.
4. Evaluate the paper against its specification. Identify where the paper falls short of the goals and requirements stated in the spec.
5. Recommend improvements that would make it publishable at a top journal. Focus on issues the tests did not already catch.

Guidelines:
- Focus on substantive issues: economic reasoning, model correctness, completeness vs incompleteness distinction, policy implications.
- Treat the paper specification as authoritative.
- The report should only suggest one or two major tasks.

Write your report to: {report_path}
The report must be a clean, human-readable markdown file with this exact format:
- Line 1: # {referee_id}
- Line 2: REFEREE — followed by the current date
- Then: ## Summary (one paragraph overall assessment)
- Then: ## Comments (numbered list)

Do NOT include a VERDICT line. This is a referee report, not a test.
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
