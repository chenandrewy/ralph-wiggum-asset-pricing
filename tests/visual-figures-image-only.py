#!/usr/bin/env python3
"""
How to run: python tests/visual-figures-image-only.py [--agent-log-mode off]
Inputs: paper/exhibits/fig-*.pdf
Outputs: test-results/visual-figures-image-only.md and process exit code (0=PASS, 1=FAIL)

Like visual-figures.py but examines the exhibit PDFs directly (no page images).
Each sub-agent receives one figure PDF and evaluates readability and
distinguishability at the panel level.
"""

from __future__ import annotations

from _test_helpers import (
    build_test_context,
    fail_test,
    run_test,
)

AGENT = "claude"
MODEL = "claude-opus-4-6"
EXHIBITS_DIR = "paper/exhibits"

# ---------------------------------------------------------------------------
# Sub-agent prompt template.  Each sub-agent receives one figure PDF
# and evaluates every panel for readability + distinguishability.
# The sub-agent reports back to the orchestrator (no file writes).
# ---------------------------------------------------------------------------
FIGURE_REVIEWER_PROMPT = """\
Open and visually inspect this figure PDF: {figure_pdf}
Use the caption to understand what each panel shows.

## Procedure
1. Identify every panel (e.g. Panel A, Panel B, or the full figure if no sub-panels).
2. For each panel individually, evaluate readability.
3. For each panel individually, evaluate distinguishability.
4. Record every readability or distinguishability problem that bears on the requirements.
5. Explain the figure's main message based on the figure and caption alone.
6. Report back with a verdict, a one-sentence reason, and per-panel findings with assessments.

## Requirements
1. Readability: titles, axis labels, legends, tick labels, and font sizes are readable.
2. Distinguishability: plotted series or marks are clearly distinguishable.
3. Contrast: every line, curve, and reference mark must have strong visual contrast against the background. Light gray, thin, or low-opacity lines fail this requirement.
4. Use of space: axis limits should be set so the data fills the plot area. Large empty regions where no data appears are wasted space and fail this requirement.
5. Narrative clarity: a reader can understand the figure's main message from the figure and caption alone.

## Guidelines
1. Treat text that is too small, overlapping, or cut off as a readability problem.
2. Treat lines, colors, or legend encodings that are confusing, ambiguous, duplicated in a misleading way, or hard to tell apart as a distinguishability problem.
3. Treat legends or insets that cover non-trivial parts of the main plot as a distinguishability problem.
4. Apply the "instant read" test: every series, whether rendered as a line, band, shaded region, set of points, or bar, should be visually separable from all other series without effort.
5. Spatial overlap between elements that use different visual channels does not count against the figure if each element remains clearly identifiable through the overlap.
6. Every plotted element — including reference lines, benchmarks, and dashed horizontal/vertical markers — must be dark and high-contrast enough to see immediately. Light gray lines fail, regardless of whether they are "auxiliary" or "reference" elements. There is no exemption for reference lines: if it is drawn on the plot, it must be clearly visible.
7. Check each axis bound independently. For each of the four edges (x-min, x-max, y-min, y-max), measure the gap between the axis limit and the nearest data. If the gap exceeds 20% of the data span on that axis, that edge fails the use-of-space requirement. Example: if data on the y-axis spans 7 to 36 (range = 29), then the y-axis maximum should be no higher than about 42 (36 + 0.2 × 29). A y-max of 50 wastes space. Apply the same logic to x-min, x-max, and y-min. "Headroom for the legend" is not a valid reason — legends can be repositioned. Also check whether the axis range extends far past where the data carries visual information: if curves have fully flattened and converged well before the axis maximum, the remaining axis is wasted.

Report back with:
- VERDICT: PASS or FAIL
- REASON: one short sentence
- Per-panel findings with assessments\
"""


def main() -> int:
    context = build_test_context(__file__)
    exhibits_dir = context.repo_root / EXHIBITS_DIR

    pdfs = sorted(exhibits_dir.glob("fig-*.pdf"))
    if not pdfs:
        return fail_test(context, f"no figure PDFs found in {EXHIBITS_DIR}")

    # Build per-figure sub-agent prompts.
    figures = []
    for pdf in pdfs:
        rel = str(pdf.relative_to(context.repo_root))
        sub_prompt = FIGURE_REVIEWER_PROMPT.format(figure_pdf=rel)
        figures.append({
            "exhibit_id": pdf.stem,
            "sub_prompt": sub_prompt,
        })

    # Format sub-agent instructions for the orchestrator.
    sub_agent_block = "\n\n".join(
        f"### {f['exhibit_id']}\n```\n{f['sub_prompt']}\n```"
        for f in figures
    )

    prompt = f"""\
You are an orchestrator for visual figure quality checks.

## Procedure
1. Launch ALL of the following sub-agents IN PARALLEL using the Agent tool (one per figure).
2. Use model "opus" for each sub-agent.
3. Each sub-agent will report its findings back to you; do not ask sub-agents to write files.
4. After all sub-agents report back, aggregate their findings figure by figure.
5. Write the aggregated report to: {context.report_path}

{sub_agent_block}

## Requirements
1. Every figure listed in the subagent block satisfies the readability requirement.
2. Every figure listed in the subagent block satisfies the distinguishability requirement.
3. Every figure listed in the subagent block satisfies the contrast requirement.
4. Every figure listed in the subagent block satisfies the use-of-space requirement.

## Guidelines
1. Evaluate every figure listed in the subagent block.

## Output
- Line 1: # {context.test_id}
- VERDICT: PASS or VERDICT: FAIL
- REASON: short summary
- Then each figure's verdict, reason, and full panel-by-panel findings
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
