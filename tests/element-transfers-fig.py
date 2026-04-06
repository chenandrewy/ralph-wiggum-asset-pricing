#!/usr/bin/env python3
"""
How to run: python tests/element-transfers-fig.py
Inputs: paper/paper.tex, spec/paper-spec.md, paper/exhibits/*.pdf
Outputs: test-results/element-transfers-fig.md and process exit code (0=PASS, 1=FAIL)

Orchestrator reads the paper and spec to identify the Extension 2 (government transfers)
exhibit PDF and its caption, then spawns a sub-agent that evaluates the figure using
only the exhibit PDF and caption — no paper text, to avoid contaminating the visual
assessment.
"""

from __future__ import annotations

from _test_helpers import (
    build_test_context,
    fail_test,
    require_paths,
    run_test,
)


AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


REVIEWER_PROMPT = """\
You are a strict test agent evaluating whether a figure in an academic paper
effectively conveys its intended economic message.

Open and visually inspect this exhibit PDF: {exhibit_path}

The figure's caption is:
{caption}

The paper argues that government transfers, which are normally too wasteful to help,
become a viable policy tool when the AI singularity generates enormous output growth.

## Task

Evaluate the figure using ONLY the exhibit PDF and the caption above. Answer these
questions:

1. Does the figure show that the singularity is catastrophic for the household if the
   government does nothing? A reader should immediately see that doing nothing is bad.

2. Does the figure show that transfers are ineffective under normal conditions?
   The deadweight costs should visibly overwhelm any benefit.

3. Does the figure show that singularity-scale growth changes the calculus — that
   transfers become effective precisely because there is so much output to redistribute,
   even after accounting for waste?

4. Is the overall message clear to a reader of a top finance journal? Could a reader
   grasp the key insight from the figure and its caption alone?

The figure passes only if all four messages come through clearly.

Report back with:
- VERDICT: PASS or FAIL
- REASON: one short sentence
- Then answer each of the four questions with a brief assessment.\
"""


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    exhibits_dir = context.repo_root / "paper/exhibits"

    preflight = require_paths(context, paper_path, spec_path, exhibits_dir)
    if preflight is not None:
        return preflight

    reviewer_prompt_template = REVIEWER_PROMPT.replace("{exhibit_path}", "<EXHIBIT_PATH>").replace("{caption}", "<CAPTION>")

    prompt = f"""
You are an orchestrator for an element test on the government transfers figure.

## Step 1: Identify the exhibit and extract its caption

Read the paper and the spec to identify which exhibit PDF in `paper/exhibits/`
corresponds to a model extension about government transfers.

- Paper source: {paper_path}
- Spec: {spec_path}
- Exhibits directory: {exhibits_dir}

Read the paper to find the figure environment for the transfers extension. Extract
the exhibit filename from the \\includegraphics command. Confirm the file exists in
`{exhibits_dir}`. Also extract the full \\caption text from the same figure environment.

If no such figure exists, write a FAIL report and stop.

## Step 2: Launch a sub-agent to evaluate the exhibit

Once you have the exhibit PDF path and the caption, launch a sub-agent using the
Agent tool with model "opus". Use the following prompt, replacing <EXHIBIT_PATH>
with the actual path to the exhibit PDF and <CAPTION> with the extracted caption text:

```
{reviewer_prompt_template}
```

Do not ask the sub-agent to write files. It will report its findings back to you.

IMPORTANT: Do not include the paper source or spec in the sub-agent prompt. The
sub-agent should evaluate the figure using only the exhibit PDF and caption.

## Step 3: Write the report

Based on the sub-agent's findings, write the final report.

Write your report to: {context.report_path}
Format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then the sub-agent's per-question assessments.
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
