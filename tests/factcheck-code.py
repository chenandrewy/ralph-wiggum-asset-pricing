#!/usr/bin/env python3
"""
How to run: python tests/factcheck-code.py
Inputs: code/*, data/*, paper/paper.tex
Outputs: test-results/factcheck-code.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"


def main() -> int:
    context = build_test_context(__file__)

    code_dir = context.repo_root / "code"
    data_dir = context.repo_root / "data"
    paper_path = context.repo_root / "paper/paper.tex"
    paper_spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, code_dir, data_dir, paper_path, paper_spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent auditing the paper's local codebase.

Read the canonical paper at: {paper_path}
Read the paper spec at: {paper_spec_path}
Inspect the code under: {code_dir}
Inspect local data or cached outputs under: {data_dir}

Task:
1. Identify the canonical local analysis path in code/ that is intended to support the paper.
2. Exclude scripts whose primary role is downloading data, external setup, or nonlocal/network-dependent work.
3. Using only local inputs already present in the repo, run the relevant local analysis steps in dependency order when feasible.
4. Check whether the code's outputs and logic match the paper's quantitative objects, exhibits, calibration, and stated implementation choices.
5. Distinguish clearly between:
   - code or workflow problems,
   - missing required local inputs,
   - missing or undocumented runtime dependencies,
   - and inability to execute because this environment lacks tools such as R or required packages.

Requirements:
- There is a coherent local analysis path for the paper
- If the paper relies on local code, there is a canonical fast local analysis path that uses only local inputs already present in the repo
- The code structure is logically organized
- The paper's claims about implemented analysis are consistent with the actual code
- Any paper output that is not reproducible from the local analysis path is clearly labeled in the paper as external, nonlocal, unreproducible from repo inputs, or illustrative/non-canonical
- The repo does not depend on hidden or unnecessary auxiliary files for the claimed local workflow

Rules:
- Use only existing local inputs. Do not download anything.
- If the required local inputs or canonical local analysis path are missing, fail the test.
- If execution is blocked only because this environment lacks R, required packages, or another runtime dependency, do not claim the code logic is broken on that basis alone. Report the execution blocker separately and use static evidence from the code and paper to judge the workflow.
- If the canonical local workflow itself requires undocumented tools or packages, treat that as a workflow problem.
- Be strict about mismatches between what the paper says was done and what the code actually does.
- When discussing reproducibility, name the exact output or claim and classify it as locally reproducible, blocked by environment, blocked by missing local inputs, or inconsistent with the code.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary with short sections for:
  - Canonical local analysis path
  - Execution status
  - Paper-code consistency
  - Reproducibility classification
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
