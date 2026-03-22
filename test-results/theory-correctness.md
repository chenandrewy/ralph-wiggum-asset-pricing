# tests/theory-correctness.py
Started: 2026-03-22 12:03:03 EDT
Runtime: 5m 25s
[ralph-garage/agent-logs/20260322T160303.667996Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T160303.667996Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All notation is consistent, assumptions are compatible, derivations are correct, and verbal claims are supported by the formal theory.

## Condition 1: Notational Consistency

All mathematical objects were cataloged and grouped by concept. No inconsistencies found.

| Concept | Symbols | Consistent? |
|---|---|---|
| Consumption | $c_t$ | Yes |
| Dividends | $D_t^A$, $D_t^N$ | Yes |
| Labor income | $L_t$ | Yes |
| Income shares | $s_t \equiv D_t^A/c_t$, $\ell_t \equiv L_t/c_t$ | Yes |
| Preferences | $\beta$, $\gamma$ | Yes |
| Growth rates | $g^A$, $g^N$, $g^L = g^N$ | Yes |
| Singularity | $\lambda$, $\theta$, $\phi$, $\phi_L$ | Yes |
| Jump factor | $J(s_t, \ell_t)$ | Yes |
| SDF | $M_{t,t+1}$ | Yes |
| Effective discount | $a \equiv \beta(1+g)^{1-\gamma}$ | Yes |
| P/D ratios | $v^A$, $v^N$, $\bar{v}$ | Yes |
| Market access | $\alpha$, $\tilde{s}(\alpha)$, $\psi$ | Yes |
| Extinction | $\delta$, $\delta_H$, $\delta_O$ | Yes |
| Friction resolution | $\pi$ | Yes |
| Business cycle | $\sigma$, $\epsilon_{t+1}$, $b^A$, $b^N$ | Yes |
| Welfare | $\omega(\alpha)$ | Yes |

## Condition 2: Consistent Assumptions

All assumptions listed:

1. CRRA utility: $\gamma > 1$, $\beta \in (0,1)$
2. Budget: $c_t = D_t^A + D_t^N + L_t$
3. Growth: $g^A \geq g^N > 0$, $g^L = g^N$
4. Singularity: one-time event, probability $\lambda \in (0,1)$
5. Singularity shocks: $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$
6. Finite valuations: $a < 1$
7. Market access: $\alpha \in [0,1]$, $\psi > 0$
8. Extinction: $\delta \in [0,1)$
9. Business cycle: i.i.d. mean-zero shocks

No contradictions. Since $\gamma > 1$ implies $(1+g)^{1-\gamma} < 1$, the condition $a = \beta(1+g)^{1-\gamma} < 1$ is automatically satisfied. All parameter ranges are compatible.

## Condition 3: Logical Results

All derivations verified:

- **Proposition 1 (Equilibrium Valuations):** Euler equation for $v^A$ correctly expanded and solved. Verified numerically against Table 1 (all four rows match within rounding).
- **Proposition 2 (Hedging Premium):** Difference $v^A - v^N$ correctly computed. Parts (i)-(iii) verified: monotonicity in $\lambda$, monotonicity in $s$ via $\partial J/\partial s = \theta + \phi > 0$, and bounds at $\lambda \in \{0,1\}$.
- **Decomposition (eq 11):** Correct factoring of $J^{-\gamma}$ from the premium formula.
- **Corollary 1 (Partial Market Access):** Follows from Prop 2(ii) via chain rule with $\tilde{s}(\alpha) = s + \alpha\psi$.
- **Corollary 2 (Welfare):** Verified sign of $\omega$ using $1-\gamma < 0$ and monotonicity of $J$ in $\tilde{s}$. Numerically verified: $\omega(0.50) \approx 1.9\%$, $\omega(1.00) \approx 3.4\%$.
- **Recursive formula (eq 14):** Correctly generalizes to $g^A \neq g^N$ with asset-specific discount factor $a_t^A$.
- **Proposition 3 (Business Cycle):** P/D ratios unchanged at first order in $\sigma^2$; return decomposition follows from independence of business-cycle shocks and singularity indicator.
- **Proposition 4 (Extinction):** Premium scaled by $(1-\delta)$. Verified numerically against Table 4.
- **Proposition 5 (Disagreement):** Four sub-states correctly enumerated; formula (eq 17) verified.
- **Proposition 6 (Hump-Shaped):** Threshold $\theta = [(1-s-\ell)\phi + \ell\phi_L]/s$ for $J=1$ is correct. Asymptotic behavior verified.

Spot-checked Table 3 sensitivity rows ($\gamma=5$; $\phi_L=0.35$; $\alpha=0.25,0.50,1.00$) — all match within rounding.

## Condition 4: Interpretations

Key verbal claims and their formal support:

1. "AI stocks command a valuation premium due to hedging demand" — Prop 2: $v^A - v^N > 0$.
2. "Premium increasing in singularity probability" — Prop 2(i).
3. "Premium decreasing in AI share" — Prop 2(ii).
4. "Hedging demand roughly doubles the cash-flow premium" — $J^{-\gamma} \approx 1.92$ at baseline.
5. "Incomplete markets are essential; complete markets eliminate hedging amplification" — Cor 1: $\alpha \to 1$ drives $J \to 1$.
6. "Non-AI valuations also rise with singularity risk" — $J^{-\gamma}(1-\phi) \approx 1.34 > 1$.
7. "Hedging channel contributes 13--23% at empirical calibrations" — Consistent with Table 2 hedging shares.
8. "Under severe calibrations, hedging share exceeds 50%" — Verified for $\gamma=5$, $\phi=0.50$, $\phi_L=0.35$: hedging share $\approx 91\%$.
9. "Business-cycle risk reconciles high betas with hedging discount" — Prop 3(ii).
10. "Self-limiting mechanism as AI share grows" — $s_t$ rising causes $J_t \to 1$, reducing hedging amplifier.
11. "Welfare gain from broadening market access" — Cor 2: $\omega > 0$.
12. "AI stocks cannot hedge extinction" — Prop 4: zero payoff in extinction state.
13. "Insider pricing robust for $\eta \leq 0.20$" — Even with $J_O^{-\gamma} = 0$, effective amplifier $\geq 0.80 \times 1.92 = 1.53 \gg 1$.

All verbal claims are supported by the formal results.
