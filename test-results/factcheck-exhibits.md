# tests/factcheck-exhibits.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 3m 20s
[ralph-garage/agent-logs/20260414T102326.833098-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260414T102326.833098-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from verified code logic, with no artifacts, labeling errors, or unsupported features.

## Figure 1: Valuation Ratios and the AI Premium (fig:ai-valuations)

**Description.** Two-panel time-series figure. Panel (a) plots the S&P 500 trailing price-dividend ratio from the Shiller dataset (2000--present). Panel (b) plots the NASDAQ Composite price relative to the S&P 500, normalized to January 2015 = 100.

### Suspicious features

1. **Dot-com spike in both panels (~2000).** Both panels show a sharp spike around 2000, which could be an artifact if the data join or normalization were wrong.
2. **Recent elevation in Panel (a).** P/D reaches historically high levels (appearing to approach or exceed 80), which could reflect a data error or stale dividend figures.

### Code check

1. **Dot-com spike.** The code downloads the Shiller dataset from datahub.io (`s-and-p-500/r/data.csv`) and NASDAQ from FRED (`NASDAQCOM`). Panel (a) computes `PD = SP500 / Dividend` directly from the Shiller columns. Panel (b) computes `Ratio = NASDAQ / SP500` from the merged monthly series and normalizes to Jan 2015 via `which.min(abs(Date - as.Date("2015-01-01")))`. The dot-com spike is a well-known feature of both series and is correctly reflected. No aggregation or join error.
2. **Recent P/D elevation.** Trailing P/D ratios of 60--80+ for the S&P 500 are consistent with recent market conditions (high prices, moderate dividend yields). The code filters `Dividend > 0` and uses the Shiller trailing dividend, which is standard. No stale-data artifact.

**Data note.** The underlying data is downloaded live from datahub.io and FRED rather than stored locally. The code logic for computing P/D and the normalized ratio is verified as correct. The data sources are authoritative public financial datasets.

**Caption check.** Caption states sources as "NASDAQ from FRED; S&P 500 from the Shiller dataset" --- matches code. Caption states normalization to "January 2015 = 100" --- matches code (`base_ratio` anchored to closest date to 2015-01-01).

**Exhibit verdict: PASS.** Visible features are real market patterns; code logic is correct.

## Table 1: Price-Dividend Ratios (tab:pd-ratios)

**Description.** Model-generated table of P/D ratios for AI stocks vs. non-AI stocks across a grid of annual singularity probabilities ($p$) and extinction probabilities ($\xi$). Parameters: $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$.

### Suspicious features

1. **AI P/D jumps sharply at high $p$.** At $p=1.0\%$, $\xi=0\%$, AI P/D is 26.5 vs. 13.3 for non-AI (ratio 2.0). The steep sensitivity to $p$ could indicate a near-divergence.
2. **Non-AI P/D is insensitive to $\xi$.** Non-AI P/D barely changes across $\xi$ values within a $p$ group (e.g., 11.1 to 10.6 for $p=0.5\%$).

### Code check

1. **Sharp AI P/D at high $p$.** Verified by manual computation. The AI SDF-weighted dividend growth factor $\Gamma^{AI} = 3.2$ is large (share reallocation + aggregate jump), making the pricing kernel $K$ approach 1 as $p$ grows. At $p=1\%$, $\xi=0$: $K_{non} \approx 0.930$, giving P/D $\approx 13.3$ (matches table). The AI exact recursion over the $\theta$-chain gives 26.5, consistent with the approximate formula showing $K_{AI}$ closer to 1. This is a real model feature, not an error.
2. **Non-AI insensitivity to $\xi$.** Extinction probability $\xi$ only enters through the singularity term $p(1-\xi)S\Gamma$. For non-AI stocks, $\Gamma^N = 1.2$ and $S = \phi^{-\gamma}(1+\eta)^{-\gamma} \approx 3.16$, so the singularity contribution is modest. Varying $\xi$ from 0% to 20% scales a small term, producing small P/D changes. Verified: correct.

**Parameter check.** Code parameters ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.50$, $\eta=0.50$, $\theta=0.15$, $\Delta\theta=0.20$) match the table footnote exactly.

**Spot-check values.**
- $p=0.1\%$, $\xi=0\%$: Non-AI P/D hand-computed as $\approx 9.8$ (matches table). AI P/D $\approx 10.4$ (matches table).
- $p=1.0\%$, $\xi=0\%$: Non-AI P/D hand-computed as $\approx 13.3$ (matches table).
- Ratios are consistent with $\text{P/D}^{AI}/\text{P/D}^{N}$ at one decimal place throughout.

**Exhibit verdict: PASS.** All values verified against code logic and manual computation; monotonicity patterns are correct.

## Figure 2: Government Transfers and the Singularity (fig:extension-panels)

**Description.** Two-panel figure showing how government transfers (tax rate $\tau$) affect AI stock valuations and household consumption in the singularity state. Panel (a): AI stock P/D ratio vs. $\tau$ for baseline ($\eta=0.5$, $\phi=0.5$) and large singularity ($\eta=9$, $\phi=0.05$). Panel (b): household consumption multiple in the singularity vs. $\tau$ (log scale). Parameters: $p=0.5\%$, $\xi=5\%$, $\alpha=0.70$, $\delta=0.50$.

### Suspicious features

1. **Panel (a): Large-singularity P/D divergence at low $\tau$.** The blue dashed line is capped/clipped at the top of the y-axis with an annotation "P/D $\to \infty$ as $\tau \to 0$." This is an extreme claim.
2. **Panel (b): Catastrophe annotation at $\tau=0$.** The large-singularity scenario shows a 50% consumption loss at $\tau=0$, marked as "Catastrophe."
3. **Panel (b): Baseline annotations.** Two labeled points on the baseline curve show "1.1$\times$" at $\tau=0.30$ and a value near $\tau=0.47$.

### Code check

1. **P/D divergence.** At $\tau=0$ for the large singularity: $\phi_{eff}=0.05$, $S = 0.05^{-4} \times 10^{-4} = 16$, $\Gamma^{AI}_1 \approx 21.3$. The pricing kernel $K \approx 0.905 \times (0.995 + 0.00475 \times 16 \times 21.3) \approx 0.905 \times 2.62 \approx 2.37 > 1$. Since $K > 1$, the P/D sum diverges --- confirmed by the existence condition in Remark 1 of the paper. As $\tau$ increases, $\phi_{eff}$ grows, $S$ shrinks, and $K$ drops below 1, restoring finite P/D. The code caps the y-axis at `ceiling(max baseline P/D)` and adds the annotation. **Verified: real feature, correctly generated.**

2. **Catastrophe at $\tau=0$.** Code: `consumption_growth(0, 9.0, 0.05) = 0.05 * (1+9) = 0.5`. This is a 50% consumption loss. The annotation reads "Catastrophe: 50% loss" with a point at $(0, 0.5)$. For baseline: `consumption_growth(0, 0.5, 0.5) = 0.5 * 1.5 = 0.75`, a 25% loss, annotated as "25% loss." Both match. **Verified: correct.**

3. **Baseline annotation values.** Code computes `consumption_growth(0.30, 0.5, 0.5) = 0.75 + 0.30 \times 0.85 \times (0.65/0.70) \times 1.5 \approx 1.105$, displayed as "1.1$\times$" via `sprintf("%.1f", ...)`. At $\tau=0.47$: `consumption_growth(0.47, 0.5, 0.5) \approx 1.25$, displayed as "1.3$\times$." **Verified: correct.**

**Parameter check.** Caption states $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$. Code: `alpha0=0.70`, `p_ext=0.005`, `xi_ext=0.05`, `delta=0.50`. All match. Legend labels show $\eta$ and $\phi$ values matching `eta_val` and `phi_val` in the code.

**Exhibit verdict: PASS.** All suspicious features traced to correct model mechanics and verified computationally.
