# Improvement Plan
AUTHOR PLAN — 2026-04-09 18:58:33 EDT

## Current State

17/25 tests pass. 8 failures across visual, writing, factual, and spec-compliance categories. No overhaul needed — the model section is sound. Focus is on fixing failing tests, then polishing.

## Failing Tests and Fixes

### 1. visual-pages (hyperref link boxes)
**Problem:** Colored hyperref boxes (red/green rectangles) visible around cross-references.
**Fix:** Add `\hypersetup{hidelinks}` after `\usepackage{hyperref}` in `paper.tex`.

### 2. spec-paper (long proof inline)
**Problem:** Proposition 1's proof (~28 lines) is inline, violating spec II.9 (long proofs go in appendix).
**Fix:** Move the Proposition 1 proof to a new appendix. Leave a one-line "See Appendix" note inline. Keep the short proofs (Corollary 1, Proposition 2) inline.

### 3. factcheck-freely (factual errors)
**Problem:** Three issues:
  - (a) Kogan, Papanikolaou, Stoffman (2020) — actual fourth author is Song, not Stoffman.
  - (b) Kogan & Papanikolaou (2014) described as introducing "displacement risk factor" — that concept originates in GKP (2012).
  - (c) Transfer model uses "income" and "surplus" inconsistently for AI owners' share.
**Fix:**
  - (a) Correct citation to Kogan, Papanikolaou, Schmidt, and Song (2020) in both `paper.tex` and `references.bib`.
  - (b) Reword the Kogan & Papanikolaou (2014) sentence to describe what they actually show (technology shocks create cross-sectional return differences), attributing "displacement risk" to GKP.
  - (c) Standardize on "surplus" throughout the transfer model section.

### 4. element-lit-review (too long)
**Problem:** Lit review spans ~75% of a page; spec says at most half a page.
**Fix:** Trim the lit review paragraph. Cut the Garleanu & Panageas (2015) and Acemoglu (2024) sentences — they are least central. Tighten remaining sentences. Target ~60% of current length.

### 5. writing-intro (flow and coverage)
**Problem:** (a) Spec arguments (c) "financial market solutions under-discussed" and (d) "singularity abundance overcomes frictions" are not prominent — buried in non-skimmable positions. (b) Abrupt transitions between paragraphs in second half of intro.
**Fix:**
  - Add a dedicated short paragraph after the hedging-motive paragraph that makes arguments (c) and (d) prominent and skimmable.
  - Smooth transitions: connect the extensions paragraph (P4→P5) with a bridging sentence; reorder quantitative preview before the meta-commentary paragraph; tighten the meta paragraph so it reads as a closing flourish, not a topic shift.

### 6. element-transfers-fig (catastrophe not visible at τ=0)
**Problem:** Panel (b) of the extension figure doesn't clearly show that zero transfers are catastrophic. The large-singularity line at τ=0 starts near the baseline, not visibly below 1.
**Fix:** In `code/generate-exhibits.R`, verify that consumption_growth at τ=0 for the large singularity is `phi_large*(1+eta_large) = 0.05*10 = 0.5`, i.e., consumption halves. This should already be the case. The visual problem may be the y-axis scale — the large-singularity curve rises so steeply that 0.5 looks close to the baseline. Fix: add a horizontal reference line at y=0.5 with an annotation like "50% consumption loss", or adjust the y-axis to start at 0 so the catastrophe is visually dramatic. Also ensure the "No change" annotation at y=1 is clear.

### 7. visual-figures-image-only (gridlines + wasted space)
**Problem:** (a) fig-ai-valuations has low-contrast light gray gridlines. (b) Extension panel (a) has wasted space — both curves flatten by 20% tax rate but x-axis goes to 70%.
**Fix:**
  - (a) In fig-ai-valuations: remove minor gridlines or darken them. Use `panel.grid.major = element_line(color = "gray70")`.
  - (b) In extension panel (a): truncate x-axis at ~40% tax rate (or wherever the curves have essentially flatlined). This concentrates visual information and eliminates dead space. Keep panel (b) x-axis at 70% since the large-singularity curve still has meaningful variation there.

### 8. visual-figures (text too small in Figure 2)
**Problem:** Axis labels, tick labels, and legend text in extension figure are too small.
**Fix:** Increase `base_size` in `theme_paper` from 12 to 14. Increase figure dimensions from 10×4.5 to 11×5 to accommodate larger text.

## Execution Order

1. **LaTeX quick fixes** (tests 1, 2): hyperref hidelinks, move proof to appendix.
2. **Factual corrections** (test 3): fix citations and terminology.
3. **Lit review trim** (test 4): cut to half-page.
4. **Intro rewrite** (test 5): restructure flow, make arguments (c)/(d) prominent.
5. **Figure fixes** (tests 6, 7, 8): update `generate-exhibits.R` for extension figure x-axis, text size, gridlines, and catastrophe visibility.
6. **Regenerate exhibits**, rebuild paper, re-run tests.
