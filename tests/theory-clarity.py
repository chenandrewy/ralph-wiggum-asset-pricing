#!/usr/bin/env python3
"""
How to run: python tests/theory-clarity.py
Inputs: paper/paper.tex
Outputs: test-results/theory-clarity.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test

AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    preflight = require_paths(context, context.repo_root / "paper/paper.tex")
    if preflight is not None:
        return preflight

    prompt = f"""
You are evaluating the clarity of model descriptions in `paper/paper.tex`.

## Definitions
- A **key model assumption or expression** is a formal assumption, inequality, definition, equation, or expression that later main results, propositions, comparative statics, or headline interpretations rely on, such that a reader who misses it would have trouble understanding or evaluating those results.
- The most critical key expressions should appear in display math in the main text, so the reader can easily find them again.
- Other key new model assumptions may remain in prose, but they should appear at or near the start of a paragraph.
- Conditions stated only inside propositions, theorems, lemmas, corollaries, or proofs are not by themselves new model assumptions.

## Procedure
1. Read `paper/paper.tex`.
2. Launch one subagent to read the whole paper and identify the key model assumptions and expressions that later main results rely on.
   The subagent should output a short canonical list grouped into:
   - items that should appear in display math in the main text
   - items that may remain in prose but should be stated at or near the start of a paragraph if they are newly introduced in prose
3. Launch one subagent to read the whole paper and, for each item on the canonical list, identify where it is first substantively introduced and how it is introduced:
   - display math in the main text
   - formal assumption block
   - setup paragraph in prose
   - proposition/theorem statement only
   - proof only
   - later recall only
4. Read both subagent reports and evaluate the paper freeform using the following questions:
   A. Are new model assumptions presented in distinct model-setup paragraphs or formal assumption blocks when they are introduced in prose?
   B. Do the most critical key expressions appear in display math in the main text?
   C. When other key new model assumptions are introduced in prose, do they appear at or near the start of a paragraph?
5. Do not fail a section merely because it recalls an earlier assumption, uses an earlier definition, or states a conditional expression inside a proposition or proof.
6. Report the final verdict for the paper as a whole, then give concise section-level findings where relevant.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a short list of the key items you identified.
- Then concise findings by section, referencing the relevant key items.
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
