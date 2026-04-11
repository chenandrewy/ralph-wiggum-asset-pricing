# tests/factcheck-theory.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 8m 23s
[ralph-garage/agent-logs/20260411T100209.010535-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260411T100209.010535-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to primitives.

## Requirement 1: Notational Consistency — PASS

Every mathematical symbol maps to a unique economic concept. No Greek or Latin letter collisions were found. All decorated variants ($\phi_\text{eff}$, $\bar{\gamma}$, $\alpha^+$, $\Gamma^{AI}$, $\Gamma^N$) are explicitly defined near first use.

Four minor issues were identified, none affecting correctness or readability:

1. **Dropped time subscript** (line 112): The prose identity writes $D^{AI} + D^{N} = C_t$ instead of $D_t^{AI} + D_t^{N} = C_t$. Typographical slip.
2. **$U$ vs $V$ notation shift**: The baseline uses $U_0^H$ for lifetime utility (Eq 3), while Extension 1 uses $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ without stating the convention change. This is a standard economics convention ($U$ for utility, $V$ for value functions in decision problems) but is implicit.
3. **Dual role of $\Delta$**: Used as a parameter prefix ($\Delta\theta$) and a difference operator ($\Delta u(\gamma)$). Standard mathematical notation; no ambiguity in context.
4. **Mixed subscript style on $c^H$**: Base notation uses time subscripts ($c_t^H$); Extension 2 uses state labels ($c^H_{post}$, $c^H_{no\text{-}transfer}$). Clear in context.

Full inventory: see `/workspace/ralph-garage/scratch/factcheck-notation.md`.

## Requirement 2: Assumption Consistency — PASS

28 assumptions were catalogued across 6 categories (structural setup, equilibrium conditions, Extension 1, Extension 2, appendix derivations, calibration parameters). All parameter restrictions, functional forms, budget constraints, and equilibrium conditions are mutually consistent.

Four minor boundary items were flagged, none representing genuine inconsistencies:

1. **$\alpha \in (0,1)$ boundary**: The positive singularity formula $\alpha_{t+1} = \min(1, \alpha_t/\phi)$ can push $\alpha$ to exactly 1, technically outside the stated open interval $(0,1)$. Trivially resolved by writing $(0,1]$.
2. **Implicit constraint $\delta\tau \leq 1$**: Required for non-negative transfers but never stated. Automatically satisfied when $\delta < 1$ (as in all calibrations where $\delta = 0.5$).
3. **$\phi(1+\eta) < 1$ never formally assumed**: Used throughout for the hedging/veto arguments but treated as a parametric consequence rather than a stated assumption. Satisfied in all calibrations.
4. **Extinction state Euler equation**: The $0 \times \infty$ indeterminate form when $c_{t+1}^H = 0$ is handled by the standard convention that zero payoff yields zero contribution.

Budget constraints verified:
- Consumption shares sum to 1 in all states (pre/post singularity, with/without transfers).
- Dividend shares sum to 1 in all states.
- Transfer budget constraint satisfied: household + AI owners + deadweight loss = aggregate output.

Full analysis: see `/workspace/ralph-garage/scratch/factcheck-assumptions.md`.

## Requirement 3: Traceability — PASS

All derived mathematical objects trace back to the primitive assumptions:

| Derived Object | Traced To |
|---|---|
| $\Gamma^{AI}$, $\Gamma^N$ | $\theta$, $\Delta\theta$, $\eta$ (A5, A7) |
| $A^j$ (Eq 5) | $\beta$, $g$, $\gamma$, $p$, $\xi$, $\eta$, $\phi$, $\Gamma^j$ (A2, A4, A5, A11) |
| $v^{AI}$, P/D ratios (Prop 1) | Euler equation (E1) + all structural assumptions |
| $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ | Utility (A11) + veto/development assumptions (C1-C5) |
| $\Delta u(\gamma)$ (Eq 6) | $q$, $\alpha$, $\phi$, $\eta$, $u(\cdot)$ (A5, A11, C1) |
| $\bar{\gamma}$ (Prop 3) | Threshold defined by $\Delta u(\gamma)$ crossing |
| $\phi_\text{eff}$ (Eq 9) | $\phi$, $\tau$, $\delta$, $\alpha$ (A3, A5, D1) |
| $c^H_{post}$ (Eq 8) | $\phi$, $\alpha$, $\eta$, $g$, $C_t$, $\tau$, $\delta$ (A2, A3, A5, D1) |
| $c^H_{no\text{-}transfer}$ | Baseline consumption: $\phi\alpha(1+\eta)C_t(1+g)$ (A2, A3, A5) |
| $\alpha^+$ | $\min(1, \alpha/\phi)$ (A3, A5, C1) |
| Transfer ratio (Eq 10) | Algebraic simplification of Eq 8 / baseline (verified: $\eta$ cancels) |

No expression was found that cannot be logically derived from the stated assumptions.
