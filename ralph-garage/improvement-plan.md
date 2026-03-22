# Improvement Plan

## Status: Targeted Fixes (No Overhaul Needed)

The paper is substantively complete: theory-correctness passes, the model is clean and well-differentiated from GKP, and all style/quality requirements are met. One test fails.

## Key Issues

1. **FAIL: spec-compliance (I.6)** — Figure 1 compares AI stocks to *non-AI stocks*. The spec requires comparison to the *market portfolio*. The market portfolio P/D ratio is $v^M = s \cdot v^A + (1-s) \cdot v^N$, a distinct object from $v^N$.

## Plan

### Fix 1: Add market portfolio curve to Figure 1 (fixes spec-compliance)

In `paper/paper.tex`, add a third curve to the figure for the market portfolio P/D ratio:
$$v^M = s \cdot v^A + (1-s) \cdot v^N$$

With $s = 0.15$, the plot formula is:
$$v^M(\lambda) = 0.15 \cdot v^A(\lambda) + 0.85 \cdot v^N(\lambda)$$

Using the existing plot expressions:
- $v^A(\lambda) = (0.92272 + 31.564\lambda) / (0.07728 + 0.92272\lambda)$
- $v^N(\lambda) = (0.92272 + 14.232\lambda) / (0.07728 + 0.92272\lambda)$

So: $v^M(\lambda) = (0.92272 + 16.832\lambda) / (0.07728 + 0.92272\lambda)$

(Numerator coefficient: $0.15 \times 31.564 + 0.85 \times 14.232 = 4.7346 + 12.0972 = 16.832$)

Steps:
- Add an `\addplot` for the market portfolio between the AI and non-AI curves, with a distinct style (e.g., black, dotted).
- Update the legend entry to "Market portfolio ($v^M$)".
- Update the caption to mention the market portfolio.
- Update the introductory text around the figure to reference the AI premium relative to the market portfolio, not just non-AI stocks.

### Fix 2: Update prose referencing the figure

The paragraph introducing Figure 1 (around line 43) describes the premium as the gap between AI and non-AI stock valuations. Adjust to frame as AI vs. market portfolio, consistent with the updated figure and the spec's intent.

## Test IDs

Non-referee: `ai-economics`, `build-latex`, `spec-compliance`, `theory-correctness`, `theory-elegance`, `visual-pages`, `writing-natural`

Referee: `referee-top3`, `cfr-r1`
