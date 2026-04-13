# tests/factcheck-exhibits.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 4m 53s
[ralph-garage/agent-logs/20260412T202602.583129-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T202602.583129-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from code and data, with no artifacts, labeling errors, or unsupported features.

## Figure 1: Valuation Ratios and the AI Premium (fig:ai-valuations, page 2)

**Description.** Two-panel figure. Panel (a) plots the S&P 500 trailing price-dividend ratio from the Shiller dataset (2000--2025). Panel (b) plots the NASDAQ Composite price relative to the S&P 500, normalized to January 2015 = 100, using FRED data.

### Suspicious features

1. **P/D spike around 2008--2009.** The trailing P/D ratio may exhibit a transient spike during the financial crisis if prices fell slower than trailing dividends adjusted.
2. **Sharp NASDAQ/S&P ratio rise post-2020.** The ratio climbs steeply from ~2020, reaching roughly 130--140 by the end of the sample.

### Code check

1. **P/D spike around 2008--2009.** The code computes `PD = SP500 / Dividend` from the Shiller dataset, where `Dividend` is trailing 12-month dividends. During recessions, dividends lag price movements, which can produce transient P/D fluctuations. This is a real feature of the standard Shiller data, not a coding artifact. The code applies no smoothing or special handling, which is appropriate.

2. **Sharp NASDAQ/S&P ratio rise post-2020.** The code downloads NASDAQ from FRED (`NASDAQCOM`) and S&P 500 from the Shiller dataset, computes the monthly price ratio, and normalizes to the observation closest to 2015-01-01. The sharp rise reflects actual market data (AI/tech outperformance). The normalization logic (`base_ratio <- df_pd$Ratio[which.min(abs(df_pd$Date - as.Date("2015-01-01")))]`) is correct.

**Exhibit verdict: PASS.** Both panels are generated from standard public data sources with straightforward transformations. No artifacts or errors found.

---

## Table 1: Price-Dividend Ratios — AI Stocks vs. Non-AI Stocks (tab:pd-ratios, page 9)

**Description.** Grid of model-implied P/D ratios for AI and non-AI stocks across singularity probabilities p = {0.1%, 0.2%, 0.5%, 0.8%, 1.0%} and extinction probabilities xi = {0%, 5%, 10%, 20%}. Parameters: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, dtheta=0.2.

### Suspicious features

1. **AI P/D ratios grow rapidly with p.** At p=1%, xi=0%, AI P/D reaches 26.5 vs. 13.3 for non-AI (ratio 2.0). The nonlinear sensitivity to p could indicate a coding error.
2. **Non-AI ratios use an approximate formula while AI ratios use exact backward recursion.** This asymmetry could introduce inconsistency.

### Code check

1. **AI P/D growth with p.** Verified by independent computation. The exact backward recursion in `compute_pd_ai_exact` iterates over a chain of 60 post-singularity theta values. Spot-checked values: p=0.5%/xi=0% gives AI=15.5, Non-AI=11.1, Ratio=1.4; p=1.0%/xi=0% gives AI=26.5, Non-AI=13.3, Ratio=2.0. These match the rendered table and the paper text (Section 3: "AI stocks trade at a P/D of about 15.5, while non-AI stocks trade near 11" and "At p=1%, the ratio rises to 2"). The nonlinearity is real: higher p puts more weight on singularity states where AI stocks' hedging value operates through the SDF term phi^(-gamma) * (1+eta)^(-gamma) * Gamma^AI.

2. **Approximate vs. exact formulas.** The approximate formula for non-AI stocks is in fact exact. The non-AI dividend growth factor Gamma^N = (1-dtheta)*(1+eta) = 0.8*1.5 = 1.2 is independent of the current theta (since (1-theta-dtheta*(1-theta))/(1-theta) = 1-dtheta for all theta). Therefore the post-singularity P/D ratio equals the pre-singularity ratio, and the closed-form is exact. No inconsistency.

3. **Parameter footnote.** The LaTeX footnote in `table-pd-ratios.tex` lists beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, dtheta=0.2, matching the code parameters on lines 18--24.

**Exhibit verdict: PASS.** All values independently verified; formulas are correct; parameters match the paper text and table footnote.

---

## Figure 2: Government Transfers and the Singularity (fig:extension-panels, page 15)

**Description.** Two-panel figure. Panel (a) plots AI stock P/D ratio vs. tax rate tau for baseline (eta=0.5, phi=0.5) and large-singularity (eta=9, phi=0.05) scenarios. Panel (b) plots household consumption growth in the singularity state vs. tau on a log scale, with a horizontal line at 1.0 ("No change"). Parameters: p=0.5%, xi=5%, alpha=0.70, delta=0.50.

### Suspicious features

1. **Large-singularity P/D divergence at low tau.** Panel (a) shows the large-singularity line entering from the top at a low tau value, with an annotation "P/D -> infinity as tau -> 0." This could be an artifact if the divergence is not genuine.
2. **Catastrophe annotation: "50% loss" at tau=0 for large singularity.** Need to verify this matches the model.
3. **Baseline annotation: "25% loss" at tau=0.** Need to verify.
4. **Baseline trajectory annotations "1.1x" at tau=0.30 and "1.3x" at tau=0.50.** Need to verify these numeric labels match the consumption growth function.
5. **Different x-axis ranges between panels.** Panel (a) extends to 40%, Panel (b) to 50%.

### Code check

1. **P/D divergence at tau=0.** Verified analytically: at tau=0, phi_eff=0.05, so phi_eff^(-gamma) = 0.05^(-4) = 160,000. The SDF term S = 160,000 * 10^(-4) = 16. The terminal K_term = B*((1-p) + p*(1-xi)*S*Gamma_term) = 0.905*(0.995 + 0.005*0.95*16*10) = 0.905*1.755 = 1.59. Since K_term >= 1, the code correctly returns NA (infinite P/D). As tau increases past ~3%, phi_eff grows enough to restore K_term < 1 and finite prices emerge. The divergence is a genuine model feature, not an artifact.

2. **"50% loss" at tau=0 for large singularity.** consumption_growth(0, 9, 0.05) = 0.05 * (1+9) = 0.50. Loss = 1 - 0.50 = 50%. Correct.

3. **"25% loss" at tau=0 for baseline.** consumption_growth(0, 0.5, 0.5) = 0.5 * 1.5 = 0.75. Loss = 1 - 0.75 = 25%. Correct.

4. **Baseline annotations.** consumption_growth(0.30, 0.5, 0.5) = 1.1 (rounds to 1.1x). consumption_growth(0.50, 0.5, 0.5) = 1.3 (rounds to 1.3x). Both verified by independent computation. Correct.

5. **Different x-axis ranges.** Panel (a) uses `limits = c(0, 0.40)` and Panel (b) uses `limits = c(0, 0.50)`. This is a deliberate design choice: P/D ratios are most informative at lower tau (where the divergence occurs), while consumption growth is interesting over a wider range. Not an error.

6. **Consumption growth formula consistency with paper.** The paper's equation (eq:transfer-ratio) states c_post/c_no-transfer = 1 + tau*(1-delta*tau)*(1-phi*alpha)/(phi*alpha). The code computes phi_eff = phi + tau*(1-delta*tau)*(1-phi*alpha)/alpha, so consumption_growth = phi_eff*(1+eta). Dividing by the no-transfer baseline phi*(1+eta) gives 1 + tau*(1-delta*tau)*(1-phi*alpha)/(phi*alpha), matching the paper exactly.

**Exhibit verdict: PASS.** All annotations verified numerically, divergence is a genuine model feature, and the consumption growth formula matches the paper's equation.
