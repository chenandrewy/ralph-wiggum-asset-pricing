# tests/factcheck-exhibits.py
Started: 2026-04-09 21:34:52 EDT
Runtime: 3m 52s
[ralph-garage/agent-logs/20260409T213452.262723-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T213452.262723-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and consistent with the paper's formulas and stated parameters.

## Figure 1 (fig:ai-valuations)

**Description:** Monthly closing prices for the NASDAQ Composite (solid blue) and S&P 500 (dashed red) from ~2015 to ~2025, normalized to January 2015 = 100. The NASDAQ rises to roughly 400–500 while the S&P 500 reaches roughly 250–300, with the gap widening sharply around 2023.

### Suspicious features

1. **Sharp widening of the NASDAQ–S&P gap post-2023.** The NASDAQ line pulls away dramatically after ~2023, which could suggest a data anomaly or fabrication.
2. **COVID dip (~2020) and 2022 drawdown.** Both series show a sharp dip around early 2020 and a notable decline in 2022, which could be artifacts.
3. **No local data cache.** The code downloads data live from FRED (NASDAQCOM) and datahub (Shiller S&P 500 dataset), with no local cached copy to verify exact values against.

### Code check

1. The post-2023 divergence is consistent with the real-world AI boom in public equities. The NASDAQ Composite is tech/AI-heavy, and this pattern matches publicly known market behavior. The code downloads real market data, normalizes both series to 100 at the earliest common month, and plots them. No fabrication or manipulation is present in the code path (`generate-exhibits.R:254–327`).
2. The COVID dip and 2022 drawdown are real market events. The code applies no smoothing or filtering that would create artificial dips.
3. Although no local data cache exists, the code logic is transparent: download, convert to monthly (last observation per month), align date ranges, normalize, and plot. The normalization function (`normalize`, line 299) correctly uses `which.min(d$Date)` to find the earliest date's value as the base. The alignment logic (`min_date`/`max_date`, lines 293–296) ensures both series share the same date range.

**Exhibit verdict: PASS** — Code logic is correct; visible features are consistent with real market data. The absence of a local cache is a limitation but not a factual error.

## Table 1 (tab:pd-ratios)

**Description:** Price-dividend ratios for AI stocks and non-AI stocks across a grid of singularity probabilities (p = 0.1%–1.0%) and extinction probabilities (ξ = 0%–20%), with parameters β = 0.96, g = 0.02, γ = 4, φ = 0.5, η = 0.5, θ = 0.15, Δθ = 0.2.

### Suspicious features

1. **Extreme AI P/D at high p.** At p = 1.0%, ξ = 0%, the AI P/D ratio is 76.4 — dramatically higher than surrounding values. The jump from p = 0.8% (33.0) to p = 1.0% (76.4) is more than a doubling.
2. **Non-AI P/D barely moves.** Non-AI stocks range only from 9.7 to 13.3 across the entire grid while AI stocks span 10.2 to 76.4.

### Code check

1. The extreme AI P/D at high p is a correct consequence of the pricing formula K/(1−K). As K approaches 1, the denominator vanishes and P/D explodes. Independently recomputing: at p = 1%, ξ = 0%, K_AI = 0.9871, giving P/D = 0.9871/0.0129 = 76.4. ✓ At p = 0.8%, K = 0.9706, P/D = 33.0. ✓ The nonlinear explosion is a real model feature (the existence condition in Remark 1).
2. Non-AI stocks have a much smaller singularity dividend growth factor (Γ^N = 1.2 vs Γ^AI = 3.2), so their K stays well below 1 and their P/D responds modestly to p. Independently verified: p = 0.1%/ξ = 0%: AI = 10.5, Non = 9.8, Ratio = 1.1 ✓; p = 0.5%/ξ = 0%: AI = 17.5, Non = 11.1, Ratio = 1.6 ✓; p = 1.0%/ξ = 0%: AI = 76.4, Non = 13.3, Ratio = 5.8 ✓. All match the rendered table.

**Exhibit verdict: PASS** — All spot-checked values match independent recomputation. The code (`generate-exhibits.R:42–96`) correctly implements the paper's Proposition 1 formula.

## Figure 2 (fig:extension-panels)

**Description:** Two panels showing the effect of government transfers (tax rate τ) under baseline (η = 0.5, φ = 0.5) and large singularity (η = 9, φ = 0.05) scenarios. Panel (a): AI stock P/D ratio vs τ (0%–40%). Panel (b): Household consumption growth in the singularity state vs τ (0%–70%), with a log-scale y-axis.

### Suspicious features

1. **Large singularity line enters Panel (a) from the top** with an annotation "P/D → ∞ as τ → 0." This is a dramatic visual feature — the line appears to start mid-chart rather than from the y-axis.
2. **Catastrophe annotations at τ = 0.** Panel (b) marks "Catastrophe: 50% loss" for the large singularity and "25% loss" for the baseline, both at τ = 0.
3. **Log-scale y-axis in Panel (b).** The large singularity line rises steeply from ~0.5 to ~5, while the baseline rises modestly from ~0.75 to ~1.5.
4. **Caption states δ = 0.5, α = 0.70, p = 0.5%, ξ = 5%.** Need to verify these match the code.

### Code check

1. At τ = 0 with large singularity parameters, K = β(1+g)^(1−γ) × [0.995 + 0.005 × 0.95 × φ^(−γ)(1+η)^(−γ)Γ^AI] = 0.9046 × [0.995 + 0.005 × 0.95 × 0.05^(−4) × 10^(−4) × 21.33] = 0.9046 × 2.617 = 2.367. Since K > 1, P/D is undefined (NA). The code correctly returns NA for K ≥ 1 (`generate-exhibits.R:123`), and the plot filters NAs (`generate-exhibits.R:169`). As τ increases, φ_eff rises, reducing K below 1, at which point the line enters the chart. The annotation is correct. ✓
2. At τ = 0: baseline consumption growth = φ(1+η) = 0.5 × 1.5 = 0.75, i.e., 25% loss. ✓ Large singularity = 0.05 × 10 = 0.5, i.e., 50% loss. ✓ Both match the code's `consumption_growth` function (`generate-exhibits.R:113–114`).
3. The steep rise of the large singularity line is correct: the transfer base (1 − φα)/α = (1 − 0.035)/0.70 = 1.379 is large, and this is multiplied by (1+η) = 10, producing rapid gains in consumption as τ increases. The log scale appropriately handles the range from 0.5 to ~5.
4. Code parameters: `alpha0 = 0.70` ✓, `p_ext = 0.005` ✓, `xi_ext = 0.05` ✓, `delta = 0.50` ✓. The `phi_eff` computation (`generate-exhibits.R:119`) matches the paper's equation (8). The `consumption_growth` function (`generate-exhibits.R:113–114`) matches the paper's equation (7) divided by pre-singularity consumption.

**Exhibit verdict: PASS** — All features are correctly generated. The P/D divergence at τ → 0, the catastrophe annotations, and the consumption growth curves are all consistent with the model equations and stated parameters.
