# tests/factcheck-theory.py
Started: 2026-04-02 21:59:20 EDT
Runtime: 6m 41s
[ralph-garage/agent-logs/20260402T215920.417886-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T215920.417886-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

22 symbol families were catalogued. No collisions, ambiguities, or reuse of symbols for different formal objects were found.

**Conventions verified as consistent:**
- Tilde convention (post-singularity values): applied uniformly to g, θ, ν, ω.
- Superscript convention (A, N, P, CM, q): applied uniformly across D, P, V, Φ.
- Subscript convention: time subscripts on Y, D, P, c, n; regime subscripts on V (explicitly flagged in Proposition 1).

**Minor style observations (not errors):**
- V subscripts denote regime (0/1) rather than time, which the paper explicitly warns about.
- R denotes a pricing-kernel quantity rather than a return; defined explicitly.
- Δ denotes a ratio rather than a difference; defined explicitly.
- P appears as both a base symbol (price) and a superscript (private capital), but in syntactically distinct positions with no overlap in usage.

## Requirement 2: Assumption Consistency — PASS

Three formal assumptions and eight inline parameter restrictions were identified. All are mutually consistent.

**Assumptions:**
1. Negative singularity: θ̃ + ν̃ < θ + ν (i.e., Δ < 1)
2. AI share growth: θ̃ > θ and ν̃ < ν
3. Existence: (1-p)β(1+g)^{1-γ} < 1 and β(1+g̃)^{1-γ} < 1

**Consistency checks performed:**
- Assumptions 1 and 2 are genuinely independent. Together they require ν - ν̃ > θ̃ - θ > 0. The numerical illustration (θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30) satisfies both.
- Assumption 3 does not interact with Assumptions 1-2 (separate parameter sets).
- The claim that Assumption 3 is "automatically satisfied for γ > 1" is correct, given the prose condition g > 0. If g could be negative (e.g., g = -0.5, γ = 3), the claim would fail. The paper states g > 0 in prose ("output grows over time") but does not elevate it to a formal parameter restriction. This is a minor formalization gap, not a mathematical error.
- All price-dividend ratios are positive under the stated assumptions (verified denominators and numerators).
- Displacement ratio satisfies 0 < Δ < 1 under the assumptions.
- Output share positivity (θ > 0, ν > 0, θ + ν < 1, and post-singularity analogues) is implicit from the economic setup but not formally stated. Minor formalization gap.

## Requirement 3: Traceability — PASS

All mathematical objects in the paper were traced back to the assumptions or derived from them.

**Derived objects verified:**
- Y_t: from growth equations (1)-(2) using g, g̃
- D_t^A, D_t^N, D_t^P: from share parameters θ, ν and Y_t (Eqs. 3-4)
- ω, ω̃, Δ: defined from θ, ν, θ̃, ν̃
- c_t: from market clearing (n_t^A = n_t^N = 1) and budget constraint → c_t = ωY_t
- R = β(1+g)^{1-γ}: from β, g, γ
- Φ^A, Φ^N: from β, Δ, γ, g̃, θ̃/θ, ν̃/ν
- V_1 = β(1+g̃)^{1-γ}/[1-β(1+g̃)^{1-γ}]: from Euler equation post-singularity
- V_0^A, V_0^N: from Euler equation pre-singularity (Proposition 1, verified algebraically)
- V_0^{A,CM}, Φ^{A,CM}: complete-markets variant with Δ effectively equal to 1
- V_0^{A,q}: extinction extension using additional parameter q
- F, τ, T: new parameters introduced for the friction-cost extension
- N(p), D(p): local proof variables in Appendix

**Derivations verified:**
- Proposition 1 (P/D ratios): Euler equation expansion confirmed. Both no-singularity and singularity branches computed correctly.
- Proposition 2 (cross-section): Subtraction of V_0^N from V_0^A confirmed. Sign follows from θ̃/θ > 1 > ν̃/ν.
- Proposition 3 (comparative static): Quotient rule derivative confirmed. Numerator simplifies correctly to Φ^A(1+V_1)(1-R) - R.
- Proposition 4 (hedging premium): Complete-markets substitution (Δ^{-γ} → 1) confirmed. Positivity follows from Δ < 1, γ > 1.
- Eq. (16) (extinction): Factor (1-q) correctly scales the singularity contribution.
- Remark 1 (extreme singularity): Limit g̃ → ∞ with γ > 1 gives (1+g̃)^{1-γ} → 0, so Φ^A → 0 and V_1 → 0. Correct.
- Eq. (17) (friction cost): Algebra verified. F/Y → 0 as Y → ∞. Correct.

No expression was found that cannot be logically derived from the assumptions.
