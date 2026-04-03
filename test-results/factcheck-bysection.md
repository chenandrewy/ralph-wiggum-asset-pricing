# tests/factcheck-bysection.py
Started: 2026-04-02 21:49:42 EDT
Runtime: 6m 10s
[ralph-garage/agent-logs/20260402T214942.812545-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260402T214942.812545-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct and all material claims are supported; only minor verbal imprecisions found.

## Introduction (lines 41–68)
- **Line 41** — section header
- **Line 43** [VERBAL] OK — "Between 2023 and 2025, the largest AI-related companies collectively gained trillions of dollars in market value" is a widely reported stylized fact.
- **Line 43** [VERBAL] OK — "trading at price-dividend ratios far above historical norms" consistent with Figure 1.
- **Line 43** [FIGURE/TABLE] OK — "Figure 1 illustrates this pattern using CRSP data" references the correct exhibit file (ai-valuations.pdf).
- **Line 43** [VERBAL] OK — "publicly traded AI stocks command a valuation premium because they serve as a hedge against a negative AI singularity" is the paper's thesis, supported by Propositions 1–4.
- **Line 48** [FIGURE/TABLE] OK — Caption matches spec requirement for a CRSP-based P/D ratio figure (spec II.8.b). Ticker list (NVDA, MSFT, GOOGL, META, AMZN) cannot be verified against PDF content but is consistent with the description.
- **Line 52** [VERBAL] OK — Description of singularity displacement matches Assumptions 1–2 (lines 103–109).
- **Line 52** [VERBAL] OK — "the typical investor cannot buy these assets" matches model structure (household excluded from private AI capital, line 124).
- **Line 54** [DEFINITION] OK — "infinite-horizon, discrete-time" matches model (lines 76, 121) and spec I.4.a.
- **Line 54** [DEFINITION] OK — "two publicly traded assets" matches model (lines 88–94) and spec I.4.c.
- **Line 54** [REFERENCE] OK — "following GKP2012, AI owners can be interpreted as future innovators" verified against GKP-2012-WP.md: "future cohorts of inventors... are not able to trade with the current population of agents."
- **Line 56** [VERBAL] OK — "We derive the price-dividend ratio in closed form" restates Proposition 1.
- **Line 56** [VERBAL] OK — "the ratio increases with the probability of a singularity" restates Proposition 3.
- **Line 56** [VERBAL] OK — SDF-covariance mechanism correctly described: displacement raises marginal utility, AI dividends rise, positive covariance lowers required return.
- **Line 56** [ARITHMETIC] OK — "valuation spread widens with singularity probability" confirmed by Table: spread goes from 0.0 (p=0) to 15.9 (p=0.05) monotonically.
- **Line 56** [VERBAL] OK — "Under complete markets, the hedging premium vanishes" restates Proposition 4.
- **Line 58** [REFERENCE] OK — Connection to Jones (2024) verified: Jones analyzes the trade-off between AI-driven growth and existential risk.
- **Line 58** [REFERENCE] OK — "barriers to intergenerational risk-sharing emphasized by GKP2012" verified against GKP source.
- **Line 58** [VERBAL] OK — "Even modest transfer mechanisms suffice when the surplus is enormous" matches Remark 2 (line 272–273).
- **Line 58** [VERBAL] OK — "the most extreme AI singularity reduces displacement risk" matches Remark 2.
- **Line 58** [VERBAL] OK — Extinction risk attenuation matches Section 4.1 (lines 246–250).
- **Line 60** [VERBAL] OK — "The human author contributed only the paper specification—approximately 80 lines—and the test suite." Spec file has 84 lines; "approximately 80" is accurate. Matches spec IV.5.d.
- **Line 60** [VERBAL] OK — Footnote about Claude and automated loop consistent with project infrastructure.
- **Line 63** [REFERENCE] OK — "GKP2012, who introduce displacement risk in an overlapping-generations economy with innovation" verified against GKP abstract.
- **Line 63** [REFERENCE] OK — "new entrants capture rents that existing agents cannot share" verified against GKP.
- **Line 63** [VERBAL] OK — "Our contribution relative to GKP is purposefully modest" matches spec I.6.d.
- **Line 63** [REFERENCE] OK — "KoganPapanikolaouStoffman2020 extend the displacement risk framework" — plausible description of known work; no spec file to verify further.
- **Line 63** [REFERENCE] OK — "KoganPapanikolaou2014 analyze investment-specific technology shocks" — plausible description of known work; no spec file to verify further.
- **Line 65** [VERBAL] OK — Rare disasters literature connection (Rietz 1988, Barro 2006, Wachter 2013) is standard. Sectoral asymmetry distinguishes from standard disaster models.
- **Line 67** [REFERENCE] OK — "Jones2024 shows curvature of utility is central" verified: Jones states "The curvature of utility is very important."
- **Line 67** [REFERENCE] OK — "HobijnJovanovic2001 document the negative impact of IT innovation on incumbent firms" verified against GKP's citation of same.
- **Line 67** [REFERENCE] OK — Remaining lit review citations (Korinek-Suh, Acemoglu-Restrepo, Pastor-Veronesi) have plausible descriptions consistent with common knowledge; no spec files to verify further.

## Model (lines 72–149)
- **Line 72** — section header
- **Line 74** — subsection header "Environment"
- **Line 76** [DEFINITION] OK — Discrete time, aggregate output Y_t, singularity absorbing with probability p ∈ (0,1).
- **Lines 77–79** [DEFINITION] OK — Normal growth: Y_{t+1} = (1+g) Y_t.
- **Lines 80–83** [DEFINITION] OK — Post-singularity growth: Y_{t+1} = (1+g̃) Y_t, g̃ > g.
- **Line 84** [VERBAL] OK — Forward reference to extension exploring g̃ → ∞; no constraint on g̃ in model.
- **Line 86** [VERBAL] OK — Household is marginal investor (confirmed by market clearing, line 130).
- **Line 86** [VERBAL] OK — AI owners hold private capital, do not participate in public markets.
- **Line 86** [REFERENCE] OK — GKP interpretation ("future innovators who have not yet entered the economy") verified against GKP-2012-WP.md.
- **Line 86** [VERBAL] OK — Paper correctly distinguishes its own interpretation (illiquid private AI ventures) from GKP's unborn-cohorts mechanism.
- **Line 88** — subsection header "Assets and dividends"
- **Lines 90–94** [DEFINITION] OK — Output shares θ, ν, 1−θ−ν sum to 1. Dividend definitions consistent.
- **Lines 96–99** [DEFINITION] OK — Post-singularity shares θ̃, ν̃, 1−θ̃−ν̃ sum to 1.
- **Lines 103–105** [ASSUMPTION] OK — Assumption 1: θ̃+ν̃ < θ+ν (household share falls). Correctly labeled.
- **Lines 107–109** [ASSUMPTION] OK — Assumption 2: θ̃ > θ and ν̃ < ν (AI gains, non-AI loses). Consistent with Assumption 1.
- **Lines 111–114** [DEFINITION] OK — ω ≡ θ+ν, ω̃ ≡ θ̃+ν̃, Δ ≡ ω̃/ω < 1. Inequality follows from Assumption 1.
- **Line 115** [VERBAL] OK — Correctly restates Assumption 1 in terms of Δ.
- **Line 117** — subsection header "The household's problem"
- **Lines 119–122** [DEFINITION] OK — Standard CRRA utility with γ > 1, β ∈ (0,1).
- **Lines 124–128** [DEFINITION] OK — Budget constraint is standard for two-asset economy with ex-dividend prices.
- **Line 130** [ARITHMETIC] OK — Market clearing n_t^A = n_t^N = 1 follows from representative household as sole public-market investor.
- **Lines 131–133** [ARITHMETIC] OK — c_t = D_t^A + D_t^N = (θ+ν)Y_t = ωY_t. Verified by substituting market clearing into budget constraint.
- **Line 134** [ARITHMETIC] OK — Post-singularity: c_t = (θ̃+ν̃)Y_t = ω̃Y_t.
- **Lines 136–139** [DEFINITION] OK — Standard Euler equation for CRRA preferences.
- **Line 141** — subsection header "Equilibrium"
- **Line 143** [VERBAL] OK — P/D ratios constant within each regime because growth rates are i.i.d. within regime. Correct.
- **Lines 145–147** [ASSUMPTION] OK — Existence conditions: (1−p)β(1+g)^{1−γ} < 1 and β(1+g̃)^{1−γ} < 1. These are the correct convergence conditions for the geometric series in each regime.
- **Line 149** [VERBAL] OK — "Automatically satisfied for γ > 1." Verified: for γ > 1 and g ≥ 0, (1+g)^{1−γ} ≤ 1, so β(1+g)^{1−γ} < 1 and (1−p)β(1+g)^{1−γ} < 1. Same logic for g̃. Strictly requires g ≥ 0, which is the obvious intended case. No substantive error.

## Results (lines 154–236)
- **Line 154** — section header
- **Lines 156–157** [DEFINITION] OK — Proposition 1 header; clarifies subscript convention (regime, not time).
- **Lines 158–160** [DEFINITION] OK — V_0^A formula. All table values independently recomputed and match.
- **Lines 161–163** [DEFINITION] OK — V_0^N formula, same structure with Φ^N.
- **Lines 166–170** [DEFINITION] OK — R, Φ^A, Φ^N, V_1 definitions match stated formulas exactly.
- **Line 172** [VERBAL] OK — Verbal glosses of R, Φ^A, Φ^N, V_1 are accurate.
- **Line 176** [ARITHMETIC] OK — Post-singularity Euler equation V_1 = β(1+g̃)^{1−γ}(1+V_1) solves to eq (V1). Verified: V_1 = 6.737.
- **Line 182** [ARITHMETIC] OK — No-singularity branch contributes (1−p)R(1+V_0^A); singularity branch contributes pΦ^A(1+V_1). Consumption growth correctly identified as (1+g) and Δ(1+g̃) respectively. Solving for V_0^A yields stated formula.
- **Line 185** [VERBAL] OK — Δ < 1 ⟹ Δ^{−γ} > 1 for γ > 0. AI stocks: θ̃/θ = 3 > 1. Non-AI: ν̃/ν = 0.545 < 1. All correct.
- **Line 190** [ARITHMETIC] OK — Cross-section formula V_0^A − V_0^N independently verified; matches direct subtraction to machine precision. Positivity holds since θ̃/θ − ν̃/ν = 2.455 > 0.
- **Line 195** [ARITHMETIC] OK — Φ^A − Φ^N = β Δ^{−γ}(1+g̃)^{1−γ}(θ̃/θ − ν̃/ν). Verified. Positivity argument correct.
- **Line 198** [VERBAL] OK — "Spread increases with p and with (1−Δ)." Verified: spread = pK/[1−(1−p)R] with K > 0 constant in p; ∂S/∂p = K/[1−(1−p)R]² > 0 unconditionally. Δ^{−γ} increasing in (1−Δ).
- **Lines 200–206** [ARITHMETIC] OK — Proposition 3: ∂V_0^A/∂p > 0 iff Φ^A(1+V_1) > R/(1−R). Verified in proof appendix.
- **Line 205** [ARITHMETIC] OK — R/(1−R) = V_0^A|_{p=0}. At p = 0: V_0^A = R/(1−R) = 11.940. Correct.
- **Line 205** [VERBAL] OK — Condition holds when Δ small, γ large, or θ̃/θ large. Each increases Φ^A.
- **Lines 214–228** [ARITHMETIC] OK — Proposition 4: complete-markets formula replaces Δ^{−γ} with 1. Hedging premium formula verified numerically for all p values.
- **Line 219** [ARITHMETIC] OK — Φ^{A,CM} = β(1+g̃)^{1−γ}(θ̃/θ). Correct: under complete markets, consumption growth at singularity is (1+g̃), not Δ(1+g̃).
- **Lines 220–221** [ARITHMETIC] OK — Hedging premium = p β(1+g̃)^{1−γ}(θ̃/θ)(Δ^{−γ}−1)(1+V_1)/[1−(1−p)R]. Verified numerically. Positivity holds since Δ^{−γ}−1 > 0.
- **Line 223** [VERBAL] OK — Premium increasing in p, θ̃/θ, and (1−Δ). Verified analytically.
- **Line 230** [VERBAL] OK — "Gap isolates the hedging premium. It arises entirely from the displacement channel." Correct: the only difference between V_0^A and V_0^{A,CM} is Δ^{−γ} vs. 1.
- **Line 233** [ARITHMETIC] OK — Parameters: β=0.96, γ=3, g=0.02, g̃=0.05, θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30.
- **Line 233** [ARITHMETIC] OK — ω = 0.60, ω̃ = 0.45, Δ = 0.75. Verified.
- **Line 233** [ARITHMETIC] OK — "V_0^A ≈ 16.1, V_0^N ≈ 11.6" at p = 0.01. Recomputed: 16.098 and 11.567. Correct.
- **Line 233** [ARITHMETIC] OK — "a ratio of roughly 1.4." 16.098/11.567 = 1.392 ≈ 1.4. Correct.
- **Line 233** [ARITHMETIC] OK — "Without singularity risk (p=0), both equal approximately 11.9." R/(1−R) = 11.940 ≈ 11.9. Correct.
- **Line 233** [ARITHMETIC] OK — "V_0^{A,CM} ≈ 12.9" at p = 0.01. Recomputed: 12.896. Correct.
- **Line 233** [ARITHMETIC] OK — "hedging premium of about 25%." (16.098−12.896)/12.896 = 24.8% ≈ 25%. Correct.
- **Line 235** [FIGURE/TABLE] OK — Table values independently recomputed for all 5 rows × 5 columns. All match to stated 1-decimal precision.

## Extension: Singularity, Extinction, and Frictions (lines 240–276)
- **Line 240** — section header
- **Line 242** [VERBAL] OK — "baseline model treats the singularity as a displacement event with certainty of economic survival." Accurate.
- **Line 242** [REFERENCE] OK — "drawing on Jones2024" verified against Jones-2024-AERI.md.
- **Line 246** [ASSUMPTION] OK — Extinction probability q ∈ [0,1) conditional on singularity. Clean setup.
- **Lines 247–249** [ARITHMETIC] OK — V_0^{A,q} formula: singularity term multiplied by (1−q). Verified: with prob q all output destroyed (0 contribution), with prob (1−q) normal singularity. Formula correct.
- **Line 250** [VERBAL] OK — "Extinction risk reduces the singularity-state contribution by the factor (1−q)." Direct from formula.
- **Line 250** [ARITHMETIC] OK — "In the limit q→1, the singularity contributes nothing." p(1−q)Φ^A(1+V_1)→0. Correct.
- **Line 252** [REFERENCE] OK — "Jones2024 shows that the trade-off depends critically on curvature of utility." Verified: Jones states "The curvature of utility is very important."
- **Line 252** [REFERENCE] OK — "With γ > 1, utility is bounded, and even infinite consumption generates finite utility." Verified against Jones: "These utility functions are bounded... even infinite consumption generates finite utility."
- **Line 252** [VERBAL] OK — "AI owners enjoy unbounded consumption" as g̃→∞. AI owners get (1−ω̃)Y_t, which grows without bound. Correct.
- **Line 252** [VERBAL] NOTE — "the household's consumption, though growing, remains a shrinking fraction ω̃ of total output." The fraction ω̃ is constant post-singularity, not actively shrinking. "Shrinking" is ambiguous: it could mean "reduced" (relative to pre-singularity ω) or "declining over time." The former reading is correct; the latter would be wrong. The word "remains" suggests a static state, making the "reduced" reading more natural. **Not materially wrong, but imprecise wording.**
- **Lines 254–255** [ARITHMETIC] OK — Remark 1: as g̃→∞ with γ > 1, (1+g̃)^{1−γ}→0, so Φ^A→0 and V_1→0. Verified.
- **Line 255** [ARITHMETIC] OK — "The hedging premium vanishes." Premium proportional to (1+g̃)^{1−γ}(Δ^{−γ}−1)(1+V_1) → 0. Correct.
- **Line 255** [VERBAL] OK — "marginal utility in singularity states becomes negligible because consumption is so high." Accurate economic intuition for γ > 1.
- **Line 255** [ARITHMETIC] OK — "For γ = 1 (log utility), the premium is independent of g̃." With γ = 1, (1+g̃)^0 = 1, so Φ^A and V_1 are independent of g̃. Verified.
- **Line 258** [VERBAL] OK — Analogy between Jones (curvature determines whether infinite consumption justifies existential risk) and this paper (curvature determines whether extreme growth sustains hedging premium). Accurate.
- **Line 262** [REFERENCE] OK — "GKP assume intergenerational risk-sharing fails due to frictions." Verified: GKP states "future innovators, who are yet to enter the economy, are not able to trade with the current population of agents."
- **Line 262** [REFERENCE] OK — "GKP discuss mechanisms such as bequests, government debt, and intergenerational transfers." Verified: GKP mentions "bequests and gifts across generations, government debt, intergenerational transfers mandated by the government."
- **Line 262** [REFERENCE] OK — "in a representative dynasty with perfect altruism the displacement factor equals one." Verified against GKP footnote 14.
- **Line 262** [REFERENCE] OK — "but do not conduct a formal analysis of how these mechanisms scale with output." Verified: GKP only mentions these in passing and leaves such extensions for future work.
- **Line 264** [ARITHMETIC] OK — "With no transfers, Δ = ω̃/ω < 1." Matches eq (5), line 113.
- **Line 264** [ARITHMETIC] OK — "With full transfers, Δ = 1 and the hedging premium vanishes." From Prop 4: premium proportional to (Δ^{−γ}−1) = 0 when Δ = 1.
- **Lines 266–269** [ARITHMETIC] OK — Friction cost formula: [F + τ(ω−ω̃)Y]/Y = F/Y + τ(ω−ω̃). Algebra verified. F/Y → 0 as Y → ∞.
- **Line 270** [ARITHMETIC] OK — "AI owners' gains are (1−ω̃)Y − (1−ω)Y = (ω−ω̃)Y." Verified: pre-singularity share (1−ω), post (1−ω̃), gain = (ω−ω̃)Y since ω > ω̃.
- **Line 270** [VERBAL] OK — If τ is small relative to gains, net surplus positive and efficient outcome attainable. Cost/gain ratio is τ < 1.
- **Lines 272–273** [ARITHMETIC] OK — Remark 2: Y→∞ makes F/Y→0. Coase theorem applies when transaction costs negligible.
- **Line 273** [VERBAL] OK — "hedging premium is largest for moderate singularities." Follows from two limits: no singularity → no premium; extreme singularity → frictions vanish → no premium. Maximum at intermediate.
- **Line 276** [VERBAL] OK — Summary accurately restates the section's argument.

## Conclusion (lines 281–296)
- **Line 281** — section header
- **Line 283** [VERBAL] OK — "AI stocks command a hedging premium under incomplete markets." Restates Proposition 4.
- **Line 283** [VERBAL] OK — Mechanism description (displacement raises marginal utility, AI stocks pay more) correctly summarizes Propositions 1–4.
- **Line 283** [VERBAL] OK — "When displacement is sufficiently severe, the price-dividend ratio increases with singularity probability." Restates Proposition 3.
- **Line 283** [VERBAL] NOTE — "and the valuation spread between AI and non-AI stocks widens." The sentence structure implies this requires the same "sufficiently severe" condition as Prop 3, but the spread is unconditionally increasing in p (from eq on line 190, ∂S/∂p > 0 always). **Not wrong — the spread does widen — but the conditioning is slightly misleading. The spread result is stronger than stated.**
- **Line 283** [VERBAL] OK — "Under complete markets, the premium vanishes." Restates Proposition 4.
- **Line 285** [VERBAL] OK — Cross-sectional prediction (AI > non-AI PD ratios) restates Proposition 2. Appropriately hedged ("deliberately stylized and not designed to match specific valuation levels").
- **Line 287** [VERBAL] OK — Channel 1 (curvature of utility, γ > 1, marginal utility negligible) accurately restates Remark 1.
- **Line 287** [VERBAL] OK — Channel 2 (fixed costs negligible at large Y, Coasean risk-sharing) accurately restates Remark 2.
- **Line 287** [VERBAL] OK — "hedging premium is largest for moderate singularities" consistent with Remark 2.
- **Line 289** [VERBAL] OK — "expanding the set of tradeable AI-related assets could reduce the displacement premium" follows from Proposition 4 (complete markets). "Improve welfare" is a standard inference from market completion, though no formal welfare theorem is stated in the paper.

## Proofs (lines 297–312)
- **Line 297** — appendix header with label `app:proofs`
- **Line 299** [REFERENCE] OK — Proof references Proposition 3 (prop:comp-static, line 200). Correct.
- **Line 300** [DEFINITION] OK — N(p) = (1−p)R + pΦ^A(1+V_1) and D(p) = 1−(1−p)R match eq (pd-ai) at line 159.
- **Line 302** [ARITHMETIC] OK — Quotient rule ∂V_0^A/∂p = [N′D − ND′]/D². Standard.
- **Line 304** [ARITHMETIC] OK — N′(p) = −R + Φ^A(1+V_1) and D′(p) = R. Both derivatives verified.
- **Line 306** [ARITHMETIC] OK — Direct substitution into N′D − ND′. Matches stated expression.
- **Line 307** [ARITHMETIC] OK — Expansion verified: (1−p)R² terms cancel; RΦ^A(1+V_1) terms combine as −[(1−p)+p]RΦ^A(1+V_1) = −RΦ^A(1+V_1). Result: −R + Φ^A(1+V_1) − RΦ^A(1+V_1).
- **Line 308** [ARITHMETIC] OK — Factoring: Φ^A(1+V_1)(1−R) − R. Correct.
- **Line 310** [ARITHMETIC] OK — Positive iff Φ^A(1+V_1) > R/(1−R), dividing by (1−R) > 0. Correct.
- **Line 310** [ARITHMETIC] OK — R/(1−R) = V_0^A|_{p=0}. At p = 0: V_0^A = R/(1−R). Verified. "Gordon growth price-dividend ratio" gloss is accurate.
- **Line 310** [VERBAL] OK — "condition (eq:comp-static) follows." Matches Proposition 3 statement exactly.
