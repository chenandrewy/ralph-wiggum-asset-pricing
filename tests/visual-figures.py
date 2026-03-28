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
4. Report back with a verdict, a one-sentence reason, and per-panel findings with assessments.

## Requirements
1. Readability: titles, axis labels, legends, tick labels, and font sizes are readable.
   - Fail if any text is too small, overlapping, or cut off.
2. Distinguishability: plotted series or marks are clearly distinguishable.
   - Fail if lines, colors, or legend encodings are confusing, ambiguous, duplicated in a misleading way, or hard to tell apart.
   - Fail if the legend or insets cover non-trivial parts of the main plot.
   - Apply the "instant read" test: every series — whether rendered as a line, band, shaded region, set of points, or bar — must be visually separable from all other series without effort. If a reader must squint, cross-reference the legend repeatedly, or mentally decompose overlapping elements to tell series apart, fail. Note: spatial overlap between elements that use different visual channels (e.g. a dashed line crossing a shaded band, or a reference boundary drawn over a confidence region) does NOT fail this test as long as each element remains clearly identifiable through the overlap.

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
4. After all sub-agents report back, write an aggregated report to: {context.report_path}

{sub_agent_block}

## Requirements
1. Every figure listed in the subagent block is evaluated.
2. The overall verdict is FAIL if any figure fails.

Format:
- Line 1: # {context.test_id}
- VERDICT: PASS or VERDICT: FAIL (FAIL if any figure failed)
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
