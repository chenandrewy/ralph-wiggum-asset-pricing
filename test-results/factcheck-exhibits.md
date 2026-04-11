# tests/factcheck-exhibits.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 3m 9s
[ralph-garage/agent-logs/20260411T103039.134728-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T103039.134728-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and data, with no artifacts, labeling errors, or unsupported features.

## Figure 1: AI Valuations vs. the Broader Market (fig:ai-valuations, page 2)

**Description:** Time-series plot of monthly NASDAQ Composite (solid blue) and S&P 500 (dashed red), normalized to January 2015 = 100, running through approximately mid-2025. NASDAQ dramatically outpaces S&P 500, with the gap widening sharply after ~2023.

### Suspicious features

1. **Sharp dip around early 2020** followed by rapid recovery in both series.
2. **Accelerating divergence post-2023**, with NASDAQ reaching ~500 while S&P stays ~300.

### Code check

1. The 2020 dip is the COVID-19 market crash — this is real market data downloaded from FRED (NASDAQ) and the Shiller/datahub dataset (S&P 500). The code at lines 311–368 downloads monthly closing prices and normalizes to the first common month. No transformation or smoothing is applied that could create artificial dips.

2. The post-2023 divergence reflects actual market performance during the generative AI boom. The code applies no artificial manipulation — it downloads raw price series, takes the last observation per month (`slice_tail(n=1)`), and normalizes. The pattern is consistent with widely reported market data.

**Caption check:** Caption states "NASDAQ Composite (solid)" and "S&P 500 (dashed)," matching `scale_linetype_manual` at line 375–376. Sources stated as "NASDAQ from FRED; S&P 500 from the Shiller dataset," matching the code's `download_fred("NASDAQCOM")` and `read.csv("https://datahub.io/core/s-and-p-500/r/data.csv")`. Normalization to "January 2015 = 100" matches the `normalize()` function applied after filtering to dates ≥ 2015-01-01.

**Exhibit verdict: PASS** — Real market data, correctly downloaded, transformed, and labeled.

## Table 1: Price-Dividend Ratios (tab:pd-ratios, page 9)

**Description:** Grid of P/D ratios for AI stocks and non-AI stocks across singularity probabilities p ∈ {0.1%, 0.2%, 0.5%, 0.8%, 1.0%} and extinction probabilities ξ ∈ {0%, 5%, 10%, 20%}. The ratio column shows AI P/D divided by non-AI P/D.

### Suspicious features

1. **Monotonic increase in AI P/D with p** — could indicate the model is well-behaved or could mask an error if the relationship should be non-monotonic.
2. **AI P/D of 26.5 at p=1%, ξ=0%** — a large value that could indicate a near-divergence.
3. **Ratio column values** — must equal pd_ai/pd_non rounded to 1 decimal.

### Code check

1. Verified by independent computation: `compute_pd_ai_exact(0.005, 0, 0.15, 0.20) = 15.49` → rounds to 15.5 (table: 15.5 ✓); `compute_pd_ai_exact(0.01, 0, 0.15, 0.20) = 26.52` → rounds to 26.5 (table: 26.5 ✓); `compute_pd_approx(0.005, 0, gamma_non) = 11.09` → rounds to 11.1 (table: 11.1 ✓). The backward-recursion algorithm at lines 51–79 is mathematically correct for iterating the Euler equation over the chain of post-singularity theta values.

2. The large value at p=1% reflects the model's hedging channel: as p increases, more probability weight is placed on singularity states where AI stocks hedge displacement. The existence condition A^j < 1 is satisfied: at p=0.01, ξ=0, A^AI ≈ 0.964 < 1.

3. Ratio column spot-checks: 15.5/11.1 = 1.396 → 1.4 (table: 1.4 ✓); 26.5/13.3 = 1.992 → 2.0 (table: 2.0 ✓); 24.8/12.9 = 1.922 → 1.9 (table: 1.9 ✓).

**Parameter check:** Table footnote states β=0.96, g=0.02, γ=4, ϕ=0.5, η=0.5, θ=0.15, Δθ=0.2. Code at lines 18–24 sets identical values.

**Exhibit verdict: PASS** — All values verified by independent recomputation; parameters, labels, and formatting are correct.

## Figure 2: Government Transfers and the Singularity (fig:extension-panels, page 14)

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate τ for baseline (η=0.5, ϕ=0.5, red solid) and large singularity (η=9, ϕ=0.05, blue dashed) scenarios. Panel (b) shows household consumption growth in the singularity state vs. τ on a log scale, with a dotted "no change" line at y=1.

### Suspicious features

1. **Large-singularity P/D missing at low τ in Panel (a)** — the line only appears above ~5% tax rate, with an annotation "P/D → ∞ as τ → 0."
2. **Catastrophe markers at τ=0 in Panel (b)** — annotations claim "50% loss" for large singularity and "25% loss" for baseline.
3. **Dramatic divergence between scenarios in Panel (b)** — the large singularity consumption growth rises much faster than baseline.

### Code check

1. **P/D divergence verified.** At τ=0 with large-singularity parameters (ϕ=0.05, η=9), the existence condition gives A^AI = 2.37 >> 1, so P/D is undefined (infinite hedging demand). The code's `compute_pd_with_transfer()` returns NA when the condition fails. At τ=0.05, ϕ_eff=0.117 and A^AI=0.949 < 1, restoring existence. This matches the visible entry point of the blue line in Panel (a) around τ ≈ 5%. The annotation is correct.

2. **Catastrophe values verified.** Baseline: ϕ(1+η) = 0.5×1.5 = 0.75, a 25% loss ✓. Large singularity: ϕ_large(1+η_large) = 0.05×10 = 0.50, a 50% loss ✓. Code at line 252–253 computes these identically.

3. **Divergence explained.** The consumption growth formula (line 145–147) is `phi*(1+eta) + tau*(1-delta*tau)*(1-phi*alpha)/alpha*(1+eta)`. For large singularity, the (1+η) factor is 10, amplifying the transfer term by 10× compared to baseline's 1.5. Additionally, (1-ϕ·α)/α = (1-0.035)/0.70 = 1.379 for large singularity vs. (1-0.35)/0.70 = 0.929 for baseline. This ~15× difference in the slope coefficient explains the dramatic divergence.

**Caption/parameter check:** Caption states α=0.70, p=0.5%, ξ=5%, δ=0.5. Code at lines 138–184 sets alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50. Match confirmed.

**Exhibit verdict: PASS** — All suspicious features are real, correctly generated, and consistent with the model mechanics.
