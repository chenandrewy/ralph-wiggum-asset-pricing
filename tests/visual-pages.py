#!/usr/bin/env python3
"""
How to run: python tests/visual-pages.py
Inputs: ralph-garage/page-images/page-*.png, spec/paper-spec.md
Outputs: test-results/visual-pages.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_page_images, require_paths, run_test


AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    spec_path = context.repo_root / "spec/paper-spec.md"
    images_dir = context.repo_root / "ralph-garage/page-images"
    preflight = require_paths(context, spec_path)
    if preflight is not None:
        return preflight
    preflight = require_page_images(context, images_dir)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict test agent evaluating the visual presentation of an academic paper.

Read the spec at: {spec_path}
Look at ALL page images in: {images_dir}

## Procedure
1. Evaluate every page image in {images_dir}.
2. Check whether every page has a visible page number.
3. Check whether figures and tables are nicely formatted and readable.
4. Check whether the paper appears well-structured with clear section headings.
5. Check whether there are obvious formatting issues such as overflowing text, broken references, or missing figures.
6. Check whether paper length conforms to the spec (less than 20 pages).
7. Record every violation of the requirements that you find.

## Requirements
1. Every page has a visible page number.
2. Figures and tables are nicely formatted and readable.
3. The paper appears well-structured with clear section headings.
4. There are no obvious formatting issues such as overflowing text, broken references, or missing figures.
5. Paper length conforms to the spec (less than 20 pages).

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then a brief summary of your findings.
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
