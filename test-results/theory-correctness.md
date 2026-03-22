# tests/theory-correctness.py
Started: 2026-03-21 22:34:54 EDT
Runtime: 5m 43s
[ralph-garage/agent-logs/20260322T023454.042030Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T023454.042030Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All mathematical notation is consistent, assumptions are compatible, derivations are correct, and verbal claims are supported by the formal theory.

## Condition 1: Notational Consistency

All mathematical objects grouped by economic concept:

| Group | Symbols | Consistent? |
|-------|---------|-------------|
| Consumption | $c_t$ | Yes |
| Dividends | $D_t^A$, $D_t^N$ | Yes — superscripts A/N used throughout |
| Preferences | $\beta$, $\gamma$ | Yes |
| Dividend growth | $g$ | Yes |
| Singularity parameters | $\lambda$, $\theta$, $\phi$ | Yes |
| AI dividend share | $s$ | Yes |
| Jump factor | $J(s)$ or $J$ | Yes — defined once, shorthand used consistently |
| Effective discount factor | $a$ | Yes |
| Valuations | $v^A$, $v^N$, $\bar{v}$ | Yes |
| SDF | $M_{t,t+1}$ | Yes |
| Extinction probability | $\delta$ | Yes (extension only) |
| Prices | $P_{t+1}^i$ | Used once in extinction proof, consistent |

No notational conflicts found.

## Condition 2: Consistent Assumptions

All mathematical assumptions:

1. $\gamma > 1$, $\beta \in (0,1)$ (eq 1)
2. $c_t = D_t^A + D_t^N$ (eq 2)
3. $s \equiv D_t^A / c_t$ constant pre-singularity (eq 3)
4. $\lambda \in (0,1)$ (Section 2.2)
5. $g > 0$ common deterministic growth (eq 4)
6. Normal transition: both dividends grow at $1+g$ (eq 4)
7. Singularity transition: AI dividends multiply by $(1+\theta)(1+g)$, non-AI by $(1-\phi)(1+g)$ (eq 5)
8. $\theta > 0$, $\phi \in (0,1)$ (eq 5)
9. $a \equiv \beta(1+g)^{1-\gamma} < 1$ (eq 7)
10. $\delta \in [0,1)$ extinction probability (extension)

Consistency checks:

- **Assumption 3 vs. 6:** Under normal transition, $D_{t+1}^A/c_{t+1} = (1+g)D_t^A / [(1+g)c_t] = s$. The share is indeed constant pre-singularity. ✓
- **Assumption 9 vs. 1,5:** $a = \beta(1+g)^{1-\gamma}$. With $\beta < 1$, $g > 0$, $\gamma > 1$: $(1+g)^{1-\gamma} < 1$, so $a < \beta < 1$. Automatically satisfied. ✓
- **All assumptions can be simultaneously true** for any parameter values in the stated ranges. ✓

## Condition 3: Logical Results

### Consumption jump (eq 6)
Derived from assumptions 2, 3, 7:
$$c_{t+1}/c_t = (1+g)[(1+\theta)s + (1-\phi)(1-s)] = (1+g)[1 - \phi + (\theta+\phi)s] = (1+g)J(s)$$
✓ Correct.

### SDF values (Section 3.1)
From CRRA utility and the consumption paths: $M_{t,t+1} = \beta(c_{t+1}/c_t)^{-\gamma}$. No-singularity: $\beta(1+g)^{-\gamma}$. Singularity: $\beta[(1+g)J]^{-\gamma}$. ✓

### Proposition 1 (eqs 8–9)
Euler equation for AI stock: $v^A = E_t[M_{t,t+1}(D_{t+1}^A/D_t^A)(1+v_{t+1}^A)]$.

Expanding pre-singularity:
$$v^A = (1-\lambda)\,a\,(1+v^A) + \lambda\,a\,J^{-\gamma}(1+\theta)(1+\bar{v})$$

Solving with $1+\bar{v} = 1/(1-a)$:
$$v^A = \bar{v} + \frac{\lambda\,a\,[J^{-\gamma}(1+\theta)-1]}{(1-a)[1-(1-\lambda)a]}$$
✓ Verified algebraically. Identical derivation for $v^N$ replacing $(1+\theta)$ with $(1-\phi)$. ✓

### Proposition 2 (eq 10, parts i–iii)
- **Eq 10:** Subtracting eq 9 from eq 8: $v^A - v^N = \lambda a J^{-\gamma}(\theta+\phi)/\{(1-a)[1-(1-\lambda)a]\}$. ✓
- **Part (i):** Writing premium as $K\lambda/(1-a+\lambda a)$, derivative is $K(1-a)/(1-a+\lambda a)^2 > 0$. ✓
- **Part (ii):** $\partial J/\partial s = \theta+\phi > 0$; since $J < 1$ and $\gamma > 1$, $J^{-\gamma}$ is decreasing in $J$, so premium decreases in $s$. ✓
- **Part (iii):** At $\lambda=0$: ratio is 1. At $\lambda=1$: $v^i = aJ^{-\gamma}F^i/(1-a)$, ratio is $(1+\theta)/(1-\phi)$. ✓ Verified.

### Proposition 3 (eq 11)
With extinction, singularity-state contribution scales by $(1-\delta)$. The no-singularity path is unchanged, so the denominator $[1-(1-\lambda)a]$ is unchanged. Premium becomes $(1-\delta)$ times the base premium. ✓ Linearly decreasing in $\delta$. ✓

### Calibration (Table 1)
Verified numerically with $\beta=0.96$, $\gamma=3$, $g=0.02$, $\theta=0.50$, $\phi=0.30$, $s=0.15$:
- $a = 0.96 \times 1.02^{-2} \approx 0.92272$
- $\bar{v} = 0.92272/0.07728 \approx 11.94$ (rounds to 11.9) ✓
- $J = 1 - 0.30 + 0.80 \times 0.15 = 0.82$; consumption drop = 18% ✓
- $J^{-3} \approx 1.8137$
- At $\lambda=0.02$: $v^A \approx 16.2$, $v^N \approx 12.6$, premium $\approx 3.6$, ratio $\approx 1.29$ ✓

### Figure 1 plot formulas
The plot expressions $(0.92272 + 31.564\lambda)/(0.07728 + 0.92272\lambda)$ and $(0.92272 + 14.232\lambda)/(0.07728 + 0.92272\lambda)$ are algebraically equivalent rearrangements of eqs 8–9 under the calibration parameters. Verified numerically. ✓

## Condition 4: Interpretations

| # | Verbal Claim | Formal Support |
|---|-------------|----------------|
| 1 | AI stocks command a valuation premium due to hedging demand | Prop 2: $v^A - v^N > 0$ |
| 2 | Premium increases with singularity probability | Prop 2(i) |
| 3 | Premium decreases with AI share | Prop 2(ii) |
| 4 | Incomplete markets are essential for the premium | Model structure: with complete markets, household hedges perfectly, $J$ irrelevant |
| 5 | AI stocks pay well when household is desperate | $J<1 \Rightarrow$ high SDF; $(1+\theta)>1 \Rightarrow$ AI dividends surge |
| 6 | Self-limiting mechanism as AI share grows | Prop 2(ii): higher $s$ raises $J$, reducing premium |
| 7 | Singularity is negative when $s < \phi/(\theta+\phi)$ | Algebra: $J<1 \iff s < \phi/(\theta+\phi)$; threshold = 0.375 > 0.15 |
| 8 | AI stocks cannot hedge extinction | Prop 3: premium scales by $(1-\delta)$ |
| 9 | Hedging premium largest in intermediate regime | Prop 2 (severity increases premium) + Prop 3 (extinction decreases it) |
| 10 | Infinite output may resolve incomplete markets | Verbal extension, clearly flagged as informal discussion |
| 11 | 2% singularity probability generates ~29% premium | Table 1: $v^A/v^N = 1.29$ at $\lambda=0.02$ |
| 12 | Broadening access to private AI capital reduces the premium | Follows from Prop 2(ii): increasing effective $s$ reduces premium |

All key economic claims are supported by the formal theory. No unsupported claims found.
