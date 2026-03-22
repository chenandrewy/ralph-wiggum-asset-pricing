# tests/theory-correctness.py
Started: 2026-03-22 12:28:34 EDT
Runtime: 4m 6s
[ralph-garage/agent-logs/20260322T162834.084932Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T162834.084932Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All notation is consistent, assumptions are compatible, results are logically derived from assumptions, and verbal claims are supported by the formal theory.

## Condition 1: Notational Consistency

All mathematical objects grouped by economic concept:

| Concept | Symbols | Status |
|---------|---------|--------|
| Consumption | $c_t$ | Consistent |
| Dividends | $D_t^A$, $D_t^N$ | Consistent |
| Labor income | $L_t$ | Consistent |
| Shares | $s_t \equiv D_t^A/c_t$, $\ell_t \equiv L_t/c_t$ | Consistent |
| Preferences | $\beta$, $\gamma$ | Consistent |
| Growth rates | $g^A$, $g^N$, $g^L = g^N$, $g$ (equal-growth baseline) | Consistent |
| Singularity | $\lambda$, $\theta$, $\phi$, $\phi_L$ | Consistent |
| Jump factor | $J(s_t, \ell_t)$ or $J$ | Consistent |
| Effective discount | $a \equiv \beta(1+g)^{1-\gamma}$ | Consistent |
| P/D ratios | $v^A$, $v^N$, $\bar{v}$ | Consistent |
| Market access | $\alpha$, $\psi$, $\tilde{s}(\alpha)$ | Consistent |
| SDF | $M_{t,t+1}$ | Consistent |
| Extinction | $\delta$, $\delta_H$, $\delta_O$ | Consistent |
| Friction resolution | $\pi$ | Consistent |
| Business cycle | $\sigma$, $\epsilon_{t+1}$, $b^A$, $b^N$ | Consistent |
| Welfare | $\omega(\alpha)$ | Consistent |
| Screening game | $q$, $Y_O$, $d_0$, $\kappa$, $\mu$, $\xi$, $d$ | Consistent |
| Aggregate growth | $G(s_t)$ | Consistent |

No notational inconsistencies found.

## Condition 2: Consistent Assumptions

All assumptions listed:

1. CRRA utility: $\gamma > 1$, $\beta \in (0,1)$ (eq 1)
2. Budget constraint: $c_t = D_t^A + D_t^N + L_t$ (eq 2)
3. Normal growth: $g^A \geq g^N > 0$, $g^L = g^N$ (eq 3)
4. Singularity shocks: $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$ (eq 4)
5. Singularity probability: $\lambda \in (0,1)$, one-time event
6. Finite valuations: $a < 1$
7. Market access: $\alpha \in [0,1]$, $\psi > 0$
8. Extinction: $\delta \in [0,1)$

Checked all pairwise interactions. Baseline calibration ($\beta=0.96$, $\gamma=3$, $g=0.02$) yields $a = 0.9227 < 1$. All parameter ranges are compatible and no pair of assumptions can be simultaneously false.

**Result: PASS**

## Condition 3: Logical Results

### Proposition 1 (Equilibrium Valuations)
Verified by expanding the Euler equation $v^A = E_t[M_{t,t+1}(D_{t+1}^A/D_t^A)(1+v_{t+1}^A)]$ into the no-singularity and singularity contributions, solving the fixed point, and confirming the closed-form matches eqs 6–7. Numerically verified against Table 1 (e.g., $v^A = 16.62$ at $\lambda=0.02$, paper reports 16.6).

### Proposition 2 (Hedging Premium)
Eq 8 follows by subtraction of eqs 6–7. Parts (i)–(iii) verified: (i) $\partial/\partial\lambda > 0$ confirmed; (ii) $\partial J/\partial s = \theta + \phi > 0$ with $J < 1$ and $\gamma > 1$ gives decreasing premium; (iii) boundary values at $\lambda=0$ and $\lambda=1$ confirmed.

### Decomposition (eq 10)
Algebraically equivalent to eq 8 after factoring. Cash-flow premium and hedging amplifier $J^{-\gamma}$ correctly identified.

### Corollary 1 (Partial Market Access)
Follows from Proposition 2(ii) with $\tilde{s}(\alpha) = s + \alpha\psi$ replacing $s$.

### Corollary 2 (Welfare)
Value function $V = [c^{1-\gamma}/(1-\gamma)] \cdot W(\tilde{s})$ correctly derived. Since $\gamma > 1$ and $J$ increasing in $\tilde{s}$, $W$ is decreasing in $\tilde{s}$, making welfare increase. The consumption-equivalent formula (eq 12) correctly follows from $(1+\omega)^{1-\gamma} = W(\tilde{s})/W(s)$.

### Proposition 3 (Business-Cycle Augmentation)
SDF separation by independence of i.i.d. shocks and singularity indicator is correct. P/D ratios unchanged to $O(\sigma^2)$. Expected-return decomposition (eq 13) verified.

### Proposition 4 (Extinction)
Extinction state contributes zero to Euler equation (zero payoffs). Premium scaled by $(1-\delta)$ as in eq 14. Verified numerically: Table 4 shows linear decline (e.g., $\delta=0.50$ halves the premium from 3.8 to 1.9).

### Proposition 5 (Disagreement)
Four sub-states correctly enumerated. In friction-resolved state, $J=1$ but cash-flow differential persists. Eq 16 verified.

### Proposition 6 (Hump Shape)
Part (i): $(1-\pi)\theta \to 0$ under super-linear growth confirmed. Part (ii): $J=1$ threshold at $\theta = [(1-s-\ell)\phi + \ell\phi_L]/s$ algebraically verified.

### Recursive formula (eq 11)
$a_t^A = \beta(1+g^A)G(s_t)^{-\gamma}$ correctly combines asset-specific dividend growth with aggregate consumption growth.

**Result: PASS**

## Condition 4: Interpretations

Key claims checked:

1. "AI stocks command a valuation premium increasing in $\lambda$" — Proposition 2(i). ✓
2. "Premium decreasing in $s$" — Proposition 2(ii). ✓
3. "Incomplete markets essential: hedging amplification vanishes if markets complete" — Corollary 1; as $\alpha \to 1$, $J \to 1$, $J^{-\gamma} \to 1$. ✓
4. "Hedging demand roughly doubles the cash-flow premium" — $J^{-3} = 0.805^{-3} = 1.917 \approx 1.92$. ✓
5. "Household consumption falls by 19%" — $1 - J = 1 - 0.805 = 0.195$. ✓
6. "Non-AI valuations also rise with singularity risk" — $J^{-\gamma}(1-\phi) = 1.917 \times 0.7 = 1.342 > 1$. ✓
7. "AI stocks earn lower expected returns in baseline" — Positive Cov(M, R^A) from high SDF and high payoff in singularity state. ✓
8. "Hedging channel contributes 13–23% at empirical calibrations" — Consistent with Table 2 hedging shares. ✓
9. "Hedging share exceeds 50% when $\gamma=5$, $\phi_L=0.35$" — $J = 0.6475$, $J^{-5} \approx 8.79$, hedging share $\approx 89\%$. ✓
10. "Welfare gains up to 3.4%" — Table 3, $\alpha=1.00$. ✓
11. "$\delta=0.10$ reduces premium by a tenth; $\delta=0.50$ halves it" — Table 4 confirms (3.4/3.8 ≈ 0.895; 1.9/3.8 = 0.50). ✓
12. "Self-limiting mechanism" — As $s_t$ rises, $J \to 1$, premium falls. Proposition 2(ii). ✓
13. "Hedging channel survives realistic consumption composition" — Labor displacement ($\phi_L$ on $\ell=0.65$) drives the consumption drop, not portfolio weight. ✓
14. GKP comparison (reducible vs. irreducible friction) — Parameterized by continuous $\alpha$ vs. structural intergenerational friction. ✓

All verbal economic claims are supported by the formal theory.

**Result: PASS**
