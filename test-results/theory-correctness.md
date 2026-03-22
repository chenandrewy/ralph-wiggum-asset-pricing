# tests/theory-correctness.py
Started: 2026-03-22 10:33:23 EDT
Runtime: 5m 34s
[ralph-garage/agent-logs/20260322T143323.816783Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T143323.816783Z_theory-correctness_claude_opus.log)

# theory-correctness

VERDICT: FAIL
REASON: Proposition 5 contains a proof error — the claimed sufficient condition for the hedging component to vanish is incorrect.

## Condition 1: Notational Consistency — PASS

All mathematical objects are used consistently throughout:

| Group | Symbols | Consistent? |
|-------|---------|-------------|
| Consumption | $c_t$ | Yes |
| Dividends | $D_t^A$, $D_t^N$ | Yes |
| AI share | $s_t$, $s$ (constant baseline) | Yes |
| Preferences | $\beta$, $\gamma$ | Yes |
| Growth rates | $g^A$, $g^N$, $g$ (equal case) | Yes |
| Singularity params | $\lambda$, $\theta$, $\phi$ | Yes |
| Jump factor | $J(s_t)$, $J$ | Yes |
| Aggregate growth | $G(s_t)$ | Yes |
| Effective discount | $a$ | Yes |
| P/D ratios | $v^A$, $v^N$, $\bar{v}$ | Yes |
| SDF | $M_{t,t+1}$ | Yes |
| Market access | $\alpha$, $\tilde{s}(\alpha)$, $\psi$ | Yes |
| Welfare | $\omega(\alpha)$ | Yes |
| Extinction | $\delta$, $\delta_H$, $\delta_O$ | Yes |
| Friction resolution | $\pi$ | Yes |
| AI output scale | $Y_O$, adverse-selection discount $d$ | Yes |

No notational conflicts found.


## Condition 2: Consistent Assumptions — PASS

All mathematical assumptions:

1. $\gamma > 1$, $\beta \in (0,1)$ (eq. 1)
2. $g^A \geq g^N > 0$ (eq. 4)
3. $\lambda \in (0,1)$ (Section 2.2)
4. $\theta > 0$, $\phi \in (0,1)$ (eq. 5)
5. $a \equiv \beta(1+g)^{1-\gamma} < 1$ (eq. 8)
6. $\alpha \in [0,1]$, $\psi > 0$ (eq. 6)
7. $\delta \in [0,1)$ (Section 4.1)

Compatibility check: Assumption 5 ($a < 1$) follows from Assumptions 1–2: since $\beta < 1$, $1+g > 1$, and $1-\gamma < 0$, we have $(1+g)^{1-\gamma} < 1$, so $a = \beta(1+g)^{1-\gamma} < 1$. All other assumptions involve disjoint parameters or are trivially compatible. No contradictions.


## Condition 3: Logical Results — FAIL

### Propositions 1–4 and Corollaries 1–2: Verified correct

**Proposition 1 (Valuations).** Re-derived from the Euler equation. The pre-singularity Euler equation for the AI stock expands to $v^A = (1-\lambda)a(1+v^A) + \lambda a J^{-\gamma}(1+\theta)(1+\bar{v})$. Solving and substituting $1+\bar{v} = 1/(1-a)$ yields eq. (9). Verified algebraically. ✓

**Proposition 2 (Premium).** Subtracting eq. (10) from eq. (9) yields eq. (11). Parts (i)–(iii) verified by direct differentiation and limit evaluation. ✓

**Decomposition (eq. 12).** Trivially factors from eq. (11). ✓

**Corollary 1 (Partial Market Access).** Follows from Proposition 2(ii) via chain rule with $\tilde{s}(\alpha) = s + \alpha\psi$. ✓

**Corollary 2 (Welfare).** The value-function structure is standard for CRRA with i.i.d. risk. The consumption-equivalent calculation is correct: since $1-\gamma < 0$ and $J$ is increasing in $\tilde{s}$, $W(\tilde{s})$ is decreasing, giving $\omega > 0$. ✓

**Proposition 3 (Extinction).** The extinction state contributes zero to the Euler equation (zero dividends and prices). Scaling the singularity contribution by $(1-\delta)$ yields eq. (15). ✓

**Proposition 4 (Disagreement).** The four sub-states (extinction, survive+friction, survive+resolve) are correctly enumerated. The premium formula (eq. 17) is verified by summing contributions. ✓

**Numerical verification.** All entries in Tables 1–3 were independently recomputed from the formulas and match to within rounding precision. ✓

### Proposition 5 (Hump-Shaped Hedging Amplification): ERROR

The hedging component is:
$$\Delta^{\text{hedge}} = C \cdot (1-\pi)(\theta+\phi)(J^{-\gamma}-1)$$
where $C > 0$ is a positive constant.

**Part (i) error.** The proposition claims $\Delta^{\text{hedge}} \to 0$ as $Y_O \to \infty$ (equivalently, as $\theta$ grows without bound). The proof claims that $Y_O = \bar{Y}(1+\theta)$ suffices. This is incorrect.

With $Y_O = \bar{Y}(1+\theta)$, as $\theta \to \infty$:
- $(1-\pi) = d/Y_O \approx d/(\bar{Y}\theta)$, which goes to zero as $1/\theta$
- $J = 1-\phi+(\theta+\phi)s \approx s\theta$, so $J^{-\gamma} \to 0$ and $J^{-\gamma}-1 \to -1$
- $(\theta+\phi) \approx \theta$

The product: $(1-\pi)(\theta+\phi)(J^{-\gamma}-1) \approx \frac{d}{\bar{Y}\theta} \cdot \theta \cdot (-1) = -\frac{d}{\bar{Y}} \neq 0$.

So with linear $Y_O$, $\Delta^{\text{hedge}}$ converges to $-Cd/\bar{Y}$, not zero. The proposition requires $Y_O$ to grow *faster than linearly* in $\theta$ (e.g., $Y_O \propto \theta^k$ for $k > 1$), but neither the proposition statement nor the proof imposes this condition.

**Part (ii) additional issue.** For sufficiently large $\theta$, $J > 1$ (the singularity becomes positive for the household), causing $J^{-\gamma} - 1 < 0$ and $\Delta^{\text{hedge}} < 0$. This occurs when $\theta > \phi(1-s)/s$ (= 1.70 at baseline). The "hump shape" description is incomplete: the hedging component rises, falls through zero, and becomes negative — not merely "hump-shaped."


## Condition 4: Interpretations — PASS

All key verbal economic claims were checked against the formal theory:

1. "AI stocks command a valuation premium increasing in singularity probability" — Proposition 2(i). ✓
2. "Incomplete markets roughly double the premium" — $J^{-\gamma} \approx 1.81$ at baseline. ✓
3. "The premium shrinks as the AI share increases" — Proposition 2(ii). ✓
4. "Self-limiting mechanism" — Follows from Proposition 2(ii). ✓
5. "Broader market access makes the household unambiguously better off" — Corollary 2. ✓
6. "AI stocks cannot hedge extinction" — Proposition 3, linear in $(1-\delta)$. ✓
7. "Disagreement about extinction risk can partially unwind the friction" — Proposition 4. ✓
8. "Cash-flow premium remains when friction resolves" — Setting $\pi = 1$ in eq. (17). ✓
9. "The hedging amplification is largest in an intermediate regime" — Qualitatively correct intuition, though the formal result (Proposition 5) has the proof error noted above. The verbal claim is directionally supported by the model structure.
10. All calibration claims (29% premium, 2–2.7× with differential growth, 3.3% welfare gain) match the verified numerical results. ✓

No unsupported verbal claims found.


## Summary

The core model (Sections 2–3) is mathematically rigorous: notation is consistent, assumptions are compatible, Propositions 1–4 and Corollaries 1–2 are correctly derived, and all numerical results verify. The failure is isolated to Proposition 5 in the extension (Section 4.3), where the proof's claimed sufficient condition ($Y_O = \bar{Y}(1+\theta)$) does not deliver the stated convergence result. The fix is straightforward — require super-linear growth of $Y_O$ in $\theta$ — but as stated, the proof is incorrect.
