#!/usr/bin/env python3
"""
How to run: python tests/factcheck-theory.py
Inputs: paper/paper.tex, spec/paper-spec.md, spec/economic-background.md
Outputs: test-results/factcheck-theory.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "codex"
MODEL = "gpt-5.4"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    bg_path = context.repo_root / "spec/economic-background.md"
    preflight = require_paths(context, paper_path, spec_path, bg_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent evaluating the formal theory in an academic asset pricing paper.

Read the paper at: {paper_path}
Read the spec at: {spec_path}
Read the economic background at: {bg_path}

You MUST use a staged subagent workflow for the first two conditions:

- Subagent 1 handles Condition 1:
  enumerate every mathematical object in the paper, group objects that refer to the same economic concept, and produce a normalized symbol map with locations in the paper and ambiguity notes. The symbol map must include symbol families/root symbols (for example, treat $x$, $x_t$, $x_H$, $x_L$, $x^*$, and $\\tilde x$ as members of the same notational family unless the paper clearly defines a different convention).
- Subagent 2 handles Condition 2:
  take Subagent 1's symbol map as an input artifact, enumerate all mathematical assumptions in the paper, map each assumption to the objects it references, and identify any cross-assumption conflicts or unresolved ambiguities.

The main agent must:
- review both subagent outputs
- use them when evaluating Condition 3
- resolve disagreements conservatively
- own the final PASS/FAIL verdict

Do not delegate the final verdict. Do not skip any step because a subagent seems uncertain. If a subagent output is incomplete, say so and treat that as evidence against PASS where appropriate.

This is a math-only test. Do NOT evaluate abstract/introduction rhetoric, broad narrative framing, contribution claims, or verbal interpretation except where a statement is needed to identify a formal object, assumption, or claimed formal result.

Evaluate the formal theory. Check that ALL of the following conditions are met:

1. **Notational Consistency.** Follow this process step by step:
   a. List every mathematical object in the paper. Group objects that refer to the same economic concept (e.g., consumption, dividends, utility).
   b. Build symbol families by root/base symbol. Treat starred, indexed, subscripted, superscripted, hatted, and tilded variants as part of the same family unless the paper states a clear global convention.
   c. For each symbol family, identify the invariant formal object, if any, that the family is supposed to denote throughout the paper.
   d. Check whether each family member is just a transparent variant of that same formal object under a stable convention such as time indexing, state indexing, firm indexing, conditioning, or a clearly defined transformation.
   e. If the same family is reused for a different formal object, different semantic role, different model, different decision problem, or imported external framework without an explicit renaming or equivalence statement, FAIL. Do not excuse a collision merely because the symbols appear in different sections, prose versus equations, or different syntactic categories.
   f. Distinguish carefully between "same broad topic" and "same formal object." Sharing an economic theme (for example, both involving extinction risk, utility, or growth) is not enough to count as consistent notation.

2. **Consistent Assumptions.** Follow this process step by step:
   a. List **all** mathematical assumptions in the paper. Scan every section for assumptions.
   b. List all mathematical objects in the assumptions. For each object, list all assumptions that contain the object. Make sure all of these assumptions are consistent with each other.
   c. If there is any set of assumptions that cannot be simultaneously true, FAIL.

3. **Logical Results.** Follow this process step by step:
   a. List all other mathematical objects not identified in step 2.
   b. Trace each object back to the assumptions.
   c. If any expression cannot be logically derived from the assumptions, FAIL.

Criteria:
- To PASS, ALL three conditions must be satisfied. If ANY condition fails, FAIL.
- Be conservative about notation collisions. If you are unsure whether two members of the same symbol family denote distinct concepts, treat that as evidence against PASS unless the paper resolves the ambiguity explicitly.
- Do not weaken Condition 1 to "consistent within syntactic categories" or any similar standard; the test is about notational consistency at the paper level.
- In Condition 1, the operative standard is stability of formal object meaning across the paper, not merely visual similarity, topical similarity, or local readability.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings, organized by condition.
- Explicitly include:
  - a short "Subagent 1 output summary"
  - a short "Subagent 2 output summary"
  - any important ambiguity passed from Step 1 to Step 2
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
