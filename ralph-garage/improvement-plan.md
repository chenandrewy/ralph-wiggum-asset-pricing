# Improvement Plan
AUTHOR PLAN — 2026-04-12 09:57:08 EDT

## Current State

- **21/25 tests pass.** No section needs an overhaul.
- **4 failing tests** are the priority. All are localized fixes.

## Failing Tests

### 1. `factcheck-lit` — Jones (2024) misattribution in introduction

**Problem:** Line 57 of `paper.tex` says "As \citet{Jones2024} models, a singularity can produce output growth so large that even grossly inefficient transfers become effective, because the resource base overwhelms the deadweight costs." Jones (2024) models explosive growth and existential risk but does not discuss transfers or deadweight costs. The transfers mechanism is this paper's contribution.

**Fix:** Rewrite to attribute only the explosive-growth modeling to Jones:
> "If a singularity produces the kind of explosive output growth modeled by \citet{Jones2024}, even grossly inefficient transfers become effective, because the resource base overwhelms the deadweight costs."

This matches the more accurate attribution already used in Section 4.2.

### 2. `visual-figures-image-only` — Fig 1 Panel (b) y-axis label clipped

**Problem:** The y-axis label "NASDAQ / S&P 500 Price Ratio\n(Jan 2015 = 100)" is truncated at the left margin, rendering as "ASDAQ / S&P 500 Price Rati".

**Fix:** In `code/generate-exhibits.R`, increase the left margin for `panel_val_b` (e.g., `l = 20` or higher in `plot.margin`) or shorten the y-axis label (e.g., "NASDAQ / S&P 500\n(Jan 2015 = 100)").

### 3. `visual-figures` — Fig 2 (extension panels) text too small

**Problem:** Axis labels, tick labels, and legend text in `fig-extension-panels.pdf` are below comfortable reading size.

**Fix:** In `code/generate-exhibits.R`, the extension figure already uses `base_size = 28` in `theme_paper`. The issue is likely the output dimensions (`width = 16, height = 9`) combined with the text sizes. Increase `base_size` to ~32, or reduce the output width to ~14 to make text proportionally larger. Also increase `legend.text` and `axis.text` sizes in the theme.

### 4. `writing-intro` — Complete-markets counterfactual buried

**Problem:** The complete-markets counterfactual ("if markets are complete, there would be no need to hedge") appears only as the final clause of paragraph 3, not as a topic sentence. A skimming reader may miss it.

**Fix:** Add a standalone sentence to the summary paragraph (paragraph 7, line 59 area) that states the complete-markets counterfactual clearly, e.g.: "Market incompleteness is the key driver: under complete markets, the displacement-driven premium would largely vanish." Alternatively, make it a topic sentence in paragraph 3.

## Execution Order

1. Fix the Jones (2024) misattribution (paper.tex, one sentence).
2. Fix the writing-intro issue (paper.tex, add one sentence to summary paragraph).
3. Fix the fig-ai-valuations clipping (generate-exhibits.R, adjust margin or label).
4. Fix the fig-extension-panels text size (generate-exhibits.R, adjust theme sizes).
5. Regenerate exhibits (`Rscript code/generate-exhibits.R`).
6. Rebuild PDF and verify.
