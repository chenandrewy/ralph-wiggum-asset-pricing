# tests/factcheck-exhibits.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 3m 51s
[ralph-garage/agent-logs/20260409T202148.448674-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T202148.448674-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and consistent with the paper's claims.

## Figure 1: Valuations of AI-Exposed Stocks vs. the Broader Market

**Description:** A time-series plot showing monthly closing prices for the NASDAQ Composite (solid line) and S&P 500 (dashed line), each normalized to January 2015 = 100. The NASDAQ line dramatically outpaces the S&P 500, with the gap widening post-2023.

### Suspicious features

1. **Sharp post-2023 divergence.** The NASDAQ line accelerates away from the S&P 500 starting around 2023, producing a widening gap.
2. **COVID dip around 2020.** Both lines show a sharp drop and rapid recovery.
3. **No local cached data.** The code downloads data from external URLs (FRED for NASDAQ, datahub Shiller dataset for S&P 500) with no local cache, so exact values cannot be verified against stored data.

### Code check

1. **Post-2023 divergence.** This reflects real market behavior: the NASDAQ Composite is heavily weighted toward AI/technology firms (NVIDIA, Microsoft, etc.) whose valuations surged with the generative AI boom. The code downloads actual market data (`NASDAQCOM` from FRED, S&P 500 from Shiller datahub) and normalizes to the first common month. No transformation beyond normalization is applied. The divergence is real.
2. **COVID dip.** Both indices dropped sharply in March 2020 and recovered quickly. This is well-documented market history. The code applies no smoothing or filtering, so the dip reflects the raw data. Real and correctly generated.
3. **No local cache.** The code at `code/generate-exhibits.R:230-301` downloads live data each run. While exact values cannot be verified from local files, the download logic is straightforward (FRED CSV API, datahub CSV), normalization is correct (`base <- d$Value[which.min(d$Date)]`; `d$Index <- d$Value / base * 100`), and the visible patterns are consistent with known market history. This is not an artifact.

**Exhibit verdict: PASS.** The figure accurately displays real market data with correct normalization. All visible features reflect genuine market movements.

## Table 1: Price-Dividend Ratios

**Description:** A grid of P/D ratios for AI stocks, non-AI stocks, and their ratio, across five singularity probabilities (p = 0.1% to 1.0%) and four extinction probabilities (xi = 0% to 20%). Parameters: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, Delta_theta=0.2.

### Suspicious features

1. **Explosive AI P/D at p=1%.** The AI stock P/D jumps from 33.0 at p=0.8% to 76.4 at p=1.0% (xi=0%), a nonlinear acceleration that could signal a coding error or near-divergence.
2. **Non-AI P/D barely changes.** Non-AI P/D moves only from 9.8 to 13.3 across the entire grid, while AI P/D spans 10.5 to 76.4.

### Code check

1. **Explosive AI P/D.** Verified by manual computation. At p=1%, xi=0%: K = 0.904629 * [0.99 + 0.01 * 16 * 0.19753 * 3.2] = 0.904629 * 1.09114 = 0.9871. P/D = K/(1-K) = 0.9871/0.0129 = 76.4. The near-unity K drives the nonlinearity (P/D = K/(1-K) has a pole at K=1). This is the correct economic behavior: as the singularity probability rises, the SDF-weighted dividend growth approaches the discount rate, and the pricing sum nearly diverges. The code (`compute_pd` at line 42) implements the formula correctly.
2. **Stable non-AI P/D.** Verified: Gamma_N = 1.2 vs Gamma_AI = 3.2. The singularity term for non-AI stocks contributes much less to K (singularity weight: phi^(-4) * (1+eta)^(-4) * 1.2 = 3.79 vs 10.11 for AI), so the denominator (1-K) stays well above zero. The asymmetry is a direct consequence of Delta_theta > 0, which makes AI dividends grow faster in the singularity. Correct.

Additional spot checks: p=0.5%/xi=0% gives AI P/D=17.5, Non-AI P/D=11.1, Ratio=1.6; p=0.008/xi=5% gives AI P/D=29.2. All verified against independent Python computation and match the table exactly.

**Exhibit verdict: PASS.** All table values are correctly generated from the closed-form P/D formula. The nonlinear behavior at high p is a genuine feature of the pricing equation, not an artifact.

## Figure 2: Government Transfers and the Singularity (Extension Panels)

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratios vs. tax rate tau for baseline (eta=0.5, phi=0.5) and large singularity (eta=9, phi=0.05). Panel (b) shows household consumption growth in the singularity state vs. tau, on a log scale. Both panels use p=0.5%, xi=5%, alpha=0.70, delta=0.5.

### Suspicious features

1. **Panel (a): Large-singularity P/D is undefined at tau=0 and drops from the y-axis cap.** The large singularity line appears to start partway through the x-axis range rather than from tau=0, with an annotation "P/D -> infinity as tau -> 0."
2. **Panel (a): Y-axis capped at 25.** The large singularity line is clipped, potentially hiding important behavior.
3. **Panel (b): Enormous consumption growth for large singularity.** The large singularity line rises steeply on the log scale, reaching values well above 1 even at moderate tau.
4. **Panel (b): Baseline line shows modest gains.** The baseline scenario barely crosses 1 even at high tau, creating a stark visual contrast.

### Code check

1. **Undefined P/D at tau=0 for large singularity.** Verified: at tau=0, phi_eff=0.05, K = 0.904629 * [0.995 + 0.005*0.95*0.05^(-4)*10^(-4)*21.333] = 0.904629 * [0.995 + 0.005*0.95*160000*0.0001*21.333] = 0.904629 * 2.617 = 2.367. Since K > 1, the P/D formula returns NA. The code correctly returns NA when K >= 1 (line 123-124). The annotation is placed via `exit_tau`, the first tau where the large singularity P/D drops below the y-cap (line 169). Correct.
2. **Y-axis cap at 25.** Set explicitly in code (`y_cap_a <- 25`, line 165) with `scale_y_continuous(limits = c(y_min_a, y_cap_a))`. This is a deliberate visualization choice to keep the panel readable; the annotation explains the asymptotic behavior. Not an artifact.
3. **Large consumption growth.** At tau=0.50: consumption_growth = 0.05*10 + 0.50*(1-0.25)*(1-0.035)/0.70*10 = 0.5 + 0.50*0.75*1.37857*10 = 0.5 + 5.17 = 5.67. The enormous growth comes from the (1+eta)=10 multiplier on the transfer base. The code (`consumption_growth` function, line 113) correctly implements: phi*(1+eta) + tau*(1-delta*tau)*(1-phi*alpha)/alpha*(1+eta). This matches equation (8) in the paper.
4. **Modest baseline gains.** At tau=0.50 for baseline: 0.5*1.5 + 0.50*0.75*(1-0.5*0.70)/0.70*1.5 = 0.75 + 0.50*0.75*0.929*1.5 = 0.75 + 0.522 = 1.27. The baseline has (1+eta)=1.5 vs 10 for the large singularity, so transfers produce proportionally smaller gains. Correct.

**Exhibit verdict: PASS.** Both panels are correctly generated. The P/D divergence at low tau for the large singularity is a genuine feature of the model (existence condition violated). The consumption growth patterns correctly reflect the formula with scenario-specific parameters.
