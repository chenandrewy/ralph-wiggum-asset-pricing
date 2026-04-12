# tests/factcheck-exhibits.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 4m 39s
[ralph-garage/agent-logs/20260411T211526.523247-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T211526.523247-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits verified against generating code; no artifacts, errors, or unsupported features found.

## Figure 1: Valuation Ratios and the AI Premium (page 2)

Two-panel empirical figure. Panel (a) shows the S&P 500 trailing 12-month price-dividend ratio from the Shiller dataset, 2000–present. Panel (b) shows the NASDAQ Composite / S&P 500 price ratio, normalized to January 2015 = 100, using NASDAQ data from FRED.

### Suspicious features

1. **Dot-com P/D peak around 60–80**: The P/D ratio in panel (a) reaches very high levels circa 2000. This is consistent with known Shiller data during the dot-com bubble (trailing P/D ratios were extreme due to low dividend yields).
2. **NASDAQ/S&P ratio decline from 2000–2010 then rise from 2015**: The pattern in panel (b) is consistent with the dot-com bust (NASDAQ fell more than S&P) and the subsequent AI/tech boom.
3. **No local data cache**: The code downloads data from external URLs (datahub Shiller CSV, FRED) with no local cache.

### Code check

- Panel (a): `PD = SP500 / Dividend` (line 310) computes trailing P/D from the Shiller dataset's nominal price and trailing 12-month dividend. The y-axis label "Price / Trailing Dividend" matches. The date filter `>= 2000-01-01` (line 369) matches the visible x-axis range.
- Panel (b): NASDAQ/S&P price ratio is computed via `inner_join` on monthly data (lines 352–357). Normalization to Jan 2015 = 100 is at lines 382–383, matching the dashed reference line at y=100 (line 387) and the y-axis label. The caption correctly states the normalization base.
- No suspicious visual features found. The dot-com peak and recent AI boom are expected empirical patterns. While no local data cache exists, there are no visually suspicious features requiring data-level verification.

**Exhibit verdict: PASS** — Visible features are consistent with known market data and code logic is correct.

## Table 1: Price-Dividend Ratios (page 9)

Model-generated table showing P/D ratios for AI stocks, non-AI stocks, and their ratio across a grid of singularity probability $p \in \{0.1\%, 0.2\%, 0.5\%, 0.8\%, 1.0\%\}$ and extinction probability $\xi \in \{0\%, 5\%, 10\%, 20\%\}$. Parameters: $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$.

### Suspicious features

1. **AI P/D ratios rise steeply with $p$** (from 10.4 at $p=0.1\%$ to 26.5 at $p=1.0\%$, $\xi=0$): Could indicate a numerical issue at higher singularity probabilities.
2. **Ratio column values only range 1.1–2.0**: Appears narrow given the AI premium story.
3. **Non-AI P/D also rises with $p$**: Counterintuitive at first glance—why would non-AI stocks benefit from higher singularity probability?

### Code check

- **Spot-checked 10 cells** (5 non-AI, 5 AI) by replicating the R formulas in Python. All match the table to one decimal place: e.g., $p=0.5\%, \xi=0$: AI=15.5, non-AI=11.1; $p=1.0\%, \xi=0$: AI=26.5, non-AI=13.3.
- **Steep AI P/D rise** (feature 1): Correct. The exact backward recursion (`compute_pd_ai_exact`, lines 51–80) builds a 60-step chain of post-singularity $\theta$ values, accounting for the declining AI premium after each successive singularity. At high $p$, the initial singularity's large dividend growth factor ($\Gamma^{AI} = 3.2$) dominates. The steep rise is real, not a numerical artifact.
- **Narrow ratio range** (feature 2): Correct. Non-AI stocks also benefit from the singularity (aggregate consumption grows by $(1+\eta)$), so the ratio reflects only the *differential* benefit of the AI share reallocation, not the full singularity effect.
- **Non-AI P/D rising with $p$** (feature 3): Correct. The SDF-weighted singularity payoff for non-AI stocks has $\gamma^N = 1.2 > 1$, so the singularity component adds to valuations. Economically: even non-AI dividends grow in the singularity (aggregate consumption jumps 50%), and the SDF amplifies this because the household's marginal utility is high (displacement).
- The footnote correctly describes all parameters and states AI P/D ratios are "numerically exact."

**Exhibit verdict: PASS** — All values verified by independent replication; patterns are economically correct.

## Figure 2: Government Transfers and the Singularity (page 15)

Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate $\tau$ for two scenarios: baseline ($\eta=0.5, \phi=0.5$) and large singularity ($\eta=9, \phi=0.05$). Panel (b) shows household consumption growth in the singularity state vs. tax rate, with a log-scale y-axis. Parameters: $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$.

### Suspicious features

1. **Large-singularity P/D diverges as $\tau \to 0$** (panel a): The blue dashed line only appears at moderate $\tau$ with an annotation "P/D → ∞ as τ → 0."
2. **Catastrophe annotations** (panel b): "50% loss" for large singularity and "25% loss" for baseline at $\tau=0$.
3. **Large-singularity consumption growth rises extremely steeply** (panel b): The blue dashed line appears to reach values well above 1 quickly.
4. **Thick black dashed horizontal line at $y=1$** in panel (b): "No change" reference line.

### Code check

- **P/D divergence** (feature 1): Verified. At $\tau=0$ with $\phi=0.05$, $\eta=9$: $S = \phi^{-\gamma}(1+\eta)^{-\gamma} = 0.05^{-4} \times 10^{-4} = 16$. The terminal $K = B[(1-p) + p(1-\xi) \cdot S \cdot \Gamma^{AI}_{term}]$ where $\Gamma^{AI}_{term} \approx 10$ gives $K \approx 0.905 \times (0.995 + 0.005 \times 0.95 \times 16 \times 10) = 0.905 \times 1.755 \approx 1.59 > 1$, so `compute_pd_with_transfer` returns NA. This is correct: the existence condition is violated. As $\tau$ increases, $\phi_{eff}$ grows, $S$ falls, and eventually $K < 1$ producing finite P/D. The annotation is accurate.
- **Catastrophe annotations** (feature 2): Verified. Baseline: $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$, i.e., 25% loss. Large singularity: $\phi_{large}(1+\eta) = 0.05 \times 10 = 0.5$, i.e., 50% loss. Both match the code (`consumption_growth` function, lines 145–147) and annotations (lines 259–266).
- **Steep rise** (feature 3): Correct. With $\eta=9$, the $(1+\eta)=10$ multiplier on the transfer term produces rapid consumption growth. At $\tau=0.5$: transfer component $\approx 0.5 \times 0.75 \times (1-0.035)/0.70 \times 10 \approx 5.18$, total $\approx 5.68$. The log scale appropriately handles this range.
- **Reference line** (feature 4): Code line 257 places `geom_hline(yintercept = 1)` with "No change" label at line 267. Correct.
- Caption parameters ($\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$) match code: `alpha0=0.70`, `p_ext=0.005`, `xi_ext=0.05`, `delta=0.50`.

**Exhibit verdict: PASS** — All suspicious features traced to correct code logic and verified analytically.
