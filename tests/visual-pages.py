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

Evaluate the following questions:
1. Does every page have a visible page number?
2. Are figures and tables nicely formatted and readable?
3. Are there formatting issues such as overflowing text, broken references, or missing figures?
4. Does the paper length conform to the spec?

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Further details on your findings.
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
