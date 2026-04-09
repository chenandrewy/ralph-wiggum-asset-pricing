# tests/factcheck-theory.py
Started: 2026-04-09 19:33:02 EDT
Runtime: 8m 40s
[ralph-garage/agent-logs/20260409T193302.029593-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T193302.029593-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to stated assumptions.

## Requirement 1: Notational Consistency — PASS

27 symbol families catalogued across the entire paper. No collisions (same symbol reused for a different formal object), no ambiguous overloading, and no undefined symbols. Superscript/subscript conventions are consistent: superscripts for asset/agent type (AI, N, H, j), subscripts for time (t) or scenario labels (post, no-transfer, ext). Time subscripts are dropped in stationary expressions, which is standard and explicitly justified.

Three minor stylistic observations (none are errors):
1. $\delta_0$ carries a subscript 0 with no companion — stylistic, not an error.
2. $u_\text{ext} = 0$ is introduced in prose rather than formally — acceptable for a brief aside.
3. $\phi^+$ uses a superscript that could theoretically be confused with exponentiation, but explicit definition makes this unambiguous.

Full notation audit: `ralph-garage/scratch/factcheck-notation.md`

## Requirement 2: Assumptions Consistency — PASS

40+ assumptions catalogued across 8 categories (structural, parameter restrictions, singularity dynamics, preferences, existence condition, Extension 1, Extension 2, calibration). Key consistency checks performed:

- **Budget constraints satisfied.** Consumption shares sum to 1. Public dividends sum to $C_t$. Private capital dividends are non-negative under $\alpha_t \leq 1 - \theta_t$.
- **Parameter restrictions non-contradictory.** All restrictions are on distinct parameters with compatible ranges.
- **Existence condition verified numerically.** $A^{AI} \approx 0.987 < 1$ at baseline ($p = 1\%$, $\xi = 0$). Violation for large-singularity scenario ($A^{AI} \approx 2.37$) is explicitly acknowledged and used as a feature of the argument.
- **Constraint $\alpha_t \leq 1 - \theta_t$ preserved under dynamics.** Requires $\phi + \Delta\theta \leq 1$, which holds for all calibrations used ($0.5 + 0.2 = 0.7$ and $0.05 + 0.2 = 0.25$). This regularity condition is not explicitly stated but is satisfied.
- **Extensions consistent with baseline.** Extension 1 (veto) nests the baseline at $\lambda = 0$. Extension 2 (transfers) nests the baseline at $\tau = 0$. No contradictions.
- **Euler equation derivation verified.** Appendix proof is algebraically consistent with Proposition 1 formulas.
- **$\Delta U^H$ formula (Eq. 6) verified.** Correctly computes the expected utility difference in the probability-$p$ event between allowing and blocking AI development, with extinction utility normalized to zero.
- **Transfer formulas (Eqs. 7-8) verified.** $c^H_{post}$ correctly reduces to baseline at $\tau = 0$. Transfer ratio formula is an algebraic identity.
- **R code implements paper formulas correctly.**

Two minor observations (neither is a mathematical inconsistency):
1. The condition $\phi + \Delta\theta \leq 1$ (needed to preserve $\alpha_t \leq 1-\theta_t$ after singularities) is unstated but satisfied for all calibrations.
2. Extension 2 labels the tax base as "AI owners' surplus" but the formula taxes their total post-singularity consumption share — a framing choice, not a formula error.

Full assumptions audit: `ralph-garage/scratch/factcheck-assumptions.md`

## Requirement 3: Traceability — PASS

All derived mathematical objects trace back to stated assumptions:

| Derived Object | Traced To |
|---|---|
| $\Gamma^{AI}$, $\Gamma^{N}$ (dividend growth factors) | $\theta$, $\Delta\theta$, $\eta$ (A7, C6, B3, B4) |
| $A^j$ (existence condition) | $\beta$, $g$, $\gamma$, $p$, $\xi$, $\eta$, $\phi$, $\Gamma^j$ (B1-B8, D1, E1) |
| $P^{AI}/D^{AI}$, $P^{N}/D^{N}$ (P/D ratios) | Euler equation (D1, D2) + dividend processes (A7, A8, C4-C6) |
| Valuation spread (Corollary 1) | Prop 1 + $\Delta\theta > 0$ (B4) |
| Comparative statics (Prop 2) | Prop 1 formulas |
| $\Delta U^H$ (veto gain) | $p$, $\xi$, $\lambda$, $\phi^+$, $\phi$, $\alpha$, $\eta$, $g$, $C_t$, $\gamma$ (F1-F6, B2, B3, D1) |
| $c^H_{post}$, transfer ratio | $\phi$, $\alpha$, $\eta$, $g$, $C_t$, $\tau$, $\delta_0$ (G1-G4, B2, B3) |

No orphaned mathematical expressions found. Every formula in the paper can be logically derived from the stated assumptions.
