# tests/theory-correctness.py
Started: 2026-03-22 09:46:19 EDT
Runtime: 4m 8s
[ralph-garage/agent-logs/20260322T134619.329981Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T134619.329981Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All four conditions are satisfied; notation is consistent, assumptions are compatible, all results derive logically from assumptions, and verbal claims are supported by formal theory.

## Condition 1: Notational Consistency

All mathematical objects grouped by concept use consistent notation throughout:

- **Consumption/dividends**: $c_t$, $D_t^A$, $D_t^N$ — consistent across all sections.
- **Parameters**: $\beta$, $\gamma$, $g$, $\theta$, $\phi$, $\lambda$ — defined once and used consistently.
- **Derived quantities**: $s$ (AI dividend share), $a$ (effective discount factor), $J$ (consumption jump factor), $\bar{v}$ (benchmark P/D) — consistent.
- **P/D ratios**: $v^A$, $v^N$ — consistent.
- **Market access**: $\alpha$, $\psi$, $\tilde{s}(\alpha)$ — consistent.
- **Extension parameters**: $\delta$, $\delta_H$, $\delta_O$, $\pi$, $Y_O$, $k$ — consistent; general $\delta$ used in Proposition 3, then split into household/owner beliefs in Proposition 4.

No notational conflicts found.

## Condition 2: Consistent Assumptions

Key assumptions:
1. CRRA utility with $\gamma > 1$, $\beta \in (0,1)$.
2. $c_t = D_t^A + D_t^N$ (consumption equals total dividends).
3. $s = D_t^A / c_t$ constant pre-singularity.
4. Singularity probability $\lambda \in (0,1)$, one-time event.
5. Normal growth at rate $g > 0$ for both dividends.
6. Singularity: AI dividends jump by $(1+\theta)$, non-AI drop by $(1-\phi)$; $\theta > 0$, $\phi \in (0,1)$.
7. $a = \beta(1+g)^{1-\gamma} < 1$.

Consistency checks:
- Assumption 3 (constant $s$) is consistent with Assumption 5: in normal transitions, both dividends grow at $g$, so the ratio is preserved.
- Assumption 7 ($a < 1$) follows automatically from $\gamma > 1$, $\beta < 1$, $g > 0$.
- All assumptions can simultaneously hold.

## Condition 3: Logical Results

Verified all propositions and key equations:

**Proposition 1 (Valuations)**: Euler equation derivation verified algebraically. The expansion into no-singularity and singularity paths, solving for $v^A$, and substituting $1 + \bar{v} = 1/(1-a)$ correctly yields eq. (7). Derivation for $v^N$ is symmetric.

**Proposition 2 (Hedging Premium)**: Subtraction of eq. (8) from eq. (7) correctly yields eq. (8). Parts (i)–(iii) verified:
- (i) $\partial/\partial\lambda[\lambda/(1-a+\lambda a)] = (1-a)/(1-a+\lambda a)^2 > 0$.
- (ii) $\partial J/\partial s = \theta + \phi > 0$ and $J < 1$ with $\gamma > 1$ implies $J^{-\gamma}$ decreasing in $s$.
- (iii) At $\lambda = 0$, ratio = 1; at $\lambda = 1$, ratio = $(1+\theta)/(1-\phi)$.

**Decomposition (eq. 9)**: Correctly separates $J^{-\gamma}$ as hedging amplifier from cash-flow premium.

**Corollary 1 (Partial Market Access)**: Follows directly from Proposition 2(ii) with $\tilde{s}$ replacing $s$.

**Proposition 3 (Extinction)**: Extinction state contributes zero to Euler equation (standard Barro convention for CRRA); premium scales by $(1-\delta)$.

**Proposition 4 (Disagreement)**: Four sub-states (extinction, survive+friction, survive+resolve, no singularity) correctly enumerated. Algebra verified: the two surviving-state contributions sum to the expression in eq. (12).

**Proposition 5 (Hump Shape)**: Part (i): $(1-\pi) \to 0$ as $Y_O \to \infty$, so hedging component vanishes. Part (ii): $(J^{-\gamma}-1)(\theta+\phi) \sim \theta^{1-\gamma}$ for large $\theta$ (with $\gamma > 1$), which declines; combined with $(1-\pi) = k/Y_O \to 0$, the hump shape follows.

**Numerical verification** at baseline ($\lambda = 0.02$): $a = 0.9227$, $\bar{v} = 11.94$, $J = 0.82$, $J^{-\gamma} = 1.81$, $v^A = 16.2$, $v^N = 12.6$, premium = 3.6, ratio = 1.29. All match Table 1.

## Condition 4: Interpretations

Key claims and their formal support:

| Claim | Support |
|-------|---------|
| AI stocks command a premium increasing in singularity probability | Proposition 2(i) |
| Premium decreasing in AI share | Proposition 2(ii) |
| Incomplete markets amplify the premium; complete markets drive hedging amplifier to 1 | Decomposition eq. (9): $J^{-\gamma} \to 1$ as $\tilde{s} \to \phi/(\theta+\phi)$ |
| Hedging demand roughly doubles the cash-flow premium | $J^{-\gamma} \approx 1.81$ at baseline |
| AI stocks act as insurance | $D^A$ surges when $c_t$ drops; formal: $J < 1$ and $(1+\theta) > 1$ |
| Self-limiting mechanism: larger AI share reduces premium | Proposition 2(ii) |
| Extinction risk reduces premium linearly | Proposition 3 |
| Disagreement about extinction can unwind friction | Proposition 4: premium decreasing in $\pi$ and $\delta_O$ |
| Hedging amplification is hump-shaped in severity | Proposition 5 |
| Singularity channel + growth can account for observed 2–2.7× gap | Calibration: 1.29× from model, residual 1.6–2.1× implies 3–5pp growth premium |

Minor note: The introduction refers to "the gap between AI and market portfolio valuations" but the formal premium is $v^A - v^N$ (AI vs. non-AI stocks). Since $s = 0.15$, the market portfolio P/D $\approx 0.85 v^N + 0.15 v^A \approx v^N$, so the distinction is economically negligible. This is a wording imprecision, not a theoretical error.

All verbal claims are supported by formal theory.
