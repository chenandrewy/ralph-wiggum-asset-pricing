# tests/theory-correctness.py
Started: 2026-03-22 13:07:06 EDT
Runtime: 6m 25s
[ralph-garage/agent-logs/20260322T170706.993192Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T170706.993192Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All notation is consistent, assumptions are mutually compatible, all results follow logically from assumptions, and all verbal claims are supported by the formal theory.

## 1. Notational Consistency

All mathematical objects were cataloged and grouped by economic concept. Notation is consistent throughout:

- **Consumption:** $c_t$ used uniformly.
- **Dividends:** $D_t^A$, $D_t^N$ consistently denote AI and non-AI dividends.
- **Labor:** $L_t$ throughout; labor share $\ell_t \equiv L_t/c_t$.
- **Shares:** $s_t \equiv D_t^A/c_t$; subscripts dropped appropriately in the common-growth baseline where shares are constant.
- **Growth rates:** $g^A$, $g^N$, $g$ (common growth); $g^L = g^N$ stated once and maintained.
- **Singularity parameters:** $\lambda$, $\theta$, $\phi$, $\phi_L$ used consistently.
- **Preferences:** $\beta$, $\gamma$ standard and consistent.
- **Aggregate growth:** $G(s_t)$ defined once, used consistently.
- **Jump factor:** $J(s_t, \ell_t)$ and shorthand $J$ used appropriately.
- **Effective discount:** $a \equiv \beta(1+g)^{1-\gamma}$ (common growth); $a_t^A \equiv \beta(1+g^A)G(s_t)^{-\gamma}$ (differential growth). Clearly distinguished.
- **P/D ratios:** $v^A$, $v^N$, $\bar{v}$ consistent.
- **Market access:** $\alpha$, $\psi$, $\tilde{s}(\alpha) = s + \alpha\psi$ consistent.
- **Extinction/disagreement:** $\delta$, $\delta_H$, $\delta_O$, $\pi$ consistent.
- **Business cycle:** $\sigma$, $\epsilon_{t+1}$, $b^A$, $b^N$ consistent.
- **SDF:** $M_{t,t+1}$ consistent.
- **Welfare:** $\omega(\alpha)$ consistent.

No notational conflicts found.

## 2. Consistent Assumptions

All mathematical assumptions listed:

1. CRRA utility with $\gamma > 1$, $\beta \in (0,1)$ (eq 1).
2. Budget/consumption identity $c_t = D_t^A + D_t^N + L_t$ (eq 2).
3. Share definitions $s_t \equiv D_t^A/c_t$, $\ell_t \equiv L_t/c_t$.
4. Singularity probability $\lambda \in (0,1)$, one-time event.
5. Deterministic growth: $g^A \geq g^N > 0$, $g^L = g^N$ (eq 3).
6. Singularity jumps: $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$ (eq 4).
7. Finite valuation condition $a < 1$ (eq 6).
8. Market access $\alpha \in [0,1]$, $\psi > 0$ (eq 5).
9. Extinction $\delta \in [0,1)$.
10. Friction resolution $\pi \in [0,1]$, increasing in $\delta_O$.

Consistency checks:
- $a = \beta(1+g)^{1-\gamma}$: with $\gamma > 1$ and $g > 0$, $(1+g)^{1-\gamma} < 1$, so $a < \beta < 1$. ✓
- All parameter ranges are non-conflicting. ✓
- Baseline calibration satisfies all constraints: $\beta = 0.96$, $\gamma = 3$, $g = 0.02$, $a \approx 0.923 < 1$, $s + \ell = 0.70 < 1$, $J \approx 0.81 < 1$. ✓

All assumptions are mutually consistent.

## 3. Logical Results

Every derived expression was traced back to assumptions:

- **$G(s_t)$ and $J(s_t, \ell_t)$** (eqs 3-4): Follow directly from the consumption identity and growth/singularity transition rules. ✓
- **SDF** (eq 5): Standard CRRA first-order condition. ✓
- **Post-singularity P/D** $\bar{v} = a/(1-a)$ (eq 7): Euler equation with no further risk, geometric series. ✓
- **Proposition 1** (eqs 8-9): Verified by expanding the pre-singularity Euler equation, substituting $1+\bar{v} = 1/(1-a)$, and solving. Algebra confirmed. ✓
- **Proposition 2** (eq 10): Verified by subtraction of eq (9) from eq (8). Comparative statics (i)-(iii) all verified analytically. ✓
- **Decomposition** (eq 11): Correct factoring of eq (10). ✓
- **Corollary 1**: Follows from Proposition 2(ii) via $\tilde{s}(\alpha)$ increasing in $\alpha$. ✓
- **Corollary 2** (eq 13): Derived value function multiplier $W(\tilde{s})$ and confirmed the consumption-equivalent formula. Verified $\omega > 0$ using $\gamma > 1$ and $J$ increasing in $\tilde{s}$. ✓
- **Differential growth** (eq 12): Verified the Euler equation structure with time-varying $a_t^A$ and $s_t$. ✓
- **Expected returns** (eq 14): Standard asset pricing identity. ✓
- **Proposition 3** (eq 15): Business-cycle augmentation. Independence of $\epsilon$ and singularity indicator gives additive decomposition. First-order invariance of P/D ratios verified. ✓
- **Proposition 4** (eq 16): Extinction state contributes zero to Euler equation (zero dividends and prices). Scaling by $(1-\delta)$ confirmed. ✓
- **Proposition 5** (eq 17): Four sub-states correctly enumerated and summed. ✓
- **Friction microfoundation** (eq 18): $\pi(Y_O)$ derived from the bilateral-trade conditions. ✓
- **Proposition 6** (hump shape): Result is correct. Minor note: the proof sketch claims $|(\theta+\phi)(J^{-\gamma}-1)| \sim \theta^{1-\gamma}$, but for large $\theta$, $J^{-\gamma}-1 \to -1$ so the expression actually grows as $\sim\theta$. The conclusion $\Delta^{\text{hedge}} \to 0$ still holds because $(1-\pi) = d/(d+Y_O) \to 0$ super-linearly in $1/\theta$, which dominates. The result is logically sound; only the intermediate bound in the proof sketch is imprecise. ✓

All expressions are logically derivable from the assumptions.

## 4. Interpretations

All key verbal claims checked against formal theory:

| Claim | Support | Status |
|---|---|---|
| AI stocks command a valuation premium increasing in $\lambda$ | Proposition 2(i) | ✓ |
| Premium decreasing in AI share $s$ | Proposition 2(ii) | ✓ |
| Incomplete markets essential: hedging amplifier collapses to 1 when $J=1$ | Decomposition (eq 11), Corollary 1 | ✓ |
| Welfare gain from market access strictly positive | Corollary 2 | ✓ |
| AI stocks act as insurance (pay well when household suffers) | $J < 1$ with $\theta > 0$ in eq (4) | ✓ |
| Self-limiting mechanism: premium erodes as $s_t$ rises | Proposition 2(ii), differential growth dynamics | ✓ |
| Non-AI valuations also rise with singularity risk | $J^{-\gamma}(1-\phi) \approx 1.34 > 1$ at baseline | ✓ |
| Hedging amplifier roughly doubles cash-flow premium | $J^{-3} \approx 1.92$ at baseline | ✓ |
| Hedging channel contributes 13-23% at empirical calibrations | Table 2 verified numerically | ✓ |
| Hedging share exceeds 50% at $\gamma=5$, $\phi_L=0.35$ | Computed hedging share ~81% at those parameters | ✓ |
| AI stocks earn lower expected returns in baseline | Positive Cov($M$, $R^A - R^N$) verified | ✓ |
| Business-cycle augmentation reconciles with high betas | Proposition 3(ii) | ✓ |
| Extinction reduces premium linearly in $\delta$ | Proposition 4 | ✓ |
| Hedging component is hump-shaped in $\theta$ | Proposition 6 | ✓ |
| The hedging channel is the only premium component depending on incomplete markets | Cash-flow premium exists at $J^{-\gamma}=1$; hedging amplifier requires $J \neq 1$ | ✓ |

All verbal claims are supported by the formal theory.
