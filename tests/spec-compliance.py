#!/usr/bin/env python3
"""
How to run: python tests/spec-compliance.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/spec-compliance.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent checking whether an academic paper complies with its specification.

Read the spec at: {spec_path}
Read the paper at: {paper_path}

Procedure:
1. List every requirement from the spec sections I (Economic Requirements) and II (Style Requirements).
2. For each requirement, check whether the paper satisfies it. Quote evidence from the paper.
3. A requirement is satisfied only if the paper clearly addresses it. Do not give credit for vague or partial coverage. Enforce this strictly.

Criteria:
- To PASS, ALL requirements must be satisfied. If ANY requirement is not met, FAIL.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings, organized by requirement.
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
