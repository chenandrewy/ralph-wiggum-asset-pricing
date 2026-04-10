# tests/factcheck-exhibits.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 5m 44s
[ralph-garage/agent-logs/20260409T215056.131017-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T215056.131017-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: FAIL
REASON: Figure 2 Panel (a) uses an approximate P/D formula that overstates AI stock valuations by ~11% versus the exact backward-recursion method used in Table 1 at identical parameters.

## Figure 1: Valuations of AI-Exposed Stocks vs. the Broader Market

**Description:** Time-series plot of NASDAQ Composite and S&P 500 monthly closing prices, normalized to January 2015 = 100. NASDAQ (solid blue) outpaces S&P 500 (dashed red), with the gap widening sharply from 2023 onward.

### Suspicious features
1. **Sharp NASDAQ run-up post-2023:** The NASDAQ line steepens notably around 2023, creating a widening gap.
2. **COVID dip (~2020) and 2022 drawdown:** Both lines show dips at these dates.

### Code check
- The code (`code/generate-exhibits.R`, lines 286–358) downloads NASDAQ from FRED and S&P 500 from the Shiller/datahub dataset, takes the last observation per month, aligns date ranges, and normalizes the earliest common month to 100.
- The sharp NASDAQ run-up post-2023 reflects the AI/tech boom in the actual market data. The COVID dip and 2022 drawdown are real market events.
- Data sources match the caption ("NASDAQ from FRED; S&P 500 from the Shiller dataset").
- Y-axis label ("Normalized Price (Jan 2015 = 100)") matches the normalization logic.
- Legend labels and line styles match the code's `scale_color_manual` and `scale_linetype_manual` specifications.

**Exhibit verdict: PASS** — All visible features are consistent with real market data and correctly generated code.

## Table 1: Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks

**Description:** Grid of P/D ratios for AI and non-AI stocks across singularity probabilities ($p$ = 0.1%–1.0%) and extinction probabilities ($\xi$ = 0%–20%). Parameters: $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$.

### Suspicious features
1. **AI P/D jumps from 15.5 to 26.5 as $p$ goes from 0.5% to 1.0% (at $\xi=0$):** A near-doubling for a doubling of $p$.
2. **Non-AI P/D also rises with $p$:** Counterintuitive since non-AI stocks lose share in a singularity.

### Code check
1. **AI P/D jump (15.5 → 26.5):** The exact backward-recursion formula (`compute_pd_ai_exact`, lines 51–80) is nonlinear in $p$. At higher $p$, the singularity SDF component ($\phi^{-\gamma}(1+\eta)^{-\gamma}\Gamma^{AI}$) dominates. Manually verified: Non-AI P/D at $p=0.001, \xi=0$ gives 9.77 → rounds to 9.8 ✓. Non-AI at $p=0.005, \xi=0.10$ gives 10.84 → rounds to 10.8 ✓. Non-AI at $p=0.01, \xi=0$ gives 13.26 → rounds to 13.3 ✓.
2. **Non-AI P/D rising with $p$:** Although non-AI dividend share shrinks ($\Gamma^N = 0.8 \times 1.5 = 1.2$), the SDF product $\phi^{-\gamma}(1+\eta)^{-\gamma}\Gamma^N = 16 \times 0.1975 \times 1.2 = 3.79 > 1$. Because the SDF-weighted dividend growth exceeds 1, higher $p$ raises non-AI P/D. This is correct: the displacement-driven marginal-utility surge ($\phi^{-\gamma}=16$) more than compensates for the dividend share loss.
3. **Footnote parameters** match code parameters at lines 18–25. Table header, column structure, and rounding format verified against `format_num` (line 97: `sprintf("%.1f", x)`).

**Exhibit verdict: PASS** — All values verified numerically; patterns are consistent with model mechanics.

## Figure 2: Government Transfers and the Singularity

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate $\tau$ for baseline ($\eta=0.5, \phi=0.5$) and large singularity ($\eta=9, \phi=0.05$). Panel (b) shows household consumption growth in the singularity state vs. $\tau$, with a log-scaled y-axis.

### Suspicious features
1. **Panel (a): Large-singularity line entering from the top with "P/D → ∞ as τ → 0" annotation.** P/D is undefined (NA) at low $\tau$ values.
2. **Panel (a): Baseline P/D level at $\tau=0$ appears to be ~16.7, but Table 1 reports 15.0 for matching parameters ($p=0.5\%, \xi=5\%$).**
3. **Panel (b): Catastrophe annotations** — "50% loss" for large singularity and "25% loss" for baseline at $\tau=0$.

### Code check
1. **Large-singularity P/D divergence:** At $\tau=0$, $\phi=0.05$, $\eta=9$: the SDF product is $0.05^{-4} \times 10^{-4} \times \Gamma^{AI} = 160{,}000 \times 0.0001 \times 21.3 = 341$. This yields $K = 0.905 \times (0.995 + 0.005 \times 0.95 \times 341) = 2.37 > 1$, so P/D is undefined. The code returns `NA` (line 155), and the annotation (lines 217–219) correctly marks this divergence. **Verified as correct.**

2. **Baseline P/D level discrepancy (16.7 vs. 15.0):** The extension figure uses `compute_pd_with_transfer` (lines 150–157), which is the *approximate* closed-form treating post-singularity P/D as equal to pre-singularity. Table 1 uses `compute_pd_ai_exact` (lines 51–80), which performs backward recursion over successive singularity states. At $p=0.005, \xi=0.05$: approximate gives 16.7, exact gives 15.0 — an 11.3% overstatement. The two exhibits use inconsistent computation methods for the same economic quantity at the same parameters without disclosure. **This is a methodological inconsistency.**

3. **Catastrophe annotations:** `consumption_growth(0, 0.5, 0.5) = 0.5 × 1.5 = 0.75`, so 25% loss ✓. `consumption_growth(0, 9.0, 0.05) = 0.05 × 10 = 0.5`, so 50% loss ✓. Both match the code (lines 227–228) and the paper text. **Verified as correct.**

**Exhibit verdict: FAIL** — Panel (a) uses an approximate P/D formula (`compute_pd_with_transfer`) that overstates the AI P/D level by ~11% versus the exact backward-recursion method (`compute_pd_ai_exact`) used to generate Table 1 at identical parameter values ($p=0.5\%, \xi=5\%$). A reader comparing the two exhibits would see the baseline starting at ~16.7 in the figure versus 15.0 in the table. The figure code should use the exact method for consistency, or the discrepancy should be disclosed.
