# tests/factcheck-exhibits.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 3m 26s
[ralph-garage/agent-logs/20260412T154740.741601-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T154740.741601-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits verified against generating code; numerical outputs match, annotations are accurate, and no artifacts or errors found.

## Figure 1: Valuation Ratios and the AI Premium (fig:ai-valuations, page 2)

**Description.** Two-panel time-series figure. Panel (a) shows the S&P 500 trailing price-dividend ratio from the Shiller dataset (2000--2025). Panel (b) shows the NASDAQ Composite price relative to the S&P 500, normalized to January 2015 = 100.

### Suspicious features

1. **Panel (a): P/D ratio reaches ~80 in recent years.** A trailing P/D of 80 implies a dividend yield of ~1.25%, which is at historically elevated levels.
2. **No local data cache.** The code downloads data live from datahub.io (Shiller) and FRED (NASDAQ). There is no local cached copy to verify exact values.

### Code check

1. **P/D ~80.** The code computes `PD = SP500 / Dividend` from the Shiller dataset, where `Dividend` is the trailing 12-month annualized dividend. S&P 500 trailing dividend yields in 2024--2025 were approximately 1.2--1.4%, so P/D ratios of 70--85 are consistent with actual market data. The code path is straightforward (`generate-exhibits.R:322-324`). **Verified as real.**
2. **No local cache.** The Shiller dataset URL (`datahub.io/core/s-and-p-500/r/data.csv`) and FRED series `NASDAQCOM` are standard, well-known public data sources. The qualitative patterns in both panels --- dot-com spike and crash in NASDAQ/S&P ratio, GFC dip in P/D, post-2020 rise in both --- are consistent with known market history. The normalization to Jan 2015 = 100 is implemented correctly (`generate-exhibits.R:394-396`). **No evidence of error; accepted with the caveat that exact replication requires re-downloading.**

**Exhibit verdict: PASS.** Patterns are consistent with known market history; code logic is correct.

## Table 1: Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks (tab:pd-ratios, page 9)

**Description.** A table of model-implied P/D ratios for AI and non-AI stocks across a grid of singularity probability p (0.1%--1.0%) and extinction probability xi (0%--20%). Parameters: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, Delta-theta=0.2.

### Suspicious features

1. **AI P/D ratios increase sharply with p (e.g., 10.4 at p=0.1% to 26.5 at p=1.0% with xi=0%).** This is a large range.
2. **Ratio column shows only values 1.1--2.0, despite large variation in underlying P/D levels.**

### Code check

1. **Numerical verification.** Re-ran the exact backward-recursion code (`compute_pd_ai_exact`) and closed-form non-AI formula (`compute_pd_approx`) for six representative cells:
   - p=0.1%, xi=0%: AI=10.4, Non=9.8, Ratio=1.1 -- matches table.
   - p=0.1%, xi=10%: AI=10.3, Non=9.7, Ratio=1.1 -- matches table.
   - p=0.5%, xi=0%: AI=15.5, Non=11.1, Ratio=1.4 -- matches table.
   - p=0.5%, xi=10%: AI=14.6, Non=10.8, Ratio=1.3 -- matches table.
   - p=1.0%, xi=0%: AI=26.5, Non=13.3, Ratio=2.0 -- matches table.
   - p=1.0%, xi=10%: AI=23.2, Non=12.6, Ratio=1.8 -- matches table.
   All values match the `.tex` output to one decimal place. **Verified.**
2. **Monotonicity.** AI P/D increasing in p and decreasing in xi is economically correct: higher singularity probability raises the option value of AI stocks; higher extinction probability reduces it. Non-AI P/D also increases in p because the SDF effect dominates (phi^{-gamma} term). The ratio column correctly reflects the differential. **Verified as real.**

**Exhibit verdict: PASS.** All checked cells match independent computation; monotonicity patterns are economically correct.

## Figure 2: Government Transfers and the Singularity (fig:extension-panels, page 15)

**Description.** Two-panel figure. Panel (a) shows AI stock P/D ratios vs. tax rate tau for two scenarios: Baseline (eta=0.5, phi=0.5) and Large singularity (eta=9, phi=0.05). Panel (b) shows household consumption growth in the singularity state vs. tax rate tau for the same two scenarios. Parameters: alpha=0.70, p=0.5%, xi=5%, delta=0.5.

### Suspicious features

1. **Panel (a): Large-singularity P/D diverges as tau approaches 0.** The annotation states "P/D -> infinity as tau -> 0." This is an extreme claim.
2. **Panel (a): The large-singularity line enters the plot area around tau ~ 5% from above the y-axis cap.** The y-axis appears truncated.
3. **Panel (b): "Catastrophe: 50% loss" annotation at tau=0 for the large singularity.** This is a specific numerical claim.
4. **Panel (b): "25% loss" annotation at tau=0 for the baseline.** Another specific numerical claim.
5. **Panel (b): "1.1x" at tau=30% and "1.3x" at tau=50% annotations for baseline.** Specific numerical claims.

### Code check

1. **P/D divergence.** Re-ran `compute_pd_with_transfer` for large singularity (eta=9, phi=0.05) at small tau values. The function returns NA (divergent) for tau <= 1%, and finite values starting around tau=5% (P/D=16.1). At phi=0.05, phi^{-gamma} = 0.05^{-4} = 160,000, which makes the SDF weighting enormous unless transfers cushion displacement. The divergence is a real economic feature of the model when the existence condition (A^j < 1) is violated. **Verified as real.** Code: `generate-exhibits.R:151-181`.
2. **Y-axis truncation.** The code computes `y_cap_a = ceiling(baseline_max_a)`. Baseline P/D at tau=0 is 15.0, so y_cap_a = 15. Large singularity P/D at tau=5% is 16.1, which exceeds the cap and is clipped. The annotation at exit_tau correctly marks where the line enters the visible region. **Verified as intentional truncation with annotation.**
3. **50% loss.** `consumption_growth(0, 9.0, 0.05) = 0.05 * (1+9) = 0.50`, i.e., 50% of pre-singularity consumption. Loss = 1 - 0.50 = 50%. The annotation `round((1 - cons_large_0) * 100)` correctly produces "50". **Verified.**
4. **25% loss.** `consumption_growth(0, 0.5, 0.50) = 0.50 * (1+0.5) = 0.75`, i.e., 75% of pre-singularity consumption. Loss = 1 - 0.75 = 25%. The annotation `round((1 - cons_base_0) * 100)` correctly produces "25". **Verified.**
5. **1.1x and 1.3x.** `consumption_growth(0.30, 0.5, 0.50) = 1.105`, which `sprintf("%.1f", ...)` formats as "1.1". `consumption_growth(0.50, 0.5, 0.50) = 1.272`, formatted as "1.3". **Verified.**

**Exhibit verdict: PASS.** All annotations and plotted features match independent computation; the P/D divergence is a genuine model property.
