# Improvement Plan

## Status Summary

- **spec-compliance**: PASS
- **theory-correctness**: FAIL — business-cycle expected-return claim ("2–3 percentage points") unsupported by the formula at stated parameters; actual value is ~5–7 basis points.
- **referee-top3**: Two substantive comments.

No section overhaul needed. The core model (Sections 2–3) is sound. The issues are a localized calibration error in the expected-returns discussion and a thin microfoundation in Section 4.3.

---

## Priority 1: Fix the Failing Test

**Problem.** Line 399 claims "the business-cycle premium differential is approximately 2–3 percentage points" with σ ≈ 0.02. Equation (17) gives (0.98)(3)(0.4–0.6)(0.0004)(~1.04) ≈ 5–7 bp, not 2–3 pp.

**Fix.** Revise the paragraph after Proposition 3's proof (around line 399) as follows:

1. Replace "2–3 percentage points" with the correct magnitude (~5–7 basis points) using σ ≈ 0.02.
2. Reframe the expected-returns narrative honestly: with consumption-growth volatility, the business-cycle premium is small and does not clearly dominate the hedging discount (~80 bp). Acknowledge this tension directly rather than claiming a clean reconciliation.
3. Note that matching observed return differentials would require return-based volatility (σ ≈ 0.15), which conflicts with the consumption-based framework's first-order invariance result (Proposition 3(i) relies on small σ). Frame this as a known limitation of the consumption-CAPM, not a defect of the hedging channel.
4. The key message should be: the hedging channel operates through *valuations* (P/D ratios), not expected returns; reconciling expected returns with observed betas is a standard challenge for consumption-based models and is orthogonal to the paper's main contribution.

**Files to edit:** `paper/paper.tex`, lines ~399 (the paragraph after Proposition 3's proof).

---

## Priority 2: Strengthen the Friction-Resolution Microfoundation (Section 4.3)

**Problem (referee comment 1).** The π(Y_O) = 1 − d/Y_O microfoundation is a single reduced-form equation. The referee flags three gaps: (a) control/governance frictions don't obviously dissolve with large output; (b) the super-linear growth condition needs more justification; (c) the adverse-selection discount d should depend on information, not just output scale.

**Fix.** Add a short (2–3 paragraph) screening/securitization microfoundation before equation (18), replacing the current single-equation treatment. Specifically:

1. Add a simple bilateral-trade setup: AI owners have private information about capital quality q ∈ {H, L}. The household offers a pooling price. High-quality owners sell only if output Y_O is large enough that the adverse-selection discount d is negligible relative to gains from trade (diversification motive for AI owners). This derives π(Y_O) from primitives rather than assuming it.
2. Address the governance objection directly: note that AI owners with infinite output have a *diversification* motive (their wealth is concentrated in a single technology) that provides the incentive to sell, even without needing the proceeds for consumption.
3. Strengthen the super-linear growth justification: cite increasing returns to scale in AI (compute scaling laws) as the economic basis, and note that the qualitative results (hump shape, convergence) hold for any growth rate exceeding linear.
4. If this pushes the paper over 20 pages, trim equal length from elsewhere (e.g., compress the Proposition 6 proof further, or tighten the extinction-risk discussion).

**Files to edit:** `paper/paper.tex`, Section 4.3 (lines ~478–508).

---

## Priority 3: Reframe Expected-Returns Discussion (Referee Comment 2 Residual)

This is largely addressed by Priority 1. The residual action:

1. In the conclusion (line ~516), soften the claim about business-cycle reconciliation. Change "the hedging channel coexists with higher expected returns for AI stocks from cyclical exposure" to acknowledge that the model predicts the coexistence qualitatively but that the quantitative reconciliation depends on parameters beyond the consumption-based framework.
2. In the introduction (line ~60), similarly temper: the current sentence about business-cycle risk "reconciling" the hedging channel should say the augmented model shows the two forces *can* coexist, without claiming a tight quantitative match to observed return differentials.

**Files to edit:** `paper/paper.tex`, introduction (~line 60) and conclusion (~line 516).
