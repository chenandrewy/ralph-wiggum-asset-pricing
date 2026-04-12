# Improvement Plan
AUTHOR PLAN — 2026-04-12 09:30:52 EDT

## Status: 23/25 tests passing

Two tests fail: `factcheck-freely`, `spec-paper`. No overhaul needed—the model section is sound and all economic requirements pass. Focus on the two failures.

---

## Priority 1: Fix `factcheck-freely` (3 issues)

### 1a. Qualify the transfer-ratio claim (Section 4.2, near eq. 9)

The paper says: "This ratio exceeds one whenever τ > 0: transfers always improve the household's position in the singularity state, regardless of η."

The ratio is `1 + τ(1 − δτ)(1 − φα)/(φα)`. This exceeds one only when `(1 − δτ) > 0`, i.e., `δτ < 1`. The claim needs the qualification "whenever τ > 0 **and** δτ < 1." For all parameterizations used in the paper (δ ≤ 0.9, τ < 1), the condition holds, but the unqualified statement is mathematically wrong.

**Fix:** Add "and δτ < 1" qualification to the sentence. Something like: "This ratio exceeds one whenever τ > 0 and δτ < 1 (i.e., deadweight costs do not consume the entire transfer)."

### 1b. Strengthen Proposition 2 proof (extinction attenuation)

The proof correctly identifies convexity of f(A) = A/(1−A) but skips the key step: why convexity plus A > 1/2 implies the conclusion. Need to show that the semi-elasticity f'(A)/f(A) = 1/[A(1−A)] is increasing for A > 1/2, so the larger absolute reduction in A^{AI} translates to a larger proportional reduction in the P/D ratio.

**Fix:** Add 1–2 sentences after the convexity statement explaining that for A > 1/2 the semi-elasticity is increasing, so equal absolute reductions produce larger proportional reductions at higher A values. Since A^{AI} > A^{N}, the ratio falls.

### 1c. Close Proposition 3 proof gap (infinite-horizon)

The proof shows one-period utility loss Δu(γ) grows without bound as γ → ∞, but the veto comparison is between infinite-horizon value functions. Need to link the per-period loss to the infinite-horizon inequality.

**Fix:** Add a sentence stating that in the infinite-horizon problem, V_develop − V_veto can be written as a discounted sum of per-period differences, with the singularity term contributing p(1−ξ)Δu(γ) each period. Since Δu(γ) → −∞ while the veto cost κ is fixed, the infinite-horizon inequality holds for γ large enough.

---

## Priority 2: Fix `spec-paper` (lit review length)

The lit review spans ~0.55–0.65 rendered pages, exceeding the half-page limit.

**Fix:** Trim the lit review. Candidates for cuts:
- The third paragraph (creative destruction citations + macro AI + rare disasters + Pastor-Veronesi) can be compressed to 1–2 lines by listing citations more compactly without individual descriptions.
- The GKP paragraph could trim the sentence about "our contribution is the more modest one" since this is already stated elsewhere in the paper.

Target: reduce from ~174 words / ~15 typeset lines to ~130 words / ~11 lines.

---

## No other changes needed

- All 28 economic sub-requirements pass.
- Code generates correct exhibits (factcheck-code, factcheck-exhibits pass).
- Model theory is correct (factcheck-theory passes).
- Writing quality passes (writing-intro, writing-intuition pass).
- Visual quality passes (visual-figures, visual-pages pass).
- No referee tests are currently enabled.
