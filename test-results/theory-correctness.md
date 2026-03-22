# tests/theory-correctness.py
Started: 2026-03-22 09:11:30 EDT
Runtime: 7m 21s
[ralph-garage/agent-logs/20260322T131130.159339Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T131130.159339Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All four conditions are satisfied; the baseline model is rigorously correct, calibration numbers verified, and extension results follow from stated assumptions.

## 1. Notational Consistency

All mathematical objects are used consistently throughout:

| Symbol | Meaning | Consistency |
|--------|---------|-------------|
| $c_t$ | Household consumption | Consistent |
| $\beta, \gamma$ | Discount factor, risk aversion | Consistent |
| $D_t^A, D_t^N$ | AI / non-AI dividends | Consistent |
| $s$ | AI dividend share $D_t^A/c_t$ | Consistent (constant pre-singularity) |
| $\lambda$ | Singularity probability | Consistent |
| $g$ | Dividend growth rate | Consistent |
| $\theta, \phi$ | AI jump / non-AI drop | Consistent |
| $J(s)$ | Consumption jump factor | Consistent |
| $a$ | Effective discount factor $\beta(1+g)^{1-\gamma}$ | Consistent |
| $\bar{v}$ | Benchmark P/D ratio | Consistent |
| $v^A, v^N$ | Pre-singularity P/D ratios | Consistent |
| $M_{t,t+1}$ | Stochastic discount factor | Consistent |
| $\delta, \delta_H, \delta_O$ | Extinction probabilities | Consistent |
| $\pi$ | Friction resolution probability | Consistent |
| $Y_O, k$ | AI output scale, fixed cost | Consistent |

No notation conflicts found.

## 2. Consistent Assumptions

Assumptions identified:
- (A1) $\gamma > 1$, $\beta \in (0,1)$ — CRRA preferences
- (A2) $c_t = D_t^A + D_t^N$ — consumption equals total dividends
- (A3) $s \equiv D_t^A / c_t$ constant pre-singularity
- (A4) $\lambda \in (0,1)$ — singularity probability
- (A5) $g > 0$ — common growth rate
- (A6) $\theta > 0$, $\phi \in (0,1)$ — singularity parameters
- (A7) $a < 1$ — finite valuations
- (A8) $\delta \in [0,1)$ — extinction probability

Consistency checks:
- (A3) follows from (A2) and the normal-transition growth equations: both $D_t^A$ and $D_t^N$ grow at rate $g$, so $s$ is constant. **Consistent.**
- (A7) is automatically satisfied: $a = \beta(1+g)^{1-\gamma}$, with $\beta < 1$ and $(1+g)^{1-\gamma} < 1$ (since $\gamma > 1$ and $g > 0$). **Consistent.**
- The negative singularity condition $J(s) < 1$ requires $s < \phi/(\theta+\phi) = 0.375$, which is satisfied at $s = 0.15$. **Consistent.**

No contradictions found among assumptions.

## 3. Logical Results

**Proposition 1 (Equilibrium Valuations).** Verified by expanding the Euler equation:
$$v^A = (1-\lambda)a(1+v^A) + \lambda a J^{-\gamma}(1+\theta)(1+\bar{v})$$
Solving yields eq (7). The derivation for $v^N$ is symmetric. **Verified algebraically and numerically.**

**Proposition 2 (Hedging Premium).** Subtracting eq (8) from eq (7):
$$v^A - v^N = \frac{\lambda a J^{-\gamma}(\theta+\phi)}{(1-a)[1-(1-\lambda)a]}$$
- Part (i): $\partial/\partial\lambda[\lambda/(1-a+\lambda a)] = (1-a)/(1-a+\lambda a)^2 > 0$. **Correct.**
- Part (ii): $\partial J/\partial s = \theta+\phi > 0$; since $J < 1$ and $\gamma > 1$, $J^{-\gamma}$ decreases in $s$. **Correct.**
- Part (iii): At $\lambda=0$, ratio is 1. At $\lambda=1$, ratio is $(1+\theta)/(1-\phi)$. **Correct.**

**Proposition 3 (Extinction).** The extinction state contributes zero to the Euler equation (all payoffs are zero; standard treatment in the rare disasters literature). The singularity contribution scales by $(1-\delta)$. Formula verified numerically—all Table 2 values match. **Correct.**

**Proposition 5 (Disagreement).** The formula adds a $(1-\pi)$ factor, corresponding to the probability that the friction persists. Under the paper's assumption that friction resolution makes the singularity both consumption-neutral and dividend-neutral (dividends "absorbed by portfolio adjustment"), the friction-resolves state contributes equally to both stocks, and the formula follows. **Correct under stated assumptions.**

**Proposition 6 (Hump-shaped premium).** The premium is proportional to $(1-\pi)J^{-\gamma}(\theta+\phi)$. As $\theta \to \infty$ with $\pi \to 1$, $(1-\pi) \to 0$ and the premium vanishes. For small $\theta$, the direct effect dominates and the premium rises; for large $\theta$, friction resolution dominates and the premium falls. The qualitative hump-shape result is correct. **Correct.**

**Calibration (Tables 1 and 2).** All numerical values independently verified:
- $a = 0.9227$, $\bar{v} = 11.9$, $J = 0.82$ (18% consumption drop)
- Table 1: All P/D ratios, premia, and ratios match to reported precision
- Table 2: All values match; premium is exactly proportional to $(1-\delta)$

## 4. Interpretations

Key economic claims and their formal support:

| Claim | Support |
|-------|---------|
| AI stocks command a valuation premium due to hedging demand | Proposition 2: $v^A - v^N > 0$ |
| Premium increases with singularity probability | Proposition 2(i) |
| Premium decreases with AI share of portfolio | Proposition 2(ii) |
| Self-limiting mechanism: larger AI share reduces risk | Proposition 2(ii): $\partial(v^A-v^N)/\partial s < 0$ |
| Incomplete markets are essential for the premium | Section 2.3: with complete markets, $J=1$ and hedging motive vanishes |
| AI stocks cannot hedge extinction | Proposition 3: premium scales by $(1-\delta)$ |
| 10% extinction probability reduces premium by a tenth | Verified: $3.257/3.619 = 0.90$, exactly 10% reduction |
| At $\delta=0.50$, premium is halved | Verified: $1.810/3.619 = 0.50$ |
| Disagreement can unwind the friction | Proposition 5: premium decreasing in $\pi$ (and hence $\delta_O$) |
| Premium is hump-shaped in singularity severity | Proposition 6 |
| Model produces 29% premium at 2% singularity probability | Table 1: $v^A/v^N = 1.29$ at $\lambda=0.02$ |
| Household consumption falls by 18% | $J = 0.82$, verified |

All key theoretical claims are supported by the formal model.
