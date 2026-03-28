#!/usr/bin/env python3
"""
How to run: python dev/qf/qf-conciseness.py
Inputs: paper/paper.tex
Outputs: dev/qf-results/qf-conciseness.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _qf_helpers import build_test_context, require_paths, run_test

AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)
    paper_path = context.repo_root / "paper/paper.tex"
    preflight = require_paths(context, paper_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a skeptical test agent auditing mathematical conciseness in an academic paper.

Read the paper at: {paper_path}

## Procedure
1. Read the full paper.
2. List every numbered equation and every named mathematical object introduced in the paper, including variables, parameters, and functions.
3. For each numbered equation, trace it forward and state which later equation, result, calibration, or interpretation depends on it.
4. For each named mathematical object, check whether it appears in at least one result that matters for the paper's conclusions.
5. Check whether any result could be stated with fewer mathematical objects. Flag redundant notation, duplicate symbols for the same concept, or intermediate expressions that could be skipped.
6. Focus on the strongest few violations and write the report.

## Definitions
1. Unnecessary formalism includes equations that are never used in a later derivation, proposition, calibration, or interpretation.
2. Unnecessary notation includes parameters, variables, or functions that do not appear in a result that matters for the paper's conclusions.
3. Redundant notation includes mathematical objects that duplicate existing notation or could be removed without weakening the paper's economic claims.

## Guidelines
1. Be adversarial. Do not give credit for merely local use inside the same paragraph if the object does not matter later.
2. Standard primitives are usually allowed, but still trace them forward.
3. If an object could be replaced with plain English without weakening the paper's claims, treat that as a violation.

## Requirements
1. Every numbered equation is used in a later derivation, result, calibration, or interpretation that matters for the paper's conclusions.
2. Every named mathematical object appears in at least one result that matters for the paper's conclusions.
3. The paper contains no redundant notation or intermediate expressions that could be removed without weakening the paper's economic claims.
4. The paper contains no formalism that could be replaced with plain English without weakening the paper's economic claims.
5. PASS only if all requirements are satisfied. FAIL if any requirement is not satisfied.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then explain the main findings briefly.
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
