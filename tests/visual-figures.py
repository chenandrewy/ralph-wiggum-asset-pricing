#!/usr/bin/env python3
"""
How to run: python tests/visual-figures.py [--agent-log-mode off]
Inputs: ralph-garage/page-images/page-*.png, ralph-garage/page-images/exhibit-manifest.json
Outputs: test-results/visual-figures.md and process exit code (0=PASS, 1=FAIL)

Orchestrator spawns one sub-agent per figure (in parallel) to evaluate
readability and distinguishability at the panel level. Sub-agents receive
only the image and a focused visual rubric — no reporting instructions.
"""

from __future__ import annotations

from _test_helpers import (
    build_test_context,
    load_manifest,
    require_manifest_pages,
    require_page_images,
    require_paths,
    run_test,
)

AGENT = "claude"
MODEL = "claude-opus-4-6"
EFFORT = "medium"
IMAGES_DIR = "ralph-garage/page-images"
MANIFEST_PATH = "ralph-garage/page-images/exhibit-manifest.json"

# ---------------------------------------------------------------------------
# Sub-agent prompt template.  Each sub-agent receives one figure's page image
# and evaluates every panel for readability + distinguishability.
# The sub-agent reports back to the orchestrator (no file writes).
# ---------------------------------------------------------------------------
FIGURE_REVIEWER_PROMPT = """\
Open and visually inspect this page image: {image_path}
It contains {exhibit_id}. Use the caption to understand what each panel shows.

## Procedure
1. Identify every panel (e.g. Panel A, Panel B, or the full figure if no sub-panels).
2. For each panel individually, evaluate readability.
3. For each panel individually, evaluate distinguishability.
4. Record every readability or distinguishability problem that bears on the requirements.
5. Explain the figure's main message based on the figure and caption alone. 
6. Explain the figure's main message based on the figure and the text of the paper.
7. Report back with a verdict, a one-sentence reason, and per-panel findings with assessments.

## Requirements
1. Readability: titles, axis labels, legends, tick labels, and font sizes are readable.
2. Distinguishability: plotted series or marks are clearly distinguishable.
3. Narrative clarity: a reader can understand the figure's main message from the figure and caption alone.

## Guidelines
1. Treat text that is too small, overlapping, or cut off as a readability problem.
2. Treat lines, colors, or legend encodings that are confusing, ambiguous, duplicated in a misleading way, or hard to tell apart as a distinguishability problem.
3. Treat legends or insets that cover non-trivial parts of the main plot as a distinguishability problem.
4. Apply the "instant read" test: every series, whether rendered as a line, band, shaded region, set of points, or bar, should be visually separable from all other series without effort.
5. Spatial overlap between elements that use different visual channels does not count against the figure if each element remains clearly identifiable through the overlap.

Report back with:
- VERDICT: PASS or FAIL
- REASON: one short sentence
- Per-panel findings with assessments\
"""


def main() -> int:
    context = build_test_context(__file__)
    images_dir = context.repo_root / IMAGES_DIR
    manifest_path = context.repo_root / MANIFEST_PATH

    preflight = require_paths(context, manifest_path)
    if preflight is not None:
        return preflight

    preflight = require_page_images(context, images_dir)
    if preflight is not None:
        return preflight

    manifest = load_manifest(manifest_path)
    preflight, figure_pages = require_manifest_pages(
        context,
        manifest,
        lambda page: page.get("has_figures"),
        "manifest contains no figure-bearing pages",
    )
    if preflight is not None:
        return preflight

    # Build the figure list and per-figure sub-agent prompts.
    figures = []
    for page in figure_pages:
        image_path = str(context.repo_root / page["image"])
        for exhibit in page.get("exhibits", []):
            if exhibit["kind"] == "Figure":
                sub_prompt = FIGURE_REVIEWER_PROMPT.format(
                    image_path=image_path,
                    exhibit_id=exhibit["exhibit_id"],
                )
                figures.append({
                    "exhibit_id": exhibit["exhibit_id"],
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
        default_agent_effort=EFFORT,
        default_agent_log_mode="verbose",
    )


if __name__ == "__main__":
    raise SystemExit(main())
