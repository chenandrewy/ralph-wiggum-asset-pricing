# tests/factcheck-theory.py
Started: 2026-04-04 23:59:28 EDT
Runtime: 6m 8s
[ralph-garage/agent-logs/20260404T235928.981688-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260404T235928.981688-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent (one minor collision), all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

20 symbol families identified and catalogued. The notation is clean and well-organized.

### Issues Found

1. **$N$ dual usage (moderate):** The letter $N$ is used as a superscript for "non-AI stocks" ($P^N$, $D^N$, $H^N$) throughout the body, and as a subscript for "no-singularity regime" ($\pi_N^i$) in the Appendix. The implied expression $\pi_N^N$ (pre-singularity P/D of non-AI stocks) would stack two $N$'s with different meanings. The subscript/superscript distinction mitigates confusion, and $\pi_N^N$ is never written, so this does not rise to genuine ambiguity that could produce an incorrect interpretation.

2. **$u(\cdot)$ undefined (minor):** The period utility function $u$ appears in the veto proof (Appendix, eqs. A.5–A.6) without formal definition. It is implicitly $u(c) = c^{1-\gamma}/(1-\gamma)$ from eq. (1). Standard convention; any finance reader would understand.

3. **$\Lambda$ overloading (minor):** $\Lambda$ is defined as the constant $(1-\phi)G$ in eq. (4), then used as a function $\Lambda(\theta, \delta)$ in eq. (10). The function nests the constant at $\theta = 0$, and the two usages are scoped to different sections.

### Clean Areas

- All 20 symbol families use consistent notation throughout.
- Greek letters denote structural parameters; Latin letters denote variables/functions — clean separation.
- Superscript conventions ($A$, $N$, $CM$, $IM$, $\text{pub}$) are stable.
- No confusion between $R$ (discount compound) and any return or interest rate.
- No confusion between $\alpha$ (AI share) and risk aversion ($\gamma$).

## Requirement 2: Assumption Consistency — PASS

22 assumptions identified across the baseline model, three extensions, and implicit modeling choices. All are mutually consistent.

### Consistency Groups Verified

1. **Parameter domains:** All parameter restrictions ($\beta \in (0,1)$, $\gamma > 1$, $g > 0$, $\alpha \in (0,1)$, $p \in (0,1)$, $G > 1$, $\phi \in (0,1)$, $\alpha_S > \alpha$) are mutually compatible. The finiteness condition $R < 1$ is automatically implied by $\beta \in (0,1)$, $g > 0$, $\gamma > 1$ — redundant but not contradictory.

2. **Consumption jump:** $\Lambda = (1-\phi)G \in (0, G)$. Can be above or below 1 depending on parameters. Both cases are discussed in the paper.

3. **Stochastic structure:** Pre-singularity has one source of uncertainty (singularity arrival, i.i.d. Bernoulli $p$). Post-singularity is deterministic Gordon growth. One-time permanent event. Internally coherent.

4. **Market structure:** Household holds all public shares, consumes all publicly traded output, prices all public assets. AI owners are segmented, hold private capital, not marginal in public markets. Coherent endowment economy.

5. **P/D well-definedness:** P/D ratios are always positive and finite for all parameter values in the assumed domains. Verified algebraically.

6. **Complete vs. incomplete markets:** $\Lambda^{CM} = G$ correctly follows from household consuming total output. Amplification factor $(1-\phi)^{1-\gamma} > 1$ for $\gamma > 1$, $\phi \in (0,1)$.

7. **Transfer extension:** Correctly nests baseline ($\theta = 0$), complete markets ($\theta = 1, \delta = 0$), and full deadweight ($\theta = 1, \delta = 1$). Range $\Lambda(\theta,\delta) \in [(1-\phi)G, G]$.

8. **Veto extension:** Under complete markets ($\Lambda = G > 1$), household never vetoes — consistent. Under incomplete markets with $\Lambda < 1$, veto threshold $\bar{\kappa} > 0$ exists by strict concavity — consistent.

9. **Extinction extension:** Scaling $H^i$ by $(1-q)$ correctly reflects that only the survival branch contributes to asset values. The "zero utility thereafter" convention for extinction is standard (household ceases to exist), not contradictory with CRRA.

10. **Cross-extension:** All three extensions modify different dimensions (consumption conditional on survival, singularity prevention, survival probability). Independent and mutually compatible.

11. **Euler equation derivation:** SDF $\times$ dividend growth correctly yields $R \cdot H^i$ in the singularity branch. Verified algebraically for both AI and non-AI stocks.

12. **Spread formula:** $(H^A - H^N) = \frac{\alpha_S - \alpha}{\alpha(1-\alpha)} \Lambda^{1-\gamma}$. Algebraically correct.

## Requirement 3: Object Traceability — PASS

All derived mathematical objects trace back to the assumptions:

| Derived Object | Source Assumptions |
|---|---|
| $R = \beta(1+g)^{1-\gamma}$ | A1 ($\beta, \gamma$), A2 ($g$) |
| $V_0, V_\infty$ | $R$, A4 ($p$) |
| $\Lambda = (1-\phi)G$ | A5 ($G$), A6 ($\phi$) |
| $H^A, H^N$ | A1 ($\gamma$), A3 ($\alpha$), A7 ($\alpha_S$), $\Lambda$ |
| $P^i/D^i$ | Euler equation (A1, A9), dividends (A20), consumption (A18) |
| Spread (eq. 9) | Algebraic from $H^A, H^N, V_0, V_\infty$ |
| Amplification (eq. 6) | A1 ($\gamma$), A6 ($\phi$) |
| $\Lambda(\theta, \delta)$ | A13 ($\theta, \delta$), A5, A6 |
| $\Lambda^{CM} = G$ | A15 |
| $\bar{\kappa}$ | A1 ($\gamma$), A14 ($\kappa$), $\Lambda$ |
| $u(\cdot)$ | Implied by A1 |
| Extinction P/D (eq. 12) | A16 ($q$), baseline objects |
| Extinction spread (eq. 13) | Algebraic from eq. 12 |
| $\pi_S, \pi_N^i$ (Appendix) | Proof notation for P/D ratios |

No expression was found that cannot be logically derived from the assumptions.
