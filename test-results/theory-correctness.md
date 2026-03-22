# tests/theory-correctness.py
Started: 2026-03-22 11:01:58 EDT
Runtime: 4m 54s
[ralph-garage/agent-logs/20260322T150158.740094Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T150158.740094Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All mathematical objects are notationally consistent, assumptions are mutually compatible, all results derive logically from the assumptions, and verbal claims are supported by the formal theory.

## Condition 1: Notational Consistency

All mathematical objects grouped by concept:

| Concept | Symbols | Consistent? |
|---|---|---|
| Consumption | $c_t$ | Yes |
| Dividends | $D_t^A$, $D_t^N$ | Yes |
| Preferences | $\beta$, $\gamma$ | Yes |
| Growth rates | $g^A$, $g^N$, $g$ (common case) | Yes |
| Singularity parameters | $\lambda$, $\theta$, $\phi$ | Yes |
| AI dividend share | $s_t$, $s$ | Yes |
| Consumption jump factor | $J(s_t)$, $J$ | Yes |
| Aggregate growth factor | $G(s_t)$ | Yes |
| Effective discount factor | $a$ | Yes |
| Price-dividend ratios | $v^A$, $v^N$, $\bar{v}$ | Yes |
| SDF | $M_{t,t+1}$ | Yes |
| Market access | $\alpha$, $\psi$, $\tilde{s}(\alpha)$ | Yes |
| Extinction | $\delta$, $\delta_H$, $\delta_O$ | Yes (generalized in extension) |
| Friction resolution | $\pi$ | Yes |
| AI output / adverse selection | $Y_O$, $d$ | Yes |
| Insider pricing | $\eta$, $J_O$ | Yes |
| Welfare | $\omega(\alpha)$ | Yes |
| Hedging component | $\Delta^{\text{hedge}}$ | Yes |
| Recursive discount | $a_t^A$ | Yes |

No notational inconsistencies found.

## Condition 2: Consistent Assumptions

All mathematical assumptions:

1. $\gamma > 1$, $\beta \in (0,1)$ (CRRA preferences)
2. $c_t = D_t^A + D_t^N$ (consumption = total dividends)
3. $s_t \equiv D_t^A / c_t$ (AI share definition)
4. $\lambda \in (0,1)$ (singularity probability)
5. $g^A \geq g^N > 0$ (positive growth, AI weakly faster)
6. $\theta > 0$ (positive AI dividend jump)
7. $\phi \in (0,1)$ (fractional non-AI drop)
8. $a \equiv \beta(1+g)^{1-\gamma} < 1$ (finite valuations)
9. $\alpha \in [0,1]$, $\psi > 0$ (market access)
10. $\delta \in [0,1)$ (extinction probability)
11. $Y_O \geq d > 0$, $Y_O$ super-linear in $\theta$ (infinite output extension)

Cross-checks:
- Assumption 8 ($a < 1$) is consistent with assumptions 1 and 5: $a = \beta(1+g)^{1-\gamma}$ with $\beta < 1$ and $(1+g)^{1-\gamma} < 1$ (since $\gamma > 1$, $g > 0$), so $a < 1$.
- The negative singularity condition $J < 1$ requires $s < \phi/(\theta+\phi)$. At baseline ($s=0.15$, $\phi=0.30$, $\theta=0.50$): $\phi/(\theta+\phi) = 0.375 > 0.15$. Consistent.
- All parameter ranges are mutually compatible.

No contradictions found.

## Condition 3: Logical Results

**Post-singularity P/D (eq 6):** $\bar{v} = a/(1-a)$. Standard Gordon growth model with deterministic growth $g$ and effective discount $a$. Correctly derived. ✓

**SDF (eq 7):** $M_{t,t+1} = \beta(c_{t+1}/c_t)^{-\gamma}$. Standard CRRA Euler condition. The two-state SDF values follow directly from normal growth ($c_{t+1}/c_t = 1+g$) and singularity growth ($c_{t+1}/c_t = (1+g)J$). ✓

**Proposition 1 (eqs 7–8):** Verified by expanding the Euler equation $v^A = E_t[M_{t,t+1}(D_{t+1}^A/D_t^A)(1+v_{t+1}^A)]$ into its two branches, solving the linear equation for $v^A$, and substituting $1+\bar{v} = 1/(1-a)$. The algebra reproduces the claimed expressions exactly. ✓

**Jump factor (eq 5):** $J(s_t)$ correctly computes the ratio of singularity-to-normal consumption growth. With $g^A = g^N = g$: $J = 1 - \phi + (\theta+\phi)s$. Verified by direct substitution. ✓

**Proposition 2 (eq 9):** Subtracting eq (8) from eq (7): numerator difference is $\lambda a J^{-\gamma}[(1+\theta)-(1-\phi)] = \lambda a J^{-\gamma}(\theta+\phi)$. ✓
- Part (i): The derivative $\partial/\partial\lambda$ of $\lambda/(1-a+\lambda a)$ is $(1-a)/(1-a+\lambda a)^2 > 0$. ✓
- Part (ii): $\partial J/\partial s = \theta+\phi > 0$; since $J < 1$ and $\gamma > 1$, $J^{-\gamma}$ is decreasing in $s$. ✓
- Part (iii): At $\lambda=0$, both P/D equal $\bar{v}$, ratio = 1. At $\lambda=1$, $v^i = aJ^{-\gamma}F^i/(1-a)$, ratio = $(1+\theta)/(1-\phi)$. ✓

**Decomposition (eq 10):** Factoring $J^{-\gamma}$ from the premium separates cash-flow and hedging components. ✓

**Corollary 1 (partial access):** $\tilde{s}(\alpha) = s + \alpha\psi$ increasing in $\alpha$; premium decreasing in effective share by Prop 2(ii). ✓

**Corollary 2 (welfare, eq 11):** Derived value function $V_t = [c_t^{1-\gamma}/(1-\gamma)] \cdot W(\tilde{s})$ where $W = [1-a+\lambda a J(\tilde{s})^{1-\gamma}]/[(1-a)(1-(1-\lambda)a)]$. Verified by substituting into the Bellman equation. Consumption-equivalent variation follows from $(1+\omega)^{1-\gamma}W(s) = W(\tilde{s})$. Positivity: $J$ increasing in $\tilde{s}$, $1-\gamma < 0$, so $J^{1-\gamma}$ decreasing, $W$ decreasing in $\tilde{s}$, meaning welfare improves. ✓

**Recursive formula (eq 12):** With $g^A \neq g^N$, the asset-specific discount $a_t^A = \beta(1+g^A)G(s_t)^{-\gamma}$ correctly captures AI dividend growth and aggregate consumption growth. ✓

**Expected returns (eq 13):** Standard asset pricing identity $E[R^i] - R^f = -R^f\text{Cov}(M, R^i)$. AI stocks have high returns when $M$ is high (singularity state), so $\text{Cov}(M, R^A) > \text{Cov}(M, R^N)$, implying lower expected excess returns for AI stocks. ✓

**Proposition 3 (extinction, eq 14):** Extinction state contributes zero to the Euler equation (both dividends and prices are zero). The surviving-singularity contribution is scaled by $(1-\delta)$. Premium linearly decreasing in $\delta$. ✓

**Proposition 4 (disagreement, eq 15):** Four sub-states correctly identified: extinction ($\lambda\delta_H$), survive + friction persists ($\lambda(1-\delta_H)(1-\pi)$), survive + friction resolves ($\lambda(1-\delta_H)\pi$), no singularity ($1-\lambda$). Each contribution correctly computed and summed. ✓

**Proposition 5 (hump-shaped, eq 16):** Hedging component $\Delta^{\text{hedge}} = (1-\pi)(J^{-\gamma}-1)(\theta+\phi) \cdot C$. As $\theta \to \infty$: $J \sim s\theta \to \infty$, $J^{-\gamma} \to 0$, $(1-\pi) = d/Y_O \to 0$ (super-linear condition), $|(\theta+\phi)(J^{-\gamma}-1)| \sim \theta$, product $(d\theta/Y_O) \to 0$. Part (ii): $J$ crosses 1 at $\theta = \phi(1-s)/s$, making hedging amplifier negative; combined with friction resolution, $\Delta^{\text{hedge}} \to 0$ from below. ✓

**$\eta$-robustness numerical checks:** $(1-\eta)J^{-\gamma} + \eta J_O^{-\gamma}$ with $J^{-3} \approx 1.81$, $J_O^{-3} \approx 0.296$. At $\eta=0$: 1.81; $\eta=0.10$: $0.9(1.81)+0.1(0.296) = 1.66$; $\eta=0.20$: $0.8(1.81)+0.2(0.296) = 1.51$. All match. ✓

## Condition 4: Interpretations

| Claim | Support |
|---|---|
| AI stocks command a valuation premium | Prop 2, eq (9): premium > 0 |
| Premium increases with singularity probability | Prop 2(i) |
| Premium decreases with AI share | Prop 2(ii) |
| Incomplete markets amplify the premium | Decomposition eq (10): $J^{-\gamma} > 1$ when $J < 1$ |
| Complete markets eliminate hedging amplification | $\tilde{s} \to$ full access $\Rightarrow J \to 1 \Rightarrow J^{-\gamma} \to 1$ |
| Hedging roughly doubles the cash-flow premium | $J^{-\gamma} \approx 1.81$ at baseline; "roughly doubles" is acceptable |
| Self-limiting mechanism as AI share grows | $s \uparrow \Rightarrow J \uparrow \Rightarrow J^{-\gamma} \downarrow$ (Prop 2(ii)) |
| Non-AI valuations also rise with singularity risk | $J^{-\gamma}(1-\phi) \approx 1.27 > 1$ at baseline, so adjustment positive |
| AI stocks earn lower expected returns than non-AI | Eq (13): positive $\text{Cov}(M, R^A - R^N)$ implies negative excess return differential |
| High realized returns consistent with low expected returns | Peso problem + belief revisions: standard, logically sound |
| Extinction reduces premium linearly | Prop 3: factor $(1-\delta)$ |
| Disagreement can unwind the friction | Prop 4: $\pi$ increasing in $\delta_O$, premium decreasing in $\pi$ |
| Hump-shaped hedging amplification | Prop 5: hedging component rises then falls to zero |
| Broadening access continuously reduces premium | Cor 1 |
| Welfare gain from access is positive and increasing | Cor 2, eq (11) |

All key verbal claims are supported by the formal theory.
