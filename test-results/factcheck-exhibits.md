# tests/factcheck-exhibits.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 3m 53s
[ralph-garage/agent-logs/20260410T225642.505749-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260410T225642.505749-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and consistent with their captions, parameters, and underlying data sources.

## Figure 1: AI Valuations vs. Broader Market (fig:ai-valuations)

**Description:** Monthly closing prices for the NASDAQ Composite (solid) and S&P 500 (dashed), normalized to January 2015 = 100. Shows the NASDAQ diverging sharply above the S&P 500, especially post-2023.

### Suspicious features

1. **NASDAQ labeled "AI/Tech-Heavy":** NASDAQ is a broad index containing many non-AI firms. However, the caption explicitly qualifies it as "heavily weighted toward AI and technology firms," which is a standard characterization, not a factual claim about index composition.

2. **No local data cache:** The code downloads data at runtime from FRED (NASDAQCOM) and datahub.io (Shiller S&P 500 dataset). No cached data exists under `/workspace/data/`. The exact plotted values cannot be verified from local files alone.

### Code check

- The download, filtering (2015–2025), monthly aggregation (`to_monthly`), normalization (`normalize` to earliest common month = 100), and plotting logic are all straightforward and correct (lines 309–383).
- The visual output is consistent with known market data: NASDAQ roughly quintupled and S&P roughly tripled from 2015 to early 2025, with COVID crash visible around 2020 and sharp AI-driven divergence post-2023.
- Caption sources ("NASDAQ from FRED; S&P 500 from the Shiller dataset") match the code's data sources exactly.

**Exhibit verdict: PASS** — Code logic is correct; visual output is consistent with known market data; caption accurately describes sources and methodology. The absence of a local cache is noted but does not constitute an error.

## Table 1: Price-Dividend Ratios (tab:pd-ratios)

**Description:** P/D ratios for AI stocks and Non-AI stocks across singularity probability p (0.1%–1.0%) and extinction probability ξ (0%–20%), with their ratio.

### Suspicious features

1. **Non-AI P/D increases with p:** At first glance, it seems counterintuitive that non-AI stock valuations rise with singularity probability. However, this is correct: with γ=4 and φ=0.5, the SDF in the singularity state is φ^(−4)·(1+η)^(−4) = 16 × 0.198 = 3.16. The non-AI dividend growth factor is (1−Δθ)·(1+η) = 0.8 × 1.5 = 1.2. The SDF-weighted dividend contribution 3.16 × 1.2 = 3.79 > 1, so singularity states add substantial risk-adjusted value even for non-AI stocks because marginal utility is very high when the household is displaced.

2. **AI P/D reaches 26.5 at p=1%, ξ=0% (ratio 2.0):** Verified by spot-checking the code. The AI dividend growth factor at θ=0.15 is (0.15+0.17)/0.15 × 1.5 = 3.2, much larger than Non-AI's 1.2, explaining the widening ratio.

### Code check

- Non-AI P/D uses a closed-form (`compute_pd_approx`, line 40–46). This is exact because the non-AI share ratio (1−Δθ) = 0.8 is independent of θ, so P/D is unchanged across singularities.
- AI P/D uses backward recursion over the θ chain (`compute_pd_ai_exact`, lines 51–79), correctly iterating 60 post-singularity states. The footnote accurately describes this as "numerically exact."
- Spot-checked three values against independent R computation: Non-AI P/D at (p=1%, ξ=0%) = 13.3 ✓, (p=0.5%, ξ=5%) = 11.0 ✓, (p=0.1%, ξ=0%) = 9.8 ✓.
- Parameters in table footnote (β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2) match code exactly (lines 18–24).

**Exhibit verdict: PASS** — All values verified; economic logic is correct; footnote accurately describes methodology and parameters.

## Figure 2: Extension Panels (fig:extension-panels)

**Description:** Two panels showing the effect of government transfers (tax rate τ). Panel (a): AI stock P/D ratio vs. τ for baseline (η=0.5, φ=0.5) and large singularity (η=9, φ=0.05). Panel (b): Household consumption growth in the singularity state vs. τ, with log-scale y-axis.

### Suspicious features

1. **Large singularity P/D → ∞ as τ → 0 (Panel a):** The line starts very high and is clipped at y=17. With φ_large=0.05 and η=9, the SDF contribution is 0.05^(−4) × 10^(−4) = 16, and the AI dividend growth factor is ~21.3 at θ=0.15. The resulting K-like term in the recursion approaches or exceeds 1, producing divergent P/D. This is consistent with Remark in the paper about A^j ≥ 1 causing infinite prices. The annotation is correct.

2. **Baseline P/D at τ=0 should match Table 1:** At p=0.5%, ξ=5%, Table 1 shows AI P/D = 15.0. The baseline line in Panel (a) starts at approximately 15 at τ=0. Consistent.

3. **Catastrophe annotations in Panel (b):** At τ=0, baseline consumption growth = φ(1+η) = 0.5×1.5 = 0.75 (25% loss); large singularity = 0.05×10 = 0.5 (50% loss). Both verified by independent computation. Annotations match exactly.

4. **Panel (a) x-axis limited to 40% while Panel (b) extends to ~70%:** This is deliberate — Panel (a) uses `limits = c(0, 0.40)` (line 238) to focus on the region where the P/D divergence is most dramatic, while Panel (b) shows the full tau_grid range to display the consumption crossover clearly.

### Code check

- `compute_pd_with_transfer` (lines 151–181) correctly modifies φ_eff to incorporate transfers: φ_eff = φ + τ(1−δτ)(1−φα₀)/α₀. This increases effective consumption share, reducing the SDF and thereby P/D.
- `consumption_growth` (lines 145–147) correctly computes post-singularity household consumption ratio with deadweight costs via pmax(0, 1−δτ).
- Caption parameters (α=0.70, p=0.5%, ξ=5%, δ=0.5) match code values exactly: alpha0=0.70 (line 140), p_ext=0.005 (line 183), xi_ext=0.05 (line 184), delta=0.50 (line 141).
- The φ_large=0.05 comment (line 25) correctly notes φ_large×(1+9)=0.5, matching the 50% loss annotation.

**Exhibit verdict: PASS** — All features verified against code and parameters; annotations are numerically correct; Panel (a) baseline P/D is consistent with Table 1.
