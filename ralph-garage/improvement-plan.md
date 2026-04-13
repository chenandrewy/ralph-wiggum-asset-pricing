# Improvement Plan
AUTHOR PLAN — 2026-04-12 19:58:22 EDT

## Status Summary

- **Tests:** 21 pass, 4 fail
- **Failing tests:** `visual-figures-image-only`, `visual-figures`, `visual-pages`, `writing-intro`
- **No overhaul needed.** All theory tests pass. Proofs are correct. Model section is sound.

## Issues and Fixes

### Priority 1: Fix failing tests

**A. fig-extension-panels visual defects (3 tests)**

All three visual test failures stem from the same figure: `fig-extension-panels.pdf`.

Defects:
1. Panel (b) title truncated at "Consumption Grow" — the title string is too long for the plot area.
2. Shared legend entries run together with no spacing between them.
3. Panel (b) x-axis tick labels are cramped.

Fix in `code/generate-exhibits.R`:
- Shorten Panel (b) title. Current: `"(b) Consumption Growth"`. The `plot.title` text size is 31 and the panel is half the figure width, causing truncation. Either shorten the title (e.g., `"(b) Cons. Growth in Singularity"` is worse; better: just reduce title font or use `"\n"`) or reduce `base_size`/`plot.title` size for this figure. Simplest fix: shorten to `"(b) Cons. Growth in Singularity"` or abbreviate, but cleaner: reduce `plot.title` size to ~26 so the full title fits.
- Add spacing between legend entries: add `legend.spacing.x = unit(1, "cm")` or similar to `theme_paper`.
- Fix cramped x-axis: use `scale_x_continuous(breaks = seq(0, 0.50, by = 0.10), ...)` to reduce the number of tick marks, or increase `axis.text` spacing.

After fixing code, regenerate the figure with `Rscript code/generate-exhibits.R`, then recompile the paper.

**B. writing-intro: Complete-markets counterfactual missing from skimmable position**

The introduction explains that markets are incomplete but never states the counterfactual — that complete markets would eliminate the premium. The word "complete" does not appear in the introduction.

Fix in `paper/paper.tex`, paragraph P2 (line 49): Add a clause making the complete-markets benchmark explicit. The test suggests appending to the hedging-channel sentence something like: "...pushing valuations above those of non-AI stocks — a premium that would vanish if markets were complete."

### Priority 2: Presentation improvements (from passing tests with notes)

**C. Delta parameter inconsistency (factcheck-bysection note)**

The in-text numerical example (line 261) uses $\delta = 0.9$ to show that even grossly inefficient transfers work, but the figure caption (line 269) and code use $\delta = 0.5$. This is not wrong (they are different parameterizations) but could confuse readers.

Fix: Add a brief clarifying phrase to the text, e.g., "To illustrate the robustness to even more severe waste, raising the deadweight cost parameter to $\delta = 0.9$ (compared with the $\delta = 0.5$ used in Figure 2)..." — making explicit that this is a separate, more extreme parameterization.

## Execution Order

1. Fix `code/generate-exhibits.R` for Panel (b) title, legend spacing, and x-axis ticks.
2. Run `Rscript code/generate-exhibits.R` to regenerate figures.
3. Edit `paper/paper.tex` P2 to add complete-markets counterfactual.
4. Edit `paper/paper.tex` Extension 2 text to clarify delta inconsistency.
5. Recompile paper PDF.
