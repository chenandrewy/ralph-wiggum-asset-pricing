# tests/factcheck-exhibits.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 5m 8s
[ralph-garage/agent-logs/20260411T214322.784596-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T214322.784596-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated; suspicious features traced to code and verified as real.

## Figure 1: Valuation Ratios and the AI Premium (`fig:ai-valuations`)

**Description.** Two-panel time-series figure. Panel (a) plots the S&P 500 trailing price-dividend ratio from the Shiller dataset, 2000–present. Panel (b) plots the NASDAQ Composite / S&P 500 price ratio, normalized to January 2015 = 100.

### Suspicious features

1. **P/D levels appear very high (reaching ~75–80).** A trailing P/D of 75–80 implies a dividend yield of ~1.3%, which is plausible for the recent S&P 500. Not an error.

2. **Sharp spike and drop in Panel (b) around 2000.** The NASDAQ/S&P ratio peaked during the dot-com bubble, then collapsed. This is the expected empirical pattern.

3. **No local data cache.** The code downloads live from datahub.io (Shiller) and FRED (NASDAQCOM). There are no cached CSVs in `/workspace/data/` to verify exact plotted values against.

### Code check

- **P/D computation** (`generate-exhibits.R:308–311`): `PD = SP500 / Dividend` where `Dividend` is the Shiller dataset's trailing 12-month dividend. This is the standard trailing P/D ratio. Correct.
- **NASDAQ/S&P normalization** (`generate-exhibits.R:382–383`): Finds the observation closest to 2015-01-01, divides all ratios by that value, multiplies by 100. The reference line at 100 (`geom_hline(yintercept = 100)`) confirms. Correct.
- **Date filtering** (`generate-exhibits.R:369`): `filter(Date >= as.Date("2000-01-01"))` restricts both panels to post-2000. Consistent with visible x-axis range.
- **Data sources match caption**: Caption says "NASDAQ from FRED; S&P 500 from the Shiller dataset." Code uses `download_fred("NASDAQCOM")` and `read.csv("https://datahub.io/core/s-and-p-500/r/data.csv")`. Consistent.
- **No local data concern**: The lack of a local data cache means the exact plotted values cannot be independently verified from local files. However, the code logic is correct, the data sources are standard and authoritative, and the visual patterns match known market history (dot-com bubble, post-GFC recovery, recent AI-driven surge). This is not a failure.

**Exhibit verdict: PASS** — Code logic is correct; visual patterns match known empirical facts; data sources are standard.

## Table 1: Price-Dividend Ratios (`tab:pd-ratios`)

**Description.** Grid of P/D ratios for AI stocks and non-AI stocks across 5 singularity probabilities (p = 0.1%–1.0%) and 4 extinction probabilities (ξ = 0%–20%). Parameters: β = 0.96, g = 0.02, γ = 4, φ = 0.5, η = 0.5, θ = 0.15, Δθ = 0.2.

### Suspicious features

1. **AI P/D jumps sharply from 15.5 (p = 0.5%) to 26.5 (p = 1.0%) at ξ = 0%.** This is a 70% increase for a doubling of singularity probability. Could indicate nonlinear amplification or a coding error.

2. **All ratios in the ξ = 0% column for p ≤ 0.2% are 1.1, suggesting near-zero AI premium at low probabilities.** Could indicate insufficient numerical precision or a regime where the model barely distinguishes AI from non-AI.

3. **Non-AI P/D also increases with p (from 9.8 to 13.3).** This is potentially counterintuitive—why would non-AI stocks gain from higher singularity probability?

### Code check

- **Numerical verification**: All 20 table entries were independently recomputed from the R code formulas. Every value matches the generated LaTeX table to one decimal place. No rounding errors or discrepancies.

- **Feature 1 (nonlinear AI P/D growth)**: The AI P/D uses exact backward recursion over a chain of 60 post-singularity theta values (`compute_pd_ai_exact`, lines 51–80). The AI dividend growth factor at θ = 0.15 is (0.15 + 0.20 × 0.85)/0.15 × 1.5 = 2.2. The SDF weight is φ^(−γ) × (1+η)^(−γ) = 0.5^(−4) × 1.5^(−4) = 16 × 0.198 = 3.16. As p increases, the term p × (1−ξ) × S × Γ grows, and the P/D formula K/(1−K) is convex in K, producing the observed nonlinearity. Correct.

- **Feature 2 (low premium at small p)**: At p = 0.1%, the singularity term contributes only 0.001 × 3.16 × 2.2 ≈ 0.007 to K, compared to the no-singularity term (1−p) × B ≈ 0.904. The AI and non-AI dividend growth factors differ by a factor of 2.2/1.2 ≈ 1.83, but this difference is multiplied by only 0.001, making the premium negligible. The ratio rounds to 1.1 at one decimal place. Correct.

- **Feature 3 (non-AI P/D increases with p)**: The non-AI dividend growth factor γ_non = share_ratio_non × (1+η) = (0.68/0.85) × 1.5 = 1.2. The SDF-weighted singularity payoff for non-AI is S × 1.2 = 3.16 × 1.2 = 3.79, which exceeds 1. This means the singularity state adds value to non-AI stocks despite share dilution, because the SDF spike (marginal utility is high when displacement occurs) more than compensates for the dividend share loss. This is economically sensible: households value consumption in the high-marginal-utility displacement state, so even a modest non-AI dividend in that state is priced at a premium. Correct.

- **Parameter footnote** matches code: β = 0.96, g = 0.02, γ = 4, φ = 0.5, η = 0.5, θ = 0.15, Δθ = 0.2. Verified at `generate-exhibits.R:18–24`.

- **In-text claims verified**:
  - "P/D of about 15.5" at p = 0.5%, ξ = 0%: table shows 15.5. ✓
  - "non-AI stocks trade near 11": table shows 11.1. ✓
  - "ratio of about 1.4": table shows 1.4. ✓
  - "At p = 1%, the ratio rises to 2": table shows 2.0. ✓
  - "1.3 to 2 times" across 0.5–1% range: ratios span 1.3–2.0. ✓

**Exhibit verdict: PASS** — All values independently verified; suspicious features explained by correct model mechanics.

## Figure 2: Government Transfers and the Singularity (`fig:extension-panels`)

**Description.** Two-panel figure. Panel (a) plots AI stock P/D ratio vs. tax rate τ for baseline (η = 0.5, φ = 0.5) and large singularity (η = 9, φ = 0.05). Panel (b) plots household consumption growth in the singularity state vs. τ on a log scale, with a reference line at 1 (no change).

### Suspicious features

1. **Panel (a): Large singularity P/D is missing/undefined at τ = 0, then drops precipitously.** The curve appears to enter from above the y-axis cap and fall steeply. This could be an error or a genuine divergence.

2. **Panel (a): The annotation "P/D → ∞ as τ → 0" is a strong claim.** Needs verification that the pricing kernel truly diverges.

3. **Panel (b): Large singularity consumption growth at τ = 0 is labeled as a "50% loss" (catastrophe annotation).** Needs verification.

4. **Panel (b): The large singularity curve rises extremely steeply, reaching values well above 1 at small τ.** The log-scale y-axis may obscure how rapidly consumption growth increases.

### Code check

- **Feature 1 (P/D divergence at τ = 0)**: At τ = 0, φ_eff = φ_large = 0.05. The SDF component is φ_eff^(−γ) = 0.05^(−4) = 160,000. The pricing kernel factor K = B × [(1−p) + p(1−ξ) × S × Γ_AI] where S = 160,000 × 10^(−4) = 16 and Γ_AI = 21.33. This gives K = 0.905 × [0.995 + 0.005 × 0.95 × 16 × 21.33] ≈ 0.905 × [0.995 + 1.621] = 0.905 × 2.616 ≈ 2.37. Since K > 1, the P/D sum diverges. The code returns NA in this case (`generate-exhibits.R:169`). The curve begins at the first τ where K < 1, which is around τ ≈ 0.05–0.06. Correct.

- **Feature 2 (annotation placement)**: The annotation is placed at `x = exit_tau + 0.01`, where `exit_tau` is the minimum τ at which `pd_ai <= y_cap_a` for the large singularity. This correctly marks where the curve enters the visible plot region. The claim "P/D → ∞ as τ → 0" is supported by the K > 1 divergence. The paper text (line 269) explains: "the existence condition in Remark 1 is violated because the household's marginal utility in the singularity state (φ^{−γ} = 160,000) is so extreme that the pricing sum diverges." Numerically verified: 0.05^(−4) = 160,000. Correct.

- **Feature 3 (50% loss annotation)**: `cons_large_0 = phi_large × (1 + eta_large) = 0.05 × 10 = 0.5`. The code computes `round((1 − 0.5) × 100) = 50`, producing the "50% loss" label. For baseline: `cons_base_0 = 0.5 × 1.5 = 0.75`, giving `round((1 − 0.75) × 100) = 25`, producing "25% loss". Both match the paper text claim "consumption halves under the large singularity" and "falls by 25% under the baseline." Correct.

- **Feature 4 (steep rise in consumption growth)**: The consumption growth formula (`generate-exhibits.R:146`) is `φ(1+η) + τ(1−δτ)(1−φα₀)/α₀ × (1+η)`. For the large singularity, the transfer term coefficient is (1−0.05×0.70)/0.70 × 10 ≈ 13.8. At τ = 0.10: growth = 0.5 + 0.10 × 0.95 × 13.8 = 0.5 + 1.31 = 1.81. At τ = 0.20: growth = 0.5 + 0.20 × 0.90 × 13.8 = 0.5 + 2.48 = 2.98. The steep rise is correct because (1+η) = 10 amplifies the transfer term enormously. The log scale appropriately displays this range. Correct.

- **Parameters match caption and code**: α = 0.70 (`alpha0`), p = 0.5% (`p_ext = 0.005`), ξ = 5% (`xi_ext = 0.05`), δ = 0.5 (`delta = 0.50`). All verified.

- **Baseline P/D values verified**: P/D at τ = 0 is 15.0, decreasing monotonically to ~9.7 at τ = 0.40. Large singularity P/D starts at NA (infinite), first finite at ~16 around τ = 0.05, dropping to ~9 by τ = 0.20. All consistent with visible figure.

**Exhibit verdict: PASS** — All suspicious features verified as correct model behavior; code logic and parameter values confirmed.
