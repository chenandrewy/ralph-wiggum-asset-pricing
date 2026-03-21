#!/usr/bin/env python3
"""
How to run: python tests/ai-economics.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/ai-economics.md and process exit code (0=PASS, 1=FAIL)
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
You are a strict test agent evaluating the economics of AI in an academic asset pricing paper.

Read the paper at: {paper_path}
Read the spec at: {spec_path}

Evaluate ONLY the economics of AI in the paper. The economics should satisfy:
1. In the singularity, productivity and output grows enormously, in aggregate.
2. In the singularity, the representative household's income is displaced by AI.
3. The owners of AI capital benefit from the singularity.
4. The incomplete markets case is distinct from the complete markets case, and both are characterized.

Criteria:
- To PASS, ALL four conditions must be satisfied. If ANY condition fails, FAIL.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings.
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
