# Improvement Plan
AUTHOR PLAN — 2026-04-09 21:43:47 EDT

## Current State

- 21/25 tests pass. 4 failures: `factcheck-bysection`, `visual-figures-image-only`, `visual-pages`, `writing-intro`.
- No model overhaul needed. The model section is sound (all theory tests pass). The main issue is a factual claim about approximation accuracy and presentation/writing polish.

---

## Priority 1: Fix approximation-error claim (`factcheck-bysection`)

**Problem:** Line 149 of `paper.tex` claims "the approximation error is small" for Δθ = 0.2, but independent recomputation shows ~12% error on AI P/D and ~41% error on the valuation spread. This is the only factual error flagged.

**Fix (code + paper):**
1. In `code/generate-exhibits.R`, compute **exact** P/D ratios via numerical value-function iteration over a grid of θ values (θ changes with each singularity, so iterate until convergence). Use exact values in the table.
2. Keep the closed-form Proposition 1 as an **intuition-building approximation**. It stays in the paper for its economic transparency.
3. Update line 149 to honestly characterize the approximation: state that the closed-form is an approximation used for intuition, and that Table 1 reports numerically exact P/D ratios computed by iterating the Euler equation. Remove the claim that the error is "small."
4. Add a brief note in the Appendix A proof (around line 299) that the table values are computed numerically without the approximation.

---

## Priority 2: Fix figure visual defects (`visual-figures-image-only`)

**Problem:** Two figure issues:
- `fig-ai-valuations`: y-axis label clipped at top; grid lines too dark (gray20).
- `fig-extension-panels`: Panel (a) has ~33% wasted vertical headroom above data; Panel (b) "No change" reference line too thin/low-contrast.

**Fix (code):**
1. In `theme_paper`, change `panel.grid.major` color from `"gray20"` to `"gray75"` (lighter grid).
2. For `fig-ai-valuations`, increase top margin in `plot.margin` to prevent y-axis label clipping.
3. For Panel (a), tighten `y_cap_a` from 19 to closer to the data max (~17) plus ~10-15% headroom.
4. For Panel (b), increase the "No change" reference line weight from `linewidth = 1.2` to ~1.5 and darken it (use `"gray30"` or `"black"`).

---

## Priority 3: Fix page 8 layout waste (`visual-pages`)

**Problem:** Discussion subsection (2.3) ends early on page 8, leaving most of the page blank before Section 3 starts on page 9 (likely due to `[H]` float placement on Table 1).

**Fix (paper):**
1. Change Table 1 float specifier from `[H]` to `[t]` or `[ht]` to let LaTeX place it more flexibly. Or remove the `\clearpage` if one exists before Section 3.
2. If the table still forces a page break, consider moving the table into the text flow (after the first paragraph of Section 3 that references it) so that prose fills page 8.

---

## Priority 4: Fix introduction flow (`writing-intro`)

**Problem:** Three structural issues:
- (a) Hedging claim in P2 doesn't distinguish the *negative* singularity clearly enough when first introduced.
- (b) P3 re-motivates after the mechanism is already stated in P2, stalling momentum.
- (c) AI-authorship paragraph (P7) breaks the arc between economic argument and lit review.

**Fix (paper):**
1. **P2:** When first stating the hedging claim, explicitly say "negative AI singularity" (not just "AI singularity") so that skimming readers immediately grasp that the hedge is against the downside.
2. **P3 restructure:** Merge the motivation material (financial markets under-explored) into P2 as a lead-in sentence, so P3 can go straight to GKP's framework and the model description without re-motivating.
3. **P5→P6 transition:** Add a bridging sentence at the end of P4 or start of P5 connecting pricing results to development decisions (e.g., "The same incomplete markets that inflate AI valuations also distort real decisions").
4. **P7 (AI-authorship):** Condense to 1-2 sentences and fold into P6 or make it a footnote, so the introduction flows directly from the economic argument into the lit review without a detour.
5. **Argument (d):** In the transfers paragraph (P6), add an explicit sentence about market frictions being overcome by abundance of resources, not just about government transfers being effective.
