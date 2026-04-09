# tests/factcheck-exhibits.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 4m 54s
[ralph-garage/agent-logs/20260409T182005.673607-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T182005.673607-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits

VERDICT: PASS
REASON: All three exhibits are correctly generated, and all paper claims about exhibit values match the underlying computations.

## Figure 1: AI Valuations vs. the Broader Market

**Description:** A line chart comparing price-earnings ratios for "AI-Exposed Firms" and the "S&P 500" from 2015 to 2025. The AI line rises steeply after 2022 (from ~38 to ~75), while the market line stays in the 18--25 range.

### Suspicious features

1. **Hardcoded data with no external source file.** The P/E values are defined inline in the code (`pe_market` and `pe_ai` vectors at `generate-exhibits.R:186-187`) rather than loaded from a data file.
2. **Sharp acceleration in AI P/E from 2023 onward** (42 to 62 to 75).

### Code check

1. The caption explicitly says "(Illustrative)" and the paper text says "based on approximate values from public sources." The code comments say "Illustrative P/E data based on publicly available market patterns." The hardcoded values are intentional and transparently disclosed. The S&P 500 values (18--26 range) and AI-firm values are broadly plausible for the stated period. **Verified: correctly labeled as illustrative.**
2. The sharp rise from 2023 onward reflects the generative-AI boom. The paper does not claim these are exact figures. **Verified: consistent with the illustrative framing.**

**Exhibit verdict: PASS** -- Data is illustrative, transparently labeled, and plausible.

## Table 1: Price-Dividend Ratios (AI Stocks vs. Non-AI Stocks)

**Description:** A table of P/D ratios for AI and non-AI stocks across a grid of singularity probabilities ($p \in \{0.1\%, 0.2\%, 0.5\%, 0.8\%, 1.0\%\}$) and extinction probabilities ($\xi \in \{0\%, 5\%, 10\%, 20\%\}$), with parameters $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$.

### Suspicious features

1. **Extreme AI P/D at $p=1\%$, $\xi=0\%$ (76.4)** -- roughly 6x the non-AI value. Potentially near a pole in the valuation formula.
2. **Non-AI P/D increases with $p$** (from 9.8 at $p=0.1\%$ to 13.3 at $p=1\%$ for $\xi=0\%$), which is less intuitive since singularity displaces non-AI firms.

### Code check

1. **P/D=76.4 at $p=1\%$, $\xi=0\%$:** Independently recomputed. The formula is $K / (1-K)$ where $K = \beta(1+g)^{1-\gamma}[(1-p) + p(1-\xi)\phi^{-\gamma}(1+\eta)^{-\gamma}\gamma_j^{AI}]$. At these parameters, $K = 0.987$ (close to 1), producing $P/D = 0.987/0.013 = 76.4$. All 20 table cells verified to match the code output exactly. **Verified: correct.**
2. **Non-AI P/D rising with $p$:** The SDF in the singularity state is $\phi^{-\gamma}(1+\eta)^{-\gamma}\gamma_j^{N}$. With $\gamma_j^{N} = 0.8 \times 1.5 = 1.2$ and $\phi^{-4}(1.5)^{-4} = 16 \times 0.1975 = 3.16$, the singularity-state SDF contribution is $3.16 \times 1.2 = 3.79$, which exceeds 1. So singularity states are high marginal-utility states where even non-AI dividends (which shrink in share but benefit from aggregate growth) are valued. Higher $p$ increases the weight on these high-SDF states, raising non-AI P/D. **Verified: economically and mathematically correct.**

**Paper cross-check:** The text says "roughly 18" for AI P/D at $p=0.5\%$, $\xi=0\%$ (actual: 17.5) and "nearly 6 to 1" for the ratio at $p=1\%$ (actual: 5.8). Both are acceptable approximations.

**Exhibit verdict: PASS** -- All 20 cells independently verified; paper claims match.

## Figure 2: Government Transfers and the Singularity

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate $\tau$ for Baseline ($\eta=0.5$) and Large singularity ($\eta=9$) scenarios. Panel (b) shows household consumption growth in the singularity state vs. $\tau$, with a dashed "No change" reference line at $y=1$.

### Suspicious features

1. **Baseline P/D appears to start at an extremely high value and drop steeply** in Panel (a), suggesting near-singular behavior at low $\tau$.
2. **Large singularity P/D appears essentially flat** across all $\tau$ values in Panel (a), showing almost no response to transfers.
3. **Baseline consumption growth starts below 1** in Panel (b), meaning the singularity hurts households absent transfers.

### Code check

1. **Near-singular Baseline P/D:** At $p=3\%$, $\xi=5\%$, the Euler-equation coefficient $K$ exceeds 1 for $\tau < 0.12$ (producing NA / infinite P/D). At $\tau=0.12$, $K=0.9993$ yielding $P/D=1510$; at $\tau=0.15$, $P/D=53.7$; at $\tau=0.30$, $P/D=13.9$. The code filters out NA values (`filter(!is.na(pd_ai))`), so the plotted line begins at the first finite value and drops steeply. This is a genuine feature of the Gordon-growth-style formula: as $K \to 1^-$, $P/D \to \infty$. **Verified: mathematically correct, real model feature.**
2. **Flat Large singularity line:** With $\eta=9$, $(1+\eta)^{-\gamma} = 10^{-4} = 0.0001$, making the singularity-state SDF contribution negligible. P/D varies from 7.22 ($\tau=0$) to 7.17 ($\tau=0.7$), a range of 0.05. Changes in $\phi_{\text{eff}}$ via transfers cannot move the needle when the SDF weight on the singularity state is $10^{-4}$. **Verified: correct and economically sensible.**
3. **Baseline consumption at $\tau=0$:** $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$. The paper states "household consumption falls to 75% of its pre-singularity level," which matches. **Verified: correct.**

**Paper cross-check:** The text correctly states that "absent transfers ($\tau=0$), the singularity reduces household consumption" and that "under a large singularity, even high tax rates produce substantial consumption gains." Both match the computed values (consumption growth = 5.0 to 9.2 for $\eta=9$).

**Exhibit verdict: PASS** -- All features trace to correct model mechanics; paper claims match.
