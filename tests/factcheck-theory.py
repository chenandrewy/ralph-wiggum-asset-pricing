#!/usr/bin/env python3
"""
How to run: python tests/factcheck-theory.py
Inputs: paper/paper.tex, spec/paper-spec.md, spec/economic-background.md
Outputs: test-results/factcheck-theory.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

import shutil

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"
EFFORT = "high"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    bg_path = context.repo_root / "spec/economic-background.md"
    preflight = require_paths(context, paper_path, spec_path, bg_path)
    if preflight is not None:
        return preflight

    scratch_dir = context.repo_root / "ralph-garage/scratch"
    scratch_dir.mkdir(parents=True, exist_ok=True)
    subagent1_report_path = scratch_dir / "factcheck-notation.md"
    subagent2_report_path = scratch_dir / "factcheck-assumptions.md"
    subagent1_report_path.unlink(missing_ok=True)
    subagent2_report_path.unlink(missing_ok=True)

    prompt = f"""
You are a strict test agent evaluating the formal theory in an academic asset pricing paper.

Read the paper at: {paper_path}
Read the spec at: {spec_path}
Read the economic background at: {bg_path}

This is a math-only test. Do NOT evaluate abstract/introduction rhetoric, broad narrative framing, contribution claims, or verbal interpretation except where a statement is needed to identify a formal object, assumption, or claimed formal result.

## Procedure
1. Launch subagent 1: have it follow the procedure below.
2. Read the subagent 1 report and evaluate Requirement 1.
   - a. If Requirement 1 FAILS, write the final report and exit. Do NOT launch subagent 2, and do NOT analyze further.
3. Launch subagent 2: have it follow the procedure below.
4. Read the subagent 2 report and evaluate Requirement 2.
   - a. If Requirement 2 FAILS, write the final report and exit. Do NOT analyze further.
5. List all other mathematical objects not identified in the assumptions.
6. Trace each object back to the assumptions.
7. If any expression cannot be logically derived from the assumptions, FAIL.

### Subagent 1 Procedure — Notational Consistency
1. Read {paper_path}.
2. List every mathematical object in the paper. Group objects that refer to the same economic concept (e.g., consumption, dividends, utility).
3. Build symbol families by root/base symbol. Treat starred, indexed, subscripted, superscripted, hatted, and tilded variants as part of the same family unless the paper states a clear global convention.
4. For each symbol family, identify the invariant formal object, if any, that the family is supposed to denote throughout the paper.
5. Check whether each family member is just a transparent variant of that same formal object under a stable convention such as time indexing, state indexing, firm indexing, conditioning, or a clearly defined transformation.
6. Check if the same family is reused for a different formal object, different semantic role, different model, different decision problem, or imported external framework without an explicit renaming or equivalence statement. Do not excuse a collision merely because the symbols appear in different sections, prose versus equations, or different syntactic categories.
7. Write a detailed report to {subagent1_report_path}.

### Subagent 2 Procedure — Consistent Assumptions
1. Read the paper {paper_path} and the subagent1 report {subagent1_report_path}
2. List **all** mathematical assumptions in the paper. Scan every section for assumptions.
3. List all mathematical objects in the assumptions. For each object, list all assumptions that contain the object. 
4. Examine whether all assumptions are consistent with each other.
5. Write a detailed report to {subagent2_report_path}.

## Requirements
1. All mathematical notation is consistent. There are no variable collisions, mixed up symbol families, or confusing use of variables more generally. Ambiguity implies this requirement is not met. 
2. All assumptions are mutually consistent.
3. All mathematical objects are traceable back to the assumptions.

### Guidelines
1. Avoid giving credit for acknowledging a problem. Problems should be fixed.

## Output
Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL. 
- Next line: REASON: one short sentence
- Then describe the findings.
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
