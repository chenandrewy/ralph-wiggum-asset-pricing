# tests/theory-correctness.py
Started: 2026-03-22 11:51:47 EDT
Runtime: 5m 28s
[ralph-garage/agent-logs/20260322T155147.273844Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T155147.273844Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All mathematical objects are consistently defined, assumptions are mutually compatible, all results derive logically from assumptions, and verbal claims are supported by formal theory.

## 1. Notational Consistency

All mathematical objects were catalogued and grouped by economic concept:

- **Consumption/Income:** $c_t$, $D_t^A$, $D_t^N$, $L_t$ — consistently defined with $c_t = D_t^A + D_t^N + L_t$ throughout.
- **Shares:** $s_t \equiv D_t^A/c_t$, $\ell_t \equiv L_t/c_t$, non-AI share $1 - s_t - \ell_t$ — used consistently; baseline uses $s, \ell$ (time-invariant) when $g^A = g^N$.
- **Preferences:** $\gamma > 1$ (CRRA), $\beta \in (0,1)$ — no conflicts.
- **Growth:** $g^A, g^N, g^L = g^N$; baseline $g^A = g^N \equiv g$ — consistent usage; $G(s_t)$ correctly reduces to $1+g$ when $g^A = g^N$.
- **Singularity:** $\lambda, \theta, \phi, \phi_L$ — defined once and used consistently.
- **Derived quantities:** $a \equiv \beta(1+g)^{1-\gamma}$; $\bar{v} = a/(1-a)$; $J(s_t,\ell_t)$ — all reduce correctly under baseline assumptions. The asset-specific discount factor $a_t^A \equiv \beta(1+g^A)G(s_t)^{-\gamma}$ reduces to $a$ when $g^A = g^N$.
- **Market access:** $\alpha, \psi, \tilde{s}(\alpha)$ — consistently defined and propagated through pricing formulas.
- **Extension:** $\delta, \delta_H, \delta_O, \pi, Y_O, d$ — no conflicts.
- **Business cycle:** $\sigma, \epsilon_{t+1}, b^A, b^N$ — consistently defined.

No notational inconsistencies found.

## 2. Consistent Assumptions

All mathematical assumptions listed:

1. CRRA utility with $\gamma > 1$, $\beta \in (0,1)$ (eq 1)
2. Consumption identity $c_t = D_t^A + D_t^N + L_t$ (eq 2)
3. Deterministic growth in both regimes (eqs 3–4), with $g^A \geq g^N > 0$, $g^L = g^N$
4. Singularity: one-time Poisson event with $\lambda \in (0,1)$, $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$
5. Finite-valuation condition $a < 1$
6. Market incompleteness: $\alpha \in [0,1]$, $\tilde{s}(\alpha) = s + \alpha\psi$, $\psi > 0$
7. Extension: $\delta \in [0,1)$; $\pi$ increasing in $\delta_O$

Compatibility checks:
- $\gamma > 1$ and $g > 0$ imply $(1+g)^{1-\gamma} < 1$, so $a = \beta(1+g)^{1-\gamma} < \beta < 1$. The assumption $a < 1$ is automatically satisfied. ✓
- Baseline calibration ($s=0.05, \ell=0.65$) satisfies $s + \ell < 1$. ✓
- $J = 0.805 < 1$ at baseline, confirming the singularity is "negative." ✓
- All parameter constraints are mutually satisfiable; no contradiction found.

## 3. Logical Results

### Proposition 1 (Equilibrium Valuations)
Verified by expanding the Euler equation $v^A = E_t[M_{t,t+1}(D_{t+1}^A/D_t^A)(1+v_{t+1}^A)]$ over the two pre-singularity states. The algebra yields eq (8) exactly. Derivation for $v^N$ is symmetric with $(1-\phi)$ replacing $(1+\theta)$. ✓

### Proposition 2 (Hedging Premium)
- Eq (10): Subtraction of (9) from (8) yields $\lambda a J^{-\gamma}(\theta+\phi)/[(1-a)(1-(1-\lambda)a)]$. ✓
- Part (i): $\partial/\partial\lambda$ of $\lambda/(1-a+\lambda a) = (1-a)/(1-a+\lambda a)^2 > 0$. ✓
- Part (ii): $\partial J/\partial s = \theta + \phi > 0$; since $J < 1$ and $\gamma > 1$, $J^{-\gamma}$ is decreasing in $J$. ✓
- Part (iii): At $\lambda=0$, ratio is 1; at $\lambda=1$, $v^A/v^N = (1+\theta)/(1-\phi)$. Verified algebraically. ✓

### Decomposition (eq 12)
Factoring $J^{-\gamma}$ from the premium expression yields cash-flow premium $\times$ hedging amplifier. ✓

### Corollary 1 (Partial Market Access)
$\tilde{s}$ increasing in $\alpha$; premium decreasing in effective AI share by Prop 2(ii). ✓

### Corollary 2 (Welfare)
Derived value function $W(\tilde{s}) = [1-a+\lambda a J(\tilde{s})^{1-\gamma}]/[(1-a)(1-(1-\lambda)a)]$ and verified the consumption-equivalent formula. Since $J$ is increasing in $\tilde{s}$ and $1-\gamma < 0$, $W$ is decreasing in $\tilde{s}$, making $\omega > 0$. Numerically confirmed: at $\alpha = 1, \psi = 0.15$, $\omega = 3.43\% \approx 3.4\%$. ✓

### Proposition 3 (Business-Cycle Augmentation)
The $O(\sigma^2)$ perturbation argument for P/D ratios is standard. The expected-return decomposition follows from independence of business-cycle shocks and the singularity indicator. ✓

### Proposition 4 (Extinction)
In the extinction state, the standard convention (following Barro 2006) is that this state contributes zero to the Euler equation. The premium scales by $(1-\delta)$, linearly decreasing. Numerically verified: at $\delta = 0.10$, $v^A = 15.86 \approx 15.9$, $v^N = 12.43 \approx 12.4$. ✓

### Proposition 5 (Disagreement)
Four sub-states traced: extinction (zero contribution), survival+friction ($J^{-\gamma}$ amplifier), survival+resolved ($J=1$, cash-flow only), normal. Summing and solving yields eq (18). ✓

### Proposition 6 (Hump-Shaped)
$J = 1$ threshold at $\theta = [(1-s-\ell)\phi + \ell\phi_L]/s$ verified. Super-linear growth of $Y_O$ ensures $(1-\pi)\theta \to 0$ as $\theta \to \infty$. Sign changes of the hedging component traced correctly. ✓

### Calibration Tables
Spot-checked multiple cells across Tables 1–5:
- Table 1: $\lambda=0.02$: $v^A=16.6$, $v^N=12.8$ ✓
- Table 3 ($\gamma=5$): $v^A=12.0$, $v^N=9.1$ ✓
- Table 3 ($\phi_L=0.35$): $v^A=20.0$, $v^N=14.4$ ✓
- Table 3 ($\alpha=0.25$): $v^A=15.8$, $\omega=1.0\%$ ✓
- Table 3 ($\alpha=1.00$): $\omega=3.4\%$ ✓
- Table 4 ($\delta=0.10$): $v^A=15.9$, $v^N=12.4$ ✓

All numerical values match the formulas within rounding tolerance.

## 4. Interpretations

Key verbal claims and their formal support:

| Claim | Support |
|-------|---------|
| AI stocks command a premium increasing in singularity probability and severity | Prop 2(i) and premium formula |
| Incomplete markets are essential; complete markets eliminate hedging amplification | Corollary 1: $\alpha \to 1$ drives $J^{-\gamma} \to 1$ |
| Hedging channel survives despite small AI share (5%) because labor displacement drives consumption drop | $J = 0.805$ at baseline; the 20% labor hit on 65% share dominates |
| Self-limiting mechanism: as AI share grows, premium shrinks | Prop 2(ii) |
| Non-AI valuations also rise with singularity risk | $J^{-\gamma}(1-\phi) \approx 1.34 > 1$ at baseline |
| AI stocks earn lower expected returns in baseline (singularity-only risk) | Positive $\text{Cov}(M, R^A - R^N)$ from eq (14)–(15) |
| Business-cycle risk reconciles high betas with hedging channel | Prop 3: cyclical premium dominates returns, hedging operates through valuations |
| Extinction reduces premium linearly | Prop 4: $(1-\delta)$ scaling |
| Pessimistic AI owners loosen friction | Prop 5: premium decreasing in $\pi$ (and hence $\delta_O$) |
| Hedging amplification is hump-shaped in singularity severity when friction is endogenous | Prop 6 |
| Welfare gain from market access is unambiguously positive | Corollary 2 |

All verbal economic claims are supported by the formal results. No unsupported interpretive claims found.
