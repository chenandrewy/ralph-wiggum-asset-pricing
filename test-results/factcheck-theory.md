# tests/factcheck-theory.py
Started: 2026-04-10 22:15:41 EDT
Runtime: 7m 15s
[ralph-garage/agent-logs/20260410T221541.756081-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260410T221541.756081-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

23 symbol families identified and audited. Zero collisions, zero ambiguities. Every symbol is introduced before use and has a single meaning throughout the paper. Key checks:

- **Aggregate vs. household consumption:** Clean case separation ($C_t$ vs. $c_t^H$) maintained throughout.
- **Consumption share vs. dividend share:** $\alpha_t$ (household consumption share) and $\theta_t$ (AI dividend share) are never conflated.
- **Superscript conventions:** $H$ (household), $AI$ (AI stocks), $N$ (non-AI stocks), $j$ (generic asset) are disjoint and consistently applied across all families.
- **$\Gamma^N$ simplification:** Prop 1 form $\frac{1-\theta-\Delta\theta(1-\theta)}{1-\theta}(1+\eta)$ is algebraically identical to Appendix A form $(1-\Delta\theta)(1+\eta)$. Verified.
- **$\phi$ vs. $\phi_\text{eff}$:** Explicitly related by Eq.(9) with a clear substitution statement.
- **$U$ vs. $u$:** Lifetime utility ($U_0^H$) and period utility ($u$, used informally in Prop 3 proof) are distinguished by standard case convention. The lowercase $u$ appears only once ("$u$ is concave") and is unambiguous from the CRRA specification.
- **Time subscript dropping:** Standard practice in stationary equilibrium formulas (Prop 1) and single-period extension analysis (Sec 4.2). No confusion.

Full notation inventory: $t$, $C_t$, $c_t^H$, $\alpha_t$, $g$, $p$, $\xi$, $\eta$, $\phi$, $\phi_\text{eff}$, $\theta_t$, $\Delta\theta$, $D_t^{AI}$, $D_t^N$, $P_t^j$, $v^{AI}$, $\Gamma^{AI}$, $\Gamma^N$, $A^j$, $\gamma$, $\beta$, $U_0^H$, $U_\text{ext}$, $u$, $\tau$, $\delta$, $\mathbb{E}_t$, $j$.

## Requirement 2: Assumption Consistency — PASS

25 assumptions identified across baseline (A1–A17, A25), Extension 1/Veto (A18–A20), and Extension 2/Transfers (A21–A24). No contradictions found. Key consistency checks:

- **Parameter ranges:** All open intervals are non-contradictory ($g>0$, $\alpha_t \in (0,1)$, $\phi \in (0,1)$, $\gamma>1$, $\beta \in (0,1)$, $\Delta\theta \in (0,1)$, $\tau \in [0,1)$, $\delta>0$).
- **Repeated displacement preserves bounds:** $\alpha_t = \phi^n \alpha_0 \in (0,1)$ since $\phi \in (0,1)$. Similarly $\theta_n = 1-(1-\theta_0)(1-\Delta\theta)^n \in (0,1)$.
- **Positive singularity preserves bounds:** $\alpha_{t+1} = \min(1, \alpha_t/\phi) \leq 1$ by construction.
- **Existence condition vs. calibration:** $A^{AI} \approx 0.987 < 1$ at baseline ($p=1\%$, $\xi=0$). Verified numerically.
- **CRRA sign vs. extinction normalization:** $\gamma > 1$ makes CRRA utility negative, so $U_\text{ext}=0$ is above all finite-consumption utilities. Paper explicitly acknowledges this is conservative. Not an inconsistency.
- **Euler equation in extinction:** $c_{t+1}^H = 0$ makes SDF undefined, but payoff is also zero. Product resolves as zero. Standard treatment.
- **Transfer formula:** Verified algebraically that Eq.(8) follows from baseline displacement (A6) plus tax/deadweight assumptions (A21–A22). $\phi_\text{eff}$ derivation is correct.
- **Extension assumptions augment baseline:** Extensions add new branches/parameters without contradicting existing assumptions.

Minor observations (not inconsistencies):
1. Implicit restriction $\delta\tau < 1$ not formally stated, but always satisfied under calibration ($\delta=0.5$, $\tau<1$).
2. Stationarity approximation acknowledged as exact only when $\Delta\theta \to 0$; numerically exact values provided separately.

## Requirement 3: Traceability — PASS

All mathematical objects trace back to the 25 assumptions. Objects not directly in the assumptions are derived quantities:

| Derived Object | Traced To |
|----------------|-----------|
| $\Gamma^{AI} = \frac{\theta+\Delta\theta(1-\theta)}{\theta}(1+\eta)$ | A5 ($\eta$), A9 ($\theta_t$), A10 ($\Delta\theta$) |
| $\Gamma^N = (1-\Delta\theta)(1+\eta)$ | A5, A10 |
| $A^j$ (existence condition) | A2 ($g$), A4 ($p$), A5 ($\eta$), A6 ($\phi$), A7 ($\xi$), A14 ($\beta,\gamma$), plus $\Gamma^j$ |
| $v^{AI} = P^{AI}/D^{AI}$ | A15 (Euler equation), A9 ($D^{AI}$) |
| $P^{AI}/D^{AI}$, $P^N/D^N$ (Prop 1) | Derived from Euler equation (A15) using consumption dynamics (A2–A7) and preferences (A14) |
| Valuation spread (Prop 2) | Derived from Prop 1 closed forms |
| $c^H_{post}$ (Eq. 8) | A3 ($\alpha$), A5 ($\eta$), A6 ($\phi$), A21 ($\tau$), A22 ($\delta$) |
| $c^H_{no\text{-}transfer}$ (Eq. 10) | A3, A5, A6 (baseline with $\tau=0$) |
| $\phi_\text{eff}$ (Eq. 9) | A6 ($\phi$), A21 ($\tau$), A22 ($\delta$), A3 ($\alpha$) |
| $u$ (Prop 3 proof) | Implicit period utility from A14: $u(c) = c^{1-\gamma}/(1-\gamma)$ |

No expression in the paper lacks a derivation path from the stated assumptions.
