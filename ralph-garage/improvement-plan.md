# Improvement Plan
AUTHOR PLAN — 2026-04-12 14:16:22 EDT

## Current State

- **21/25 tests pass.** No model or theory failures. No overhaul needed.
- **4 failures** trace to exactly 2 issues.

## Issue 1: Figure 2 panel (b) title truncation (3 test failures)

**Tests:** `visual-figures-image-only`, `visual-figures`, `visual-pages`

**Problem:** Panel (b) title reads "HH Consumption Grow" — the word "Growth" is clipped at the right edge of the plot. The title `"(b) HH Consumption Growth"` is too long for the panel width at `base_size = 32`.

**Fix in `code/generate-exhibits.R`:** Shorten panel (b) title to `"(b) Consumption Growth"` (drop "HH"). The y-axis label already says "Household Consumption Growth in Singularity", so context is preserved.

## Issue 2: Introduction transitions P3→P4 and P4→P5 (1 test failure)

**Test:** `writing-intro`

**Problem:** P3 ends on extinction risk / Proposition 2. P4 pivots to AI development distortion (Proposition 3) with no bridge. P4 ends with a welfare claim; P5 opens with a meta-observation about financial market solutions being "under-discussed" — connection is implicit.

**Fix in `paper/paper.tex`:**
- Add a bridging opening to P4, e.g.: "Beyond valuations, incomplete markets may also distort the development of AI itself."
- Add a bridging sentence at the start of P5 that connects the veto problem to financial market solutions, e.g.: "These distortions call for market-based solutions, yet financial approaches to AI disaster risk are strikingly under-discussed..."

## Execution Order

1. Fix the figure title in R code, regenerate exhibits.
2. Fix the two paragraph transitions in the introduction.
3. Rebuild the paper PDF and page images, then rerun tests.
