# tests/factcheck-exhibits.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 3m 52s
[ralph-garage/agent-logs/20260409T194838.566317-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T194838.566317-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and consistent with the paper's formulas and claims.

## Figure 1: AI Valuations vs. the Broader Market

Shows NASDAQ Composite (solid) and S&P 500 (dashed), each normalized to January 2015 = 100, plotted monthly through the end of the available sample. NASDAQ dramatically outpaces S&P 500, with the gap widening after 2023.

### Suspicious features

- **Sharp acceleration post-2023**: The NASDAQ line steepens noticeably around 2023, creating a widening gap. This could be an artifact of data processing or an outlier.
- **End-of-sample divergence**: By the end of the sample, NASDAQ appears to reach roughly 4--5x its 2015 level while S&P 500 reaches roughly 3x.

### Code check

- The NASDAQ data is downloaded from FRED (series NASDAQCOM) and S&P 500 from the Shiller/datahub dataset. Both are real market data, not model-generated (`generate-exhibits.R:220-268`).
- Normalization divides by the first common month's value and multiplies by 100 (`generate-exhibits.R:265-269`). This correctly implements the caption's "January 2015 = 100."
- The post-2023 acceleration reflects real market movements driven by AI/generative-AI enthusiasm. The magnitudes (NASDAQ ~4-5x, S&P ~3x over 2015--2025) are consistent with publicly known index performance.
- Both series use monthly last-observation aggregation (`to_monthly` function, line 249), which is standard.

**Exhibit verdict: PASS** — Data sourced from standard public repositories; normalization is correct; visual features reflect real market movements.

## Table 1: Price-Dividend Ratios

Reports P/D ratios for AI and non-AI stocks across a grid of singularity probabilities ($p \in \{0.1\%, 0.2\%, 0.5\%, 0.8\%, 1.0\%\}$) and extinction risks ($\xi \in \{0\%, 5\%, 10\%, 20\%\}$). Parameters: $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$.

### Suspicious features

- **Large AI P/D at $p=1\%$, $\xi=0\%$**: The AI stock P/D ratio reaches 76.4, dramatically higher than the non-AI value of 13.3 (ratio 5.8). This could indicate a near-singularity in the pricing formula.
- **Non-AI P/D barely moves**: Non-AI P/D ranges only from 9.7 to 13.3 across the entire grid, while AI P/D ranges from 10.2 to 76.4.

### Code check

- The `compute_pd` function (`generate-exhibits.R:42-48`) implements $K / (1-K)$ where $K = \beta(1+g)^{1-\gamma}[(1-p) + p(1-\xi)\phi^{-\gamma}(1+\eta)^{-\gamma}\Gamma^j]$. This matches the paper's Proposition 1 (equations 4--5).
- Dividend growth factors: $\Gamma^{AI} = 2.1333 \times 1.5 = 3.2$, $\Gamma^{N} = 0.8 \times 1.5 = 1.2$. These match the paper's definitions.
- Independent recomputation of five representative cells ($p=0.1\%/\xi=0\%$; $p=0.5\%/\xi=0\%$; $p=0.5\%/\xi=5\%$; $p=1.0\%/\xi=0\%$; $p=1.0\%/\xi=20\%$) all match the table to one decimal place.
- The large AI P/D at $p=1\%$ is explained by $K$ approaching 1: $K = 0.987$, so $P/D = 0.987/0.013 = 76.4$. The formula is correct; the asset's hedge value is near-explosive. This is economically discussed in Remark 1.
- Non-AI P/D moves less because $\Gamma^N = 1.2$ is much smaller than $\Gamma^{AI} = 3.2$, so the singularity term has less weight.

**Exhibit verdict: PASS** — All table entries verified against independent recomputation of the closed-form formula; patterns are economically consistent.

## Figure 2: Government Transfers and the Singularity

Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate $\tau$ for two scenarios: baseline ($\eta=0.5$, $\phi=0.5$) and large singularity ($\eta=9$, $\phi=0.05$). Panel (b) shows household consumption growth in the singularity state vs. $\tau$, with catastrophe markers at $\tau=0$.

### Suspicious features

- **Large singularity P/D line starts mid-range in Panel (a)**: The blue (large singularity) line does not begin at $\tau=0$ but appears around $\tau \approx 4\text{--}5\%$. This gap could indicate a coding error or boundary issue.
- **Steep initial drop in Panel (a) large singularity**: Where the large-singularity line first appears, it starts at a very high P/D and drops steeply, creating a near-vertical segment.
- **Log-scale Panel (b)**: The y-axis uses a log scale, which could visually compress or exaggerate features.
- **Catastrophe markers at $\tau=0$**: Annotated as 50% loss (large) and 25% loss (baseline).

### Code check

- **Missing P/D at low $\tau$**: At $\tau=0$, the large singularity has $\phi^{-\gamma} = 0.05^{-4} = 160{,}000$, making $K = 2.37 \gg 1$. The function correctly returns NA. Independent computation shows $K$ drops below 1 between $\tau=0.03$ and $\tau=0.04$ (at $\tau=0.04$: $K=0.978$, $P/D=45.2$; at $\tau=0.03$: $K=1.035$, undefined). This matches the visible gap in Panel (a) and is correctly discussed in the paper as a violation of the existence condition (Remark 1).
- **Steep initial drop**: At $\tau=0.04$, $P/D \approx 45$; at $\tau=0.05$, $P/D \approx 18.5$. The steep decline is real: small increases in $\tau$ dramatically increase $\phi_{\text{eff}}$, which enters the formula at the $-\gamma = -4$ power. Correct behavior.
- **Effective phi**: `phi_eff = phi_val + tau*(1-delta0*tau)*(1-phi_val*alpha0)/alpha0` (`generate-exhibits.R:119`). This matches the transfer model: transfers increase the household's effective consumption share in the singularity state without altering AI stock dividends (taxes fall on AI owners' private surplus, not public stock dividends).
- **Consumption growth at $\tau=0$**: Baseline: $0.5 \times 1.5 = 0.75$ (25% loss). Large: $0.05 \times 10 = 0.50$ (50% loss). Both verified independently and match the annotations.
- **Baseline P/D at $\tau=0$**: Matches Table 1 entry for $p=0.5\%$, $\xi=5\%$: $P/D = 16.7$. Verified.
- **Log scale in Panel (b)**: Appropriate given the large range of consumption growth values (0.5 to 5+). Not misleading.

**Exhibit verdict: PASS** — All suspicious features trace to correct code logic; the undefined-P/D gap is a genuine economic feature, not an artifact; numerical values verified independently.
