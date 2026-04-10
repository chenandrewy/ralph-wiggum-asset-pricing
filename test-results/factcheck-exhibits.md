# tests/factcheck-exhibits.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 3m 3s
[ralph-garage/agent-logs/20260409T212047.316096-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T212047.316096-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits

VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and consistent with the paper's claims; no artifacts or errors found.

## Figure 1: AI Valuations vs. the Broader Market

**Description:** A line chart showing monthly closing prices for the NASDAQ Composite (solid, blue) and S&P 500 (dashed, red), each normalized to January 2015 = 100, covering roughly 2015--2026. The NASDAQ rises to approximately 450--500 by the end of the sample, while the S&P 500 reaches roughly 280--300, with the gap widening sharply after 2023.

### Suspicious features

1. **Sharp acceleration in NASDAQ post-2023.** The NASDAQ line steepens dramatically after roughly 2023, creating a widening gap with the S&P 500.
2. **No local data cache.** The code downloads data live from FRED (NASDAQCOM) and datahub (Shiller S&P 500 dataset), so exact values cannot be verified from local files.

### Code check

1. **Post-2023 acceleration.** The code (`code/generate-exhibits.R`, lines 254--326) performs a straightforward download-normalize-plot pipeline with no transformations beyond normalization to the first common month = 100. There is no filtering, smoothing, or manipulation that could create a spurious divergence. The sharp post-2023 acceleration reflects real market data (the AI/generative-AI boom following ChatGPT's release in late 2022). **Verified as real.**

2. **No local data cache.** The code downloads from standard public data sources (FRED, datahub Shiller). The normalization logic (lines 299--303) divides by the first observation's value and multiplies by 100. The caption correctly states "Sources: NASDAQ from FRED; S&P 500 from the Shiller dataset." Line styles (solid NASDAQ, dashed S&P) match the legend and caption. While exact plotted values cannot be independently verified from local data, the code logic is transparent and correct. **No artifact detected.**

**Exhibit verdict: PASS** -- Code logic is correct, data sources are standard, and the visible features reflect real market data.

## Table 1: Price-Dividend Ratios

**Description:** A table reporting model-implied P/D ratios for AI stocks and non-AI stocks across a grid of singularity probabilities (p = 0.1% to 1.0%) and extinction probabilities (xi = 0% to 20%), along with the AI/non-AI ratio. Parameters: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, Delta-theta=0.2.

### Suspicious features

1. **Explosive P/D ratio at p=1%, xi=0%.** The AI stock P/D jumps from 33.0 at p=0.8% to 76.4 at p=1.0% (with xi=0%), a 130% increase from only a 25% increase in p. The ratio column jumps from 2.7 to 5.8.
2. **Non-AI P/D barely moves.** Non-AI P/D rises only from 9.8 to 13.3 across the entire p range, while AI P/D rises from 10.5 to 76.4.

### Code check

1. **Explosive P/D at p=1%.** Manually verified the Euler-equation computation (`code/generate-exhibits.R`, lines 42--48). The key driver is K = beta*(1+g)^(1-gamma) * [(1-p) + p*(1-xi)*sdf_sing]. At p=1%, xi=0%: sdf_sing for AI = phi^(-4)*(1+eta)^(-4)*gamma_ai = 16 * 0.1975 * 3.2 = 10.11. K = 0.9046 * (0.99 + 0.01*10.11) = 0.9046 * 1.0911 = 0.987. P/D = 0.987/0.013 = 76.3, matching the table value of 76.4 (rounding). The convexity arises because K/(1-K) is highly nonlinear as K approaches 1. **Verified as correct.**

2. **Muted non-AI response.** For non-AI stocks, gamma_non = share_ratio_non*(1+eta) = 0.8*1.5 = 1.2. sdf_sing_non = 16*0.1975*1.2 = 3.79. At p=1%, xi=0%: K = 0.9046*(0.99 + 0.01*3.79) = 0.9046*1.0279 = 0.930. P/D = 0.930/0.070 = 13.3. The singularity SDF factor for non-AI is much smaller (3.79 vs. 10.11) because the non-AI dividend share *shrinks* in a singularity, so K remains far from 1. **Verified as correct.**

The table footnote parameters match the code parameters exactly (lines 18--24). The paper's claims about the table (ratios of 1.5 to 6 for p in 0.5--1% range; extinction compressing the premium) match the table values.

**Exhibit verdict: PASS** -- All values manually verified against the generating code; the explosive nonlinearity is a genuine property of the pricing formula.

## Figure 2: Extension Panels (Government Transfers and the Singularity)

**Description:** Two panels. Panel (a) plots AI stock P/D ratio vs. tax rate tau for two scenarios: Baseline (eta=0.5, phi=0.5) and Large Singularity (eta=9, phi=0.05), with p=0.5%, xi=5%. Panel (b) plots household consumption growth in the singularity state vs. tau on a log scale, with a horizontal dashed line at 1 (no change).

### Suspicious features

1. **Large-singularity P/D diverges as tau approaches 0 in Panel (a).** The blue dashed line exits the top of the chart at low tau, with an annotation "P/D -> infinity as tau -> 0".
2. **Catastrophe annotation in Panel (b).** The large-singularity scenario shows consumption growth = 0.5 at tau=0 (labeled "Catastrophe: 50% loss"), and the baseline shows 0.75 ("25% loss").
3. **Panel (a) y-axis capped at 20.** The large-singularity line is cut off at low tau values.

### Code check

1. **P/D divergence at tau=0.** At tau=0, phi_eff = phi_large = 0.05. sdf_sing = 0.05^(-4) * 10^(-4) * 21.33 = 160000 * 0.0001 * 21.33 = 341.3. K = 0.9046*(0.995 + 0.005*0.95*341.3) = 0.9046*2.616 = 2.367 > 1, so P/D is undefined (NA). As tau increases, phi_eff grows, the SDF factor shrinks, and K eventually drops below 1, producing finite P/D values that decrease with tau. The code correctly returns NA when K >= 1 (line 124) and the plot filters out NA values (line 169). The paper correctly explains this as a violation of the existence condition (Remark 1). **Verified as correct.**

2. **Catastrophe annotations.** cons_large_0 = phi_large*(1+eta_large) = 0.05*10 = 0.5 (50% loss). cons_base_0 = phi*(1+eta) = 0.5*1.5 = 0.75 (25% loss). These match the code (lines 195--196) and the annotation labels (lines 202--209). The paper states "consumption halves under the large singularity (phi(1+eta)=0.5)" and "falls by 25% under the baseline (phi(1+eta)=0.75)" -- both correct. **Verified as correct.**

3. **Y-axis cap.** The code sets y_cap_a = 20 (line 170) and uses scale_y_continuous(limits = c(7, 20)) on line 184. The annotation at exit_tau explains the divergence. This is a presentation choice, not an artifact. **No error.**

Parameters match the paper's stated values: alpha=0.70 (line 108), p=0.5% (line 127), xi=5% (line 128), delta=0.5 (line 109). The consumption growth formula (line 113) matches equation (eq:transfer-ratio) in the paper.

**Exhibit verdict: PASS** -- All features verified against code; the divergence and catastrophe markers are genuine mathematical properties correctly computed and labeled.
