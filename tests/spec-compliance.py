#!/usr/bin/env python3
"""
How to run: python tests/spec-compliance.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/spec-compliance.md and process exit code (0=PASS, 1=FAIL)

Orchestrator spawns one sub-agent per top-level requirement section (in parallel)
to evaluate compliance. Checks all straightforward requirements (everything except
the Quality Requirements section).
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test

AGENT = "claude"
MODEL = "claude-opus-4-6"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""\
You are an orchestrator for spec-compliance checks on an academic paper.

Read the spec at: {spec_path}

For each top-level requirement section (roman numerals) EXCEPT "Quality Requirements",
launch a sub-agent IN PARALLEL using the Agent tool.

Each sub-agent should:
- Read the spec at {spec_path} and the paper at {paper_path}
- Check every requirement (and sub-requirement) in its assigned section
- Verify compliance across ALL sections of the paper, not just one or two
- Quote evidence from the paper for each requirement
- Use model "opus"
- Report back (do not write files)

After all sub-agents report back, write an aggregated report to: {context.report_path}

Format:
- Line 1: # {context.test_id}
- VERDICT: PASS or VERDICT: FAIL (FAIL if any section failed)
- REASON: short summary
- Then each section's verdict, reason, and per-requirement findings
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
