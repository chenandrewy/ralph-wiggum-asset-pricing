#!/usr/bin/env python3
"""
How to run: python tests/spec-economic.py
Inputs: paper/paper.tex, spec/economic-background.md
Outputs: test-results/spec-economic.md and process exit code (0=PASS, 1=FAIL)

Checks that the paper consistently uses the definitions in the economic background spec.
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test

AGENT = "claude"
MODEL = "opus"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/economic-background.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""\
Read the economic background spec at: {spec_path}
Read the paper at: {paper_path}

For every section of the paper, check whether each concept from the spec is used
consistently with its definition. Quote each relevant usage and flag any
inconsistency. FAIL if any usage is inconsistent. Be strict.

Write your report to: {context.report_path}
Format: line 1 "# {context.test_id}", then "VERDICT: PASS" or "VERDICT: FAIL",
then "REASON: ...", then section-by-section findings.
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
