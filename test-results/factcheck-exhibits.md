# tests/factcheck-exhibits.py
Started: 2026-04-14 10:33:09 EDT
Runtime: 4m 31s
[ralph-garage/agent-logs/20260414T103309.997798-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260414T103309.997798-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated and consistent with their code, data sources, and captions.

## Figure 1: Valuation Ratios and the AI Premium

Panel (a) shows the S&P 500 trailing price-dividend ratio (2000–2024) from the Shiller dataset. Panel (b) shows the NASDAQ/S&P 500 price ratio normalized to January 2015 = 100.

### Suspicious features

1. **No local data cache.** The code downloads data at runtime from datahub.io (Shiller) and FRED (NASDAQ series NASDAQCOM). The `/workspace/data/` directory is empty, so the exact plotted values cannot be independently re-verified from local files.

2. **P/D ratio reaching ~80 in recent years.** This is a high level for the S&P 500 P/D ratio.

3. **NASDAQ/S&P ratio pattern.** The ratio starts at ~180 in 2000, drops to ~60–80, then rises after 2015 to ~130–140.

### Code check

1. **Data source.** The code (lines 318–319, 348) downloads from well-known authoritative sources. The transformations are straightforward: `PD = SP500 / Dividend` (line 326) and `Ratio = NASDAQ / SP500` normalized to Jan 2015 = 100 (lines 399–400). While exact values cannot be re-verified without re-downloading, the code path is transparent and the patterns match well-documented market history.

2. **High P/D ratio.** An S&P 500 P/D ratio of ~80 corresponds to a dividend yield of ~1.25%, which is consistent with recent market data (dividend yields have been historically low). Not an error.

3. **NASDAQ/S&P pattern.** The decline from 2000 reflects the dot-com bust; the rise after 2015 reflects AI/tech outperformance. The normalization code at line 399 is correct. Consistent with known market history.

4. **Caption accuracy.** Caption states data from Shiller dataset and FRED, normalized to Jan 2015 = 100. Matches code exactly. Date range filtered to 2000+ at line 384.

**Exhibit verdict: PASS** — Code logic is transparent, patterns match known market history, captions are accurate.

## Table 1: Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks

The table shows model-implied P/D ratios for AI and non-AI stocks across singularity probabilities (p = 0.1%–1.0%) and extinction probabilities (ξ = 0%–20%).

### Suspicious features

1. **AI P/D increases monotonically with p.** Higher singularity probability raises AI stock valuations from 10.4 (p = 0.1%) to 26.5 (p = 1.0%).

2. **Non-AI P/D also increases with p**, but less dramatically (9.8 to 13.3).

3. **Ratio reaches 2.0 at p = 1.0%, ξ = 0%.** This is a large valuation premium.

### Code check

1. **Spot-check: Non-AI P/D at p = 0.1%, ξ = 0%.** Manual computation: `share_ratio_non = 0.8`, `gamma_non = 1.2`, `sdf_sing = 16 × 0.1975 × 1.2 ≈ 3.79`, `base = 0.96 × 1.02^(-3) ≈ 0.9046`, `K = 0.9046 × 1.00279 ≈ 0.9071`, `P/D ≈ 9.77`. Code output: 9.77, displayed as 9.8 after rounding. Correct.

2. **Non-AI formula is exact, not approximate.** `share_ratio_non = 1 - dtheta = 0.8` is theta-independent, so the "approximate" closed-form at line 40–46 is actually exact for non-AI stocks. No error from using the approximate formula.

3. **AI P/D uses exact backward recursion** (lines 51–79, n_steps = 60). The theta chain converges as `theta_k → 1`, making the terminal approximation accurate. The recursion properly accounts for the changing AI dividend share after successive singularities.

4. **Monotonicity patterns.** AI P/D rising with p reflects the AI singularity premium (dividends jump favorably). Non-AI P/D rising with p reflects the aggregate consumption jump (eta = 0.5) partially offsetting the share dilution. The ratio rising with p and falling with ξ is economically sensible.

5. **Caption parameters.** Footnote states β = 0.96, g = 0.02, γ = 4, φ = 0.5, η = 0.5, θ = 0.15, Δθ = 0.2. All match the code (lines 18–24).

**Exhibit verdict: PASS** — Spot-checked numerical values match, monotonicity patterns are economically correct, parameters in footnote match code.

## Figure 2: Government Transfers and the Singularity

Panel (a) shows AI stock P/D ratio vs. tax rate τ for two scenarios: baseline (η = 0.5, φ = 0.5) and large singularity (η = 9, φ = 0.05). Panel (b) shows the household consumption multiple in the singularity state vs. tax rate, on a log scale.

### Suspicious features

1. **Large singularity P/D diverges as τ → 0.** The line enters the plot from the top at some τ > 0 with an annotation "P/D → ∞ as τ → 0".

2. **Catastrophe annotation "50% loss" at τ = 0** for the large singularity scenario.

3. **"25% loss" annotation at τ = 0** for the baseline scenario.

4. **Numeric annotations "1.1×" and "1.3×"** on the baseline trajectory in Panel (b).

5. **P/D axis clipped to [7, cap].** The large singularity line is partially outside the y-axis range.

### Code check

1. **P/D divergence.** At τ = 0, φ_eff = φ_large = 0.05. Computed `K_term = 0.05^(-4) × 10^(-4) × ... = 1.588 > 1`, so the function returns NA. At τ = 0.10, K_term = 0.904 < 1, yielding P/D ≈ 9.9. Confirmed: the P/D is undefined at τ = 0 and becomes finite for τ > ~0.05. The annotation is correct.

2. **50% loss.** `cons_large_0 = 0.05 × (1 + 9) = 0.5`. Loss = 1 − 0.5 = 50%. Correct.

3. **25% loss.** `cons_base_0 = 0.5 × (1 + 0.5) = 0.75`. Loss = 1 − 0.75 = 25%. Correct.

4. **Numeric annotations.** `consumption_growth(0.30, 0.5, 0.5) = 1.105`, displayed as "1.1×". `consumption_growth(0.47, 0.5, 0.5) = 1.251`, displayed as "1.3×". Both verified by direct computation. Correct.

5. **Y-axis clipping.** Panel A uses `y_min_a = 7` and `y_cap_a = ceiling(baseline_max)`. The large singularity line is clipped at high values, which is appropriate given the divergence. The annotation explains the off-chart behavior.

6. **Caption parameters.** Caption states α = 0.70, p = 0.5%, ξ = 5%, δ = 0.5. Code uses `alpha0 = 0.70`, `p_ext = 0.005`, `xi_ext = 0.05`, `delta = 0.50`. All match.

7. **Legend labels.** "Baseline (η = 0.5, φ = 0.5)" and "Large singularity (η = 9, φ = 0.05)" match the code parameters at lines 186–193.

**Exhibit verdict: PASS** — All suspicious features verified against code. Divergence is theoretically expected and correctly annotated, consumption loss calculations are arithmetically correct, caption parameters match code.
