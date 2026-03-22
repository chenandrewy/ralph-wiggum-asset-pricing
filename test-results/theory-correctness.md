# tests/theory-correctness.py
Started: 2026-03-22 13:31:16 EDT
Runtime: 6m 1s
[ralph-garage/agent-logs/20260322T173116.753423Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T173116.753423Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All four conditions—notational consistency, consistent assumptions, logical results, and supported interpretations—are satisfied.

## 1. Notational Consistency

All mathematical objects are notated consistently throughout the paper. Objects grouped by concept:

- **Consumption/Income** ($c_t$, $D_t^A$, $D_t^N$, $L_t$, $s_t$, $\ell_t$): consistent definitions and usage.
- **Preferences** ($\beta$, $\gamma$): consistent.
- **Growth** ($g^A$, $g^N$, $g$, $G(s_t)$): $g$ used only in the baseline $g^A = g^N$ case; $G(s_t)$ properly defined as aggregate consumption growth factor.
- **Singularity** ($\lambda$, $\theta$, $\phi$, $\phi_L$, $J$): $J$ defined as a function of $(s_t, \ell_t)$ and simplified correctly in the baseline.
- **Valuations** ($v^A$, $v^N$, $\bar{v}$, $a$, $M_{t,t+1}$): $a_t^A$ properly distinguished from $a$ for differential growth.
- **Market access** ($\alpha$, $\psi$, $\tilde{s}$): consistent.
- **Extension** ($\delta$, $\delta_H$, $\delta_O$, $\pi$, $Y_O$, $d_0$, $\kappa$, $d$, $\mu$, $\xi$, $\eta$, $J_O$): consistent.
- **Business cycle** ($\sigma$, $\epsilon_{t+1}$, $b^A$, $b^N$): consistent.
- **Welfare** ($\omega$, $W$): consistent.

Figure 2's $\pi(\theta) = \theta^2/(d^2 + \theta^2)$ is consistent with the microfoundation $\pi = Y_O/(d + Y_O)$ under $Y_O = \theta^2/d$, which satisfies the super-linear condition.

## 2. Consistent Assumptions

All mathematical assumptions can be simultaneously satisfied:

- CRRA with $\gamma > 1$, $\beta \in (0,1)$: standard.
- Budget constraint $c_t = D_t^A + D_t^N + L_t$: well-defined.
- Growth: $g^A \geq g^N > 0$, $g^L = g^N$: no conflicts.
- Singularity: $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$, $\lambda \in (0,1)$: no conflicts.
- Finite valuations: $a = \beta(1+g)^{1-\gamma} < 1$: satisfied at baseline ($a = 0.923$).
- Negative singularity: $J < 1$ at baseline ($J = 0.805$): verified from parameter values.
- Extension parameters ($\delta$, $\pi$, $\alpha$): all bounded and compatible.

No pair of assumptions is contradictory.

## 3. Logical Results

All mathematical results verified:

- **Proposition 1 (Valuations)**: Euler equation derivation verified algebraically. Table 1 spot-checked: $v^A = 16.6$, $v^N = 12.8$ at $\lambda = 0.02$ confirmed.
- **Proposition 2 (Premium)**: Subtraction yields eq (12). Monotonicity in $\lambda$ (part i), $s$ (part ii), and bounds (part iii) verified.
- **Corollary 1 (Partial Access)**: Follows from composition of monotone functions. Numerically confirmed ($\alpha = 0.25$: $v^A/v^N = 1.27$).
- **Corollary 2 (Welfare)**: Derivation from value function verified. Sign of $\omega$ confirmed via monotonicity of $W$ in $\tilde{s}$ with $\gamma > 1$. Numerically confirmed ($\omega(1.0) = 3.4\%$).
- **Proposition 3 (Business Cycle)**: First-order invariance of P/D ratios to $\sigma^2$ perturbation is standard. Return decomposition by independence verified.
- **Proposition 4 (Extinction)**: Zero contribution from extinction state (all payoffs zero) correctly scales premium by $(1-\delta)$.
- **Proposition 5 (Disagreement)**: Four sub-states correctly weighted; friction-resolved state sets $J = 1$ while preserving cash-flow differential.
- **Proposition 6 (Hump Shape)**: Limiting behavior verified: $(1-\pi) \cdot \theta \to 0$ under super-linear condition; $J = 1$ threshold correctly identified.
- **Eq (15) (Recursive)**: Verified $a_t^A = \beta(1+g^A)G(s_t)^{-\gamma}$ is the correct asset-specific discount factor.
- **Sensitivity table**: Multiple entries verified numerically ($\gamma = 5$, $\phi = 0.50/\phi_L = 0.35$, partial access rows).
- **Table 2 hedging shares**: Verified as ratio-based decomposition; values match (e.g., 40% at 0 pp/$\lambda = 0.02$, 44% at 0 pp/$\lambda = 0.01$).

## 4. Interpretations

All key verbal claims supported by formal theory:

1. "AI stocks command a valuation premium" — Prop 2: $v^A - v^N > 0$. ✓
2. "Premium increasing in singularity probability" — Prop 2(i). ✓
3. "Premium decreasing in AI share" — Prop 2(ii). ✓
4. "Incomplete markets essential; hedging amplification vanishes with complete markets" — $J = 1 \Rightarrow J^{-\gamma} = 1$. ✓
5. "Hedging demand roughly doubles the cash-flow premium" — $J^{-3} = 1.92$ at baseline. ✓
6. "Self-limiting: premium erodes as $s_t$ rises" — dynamic application of Prop 2(ii). ✓
7. "Non-AI valuations also rise with singularity risk" — $J^{-\gamma}(1-\phi) = 1.34 > 1$. ✓
8. "AI stocks earn lower expected returns in baseline" — positive $\text{Cov}(M, R^A)$. ✓
9. "Hedging channel contributes 13–23% at empirical calibrations" — verified from Table 2. ✓
10. "Hedging premium linearly decreasing in extinction probability" — factor $(1-\delta)$ in Prop 4. ✓
11. "Welfare gain strictly positive from market access" — Cor 2. ✓
12. "Hedging component is hump-shaped in $\theta$" — Prop 6. ✓
13. "Higher labor displacement pushes hedging toward dominance" — $\partial J/\partial \phi_L = -\ell < 0$ raises $J^{-\gamma}$. ✓
