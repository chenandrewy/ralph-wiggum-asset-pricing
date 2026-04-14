# tests/factcheck-theory.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 6m 35s
[ralph-garage/agent-logs/20260414T102326.829091-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260414T102326.829091-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the stated assumptions.

## Requirement 1: Notational Consistency — PASS

26 symbol families identified. No collisions, no ambiguities, no confusing reuse of variables. Every symbol maps to a unique formal object throughout the paper, including across the baseline model, both extensions, and the appendix.

Symbol families catalogued: $t$, $C$, $c^H$, $\alpha$, $\phi$, $g$, $p$, $\xi$, $\eta$, $\theta$, $\Delta\theta$, $D$, $P$, $\Gamma$, $A^j$, $\beta$, $\gamma$, $U/u$, $V$, $v$, $q$, $\kappa$, $\tau$, $\delta$, $\Delta u$, $j$.

Potential near-collisions examined and cleared:
- $\alpha$ (household consumption share) vs. $\theta$ (AI dividend share): explicitly distinguished in the text.
- $U$ (lifetime utility) vs. $u$ (period felicity) vs. $V$ (value function) vs. $v$ (P/D ratio): standard case/context conventions, no collision.
- $\phi_\text{eff}$ used informally in Section 2.3 before formal definition in Extension 2: verbal shorthand, not a true inconsistency.

Full notation report: `ralph-garage/scratch/factcheck-notation.md`.

## Requirement 2: Assumption Consistency — PASS

14 parameter restrictions, 13 structural/definitional assumptions, 5 probability structure assumptions, 8 extension-specific assumptions, and 2 stated approximations catalogued across all sections.

Key consistency checks:
- **Parameter ranges**: No contradictions. All restrictions are compatible with each other and with every structural equation.
- **Structural equations**: Dividend definitions sum to aggregate consumption. Growth factors $\Gamma^{AI}$, $\Gamma^{N}$ correctly derived from dividend and theta-update equations.
- **Probability trees**: Sum to 1 in both the baseline (3 states) and Extension 1 (4 states).
- **Extensions vs. baseline**: Both extensions generalize the baseline; setting extension parameters to null values recovers the baseline exactly.
- **Budget constraint (Eq. 8)**: Household + AI owners + deadweight loss = total post-singularity consumption. Balances exactly.
- **$\phi_\text{eff}$ (Eq. 9)**: Algebraically correct derivation from Eq. 8. Reduces to $\phi$ when $\tau = 0$.
- **Transfer ratio (Eq. 10)**: Correctly derived; $(1+\eta)$ factors cancel as claimed.
- **Complete markets**: $\phi_\text{eff} \to 1$ consistent with stated household consumption $\alpha(1+\eta)C_t(1+g)$.
- **Veto proof (Prop. 3)**: Limit argument as $\gamma \to \infty$ valid given $\phi(1+\eta) < 1$.
- **Numerical calibrations**: All verified ($\phi(1+\eta) = 0.75$ and $0.5$; net transfer factor $0.219$; consumption multiple $3.5\times$).

Full assumption report: `ralph-garage/scratch/factcheck-assumptions.md`.

## Requirement 3: Traceability — PASS

All mathematical objects trace back to the stated assumptions:

| Expression | Traced to |
|---|---|
| P/D ratios (Prop. 1, Eqs. 3–4) | Euler equation (Eq. 11) + probability structure + consumption growth (Eq. 1) + displacement (Eq. 2) + dividend definitions + preferences (Eq. 4) |
| $\Gamma^{AI}$, $\Gamma^{N}$ | Theta-update rule (Eq. 3) + dividend definitions |
| Existence condition $A^j < 1$ (Remark 1, Eq. 5) | Positivity of P/D denominator from Prop. 1 |
| Extinction attenuation (Prop. 2) | $(1-\xi)$ factor in P/D formulas |
| $\Delta u(\gamma)$ (Eq. 7) | Extension 1 singularity tree + CRRA felicity + displacement/positive-singularity rules |
| Veto result (Prop. 3) | $\Delta u(\gamma)$ + infinite-horizon Bellman + veto cost $\kappa$ + extinction normalization |
| Transfer consumption $c^H_{post}$ (Eq. 8) | Baseline displacement + tax rate $\tau$ + deadweight cost $\delta\tau$ |
| $\phi_\text{eff}$ (Eq. 9) | Algebraic factoring of Eq. 8 |
| Transfer ratio (Eq. 10) | Ratio of Eq. 8 to its $\tau=0$ specialization |
| Appendix derivation (Eqs. 11–13) | Euler equation expanded over three states; consistent with Prop. 1 |

No expression was found that cannot be logically derived from the stated assumptions.
