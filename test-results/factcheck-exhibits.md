# tests/factcheck-exhibits.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 3m 6s
[ralph-garage/agent-logs/20260411T101504.820581-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T101504.820581-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are consistent with their generating code and parameters; no artifacts, labeling errors, or unsupported features found.

## Figure 1: AI Valuations vs. Broader Market (fig:ai-valuations, page 2)

**Description:** Monthly closing prices for the NASDAQ Composite (solid) and S&P 500 (dashed), normalized to January 2015 = 100, plotted from ~2015 to ~2026. Shows the NASDAQ outpacing the S&P 500, with the gap widening sharply after 2023.

### Suspicious features

1. **NASDAQ reaches ~500 (5x) by late 2025.** This implies the NASDAQ roughly quintupled from Jan 2015. The NASDAQ Composite was ~4700 in Jan 2015 and reached ~19000+ in late 2024, so ~4x is plausible; values near 5x depend on exact endpoint month. This is within a reasonable range.

2. **No local data cache to verify plotted values.** The code downloads data live from FRED (NASDAQ) and datahub.io (S&P 500 Shiller dataset). The `/workspace/data/` directory is empty.

### Code check

- Code downloads NASDAQ from FRED via `download_fred("NASDAQCOM")` and S&P 500 from `datahub.io/core/s-and-p-500/r/data.csv` (lines 310-333).
- Data is filtered to 2015-01-01 through 2025-12-31, aggregated to monthly (last obs per month), aligned to common date range, and normalized so the first common month = 100 (lines 339-362).
- The normalization logic (`d$Value[which.min(d$Date)]`) correctly picks the earliest date as base.
- Caption says "NASDAQ from FRED; S&P 500 from the Shiller dataset" — matches code sources exactly.
- Caption says "normalized to January 2015 = 100" — matches code logic (first month after 2015-01-01 filter).
- Legend labels "NASDAQ Composite (AI/Tech-Heavy)" and "S&P 500" match code (lines 365-367).
- Line styles (solid NASDAQ, dashed S&P) match code `scale_linetype_manual` (lines 374-375) and caption description.

The absence of a local data cache means exact plotted values cannot be independently verified from repo contents alone. However, the code logic is straightforward (download, filter, normalize, plot) with no transformations that could introduce artifacts. The visual magnitudes are consistent with known market data for this period.

**Exhibit verdict: PASS** — code logic is correct; visual features match known market behavior; no artifacts.

## Table 1: Price-Dividend Ratios (tab:pd-ratios, page 9)

**Description:** Compares model-implied P/D ratios for AI stocks vs. non-AI stocks across singularity probabilities p (0.1%–1.0%) and extinction probabilities ξ (0%–20%). Parameters: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2.

### Suspicious features

1. **AI P/D of 26.5 at p=1.0%, ξ=0% — much higher than non-AI (13.3).** A 2:1 ratio seems large for a 1% annual probability event.

2. **Ratio column values all ≥ 1.** AI stocks always trade at a premium regardless of extinction risk.

3. **At p=0.1%, the AI premium is very small (ratio 1.1).** The singularity is rare enough that the hedging channel barely matters.

### Code check

- Non-AI P/D uses closed-form `compute_pd_approx` (lines 40-46). Spot-checked: for p=0.1%, ξ=0%, the formula yields 9.77, rounding to 9.8. For p=1.0%, ξ=0%, it yields 13.26, rounding to 13.3. Both match the table.
- AI P/D uses exact backward recursion `compute_pd_ai_exact` (lines 51-80) over 60 steps of the theta chain. This is the correct numerical approach since the AI dividend share changes after each singularity (theta updates via `thetas[k] = thetas[k-1] + dtheta*(1-thetas[k-1])`).
- Ratio column = AI/Non-AI. Verified: 10.4/9.8 = 1.06 → 1.1; 26.5/13.3 = 1.99 → 2.0. Correct after rounding.
- The AI premium increases with p because higher singularity probability amplifies the hedging value of AI stocks. This is the paper's central mechanism.
- Higher ξ reduces both P/D ratios (extinction destroys value) and compresses the AI premium (extinction eliminates the hedging benefit). Pattern is monotonic and economically coherent.
- Table footnote parameters (β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2) match code variables exactly (lines 18-24).
- The generated `.tex` file matches the rendered table values exactly.

**Exhibit verdict: PASS** — numerical values verified against formulas; patterns are economically coherent; parameters match between code and caption.

## Figure 2: Government Transfers and the Singularity (fig:extension-panels, page 14)

**Description:** Two panels. Panel (a): AI stock P/D ratio vs. tax rate τ for baseline (η=0.5, φ=0.5) and large singularity (η=9, φ=0.05) scenarios. Panel (b): Household consumption growth in singularity vs. tax rate τ, log scale, with a dotted line at 1 (no change).

### Suspicious features

1. **Panel (a): Large singularity line starts off-chart with annotation "P/D → ∞ as τ → 0".** The P/D appears to diverge as the tax rate approaches zero for the large singularity case.

2. **Panel (b): Large singularity consumption growth = 0.5 at τ=0 labeled "Catastrophe: 50% loss".** Need to verify this is computed correctly.

3. **Panel (b): Baseline consumption growth at τ=0 labeled "25% loss".** Need to verify.

4. **Panel (a): x-axis limited to 0–40% while Panel (b) extends to ~70%.** Different axis ranges across panels.

### Code check

1. **P/D → ∞ for large singularity at τ=0:** With φ_large=0.05, η=9, the SDF singularity term S = 0.05^(−4) × 10^(−4) = 16. The AI dividend growth at terminal theta ≈ 10. So K_term = B × (0.995 + 0.005 × 0.95 × 16 × 10) ≈ 0.905 × 1.755 = 1.59 > 1, which means `compute_pd_with_transfer` correctly returns NA (line 169). As τ increases, φ_eff rises, S falls, and eventually K_term < 1, making P/D finite. The annotation is accurate.

2. **Consumption at τ=0, large singularity:** `consumption_growth(0, 9, 0.05) = 0.05 × 10 + 0 = 0.5`. A growth factor of 0.5 means consumption drops by 50%. The "50% loss" annotation is correct (code line 261: `round((1-cons_large_0)*100)` = `round(50)` = 50).

3. **Consumption at τ=0, baseline:** `consumption_growth(0, 0.5, 0.5) = 0.5 × 1.5 + 0 = 0.75`. Growth factor 0.75 → 25% loss. The annotation is correct (code line 265: `round((1-cons_base_0)*100)` = `round(25)` = 25).

4. **Different x-axis ranges:** Panel (a) uses `limits = c(0, 0.40)` (line 238) because P/D values stabilize and the interesting dynamics are in the 0–40% range. Panel (b) uses the full `tau_grid` range of 0–0.70 (line 138) to show the full consumption growth curve including the quadratic deadweight cost drag. This is an intentional design choice, not an error.

- Caption parameters "α = 0.70, p = 0.5%, ξ = 5%, δ = 0.5" match code variables: `alpha0=0.70`, `p_ext=0.005`, `xi_ext=0.05`, `delta=0.50` (lines 140-141, 183-184).
- Scenario labels in legend match code: "Baseline (η = 0.5, φ = 0.5)" and "Large singularity (η = 9, φ = 0.05)" (lines 211-214).
- The `phi_large` comment on line 25 states "phi_large*(1+9)=0.5" confirming the intended household consumption at τ=0.

**Exhibit verdict: PASS** — all suspicious features verified as correctly generated; parameter values match between code and caption; economic logic is coherent.
