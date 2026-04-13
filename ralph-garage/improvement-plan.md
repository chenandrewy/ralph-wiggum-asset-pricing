# Improvement Plan
AUTHOR PLAN — 2026-04-12 20:22:00 EDT

## Current State

- **Tests**: 23/25 pass. Two failures: `visual-figures-image-only`, `writing-intro`.
- **Model**: No overhaul needed. Theory fact-checks pass clean (notation, assumptions, traceability, arithmetic). Code matches paper.
- **Referees**: Disabled; no referee outputs in summary.

## Failing Tests

### 1. `visual-figures-image-only` (FAIL)

**fig-ai-valuations issues:**
- X-axis tick labels cramped in both panels (5-year breaks at 28pt on ~6-inch panels).
- Panel (b) title truncated: "(b) NASDAQ vs. S&P 5" instead of "(b) NASDAQ vs. S&P 500".

**fig-extension-panels issues:**
- Shared legend truncated (closing parenthesis and parameter value cut off).
- Grid lines in both panels are light gray with insufficient contrast.

**Fix (code/generate-exhibits.R):**
- fig-ai-valuations: Reduce x-axis tick label size (e.g., `axis.text.x = element_text(size = 22)`). Shorten panel (b) title or reduce title font size to prevent truncation.
- fig-extension-panels: Increase legend text wrapping or reduce legend text size to prevent truncation. Darken grid lines further (already `gray75`; try `gray55` or darker).

### 2. `writing-intro` (FAIL)

**Issues:**
- P3->P4 transition: P3 closes on extinction-risk nuance, P4 jumps to development distortions without bridging.
- P6->P7 transition: P6 and P7 opening say nearly the same thing, creating redundancy that stalls momentum.

**Fix (paper/paper.tex):**
- P3->P4: Add a bridging sentence at end of P3 or start of P4 connecting the extinction discussion to the broader incomplete-markets theme before pivoting to real distortions.
- P6->P7: Rewrite P7 opening to avoid repeating P6's closing. Go directly to the roadmap without restating the "growth creates and resolves the problem" line.

## Passing Tests with Actionable Suggestions

### 3. `theory-clarity` (PASS, with suggestion)

The AI dividend share update rule $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ is currently in a bullet point. This is the single expression driving $\Gamma^{AI} \neq \Gamma^{N}$ and therefore the entire valuation spread. Elevate it to a numbered display equation.

## Execution Order

1. Fix fig-ai-valuations (code change: tick labels, panel title).
2. Fix fig-extension-panels (code change: legend truncation, grid contrast).
3. Fix P3->P4 and P6->P7 intro transitions (paper change).
4. Elevate theta update rule to display math (paper change).
