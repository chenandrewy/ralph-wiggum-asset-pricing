# tests/theory-correctness.py
Started: 2026-03-22 10:08:02 EDT
Runtime: 6m 32s
[ralph-garage/agent-logs/20260322T140802.519168Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T140802.519168Z_theory-correctness_claude_opus.log)

# theory-correctness

VERDICT: PASS

REASON: All notation is consistent, assumptions are mutually compatible, all results derive logically from the assumptions, and all verbal claims are supported by the formal theory.

## 1. Notational Consistency

All mathematical objects grouped by concept:

- **Consumption/Preferences:** $c_t$ (consumption), $\gamma$ (RRA coefficient, $\gamma > 1$), $\beta$ (discount factor, $\beta \in (0,1)$). Used consistently throughout.
- **Dividends:** $D_t^A$ (AI), $D_t^N$ (non-AI). Superscripts $A$/$N$ used consistently.
- **AI share:** $s \equiv D_t^A / c_t$ (public share), $\tilde{s}(\alpha) = s + \alpha\psi$ (effective share with market access). Consistent.
- **Singularity parameters:** $\lambda$ (probability), $\theta$ (AI dividend jump), $\phi$ (non-AI dividend drop), $g$ (common growth rate). Consistent.
- **Derived quantities:** $J(s) = 1 - \phi + (\theta+\phi)s$ (consumption jump factor), $a = \beta(1+g)^{1-\gamma}$ (effective discount factor), $\bar{v} = a/(1-a)$ (benchmark P/D), $M_{t,t+1}$ (SDF). All consistent.
- **Market access:** $\alpha \in [0,1]$ (market-access parameter), $\psi > 0$ (private AI capital size). Consistent.
- **Extension parameters:** $\delta$ ($\delta_H$, $\delta_O$) for extinction probability, $\pi$ for friction-resolution probability, $Y_O$ for post-singularity output, $d$ for adverse-selection discount. All consistent.

No notational conflicts found.

## 2. Consistent Assumptions

All mathematical assumptions:

1. CRRA preferences: $\gamma > 1$, $\beta \in (0,1)$ (eq. 1)
2. Budget constraint: $c_t = D_t^A + D_t^N$ (eq. 2)
3. Constant pre-singularity AI share: $s \equiv D_t^A / c_t$ (eq. 3)
4. Singularity probability: $\lambda \in (0,1)$ (Section 2.2)
5. Normal growth: $D_{t+1}^i = (1+g)D_t^i$, $g > 0$ (eq. 4)
6. Singularity growth: AI multiplied by $(1+\theta)(1+g)$, non-AI by $(1-\phi)(1+g)$ (eq. 5)
7. Parameter restrictions: $\theta > 0$, $\phi \in (0,1)$ (after eq. 5)
8. Finite valuations: $a < 1$ (eq. 8)
9. Market access: $\alpha \in [0,1]$, $\psi > 0$ (Section 2.3)
10. Extinction: $\delta \in [0,1)$ (Section 4.1)
11. Friction resolution: $\pi \in [0,1]$, $\pi(Y_O) = 1 - d/Y_O$ for $Y_O \geq d$ (Section 4.3)

Consistency checks:
- Assumption 3 (constant $s$) is consistent with assumption 5 (common growth rate $g$): if both dividends grow at $g$, their ratio is constant. ✓
- Assumption 8 ($a < 1$) follows from assumptions 1 ($\gamma > 1$, $\beta < 1$) and 5 ($g > 0$): $(1+g)^{1-\gamma} < 1$ when $\gamma > 1$, so $a = \beta(1+g)^{1-\gamma} < 1$. ✓
- The consumption jump $J(s) = 1 - \phi + (\theta+\phi)s$ is derived from assumptions 2, 3, 6. With baseline parameters, $J = 0.82 < 1$, consistent with the "negative singularity" condition $s < \phi/(\theta+\phi) = 0.375$. ✓
- No pair of assumptions is contradictory.

## 3. Logical Results

All derived results traced back to assumptions:

**Post-singularity P/D (eq. 7):** From the Euler equation with deterministic growth $g$: $v = a(1+v) \Rightarrow v = a/(1-a)$. ✓

**Proposition 1 (eqs. 9–10):** The Euler equation for the AI stock expands to $v^A = (1-\lambda)a(1+v^A) + \lambda a J^{-\gamma}(1+\theta)(1+\bar{v})$. Solving yields eq. 9. Verified algebraically and numerically. ✓

**Proposition 2 (eq. 11):** Subtracting eq. 10 from eq. 9 yields the premium. Comparative statics in (i)–(iii) verified:
- (i) $\partial/\partial\lambda$ of $\lambda/(1-a+\lambda a)$ is $(1-a)/(1-a+\lambda a)^2 > 0$. ✓
- (ii) $\partial J/\partial s = \theta+\phi > 0$ and $J < 1, \gamma > 1 \Rightarrow J^{-\gamma}$ decreasing in $s$. ✓
- (iii) Boundary values at $\lambda=0$ (ratio=1) and $\lambda=1$ (ratio=$(1+\theta)/(1-\phi)$) verified. ✓

**Decomposition (eq. 12):** Factoring $J^{-\gamma}$ from the premium expression yields the cash-flow premium times the hedging amplifier. ✓

**Corollary 1:** Since $\tilde{s}(\alpha)$ is increasing in $\alpha$ and the premium is decreasing in effective share, the premium is decreasing in $\alpha$. ✓

**Proposition 3 (eq. 14):** Extinction state contributes zero to the Euler equation (standard convention for CRRA with extinction: $M \cdot 0$ product handled via the survival-conditional pricing interpretation standard in the rare disasters literature). Scaling the singularity contribution by $(1-\delta)$ yields eq. 14. ✓

**Proposition 4 (eq. 15):** The singularity-survival state splits into friction-persists (probability $(1-\pi)$, hedging amplifier $J^{-\gamma}$) and friction-resolves (probability $\pi$, hedging amplifier 1). Summing gives eq. 15. Verified by expanding the proof's four sub-states. ✓

**Proposition 5 (hump-shaped):** With $\pi = 1 - d/Y_O$ and $Y_O$ increasing in $\theta$: (i) as $\theta \to \infty$, $(1-\pi) \to 0$ so hedging component vanishes; (ii) for small $\theta$, the dividend-differential growth dominates the declining hedging amplifier, while for large $\theta$, friction resolution dominates. The claim is conditional on $Y_O$ growing sufficiently fast, which is stated. ✓

**Numerical verification:** All values in Tables 1–3 independently computed and match the paper to within rounding (±0.1 on P/D ratios). ✓

## 4. Interpretations

Key verbal economic claims and their formal support:

| Claim | Support |
|-------|---------|
| AI stocks command a valuation premium | Prop. 2: $v^A - v^N > 0$ (eq. 11, all terms positive) |
| Premium increases with singularity probability | Prop. 2(i) |
| Premium decreases with AI share | Prop. 2(ii) |
| Incomplete markets are essential; complete markets collapse hedging amplifier to 1 | Corollary 1: as $\alpha \to 1$, $\tilde{s}$ rises, $J \to 1$, $J^{-\gamma} \to 1$ |
| Hedging demand roughly doubles the cash-flow premium | $J^{-\gamma} \approx 1.81$ at baseline; "roughly doubles" is reasonable |
| Self-limiting mechanism: larger AI share reduces the premium | Prop. 2(ii) |
| AI stocks cannot hedge extinction | Prop. 3: premium scaled by $(1-\delta)$ |
| Disagreement reduces hedging amplification but cash-flow premium remains | Prop. 4: at $\pi=1$, hedging amplifier = 1 but $(\theta+\phi)$ term persists |
| Hedging amplification largest in intermediate regime | Prop. 5 (hump-shape) |
| 29% premium at $\lambda=0.02$ | Table 1: $v^A/v^N = 1.29$, verified numerically |
| Residual growth premium of 3–5 pp consistent with data | $2.0/1.29 \approx 1.55$ to $2.7/1.29 \approx 2.09$; Gordon model growth differentials in this range are plausible |
| Risk-neutral investor pays cash-flow premium only | $\gamma \to 0 \Rightarrow J^{-\gamma} \to 1$, leaving only cash-flow component |

All key claims are supported by the formal results.
