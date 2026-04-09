# tests/factcheck-exhibits.py
Started: 2026-04-09 19:33:01 EDT
Runtime: 4m 37s
[ralph-garage/agent-logs/20260409T193302.025679-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T193302.025679-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated; suspicious features trace to valid code logic and match the paper's claims.

## Figure 1 (fig:ai-valuations): Valuations of AI-Exposed Stocks vs. the Broader Market

**Description:** Time-series plot showing monthly closing prices for the NASDAQ Composite (solid blue) and S&P 500 (dashed red), normalized to January 2015 = 100, from approximately 2015 to 2025. The NASDAQ dramatically outpaces the S&P 500, with the gap widening sharply after 2023.

### Suspicious features

1. **NASDAQ reaches ~400–500 range (4–5× appreciation).** The NASDAQ appears to roughly quadruple or more over the period. This is a large move but plausible: NASDAQ went from ~5,000 in Jan 2015 to ~18,000+ by late 2024.
2. **No local data cache to verify exact plotted values.** The code downloads data at runtime from FRED (NASDAQCOM) and datahub (Shiller S&P 500) with no local cache.

### Code check

- The code (`code/generate-exhibits.R`, lines 217–288) downloads monthly data from two sources, aligns date ranges, normalizes to the first common month = 100, and plots. The logic is straightforward and correct.
- The caption states "Sources: NASDAQ from FRED; S&P 500 from the Shiller dataset" which matches the code's data sources (lines 233–243).
- The y-axis label "Normalized Price (Jan 2015 = 100)" matches the normalization logic: both series are filtered to start at 2015-01-01, and the first common month is used as the base (line 262–268).
- No suspicious visual artifacts (no discontinuities, implausible spikes, or labeling mismatches). The COVID dip in 2020 and post-2023 AI divergence are expected real-world features.
- While no local data cache exists, the absence of suspicious features means there is nothing requiring local verification beyond the code logic, which is correct.

**Exhibit verdict: PASS** — Code logic is correct; data sources match the caption; no suspicious visual features identified.

## Table 1 (tab:pd-ratios): Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks

**Description:** Grid of P/D ratios for AI and non-AI stocks across five singularity probabilities (p = 0.1% to 1.0%) and four extinction probabilities (ξ = 0% to 20%). Parameters: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2.

### Suspicious features

1. **Extreme AI P/D at p=1%, ξ=0% (76.4).** This is roughly 5.8× the non-AI P/D of 13.3. The value is unusually high for a P/D ratio.
2. **Non-AI P/D barely moves across p (9.7–13.3) while AI P/D explodes (10.2–76.4).** The asymmetry is striking.
3. **Ratios at p=0.2% are displayed as 1.1 for ξ=5%, 10%, 20%.** This collapses three potentially distinct ratios to the same displayed value.

### Code check

1. **P/D = 76.4 at p=1%, ξ=0%:** Manual computation confirms K_ai = 0.9046 × (0.99 + 0.01 × 10.114) = 0.9871, giving P/D = 0.9871/0.0129 = 76.5 ≈ 76.4. The K value approaches 1, causing the P/D to explode. This is the expected behavior from the Euler equation: as singularity probability rises, the high marginal-utility-weighted AI dividend growth pushes K toward 1. **Verified as correct.**
2. **Asymmetry between AI and non-AI:** The SDF-weighted dividend growth in the singularity is sdf_sing_ai = 10.11 vs. sdf_sing_non = 3.79. AI stocks have nearly 3× the singularity contribution because share_ratio_ai (2.13) >> share_ratio_non (0.80). The asymmetry is an intended model feature. **Verified as correct.**
3. **Ratio rounding at p=0.2%:** At ξ=5%, pd_ai/pd_non = 11.5/10.0 = 1.15, which rounds to 1.1 or 1.2 depending on floating-point representation. R's `sprintf("%.1f", ...)` rounds 1.15 to "1.1" due to IEEE 754 representation (1.15 is stored as 1.14999...). Similarly at ξ=10%: 11.4/10.0 = 1.14 → "1.1", and ξ=20%: 11.1/9.9 = 1.1212 → "1.1". These are standard rounding artifacts, not errors. **Verified as correct.**

Additional spot-checks:
- p=0.5%, ξ=0%: K_ai = 0.9046 × 1.04557 = 0.9458 → P/D = 17.5 ✓; K_non = 0.9046 × 1.01396 = 0.9173 → P/D = 11.1 ✓; Ratio = 1.58 → 1.6 ✓
- p=0.8%, ξ=10%: K_ai = 0.9046 × 1.06482 = 0.9633 → P/D = 26.2 ✓; K_non = 0.9046 × 1.01931 = 0.9221 → P/D = 11.8 ✓; Ratio = 2.2 ✓

**Exhibit verdict: PASS** — All values verified against the code's formulas; extreme values are a correct consequence of the model's Euler equation as K → 1.

## Figure 2 (fig:extension-panels): Government Transfers and the Singularity

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate τ for two scenarios (Baseline: η=0.5, φ=0.5; Large singularity: η=9, φ=0.05). Panel (b) shows household consumption growth in the singularity state vs. τ for the same scenarios. Parameters: p=0.5%, ξ=5%, δ₀=0.5.

### Suspicious features

1. **Panel (a): Large-singularity P/D is undefined (missing) at τ=0 and appears only for τ > ~3–5%.** The line starts abruptly at a high P/D and drops steeply.
2. **Panel (b): Large-singularity consumption growth starts at 0.5 (50% loss) and rises dramatically, far exceeding the baseline.** At τ=50%, it appears to reach ~5–6.
3. **Panel (a) x-axis limited to 40% while Panel (b) extends to ~70%.** Different ranges for the same variable could be misleading.
4. **Panel (b): "Catastrophe: 50% loss" annotation at τ=0 for large singularity.** Need to verify.

### Code check

1. **Large-singularity P/D undefined at τ=0:** With φ=0.05, γ=4: φ^(-γ) = 160,000. The SDF contribution: K = 0.9046 × (0.995 + 0.00475 × 160,000 × 10^(-4) × 21.333) = 0.9046 × 2.616 = 2.37 > 1, so K ≥ 1 and P/D is NA. The code returns NA when K ≥ 1 (line 46). As τ increases, φ_eff grows, φ_eff^(-γ) shrinks, and K drops below 1 around τ ≈ 3.5%. **Verified as correct.** The paper explicitly discusses this: "the P/D ratio is undefined at τ=0: the existence condition... is violated because the household's marginal utility in the singularity state (φ^{−γ} = 160,000) is so extreme."
2. **Large-singularity consumption growth:** At τ=0: consumption_growth(0, 9, 0.05) = 0.05 × 10 = 0.5 ✓. At τ=0.5: = 0.5 + 0.5 × 0.75 × (1−0.035)/0.70 × 10 = 0.5 + 5.17 = 5.67, consistent with the figure. The code formula (line 114) matches equation (4) in the paper. **Verified as correct.**
3. **Different x-axis ranges:** Panel (a) is limited to τ ≤ 0.40 (line 167) because P/D ratios become very low and uninteresting beyond 40%. Panel (b) shows the full range to 70% to display the consumption story. Both axes are labeled clearly. This is a presentation choice, not an error. **Not a failure.**
4. **"Catastrophe: 50% loss" annotation:** cons_large_0 = 0.05 × 10 = 0.5; round((1−0.5)×100) = 50 → "50% loss". For baseline: cons_base_0 = 0.5 × 1.5 = 0.75; round((1−0.75)×100) = 25 → "25% loss". Both match the paper's text: "consumption halves under the large singularity (φ(1+η)=0.5) and falls by 25% under the baseline (φ(1+η)=0.75)." **Verified as correct.**

Additional check: Baseline P/D at τ=0 should match Table 1 at p=0.5%, ξ=5%. Table shows 16.7; the figure's baseline line starts at approximately 16–17. **Consistent.**

**Exhibit verdict: PASS** — All suspicious features trace to correct code logic and match the paper's analytical discussion.
