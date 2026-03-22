# tests/theory-correctness.py
Started: 2026-03-22 13:21:40 EDT
Runtime: 4m 40s
[ralph-garage/agent-logs/20260322T172140.396226Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T172140.396226Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All mathematical notation, assumptions, derivations, and verbal interpretations are internally consistent and correctly derived.

## 1. Notational Consistency

All mathematical objects grouped by concept:

- **Consumption/utility:** $c_t$, $\gamma$, $\beta$, $E_0$ — used consistently throughout.
- **Dividends/income:** $D_t^A$, $D_t^N$, $L_t$, $s_t \equiv D_t^A/c_t$, $\ell_t \equiv L_t/c_t$ — defined once (eq 2) and used consistently.
- **Growth rates:** $g^A$, $g^N$, $g^L = g^N$, $g$ (common-growth baseline where $g^A = g^N \equiv g$), $G(s_t)$ — no conflicts; the distinction between general and baseline cases is clearly stated.
- **Singularity parameters:** $\lambda$, $\theta$, $\phi$, $\phi_L$, $J(s_t, \ell_t)$ — consistently defined and used.
- **Market access:** $\alpha$, $\psi$, $\tilde{s}(\alpha) = s + \alpha\psi$ — consistent.
- **Pricing:** $M_{t,t+1}$, $a \equiv \beta(1+g)^{1-\gamma}$, $\bar{v}$, $v^A$, $v^N$ — consistent. The asset-specific $a_t^A$ in eq (8) is clearly distinguished from the common-growth $a$.
- **Extension:** $\delta$, $\delta_H$, $\delta_O$, $\pi$, $Y_O$, $q$, $\mu$, $\xi$, $d_0$, $\kappa$, $d = d_0/\kappa$ — all introduced with clear definitions and used consistently.
- **Business cycle:** $\sigma$, $\epsilon_{t+1}$, $b^A$, $b^N$, $R^f$, $R^i$ — consistent.

No notational conflicts found.

## 2. Consistent Assumptions

All mathematical assumptions:

1. CRRA utility: $\gamma > 1$, $\beta \in (0,1)$ (eq 1)
2. Budget constraint: $c_t = D_t^A + D_t^N + L_t$ (eq 2)
3. Normal transition: deterministic growth at $g^A$, $g^N$, $g^L = g^N$ (eq 3)
4. Growth ordering: $g^A \geq g^N > 0$
5. Singularity: probability $\lambda \in (0,1)$, one-time event (eq 4)
6. Singularity parameters: $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$
7. Finite valuations: $a < 1$
8. Market access: $\alpha \in [0,1]$, $\psi > 0$
9. Extension: $\delta \in [0,1)$, $\pi \in [0,1]$

Consistency checks:
- **Assumption 7 ($a < 1$):** With $\beta < 1$ and $(1+g)^{1-\gamma} < 1$ (since $\gamma > 1$, $g > 0$), $a < 1$ is automatically satisfied. Consistent with assumptions 1 and 4.
- **Negative singularity ($J < 1$):** At baseline, $J = 0.805 < 1$. Consistent with the parameter ranges in assumptions 5–6.
- **Budget constraint holds in all states:** Normal transition scales all income streams; singularity transition scales them asymmetrically but $c_{t+1}$ remains the sum of the three scaled components. No violation.

All assumptions are mutually consistent.

## 3. Logical Results

### Proposition 1 (Equilibrium Valuations, eqs 7–8)
Verified by expanding the Euler equation $v^A = E_t[M_{t,t+1}(D_{t+1}^A/D_t^A)(1+v_{t+1}^A)]$:
- No-singularity branch: $(1-\lambda) \cdot a \cdot (1+v^A)$
- Singularity branch: $\lambda \cdot a \cdot J^{-\gamma}(1+\theta) \cdot (1+\bar{v})$

Solving yields eq (7). Algebraically verified that $\bar{v} + \lambda a[J^{-\gamma}(1+\theta)-1]/[(1-a)(1-(1-\lambda)a)]$ equals the solved expression. Derivation for $v^N$ is identical with $(1-\phi)$ replacing $(1+\theta)$. **Correct.**

### Proposition 2 (Hedging Premium, eq 9)
- Subtraction of eqs 7–8 yields $\lambda a J^{-\gamma}(\theta+\phi)/[(1-a)(1-(1-\lambda)a)]$. **Correct.**
- Part (i): $\partial/\partial\lambda[\lambda/(1-a+\lambda a)] = (1-a)/(1-a+\lambda a)^2 > 0$. **Correct.**
- Part (ii): $\partial J/\partial s = (1+\theta)-(1-\phi) = \theta+\phi > 0$; since $J < 1$ and $\gamma > 1$, $J^{-\gamma}$ decreases. **Correct.**
- Part (iii): At $\lambda=0$, ratio is 1. At $\lambda=1$, $v^i = aJ^{-\gamma}F^i/(1-a)$, ratio is $(1+\theta)/(1-\phi)$. **Correct.**

### Decomposition (eq 10)
Direct factoring of $J^{-\gamma}$ from the premium formula. **Correct.**

### Corollary 1 (Partial Market Access)
$\tilde{s}(\alpha) = s + \alpha\psi$ increasing in $\alpha$; premium decreasing in effective AI share by Prop 2(ii). **Correct.**

### Corollary 2 (Welfare, eq 12)
$(1+\omega)^{1-\gamma} = W(\tilde{s})/W(s)$ where $W$ is decreasing in $\tilde{s}$ (since $J^{1-\gamma}$ is decreasing in $J$ for $\gamma > 1$). With $1-\gamma < 0$, $\omega > 0$. **Correct.**

### Proposition 3 (Business Cycle, eq 13)
Independence of $\epsilon_{t+1}$ and the singularity indicator allows covariance separation. First-order invariance of P/D ratios follows from standard perturbation. **Correct.**

### Proposition 4 (Extinction, eq 15)
Extinction state contributes zero to Euler equation (zero dividends/prices). Premium scaled by $(1-\delta)$. **Correct.**

### Proposition 5 (Disagreement, eq 14)
Four sub-states enumerated correctly. In friction-resolved state, $J=1$ so hedging amplifier is 1. Weighted average gives $(1-\pi)J^{-\gamma}+\pi$. **Correct.**

### Proposition 6 (Hump Shape)
- For large $\theta$: $J \approx s\theta \to \infty$, $(1-\pi) = O(1/Y_O) = o(1/\theta)$ by super-linear condition, so $\Delta^{\text{hedge}} \to 0$. **Correct.**
- $J = 1$ threshold: $\theta = [(1-s-\ell)\phi + \ell\phi_L]/s$. Verified algebraically. **Correct.**

### Numerical Verification (Tables 1 and 3)
Spot-checked against closed-form expressions:

| Entry | Computed | Paper | Match |
|-------|----------|-------|-------|
| $\bar{v}$ | 11.92 | 11.9 | ✓ |
| $v^A$ ($\lambda=0.01$) | 14.50 | 14.5 | ✓ |
| $v^N$ ($\lambda=0.01$) | 12.39 | 12.4 | ✓ |
| $v^A$ ($\lambda=0.05$) | 20.96 | 21.0 | ✓ |
| $v^N$ ($\lambda=0.05$) | 13.57 | 13.6 | ✓ |
| $v^A$ ($\gamma=5$) | 11.98 | 12.0 | ✓ |
| $v^N$ ($\gamma=5$) | 9.14 | 9.1 | ✓ |
| $v^A$ ($\phi=0.50,\phi_L=0.35$) | 23.17 | 23.2 | ✓ |
| $v^A-v^N$ ($\alpha=0.25$) | 3.42 | 3.4 | ✓ |
| $\omega$ ($\alpha=1.00$) | 3.42% | 3.4% | ✓ |

All numerical values are consistent with the formulas to within rounding precision.

## 4. Interpretations

Key verbal claims and their formal support:

1. "AI stocks command a valuation premium increasing in singularity probability" — Prop 2(i). ✓
2. "Premium decreasing in AI dividend share" — Prop 2(ii). ✓
3. "Incomplete markets essential: hedging amplification vanishes if markets complete" — Corollary 1: as $\alpha \to 1$, $J \to 1$, amplifier $J^{-\gamma} \to 1$. ✓
4. "Hedging demand roughly doubles the cash-flow premium" — $J^{-\gamma} \approx 1.92$ at baseline. ✓
5. "Natural self-limiting mechanism" — as $s$ rises, $J \to 1$ and premium erodes. Prop 2(ii). ✓
6. "Broader market access makes household unambiguously better off" — Corollary 2: $\omega > 0$. ✓
7. "AI stocks earn lower expected returns in baseline" — positive Cov$(M, R^A)$ from eq (11). ✓
8. "AI stocks cannot hedge extinction" — zero payoffs in extinction state. ✓
9. "Premium linearly decreasing in $\delta$" — eq (15): proportional to $(1-\delta)$. ✓
10. "Hedging amplification hump-shaped" — Prop 6. ✓
11. "Non-AI valuations also rise with singularity risk" — $J^{-\gamma}(1-\phi) \approx 1.34 > 1$. ✓
12. "13–23% hedging share at empirical calibrations" — Table 2, structural decomposition. ✓
13. "Welfare gains up to 3.4%" — Table 3. Verified numerically. ✓
14. "$J \approx 0.81$, consumption falls by 19%" — computed $J = 0.805$, consistent with stated rounding. ✓

All verbal economic claims are supported by the formal theory.
