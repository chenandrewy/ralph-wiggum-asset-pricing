# tests/theory-correctness.py
Started: 2026-03-22 08:55:14 EDT
Runtime: 8m 6s
[ralph-garage/agent-logs/20260322T125514.658743Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T125514.658743Z_theory-correctness_claude_opus.log)

# theory-correctness

VERDICT: PASS

REASON: Core theoretical propositions are correctly derived; one table has a minor computational error in individual P/D levels (premiums unaffected), and one extension proposition relies on an implicit assumption that should be stated.

---

## Condition 1: Notational Consistency

**Result: PASS**

Mathematical objects grouped by concept:

| Group | Symbols | Consistent? |
|-------|---------|-------------|
| Consumption | $c_t$ | Yes |
| Dividends | $D_t^A$, $D_t^N$ | Yes |
| Preferences | $\beta$, $\gamma$ | Yes |
| Singularity params | $\lambda$, $\theta$, $\phi$ | Yes |
| AI share | $s$ | Yes |
| Jump factor | $J(s)$ / $J$ | Yes (shorthand is clear) |
| Effective discount | $a$ | Yes |
| Valuations | $v^A$, $v^N$, $\bar{v}$ | Yes |
| SDF | $M_{t,t+1}$ | Yes |
| Extinction | $\delta$, $\delta_H$, $\delta_O$ | Yes ($\delta$ general, then split by agent) |
| Friction resolution | $\pi$ | Yes |

No notational inconsistencies found.

---

## Condition 2: Consistent Assumptions

**Result: PASS**

All mathematical assumptions:

1. $\gamma > 1$, $\beta \in (0,1)$ — preference parameters (eq 1)
2. $c_t = D_t^A + D_t^N$ — market clearing (eq 2)
3. $s \equiv D_t^A / c_t$ constant pre-singularity (eq 3)
4. $\lambda \in (0,1)$ — singularity probability
5. $g > 0$ — deterministic growth rate
6. $\theta > 0$ — AI dividend jump
7. $\phi \in (0,1)$ — non-AI dividend drop
8. $a \equiv \beta(1+g)^{1-\gamma} < 1$ — finite valuations (eq 6)
9. $\delta \in [0,1)$ — extinction probability
10. $\pi \in [0,1]$, increasing in $\delta_O$ — friction resolution

**Consistency checks:**

- Assumption 8 ($a < 1$) is automatically satisfied: $\beta < 1$ and $(1+g)^{1-\gamma} < 1$ (since $g > 0$, $\gamma > 1$), so $a < 1$.
- Constant $s$ pre-singularity (assumption 3) is consistent with eqs (4)–(5): in normal transitions both dividends grow at $g$, preserving $s$.
- $J(s) = 1 - \phi + (\theta + \phi)s < 1$ when $s < \phi/(\theta+\phi)$. Baseline: $0.15 < 0.375$. Consistent with "negative singularity."

All assumptions can be simultaneously true.

---

## Condition 3: Logical Results

**Result: PASS (with notes)**

### Propositions 1–2 (Equilibrium Valuations and Hedging Premium): Correct

Verified the Euler equation derivation step by step:

- Post-singularity P/D: $\bar{v} = a/(1-a)$. Verified: standard Gordon growth. ✓
- Pre-singularity AI Euler equation expands to $v^A = (1-\lambda)a(1+v^A) + \lambda a J^{-\gamma}(1+\theta)(1+\bar{v})$. Solving yields eq (8). ✓
- Premium eq (10): subtraction of eqs (8)–(9) gives $\lambda a J^{-\gamma}(\theta+\phi)/[(1-a)(1-(1-\lambda)a)]$. ✓
- Part (i): $\lambda \mapsto \lambda/(1-a+\lambda a)$ has positive derivative $(1-a)/(1-a+\lambda a)^2$. ✓
- Part (ii): $\partial J/\partial s = \theta+\phi > 0$; $J < 1$, $\gamma > 1$ implies $J^{-\gamma}$ decreasing in $s$. ✓
- Part (iii): At $\lambda=0$, ratio = 1. At $\lambda=1$, ratio = $(1+\theta)/(1-\phi)$. Verified numerically: 2.1429. ✓

### Calibration Table 1: Correct

Numerically verified all entries:

| $\lambda$ | $v^A$ (model) | $v^A$ (paper) | $v^N$ (model) | $v^N$ (paper) | Premium | Ratio |
|-----------|---------------|---------------|---------------|---------------|---------|-------|
| 0.00 | 11.94 | 11.9 | 11.94 | 11.9 | 0.0 | 1.00 |
| 0.01 | 14.32 | 14.3 | 12.31 | 12.3 | 2.0 | 1.16 |
| 0.02 | 16.23 | 16.2 | 12.61 | 12.6 | 3.6 | 1.29 |
| 0.05 | 20.26 | 20.3 | 13.24 | 13.2 | 7.0 | 1.53 |

All values match within rounding. ✓

### Proposition 3 (Extinction): Premium formula correct; Table 2 individual P/D values have a computational error

The premium formula (eq 11) is correct: $(1-\delta)$ correctly scales the singularity-state contribution. Verified numerically. ✓

However, the **individual P/D ratios** ($v^A$, $v^N$) in Table 2 contain a systematic error. The correct formula for individual valuations is:

$$v^A = \bar{v} + \frac{\lambda a \bigl[(1-\delta)J^{-\gamma}(1+\theta) - 1\bigr]}{(1-a)[1-(1-\lambda)a]}$$

where $(1-\delta)$ multiplies only the $J^{-\gamma}(1+\theta)$ term **inside** the bracket. The table appears to compute $(1-\delta)$ **outside** the bracket:

$$v^A_{\text{table}} = \bar{v} + (1-\delta) \cdot \frac{\lambda a [J^{-\gamma}(1+\theta) - 1]}{(1-a)[1-(1-\lambda)a]}$$

This overestimates both $v^A$ and $v^N$ by the same constant $\lambda a \delta / [(1-a)(1-(1-\lambda)a)]$. The error cancels in the premium $v^A - v^N$ and the ratio $v^A/v^N$, so **the premium and ratio columns are correct**.

| $\delta$ | $v^A$ (correct) | $v^A$ (paper) | Error |
|----------|-----------------|---------------|-------|
| 0.00 | 16.23 | 16.2 | 0.00 |
| 0.10 | 15.55 | 15.8 | +0.25 |
| 0.25 | 14.54 | 15.2 | +0.62 |
| 0.50 | 12.84 | 14.1 | +1.25 |

This is a computational error, not a theoretical error. The propositions and their proofs are unaffected.

### Proposition 4 (Disagreement and Friction Resolution): Correct under an implicit assumption

The premium formula (eq 12) is correct **if** friction resolution eliminates the asymmetric dividend shocks ($\theta$, $\phi$ do not apply in the friction-resolves state). Under this interpretation, both stocks grow at $(1+g)$ when friction resolves, contributing zero premium from that state.

If instead the dividend shocks persist even when friction resolves (AI stock still jumps by $\theta$, non-AI still drops by $\phi$, but household consumption is buffered by private AI capital so $J=1$), then the correct premium would be:

$$v^A - v^N = \frac{\lambda(1-\delta_H) a (\theta+\phi)[\pi + (1-\pi)J^{-\gamma}]}{(1-a)[1-(1-\lambda)a]}$$

which is strictly larger than eq (12) for $\pi > 0$ (since $J^{-\gamma} > 1$). The paper's implicit assumption—that friction resolution neutralizes the dividend asymmetry—is economically reasonable (household rebalancing through private AI capital offsets the redistribution) but should be stated explicitly.

---

## Condition 4: Interpretations

**Result: PASS**

Key economic claims and their formal support:

1. **"AI stocks command a valuation premium that increases with the probability and severity of the singularity."** — Supported by Proposition 2(i) ($\lambda$) and the structure of $J^{-\gamma}(\theta+\phi)$ in eq (10). ✓

2. **"Incomplete markets are essential: if households could access private AI capital, the hedging motive would disappear."** — Supported by Section 2.3 discussion and Proposition 4 ($\pi \to 1$ eliminates the hedging component). ✓

3. **"The premium is decreasing in the existing AI share."** — Proposition 2(ii). ✓

4. **"AI stocks cannot hedge extinction."** — Proposition 3: extinction state contributes zero to Euler equation. ✓

5. **"Even a 10% conditional extinction probability reduces the premium by a tenth; at $\delta = 0.50$, the premium is halved."** — From eq (11), premium is linear in $(1-\delta)$. $\delta = 0.10$ gives exactly 10% reduction; $\delta = 0.50$ gives exactly 50% reduction. ✓

6. **"If AI owners are pessimistic, they discount their private capital, loosening the friction."** — Captured by $\pi$ increasing in $\delta_O$ in Proposition 4. ✓

7. **"The AI valuation premium is largest in an intermediate regime... infinite output would eliminate the household's need for a hedge."** — Supported by $\pi \to 1$ in the infinite-output limit. ✓

8. **"Household consumption falls by 18%."** — $J = 0.82$, so $1 - J = 0.18$. ✓

9. **"Unlike the intergenerational friction in GKP, which is permanent, our friction is potentially self-resolving."** — Consistent with model: GKP friction is non-existence of trading partners; this paper's friction is asset accessibility, which singularity could resolve. ✓

All key economic claims are supported by the formal theory.
