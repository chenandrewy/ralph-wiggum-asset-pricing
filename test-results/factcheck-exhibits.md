# tests/factcheck-exhibits.py
Started: 2026-04-10 22:15:41 EDT
Runtime: 3m 8s
[ralph-garage/agent-logs/20260410T221541.790981-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260410T221541.790981-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated, with table values, figure parameters, and data sources verified against the code.

## Figure 1: AI Valuations vs. the Broader Market

**Description:** Time-series plot of NASDAQ Composite (solid blue) and S&P 500 (dashed red), monthly closing prices normalized to January 2015 = 100. Shows NASDAQ dramatically outpacing S&P 500, especially post-2023.

### Suspicious features

1. **Data ends near 2026 despite code requesting through 2025-12-31.** The x-axis extends to approximately 2026. The code downloads S&P 500 from datahub (Shiller dataset) and NASDAQ from FRED, both filtered to end at 2025-12-31. The rendered endpoint depends on data availability at generation time. No truncation artifacts or discontinuities visible at the end of either series.

2. **No other suspicious features.** Lines are smooth with expected features: a COVID dip around early 2020 and accelerating NASDAQ divergence post-2023. No abrupt jumps, implausible spikes, or seasonal artifacts. Legend labels match line styles (solid = NASDAQ, dashed = S&P 500). Caption correctly attributes NASDAQ to FRED and S&P 500 to the Shiller dataset, matching the code (lines 326, 335).

### Code check

- Normalization to first common month = 100: code lines 354-358, confirmed correct.
- Monthly aggregation (last observation per month): code lines 338-342, standard approach.
- Data sources match caption: FRED for NASDAQ (line 335), datahub/Shiller for S&P 500 (line 326).
- Color and linetype assignments match legend: NASDAQ solid blue (#2166AC), S&P dashed red (#B2182B) at lines 371-374.

**Exhibit verdict: PASS** — Data sources, normalization, and visual features are all consistent with the generating code.

## Table 1: Price-Dividend Ratios

**Description:** Grid of P/D ratios for AI and non-AI stocks across singularity probability p (0.1%–1.0%) and extinction probability xi (0%–20%). Shows AI stocks trading at 1.1–2.0x the P/D of non-AI stocks, with the premium increasing in p and decreasing in xi.

### Suspicious features

1. **Non-AI P/D ratios increase with p.** At xi=0%, non-AI P/D goes from 9.8 (p=0.1%) to 13.3 (p=1.0%). This is counterintuitive only if one expects higher disaster probability to lower valuations, but the singularity raises aggregate consumption by factor (1+eta)=1.5 for survivors. The non-AI dividend growth factor gamma_non = 0.8 * 1.5 = 1.2, and with phi^(-gamma) * (1+eta)^(-gamma) = 16 * 0.1975 = 3.16, the SDF-weighted payoff sdf_sing = 3.16 * 1.2 = 3.79 > 1 in the singularity state. Higher p gives more weight to this high-value state, raising the P/D.

2. **Ratio column values appear rounded aggressively.** For example, p=0.5%/xi=0%: AI=15.5, Non-AI=11.1, ratio=15.5/11.1=1.396, reported as 1.4. p=1.0%/xi=0%: 26.5/13.3=1.992, reported as 2.0. All ratios are computed as pd_ai/pd_non and formatted to one decimal place, which is correct.

### Code check

- Spot-checked three cells by re-running the exact computation functions:
  - p=1.0%, xi=0%: AI=26.5, Non-AI=13.3 (matches table row)
  - p=0.5%, xi=5%: AI=15.0, Non-AI=11.0 (matches table row)
  - p=0.1%, xi=20%: AI=10.2, Non-AI=9.7 (matches table row)
- AI P/D uses exact backward recursion over 60 post-singularity theta states (`compute_pd_ai_exact`, lines 51-80). Non-AI uses closed form (`compute_pd_approx`, lines 40-46), which is exact because the non-AI dividend growth factor (1-dtheta)*(1+eta) is theta-independent.
- Table footnote parameters (beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, dtheta=0.2) match code lines 18-24.

**Exhibit verdict: PASS** — Table values verified by independent computation; parameters in footnote match code.

## Figure 2: Extension Panels (Transfers and the Singularity)

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate tau for baseline (eta=0.5, phi=0.5) and large singularity (eta=9, phi=0.05) scenarios. Panel (b) shows household consumption growth in the singularity state vs. tau on a log scale. Both use p=0.5%, xi=5%.

### Suspicious features

1. **Panel (a): Large singularity line emerges from the top of the chart.** The y-axis is capped at 17. The large singularity P/D is undefined (infinite) at tau=0. Verified: at tau=0, phi_eff=phi_large=0.05, so phi_eff^(-gamma)=0.05^(-4)=160,000. The terminal condition K_term = B*((1-p) + p*(1-xi)*S*gamma_ai_term) evaluates to approximately 1.59 > 1, causing NA return. The annotation "P/D → infinity as tau → 0" is correct. The code caps the y-axis at 17 (line 239) and annotates the divergence (lines 240-242).

2. **Panel (b): Large singularity consumption growth starts at 0.5 (50% loss) at tau=0.** Verified: cons_growth(0, 9.0, 0.05) = phi_large*(1+eta_large) = 0.05*10 = 0.5. The annotation says "Catastrophe: 50% loss" — correct. Baseline starts at 0.75 (25% loss): phi*(1+eta) = 0.5*1.5 = 0.75, annotation says "25% loss" — correct.

3. **Panel (b): Large singularity consumption growth appears to reach very high values.** At high tau, consumption_growth(tau, 9, 0.05) = 0.05*10 + tau*max(0, 1-0.5*tau)*(1-0.05*0.70)/0.70*10, which grows rapidly. At tau=0.5: 0.5 + 0.5*0.75*0.965/0.70*10 = 0.5 + 5.175 = 5.675. The log scale handles this range. The deadweight term max(0, 1-delta*tau) = max(0, 1-0.5*tau) goes to zero at tau=2, so the transfer efficiency declines but stays positive in the plotted range (tau up to 0.70). No artifacts.

### Code check

- Parameters match caption: alpha=0.70 (code line 140), p=0.5% (line 183), xi=5% (line 184), delta=0.5 (line 141).
- Baseline: eta=0.5, phi=0.5. Large singularity: eta=9, phi=0.05 (lines 186-197). Match caption.
- `compute_pd_with_transfer` (lines 151-181) correctly mirrors `compute_pd_ai_exact` but substitutes phi_eff incorporating transfers.
- Consumption growth formula (lines 145-147) correctly implements the transfer mechanism with deadweight costs.

**Exhibit verdict: PASS** — Parameter values, divergence behavior, annotation labels, and consumption growth computations all verified against code.
