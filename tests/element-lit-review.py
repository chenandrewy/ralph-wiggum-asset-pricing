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
finance paper cites the most relevant related work from the top finance and
economics journals and keeps the literature review appropriately concise.

Target journals (abbreviations used below):

  Finance:
    JF   = Journal of Finance
    JFE  = Journal of Financial Economics
    RFS  = Review of Financial Studies
    JFQA = Journal of Financial and Quantitative Analysis
    RAPS = Review of Asset Pricing Studies
    MS   = Management Science

  Economics:
    AER  = American Economic Review
    JPE  = Journal of Political Economy
    QJE  = Quarterly Journal of Economics
    ECMA = Econometrica
    REStud = Review of Economic Studies

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
- Identify the paper's PRIMARY topic — the central subject that the title,
  abstract, and main argument are about.
- Infer the minimum literature coverage needed to support those themes.
- Do NOT assume subtopics unless the paper or spec explicitly includes them.
- Also scan the paper text for specific claims, theorems, results, and
  frameworks that the paper invokes or relies on, even if they are not part
  of the paper's main themes. These in-text references are part of the
  evaluation scope: any named result or concept the paper uses needs a
  citation regardless of which journal it appeared in.

Step 4 — Build a candidate set of expected citations:
Using the paper, spec, and optional context, identify papers published in the
target journals that are highly relevant to the paper's actual stated themes.
Also include original sources for any specific results, theorems, or named
concepts identified in Step 3 that the paper invokes without citing.

Topic-proportionality rule: The candidate set must reflect the paper's topic
emphasis. If the paper is primarily about topic X, then papers about X in the
target journals should form the majority of your candidate set. Do not let
secondary themes (rare disasters, general incomplete-markets theory, etc.)
crowd out the primary topic. A paper with thin coverage of its own primary
topic fails even if secondary themes are well covered.

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
  - CRITICAL: A prominent paper in the target journals on the paper's PRIMARY
    topic that a specialist referee would expect to see cited. Also: any paper
    in the target journals that is directly on-point for a contribution claim
    the paper makes. Also: the original source for any named theorem, result,
    or concept that the paper invokes by name without citing (regardless of
    journal).
  - IMPORTANT: A well-known paper in the target journals on a secondary theme
    of the paper, or a literature review that is materially longer than half a
    page.
  - MINOR: A tangentially relevant paper whose omission is understandable given
    the paper's scope and length, or a literature review that is only marginally
    close to the half-page limit without clearly exceeding it.

Classification guidance:
  - Do NOT downgrade a gap from CRITICAL to IMPORTANT/MINOR just because the
    paper is "purely theoretical" or "does not engage with empirical work."
    A theory paper about topic X must still cite the landmark papers about X
    in the target journals, whether those papers are theoretical or empirical.
  - When in doubt about whether a gap is CRITICAL or IMPORTANT, ask: "Would a
    referee who specializes in the paper's primary topic flag this omission in
    their report?" If yes, it is CRITICAL.

Criteria:
  - To PASS, there must be NO critical gaps AND no more than one IMPORTANT gap.
  - The literature review must not clearly exceed half a page in the compiled
    paper.
  - If there are critical gaps, FAIL and list the missing papers with brief
    explanations of why they are essential.
  - If there are two or more IMPORTANT gaps, FAIL.
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
  4. Focus on the target journal set (finance and economics)
  5. Literature review length check
  6. Suggested additions (author, year, title, journal, and a one-sentence
     explanation of relevance)

In section 4, assess whether the literature review is appropriately focused on
relevant papers from the target journal set (both finance and economics). Do not
require that every listed journal appear in the bibliography or literature review.
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
