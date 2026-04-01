#!/usr/bin/env python3
"""
How to run: python tests/element-lit-review.py
Inputs: paper/paper.tex, paper/paper.pdf, paper/references.bib, spec/paper-spec.md, optional context from dev/journal and spec/lit/
Outputs: test-results/element-lit-review.md and process exit code (0=PASS, 1=FAIL)
"""

from __future__ import annotations

from _test_helpers import (
    build_test_context,
    require_page_images,
    require_paths,
    run_test,
)

AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"


def main() -> int:
    context = build_test_context(__file__)

    paper_path = context.repo_root / "paper/paper.tex"
    pdf_path = context.repo_root / "paper/paper.pdf"
    bib_path = context.repo_root / "paper/references.bib"
    spec_path = context.repo_root / "spec/paper-spec.md"
    report_source = context.repo_root / "spec/CFR-R1-report.md"
    journal_dir = context.repo_root / "dev/journal"
    lit_dir = context.repo_root / "spec/lit"
    page_images_dir = context.repo_root / "ralph-garage/page-images"

    preflight = require_paths(context, paper_path, pdf_path, bib_path, spec_path)
    if preflight is not None:
        return preflight

    page_image_check = require_page_images(context, page_images_dir)
    if page_image_check is not None:
        return page_image_check

    lit_files = []
    if lit_dir.is_dir():
        lit_files = sorted(f.name for f in lit_dir.iterdir() if f.is_file())
    lit_list = "\n".join(f"  - {name}" for name in lit_files) if lit_files else "  (none found)"

    journal_files = []
    if journal_dir.is_dir():
        journal_files = sorted(f.name for f in journal_dir.iterdir() if f.is_file())
    journal_list = "\n".join(f"  - {name}" for name in journal_files[:20]) if journal_files else "  (none found)"
    report_status = str(report_source) if report_source.exists() else "(not found)"

    prompt = f"""
You are a literature-review test agent. Your job is to check whether an academic
finance paper cites the most relevant related work from the top finance journals
and keeps the literature review appropriately concise.

Target journals (abbreviations used below):
  JF  = Journal of Finance
  JFE = Journal of Financial Economics
  RFS = Review of Financial Studies
  JFQA = Journal of Financial and Quantitative Analysis
  RAPS = Review of Asset Pricing Studies
  MS  = Management Science

Step 1 — Read the paper and bibliography:
  Paper source: {paper_path}
  Paper PDF: {pdf_path}
  Bibliography: {bib_path}
  Spec: {spec_path}

Step 2 — Read additional context files if they exist:
  Referee report: {report_status}
  Optional journal notes directory: {journal_dir}
  Optional literature directory: {lit_dir}

Step 3 — Derive evaluation scope from the spec and paper:
- Extract the paper's required research questions, theoretical focus, and
  contribution claims from the spec.
- Infer the minimum literature coverage needed to support those themes.
- Do NOT assume subtopics unless the paper or spec explicitly includes them.

Step 4 — Build a candidate set of expected citations:
Using the paper, spec, and optional context, identify papers published in the
target journals (JF, JFE, RFS, JFQA, RAPS, MS) that are highly relevant to the
paper's actual stated themes.

For each theme, identify important papers a referee would reasonably expect to
see cited. Search the web to broaden coverage and reduce omissions, but keep the
focus on likely relevant papers from the target journals.

Step 5 — Compare against the paper's current bibliography. For each paper you
identified, check whether it (or a close substitute covering the same idea) is
already cited.

Step 6 — Evaluate literature-review length:
- The spec requires the literature review to be at most half a page.
- Use the paper PDF and rendered page images under {page_images_dir} to judge
  whether the literature review as presented to a reader exceeds half a page.
- Evaluate the visible lit-review discussion in the compiled paper, not just the
  raw LaTeX source.

Step 7 — Assess adequacy. Classify each issue as:
  - CRITICAL: A highly influential paper in the target journals directly on the
    paper's core stated topics that any referee would flag as missing.
  - IMPORTANT: A well-known paper in the target journals on a closely related
    topic that strengthens the literature positioning, or a literature review
    that is materially longer than half a page.
  - MINOR: A relevant paper whose omission is understandable given the paper's
    scope and length, or a literature review that is only marginally close to
    the half-page limit without clearly exceeding it.

Criteria:
  - To PASS, there must be NO critical gaps.
  - The literature review must not clearly exceed half a page in the compiled
    paper.
  - A small number of IMPORTANT citation gaps is acceptable for a PASS if the
    paper's existing citations adequately cover the core themes.
  - If there are critical gaps, FAIL and list the missing papers with brief
    explanations of why they are essential.
  - If the lit review clearly exceeds half a page, FAIL.

Search guidance:
  - Search the web to expand the candidate set of relevant papers and reduce the
    risk of missing obvious related work.
  - This test is about literature coverage, not bibliographic accuracy.
  - You may use external sources to discover relevant papers, but do not turn
    uncertain metadata into the main issue here; focus on whether the paper is
    missing likely important references.

Files available in spec/lit/ for additional context:
{lit_list}

Files available in dev/journal/ for optional context:
{journal_list}

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence
- Then sections:
  1. Scope extracted from spec and paper
  2. Current bibliography summary (what the paper already cites)
  3. Missing references by topic area (with gap classification)
  4. Focus on the target journal set (JF, JFE, RFS, JFQA, RAPS, MS)
  5. Literature review length check
  6. Suggested additions (author, year, title, journal, and a one-sentence
     explanation of relevance)

In section 4, assess whether the literature review is appropriately focused on
relevant papers from the target journal set. Do not require that every listed
journal appear in the bibliography or literature review.
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
