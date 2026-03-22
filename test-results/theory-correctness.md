# tests/theory-correctness.py
Started: 2026-03-22 12:14:19 EDT
Runtime: 7m 16s
[ralph-garage/agent-logs/20260322T161419.088987Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T161419.088987Z_theory-correctness_claude_opus.log)

# theory-correctness

VERDICT: FAIL

REASON: The verbal claim that the business-cycle premium differential is "approximately 2–3 percentage points" is not supported by the formal theory with the stated parameters; the formula yields ~5–7 basis points.

---

## Condition 1: Notational Consistency — PASS

All mathematical objects were catalogued and grouped by economic concept:

- **Consumption/utility:** $c_t$, $\gamma$, $\beta$ — used consistently throughout.
- **Dividends/income:** $D_t^A$, $D_t^N$, $L_t$, $s_t$, $\ell_t$ — defined once and used consistently.
- **Growth rates:** $g^A$, $g^N$, $g^L = g^N$, $g$ (common growth), $G(s_t)$ — no conflicts.
- **Singularity parameters:** $\lambda$, $\theta$, $\phi$, $\phi_L$, $J$ — consistent definitions and usage.
- **Market incompleteness:** $\alpha$, $\psi$, $\tilde{s}(\alpha)$ — consistent.
- **SDF/pricing:** $M_{t,t+1}$, $a$, $\bar{v}$, $v^A$, $v^N$ — consistent.
- **Extensions:** $\delta$, $\delta_H$, $\delta_O$, $\pi$, $Y_O$, $d$, $\eta$, $J_O$, $\omega$, $W$ — consistent.
- **Business cycle:** $\sigma$, $\epsilon$, $b^A$, $b^N$, $R^f$, $R^i$ — consistent.

No notational inconsistencies found.

---

## Condition 2: Consistent Assumptions — PASS

All assumptions were catalogued:

1. CRRA utility: $\gamma > 1$, $\beta \in (0,1)$ (eq 1)
2. Budget constraint: $c_t = D_t^A + D_t^N + L_t$ (eq 2)
3. Normal growth: $g^A \geq g^N > 0$, $g^L = g^N$ (eq 3)
4. Singularity shocks: $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$ (eq 4)
5. Singularity probability: $\lambda \in (0,1)$
6. Finite valuations: $a \equiv \beta(1+g)^{1-\gamma} < 1$
7. Market access: $\alpha \in [0,1]$, $\psi > 0$
8. Extinction: $\delta \in [0,1)$
9. Business-cycle shocks: i.i.d. mean-zero, unit-variance $\epsilon$

Cross-checks:
- Assumption 6 ($a < 1$) is automatically satisfied under assumptions 1 and 3: $\beta < 1$ and $(1+g)^{1-\gamma} < 1$ when $\gamma > 1$ and $g > 0$.
- No parameter ranges overlap or conflict.
- All assumptions can be simultaneously true.

---

## Condition 3: Logical Results — PASS

All formal results were traced back to assumptions.

**Proposition 1 (Equilibrium Valuations).** Verified. The Euler equation $v^A = (1-\lambda)a(1+v^A) + \lambda a J^{-\gamma}(1+\theta)(1+\bar{v})$ solves to eq (7). Numerical check at baseline ($\lambda = 0.02$): $a = 0.9224$, $\bar{v} = 11.88$, $J = 0.805$, $J^{-3} = 1.916$, $v^A = 16.5$ (paper: 16.6), $v^N = 12.7$ (paper: 12.8). Rounding consistent. ✓

**Proposition 2 (Hedging Premium).** Verified. Subtracting eq (8) from (7) yields eq (10). Parts (i)–(iii) confirmed: (i) $\partial/\partial\lambda > 0$ via quotient rule; (ii) $\partial J/\partial s = \theta + \phi > 0$ with $J < 1$, $\gamma > 1$ implies $J^{-\gamma}$ decreasing in $s$; (iii) boundary values at $\lambda = 0$ and $\lambda = 1$ correct. ✓

**Decomposition (eq 14).** Verified. Factoring $J^{-\gamma}$ from the premium. ✓

**Corollary 1 (Partial Market Access).** Verified. Follows from $\tilde{s}(\alpha)$ increasing in $\alpha$ and Prop 2(ii). ✓

**Corollary 2 (Welfare).** Verified. The value-function multiplier $W(\tilde{s}) = [1-a+\lambda a J(\tilde{s})^{1-\gamma}]/[(1-a)(1-(1-\lambda)a)]$ is correctly derived. Since $J$ increasing in $\tilde{s}$ and $1-\gamma < 0$, $J^{1-\gamma}$ is decreasing; combined with $1/(1-\gamma) < 0$ exponent, $\omega > 0$. ✓

**Proposition 3 (Business-Cycle Augmentation).** Verified at the formula level. The separation of normal-period and singularity contributions to covariance via independence is valid. The first-order invariance of P/D ratios follows from $E[(1+\sigma\epsilon)^{-\gamma}(1+\sigma b^i \epsilon)] = 1 + O(\sigma^2)$. ✓

**Proposition 4 (Extinction).** Verified. Extinction state contributes zero to Euler equation (zero dividends, zero prices). Survival probability $(1-\delta)$ scales the singularity contribution linearly. ✓

**Proposition 5 (Disagreement).** Verified. The four sub-states (extinction, friction-persists, friction-resolves, normal) are correctly weighted. When friction resolves, $J = 1$ so $J^{-\gamma} = 1$, but cash-flow differential persists. ✓

**Proposition 6 (Hump Shape).** Verified. Part (i): for large $\theta$, $J \approx s\theta$, and super-linear growth of $Y_O$ ensures $(1-\pi)\theta \to 0$. Part (ii): $J = 1$ threshold correctly identified at $\theta = [(1-s-\ell)\phi + \ell\phi_L]/s$. ✓

---

## Condition 4: Interpretations — FAIL

All key verbal economic claims were identified and checked against the formal theory.

**Claims that PASS:**

1. "AI stocks command a valuation premium that increases with the probability and severity of the singularity" — Supported by Prop 2(i) and the structure of eq (10). ✓
2. "hedging demand roughly doubles the cash-flow-only premium" — $J^{-\gamma} \approx 1.92$ at baseline. ✓
3. "The hedging component of the AI valuation premium would vanish [under complete markets]" — With complete markets $J \to 1$, amplifier $\to 1$. ✓
4. "The premium is strictly decreasing in $s$" — Prop 2(ii). ✓
5. "broadening access to private AI capital continuously reduces the hedging premium" — Corollary 1. ✓
6. "welfare gains of up to 3.4%" — Table 3 at $\alpha = 1$, consistent with Corollary 2. ✓
7. "non-AI stock valuations also rise with singularity risk" — $J^{-\gamma}(1-\phi) \approx 1.34 > 1$, so the singularity adjustment is positive. ✓
8. "AI stocks earn lower expected returns" in baseline — Positive Cov(M, R^A) from singularity state. ✓
9. "the hedging premium erodes over time" as $s_t$ rises — Premium decreasing in $s$, and $s$ rises under differential growth. ✓
10. "the hedging channel contributes 13–23% [of the valuation gap]" — Consistent with Table 2 hedging shares at empirically relevant calibrations (3–5 pp growth differential, $\lambda = 0.02$–$0.05$). Verified the hedging-share computation for the 0pp rows via direct calculation. ✓
11. "the hedging channel is the only component of the premium that depends on incomplete markets" — In the decomposition (eq 14), only $J^{-\gamma}$ depends on $\alpha$; the cash-flow factor $(\theta + \phi)$ does not. ✓
12. "the hedging channel survives realistic consumption composition" — Labor displacement ($\phi_L = 0.20$ on $\ell = 0.65$) drives 13 pp of the 19 pp consumption drop. ✓
13. "exceeding 50% of the premium when [$\gamma = 5$, $\phi_L = 0.35$]" — Verified: at $\gamma = 5$, $\phi = 0.50$, $\phi_L = 0.35$, $J \approx 0.648$, $J^{-5} \approx 8.9$, hedging share $\approx 81\%$. ✓

**Claim that FAILS:**

14. "the business-cycle premium differential is approximately 2–3 percentage points" (with $\sigma \approx 0.02$, $b^A \approx 1.3$–$1.5$, $b^N \approx 0.9$, $\gamma = 3$).

Using eq (16), the business-cycle component is $(1-\lambda)\gamma(b^A - b^N)\sigma^2 R^f$. Plugging in the stated parameters:

$(0.98)(3)(0.4\text{–}0.6)(0.0004)({\sim}1.04) \approx 0.05\%\text{–}0.07\%$

This is approximately **5–7 basis points**, roughly 30–40 times smaller than the claimed 2–3 percentage points. To generate 2–3 pp, $\sigma$ would need to be $\approx 0.12$–$0.14$ (closer to return volatility than consumption-growth volatility). The formal theory with the stated parameter $\sigma \approx 0.02$ does not support this claim.

Note: the qualitative argument is correct — business-cycle risk can dominate expected returns while the hedging channel operates through valuations. The error is quantitative, not conceptual, and does not affect the paper's main results about valuations and the hedging premium.
