# Improvement Plan
AUTHOR PLAN — 2026-04-11 21:39:31 EDT

## Current State

- **22/25 tests pass.** 3 failures: `spec-paper`, `visual-figures`, `writing-intro`.
- Model section, proofs, code, and all factchecks pass. No overhaul needed.

## Failing Tests

### 1. `spec-paper` — Missing "under-discussed" claim (I.3c)

**Problem:** Spec requires the paper to argue that "financial market solutions to AI disaster risk are under-discussed." The paper says the natural fix is *blocked* but never says financial market solutions are *under-discussed* in the literature or policy discourse.

**Fix:** Add a sentence in the introduction (paragraph 4 or 5, near the "natural fix" discussion) explicitly stating that financial market solutions to AI disaster risk are under-discussed relative to regulatory approaches, even though frictions limit their effectiveness. One sentence suffices — e.g., noting that discussion of AI risk focuses on regulation and alignment while financial hedging mechanisms receive little attention.

### 2. `visual-figures` — Figure 2 readability and distinguishability

**Problem:** `fig-extension-panels.pdf` (Exhibit 3) fails on:
- Axis labels too small in both panels
- Legend text too small
- Panel (a) has 5 series in similar styles that are hard to distinguish

**Fix in `code/generate-exhibits.R`:**
- The figure currently has only 2 scenarios (Baseline and Large singularity), so the "5 series" complaint likely stems from the legend rendering or visual complexity of annotations. Increase `base_size` in `theme_paper` from 22 to something larger, or more precisely:
  - Increase axis title font size (currently 20 → 22+)
  - Increase axis text / tick label size (currently 18 → 20+)
  - Increase legend text size (currently 18 → 20+)
  - Ensure only 2 series are plotted in Panel (a) with clearly distinct colors and line styles (already dark red vs. dark blue, solid vs. longdash — verify this renders cleanly)
- Increase figure output dimensions if needed (`width = 14, height = 8` instead of `12, 7`)
- Rebuild exhibits and recompile PDF

### 3. `writing-intro` — Skimmability and promise fulfillment

**Problem A:** Arguments (c), (d), (e) from the spec are not in first sentences of their paragraphs:
- **(c)** "Financial market solutions under-discussed" — absent entirely (overlaps with spec-paper fix above)
- **(d)** "Singularity overcomes frictions" — buried mid-paragraph 5, not in the first sentence
- **(e)** "Incomplete markets distort AI development" — second sentence of paragraph 4

**Fix A:** Restructure introduction paragraphs so each of the 5 spec arguments leads its own paragraph's first sentence:
- Current ¶4 starts with complete markets / incompleteness (argument b), then buries (e) in sentence 2. Split: give (e) its own paragraph or promote it to lead.
- Current ¶5 opens with the natural fix being blocked, then gets to (d) mid-paragraph. Restructure so (d) — "singularity growth overcomes frictions" — leads or is very near the top.
- Add (c) — "financial market solutions are under-discussed" — as a distinct first-sentence claim (this also fixes spec-paper).

**Problem B:** Promise 7 — "even grossly inefficient transfers become effective" is under-delivered. The paper shows δ=0.5 but doesn't demonstrate the claim at extreme δ values.

**Fix B:** Add a brief numerical example in Extension 2 text (or a parenthetical in the figure discussion) showing that transfers remain effective even at δ=0.9 (90% waste). Alternatively, moderate the intro language. The stronger fix is to add the example — it's a single computation and strengthens the argument. Could also add a δ=0.9 line to Figure 3 Panel (b) or mention the result in the caption.

## Execution Order

1. **Fix introduction structure** (addresses `writing-intro` skimmability + `spec-paper` I.3c simultaneously)
2. **Fix Figure 2 formatting** in `generate-exhibits.R` (addresses `visual-figures`)
3. **Add high-δ example** in Extension 2 text (addresses `writing-intro` promise 7)
4. Rebuild exhibits (`Rscript code/generate-exhibits.R`) and recompile paper
