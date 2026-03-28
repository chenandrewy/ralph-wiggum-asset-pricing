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
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""\
You are a strict test agent evaluating whether an academic paper satisfies the paper specification, except for the Quality Requirements section.

Read the paper at: {paper_path}
Read the spec at: {spec_path}

This is a spec-compliance test. Do NOT evaluate Quality Requirements. Do NOT do a general referee report. Focus only on whether the paper satisfies the listed requirements in Sections I, II, and III of the spec, excluding the top-level section named "Quality Requirements".

## Procedure
1. Launch one subagent IN PARALLEL for each top-level requirement section (roman numerals) EXCEPT "Quality Requirements".
2. Each subagent should:
   - Read the paper at {paper_path} and the spec at {spec_path}.
   - Audit only its assigned top-level requirement section.
   - Check every requirement and sub-requirement in that section.
   - Verify compliance across the full paper, not just one local passage.
   - Quote concrete evidence from the paper for each requirement.
   - Report back to you. Do NOT write files.
3. Read all subagent reports.
4. Evaluate each assigned top-level section.
5. Record the compliance status of each assigned top-level section.

## Requirements
1. Every non-Quality top-level requirement section in the spec is satisfied.
2. Within each such section, every requirement and sub-requirement is satisfied.

### Guidelines
1. Be strict. A requirement is not satisfied merely because the paper gestures at it.
2. Do not give credit for partial compliance when the spec states a clear requirement.
3. Keep the Quality Requirements section out of scope even if you notice issues there.
4. Judge each requirement against the paper as a whole, not a narrow local snippet.
5. Support each judgment with concrete evidence from the paper.

## Output
Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then, for each audited top-level section:
  - section verdict
  - short reason
  - per-requirement findings with quoted evidence
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
