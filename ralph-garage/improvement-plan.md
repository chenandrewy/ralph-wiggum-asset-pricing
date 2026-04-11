# Improvement Plan
AUTHOR PLAN — 2026-04-11 14:57:23 EDT

## Status: 20/25 tests pass, 5 fail

## Failing Tests and Fixes

### 1. factcheck-bysection (paper + code)

**Issue A — Prop 2 proof false claim (line 164).** The proof says "common additive reduction" when xi increases. This is wrong: the singularity component is proportional to Gamma^j, so the additive changes differ by factor Gamma^AI/Gamma^N ≈ 2.67. The factor (1-xi) applies multiplicatively to both, so the correct argument is: higher xi scales down the singularity component by the same *multiplicative* factor in both A^AI and A^N. Since A/(1-A) is increasing and convex and A^AI > A^N, a common multiplicative scaling of the singularity term (which is larger for AI) compresses the ratio.

- **Fix:** Rewrite the Prop 2 proof to use the multiplicative argument. Replace "common additive reduction" with the correct reasoning.

**Issue B — "roughly 50%" claim (line 191).** The figure shows NASDAQ ending ~470-480 vs S&P ~340 (normalized to 100), which is ~38% outperformance, not 50%.

- **Fix:** Change "roughly 50%" to "roughly 40%" or regenerate the figure to check the exact latest data point, then state the correct number.

### 2. writing-intro (paper)

**Issues:** P4 is overloaded (model + closed-form + quantitative + complete markets + extinction in one paragraph). P4→P5 transition is forced. P5→P6 is a non-sequitur. P2/P3 redundancy.

- **Fix:** 
  - Merge P2 and P3 into a single tighter paragraph that introduces the hedging motive and explains restricted equity once.
  - Split P4: one paragraph on the model and its main result (hedging premium), a second on complete markets and extinction attenuation.
  - Smooth P5 transition by linking from "market incompleteness drives valuations" to "market incompleteness also distorts development."
  - Tighten P6 opening so it flows from veto → policy response.

### 3. element-rhetoric-meta (paper)

**Issues:** "requiring zero traditional research labor" is too blunt/boastful. Near-identical phrasing in abstract and intro. The device takes too much space in the abstract.

- **Fix:**
  - Abstract: shorten to something like "This paper demonstrates the displacement it models: AI agents produced all analysis and writing from a human-authored specification." Drop the "requiring zero" quantifier.
  - Intro: vary the phrasing — develop the device with more specificity about the human/AI division rather than repeating the abstract's formulation.

### 4. visual-figures-image-only (code)

**Issue:** Panel (b) x-axis extends to ~65%, but curves flatten and converge by ~50%.

- **Fix:** Cap Panel (b) x-axis at 50% (tau_max = 0.50) so curves fill the plot area.

### 5. visual-figures (paper + code)

**Issue:** Panel (a) large-singularity line is absent for most of x-axis (P/D undefined at low tau), and caption doesn't explain this.

- **Fix:** Add to the caption for Panel (a): explain that the large-singularity P/D is undefined at low tax rates because the existence condition is violated (the hedge value becomes infinite). This is actually a key visual message — make it explicit in the caption.

## Execution Order

1. **Code fix (items 4, 5, 1B):** Tighten Panel (b) x-axis to 50%. Regenerate figures. Check exact NASDAQ/S&P outperformance from the data.
2. **Prop 2 proof fix (item 1A):** Rewrite the proof's intermediate reasoning.
3. **Caption fix (item 5):** Add existence-condition explanation to fig-extension-panels caption.
4. **Intro rewrite (items 2, 3):** Restructure paragraphs, soften meta-rhetoric, vary abstract vs intro phrasing.
