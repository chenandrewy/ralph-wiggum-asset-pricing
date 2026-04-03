# tests/factcheck-theory.py
Started: 2026-04-02 22:39:49 EDT
Runtime: 5m 50s
[ralph-garage/agent-logs/20260402T223949.801599-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T223949.801599-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is internally consistent, all assumptions are mutually compatible, and all mathematical objects trace back to the assumptions with correct derivations.

## 1. Notational Consistency (Requirement 1): PASS

21 symbol families were cataloged. Every symbol is defined before use, used consistently, and no symbol family is repurposed for a different formal object anywhere in the paper.

**Conventions verified as consistent throughout:**
- Tilde convention (post-singularity values): g̃, θ̃, ν̃, ω̃ — all uniform
- Superscript convention (asset type / market structure): A, N, P, CM, q — all stable
- Subscript convention (time vs. regime): t/t+1 on time-varying quantities; pre/post on regime-constant P/D ratios — no collision

**Minor readability notes (no internal collisions):**
- R is used for the normal-state pricing kernel β(1+g)^{1−γ}, which could be confused with gross returns by finance readers. No within-paper collision.
- Δ is used as a ratio (ω̃/ω), not a difference operator. No within-paper collision.
- `\text{CM}` vs `\mathrm{CM}` LaTeX source inconsistency (lines 203 vs 219) — visually identical output.

## 2. Assumption Consistency (Requirement 2): PASS

**Formal assumptions:**
- A1 (Negative singularity): ω̃ < ω, i.e., Δ < 1
- A2 (AI share growth): θ̃ > θ and ν̃ < ν
- A3 (Existence): (1−p)β(1+g)^{1−γ} < 1 and β(1+g̃)^{1−γ} < 1

**Findings:**
- A1 and A2 are logically independent (neither implies the other). Correct model design.
- A3 is redundant given γ > 1, β ∈ (0,1), and positive growth rates. The paper correctly acknowledges this (line 148).
- The paper's numerical illustration (β=0.96, γ=3, g=0.02, g̃=0.05, θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30, p=0.01) satisfies all assumptions simultaneously.
- No conflicts between baseline and extension assumptions. Extension parameters (q, F, τ) are independent of baseline constraints.

**Minor notes:**
- Output share positivity (θ, ν, θ̃, ν̃ ∈ (0,1) with θ+ν < 1, θ̃+ν̃ < 1) is required but never formally stated. Standard implicit assumption.
- Remark 1 (line 241) mentions γ=1 (log utility), which is outside the maintained assumption γ > 1. This is a boundary observation, not a claimed result, but could be qualified.

## 3. Traceability of Mathematical Objects (Requirement 3): PASS

Every mathematical expression in the paper traces back to the primitive parameters and assumptions through a clear derivation chain:

1. **Primitives** → β, γ, g, g̃, p, θ, θ̃, ν, ν̃ (from model environment and assumptions)
2. **Definitions** → ω, ω̃, Δ (algebraic combinations of primitives)
3. **Pricing objects** → R, Φ^A, Φ^N, V_post (from Euler equation applied to primitives)
4. **Equilibrium** → c_t = ωY_t (from market clearing + dividend definitions)
5. **Results** → V_pre^A, V_pre^N, V_pre^{A,CM}, hedging premium (from Euler equation + above)
6. **Extension** → V_pre^{A,q}, friction cost eq (9) (from new parameters q, F, τ + baseline)

**Proof verification:**
- Proposition 1 (P/D ratios): Euler equation expansion verified. Two-state decomposition (no singularity / singularity) correctly yields eqs (6a)-(6b).
- Proposition 2 (comparative static): Quotient rule derivative verified. Numerator simplification in eqs (15)-(16) is algebraically correct. The condition Φ^A(1+V_post) > R/(1−R) correctly characterizes positivity.
- Proposition 3 (complete markets): Setting Δ=1 in Φ^A correctly yields Φ^{A,CM}. Subtraction yields eq (12), which is positive since Δ^{−γ} > 1 when Δ < 1 and γ > 1.

No expression in the paper fails to trace back to the assumptions.
