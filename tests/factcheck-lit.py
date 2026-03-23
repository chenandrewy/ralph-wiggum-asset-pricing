#!/usr/bin/env python3
"""
How to run: python tests/factcheck-lit.py
Inputs: paper/paper.tex, paper/references.bib
Outputs: test-results/factcheck-lit.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import build_test_context, require_paths, run_test


AGENT = "claude"
MODEL = "opus"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    bib_path = context.repo_root / "paper/references.bib"
    preflight = require_paths(context, paper_path, bib_path)
    if preflight is not None:
        return preflight

    prompt = f"""
You are a strict citation-audit test agent reviewing an academic finance paper.

Read the canonical paper at: {paper_path}
Read the bibliography at: {bib_path}

Your job is to verify that the citations used in the paper are accurate.

You must use external verification sources when needed, prioritizing publisher pages, DOI landing pages, journal pages, Crossref, Google Scholar, SSRN, and author pages.

Scope:
- Audit every work that is actually cited in the paper text, including footnotes.
- Ignore bibliography entries that are never cited.

For each cited work, verify:
1. Bibliographic metadata accuracy:
   - author names
   - publication year
   - title
   - journal, outlet, or working-paper series
2. Citation-to-claim accuracy:
   - whether the surrounding text describes the cited work fairly
   - whether the citation is being used for a claim the cited work actually supports
3. Source quality:
   - prefer the published version when available
   - use working-paper versions only when appropriate and clearly matching the cited work

Severity rules:
- CRITICAL:
  - wrong paper matched to a citation key
  - materially wrong author list, year, title, or outlet
  - in-text description attributes a result, mechanism, or comparison that the cited work does not support
- IMPORTANT:
  - real metadata errors that need correction
  - noticeable but not fatal overstatement or mischaracterization
- MINOR:
  - cosmetic formatting issues or harmless inconsistencies

Pass/fail standard:
- PASS only if there are no CRITICAL problems and no pattern of IMPORTANT errors.
- FAIL if any CRITICAL issue exists, or if multiple IMPORTANT issues make the citation apparatus unreliable.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then sections:
  1. Citation inventory audited
  2. Metadata accuracy findings
  3. In-text description accuracy findings
  4. Flagged issues by citation key and severity
  5. Overall reliability of the paper's citations
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
