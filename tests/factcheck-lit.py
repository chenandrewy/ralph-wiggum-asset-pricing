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
EFFORT = "medium"
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

## Procedure
1. Audit only the listed citation keys.
2. Verify each listed citation key using external web sources.
3. Use local paper text only to identify how the citation is used.
4. Use external sources for factual judgments about the cited work.
5. Record, for each listed key, whether it is VERIFIED or UNVERIFIED and list the external source or sources used.
6. Record every metadata issue, claim-support issue, source-quality issue, and verification gap that bears on the requirements.
7. Return only the audit results for these keys. Do not write files.

## Requirements
1. Every listed citation key is externally verified or else remains explicitly UNVERIFIED.
2. The bibliographic metadata for each listed citation key is materially accurate.
3. The paper's in-text use of each listed citation key is materially accurate and supported by the cited work.
4. Every IMPORTANT or CRITICAL issue is supported by external sources.
5. A concern that lacks adequate external support is not treated as an error.

### Guidelines
1. Do not use memory, training data, guessing, or silent fallback to prior knowledge for factual judgments about cited works.
2. Preferred sources are publisher pages, DOI landing pages, journal pages, Crossref, Google Scholar, SSRN, and author pages.
3. If web tools are unavailable, or if a listed key cannot be verified externally, leave it UNVERIFIED rather than guessing.

For each citation key, report:
- key
- VERIFIED or UNVERIFIED
- external sources used
- metadata verdict
- in-text claim-support verdict
- any issue severity: CRITICAL, IMPORTANT, MINOR, or NONE
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

## Procedure
1. Launch one subagent per citation batch below using model "opus".
2. Do not ask subagents to write files; collect their results and own the final verdict yourself.
3. Audit every work that is actually cited in the paper text, including footnotes.
4. Ignore bibliography entries that are never cited.
5. Be exhaustive. Do not use sampling.
6. Do not omit any cited key; all cited keys in the paper are included in the batched subagent tasks above.
7. For each cited work, verify:
   - Bibliographic metadata accuracy:
     - author names
     - publication year
     - title
     - journal, outlet, or working-paper series
   - Citation-to-claim accuracy:
     - whether the surrounding text describes the cited work fairly
     - whether the citation is being used for a claim the cited work actually supports
   - Source quality:
     - prefer the published version when available
     - use working-paper versions only when appropriate and clearly matching the cited work
8. Record, for each cited work, whether it is VERIFIED or UNVERIFIED and list the external source or sources used.
9. Record every metadata error, claim-support problem, source-quality problem, and verification gap that bears on the requirements.

## Requirements
1. External verification is required for this test.
2. Every cited work is externally verified or else remains explicitly UNVERIFIED.
3. The paper's bibliographic metadata for each cited work is materially accurate.
4. The paper's in-text description of each cited work is materially accurate and supported by that work.
5. Every CRITICAL or IMPORTANT finding is supported by external sources.
6. A concern that lacks adequate external support is not treated as an error.

### Guidelines
1. Use external sources for all factual judgments about the cited work itself.
2. Do not use memory, training data, guessing, or silent fallback to prior knowledge for factual judgments about cited works.
3. Preferred sources are publisher pages, DOI landing pages, journal pages, Crossref, Google Scholar, SSRN, and author pages.
4. If web search or external fetch tools are unavailable, or if there is not enough external evidence to verify every cited work, treat that as a failure to satisfy Requirement 2 rather than guessing.
5. Use local paper text only to identify the citation key, the surrounding claim, and the paper's description of the cited work.
6. Use source matches of sufficient quality to identify the cited work correctly before making factual judgments about it.
7. If the external sources are insufficient to verify a claim about the cited work, leave that item UNVERIFIED rather than calling it wrong.
8. Severity rules are as follows:
   - CRITICAL:
     - wrong paper matched to a citation key
     - materially wrong author list, year, title, or outlet
     - in-text description attributes a result, mechanism, or comparison that the cited work does not support
   - IMPORTANT:
     - real metadata errors that need correction
     - noticeable but not fatal overstatement or mischaracterization
   - MINOR:
     - cosmetic formatting issues or harmless inconsistencies

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
        default_agent_effort=EFFORT,
        default_agent_log_mode="verbose",
    )


if __name__ == "__main__":
    raise SystemExit(main())
