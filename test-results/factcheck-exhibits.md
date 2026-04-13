# tests/factcheck-exhibits.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 3m 48s
[ralph-garage/agent-logs/20260412T200023.660687-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T200023.660687-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and data; no artifacts or errors found.

## Figure 1: Valuation Ratios and the AI Premium (fig:ai-valuations, page 2)

**Description.** Two-panel figure. Panel (a) shows the S&P 500 trailing price-dividend ratio from ~2000–2025 using the Shiller dataset. Panel (b) shows the NASDAQ Composite price relative to the S&P 500, normalized to January 2015 = 100, using NASDAQ data from FRED.

### Suspicious features

1. **P/D ratio reaches ~80 in recent years.** A trailing P/D of ~80 implies a dividend yield of ~1.25%, which is plausible for the S&P 500 in 2024–2025.
2. **NASDAQ/S&P ratio spike in 2000 and again post-2020.** The dot-com peak and the recent AI-driven surge are well-documented market phenomena.

### Code check

- Panel (a) computes `PD = SP500 / Dividend` from the Shiller dataset downloaded from datahub.io (`code/generate-exhibits.R:323`). The Dividend field is the trailing 12-month dividend. The filter restricts to 2000–2025. No transformations beyond the ratio are applied. **Correct.**
- Panel (b) downloads NASDAQ from FRED (`NASDAQCOM`), merges with S&P 500 monthly data, computes `Ratio = NASDAQ / SP500`, and normalizes to Jan 2015 = 100 (`code/generate-exhibits.R:396–397`). The normalization divides by the ratio value closest to 2015-01-01 and multiplies by 100. **Correct.**
- Both panels use standard, reputable data sources (Shiller dataset, FRED). No suspicious data manipulations.

**Exhibit verdict: PASS** — Data sourced from standard references, computations are straightforward ratios, and visible features reflect known market patterns.

## Table 1: Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks (tab:pd-ratios, page 9)

**Description.** Grid of model-implied P/D ratios for AI and non-AI stocks across singularity probabilities p ∈ {0.1%, 0.2%, 0.5%, 0.8%, 1.0%} and extinction probabilities ξ ∈ {0%, 5%, 10%, 20%}. Parameters: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2.

### Suspicious features

1. **AI P/D ratio of 26.5 at p=1%, ξ=0% is more than double the non-AI ratio of 13.3.** This is the paper's central quantitative claim.
2. **Monotonic patterns: AI and non-AI P/D both increase in p and decrease in ξ.** Could indicate a coding error if the economics don't support it.

### Code check

- Non-AI P/D uses closed-form `compute_pd_approx` (`code/generate-exhibits.R:40–46`). I independently recomputed: at p=0.5%/ξ=0%, K=0.9173 → P/D=11.1; at p=1%/ξ=0%, K=0.9299 → P/D=13.3; at p=0.1%/ξ=0%, P/D=9.8. **All match the table.**
- AI P/D uses exact backward recursion `compute_pd_ai_exact` (`code/generate-exhibits.R:51–80`) over a chain of 60 post-singularity theta values. I re-ran the function and confirmed: p=0.5%/ξ=0% → 15.5; p=1%/ξ=0% → 26.5; p=0.1%/ξ=0% → 10.4; p=1%/ξ=20% → 20.5. **All match.**
- Ratios at p=0.5%/ξ=0%: 15.5/11.1=1.4; at p=1%/ξ=0%: 26.5/13.3=2.0. **Match the table.**
- Monotonicity is economically correct: higher p increases expected singularity-state dividends (raising both P/D ratios, AI more so due to hedging); higher ξ reduces the weight on non-extinction states (lowering both, AI more so).
- Table footnote parameters match code globals exactly (`code/generate-exhibits.R:18–24`). **Correct.**

**Exhibit verdict: PASS** — All values independently verified against the generating code; monotonicity patterns are economically justified.

## Figure 2: Government Transfers and the Singularity (fig:extension-panels, page 15)

**Description.** Two-panel figure. Panel (a) shows AI stock P/D ratios vs. tax rate τ for baseline (η=0.5, φ=0.5) and large singularity (η=9, φ=0.05). Panel (b) shows household consumption growth in the singularity state vs. τ for both scenarios, with a log-scaled y-axis.

### Suspicious features

1. **Panel (a): Large singularity P/D is infinite at low τ and drops abruptly to finite values.** The annotation states "P/D → ∞ as τ → 0."
2. **Panel (b): Large singularity consumption growth starts at 0.5 (catastrophe) and rises steeply.** The annotation says "50% loss."
3. **Panel (b): Baseline consumption growth starts at 0.75 with annotation "25% loss."**
4. **Panel (a) x-axis goes to 40% while Panel (b) goes to 50%.** Different axis ranges between panels.

### Code check

1. **Infinite P/D at low τ.** At τ=0: φ_large^(−γ) = 0.05^(−4) = 160,000 (`code/generate-exhibits.R:25`). The existence condition parameter K = β(1+g)^(1−γ)[(1−p) + p(1−ξ)·S·Γ^AI] exceeds 1 when S = φ_eff^(−γ)(1+η)^(−γ) is large. I verified: K=2.37 at τ=0 (diverges); K drops below 1 at τ≈0.04, where finite P/D ratios emerge. The function `compute_pd_with_transfer` (`code/generate-exhibits.R:151–181`) returns NA when K≥1, so the line simply doesn't appear at low τ. The annotation is added via `annotate()` at line 242. **Correct and consistent with Remark 1 in the paper.**

2. **Consumption at τ=0.** `consumption_growth(0, 9, 0.05)` = 0.05×10 = 0.5 (`code/generate-exhibits.R:145–147`). Annotation computes `round((1−0.5)×100) = 50`. **Matches "50% loss."** Similarly, `consumption_growth(0, 0.5, 0.5)` = 0.5×1.5 = 0.75 → 25% loss. **Correct.**

3. **Baseline annotations at τ=0.30 and τ=0.50.** I verified: consumption_growth(0.30, 0.5, 0.5) = 1.1; consumption_growth(0.50, 0.5, 0.5) = 1.3. Code formats these as "1.1×" and "1.3×" via `sprintf("%.1f", ...)` at lines 275, 279. **Match the visible annotations.**

4. **Different x-axis ranges.** Panel (a) uses `limits = c(0, 0.40)` and Panel (b) uses `limits = c(0, 0.50)` — both are explicitly set in the code (lines 240, 285) and clearly labeled in the rendered figure. This is a deliberate design choice, not an error.

5. **Parameter verification.** Caption states α=0.70, p=0.5%, ξ=5%, δ=0.5. Code: `alpha0=0.70`, `p_ext=0.005`, `xi_ext=0.05`, `delta=0.50`. Legend labels "Baseline (η=0.5, φ=0.5)" and "Large singularity (η=9, φ=0.05)" match `scenario_labels` at lines 212–215, which in turn match the `eta_val`/`phi_val` assignments at lines 193–194. **All consistent.**

**Exhibit verdict: PASS** — Infinite-to-finite P/D transition verified via existence condition; consumption growth values confirmed analytically; all parameters match between code, caption, and legend.
