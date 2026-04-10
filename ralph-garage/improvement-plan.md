# Improvement Plan
AUTHOR PLAN — 2026-04-09 21:59:47 EDT

## Current State

21/25 tests pass. No section needs an overhaul. The model, proofs, and quantitative analysis are verified correct. Four tests fail on discrete, fixable issues.

## Failing Tests

| Test | Issue |
|------|-------|
| `factcheck-exhibits` | Figure 2 Panel (a) uses approximate P/D formula (`compute_pd_with_transfer`) that overstates AI P/D by ~11% vs the exact backward-recursion (`compute_pd_ai_exact`) used in Table 1. At p=0.5%, ξ=5%: approximate gives ~16.7, exact gives ~15.0. |
| `factcheck-lit` | (1) `AghionJonesJones2019` bib entry: pages should be 237–290 not 237–282, and type should be `@incollection` with `booktitle`/`publisher` fields. (2) `Acemoglu2024` now published in *Economic Policy* (2025, vol 40, pp 13–58); should cite published version. |
| `visual-figures-image-only` | `fig-ai-valuations` grid lines are light gray, failing contrast requirement. |
| `writing-intro` | (1) "Financial markets under-discussed" claim buried mid-paragraph, invisible to skimmers. (2) Paragraph 2 overloaded with 5 new concepts. (3) Redundant pivot sentences in paragraph 4. |

## Plan

### 1. Fix Figure 2 P/D computation (code + paper)

**Code (`code/generate-exhibits.R`):** Replace `compute_pd_with_transfer` with an exact backward-recursion version that mirrors `compute_pd_ai_exact` but incorporates `phi_eff` from transfers. The new function should:
- Build the theta chain as in `compute_pd_ai_exact`
- At each step, compute `phi_eff` from the transfer parameters
- Use `phi_eff` in place of `phi` for the SDF calculation
- Return NA when the existence condition fails

This ensures Figure 2 Panel (a) baseline P/D matches Table 1 at the same parameters.

**Paper (`paper/paper.tex`):** No text changes needed if the code fix makes the figures consistent. The existing disclosure about approximate vs exact methods in Section 2.2 already covers this.

### 2. Fix bibliography entries (paper)

**`paper/references.bib`:**
- `AghionJonesJones2019`: Change `@article` to `@incollection`, replace `journal` with `booktitle = {The Economics of Artificial Intelligence: An Agenda}` and add `publisher = {University of Chicago Press}`, fix pages to `237--290`.
- `Acemoglu2024`: Update to published version: `journal = {Economic Policy}`, `volume = {40}`, `number = {121}`, `pages = {13--58}`, `year = {2025}`.

### 3. Fix Figure 1 grid line contrast (code)

**Code (`code/generate-exhibits.R`):** In the `fig_val` plot for `fig-ai-valuations.pdf`, the plot currently inherits `theme_paper` which sets `panel.grid.major = element_line(color = "gray75")`. Override with darker grid lines (e.g., `"gray50"`) or remove grid lines entirely for this figure. Adding `panel.grid.major = element_line(color = "gray50")` to the figure's theme should suffice.

### 4. Restructure introduction paragraphs (paper)

**`paper/paper.tex`, Section 1:**

(a) **Surface the "under-discussed" claim.** Move "the role of financial markets remains under-explored" to the first or last sentence of a paragraph so skimmers see it.

(b) **Break up paragraph 2.** Current paragraph 2 introduces: (i) the thesis, (ii) "negative AI singularity" definition, (iii) market incompleteness, (iv) restricted equity distinction, (v) hedging mechanism. Split into two paragraphs: one for the thesis + hedging motive + under-discussed framing, another for the model's mechanism (singularity definition, incomplete markets, restricted equity).

(c) **Cut redundant pivot in paragraph 4.** "The same incomplete markets that inflate AI valuations also distort real decisions. Market incompleteness distorts the development of AI itself." — delete one of these two sentences.
