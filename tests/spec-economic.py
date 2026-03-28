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
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/economic-background.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    prompt = f"""\
You are a strict test agent evaluating whether an academic asset pricing paper uses the project's economic terminology consistently.

Read the economic background spec at: {spec_path}
Read the paper at: {paper_path}

This is a terminology-consistency test. Focus on whether the paper uses the concepts from the economic background spec in a way that matches the spec's definitions throughout the paper.

## Procedure
1. Read the full economic background spec.
2. Identify each concept in the spec that imposes a definitional constraint on how the paper should use economic terms.
3. Scan the full paper section by section.
4. For each relevant concept, collect the paper's usages and quote the relevant passages.
5. For each relevant concept, compare the paper's usage against the definition in the spec.
6. Evaluate whether the term keeps the same economic meaning across sections, models, and rhetorical contexts.
7. Record every inconsistency, ambiguity that changes the economic meaning, and cross-section drift that you find.

## Requirements
1. Each concept from the economic background spec is used consistently with its definition in EVERY SECTION of the paper.
2. Terminology is consistent across sections, models, or rhetorical contexts.

### Guidelines
1. Be strict. Do not give credit for approximate or suggestive alignment when the definition is more precise.
2. Treat ambiguity as a problem when it creates uncertainty about the paper's economic meaning.
3. Evaluate the full paper, not just the main model section.
4. Quote the relevant paper usage and the corresponding spec definition for each inconsistency you identify.
5. If a term appears only rarely, still judge whether the usage is consistent with the spec rather than excusing the issue for lack of repetition.

## Output
Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then section-by-section findings with the relevant quoted usages and any inconsistencies.
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
