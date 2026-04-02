# tests/factcheck-exhibits.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 2m 47s
[ralph-garage/agent-logs/20260402T184535.071107-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T184535.071107-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits

VERDICT: PASS
REASON: Both exhibits are correctly generated and consistent with code, data logic, and in-text claims.

## Figure 1: AI vs. Non-AI Stock Valuations (CRSP)

**Description:** Time-series plot of price-dividend ratios (trailing 12-month dividends) for a portfolio of five AI stocks (NVDA, MSFT, GOOGL, META, AMZN) versus the rest of the CRSP universe, from 2019 to 2025. AI stocks (blue) rise sharply from ~100 to ~400+; non-AI stocks (red) remain relatively flat around 50.

### Suspicious features

1. **AI portfolio P/D reaches ~400+, which is extremely high.** A price-dividend ratio of 400 means the portfolio's market cap is 400x its trailing 12-month dividends. This is unusually elevated even for growth stocks.

2. **Y-axis capped at 500 in the code (line 128).** The code sets `ylim[2] <- min(ylim[2], 500)`, which could hide spikes above 500.

### Code check

1. **High P/D level:** The code computes portfolio-level P/D as total market cap / total trailing 12-month dividends (`code/ai-valuations-figure.R:112`). Among the five AI stocks, AMZN pays zero dividends (throughout the sample), and META and GOOGL only began paying dividends in 2024. NVDA pays a minimal dividend; MSFT pays a modest one. AMZN and the pre-dividend META/GOOGL contribute enormous market cap to the numerator but zero to the denominator, mechanically inflating the portfolio P/D ratio. This is a correct computation of the aggregate P/D for these five stocks---it is not a coding error. The high level is a real feature of these stocks' low dividend yields.

2. **Y-axis cap at 500:** The cap is applied to prevent extreme outliers from compressing the rest of the plot. In the rendered figure, the AI line appears to stay below 500, so the cap does not appear to be binding. No data is visibly truncated.

**Data verification note:** The figure is generated from a live WRDS/CRSP query (`code/ai-valuations-figure.R`). No cached intermediate data exists locally. The SQL logic is correct: it identifies AI stocks by PERMNO via ticker matching, computes monthly market cap, joins monthly distributions, and computes trailing 12-month portfolio dividends. The qualitative pattern (sharply rising AI P/D, stable non-AI P/D) is consistent with known market behavior over 2019--2025. The paper makes no specific numerical claims about the figure beyond the qualitative description.

**Exhibit verdict: PASS** -- Code logic is correct; visible features are explained by the composition of the AI portfolio; no coding errors or artifacts identified.

## Table 1: Numerical Illustration: Price-Dividend Ratios

**Description:** A table reporting price-dividend ratios ($V_0^A$, $V_0^N$, $V_0^{A,\text{CM}}$), the AI-minus-non-AI spread, and the hedging premium (%) for five values of the singularity probability $p \in \{0, 0.005, 0.01, 0.02, 0.05\}$. Parameters: $\beta = 0.96$, $\gamma = 3$, $g = 0.02$, $\tilde{g} = 0.05$, $\theta = 0.05$, $\tilde{\theta} = 0.15$, $\nu = 0.55$, $\tilde{\nu} = 0.30$.

### Suspicious features

1. **$V_0^A$ grows rapidly with $p$, reaching 26.5 at $p = 0.05$.** This is a 122% increase over the $p=0$ baseline of 11.9 from a 5% singularity probability.

2. **$V_0^N$ decreases as $p$ rises.** Non-AI stocks lose value as singularity risk increases, which could be counterintuitive.

3. **Hedging premium reaches 73.4% at $p = 0.05$.** This is a large premium from a small probability shift.

### Code check

All values independently verified by re-running `code/numerical-illustration.R` and by manual computation from the model formulas in the paper (Proposition 1, equations for $V_0^A$, $V_0^N$, $V_0^{A,\text{CM}}$):

| $p$ | $V_0^A$ (computed) | $V_0^N$ (computed) | $V_0^{A,\text{CM}}$ (computed) | Spread | Hedge Prem. |
|---|---|---|---|---|---|
| 0.000 | 11.940 | 11.940 | 11.940 | 0.000 | 0.0% |
| 0.005 | 14.136 | 11.743 | 12.445 | 2.393 | 13.6% |
| 0.010 | 16.098 | 11.567 | 12.896 | 4.531 | 24.8% |
| 0.020 | 19.454 | 11.266 | 13.668 | 8.189 | 42.3% |
| 0.050 | 26.512 | 10.632 | 15.291 | 15.880 | 73.4% |

All values round correctly to the one-decimal-place figures shown in the table.

1. **Rapid growth of $V_0^A$:** Correctly generated. The formula $V_0^A = [(1-p)R + p\Phi^A(1+V_1)] / [1-(1-p)R]$ has $\Phi^A = 6.19$, which is large because $\delta^{-\gamma} = 0.75^{-3} \approx 2.37$ amplifies the singularity-state pricing kernel. This is the core hedging mechanism of the model.

2. **Declining $V_0^N$:** Correctly generated. $\Phi^N = 1.13 < R/(1-R) \approx 11.94$, so the singularity state contributes less than the normal state for non-AI stocks. Increasing $p$ shifts weight toward the low-value singularity state.

3. **Large hedging premium:** Correctly generated. The premium is $(V_0^A - V_0^{A,\text{CM}})/V_0^{A,\text{CM}}$. The difference between $\Phi^A$ (6.19, with displacement) and $\Phi^{A,\text{CM}}$ (2.61, without displacement) drives this wedge.

**In-text claims verified:** The paper states $V_0^A \approx 16.1$ (computed: 16.098), $V_0^N \approx 11.6$ (computed: 11.567), ratio "roughly 1.4" (16.1/11.6 = 1.39), both equal "approximately 11.9" at $p=0$ (computed: 11.940), $V_0^{A,\text{CM}} \approx 12.9$ (computed: 12.896), hedging premium "about 25%" (computed: 24.8%). All correct.

**Exhibit verdict: PASS** -- All table values independently verified by re-running the generating code and by manual computation from the paper's formulas. In-text claims match.
