#!/usr/bin/env python3
"""
How to run: python tests/element-rhetoric-meta.py
Inputs: paper/paper.tex
Outputs: test-results/element-rhetoric-meta.md and process exit code (0=PASS, 1=FAIL)
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
paper/paper.tex is about AI displacement risk, and is itself written by AI. Evaluate how the paper uses the rhetorical device. The rhetorical device should be used in both the abstract and introduction, but subtly enough that it does not turn off human readers.

As background, humans strongly prefer to read writing written by humans. Indeed, a previous draft of this paper was rejected from `arxiv.org` (a very rare occurrence), likely because it was written by AI.

Evaluate the following elements as PASS/FAIL.

## Elements
1. Is the rhetorical device used in both the abstract and introduction?
2. Would humans be turned off by the use of the rhetorical device?
3. Is the use of the rhetorical device compelling and interesting?
4. Is the use of the rhetorical device distracting or overbearing?
5. Is the description of the human's role accurate based on the key files in the repo, including `spec/*`?

## Output
Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Describe your findings in detail.
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
