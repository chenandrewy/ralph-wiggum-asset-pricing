# tests/theory-correctness.py
Started: 2026-03-22 11:29:42 EDT
Runtime: 4m 27s
[ralph-garage/agent-logs/20260322T152942.722477Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T152942.722477Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All notation is consistent, assumptions are mutually compatible, all results follow logically from the assumptions, and all verbal claims are supported by the formal theory.

## Condition 1: Notational Consistency

All mathematical objects grouped by concept:

- **Consumption/Income:** $c_t$ (consumption), $D_t^A$ (AI dividends), $D_t^N$ (non-AI dividends), $L_t$ (labor income), $s_t \equiv D_t^A/c_t$ (AI share), $\ell_t \equiv L_t/c_t$ (labor share). Used consistently throughout.
- **Preferences:** $\beta$ (discount factor), $\gamma$ (CRRA coefficient). Defined once in eq (1), used consistently.
- **Growth:** $g^A$, $g^N$, $g^L = g^N$, $g$ (common rate when equal), $G(s_t)$ (aggregate growth factor). All consistent; $g$ is only used when $g^A = g^N$ is assumed.
- **Singularity parameters:** $\lambda$ (probability), $\theta$ (AI jump), $\phi$ (non-AI drop), $\phi_L$ (labor drop), $J$ (consumption jump factor). Defined once, used consistently.
- **Market incompleteness:** $\alpha$ (access parameter), $\psi$ (private AI capital), $\tilde{s}(\alpha) = s + \alpha\psi$ (effective share). Consistent.
- **Pricing:** $M_{t,t+1}$ (SDF), $a \equiv \beta(1+g)^{1-\gamma}$ (effective discount), $\bar{v} = a/(1-a)$ (benchmark P/D), $v^A$, $v^N$ (P/D ratios). Consistent.
- **Extensions:** $\delta$, $\delta_H$, $\delta_O$ (extinction beliefs), $\pi$ (friction resolution), $Y_O$ (AI output), $d$ (adverse-selection discount), $\omega$ (welfare), $\eta$ (insider pricing share), $J_O$ (AI owners' jump). All consistent.
- **Business cycle:** $\sigma$, $\epsilon_{t+1}$, $b^A$, $b^N$, $R^f$, $R^i$. Consistent.

**Result: PASS.** No notational inconsistencies found.

## Condition 2: Consistent Assumptions

All mathematical assumptions:

1. CRRA utility: $\gamma > 1$, $\beta \in (0,1)$ (eq 1)
2. Budget constraint: $c_t = D_t^A + D_t^N + L_t$ (eq 2)
3. Growth: $g^A \geq g^N > 0$, $g^L = g^N$ (eq 3)
4. Singularity: $\lambda \in (0,1)$, one-time event (Section 2.2)
5. Singularity parameters: $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$ (eq 4)
6. Finite valuations: $a < 1$ (eq 6)
7. Market access: $\alpha \in [0,1]$, $\psi > 0$ (eq 5)
8. Extinction: $\delta \in [0,1)$ (Section 4.1)

Consistency checks:
- Assumption 6 ($a < 1$) follows from assumptions 1 and 3: $a = \beta(1+g)^{1-\gamma}$ with $\beta < 1$ and $(1+g)^{1-\gamma} < 1$ (since $\gamma > 1$, $g > 0$). Consistent.
- The budget constraint (2) and growth processes (3, 4, 5) are jointly consistent—they describe different states with non-overlapping conditions.
- All parameter ranges are compatible with each other.

**Result: PASS.** No contradictions among assumptions.

## Condition 3: Logical Results

### Proposition 1 (Equilibrium Valuations, eqs 7–8)
Verified by expanding the Euler equation $v^A = E_t[M_{t,t+1}(D_{t+1}^A/D_t^A)(1+v_{t+1}^A)]$ in the pre-singularity regime. With probability $(1-\lambda)$: SDF $= \beta(1+g)^{-\gamma}$, dividend growth $= 1+g$, next P/D $= v^A$. With probability $\lambda$: SDF $= \beta[(1+g)J]^{-\gamma}$, dividend growth $= (1+g)(1+\theta)$, next P/D $= \bar{v}$. Solving yields eq (7). Derivation for eq (8) is identical with $(1-\phi)$ replacing $(1+\theta)$. **Verified.**

Numerical check at baseline ($\beta=0.96$, $\gamma=3$, $g=0.02$, $\lambda=0.02$): $a = 0.96/1.0404 \approx 0.9227$, $\bar{v} \approx 11.94$, $J = 0.805$, $J^{-3} \approx 1.917$. Computed $v^A \approx 16.6$, $v^N \approx 12.8$. **Matches Table 1.**

Also verified $\lambda = 0.05$: $v^A \approx 21.0$, $v^N \approx 13.6$. **Matches Table 1.**

### Proposition 2 (Hedging Premium, eq 9)
Subtracting eq (8) from eq (7) yields $J^{-\gamma}[(1+\theta)-(1-\phi)] = J^{-\gamma}(\theta+\phi)$. **Verified.**

- Part (i): $f(\lambda) = \lambda/(1-a+\lambda a)$ has $f'(\lambda) = (1-a)/(1-a+\lambda a)^2 > 0$. **Verified.**
- Part (ii): $\partial J/\partial s = (1+\theta)-(1-\phi) = \theta+\phi > 0$. Since $J < 1$ and $\gamma > 1$, $J^{-\gamma}$ is decreasing in $J$, so premium decreases in $s$. **Verified.**
- Part (iii): At $\lambda=0$, ratio is 1. At $\lambda=1$, $v^i = aJ^{-\gamma}F^i/(1-a)$, giving ratio $(1+\theta)/(1-\phi)$. **Verified.**

### Decomposition (eq 11)
Factoring $J^{-\gamma}$ from eq (9): cash-flow premium $\times$ hedging amplifier. Risk-neutral limit ($\gamma \to 0$): $J^{-\gamma} \to 1$. At baseline: $J^{-3} \approx 1.92$. **Verified.**

### Corollary 1 (Partial Market Access)
$\tilde{s}(\alpha) = s + \alpha\psi$ increasing in $\alpha$; premium decreasing in effective share by Prop 2(ii). **Verified.**

### Corollary 2 (Welfare, eq 15)
Computed $\omega(1) = 0.9348^{-0.5} - 1 \approx 3.42\% \approx 3.4\%$ at $\alpha=1$, $\psi=0.15$. Also verified $\omega(0.25) \approx 1.0\%$. **Matches Table 3.**

### $\eta$-Robustness (inline numbers)
$(1-\eta)J^{-\gamma} + \eta J_O^{-\gamma}$ with $J^{-3} \approx 1.92$, $J_O^{-3} = 1.5^{-3} \approx 0.296$: at $\eta=0$: 1.92, at $\eta=0.10$: 1.76, at $\eta=0.20$: 1.60. **Verified.**

### Sensitivity Table (Table 3)
Spot-checked $\gamma=5$: $a \approx 0.887$, $\bar{v} \approx 7.84$, $J^{-5} \approx 2.96$, yielding $v^A \approx 12.0$, $v^N \approx 9.1$. **Matches.**

### Recursive formula (eq 13)
With differential growth, verified that $a_t^A = \beta(1+g^A)G(s_t)^{-\gamma}$ is the correct asset-specific discount factor from the SDF and AI dividend growth. Singularity contribution involves $a_t^A \cdot J^{-\gamma}(1+\theta)$ by the same logic. **Verified.**

### Proposition 3 (Extinction, eq 14)
Extinction state: $D_{t+1}^i = 0$, $P_{t+1}^i = 0$, contributing 0 to Euler equation (standard treatment following Barro 2006). Surviving singularity contribution scaled by $(1-\delta)$. Premium: $(1-\delta)$ times the baseline premium. **Verified.**

### Proposition 4 (Disagreement, eq 16)
Singularity splits into extinction ($\lambda\delta_H$, zero contribution), survive+friction ($\lambda(1-\delta_H)(1-\pi)$, amplifier $J^{-\gamma}$), and survive+resolved ($\lambda(1-\delta_H)\pi$, amplifier 1). Summing gives $(\theta+\phi)[(1-\pi)J^{-\gamma}+\pi]$. **Verified.**

### Proposition 5 (Hump-shaped)
Part (i): $J \approx s\theta$ for large $\theta$, so $|J^{-\gamma}-1| \to 1$ and $(\theta+\phi) \sim \theta$. Super-linear condition $Y_O/\theta \to \infty$ ensures $(1-\pi)\theta \to 0$. **Verified.**
Part (ii): $J$ crosses 1 at $\theta = [(1-s-\ell)\phi + \ell\phi_L]/s$, making $J^{-\gamma}-1$ negative. Hedging component goes positive → negative → 0. **Verified.**

### Expected Returns (eqs 15–17)
Standard asset pricing: $E[R^i]-R^f = -R^f\text{Cov}(M,R^i)$. AI stocks have positive SDF covariance in singularity state (high M, high return), yielding hedging discount. Business-cycle augmentation adds positive premium from cyclical beta. Decomposition is standard. **Verified.**

**Result: PASS.** All results logically derived from assumptions.

## Condition 4: Interpretations

Key verbal claims and their formal support:

1. "AI stocks command a valuation premium increasing in singularity probability" → Proposition 2(i). **Supported.**
2. "Premium decreasing in AI dividend share" → Proposition 2(ii). **Supported.**
3. "Incomplete markets are essential; if complete, hedging amplification vanishes" → As $\alpha \to 1$, $\tilde{s}$ rises, $J \to 1$, $J^{-\gamma} \to 1$. Corollary 1. **Supported.**
4. "Hedging channel survives realistic consumption composition because singularity displaces labor" → $\phi_L > 0$ on $\ell = 0.65$ drives $J < 1$ even with $s = 0.05$. **Supported.**
5. "Hedging demand roughly doubles the cash-flow premium" → $J^{-\gamma} \approx 1.92$ at baseline. Eq (11). **Supported.**
6. "Non-AI valuations rise with singularity risk" → $J^{-\gamma}(1-\phi) \approx 1.34 > 1$. Eq (8). **Supported.**
7. "AI stocks earn lower expected returns in baseline" → Positive $\text{Cov}(M, R^A-R^N)$ from singularity channel. Eq (16). **Supported.**
8. "Business-cycle risk reconciles high betas with hedging channel" → Eq (17) decomposes into positive cycle premium and negative hedging discount. **Supported.**
9. "Self-limiting mechanism: premium erodes as AI share grows" → Dynamic model: $s_t$ rises, $J_t \to 1$, amplifier declines. Eq (13). **Supported.**
10. "Extinction risk reduces premium linearly" → Factor $(1-\delta)$ in Proposition 3. **Supported.**
11. "Disagreement partially unwinds friction" → $\pi$ increasing in $\delta_O$ lowers amplifier. Proposition 4. **Supported.**
12. "Hedging amplification is hump-shaped when friction resolution depends on AI output" → Proposition 5. **Supported.**
13. "Welfare gains of up to 3.4% from full market access" → Corollary 2, verified numerically. **Supported.**
14. "Model generates valuation ratios of 1.8–2.3× with differential growth" → Table 2 at $g^A-g^N$ = 3–5pp, $\lambda$ = 0.02–0.05. **Supported.**

**Result: PASS.** All verbal claims are supported by the formal theory.
