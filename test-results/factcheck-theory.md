# tests/factcheck-theory.py
Started: 2026-04-12 09:46:31 EDT
Runtime: 8m 7s
[ralph-garage/agent-logs/20260412T094631.065849-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260412T094631.065849-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually compatible, and all mathematical objects trace back to the stated assumptions.

## Requirement 1: Notational Consistency — PASS

29 symbol families were identified covering every mathematical object in the paper. Each family has a single, clearly defined formal object, and all variants (time-indexed, superscripted by asset type, explicitly defined transformations like $\phi_\text{eff}$, $\alpha^+$) are transparent.

No collisions or substantive inconsistencies found. Two minor, non-blocking items:

1. **$U$ vs. $V$ for lifetime utility:** The paper uses $U_0^H$ (eq. 3) for lifetime utility in the baseline and $V_\text{veto}$, $V_\text{develop}$ in Extension 1. Both denote the household's lifetime utility. The shift follows a common convention (reduced-form vs. Bellman) but is never explicitly acknowledged. Not a collision — the subscripts disambiguate — but a sentence connecting the two would improve clarity.

2. **$\theta$ subscript convention:** In the Appendix, $\theta_0, \theta_1, \theta_2$ index the chain of post-singularity states (counting singularity events), while in the main text $\theta_t$ uses $t$ as a time index. The Appendix context makes the meaning clear, but the two indexing conventions on the same base symbol are a minor infelicity.

## Requirement 2: Assumption Consistency — PASS

45 assumptions cataloged: 15 parameter domain restrictions, 23 structural/model-definition assumptions, 2 existence/technical conditions, and 5 implicit assumptions used in proofs. 17 consistency checks performed:

- **Parameter domains** are all compatible with each other and with the structural equations.
- **$\phi(1+\eta) < 1$** is correctly used as a sufficient condition (not a universal assumption) and holds for all calibrations.
- **$A^j < 1$ existence condition** is properly treated as a condition that can fail; the paper explicitly discusses the violation under the large singularity as economic motivation.
- **$A^j > 1/2$** (needed in Prop 2 proof) is verified: even without singularity risk, $A^j \approx 0.89$ at baseline parameters.
- **$\Gamma^{AI} > \Gamma^N$** follows algebraically from $\Delta\theta \in (0,1)$.
- **Prop 3 limit argument** is mathematically correct: $\Delta u(\gamma) \to -\infty$ as $\gamma \to \infty$ when $\phi(1+\eta) < 1$.
- **Prop 2 semi-elasticity argument** is valid for $A > 1/2$.
- **Extension assumptions** (positive singularity, transfers) are compatible with the baseline model.
- **Numerical calibrations** satisfy all conditions where claimed; violations of the existence condition under the large singularity are intentional and explicitly discussed.
- **Transfer formula** (eqs 6–8) verified algebraically consistent.

No contradictions, conflicts, or tensions found.

## Requirement 3: Traceability — PASS

All derived mathematical objects trace back to the primitive assumptions:

| Derived Object | Traced To |
|---|---|
| $\Gamma^{AI}, \Gamma^N$ | $\theta, \Delta\theta, \eta$ (A6, A10, A11, B8) |
| $A^j$ | $\beta, g, \gamma, p, \xi, \eta, \phi, \Gamma^j$ (A2, A4–A9, B4) |
| $D_t^{AI}, D_t^N$ | $\theta_t, C_t$ (B6, B7) |
| $P_t^{AI}, P_t^N$ | Euler equation from SDF, dividends (B12, B14) |
| $v^{AI}$ | $A^{AI}$, Euler equation |
| $\bar{\gamma}$ | Prop 3 threshold, derived from $\Delta u(\gamma)$ |
| $V_\text{veto}, V_\text{develop}, V_\text{develop}^{CM}$ | $\beta, \gamma, \alpha, g, p, \xi, \eta, \phi, \kappa, q$ |
| $\Delta u(\gamma)$ | $\gamma, \alpha, \phi, \eta, q$ (A3, A6–A8, A13, B16) |
| $\phi_\text{eff}$ | $\phi, \tau, \delta, \alpha$ (A3, A7, A14, A15, B23) |
| $c^H_{post}, c^H_{no\text{-}transfer}$ | $\phi, \alpha, \eta, \tau, \delta, g, C_t$ (B22) |
| $\alpha^+$ | $\alpha, \phi$ (A3, A7, B16) |
| $B, S, f$ | Proof auxiliaries from primitive parameters |

No expression was found that cannot be logically derived from the stated assumptions.
