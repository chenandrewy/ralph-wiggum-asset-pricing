# tests/factcheck-exhibits.py
Started: 2026-04-12 09:46:31 EDT
Runtime: 7m 21s
[ralph-garage/agent-logs/20260412T094631.065270-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T094631.065270-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated, with numerical values matching the code, parameters matching the paper text, and no artifacts or unsupported features found.

## Figure 1: Valuation Ratios and the AI Premium (fig:ai-valuations, page 2)

**Description:** Two-panel figure. Panel (a) shows the S&P 500 trailing price-to-dividend ratio from ~2000 to present using the Shiller dataset. Panel (b) shows the NASDAQ Composite price relative to the S&P 500, normalized to January 2015 = 100, using FRED data.

### Suspicious features

1. **Panel (a) P/D spike circa 2008–2009:** The trailing P/D ratio appears to spike during the financial crisis period. This would be unusual if driven by rising prices, but trailing P/D can spike when dividends are cut faster than prices recover. This is a known feature of trailing-dividend-based P/D ratios during dividend-cut episodes and is consistent with the Shiller dataset behavior.

2. **Panel (b) normalization choice:** The NASDAQ/S&P ratio is normalized to Jan 2015 = 100. The code normalizes to the closest available date to 2015-01-01 via `which.min(abs(df_pd$Date - as.Date("2015-01-01")))`. This is standard.

### Code check

- **Data sources:** Panel (a) uses `datahub.io/core/s-and-p-500/r/data.csv` (Shiller dataset); Panel (b) uses FRED series `NASDAQCOM`. Caption correctly identifies "Sources: NASDAQ from FRED; S&P 500 from the Shiller dataset." Match confirmed.
- **P/D computation:** `PD = SP500 / Dividend` where `Dividend` is the Shiller trailing 12-month dividend. Caption says "trailing price-dividend ratio." Match confirmed.
- **Normalization:** Code divides by the ratio value nearest Jan 2015 and multiplies by 100. Y-axis label says "Jan 2015 = 100." Match confirmed.
- **Date range:** Code filters `Date >= as.Date("2000-01-01")`. The x-axis in the rendered image starts around 2000–2003 (constrained by the NASDAQ/S&P inner join). Consistent.
- **In-text claim (line 189):** "the AI-heavy NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015." Panel (b) shows the ratio reaching ~150 by recent dates, consistent with ~50% outperformance.

**Exhibit verdict: PASS** — Data sources, computations, labels, and captions all match. The P/D spike is a real feature of trailing-dividend ratios during dividend-cut episodes.

## Table 1: Price-Dividend Ratios: AI vs. Non-AI Stocks (tab:pd-ratios, page 9)

**Description:** Grid of price-dividend ratios for AI stocks, non-AI stocks, and their ratio, across singularity probabilities p ∈ {0.1%, 0.2%, 0.5%, 0.8%, 1.0%} and extinction probabilities ξ ∈ {0%, 5%, 10%, 20%}. Parameters: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2.

### Suspicious features

1. **Large AI P/D at high p:** At p=1.0%, ξ=0%, the AI P/D reaches 26.5, more than double the non-AI value (13.3). This is a striking but not implausible magnitude, driven by the large SDF-weighted dividend growth factor for AI stocks.

2. **Ratio monotonicity:** The AI/non-AI ratio increases with p and decreases with ξ. This could be an artifact if the formulas were incorrectly specified, so it requires verification.

### Code check

- **Parameters match footnote:** Code defines β=0.96, g=0.02, γ=4, φ=0.50, η=0.50, θ=0.15, Δθ=0.20. Table footnote lists identical values. Match confirmed.
- **AI P/D computation:** Uses `compute_pd_ai_exact` with backward recursion over 60 theta-chain steps. Footnote says "AI P/D ratios are numerically exact, computed by iterating the Euler equation over post-singularity states." Match confirmed.
- **Non-AI P/D computation:** Uses `compute_pd_approx` with `gamma_non = 0.8 * 1.5 = 1.2`. The approximate formula is actually exact for non-AI stocks because Γ^N = (1−Δθ)(1+η) is theta-independent (code comment confirms: "Gamma^N is theta-independent"). Correct.
- **Spot-check values (verified via R execution):**
  - p=0.5%, ξ=0%: AI=15.5, Non-AI=11.1, Ratio=1.4. Paper text (line 187) says "AI stocks trade at a P/D of about 15.5, while non-AI stocks trade near 11—a ratio of about 1.4." Exact match.
  - p=1.0%, ξ=0%: AI=26.5, Non-AI=13.3, Ratio=2.0. Paper text says "At p=1%, the ratio rises to 2." Exact match.
  - p=0.5%, ξ=20%: AI=13.8, Non-AI=10.6, Ratio=1.3. Consistent with stated range "1.3 to 2 times."
- **Monotonicity:** Ratio increases with p (higher singularity probability → more hedging value) and decreases with ξ (higher extinction → fewer payoff states). Both patterns are economically correct and match Proposition comparative statics cited in the text.

**Exhibit verdict: PASS** — All spot-checked values match exactly. Parameters in code, footnote, and body text are consistent. Comparative statics patterns are correct.

## Figure 2: Government Transfers and the Singularity (fig:extension-panels, page 15)

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate τ for two scenarios: baseline (η=0.5, φ=0.5) and large singularity (η=9, φ=0.05). Panel (b) shows household consumption growth in the singularity state vs. tax rate, with a log-scaled y-axis. Parameters: α=0.70, p=0.5%, ξ=5%, δ=0.5.

### Suspicious features

1. **Panel (a): Large-singularity P/D divergence at τ→0.** The blue dashed line enters the plot from above with an annotation "P/D → ∞ as τ → 0." This is a dramatic claim.

2. **Panel (b): Catastrophe annotations.** The "50% loss" and "25% loss" labels at τ=0 are specific numerical claims. The "1.1×" and "1.3×" annotations at τ=30% and τ=50% for the baseline are also specific.

3. **Panel (a): Y-axis capping.** The y-axis appears capped, clipping the large-singularity line at high P/D values.

### Code check

- **Parameters match caption:** Code: `alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50`. Caption: "α=0.70, p=0.5%, ξ=5%, δ=0.5." Match confirmed.
- **Scenario parameters match text (line 263):** Baseline uses η=0.5, φ=0.5; large singularity uses η=9, φ=0.05. Code: `eta_val = ifelse(grepl("Baseline",...), 0.5, 9.0)`, `phi_val = ifelse(grepl("Baseline",...), phi, phi_large)`. Match confirmed.
- **P/D divergence (verified via R execution):** At τ=0 for large singularity, `compute_pd_with_transfer` returns NA because φ_eff=0.05, giving φ^{-γ}=160,000, which makes K>1 and the pricing sum diverges. The paper text (line 265) explains: "the existence condition in Remark 1 is violated because the household's marginal utility in the singularity state (φ^{-γ}=160,000) is so extreme that the pricing sum diverges." Code and text agree. Correct.
- **Catastrophe annotations (verified via R execution):**
  - Baseline τ=0: consumption_growth = 0.75, i.e., 25% loss. Annotation says "25% loss." Exact match.
  - Large singularity τ=0: consumption_growth = 0.50, i.e., 50% loss. Annotation says "50% loss." Exact match.
  - Paper text (line 263): "consumption halves under the large singularity (φ(1+η)=0.5) and falls by 25% under the baseline (φ(1+η)=0.75)." Both confirmed: 0.05×10=0.5, 0.5×1.5=0.75.
- **Trajectory annotations (verified via R execution):**
  - Baseline τ=30%: consumption_growth = 1.1052, rounds to 1.1. Annotation says "1.1×." Match.
  - Baseline τ=50%: consumption_growth = 1.2723, rounds to 1.3. Annotation says "1.3×." Match.
- **Y-axis capping:** Code sets `y_cap_a <- ceiling(baseline_max_a)` and `y_min_a <- 7`, with `scale_y_continuous(limits = c(y_min_a, y_cap_a))`. The large-singularity line at small τ exceeds this cap and is clipped, with the annotation explaining the divergence. This is intentional and correctly documented.
- **Large singularity P/D at finite τ (verified via R execution):** At τ=5%, PD=16.1; at τ=10%, PD=9.9. These are consistent with the plotted curve entering from above and declining steeply.

**Exhibit verdict: PASS** — All numerical annotations verified exactly. Divergence behavior is real, correctly generated, and properly explained in both the annotation and paper text. Parameters are consistent across code, caption, and body text.
