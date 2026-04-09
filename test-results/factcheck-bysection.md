# tests/factcheck-bysection.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 8m 6s
[ralph-garage/agent-logs/20260409T184838.289841-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T184838.289841-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct and all verbal claims are supported; a few minor language imprecisions exist but no claim is materially wrong.

## Introduction (lines 37–71)

- **Line 37** — section header
- **Line 39** [FIGURE/TABLE] OK — Figure 1 is generated from illustrative P/E data in `generate-exhibits.R`; the caption labels it "Illustrative" and the text says "based on approximate values from public sources." The gap widening post-2023 is visible in the data (AI P/E rises from 42.0 to 75.0 vs. S&P 500 from 19.2 to 22.5).
- **Line 48** [VERBAL] OK — "AI stocks serve as a hedge against displacement" is supported by Proposition 1 (lines 122–134): Γ^AI > Γ^N combined with high household marginal utility in singularity states creates the hedging channel (line 166).
- **Line 48** [VERBAL] OK — "If markets were complete, investors could insure directly" is supported by Proposition 3(ii) (line 248) and Discussion (line 197).
- **Line 48** [REFERENCE] OK — Attribution to GKP2012 for market incompleteness and displacement risk is consistent with the paper's treatment throughout (lines 63, 195–197).
- **Line 50** [VERBAL] OK — Model description (representative household, stochastic singularity, two public assets) matches Section 2.1 (lines 76–107).
- **Line 50** [REFERENCE] OK — Jones2024 extinction risk matches Section 2.1 (line 96).
- **Line 50** [VERBAL] OK — "closed-form price-dividend ratios" confirmed by Proposition 1.
- **Line 52** [VERBAL] OK — Three stated contributions (discrete singularity, extinction interaction, policy implications) correspond to baseline model, Proposition 2(iii), and Section 4.2.
- **Line 54** [REFERENCE] OK — "positive singularity is most likely" matches λ > 1/2 assumption in Extension 1 (line 233); veto result matches Proposition 3(i) (line 247); complete markets result matches Proposition 3(ii) (line 248).
- **Line 54** [VERBAL] OK — "Both extensions branch directly off the baseline" is accurate; Extensions 1 and 2 do not stack.
- **Line 56** [ARITHMETIC] OK (borderline) — "up to roughly six times higher": the maximum P/D ratio in Table 1 is 5.8 (at p=1%, ξ=0%). "Roughly six" is a defensible approximation of 5.8. The phrasing "six times higher" in strict English implies ratio = 7, but colloquial usage means ratio ≈ 6. The Quantitative Analysis section (line 213) correctly says "nearly 6 to 1."
- **Line 56** [REFERENCE] OK — "Proposition 2(iii) shows extinction risk attenuates this gap" is confirmed: the proposition states both spread and ratio decrease in ξ, verified numerically (ratio falls from 5.8 to 4.3 to 3.5 to 2.6 as ξ rises from 0% to 20% at p=1%).
- **Line 58** [VERBAL] OK — "AI agents produced all analysis and writing; human contributed only economic specification and test scripts" matches spec requirement IV.4.c.
- **Line 63** [REFERENCE] OK — GKP2012 characterization ("innovation displaces existing agents, creates systematic risk factor under incomplete markets") is internally consistent with the paper's treatment in Section 2.3.
- **Line 63** [VERBAL] OK — "simplifies their overlapping-generations structure" is consistent with Section 2.1 (line 76): "we do not explicitly model the entry of new cohorts."
- **Line 65** [REFERENCE] OK — Jones2024 characterization (trade-off between AI growth and existential risk, bounded utility) is consistent with the paper's usage throughout.
- **Line 65** [VERBAL] OK — "extinction risk interacts with displacement in a countervailing way, attenuating rather than amplifying" is confirmed by Proposition 2(iii).
- **Lines 67** [REFERENCE] OK — Literature citations (Kogan-Papanikolaou 2014, Kogan-Papanikolaou-Stoffman 2020, Barro 2006, Wachter 2013, Garleanu-Panageas 2015, Korinek-Suh 2024, Acemoglu 2024) are characterized in plausible and standard ways for the finance/macro literature. Cannot independently verify characterizations without reading the papers.

## Model (lines 72–201)

- **Line 72** — section header
- **Line 76** [DEFINITION] OK — Representative household as marginal investor, AI owners holding private capital, analogy to GKP2012 future owners.
- **Line 76** [VERBAL] OK — "we do not explicitly model the entry of new cohorts of firms or workers" is a clear and accurate disclaimer.
- **Lines 79–83** [DEFINITION] OK — Eq. (1): C_{t+1} = (1+g)C_t. Consistently used in the proof (line 146).
- **Line 85** [DEFINITION] OK — α_t ∈ (0, 1−θ_t], c_t^H = α_t C_t, AI owners get (1−α_t)C_t. Upper bound ensures non-negative private AI residual.
- **Line 91** [DEFINITION] OK (minor ambiguity) — "aggregate consumption jumps by a factor 1+η" in the singularity period. The proof (line 147) uses c_{t+1}^H/c_t^H = φ(1+g)(1+η), implying both η and g apply simultaneously. The (1+g) factors cancel in the Euler equation, so the derivation is unaffected; the ambiguity is presentational only.
- **Lines 93–95** [DEFINITION] OK — Eq. (2): α_{t+1} = φα_t, φ ∈ (0,1). Consistently used throughout.
- **Line 96** [REFERENCE] OK — Extinction following Jones2024 is correctly modeled as C_{t+1} = 0 for all subsequent dates.
- **Line 105** [DEFINITION] OK — θ_{t+1} = θ_t + Δθ(1−θ_t) upon non-extinction singularity. Verified: with θ=0.15, Δθ=0.20, new θ = 0.15 + 0.20 × 0.85 = 0.32.
- **Line 106** [DEFINITION] OK — D_t^N = (1−θ_t)C_t. Public dividends sum to C_t.
- **Line 109** [ARITHMETIC] OK — Private AI capital dividends = (1−α_t)C_t − θ_t C_t = (1−α_t−θ_t)C_t ≥ 0 by the constraint α_t ≤ 1−θ_t.
- **Line 112** [DEFINITION] OK — CRRA with γ > 1 and β ∈ (0,1). The γ > 1 restriction is used at line 244 (u(c) < 0 for γ > 1) and in Proposition 2(ii).
- **Lines 125–133** [ARITHMETIC] OK — P/D formulas verified. Γ^AI = (0.15 + 0.2×0.85)/0.15 × 1.5 = 0.32/0.15 × 1.5 = 3.2. Γ^N = (0.85 − 0.17)/0.85 × 1.5 = 0.68/0.85 × 1.5 = 1.2. Cross-check: θΓ^AI + (1−θ)Γ^N = 0.15×3.2 + 0.85×1.2 = 0.48 + 1.02 = 1.50 = 1+η. ✓
- **Lines 143–148** [ARITHMETIC] OK — Three consumption growth cases correctly derived: no singularity (1+g), non-extinction singularity (φ(1+g)(1+η)), extinction (0). Dividend growth cases match.
- **Lines 152–155** [ARITHMETIC] OK — Euler equation expansion correct. SDF × dividend growth factors properly combined.
- **Line 157** [VERBAL] OK — Stationarity approximation (post-singularity P/D ≈ v^AI) is explicitly stated as an approximation, not hidden.
- **Lines 159–161** [ARITHMETIC] OK — Solving v = K(v+1) gives v = K/(1−K). Matches eqs. (6)–(7).
- **Line 163** [VERBAL] OK — Non-AI derivation is identical by symmetry, replacing Γ^AI with Γ^N.
- **Line 166** [VERBAL] OK — Hedging channel: household consumption falls in singularity (φ(1+η) = 0.75 < 1 with baseline parameters) while AI dividends grow (Γ^AI = 3.2 > 1). High marginal utility × high payoff → premium. Supported by the math.
- **Line 166** [ARITHMETIC] OK — "φ(1+η) < 1 when φ is sufficiently small": with φ=0.5, η=0.5, φ(1+η) = 0.75 < 1. ✓
- **Lines 168–174** [ARITHMETIC] OK — Corollary 1: K/(1−K) is increasing in K; K is increasing in Γ^j; Δθ > 0 ⟹ Γ^AI > Γ^N ⟹ P/D^AI > P/D^N. Proof correct.
- **Line 179** [VERBAL] OK — Prop. 2(i): spread increasing in displacement severity (decreasing in φ). Verified: smaller φ raises φ^{-γ}, amplifying the singularity term more for AI (larger Γ^AI).
- **Line 180** [VERBAL] OK — Prop. 2(ii): spread increasing in p for γ sufficiently large. The qualifier is conservative (numerically the spread is monotone in p for all tested γ) but mathematically correct.
- **Lines 181–182** [VERBAL] OK — Prop. 2(iii): both spread and ratio decrease in ξ. Verified numerically: at p=1%, ratio goes 5.8 → 4.3 → 3.5 → 2.6 as ξ goes 0% → 5% → 10% → 20%.
- **Lines 186–191** [VERBAL] OK — Proof sketches for all three parts are logically sound and consistent with the formulas.
- **Line 195** [REFERENCE] OK — GKP2012 characterization ("growth stocks earn lower expected returns because they hedge displacement risk") is internally consistent with the paper's discussion. Cannot independently verify against GKP without reading their paper.
- **Line 197** [VERBAL] OK — "If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk, and the valuation spread would collapse." Follows directly from the model structure.

## Quantitative Analysis (lines 202–219)

- **Line 202** — section header
- **Line 204** [ASSUMPTION] OK — Parameters β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2 match the R code (lines 18–24 of `generate-exhibits.R`) and the table footnote exactly.
- **Line 204** [ARITHMETIC] OK — "φ(1+η) = 0.75 and household consumption falls by 25%": 0.5 × 1.5 = 0.75; 1 − 0.75 = 0.25. ✓
- **Line 204** [ARITHMETIC] OK — "η = 0.5 (aggregate consumption rises by 50% in a singularity)": 0.5 = 50%. ✓
- **Line 204** [ASSUMPTION] OK — "θ = 0.15 (AI stocks are initially 15% of the economy)" and "Δθ = 0.2 (AI's share jumps by 20% of the non-AI remainder)": match code and table footnote.
- **Lines 206–211** [FIGURE/TABLE] OK — Table generated by `generate-exhibits.R`. All values independently verified by recomputing K = β(1+g)^{1−γ} × [(1−p) + p(1−ξ)(1+η)^{−γ}φ^{−γ}Γ^j], P/D = K/(1−K).
  - Spot checks: p=0.5%/ξ=0: AI=17.5, Non-AI=11.1, Ratio=1.6 ✓; p=1%/ξ=0: AI=76.4, Non-AI=13.3, Ratio=5.8 ✓; p=0.5%/ξ=5%: AI=16.7, Non-AI=11.0, Ratio=1.5 ✓.
- **Line 213** [ARITHMETIC] OK — "AI stocks trade at a P/D of roughly 18" for p=0.5%/ξ=0: table value is 17.5, "roughly 18" is a fair description.
- **Line 213** [ARITHMETIC] OK — "non-AI stocks trade near 11": table value is 11.1. ✓
- **Line 213** [ARITHMETIC] OK — "a ratio of about 1.6": table value is 1.6. ✓
- **Line 213** [ARITHMETIC] OK (borderline) — "At p=1%, the ratio rises to nearly 6 to 1": table value is 5.8. "Nearly 6" is a mild overstatement of 5.8 but within normal rounding tolerance for "nearly."
- **Line 213** [REFERENCE] OK — "Proposition 2(iii) predicts" extinction risk reduces both valuations and compresses the premium. Confirmed by the proposition statement (lines 181–182) and verified numerically in the table.
- **Line 215** [VERBAL] OK (soft) — "Leading AI firms have traded at P/E ratios two to five times the market average in recent years." The paper's own illustrative figure data shows a maximum aggregate ratio of ~3.3× (75/22.5 in 2025). However, the text refers to "leading AI firms" (individual companies), not the aggregate basket plotted in the figure, and individual firms like NVIDIA have at times traded at P/E ratios exceeding 5× the market. The claim is labeled as empirical context with no formal citation, and the figure is labeled "Illustrative."
- **Line 215** [VERBAL] OK — "(P/E ratios proxy for P/D ratios here)": standard and reasonable in asset pricing.
- **Line 215** [ARITHMETIC] OK — "aligns with our model's predictions for annual singularity probabilities in the 0.5–1% range": model ratios span 1.6 (p=0.5%) to 5.8 (p=1%), which overlaps with the stated "two to five times" empirical range.

## Extensions: Market Incompleteness and the Singularity (lines 220–293)

- **Line 220** — section header
- **Line 222** [VERBAL] OK — Framing ("distorts development" and "government policy") accurately previews Extensions 1 and 2.

### Extension 1: Veto and Efficient Development (lines 224–258)

- **Lines 226–231** [DEFINITION] OK — Two-outcome non-extinction singularity (positive with probability λ, negative with probability 1−λ) is clearly defined.
- **Line 233** [ASSUMPTION] OK — λ > 1/2 is stated as an assumption ensuring social efficiency.
- **Lines 237–242, Eq. (10)** [ARITHMETIC] OK — Veto gain formula verified from first principles. The (1−p) no-singularity states cancel, leaving ΔU^H = p(1−ξ)[λu(φ⁺α(1+η)(1+g)C_t) + (1−λ)u(φα(1+η)(1+g)C_t)] − p u(α(1+g)C_t). Matches the paper exactly.
- **Line 244** [ARITHMETIC] OK — "u(c) < 0 for all c > 0 when γ > 1": for CRRA u(c) = c^{1−γ}/(1−γ), when γ > 1, (1−γ) < 0 and c^{1−γ} > 0, so u(c) < 0. ✓
- **Line 244** [VERBAL] OK — Normalizing u_ext = 0 is "conservative" because u(c) < 0 means extinction (utility 0) is treated as better than any finite positive consumption, making the veto result harder to obtain. ✓
- **Line 247** [VERBAL] OK — Proposition 3(i): for γ sufficiently large, household vetoes even when development is socially efficient. Verified numerically (at γ=10, λ=0.6, φ=0.5, φ⁺=1.5: ΔU^H < 0).
- **Line 248** [VERBAL] OK — Proposition 3(ii): under complete markets, household never vetoes socially efficient development. Standard result: hedged household captures social surplus. ✓
- **Line 258** [VERBAL] OK — Extinction risk interaction: under u_ext = 0, higher ξ reduces veto incentive (fewer non-extinction states to worry about); under more severe extinction penalty, higher ξ would amplify it. Directional reasoning correct.

### Extension 2: Government Transfers (lines 260–289)

- **Line 262** [REFERENCE] OK — Attribution to GKP2012 for intergenerational transfers is plausible and internally consistent.
- **Line 264** [DEFINITION] OK — Deadweight cost δ₀τ of the transferred amount. Verified: net transfer fraction = τ(1−δ₀τ), so deadweight fraction = δ₀τ.
- **Lines 266–268, Eq. (11)** [ARITHMETIC] OK — c^H_post = φα(1+η)C_t(1+g) + τ(1−δ₀τ)(1−φα)(1+η)C_t(1+g). First term: displaced household income. Second term: net transfer = tax rate × (1 − deadweight) × AI owners' post-singularity income (1−φα)(1+η)C_t(1+g). Correct.
- **Lines 274–276, Eq. (12)** [ARITHMETIC] OK — Ratio = c^H_post / c^H_no-transfer = 1 + τ(1−δ₀τ)(1−φα)/(φα). The (1+η), C_t, and (1+g) terms cancel completely. ✓
- **Line 272** [VERBAL] OK — "Independent of the productivity jump η": confirmed algebraically; η cancels in the ratio. ✓
- **Line 276** [VERBAL] OK — "exceeds one whenever τ > 0": ratio = 1 + positive term. ✓
- **Line 278** [VERBAL] OK — "both c^H_post and c^H_no-transfer grow without bound" as η grows: both scale with (1+η). ✓
- **Line 280** [ASSUMPTION] OK — Figure parameters: p=0.5%, ξ=5%. Match R code (p_ext=0.005, xi_ext=0.05).
- **Line 280** [ASSUMPTION] OK — Baseline: η=0.5, φ=0.5; large singularity: η=9, φ=0.05. Match R code.
- **Line 280** [ARITHMETIC] OK — "consumption halves under the large singularity (φ(1+η) = 0.5)": 0.05 × 10 = 0.5. ✓
- **Line 280** [ARITHMETIC] OK — "falls by 25% under the baseline (φ(1+η) = 0.75)": 0.5 × 1.5 = 0.75. ✓
- **Line 280** [VERBAL] OK — "the large singularity responds dramatically" to transfers: verified from code. At τ=0, large-singularity consumption growth = 0.5; at τ=0.3, ~4.0; at τ=0.7, ~6.8. Baseline rises only from 0.75 to ~1.38.
- **Line 280** [FIGURE/TABLE] OK — Left panel: "transfers reduce the hedge value of AI stocks, compressing P/D ratios." Verified from code: large-singularity P/D falls from ~45 to ~9 as τ rises from ~5% to ~20%.
- **Line 289** [REFERENCE] OK — Citations to Jones2024 and Nordhaus2021 for "explosive output growth" are standard references in the AI growth literature.

## Conclusion (lines 294–299)

- **Line 294** — section header
- **Line 296** [VERBAL] OK — "AI stocks trade at high valuations": supported by Figure 1 and introduction (line 39).
- **Line 296** [VERBAL] OK — "part of this premium reflects a hedging motive": supported by Proposition 1 and the hedging channel discussion (line 166).
- **Line 296** [VERBAL] OK — "requires market incompleteness—the inability to trade private AI capital": supported by lines 109–110, 197, and Proposition 3(ii).
- **Line 296** [VERBAL] OK — "attenuated by extinction risk, which reduces the weight on non-extinction states": supported by Proposition 2(iii) (lines 181–182), verified numerically.
- **Line 296** [VERBAL] OK — "risk-averse households may inefficiently block AI development": supported by Proposition 3(i) (line 247). "May" correctly reflects the conditionality (γ sufficiently large).
- **Line 296** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough to overwhelm deadweight costs": supported by Extension 2 (lines 260–289). Minor imprecision: the transfer ratio (eq. 12) is independent of η, so transfers are always beneficial in singularity states. The argument is about consumption levels relative to the pre-singularity baseline growing with η, consistent with the paper's own rhetoric (lines 278–279, 289).
- **Lines 298–299** [VERBAL] OK — Scope statement; no factual claims to verify.
