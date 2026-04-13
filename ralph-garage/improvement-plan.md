# Improvement Plan
AUTHOR PLAN — 2026-04-12 20:10:07 EDT

## Current State

- **Tests**: 24/25 pass. One failure: `visual-figures-image-only`.
- **Model section**: Sound. No overhaul needed.
- **Referee feedback (CFR-R1)**: Addressed by the extensions section (veto + transfers).

## Issues

### 1. Failing test: `visual-figures-image-only`

`fig-extension-panels` fails on two visual defects:

**(a) Panel (b) x-axis tick labels are cramped and overlapping.**
The current code uses `breaks = seq(0, 0.50, by = 0.10)`, producing 6 tick labels (0%, 10%, 20%, 30%, 40%, 50%) in a narrow half-width panel at base_size 32. The labels collide.

**(b) Shared legend entries run together without spacing.**
`legend.spacing.x = unit(1, "cm")` is insufficient at the current font sizes; the two legend items appear as one garbled string.

### 2. Grid line contrast (noted but not failing)

The test flagged Panel (a) grid lines as "distractingly bold" (`panel.grid.major = element_line(color = "gray40")`). This is a marginal pass but worth softening.

## Plan

### Step 1: Fix fig-extension-panels visual issues (code/generate-exhibits.R)

1. **Reduce Panel (b) x-axis tick density**: Change `by = 0.10` to `by = 0.20` so only 3 ticks appear (0%, 20%, 40%) — or use `breaks = c(0, 0.10, 0.30, 0.50)` for better coverage without crowding.
2. **Increase legend spacing**: Raise `legend.spacing.x` to `unit(2, "cm")` or more, and/or add `legend.key.width = unit(2.5, "cm")` to give each entry breathing room.
3. **Soften grid lines**: Change `gray40` to `gray70` or `gray75` in `theme_paper` so data lines dominate.

### Step 2: Rebuild exhibits and verify

Run `Rscript code/generate-exhibits.R`, recompile the paper, regenerate page images, and re-run the failing test to confirm it passes.
