#!/usr/bin/env python3
"""
How to run: python tests/factcheck-exhibits.py
Inputs: paper/paper.tex, paper/exhibits/, code/*, data/*,
ralph-garage/page-images/page-*.png, ralph-garage/page-images/exhibit-manifest.json
Outputs: test-results/factcheck-exhibits.md and process exit code (0=PASS, 1=FAIL)
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


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    exhibits_dir = context.repo_root / "paper/exhibits"
    code_dir = context.repo_root / "code"
    data_dir = context.repo_root / "data"
    images_dir = context.repo_root / IMAGES_DIR
    manifest_path = context.repo_root / MANIFEST_PATH

    preflight = require_paths(
        context,
        paper_path,
        exhibits_dir,
        code_dir,
        data_dir,
        manifest_path,
    )
    if preflight is not None:
        return preflight

    preflight = require_page_images(context, images_dir)
    if preflight is not None:
        return preflight

    manifest = load_manifest(manifest_path)
    preflight, exhibit_pages = require_manifest_pages(
        context,
        manifest,
        lambda page: page.get("has_figures") or page.get("has_tables"),
        "manifest contains no exhibit-bearing pages",
    )
    if preflight is not None:
        return preflight

    exhibit_lines = []
    seen_ids: set[str] = set()
    for page in exhibit_pages:
        image_path = str(context.repo_root / page["image"])
        page_no = page["page"]
        for exhibit in page.get("exhibits", []):
            exhibit_id = exhibit.get("exhibit_id", f"Page {page_no} exhibit")
            if exhibit_id in seen_ids:
                continue
            seen_ids.add(exhibit_id)
            exhibit_lines.append(
                f"- {exhibit_id}: page {page_no}, image {image_path}, "
                f"label {exhibit.get('latex_label', 'none')}, kind {exhibit.get('kind', 'unknown')}"
            )

    exhibit_block = "\n".join(exhibit_lines)

    prompt = f"""\
You are a strict exhibit fact-checking agent for an academic paper.

Read the paper at: {paper_path}
Read the exhibit files in: {exhibits_dir}
Inspect the code under: {code_dir}
Inspect local data or cached outputs under: {data_dir}
Inspect exhibit-bearing page images via the manifest at: {manifest_path}

The paper's rendered exhibits are:
{exhibit_block}

This is an accuracy test, not a style test. Your job is to examine each exhibit for suspicious visible features, then check whether those features are actually supported by the generating code and local data.

## Procedure
1. Evaluate every exhibit listed above. Do not skip any exhibit.
2. Start from the exhibit itself:
   - inspect the rendered exhibit image on its page
   - identify what the exhibit shows
   - list the main visible features that matter for the paper's claims
3. For each exhibit, identify suspicious features if any. Suspicious features include, for example:
   - abrupt jumps, crashes, spikes, or discontinuities
   - suspicious breaks in sample coverage or category membership
   - values near impossible or highly implausible boundaries
   - dominant rows, cells, or plotted objects that look mechanically generated
   - labels, legends, or captions that do not seem to match the object
   - distracting seasonality or noise
4. For each suspicious feature, trace it back to the local generating code and local data or cached outputs when possible.
5. Decide whether each suspicious feature is real and correctly generated, or whether it is an artifact, coding error, aggregation error, labeling error, or unsupported feature.
6. If a suspicious feature is real, explain briefly how the code generates it and why that logic is correct.
7. If a suspicious feature is not real, not justified, or cannot be verified from the local code/data, treat that as a failure.
8. Record every failure. Be strict.

## Requirements
1. Every exhibit is examined individually.
2. For every exhibit, the report clearly describes what the exhibit shows.
3. For every exhibit, suspicious visible features are listed explicitly, or the report states that none were found.
4. Every suspicious feature is traced to the local code and local data or cached outputs when feasible.
5. Every suspicious feature is either verified as real and correctly generated, or it causes the test to fail.
6. The test fails if any suspicious feature appears to be an artifact, an error, unsupported by the code/data, or left materially unexplained.

## Guidelines
1. Start from the rendered exhibit, not from the code.
2. Be concrete. Name the feature, the relevant code path, and the reason for your judgment.
3. Do not pass an exhibit merely because the code runs.
4. If the repo lacks enough local evidence to verify a suspicious feature, fail rather than giving the benefit of the doubt.
5. Keep the report concise, but include enough detail to make the verification logic auditable.

## Output
Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then, for each exhibit, include:
  - the exhibit name as a section header
  - a short description of the exhibit
  - a `Suspicious features` subsection
  - if suspicious features exist, a `Code check` subsection explaining how they are generated and why the code is correct or incorrect
  - an exhibit verdict: PASS or FAIL with a short reason
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
