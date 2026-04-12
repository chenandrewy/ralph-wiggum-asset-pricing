# tests/factcheck-exhibits.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 4m 2s
[ralph-garage/agent-logs/20260412T095842.945482-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T095842.945482-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits verified against generating code and local computations; no artifacts, errors, or unsupported features found.

## Figure 1: Valuation Ratios and the AI Premium (fig:ai-valuations)

**Description:** Two-panel figure. Panel (a) shows the S&P 500 trailing price-dividend ratio from the Shiller dataset (2000–present). Panel (b) shows the NASDAQ Composite price relative to the S&P 500, normalized to January 2015 = 100.

### Suspicious features

1. **Dot-com spike in Panel (b) around 2000:** The NASDAQ/S&P ratio shows a very high value (~140–150) at the start of the sample before crashing. This is a large swing.
2. **Sharp post-2020 rise in Panel (b):** The ratio climbs steeply from ~100 to ~140+ after 2020.
3. **Panel (a) P/D spike around 2002 and volatile behavior:** The P/D ratio shows extreme volatility near 2001–2003 and 2008–2009.

### Code check

1. **Dot-com spike:** The code downloads NASDAQ (FRED series NASDAQCOM) and S&P 500 (Shiller dataset), computes their price ratio, and normalizes to Jan 2015 = 100. The NASDAQ peaked at roughly 2.5× the S&P 500 level in March 2000 relative to 2015, so a value of ~140–150 is consistent with the dot-com bubble. This is real.
2. **Post-2020 rise:** Reflects the actual NASDAQ outperformance driven by tech/AI stocks. Consistent with publicly known market data. Real.
3. **P/D volatility:** The Shiller dataset computes P/D as price divided by trailing 12-month dividends. During recessions (2001, 2008–09), prices fell while dividends lagged, creating spikes and drops. The code correctly computes `SP500 / Dividend` and filters for `Dividend > 0`. This is real market behavior, not an artifact.

**Caption check:** Caption correctly states sources (NASDAQ from FRED; S&P 500 from Shiller), normalization base (Jan 2015 = 100), and panel descriptions match the code. Verified.

**Exhibit verdict: PASS** — All visible features reflect real market data downloaded from standard sources, processed correctly by the code.

---

## Table 1: Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks (tab:pd-ratios)

**Description:** Grid of P/D ratios for AI and non-AI stocks across singularity probability p (0.1%–1.0%) and extinction probability ξ (0%–20%). Parameters: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2.

### Suspicious features

1. **AI P/D ratio reaches 26.5 at p=1%, ξ=0%:** This is 2.0× the non-AI ratio. A factor-of-two premium seems large.
2. **All ratios in the "Ratio" column round to one decimal and are modest (1.1–2.0):** Could indicate rounding masking divergence or issues.
3. **Non-AI P/D ratios also increase with p:** Non-AI stocks benefit from singularity (they get aggregate consumption growth η), so rising P/D with p is expected but worth checking.

### Code check

1. **AI P/D = 26.5 at p=1%, ξ=0%:** Independently recomputed using the exact backward-recursion algorithm (`compute_pd_ai_exact`). Result: 26.5. The code iterates over 60 steps of the theta chain, which is more than sufficient for convergence (theta approaches 1 geometrically). The large premium reflects the hedging value of AI stocks: they pay more in the high-marginal-utility singularity state. Verified as correct.
2. **Rounded ratios:** Recomputation confirms all 20 cells match the table to one decimal place. No masking of divergence — the ratios are genuinely moderate because both AI and non-AI stocks benefit from the singularity-state consumption growth.
3. **Non-AI P/D rising with p:** The non-AI dividend growth factor γ_non = (1 − θ − Δθ(1−θ))/(1−θ) × (1+η) = 0.8 × 1.5 = 1.2. Combined with φ^(−γ) = 16 (high marginal utility in singularity), the SDF-weighted dividend growth is large enough to raise valuations. Correct economic logic.

**Caption check:** All stated parameters match the code. The footnote correctly describes the computation method (exact iteration over Euler equation). Verified.

**Exhibit verdict: PASS** — All 20 cells independently verified; economic logic is sound; caption parameters match code.

---

## Figure 2: Government Transfers and the Singularity (fig:extension-panels)

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratios vs. tax rate τ for two scenarios: Baseline (η=0.5, φ=0.5) and Large singularity (η=9, φ=0.05). Panel (b) shows household consumption growth in the singularity state vs. tax rate τ, with a log-scale y-axis.

### Suspicious features

1. **Large singularity line in Panel (a) is undefined for low τ, then drops rapidly from very high values:** The line appears only for τ ≥ ~3% and starts near the top of the chart, falling steeply.
2. **Annotation "P/D → ∞ as τ → 0" in Panel (a):** Claims P/D diverges at zero tax rate for the large singularity.
3. **Panel (b) "Catastrophe: 50% loss" annotation at τ=0 for large singularity:** The consumption growth at τ=0 is labeled as a 50% loss.
4. **Panel (b) baseline "25% loss" annotation at τ=0:** The baseline consumption growth at τ=0 is labeled as a 25% loss.
5. **Panel (b) baseline annotations "1.1×" at τ=30% and "1.3×" at τ=50%:** Numeric consumption multipliers annotated on the baseline curve.
6. **Large singularity line in Panel (b) rises extremely steeply:** From 0.5 at τ=0 to above 5.0 at τ=50%, suggesting massive consumption gains from small tax rates.
7. **Paper body text claims φ^(−γ) = 160,000:** This drives the divergence of P/D.

### Code check

1. **P/D undefined at low τ:** Recomputed: P/D is NA for τ = 0.00, 0.01, 0.02, and first becomes finite at τ = 0.03 (P/D ≈ 66.4). The code uses `compute_pd_with_transfer` with exact backward recursion. At τ=0 with φ=0.05 and η=9, φ_eff^(−γ) = 160,000 and (1+η)^(−γ) = 10^(−4), giving S=16. Combined with the large dividend growth factor (~21.3), the Euler sum diverges (K ≈ 2.37 > 1). The y-axis is capped at ceiling(baseline_max) = 16, so the large singularity line enters the visible range at ~τ=0.03 with very high values falling to ~9 by τ=0.15. Verified as correct.
2. **"P/D → ∞" annotation:** Justified by the divergence calculation above. The existence condition is violated when K ≥ 1. Correct.
3. **50% loss:** cons_growth(0, 9, 0.05) = 0.05 × 10 = 0.5. Loss = 1 − 0.5 = 50%. `round((1 - 0.5) * 100) = 50`. Correct.
4. **25% loss:** cons_growth(0, 0.5, 0.5) = 0.5 × 1.5 = 0.75. Loss = 1 − 0.75 = 25%. `round((1 - 0.75) * 100) = 25`. Correct.
5. **Baseline annotations:** cons_growth(0.30, 0.5, 0.5) = 0.75 + 0.30 × 0.85 × 0.65/0.70 × 1.5 = 1.1 (verified: sprintf gives "1.1"). cons_growth(0.50, 0.5, 0.5) = 0.75 + 0.50 × 0.75 × 0.65/0.70 × 1.5 = 1.3 (verified: sprintf gives "1.3"). Correct.
6. **Steep large singularity curve in Panel (b):** With η=9, (1+η)=10, so even a small tax raises enormous revenue from the explosive output growth. cons_growth(0.10, 9, 0.05) = 0.5 + 0.10 × 0.95 × 0.965/0.70 × 10 ≈ 1.81. The steep rise is real and economically meaningful: explosive output growth makes redistribution highly effective despite deadweight costs. Verified.
7. **φ^(−γ) = 160,000:** 0.05^(−4) = 1/(0.05^4) = 1/0.00000625 = 160,000. Correct.

**Caption check:** Caption states α=0.70, p=0.5%, ξ=5%, δ=0.5. Code uses alpha0=0.70, p_ext=0.005 (0.5%), xi_ext=0.05 (5%), delta=0.50. All match. Legend labels correctly show scenario parameters. Verified.

**Exhibit verdict: PASS** — All suspicious features traced to code and verified as correct; divergence behavior, annotations, and parameter values all confirmed.
