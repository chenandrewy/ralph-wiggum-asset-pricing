# tests/factcheck-theory.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 7m 58s
[ralph-garage/agent-logs/20260412T093252.142929-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.142929-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to stated assumptions.

## Requirement 1: Notational Consistency — PASS

28 symbol families were identified and cataloged. No symbol is reused for a different formal object anywhere in the paper. No notational collisions were found.

**Minor cosmetic issues (not failures):**
1. Missing time subscripts on dividends in Section 2.1: the paper writes `$D^{AI} + D^{N} = C_t$` where the left side should carry $t$ subscripts for formal consistency. The meaning is unambiguous from context.
2. The time subscript on $\alpha_t$ is sometimes dropped in the extensions (e.g., Section 4.2 writes $\alpha$ instead of $\alpha_t$), though the paper evaluates at a point in time and the meaning is clear.

**Notable design choices (verified as consistent):**
- $\Gamma$ (dividend growth factor, always superscripted) vs. $\gamma$ (risk aversion, never superscripted): visually similar but never ambiguous.
- $\alpha$ (household consumption share) vs. $\theta$ (AI dividend share): the paper explicitly distinguishes these in the text.
- $U$ (lifetime utility), $V$ (value functions), $u$ (period utility): three related but clearly distinct objects following standard convention.

## Requirement 2: Assumption Consistency — PASS

52 assumptions were cataloged across 6 categories: parameter restrictions (A1–A15), structural assumptions (B1–B14), equilibrium/pricing assumptions (C1–C5), normalizations (D1–D2), Extension 1 assumptions (E1–E7), and Extension 2 assumptions (F1–F5).

All assumptions are mutually consistent. Key consistency checks verified:

- **Parameter restrictions** do not contradict each other. Repeated singularities preserve $\alpha_t > 0$ (since $\phi > 0$) and $\theta_t < 1$ (since $\Delta\theta < 1$).
- **Structural assumptions** are compatible: deterministic growth conditional on no singularity, stochastic singularity events, i.i.d. structure.
- **Extensions do not contradict the baseline.** Extension 1 generalizes the baseline (the baseline is the $q = 0$ special case). Extensions are independent of each other.
- **The equilibrium concept is well-defined** given the existence condition $A^j < 1$, which the paper explicitly discusses (Remark 1) and which holds for all calibrations.
- **The normalization $U_\text{ext} = 0$** is internally consistent; with $\gamma > 1$, CRRA utility is negative for all $c > 0$, making extinction preferred to living. The paper explicitly acknowledges this is conservative for the veto result.
- **All calibration values** satisfy the stated parameter restrictions.
- **The $\phi_\text{eff}$ derivation** is algebraically verified: dividing eq (8) by $\alpha(1+\eta)(1+g)C_t$ yields eq (9).

**Minor issues (not failures):**
1. The condition $\phi(1+\eta) < 1$, critical for Proposition 3 (veto), appears only in the proof, not in the proposition statement. It is satisfied by all calibrations but should ideally be a stated assumption.
2. Formal bounds on $p$ and $\xi$ (both probabilities) are implicit rather than explicit.
3. $\phi_\text{eff}$ can exceed 1 for large $\tau$ and small $\alpha$ (household is over-compensated). The paper does not discuss this edge case, though it does not affect any stated result.

## Requirement 3: Traceability — PASS

All derived mathematical objects trace back to the stated assumptions:

| Derived Object | Traces to |
|---|---|
| $\Gamma^{AI}, \Gamma^N$ (dividend growth factors) | $\theta$ (A9/B8/B10), $\Delta\theta$ (A10/B10), $\eta$ (A4/B6) |
| P/D ratios (Proposition 1) | Euler equation (C5) + all primitives ($\beta, g, \gamma, p, \xi, \eta, \phi, \Gamma^j$) |
| $A^j$ (existence condition) | Same components as P/D ratios |
| $V_\text{veto}$ | $\kappa$ (A12), $\alpha$ (A8), $\beta$ (A7), $\gamma$ (A6), $g$ (A1) |
| $V_\text{develop}, V_\text{develop}^{CM}$ | $p$ (A2), $\xi$ (A3), $q$ (A11), $\phi$ (A5), $\eta$ (A4), $\alpha$ (A8), $\beta$ (A7), $\gamma$ (A6), $g$ (A1), E6 |
| $\Delta u(\gamma)$ (per-period utility gain) | $q$ (A11), $\alpha^+$ (E1), $\phi$ (A5), $\alpha$ (A8), $\eta$ (A4), $\gamma$ (A6) |
| $\bar{\gamma}$ (veto threshold) | Implicitly defined from $V_\text{develop} = V_\text{veto}$; all primitives |
| $c^H_{post}$ (post-transfer consumption) | $\phi$ (A5), $\alpha$ (A8), $\eta$ (A4), $\tau$ (A13), $\delta$ (A14), $C_t$ (B2), $g$ (A1) |
| $\phi_\text{eff}$ (effective displacement) | $\phi$ (A5), $\tau$ (A13), $\delta$ (A14), $\alpha$ (A8) |
| $B, S, f$ (proof auxiliaries) | Local definitions from primitives |

No expression in the paper fails to trace back to the stated assumptions.
