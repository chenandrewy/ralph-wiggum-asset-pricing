#!/usr/bin/env python3
"""
How to run: python tests/factcheck-lit.py
Inputs: paper/paper.tex, paper/references.bib
Outputs: test-results/factcheck-lit.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

import re

from _test_helpers import build_test_context, fail_test, require_paths, run_test


AGENT = "claude"
MODEL = "opus"
KEYS_PER_BATCH = 8


def extract_citation_keys(tex: str) -> list[str]:
    pattern = re.compile(r"\\cite[a-zA-Z*]*?(?:\[[^\]]*\])?(?:\[[^\]]*\])?\{([^}]+)\}")
    keys: list[str] = []
    seen: set[str] = set()
    for match in pattern.finditer(tex):
        raw_group = match.group(1)
        for raw_key in raw_group.split(","):
            key = raw_key.strip()
            if key and key not in seen:
                seen.add(key)
                keys.append(key)
    return keys


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    bib_path = context.repo_root / "paper/references.bib"
    preflight = require_paths(context, paper_path, bib_path)
    if preflight is not None:
        return preflight

    citation_keys = extract_citation_keys(paper_path.read_text(encoding="utf-8"))
    if not citation_keys:
        return fail_test(context, "no cited works found in paper.tex")

    batches = []
    for i in range(0, len(citation_keys), KEYS_PER_BATCH):
        chunk = citation_keys[i : i + KEYS_PER_BATCH]
        label = f"Batch {len(batches) + 1}: {chunk[0]} to {chunk[-1]}"
        key_list = "\n".join(f"- {key}" for key in chunk)
        sub_prompt = f"""\
Read the canonical paper at: {paper_path}
Read the bibliography at: {bib_path}

Audit only the following citation keys:
{key_list}

Requirements:
- Verify every listed citation key using external web sources.
- Do not rely on memory or training data.
- If web tools are unavailable, or if any listed key cannot be verified externally, mark it UNVERIFIED.
- Prefer publisher pages, DOI landing pages, journal pages, Crossref, Google Scholar, SSRN, and author pages.
- Use local paper text only to identify how the citation is used; use external sources for factual judgments about the cited work.
- Every IMPORTANT or CRITICAL issue must name the external source that supports it.
- If a concern is not externally supported, do not report it as an error.

For each citation key, report:
- key
- VERIFIED or UNVERIFIED
- external sources used
- metadata verdict
- in-text claim-support verdict
- any issue severity: CRITICAL, IMPORTANT, MINOR, or NONE

Do not write files. Return only the audit results for these keys.\
"""
        batches.append({"label": label, "sub_prompt": sub_prompt})

    sub_agent_block = "\n\n".join(
        f"### {batch['label']}\n```\n{batch['sub_prompt']}\n```" for batch in batches
    )

    prompt = f"""
You are a strict citation-audit test agent reviewing an academic finance paper.

Read the canonical paper at: {paper_path}
Read the bibliography at: {bib_path}

Your job is to verify that the citations used in the paper are accurate.

You must use a staged subagent workflow. Launch one subagent per citation batch below. Use model "opus" for each subagent. Subagents must not write files; they report back to you, and you own the final verdict.

{sub_agent_block}

External verification is required for this test. Do not rely on memory or training data for factual judgments about cited works. Prioritize publisher pages, DOI landing pages, journal pages, Crossref, Google Scholar, SSRN, and author pages.

If web search or external fetch tools are unavailable, or if you cannot find enough external evidence to verify every cited work, FAIL the test. Do not guess, hallucinate, or silently fall back to prior knowledge.

Scope:
- Audit every work that is actually cited in the paper text, including footnotes.
- Ignore bibliography entries that are never cited.
- Exhaustiveness is required. Do not use sampling.
- All cited keys in the paper are included in the batched subagent tasks above. Do not omit any key.

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

Evidence rules:
- Every cited work must include an external verification status: VERIFIED or UNVERIFIED.
- Every CRITICAL or IMPORTANT finding must name the external source or sources that support it.
- If a concern is not supported by an external source, do not report it as an error.
- If the external sources are insufficient to verify a claim about the cited work, mark that item UNVERIFIED rather than WRONG.
- Use local paper text only to identify the citation key, the surrounding claim, and the paper's description of the cited work. Use external sources for all factual judgments about the cited work itself.

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
- PASS only if every cited work is externally verified.
- PASS only if there are no CRITICAL problems and no pattern of IMPORTANT errors.
- FAIL if any cited work is left UNVERIFIED.
- FAIL if any CRITICAL issue exists, or if multiple IMPORTANT issues make the citation apparatus unreliable.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then sections:
  1. Citation inventory audited
  2. External verification coverage
  3. Metadata accuracy findings
  4. In-text description accuracy findings
  5. Flagged issues by citation key and severity
  6. Overall reliability of the paper's citations

In section 2, list every cited work and label it VERIFIED or UNVERIFIED, with the external source(s) used.
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
