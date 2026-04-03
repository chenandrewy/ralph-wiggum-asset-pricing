# tests/factcheck-exhibits.py
Started: 2026-04-02 22:54:31 EDT
Runtime: 2m 14s
[ralph-garage/agent-logs/20260402T225431.388905-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T225431.388905-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: Both exhibits are correctly generated and consistent with code, data methodology, and paper claims.

## Figure 1: AI vs. Non-AI Stock Valuations (CRSP)

**Description:** Time-series plot (2019–2025) of trailing 12-month price-dividend ratios for five AI stocks (NVDA, MSFT, GOOGL, META, AMZN) versus the rest of the CRSP universe. AI stocks (blue) rise from ~100 to 400+; non-AI stocks (red) remain relatively flat around 50–150.

### Suspicious features

1. **AI P/D ratio reaches very high levels (~400+).** Price-dividend ratios above 400 are unusual for broad indices but plausible for a handful of mega-cap tech stocks with very low dividend yields (e.g., NVDA's dividend yield is negligible relative to its market cap post-2023).

2. **Sharp surge in AI line during 2024–2025.** The AI P/D ratio roughly doubles between early 2023 and late 2024, which looks abrupt.

3. **Non-AI line is much lower and flatter than the AI line.** The broad CRSP universe has a much higher aggregate dividend yield than the five AI names, so a lower P/D ratio is expected, but the magnitude of the gap is worth checking.

### Code check

1. **High AI P/D values:** The code (`ai-valuations-figure.R:46–83`) computes group-level P/D by summing market caps and trailing 12-month dividends across the five AI stocks. Because these firms (especially NVDA) have very high market capitalizations but very low dividend payouts, a group P/D of 400+ is mechanically plausible. The y-axis is capped at 500 (line 124), which is a reasonable readability safeguard. **Verified as plausible.**

2. **Sharp 2023–2025 surge:** This mirrors the well-documented AI stock boom (NVDA alone went from ~$300B to $3T+ market cap while dividends barely changed). The code computes dividends via `ret - retx` (total return minus price return), which correctly captures split-adjusted dividends and avoids the NVDA 10:1 split issue noted in the code comments (lines 48–49). **Verified as plausible.**

3. **AI vs. Non-AI gap:** "Non-AI" is defined as the entire rest of the CRSP universe (LEFT JOIN on `ai_permnos`, line 72), which matches the caption ("rest of the CRSP universe"). The broader market naturally has higher dividend yields, producing lower P/D ratios. **Verified as consistent.**

**Note:** No cached CRSP data exists locally (`/workspace/data/` is empty), so exact data values cannot be independently verified. However, the SQL query methodology is sound: dividends are derived from `ret - retx` applied to lagged market cap, avoiding split-adjustment pitfalls, and trailing 12-month sums use a correct rolling window. The code is consistent with standard CRSP practices.

**Exhibit verdict: PASS** — Visual features are consistent with the generating code and known market dynamics. No artifacts or errors detected.

## Table 1: Numerical Illustration: Price-Dividend Ratios

**Description:** Table showing price-dividend ratios ($V_{\mathrm{pre}}^A$, $V_{\mathrm{pre}}^N$, $V_{\mathrm{pre}}^{A,\mathrm{CM}}$), the spread, and the hedging premium for five values of singularity probability $p \in \{0, 0.005, 0.01, 0.02, 0.05\}$.

### Suspicious features

1. **At $p = 0$, all three valuation columns equal 11.9 and the spread and premium are exactly zero.** This is a potential edge case.

2. **AI valuation $V_{\mathrm{pre}}^A$ grows rapidly with $p$ (11.9 → 26.5) while non-AI $V_{\mathrm{pre}}^N$ declines (11.9 → 10.6).** The divergence is large — a 5% singularity probability more than doubles the AI P/D ratio.

3. **Hedging premium reaches 73.4% at $p = 0.05$.** This is a very large premium from a small probability event.

### Code check

All table values were independently recomputed from the model parameters:

| $p$ | $V_{\mathrm{pre}}^A$ | $V_{\mathrm{pre}}^N$ | $V_{\mathrm{pre}}^{A,\mathrm{CM}}$ | Spread | Hedge Prem. (%) |
|---|---|---|---|---|---|
| 0.000 | 11.94 | 11.94 | 11.94 | 0.00 | 0.00 |
| 0.005 | 14.14 | 11.74 | 12.45 | 2.39 | 13.59 |
| 0.010 | 16.10 | 11.57 | 12.90 | 4.53 | 24.83 |
| 0.020 | 19.45 | 11.27 | 13.67 | 8.19 | 42.33 |
| 0.050 | 26.51 | 10.63 | 15.29 | 15.88 | 73.38 |

These match the table values after rounding to one decimal place. Specifically:

1. **$p = 0$ edge case:** When $p = 0$, all formulas reduce to $V = R/(1-R) = 0.9227/0.0773 = 11.94 \approx 11.9$. Spread and premium are exactly zero because without singularity risk there is no hedging channel. **Correct.**

2. **Divergence with $p$:** The AI valuation rises because $\Phi^A = 6.19 \gg 1$, meaning the singularity state delivers a large payoff to AI stocks (driven by $\delta^{-\gamma} = 0.75^{-3} = 2.37$ and $\tilde{\theta}/\theta = 3$). Non-AI stocks decline because $\Phi^N = 1.13$, meaning the singularity payoff barely exceeds the normal state, and the denominator effect (higher effective discount rate from $(1-p)R$ falling) dominates. **Correct.**

3. **Large hedging premium:** The premium isolates the $\delta^{-\gamma}$ displacement channel. With $\gamma = 3$ and $\delta = 0.75$, the marginal utility multiplier is $(0.75)^{-3} = 2.37$, which amplifies the covariance between the SDF and AI dividends. A 73% premium at $p = 0.05$ is large but mechanically follows from the model parameters. **Correct.**

**Paper prose consistency:** The text (line 219) claims $V_{\mathrm{pre}}^A \approx 16.1$ (✓), $V_{\mathrm{pre}}^N \approx 11.6$ (✓), ratio "roughly 1.4" (actual 1.39 ✓), both equal "approximately 11.9" at $p=0$ (✓), $V_{\mathrm{pre}}^{A,\mathrm{CM}} \approx 12.9$ (✓), and hedging premium "about 25%" (actual 24.8% ✓).

**Parameters in table notes** match the code: $\beta = 0.96$, $\gamma = 3$, $g = 0.02$, $\tilde{g} = 0.05$, $\theta = 0.05$, $\tilde{\theta} = 0.15$, $\nu = 0.55$, $\tilde{\nu} = 0.30$. ✓

**Exhibit verdict: PASS** — All values independently verified from model formulas. Table is correctly generated and consistent with paper prose.
