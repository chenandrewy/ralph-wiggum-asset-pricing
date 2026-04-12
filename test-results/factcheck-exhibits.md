# tests/factcheck-exhibits.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 2m 32s
[ralph-garage/agent-logs/20260412T093252.135772-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T093252.135772-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from their code and parameters, with no artifacts, labeling errors, or unsupported features.

## Figure 1: Valuation Ratios and the AI Premium (fig:ai-valuations)

**Description:** Two-panel time-series figure. Panel (a) shows S&P 500 trailing price-dividend ratio from the Shiller dataset (2000--present). Panel (b) shows NASDAQ Composite price relative to S&P 500, normalized to January 2015 = 100.

### Suspicious features

1. **P/D ratio reaching ~80 at the right edge.** A trailing P/D of ~80 is unusually high historically, which could suggest a data error.
2. **NASDAQ/S&P ratio starting high (~130), dropping, then rising sharply.** Could indicate a normalization artifact.

### Code check

1. **P/D ~80:** The code computes `PD = SP500 / Dividend` using the Shiller dataset's trailing 12-month dividends (line 309). With the S&P 500 near ~5000 and trailing dividends around $60 in recent years, a P/D of ~80 is plausible. The Shiller dataset is a standard academic source. **Verified as real.**

2. **NASDAQ/S&P ratio shape:** The code normalizes to the value closest to 2015-01-01 (line 382: `base_ratio <- df_pd$Ratio[which.min(abs(df_pd$Date - as.Date("2015-01-01")))]`). The high starting value reflects the dot-com era tech premium; the subsequent decline and recovery reflect known market history. The y-axis label correctly states "(Jan 2015 = 100)". **Verified as real.**

**Exhibit verdict: PASS** — Data sourced from Shiller dataset (datahub) and FRED NASDAQCOM series; transformations are straightforward and correctly labeled.

## Table 1: Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks (tab:pd-ratios)

**Description:** Grid of P/D ratios for AI and non-AI stocks across singularity probability p (0.1%--1.0%) and extinction probability xi (0%--20%), with their ratio. Parameters: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, Delta_theta=0.2.

### Suspicious features

1. **AI P/D jumps from 15.5 to 26.5 between p=0.5% and p=1.0% (xi=0), while non-AI only goes from 11.1 to 13.3.** The non-linear acceleration in AI P/D could indicate a coding error.
2. **Ratio column shows only one decimal place and values cluster at 1.1 for low p.** Could mask meaningful variation.

### Code check

1. **Non-linear AI P/D growth:** The AI P/D is computed via exact backward recursion over the chain of post-singularity theta values (function `compute_pd_ai_exact`, lines 51--80). As p increases, the SDF-weighted singularity payoff (which includes AI share growth Gamma^AI = 2.13x at the first step) becomes more dominant. The recursion amplifies this because each singularity further increases theta, making subsequent Gamma^AI smaller but cumulative effects larger. Non-AI stocks use the simpler closed-form `compute_pd_approx` (lines 40--46) with Gamma^N = 0.80*1.5 = 1.2, which is below 1 in SDF terms, so non-AI P/D grows more slowly. Spot-checked four cells by independent recomputation:
   - p=0.001, xi=0: AI=10.4, Non-AI=9.8 (matches)
   - p=0.005, xi=0: AI=15.5, Non-AI=11.1 (matches)
   - p=0.01, xi=0.05: AI=24.8, Non-AI=12.9 (matches)
   - p=0.01, xi=0.20: AI=20.5, Non-AI=12.0 (matches)
   **Verified as correct.**

2. **Ratio rounding:** The ratio column is computed as pd_ai/pd_non and formatted to one decimal place (line 98: `sprintf("%.1f", x)`). At low p, both P/D ratios are close (e.g., 10.4/9.8=1.06, rounds to 1.1), so the clustering is a rounding artifact, not a data error. The footnote correctly describes the ratio. **Verified as correct.**

**Exhibit verdict: PASS** — All values independently verified; parameters in the footnote match the code; formatting is consistent.

## Figure 2: Government Transfers and the Singularity (fig:extension-panels)

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate tau for baseline (eta=0.5, phi=0.5) and large singularity (eta=9, phi=0.05) scenarios. Panel (b) shows household consumption growth in the singularity state vs. tau, with a log y-axis and a horizontal "no change" reference line at 1.

### Suspicious features

1. **Large-singularity P/D line appears to start from outside the plot at the left, entering from above.** The annotation says "P/D -> infinity as tau -> 0". This could be an error if the existence condition is not actually violated.
2. **Consumption growth for "Large singularity" at tau=0 is labeled as "Catastrophe: 50% loss".** Need to verify the formula yields exactly 0.5.
3. **Baseline consumption growth at tau=0 labeled "25% loss".** Same verification needed.
4. **Panel (b) y-axis is log-scaled.** Could distort visual interpretation.

### Code check

1. **P/D divergence at tau=0 for large singularity:** At tau=0, phi_eff = phi_large = 0.05. Then phi_eff^(-gamma) = 0.05^(-4) = 160,000. The SDF term S = 160,000 * (1+9)^(-4) = 160,000 * 0.0001 = 16. The first-step AI dividend growth Gamma^AI = (0.15 + 0.20*0.85)/0.15 * 10 = 21.33. The pricing kernel A = B*((1-p) + p*(1-xi)*S*Gamma^AI) = 0.905*(0.995 + 0.005*0.95*16*21.33) = 0.905*(0.995 + 1.622) = 2.37 >> 1. Since A > 1, the pricing sum diverges and P/D is infinite. The backward recursion returns NA for these parameter values (lines 168--169). The code correctly clips the x-axis to tau <= 0.40 and caps the y-axis (lines 224--228). **Verified as correct.**

2. **Consumption at tau=0, large singularity:** The formula is `phi_val*(1+eta_val)` = 0.05 * 10 = 0.50. Loss = 1 - 0.50 = 50%. The annotation `round((1 - cons_large_0) * 100)` yields 50. **Verified as correct.**

3. **Consumption at tau=0, baseline:** `phi*(1+eta)` = 0.50 * 1.50 = 0.75. Loss = 25%. The annotation computes `round((1 - cons_base_0) * 100)` = 25. **Verified as correct.**

4. **Log y-axis:** The code uses `scale_y_log10` (line 272) with breaks at 0.1, 0.25, 0.5, 1, 2, 5. This is appropriate because the two scenarios span very different magnitudes (0.5 to >5). Not an artifact. **Verified as correct.**

**Caption parameter check:** Caption states "alpha=0.70, p=0.5%, xi=5%, delta=0.5". Code: alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50. All match.

**Exhibit verdict: PASS** — Divergence at tau=0 is mathematically verified; consumption loss annotations match exact formula outputs; parameters match caption.
