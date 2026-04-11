# Improvement Plan
AUTHOR PLAN — 2026-04-11 10:25:27 EDT

## Status

- **Tests**: 21/25 pass, 4 fail
- **No overhaul needed**: Model, extensions, and code are structurally sound. All issues are targeted fixes.

## Failing Tests (Priority)

### 1. factcheck-anaphora (paper fix)

**Issue**: Line 195–196 says "extinction risk reduces both valuations and compresses the AI premium, as Proposition 2(iii) predicts." Proposition 2(iii) only establishes that the *spread* and *ratio* decrease in $\xi$ — it says nothing about individual P/D levels decreasing.

**Fix**: Narrow the claim. Change to something like: "extinction risk compresses the AI premium, as Proposition 2(iii) predicts — at high extinction probabilities, even AI stocks lose value because the states in which they pay off become less likely." The separate observation about both levels falling can stand on its own without citing Prop 2(iii).

### 2. factcheck-freely (paper fix — two sub-issues)

**Issue A**: Section 2.3, line 177–178 claims the P/D spread "vanishes" when $\phi_\text{eff} \to 1$. This is false within the model: $\Gamma^{AI} \neq \Gamma^{N}$ regardless of $\phi$, so a residual spread from differential dividend growth remains even when displacement is fully hedged. The displacement-driven component of the spread vanishes, but the total spread does not.

**Fix A**: Replace "the P/D spread between AI and non-AI stocks vanishes" with language reflecting that the displacement-driven spread is eliminated while a small residual spread from differential dividend growth remains. E.g., "the displacement-driven valuation premium largely collapses" or "the valuation spread would collapse to a small residual reflecting differential dividend growth."

**Issue B**: Proposition 3(ii) states unconditionally "the household never vetoes" but the proof establishes this only for $\kappa$ sufficiently small. The proposition and proof are misaligned.

**Fix B**: Add "for $\kappa$ sufficiently small" to the proposition statement, or note it holds for the same $\kappa$ as in part (i). The proof already says "for any $\kappa$ small enough, and in particular for the same $\kappa$ used in part (i)" — so the fix is just aligning the proposition statement with the proof.

### 3. visual-figures-image-only (code fix)

**Issue**: Panel (a) of fig-extension-panels has ~31% y-axis headroom (y-axis runs to ~17.5 but data only reaches ~15.3). The threshold is 20%.

**Fix**: In `code/generate-exhibits.R`, tighten the y-axis upper limit for Panel (a). Currently `y_cap_a <- 17`. Reduce to ~16 or compute it from the data (e.g., `ceiling(max(pd_data_a$pd_ai, na.rm=TRUE)) + 0.5`). Then regenerate exhibits.

### 4. writing-intro (paper fix)

**Issue**: Two of five main arguments are not skimmable in the introduction:
- **Argument 2** (complete markets eliminate the valuation premium): The counterfactual appears only in the veto paragraph (P5), not in the pricing discussion (P2–P3). A skimmer may not connect it back to valuations.
- **Argument 3** ("financial market solutions are under-discussed"): This literature-positioning claim is absent from any topic sentence.

**Fix**:
- Add a sentence in the pricing discussion (around paragraphs 2–3) explicitly stating the complete-markets counterfactual: if markets were complete, the valuation premium would vanish (or nearly vanish, per fix 2A above).
- Surface argument 3 — e.g., add a brief clause in paragraph 3 or 6 noting that financial market solutions to AI disaster risk are under-discussed in the literature, though frictions limit their effectiveness.

## Sequencing

1. Fix paper text for factcheck-anaphora (line 195–196 rewording)
2. Fix paper text for factcheck-freely Issue A (Section 2.3 "vanishes" claim) and Issue B (Proposition 3(ii) qualifier)
3. Fix code for visual-figures-image-only (tighten Panel (a) y-axis), regenerate exhibits
4. Fix intro for writing-intro (add complete-markets counterfactual + under-discussed claim)
5. Rebuild LaTeX to verify
