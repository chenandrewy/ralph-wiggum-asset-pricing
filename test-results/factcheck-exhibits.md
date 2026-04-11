# tests/factcheck-exhibits.py
Started: 2026-04-11 15:15:40 EDT
Runtime: 2m 52s
[ralph-garage/agent-logs/20260411T151540.064897-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T151540.064897-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated and consistent with their code, data sources, and paper claims.

## Figure 1: Prices of AI-Exposed Stocks vs. the Broader Market

**Description:** Time-series plot of monthly closing prices for the NASDAQ Composite (solid blue) and S&P 500 (dashed red), each normalized to January 2015 = 100, spanning 2015–2026.

### Suspicious features

1. **Sharp dip around 2022 followed by steep recovery (especially NASDAQ):** The NASDAQ drops noticeably around 2022 then recovers sharply through 2023–2025, with the gap between NASDAQ and S&P 500 widening dramatically.

2. **Y-axis label claims "Jan 2015 = 100" — does the normalization base actually start in January 2015?**

### Code check

1. **2022 dip and AI-era recovery:** The code downloads real market data — NASDAQ from FRED (`NASDAQCOM`) and S&P 500 from the Shiller/datahub dataset. The 2022 dip reflects the actual tech selloff, and the post-2023 surge reflects the generative AI rally. This is real market data, not a modeling artifact. **Verified: real and correct.**

2. **Normalization base:** The code filters both series to `Date >= "2015-01-01"`, aggregates to monthly (last observation per month), then normalizes via `base <- d$Value[which.min(d$Date)]`, which selects the earliest date in the filtered data. Since the filter starts at 2015-01-01, the first month is January 2015. The y-axis label "Jan 2015 = 100" is accurate. **Verified: correct.**

**Exhibit verdict: PASS** — Data is sourced from FRED and Shiller, normalization is correct, and visible patterns reflect real market movements.

## Table 1: Price-Dividend Ratios — AI Stocks vs. Non-AI Stocks

**Description:** A grid of model-implied P/D ratios for AI and non-AI stocks across five singularity probabilities (p = 0.1%–1.0%) and four extinction probabilities (ξ = 0%–20%). Parameters: β = 0.96, g = 0.02, γ = 4, φ = 0.5, η = 0.5, θ = 0.15, Δθ = 0.2.

### Suspicious features

1. **AI P/D grows rapidly with p while non-AI P/D grows modestly:** At p = 0.1%, AI P/D ≈ 10.4 and non-AI ≈ 9.8 (ratio 1.1). At p = 1.0%, AI P/D ≈ 26.5 vs non-AI ≈ 13.3 (ratio 2.0). The AI premium accelerates non-linearly.

2. **Ratios are rounded to one decimal place — could rounding obscure important differences?**

### Code check

1. **P/D values independently recomputed:** All 20 table entries were recomputed from the exact backward-recursion algorithm (`compute_pd_ai_exact`) for AI stocks and the closed-form approximation (`compute_pd_approx`) for non-AI stocks. Every value matches the table to one decimal place. The non-linear growth in the AI premium is a genuine feature of the model: the hedging value of AI stocks increases super-linearly in p because the SDF weighting of singularity states compounds through the backward recursion over the θ chain. **Verified: correct.**

2. **Rounding:** Values are formatted with `sprintf("%.1f", ...)`. Recomputation confirms rounding does not obscure qualitative differences. For example, at p = 0.5%, ξ = 10%, the exact ratio is 14.56/10.83 = 1.344, which rounds to 1.3 — the direction is unambiguous. **Verified: correct.**

3. **Paper text claim check:** The paper states "AI stock P/D ratios are 1.3 to 2 times those of non-AI stocks across annual singularity probabilities in the 0.5–1% range." The table shows ratios from 1.3 (at p = 0.5%, ξ = 10–20%) to 2.0 (at p = 1.0%, ξ = 0%). **Verified: consistent.**

**Exhibit verdict: PASS** — All values independently verified; parameter footnote matches code; paper claims consistent with table.

## Figure 2: Government Transfers and the Singularity (Extension Panels)

**Description:** Two-panel figure. Panel (a): AI stock P/D ratio vs. tax rate τ for baseline (η = 0.5, φ = 0.5) and large-singularity (η = 9, φ = 0.05) scenarios. Panel (b): Household consumption growth in the singularity state vs. τ, with a log-scaled y-axis and a horizontal reference line at 1 ("No change"). Parameters: α = 0.70, p = 0.5%, ξ = 5%, δ = 0.5.

### Suspicious features

1. **Large-singularity P/D diverges as τ → 0 (Panel a):** The blue dashed line shoots upward and exits the plot at low τ, with an annotation "P/D → ∞ as τ → 0". This is a strong claim — is the existence condition genuinely violated?

2. **Catastrophe annotation "50% loss" at τ = 0 for large singularity (Panel b):** The large-singularity line starts at a consumption growth of 0.5 at τ = 0, implying a 50% consumption loss.

3. **Baseline annotation "25% loss" at τ = 0 (Panel b):** The baseline starts at 0.75, implying a 25% loss.

4. **Different x-axis ranges:** Panel (a) uses [0%, 40%] while Panel (b) uses [0%, 50%].

### Code check

1. **P/D divergence:** Recomputation confirms `compute_pd_with_transfer(0.005, 0.05, tau, 9.0, 0.05)` returns NA (diverges) for τ = 0, 0.01, and 0.02, and returns finite values starting at τ = 0.03 (P/D ≈ 66.4). The divergence occurs because φ_large = 0.05 and η = 9 yield an SDF singularity factor of φ^(−γ) · (1+η)^(−γ) = 160,000 · 0.0001 = 16, which makes the pricing kernel blow up at low transfer rates when the marginal-utility weight of the singularity state dominates. The annotation and plot behavior are correct. **Verified: real and correctly generated.**

2. **Consumption growth at τ = 0:** `consumption_growth(0, 9.0, 0.05)` = φ_large · (1 + η) = 0.05 · 10 = 0.5. The 50% loss annotation is correct. **Verified: correct.**

3. **Baseline at τ = 0:** `consumption_growth(0, 0.5, 0.5)` = φ · (1 + η) = 0.5 · 1.5 = 0.75. The 25% loss annotation is correct. **Verified: correct.**

4. **Different x-axis ranges:** Panel (a) uses `limits = c(0, 0.40)` and Panel (b) uses `limits = c(0, 0.50)` in the code. This is intentional — Panel (a) is capped because the baseline P/D is nearly flat beyond 40%, while Panel (b) extends further to show the consumption growth trajectory. The axis labels and tick marks in the rendered image match. **Verified: intentional and correctly rendered.**

5. **Parameter consistency:** Code uses `alpha0 = 0.70`, `p_ext = 0.005`, `xi_ext = 0.05`, `delta = 0.50`, matching the caption's stated parameters (α = 0.70, p = 0.5%, ξ = 5%, δ = 0.5). **Verified: consistent.**

**Exhibit verdict: PASS** — All suspicious features trace to correct model mechanics; annotations match computed values; parameters match caption.
