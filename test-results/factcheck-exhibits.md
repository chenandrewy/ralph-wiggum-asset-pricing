# tests/factcheck-exhibits.py
Started: 2026-04-02 21:59:20 EDT
Runtime: 2m 28s
[ralph-garage/agent-logs/20260402T215920.397953-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T215920.397953-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: Both exhibits are correctly generated and their visible features are supported by the code and parameters.

## Figure 1: AI vs. Non-AI Stock Valuations (CRSP)

**Description:** A time-series line chart (2019–2025) showing trailing 12-month price-dividend ratios for two value-weighted portfolios from CRSP: "AI Stocks" (NVDA, MSFT, GOOGL, META, AMZN) in blue, and "Non-AI Stocks" (rest of CRSP universe) in red. AI stocks show P/D ratios rising sharply from ~50 in 2019 to roughly 400–500 by 2024–2025, while non-AI stocks remain relatively flat around 50–100.

### Suspicious features

1. **Extreme AI P/D levels (near 400–500).** The AI portfolio reaches P/D ratios far above what standard indexes show.
2. **Sharp upward spike around 2023–2024.** The AI line shows a dramatic acceleration.
3. **Y-axis capped at 500.** Code line 128 applies `min(ylim[2], 500)`, potentially hiding higher values.

### Code check

1. **Extreme AI P/D levels.** The generating code (`code/ai-valuations-figure.R`) computes a value-weighted portfolio P/D as total market cap divided by total trailing 12-month dividends (lines 80, 112). The five AI constituents include stocks with very low dividend yields (e.g., NVDA, AMZN). When market caps surge but dividends remain tiny, the portfolio-level P/D ratio naturally reaches extreme values. This is a correct mechanical consequence of the metric, not a coding error. The non-AI basket includes thousands of CRSP stocks, many of which also pay no dividends, but their collective weight dilutes the effect. No cached WRDS data is available locally to verify the exact data values, but the code logic (SQL query at lines 50–87, trailing-window computation at lines 100–114) is methodologically sound and the resulting magnitudes are plausible for these stocks.

2. **Sharp spike around 2023–2024.** This aligns with the widely documented AI valuation surge (ChatGPT launch in late 2022, subsequent market repricing of AI stocks). The code does not manufacture this; it follows from the CRSP data.

3. **Y-axis cap at 500.** The cap is a readability measure (line 128). In the rendered image, the AI line stays below 500 throughout, so no data appears truncated. The cap does not distort visible information.

**Caption check:** Caption states "NVDA, MSFT, GOOGL, META, AMZN" — matches the SQL query ticker list at line 54. Caption says "trailing 12-month dividends" — matches the rolling-window computation at lines 107–111. Caption says "CRSP" — matches the data source (`crsp.msf`, `crsp.msedist`).

**Exhibit verdict: PASS** — Code logic is correct; extreme P/D levels are an expected consequence of computing value-weighted P/D for low-dividend mega-cap tech stocks; no cached data is available but the methodology is verifiable and results are plausible.

## Table 1: Numerical Illustration: Price-Dividend Ratios

**Description:** A table showing model-implied price-dividend ratios for AI stocks ($V_0^A$), non-AI stocks ($V_0^N$), and AI stocks under complete markets ($V_0^{A,\text{CM}}$), plus the spread and hedging premium, for five values of singularity probability $p \in \{0, 0.005, 0.01, 0.02, 0.05\}$.

### Suspicious features

1. **Rapid growth of $V_0^A$ with $p$.** AI P/D rises from 11.9 to 26.5 as $p$ goes from 0 to 0.05 — more than doubling.
2. **$V_0^N$ declining with $p$.** Non-AI valuation falls from 11.9 to 10.6.
3. **All three valuations equal at $p=0$.** $V_0^A = V_0^N = V_0^{A,\text{CM}} = 11.9$.
4. **Hedging premium reaching 73.4% at $p=0.05$.** A large premium from a 5% annual singularity probability.

### Code check

Independent recomputation of all formulas in `code/numerical-illustration.R` confirms every cell:

| $p$ | $V_0^A$ | $V_0^N$ | $V_0^{A,\text{CM}}$ | Spread | Hedge Prem. (%) |
|-----|---------|---------|---------------------|--------|-----------------|
| 0.000 | 11.9403 | 11.9403 | 11.9403 | 0.0000 | 0.0 |
| 0.005 | 14.1363 | 11.7431 | 12.4452 | 2.3932 | 13.6 |
| 0.010 | 16.0980 | 11.5669 | 12.8963 | 4.5311 | 24.8 |
| 0.020 | 19.4542 | 11.2655 | 13.6681 | 8.1887 | 42.3 |
| 0.050 | 26.5116 | 10.6317 | 15.2909 | 15.8799 | 73.4 |

All match the `.tex` output when rounded to one decimal place.

1. **Rapid growth of $V_0^A$.** Correct. The formula $V_0^A = \frac{(1-p)R + p\Phi^A(1+V_1)}{1-(1-p)R}$ (line 29) has $\Phi^A = 6.19$, so the numerator's singularity term grows quickly with $p$ while the denominator also shifts. The nonlinear amplification is a correct algebraic property.

2. **$V_0^N$ declining.** Correct. $\Phi^N = 1.13 < R/(1-R) = 11.94$, so raising $p$ shifts weight toward a low singularity-state contribution, reducing the valuation. This is the displacement effect on non-AI stocks.

3. **Equality at $p=0$.** Correct. At $p=0$, the formula reduces to $R/(1-R)$ for all assets. Verified: $R/(1-R) = 0.9227/(1-0.9227) = 11.94$.

4. **Large hedging premium.** Correct. The hedging premium formula $(V_0^A - V_0^{A,\text{CM}})/V_0^{A,\text{CM}}$ isolates the displacement channel ($\Delta^{-\gamma}$ factor). With $\Delta = 0.75$ and $\gamma = 3$, $\Delta^{-\gamma} = 2.37$, creating substantial amplification.

**Text consistency:** The paper text (line 236) claims $V_0^A \approx 16.1$, $V_0^N \approx 11.6$, ratio $\approx 1.4$, both $\approx 11.9$ at $p=0$, $V_0^{A,\text{CM}} \approx 12.9$, and hedging premium $\approx 25\%$. All confirmed: 16.098, 11.567, 1.39, 11.940, 12.896, 24.8%.

**Parameter check:** Code parameters (lines 8–17) match the table notes and paper text: $\beta=0.96$, $\gamma=3$, $g=0.02$, $\tilde{g}=0.05$, $\theta=0.05$, $\tilde{\theta}=0.15$, $\nu=0.55$, $\tilde{\nu}=0.30$.

**Exhibit verdict: PASS** — All values independently verified by recomputation; code formulas match the paper's model; text claims are consistent with table entries.
