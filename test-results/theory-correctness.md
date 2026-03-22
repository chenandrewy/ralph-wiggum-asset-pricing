# tests/theory-correctness.py
Started: 2026-03-22 10:45:45 EDT
Runtime: 5m 20s
[ralph-garage/agent-logs/20260322T144545.635988Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T144545.635988Z_theory-correctness_claude_opus.log)

# theory-correctness

VERDICT: FAIL

REASON: Inline numerical claims for the insider-pricing robustness check ($\eta$ exercise) are inconsistent with the stated formula and parameters.

## Condition 1: Notational Consistency — PASS

All mathematical objects grouped by concept:

- **Consumption/Utility:** $c_t$, $\gamma$, $\beta$, CRRA utility (eq 1). Consistent throughout.
- **Dividends:** $D_t^A$, $D_t^N$. Always superscripted A/N. $c_t = D_t^A + D_t^N$ (eq 2). Consistent.
- **AI share:** $s_t \equiv D_t^A / c_t$ (eq 3), $s$ when constant. $\tilde{s}(\alpha) = s + \alpha\psi$ (eq 6) for market access. Consistent.
- **Growth:** $g^A$, $g^N$, $g$ (common case), $G(s_t)$ aggregate growth factor. Consistent.
- **Singularity:** $\lambda$, $\theta$, $\phi$, $J(s_t)$ consumption jump factor (eq 5). Consistent.
- **Market access:** $\alpha$, $\psi$. Consistent.
- **Pricing:** $M_{t,t+1}$ SDF (eq 7), $a$ effective discount factor (eq 8), $\bar{v}$ benchmark P/D (eq 9), $v^A$, $v^N$ P/D ratios. $a_t^A$ for differential growth (eq 12). Consistent; $a_t^A$ reduces to $a$ in the baseline case as expected.
- **Extension:** $\delta$, $\delta_H$, $\delta_O$, $\pi$, $Y_O$, $d$, $\eta$, $J_O$, $\omega(\alpha)$. All introduced cleanly and used consistently.

No notation conflicts found.

## Condition 2: Consistent Assumptions — PASS

Key assumptions:
1. $\gamma > 1$, $\beta \in (0,1)$ (CRRA preferences, eq 1)
2. $c_t = D_t^A + D_t^N$ (market clearing, eq 2)
3. $g^A \geq g^N > 0$ (growth rates, eq 4)
4. $\lambda \in (0,1)$ (singularity probability)
5. $\theta > 0$ (AI dividend jump, eq 5)
6. $\phi \in (0,1)$ (non-AI dividend drop, eq 5)
7. $a < 1$ (finite valuations, eq 8)
8. $\alpha \in [0,1]$, $\psi > 0$ (market access, eq 6)
9. $\delta \in [0,1)$ (extinction probability)

Consistency check: Assumption 7 ($a < 1$) follows from assumptions 1 and 3: $a = \beta(1+g)^{1-\gamma}$ with $\beta < 1$, $g > 0$, $\gamma > 1$ implies $(1+g)^{1-\gamma} < 1$, so $a < 1$. All parameter domains are compatible. No pair of assumptions is contradictory.

## Condition 3: Logical Results — FAIL

**Proposition 1 (Equilibrium Valuations):** Verified. The Euler equation expands correctly into the two-state formula. Solving for $v^A$ and substituting $1 + \bar{v} = 1/(1-a)$ yields eq (10). Numerically confirmed: all values in Table 1 match to stated precision.

**Proposition 2 (Hedging Premium):** Verified. Eq (11) follows from subtracting eq (10b) from eq (10a). Parts (i)–(iii) verified analytically. Decomposition (eq 11) confirmed.

**Corollary 1 (Partial Market Access):** Verified. Follows from Prop 2(ii) and $\tilde{s}$ increasing in $\alpha$.

**Corollary 2 (Welfare):** Verified. The value function is separable in $c$ and $s$ under CRRA with geometric growth. $W(\tilde{s}) = [1-a+\lambda a J(\tilde{s})^{1-\gamma}]/[(1-a)(1-(1-\lambda)a)]$. The consumption-equivalent variation follows. Welfare gains in Table 2 confirmed numerically (0.9%, 1.8%, 3.3%).

**Proposition 3 (Extinction):** Verified. The extinction state contributes $M \times 0 = 0$ to the Euler equation (payoffs are zero regardless of SDF). Scaling by $(1-\delta)$ is correct. Table 3 values confirmed.

**Proposition 4 (Disagreement):** Verified. The four sub-states decompose correctly. Eq (16) confirmed algebraically.

**Proposition 5 (Hump-Shaped):** Verified. Part (i): $(1-\pi)\theta \to 0$ under super-linear growth. Part (ii): $J > 1$ threshold at $\theta > \phi(1-s)/s$ is correct.

**Tables 1–3 and sensitivity table:** All numerical values confirmed to stated precision.

**FAILURE: Inline $\eta$ robustness computation.** The paper states the effective hedging amplifier $(1-\eta)J^{-\gamma} + \eta J_O^{-\gamma}$ equals 1.81 at $\eta=0$, 1.50 at $\eta=0.10$, and 1.21 at $\eta=0.20$, with $J \approx 0.82$, $\gamma=3$, $J_O \approx 1.5$. The formula gives:
- $\eta=0$: $1.81$ (correct)
- $\eta=0.10$: $0.9 \times 1.814 + 0.1 \times 0.296 = 1.662$ (paper claims 1.50)
- $\eta=0.20$: $0.8 \times 1.814 + 0.2 \times 0.296 = 1.510$ (paper claims 1.21)

The claimed values cannot be derived from the stated formula and parameters. The discrepancy is large (10–20%). An alternative formula $[(1-\eta)J + \eta J_O]^{-\gamma}$ gives 1.43 and 1.14 respectively—closer but still inconsistent with the claims. No parameterization of the stated formula reproduces the claimed values.

## Condition 4: Interpretations — PASS (conditional on Condition 3 failure)

All key verbal economic claims are supported by the formal theory:

1. "Hedging demand is part of the explanation" for high AI valuations — supported by $v^A > v^N$ (Prop 2).
2. "Incomplete markets roughly double the premium" — $J^{-\gamma} \approx 1.81$ at baseline.
3. Premium increasing in $\lambda$, decreasing in $s$ — Prop 2(i)–(ii).
4. "If markets were complete, the hedging amplification would vanish" — $\tilde{s} \to$ large value, $J \to 1$, amplifier $\to 1$.
5. Non-AI valuations rise with singularity risk — confirmed from $J^{-\gamma}(1-\phi) \approx 1.27 > 1$.
6. "AI stocks cannot hedge extinction" — Prop 3, $(1-\delta)$ scaling.
7. "Disagreement about extinction risk can partially unwind the friction" — Prop 4.
8. "Broader market access makes the household unambiguously better off" — Corollary 2, $\omega > 0$.
9. Self-limiting mechanism — $J(s_t)$ rising toward 1 as $s_t$ grows, confirmed analytically.
10. Hump-shaped hedging amplification — Prop 5.

The qualitative claims in the $\eta$ robustness paragraph ("premium remains substantial," "degrades smoothly") are directionally correct, but the specific numerical values cited are wrong (see Condition 3).
