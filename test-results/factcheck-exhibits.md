# tests/factcheck-exhibits.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 3m 34s
[ralph-garage/agent-logs/20260411T100208.993077-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T100208.993077-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated and consistent with the code and parameters.

## Figure 1: AI Valuations vs. the Broader Market

Shows monthly NASDAQ Composite and S&P 500 prices normalized to January 2015 = 100. NASDAQ (solid blue) outperforms S&P 500 (dashed red), reaching roughly 450–500 by end of sample vs. ~250–280. Both series show COVID dip (2020) and 2022 drawdown, with a sharp NASDAQ uptick during the 2024–2025 AI boom.

### Suspicious features

None found. The series show plausible real-world market dynamics with no discontinuities, label mismatches, or implausible values.

### Code check

- Data sources match caption: NASDAQ from FRED (`NASDAQCOM`), S&P 500 from datahub Shiller dataset (`generate-exhibits.R:326–335`).
- Monthly aggregation uses last observation per month (`slice_tail(n=1)`), consistent with "monthly closing prices" caption.
- Normalization divides by first common month value and multiplies by 100 (`generate-exhibits.R:354–358`), matching the "Jan 2015 = 100" label.
- Legend labels ("NASDAQ Composite (AI/Tech-Heavy)", "S&P 500") and line styles (solid, dashed) match code at lines 371–374.

**Exhibit verdict: PASS** — Real data from public sources, correctly downloaded, aggregated, and labeled.

## Table 1: Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks

Shows model-implied P/D ratios for AI and non-AI stocks across annual singularity probabilities p ∈ {0.1%, 0.2%, 0.5%, 0.8%, 1.0%} and extinction probabilities ξ ∈ {0%, 5%, 10%, 20%}. AI P/D ratios range from 10.2 to 26.5; non-AI from 9.7 to 13.3; ratios from 1.1 to 2.0.

### Suspicious features

1. **All ratios ≥ 1.0**: AI stocks always command a premium. Need to verify this is a property of the model, not an error.
2. **Monotonicity in p**: Both P/D ratios increase with p. Since higher singularity probability could destroy value (via extinction), this needs checking.

### Code check

1. **AI premium (ratio ≥ 1)**: AI dividend share jumps from θ to θ + Δθ(1−θ) upon singularity, giving AI dividend growth factor γ_AI = 2.133 × 1.5 = 3.2, while non-AI gets γ_N = 0.8 × 1.5 = 1.2 (`generate-exhibits.R:34–37`). Since γ_AI > γ_N, AI stocks benefit more from the singularity state in the SDF, producing higher P/D. Correct.

2. **P/D increasing in p**: The SDF-weighted singularity payoff exceeds unity for both stock types (verified: sdf_sing for non-AI ≈ 3.79 > 1 at baseline parameters). So increasing p raises the probability-weighted contribution of a high-payoff state, increasing P/D. The net effect of extinction (which subtracts from the singularity contribution via the (1−ξ) factor) is small relative to the large SDF weight from displacement (φ^{−γ} = 16). Correct.

3. **Parameter verification**: Table footnote states β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2. Code parameters at lines 18–24 match exactly.

4. **Spot-check at p=0.1%, ξ=0%**: Manual calculation gives non-AI P/D ≈ 9.8 (K ≈ 0.9072), matching the table. AI approximate P/D ≈ 10.5; exact backward recursion yields 10.4, matching the table.

5. **Non-AI "approximate" formula is exact**: γ_N = (1−Δθ)(1+η) is independent of θ, so post-singularity non-AI P/D equals pre-singularity P/D, making the closed-form exact (`generate-exhibits.R:40–46`). Correct.

6. **AI exact computation**: Uses 60-step backward recursion over the theta chain (`generate-exhibits.R:51–80`). At large k, theta→1 and the terminal value is nearly exact. Correct methodology.

**Exhibit verdict: PASS** — Values are consistent with the model parameters, the generating code is mathematically sound, and spot checks confirm numeric accuracy.

## Figure 2: Government Transfers and the Singularity

Two-panel figure. Panel (a): AI stock P/D ratio vs. tax rate τ for baseline (η=0.5, φ=0.5) and large singularity (η=9, φ=0.05). Panel (b): Household consumption growth in singularity state vs. τ, with log-scale y-axis and a "No change" reference line at 1.

### Suspicious features

1. **Panel (a): Large-singularity line appears to diverge as τ→0**, with annotation "P/D → ∞ as τ → 0". Need to verify this is real, not a plotting artifact.
2. **Panel (a): Baseline P/D at τ=0 should be consistent with Table 1** at matching parameters (p=0.5%, ξ=5%).
3. **Panel (b): Catastrophe annotations** claim 50% loss (large singularity) and 25% loss (baseline) at τ=0. Need to verify.

### Code check

1. **P/D divergence at τ=0 for large singularity**: At τ=0, φ_eff = φ_large = 0.05. The SDF term S = 0.05^{−4} × 10^{−4} = 16. The terminal K = B × [(1−p) + p(1−ξ) × S × γ_AI_term]. With γ_AI_term ≈ 10 at theta→1, K ≈ 0.905 × [0.995 + 0.005 × 0.95 × 16 × 10] = 0.905 × 1.755 ≈ 1.59 > 1, so the terminal P/D is undefined (function returns NA at line 68–69). The code correctly drops NA values (`filter(!is.na(pd_ai))` at line 224) and places an annotation at the boundary (`generate-exhibits.R:240–242`). As τ increases slightly, φ_eff rises enough to bring K < 1, giving finite but very large P/D. **Verified: real model feature, correctly handled.**

2. **Cross-consistency with Table 1**: Table 1 at p=0.5%, ξ=5% shows AI P/D = 15.0. Panel (a) uses the same parameters (p_ext=0.005, xi_ext=0.05 at lines 183–184) and the baseline line at τ=0 starts at approximately 15 in the image. The code calls `compute_pd_with_transfer` with tau=0, which gives phi_eff=phi=0.5, equivalent to the Table 1 computation. **Consistent.**

3. **Catastrophe annotations**: At τ=0:
   - Baseline: consumption_growth = φ(1+η) = 0.5 × 1.5 = 0.75, i.e., 25% loss. ✓
   - Large singularity: consumption_growth = φ_large(1+η_large) = 0.05 × 10 = 0.5, i.e., 50% loss. ✓
   Code at `generate-exhibits.R:250–251` computes these values and the annotations at lines 258–264 display them. **Correct.**

4. **Caption parameters**: Caption states α=0.70, p=0.50%, ξ=5%, δ=0.5. Code has alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50. **Match.**

**Exhibit verdict: PASS** — Panel (a) divergence is a genuine model feature correctly annotated; consumption growth annotations verified analytically; cross-consistency with Table 1 confirmed.
