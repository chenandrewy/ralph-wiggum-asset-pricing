# tests/factcheck-exhibits.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 3m 52s
[ralph-garage/agent-logs/20260409T220435.847828-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T220435.847828-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and consistent with the paper's claims; no artifacts or errors found.

## Figure 1: Valuations of AI-Exposed Stocks vs. the Broader Market

**Description:** A time-series plot showing monthly closing prices for the NASDAQ Composite (solid blue) and S&P 500 (dashed red) from 2015 to ~2025, each normalized to January 2015 = 100.

### Suspicious features

1. **Sharp divergence starting ~2023.** The NASDAQ line rises steeply relative to the S&P 500 around 2023–2024, with NASDAQ reaching roughly 5× its 2015 level while S&P reaches roughly 3×.
2. **COVID dip ~2020.** Both series show a visible dip around early 2020.

### Code check

1. **Sharp divergence:** The code downloads real market data from FRED (NASDAQ) and the Shiller/datahub dataset (S&P 500). The post-2023 divergence reflects the actual AI/tech boom in public markets. Both series are normalized to first-common-month = 100 (`normalize()` at line 354). The NASDAQ ending near 500 and S&P near 300 is consistent with actual market performance over this period. **Verified as real.**
2. **COVID dip:** Real market event (March 2020 crash). Both indices fell sharply before recovering. **Verified as real.**

**Exhibit verdict: PASS** — Data is downloaded from authoritative external sources (FRED, Shiller dataset), normalization logic is correct, labels and caption match the code.

## Table 1: Price-Dividend Ratios — AI Stocks vs. Non-AI Stocks

**Description:** A grid of model-implied P/D ratios for AI and non-AI stocks across five singularity probabilities (p = 0.1% to 1.0%) and four extinction probabilities (ξ = 0% to 20%). Parameters: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2.

### Suspicious features

1. **AI P/D at p=1%, ξ=0% is 26.5, much higher than the rest of the table.** This could be an artifact of the recursion diverging.
2. **Non-AI P/D varies little across ξ at low p.** At p=0.1%, non-AI P/D ranges from 9.7 to 9.8 — nearly flat.

### Code check

1. **High AI P/D at p=1%, ξ=0%:** Manual verification of the non-AI closed-form formula confirms the non-AI value (13.3) is correct: K = β(1+g)^(1−γ) × [(1−p) + p(1−ξ)S·Γ^N] ≈ 0.9046 × 1.0280 = 0.9299, yielding P/D = 0.9299/0.0701 ≈ 13.3. The AI exact recursion (`compute_pd_ai_exact`, lines 51–80) iterates backward over 60 post-singularity theta states. At high p, AI's dividend growth multiplier (Γ^AI ≈ 3.2 at θ₀=0.15 vs Γ^N ≈ 1.2) amplifies the option value, producing legitimately high P/D. The ratio of 2.0 is economically sensible: higher singularity probability means AI stocks' hedging value is more frequently realized. **Verified as correct.**

2. **Flat non-AI P/D at low p:** At p=0.1%, the singularity-related term p(1−ξ)S·Γ^N contributes only ~0.0038 to K, so varying ξ from 0% to 20% changes K by ~0.0008, producing negligible variation in P/D. This is mathematically correct — extinction risk is essentially irrelevant at very low singularity probabilities. **Verified as correct.**

**Exhibit verdict: PASS** — Spot-checked entries match manual calculations; monotonicity patterns (increasing in p, decreasing in ξ) are economically correct; the exact backward-recursion code for AI stocks is properly implemented; table footnote accurately describes the method.

## Figure 2: Government Transfers and the Singularity

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratios vs. tax rate τ (0–40%) for baseline (η=0.5, φ=0.5) and large-singularity (η=9, φ=0.05) scenarios. Panel (b) shows household consumption growth in the singularity state vs. τ (0–70%) on a log scale, with annotations marking the catastrophic losses at τ=0.

### Suspicious features

1. **Panel (a): The large-singularity line appears to start from the upper boundary of the chart, with an annotation "P/D → ∞ as τ → 0".** This suggests the P/D is undefined at τ=0 for the large singularity.
2. **Panel (b): The large-singularity line starts very low (~0.5) and rises steeply, crossing the baseline line.** The crossover and steep rise could be artifacts.
3. **Panel (b): Annotation says "Catastrophe: 50% loss" at τ=0 for large singularity and "25% loss" for baseline.**

### Code check

1. **P/D undefined at τ=0 for large singularity:** At τ=0, φ_eff = φ_large = 0.05. The SDF factor S = 0.05^(−4) × 10^(−4) = 160,000 × 0.0001 = 16. The terminal K_term = B × [(1−p) + p(1−ξ)·S·Γ_term] with Γ_term ≈ 10 gives K_term = 0.9046 × (0.995 + 0.005 × 0.95 × 16 × 10) = 0.9046 × 1.755 ≈ 1.59 > 1, so the function correctly returns NA. The annotation and paper text (line 250: "the existence condition in Remark 1 is violated because φ^(−γ) = 160,000") are consistent. **Verified as correct.**

2. **Steep rise of large-singularity consumption:** `consumption_growth(τ, 9, 0.05)` = 0.05×10 + τ(1−0.5τ)(1−0.035)/0.70 × 10 = 0.5 + τ(1−0.5τ)×13.79. At τ=0.5: 0.5 + 0.5×0.75×13.79 = 0.5 + 5.17 = 5.67. The large-singularity curve rises far faster than baseline because the transfer base scales with (1+η)=10. The crossover is real: at low τ, baseline starts higher (0.75 vs 0.5), but the large-singularity curve's slope is ~10× steeper. **Verified as correct.**

3. **Catastrophe annotations:** At τ=0: cons_large_0 = φ_large×(1+η) = 0.05×10 = 0.5 → 50% loss. cons_base_0 = φ×(1+η) = 0.5×1.5 = 0.75 → 25% loss. Both annotations match the code output exactly. **Verified as correct.**

**Exhibit verdict: PASS** — The P/D divergence at τ=0 for large singularity is a genuine mathematical feature (K>1), not an artifact; consumption growth formulas produce correct values at boundary cases; annotations match computed quantities; caption parameters (α=0.70, p=0.5%, ξ=5%, δ=0.5) match the code (p_ext=0.005, xi_ext=0.05, alpha0=0.70, delta=0.50).
