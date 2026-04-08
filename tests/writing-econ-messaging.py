#!/usr/bin/env python3
"""
How to run: python tests/writing-econ-messaging.py
Inputs: paper/paper.tex
Outputs: test-results/writing-econ-messaging.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test

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
Read `{paper_path}` and evaluate the paper's economic messaging by main section.

Ignore non-core sections such as the blank preface, proofs, and bibliography.

## Procedure
1. Identify the paper's core main sections yourself.
2. Spawn one subagent per core main section. Run them in parallel.
3. Each subagent should evaluate its assigned section and answer:

   "Does this section make its economic message(s) clear? Yes or no?"

   The subagent should state:
   - the economic message(s) it identifies
   - whether they are clearly stated or must be inferred
   - YES or NO with a short explanation

4. Review the subagent outputs and compile one report.
5. PASS only if every core main section gets YES. FAIL if any core main section gets NO.

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then list the core main sections you evaluated
- Then, for each section:

## [Section Name]
- **Subagent verdict:** YES or NO
- **Economic message(s) identified:** ...
- **Assessment:** ...
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
