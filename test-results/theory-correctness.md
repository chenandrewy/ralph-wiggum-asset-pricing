# tests/theory-correctness.py
Started: 2026-03-22 11:42:18 EDT
Runtime: 3m 50s
[ralph-garage/agent-logs/20260322T154218.066243Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T154218.066243Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All notation is consistent, assumptions are mutually compatible, results derive correctly from assumptions, and verbal claims are supported by the formal theory.

## 1. Notational Consistency

All mathematical objects grouped by concept:

| Concept | Symbols | Consistent? |
|---|---|---|
| Consumption | $c_t$ | Yes |
| Dividends | $D_t^A$, $D_t^N$ | Yes |
| Labor income | $L_t$ | Yes |
| AI share | $s_t \equiv D_t^A/c_t$, simplified to $s$ at baseline | Yes |
| Labor share | $\ell_t \equiv L_t/c_t$, simplified to $\ell$ at baseline | Yes |
| Growth rates | $g^A$, $g^N$, $g^L = g^N$, $g$ (when equal) | Yes |
| Singularity shocks | $\theta$ (AI jump), $\phi$ (non-AI drop), $\phi_L$ (labor drop) | Yes |
| Singularity probability | $\lambda$ | Yes |
| Preferences | $\beta$, $\gamma$ | Yes |
| Aggregate growth | $G(s_t)$ | Yes |
| Jump factor | $J(s_t, \ell_t)$ or $J$ | Yes |
| Effective discount | $a \equiv \beta(1+g)^{1-\gamma}$ | Yes |
| P/D ratios | $v^A$, $v^N$, $\bar{v}$ | Yes |
| Market access | $\alpha$, $\tilde{s}(\alpha)$, $\psi$ | Yes |
| SDF | $M_{t,t+1}$ | Yes |
| Extinction | $\delta$, $\delta_H$, $\delta_O$ | Yes |
| Friction resolution | $\pi$ | Yes |
| Business cycle | $\sigma$, $\epsilon_{t+1}$, $b^A$, $b^N$ | Yes |
| Welfare | $\omega(\alpha)$ | Yes |
| Insider pricing | $\eta$ | Yes |

No notational inconsistencies found.

## 2. Consistent Assumptions

Key assumptions:

1. CRRA utility with $\gamma > 1$, $\beta \in (0,1)$ (eq 1)
2. Budget constraint: $c_t = D_t^A + D_t^N + L_t$ (eq 2)
3. Shares: $s_t \equiv D_t^A/c_t$, $\ell_t \equiv L_t/c_t$, non-AI share $1 - s_t - \ell_t$
4. Singularity: probability $\lambda \in (0,1)$, one-time event
5. Normal transition: $g^A \geq g^N > 0$, $g^L = g^N$ (eq 3)
6. Singularity transition: $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$ (eq 4)
7. Finite valuations: $a < 1$
8. Market access: $\alpha \in [0,1]$, $\psi > 0$
9. Extinction: $\delta \in [0,1)$
10. Business-cycle shocks: i.i.d., mean-zero

All assumptions are mutually compatible. The share definitions (assumption 3) are consistent with the budget constraint (assumption 2). The growth rates and shock parameters do not conflict. The condition $a < 1$ is achievable with the stated parameter ranges ($\beta < 1$, $\gamma > 1$, $g > 0$). No set of assumptions is simultaneously contradictory.

## 3. Logical Results

**Proposition 1 (Equilibrium Valuations).** Verified by expanding the Euler equation $v^A = E_t[M_{t,t+1}(D_{t+1}^A/D_t^A)(1+v_{t+1}^A)]$ into its two states, solving for $v^A$, and confirming the algebra yields eq (9). The non-AI derivation with $(1-\phi)$ replacing $(1+\theta)$ is identical.

**Proposition 2 (Hedging Premium).** Verified: subtracting eq (10) from eq (9) yields $J^{-\gamma}[(1+\theta)-(1-\phi)] = J^{-\gamma}(\theta+\phi)$. Parts (i)–(iii) confirmed via direct differentiation and limit evaluation.

**Decomposition (eq 12).** Correct factoring of $J^{-\gamma}$ from the premium expression.

**Corollary 1 (Partial Market Access).** Follows from $\tilde{s}(\alpha) = s + \alpha\psi$ increasing in $\alpha$ and Proposition 2(ii).

**Corollary 2 (Welfare).** Verified: the value function $V = [c^{1-\gamma}/(1-\gamma)] \cdot W(\tilde{s})$ with $W = [1-a+\lambda a J(\tilde{s})^{1-\gamma}]/[(1-a)(1-(1-\lambda)a)]$. The consumption-equivalent formula matches. Positivity confirmed via signs: $J$ increasing in $\tilde{s}$, $1-\gamma < 0$ flips the inequality.

**Proposition 3 (Business-Cycle Augmentation).** The first-order invariance of P/D ratios to $\sigma^2$ is correct (the correction factor is $1 + O(\sigma^2)$). The return decomposition follows from independence of $\epsilon_{t+1}$ and the singularity indicator.

**Recursive formula (eq 14).** Verified: with $g^A \neq g^N$, the asset-specific discount factor $a_t^A = \beta(1+g^A)G(s_t)^{-\gamma}$ correctly enters the Euler equation.

**Proposition 4 (Extinction).** Correct: extinction state contributes zero to Euler equations (dividends and prices are zero), so survival probability $(1-\delta)$ scales the singularity term.

**Proposition 5 (Disagreement).** Verified: the four sub-states (extinction, survival with friction, survival without friction, normal) are correctly enumerated. When friction resolves ($J = 1$), the hedging amplifier equals 1 but the cash-flow differential persists.

**Proposition 6 (Hump-Shaped).** Verified: for large $\theta$, $J \approx s\theta$ so $(1-\pi)(\theta+\phi)|J^{-\gamma}-1| \to 0$ under the super-linear condition. The $J = 1$ threshold $\theta^* = [(1-s-\ell)\phi + \ell\phi_L]/s$ is correctly derived.

**Numerical verification.** Spot-checked Table 1 at $\lambda = 0.02$: $a \approx 0.922$, $\bar{v} \approx 11.9$, $J \approx 0.805$, $J^{-3} \approx 1.92$, $v^A \approx 16.5$, $v^N \approx 12.7$, ratio $\approx 1.30$. All match. Also confirmed $J^{-\gamma}(1-\phi) \approx 1.34 > 1$ for the level-effects claim.

## 4. Interpretations

All key verbal economic claims are supported by the formal theory:

1. "AI stocks command a valuation premium increasing in singularity probability" — Proposition 2(i). ✓
2. "Incomplete markets are essential; hedging amplification vanishes with complete markets" — Corollary 1 and decomposition ($J \to 1 \Rightarrow J^{-\gamma} \to 1$). ✓
3. "Hedging channel survives realistic consumption composition" — Labor displacement ($\phi_L = 0.20$ on $\ell = 0.65$) keeps $J \approx 0.81 < 1$. ✓
4. "Hedging demand roughly doubles the cash-flow premium" — $J^{-\gamma} \approx 1.92$ at baseline. ✓
5. "Self-limiting mechanism as AI share grows" — $\partial J/\partial s = \theta + \phi > 0$, so rising $s$ pushes $J \to 1$. ✓
6. "Non-AI valuations also rise with singularity risk" — $J^{-\gamma}(1-\phi) \approx 1.34 > 1$. ✓
7. "AI stocks earn lower expected returns in baseline, higher with business-cycle risk" — Proposition 3(ii), opposing forces. ✓
8. "AI stocks cannot hedge extinction" — All assets worth zero in extinction state. ✓
9. "Pessimistic AI owners may unwind the friction" — Proposition 5, premium decreasing in $\pi$ (and $\delta_O$). ✓
10. "Hedging amplification is hump-shaped in severity" — Proposition 6. ✓
11. "Welfare gains of up to 3.4% from broadening market access" — Table 3, Corollary 2. ✓
12. "The hedging channel is driven by labor displacement" — Sensitivity analysis: $\phi_L$ increase has large effect because $\ell = 0.65$. ✓

No unsupported claims found.
