# tests/factcheck-bysection.py
Started: 2026-04-02 18:34:30 EDT
Runtime: 6m 10s
[ralph-garage/agent-logs/20260402T183430.355890-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260402T183430.355890-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong; one minor wording imprecision noted on line 252.

## Introduction (lines 41–71)
- **Line 41** — section header
- **Line 43** [VERBAL] OK — "recent surge in AI stock valuations" is uncontroversial factual background
- **Line 43** [VERBAL] OK — "Between 2023 and 2025, the largest AI-related companies collectively gained trillions of dollars in market value" is consistent with common knowledge
- **Line 43** [FIGURE/TABLE] OK — "Figure 1 illustrates this pattern using CRSP data: the price-dividend ratio of major AI stocks has risen sharply relative to non-AI stocks." Verified against ai-valuations.pdf: figure shows AI stocks (blue line) with P/D ratios ~150–400 rising sharply post-2023, vs non-AI stocks (red line) flat at ~30–50. Title confirms CRSP data.
- **Line 43** [VERBAL] OK — "We propose an additional channel: publicly traded AI stocks command a valuation premium because they serve as a hedge against a negative AI singularity." Thesis statement consistent with abstract and Proposition 4.
- **Lines 45–50** [FIGURE/TABLE] OK — Caption accurately describes ai-valuations.pdf content (AI stocks: NVDA, MSFT, GOOGL, META, AMZN; CRSP universe; trailing 12-month dividends).
- **Line 52** [VERBAL] OK — "representative investor whose wealth is largely tied to existing firms" consistent with model setup (line 86, 130)
- **Line 52** [VERBAL] OK — "displacing traditional businesses and reducing the investor's share of total output" supported by Assumption 1 (line 104)
- **Line 52** [VERBAL] OK — "the typical investor cannot buy these assets" supported by budget constraint (line 124–126)
- **Line 52** [VERBAL] OK — "publicly traded AI stocks offer the best available hedge" supported by Assumption 2 and Proposition 2
- **Line 54** [VERBAL] OK — "infinite-horizon, discrete-time asset pricing model" confirmed at lines 76, 121
- **Line 54** [VERBAL] OK — "two publicly traded assets" confirmed at lines 88–92
- **Line 54** [REFERENCE] OK — "following GKP2012, can be interpreted as future innovators who do not yet participate in public markets" confirmed by GKP-2012-WP.md: "the future innovators, who are yet to enter the economy, are not able to trade with the current population of agents"
- **Line 54** [VERBAL] OK — "AI stocks gain a larger share of total output while non-AI stocks shrink" confirmed by Assumption 2 (line 108)
- **Line 54** [VERBAL] OK — "The household is displaced—its consumption share falls" confirmed by Assumption 1 and eq (6) on line 132
- **Line 56** [VERBAL] OK — "We derive the price-dividend ratio of AI stocks in closed form" confirmed by Proposition 1 (line 156)
- **Line 56** [VERBAL] OK — "the ratio increases with the probability of a singularity" confirmed by Proposition 3 (line 200) under stated conditions
- **Line 56** [VERBAL] OK — "positive covariance between the stochastic discount factor and AI dividends lowers the required return" standard asset pricing logic, confirmed by Φ^A formula (line 168) containing Δ^{−γ} > 1 and θ̃/θ > 1
- **Line 56** [VERBAL] OK — "the valuation spread between AI and non-AI stocks widens with singularity probability" confirmed by Proposition 2 (line 187), spread formula has p in numerator
- **Line 56** [VERBAL] OK — "Under complete markets, the household could invest in private AI capital, eliminating displacement risk and the hedging premium" confirmed by Proposition 4 (line 214)
- **Line 58** [REFERENCE] OK — "connect to Jones (2024) on the trade-off between AI-driven growth and existential risk" confirmed by Extension section (lines 240–282) and Jones-2024-AERI.md
- **Line 58** [VERBAL] OK — "Even modest transfer mechanisms suffice when the surplus is enormous" confirmed by eq (26) on line 274: F/Y → 0 as Y → ∞
- **Line 58** [VERBAL] OK — "the most extreme AI singularity reduces displacement risk" confirmed by Remarks 1 and 2
- **Line 58** [VERBAL] OK — "if the singularity may destroy the economy entirely, the hedging premium is attenuated" confirmed by eq (22) on line 248
- **Line 60** [VERBAL] OK — "The human author contributed only the paper specification and testing framework—approximately 80 lines" paper-spec.md is 84 lines, consistent with "approximately 80 lines"
- **Line 60** [REFERENCE] OK — Footnote on Claude/Anthropic consistent with repo structure (ralph/ directory)
- **Line 63** [REFERENCE] OK — "GKP2012, who introduce displacement risk in an overlapping-generations economy with innovation" confirmed by GKP-2012-WP.md and references.bib (JFE 2012)
- **Line 63** [REFERENCE] OK — "They show that innovation creates a systematic risk factor because new entrants capture rents" confirmed by GKP-2012-WP.md
- **Line 63** [VERBAL] OK — "Our contribution relative to GKP is purposefully modest" consistent with spec I.6.d
- **Line 63** [REFERENCE] OK — "KoganPapanikolaouStoffman2020 extend the displacement risk framework to study how creative destruction generates inequality" confirmed by references.bib: JPE 2020, "Left Behind: Creative Destruction, Inequality, and the Stock Market"
- **Line 63** [REFERENCE] OK — "KoganPapanikolaou2014 analyze how investment-specific technology shocks affect asset prices" confirmed by references.bib: JF 2014, "Growth Opportunities, Technology Shocks, and Asset Prices"
- **Line 65** [REFERENCE] OK — "rare disasters literature (Rietz1988, Barro2006, Wachter2013)" all three confirmed in references.bib as foundational rare disasters papers
- **Line 65** [VERBAL] OK — "asymmetric effects across sectors: AI stocks benefit while non-AI stocks suffer" confirmed by Assumption 2 and Proposition 2
- **Line 67** [REFERENCE] OK — "Jones (2024) analyzes the trade-off between AI-driven growth and existential risk, showing that the curvature of utility is central" confirmed by Jones-2024-AERI.md
- **Line 67** [REFERENCE] OK — "KorinekSuh2024 study scenarios for the transition to artificial general intelligence, characterizing conditions under which wages collapse" confirmed by Korinek-Suh-2024.md
- **Line 67** [REFERENCE] OK — "AcemogluRestrepo2018 model the race between automation and labor" confirmed by references.bib: AER 2018, "The Race Between Man and Machine"
- **Line 67** [REFERENCE] OK — "PastorVeronesi2009 study how technological revolutions affect stock prices" confirmed by references.bib: AER 2009
- **Line 67** [REFERENCE] OK — "HobijnJovanovic2001 document the negative impact of IT innovation on incumbent firms" confirmed by references.bib: AER 2001 and GKP-2012-WP.md

## Model (lines 72–153)
- **Line 72** — section header
- **Line 76** [DEFINITION] OK — discrete time t = 0, 1, 2, ...; aggregate output Y_t; singularity as absorbing event with probability p ∈ (0,1)
- **Line 78** [DEFINITION] OK — eq (1): Y_{t+1} = (1+g) Y_t, standard constant growth
- **Line 80** [VERBAL] OK — "strictly higher rate" consistent with g̃ > g in eq (2)
- **Line 82** [DEFINITION] OK — eq (2): Y_{t+1} = (1+g̃) Y_t, g̃ > g
- **Line 84** [REFERENCE] OK — "the extension explores the limit g̃ → ∞" confirmed in Remark 1 (line 254)
- **Line 86** [VERBAL] OK — "The household is the marginal investor in public markets" consistent with market clearing (line 130)
- **Line 86** [VERBAL] OK — "AI owners hold private AI capital and do not participate in public stock markets" consistent with budget constraint (line 124–126)
- **Line 86** [REFERENCE] OK — "Following GKP2012, AI owners can be interpreted as future innovators" confirmed by GKP-2012-WP.md
- **Line 90** [DEFINITION] OK — output shares θ, ν, 1−θ−ν sum to 1
- **Line 92** [DEFINITION] OK — eq (3): pre-singularity dividend definitions
- **Line 96** [VERBAL] OK — "output shares shift permanently" consistent with absorbing-state assumption
- **Line 98** [DEFINITION] OK — eq (4): post-singularity dividend definitions
- **Lines 103–105** [ASSUMPTION] OK — Assumption 1: θ̃+ν̃ < θ+ν. Verified with Table 1 parameters: 0.15+0.30 = 0.45 < 0.60 = 0.05+0.55
- **Lines 107–109** [ASSUMPTION] OK — Assumption 2: θ̃ > θ and ν̃ < ν. Verified: 0.15 > 0.05 and 0.30 < 0.55
- **Line 111** [DEFINITION] OK — ω ≡ θ+ν and ω̃ ≡ θ̃+ν̃
- **Line 113** [DEFINITION] OK — Δ ≡ ω̃/ω < 1, follows from Assumption 1
- **Line 115** [VERBAL] OK — correct restatement of Assumption 1 in terms of Δ
- **Lines 119–122** [DEFINITION] OK — standard CRRA utility with γ > 1, β ∈ (0,1)
- **Line 124** [VERBAL] OK — household trades two public assets, cannot invest in private AI capital
- **Line 126** [DEFINITION] OK — standard budget constraint with ex-dividend prices
- **Line 130** [VERBAL] OK — market clearing requires n_t^A = n_t^N = 1 with single representative household
- **Line 132** [ARITHMETIC] OK — c_t = D_t^A + D_t^N = θY_t + νY_t = ωY_t. Correct.
- **Line 134** [VERBAL] OK — c_t = ω̃Y_t post-singularity, by identical logic with tilded shares
- **Lines 136–139** [DEFINITION] OK — standard Euler equation for asset pricing
- **Line 143** [VERBAL] OK — PD ratio constant within each regime because growth rates are deterministic constants
- **Lines 145–147** [ASSUMPTION] OK — Assumption 3: convergence conditions for finite PD ratios
- **Line 149** [VERBAL] OK — "automatically satisfied for γ > 1": when γ > 1, (1+g)^{1−γ} < 1, so β(1+g)^{1−γ} < β < 1, and (1−p) times that is even smaller. Correct.

## Results (lines 154–239)
- **Line 154** — section header
- **Lines 156–171** [DEFINITION] OK — Proposition 1: closed-form PD ratios. Formulas for V_0^A, V_0^N, R, Φ^A, Φ^N, V_1 are self-consistent definitions.
- **Line 172** [VERBAL] OK — verbal descriptions of R, Φ^A, Φ^N, V_1 are accurate
- **Lines 175–183** [ARITHMETIC] OK — Proof of Proposition 1 verified:
  - V_1 derivation from Euler equation: V_1 = β(1+g̃)^{1−γ}(1+V_1), solving yields eq (10). Correct.
  - Normal-state contribution: (1−p)R(1+V_0^A). Correct.
  - Singularity contribution: SDF = β(Δ(1+g̃))^{−γ}, dividend growth = (θ̃/θ)(1+g̃), product = Φ^A. Correct.
  - Solving for V_0^A yields eq (5). Correct.
- **Line 185** [VERBAL] OK — Δ < 1 implies Δ^{−γ} > 1 (correct for γ > 0); θ̃/θ > 1 by Assumption 2; ν̃/ν < 1 by Assumption 2
- **Lines 187–196** [ARITHMETIC] OK — Proposition 2 and proof verified. V_0^A − V_0^N has identical denominator; numerator difference is p(Φ^A − Φ^N)(1+V_1). Φ^A − Φ^N = β Δ^{−γ}(1+g̃)^{1−γ}(θ̃/θ − ν̃/ν) > 0 since θ̃/θ = 3 > 1 > 0.545 ≈ ν̃/ν. Correct.
- **Line 198** [VERBAL] OK — spread increases with p (p in numerator, positive denominator) and with 1−Δ (Δ^{−γ} increases as Δ decreases). Correct.
- **Lines 200–206** [ARITHMETIC] OK — Proposition 3: ∂V_0^A/∂p > 0 iff Φ^A(1+V_1) > R/(1−R). Condition verified algebraically in Appendix proof. R/(1−R) = V_0^A|_{p=0} confirmed by setting p=0 in eq (5).
- **Lines 208–210** [REFERENCE] OK — "See Appendix" references app:proofs (line 303), which contains the proof
- **Line 212** [VERBAL] OK — economic interpretation correctly summarizes condition (12)
- **Lines 214–228** [ARITHMETIC] OK — Proposition 4 verified:
  - Φ^{A,CM} = β(1+g̃)^{1−γ}(θ̃/θ): under complete markets, c_{t+1}/c_t = (1+g̃) at singularity (not Δ(1+g̃)), so Δ^{−γ} drops out. Correct.
  - Hedging premium = p·β·(1+g̃)^{1−γ}·(θ̃/θ)·(Δ^{−γ}−1)·(1+V_1) / [1−(1−p)R] > 0. Positivity follows from Δ^{−γ}−1 > 0. Correct.
  - Comparative statics (increasing in p, θ̃/θ, 1−Δ) follow by inspection. Correct.
- **Line 230** [VERBAL] OK — "arises entirely from the displacement channel" correct: premium is proportional to (Δ^{−γ}−1), zero iff Δ=1
- **Line 233** [ARITHMETIC] OK — All numerical claims independently recomputed with β=0.96, γ=3, g=0.02, g̃=0.05, θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30:
  - ω = 0.60, ω̃ = 0.45, Δ = 0.75. Correct.
  - R = 0.96·(1.02)^{−2} = 0.9225
  - V_1 = 0.96·(1.05)^{−2} / (1 − 0.96·(1.05)^{−2}) = 0.8707/0.1293 = 6.734
  - At p=0: V_0^A = R/(1−R) = 0.9225/0.0775 = 11.9. Correct.
  - At p=0.01: Φ^A = 0.96·(0.75)^{−3}·(1.05)^{−2}·3 = 6.198; V_0^A = ((0.99)(0.9225) + (0.01)(6.198)(7.734))/(1−(0.99)(0.9225)) = 16.1. Correct.
  - V_0^N at p=0.01 ≈ 11.6. Correct.
  - V_0^A/V_0^N ≈ 1.39, claimed "roughly 1.4". Correct.
  - V_0^{A,CM} at p=0.01 ≈ 12.9. Correct.
  - Hedging premium: (16.1−12.9)/12.9 ≈ 24.8%, claimed "about 25%". Correct.
- **Line 235** [FIGURE/TABLE] OK — Table 1 (numerical-illustration.tex) verified: all five rows (p = 0, 0.005, 0.01, 0.02, 0.05) match independent computation at reported one-decimal precision for V_0^A, V_0^N, V_0^{A,CM}, Spread, and Hedge Premium %.

## Extension: Singularity, Extinction, and Frictions (lines 240–286)
- **Line 240** — section header
- **Line 242** [VERBAL] OK — "baseline model treats the singularity as a displacement event with certainty of economic survival" correct, no extinction in baseline
- **Line 242** [REFERENCE] OK — "drawing on Jones (2024)" for extinction risk and large-output analysis; Jones (2024) analyzes AI-driven growth vs existential risk
- **Line 246** [DEFINITION] OK — probability q ∈ [0,1) of catastrophic extinction conditional on singularity
- **Line 248** [ARITHMETIC] OK — V_0^{A,q} formula verified: singularity state splits into extinction (probability q, contribution 0) and survival (probability 1−q, contribution Φ^A(1+V_1)); solving the Euler equation yields eq (22). Correct.
- **Line 250** [VERBAL] OK — "Extinction risk reduces the singularity-state contribution by the factor (1−q)" direct comparison of eq (22) vs eq (5)
- **Line 250** [VERBAL] OK — "In the limit q→1, the singularity contributes nothing to AI stock valuations" correct: p(1−q)Φ^A(1+V_1) → 0
- **Line 252** [REFERENCE] OK — "Jones (2024) shows that the trade-off between AI-driven growth and existential risk depends critically on the curvature of utility" confirmed by Jones-2024-AERI.md
- **Line 252** [VERBAL] OK — "With γ>1, utility is bounded, and even infinite consumption generates finite utility" standard CRRA property: u(c) → 1/(γ−1) as c→∞
- **Line 252** [VERBAL] NOTE — "the household's consumption, though growing, remains a shrinking fraction ω̃ of total output" is slightly imprecise. Post-singularity, the household's share is fixed at ω̃, not shrinking over time. The share drops discretely at the singularity from ω to ω̃, then stays constant. The word "shrinking" could mislead, but the underlying economics (household gets a smaller share than pre-singularity) is correct. Not materially wrong.
- **Lines 254–256** [ARITHMETIC] OK — Remark 1: for γ>1, (1+g̃)^{1−γ} → 0 as g̃→∞ (since 1−γ < 0). Therefore Φ^A → 0 (linear in (1+g̃)^{1−γ}) and V_1 → 0 (numerator → 0, denominator → 1). Hedging premium vanishes. Correct.
- **Line 255** [VERBAL] OK — "For γ=1 (log utility), the premium is independent of g̃" verified: (1+g̃)^0 = 1, so Φ^A and V_1 are independent of g̃. Correct.
- **Line 258** [REFERENCE] OK — parallel between Jones's utility curvature result and this paper's hedging premium result is accurately drawn
- **Line 262** [REFERENCE] OK — "GKP2012 assume that intergenerational risk-sharing fails due to frictions" confirmed by GKP-2012-WP.md
- **Line 262** [REFERENCE] OK — "GKP discuss how mechanisms such as bequests, government debt, and intergenerational transfers would affect the magnitude of the displacement factor" confirmed by GKP-2012-WP.md (lines 360–362)
- **Line 262** [REFERENCE] OK — "in a representative dynasty with perfect altruism the displacement factor equals one" confirmed by GKP-2012-WP.md (line 362)
- **Line 262** [REFERENCE] OK — "but do not conduct a formal analysis of how these mechanisms scale with output" confirmed: GKP mention these in passing and leave extensions for future work
- **Lines 264–268** [DEFINITION] OK — Δ(λ) = 1 − (1−Δ_0)(1−λ) is a modeling definition
- **Line 268** [ARITHMETIC] OK — boundary cases verified: Δ(0) = Δ_0; Δ(1) = 1. Correct.
- **Line 268** [VERBAL] OK — "At λ=1, transfers fully offset displacement and Δ=1, eliminating the hedging premium as in the complete-markets case" confirmed: Δ=1 implies Δ^{−γ}−1 = 0, premium = 0 by eq (14)
- **Line 270** [VERBAL] OK — Coase theorem statement is standard
- **Line 272** [ARITHMETIC] OK — transfer needed: T = (ω−ω̃)Y to restore household share to ω. Correct.
- **Line 274** [ARITHMETIC] OK — friction cost fraction: (F + τ(ω−ω̃)Y)/Y = F/Y + τ(ω−ω̃). Correct.
- **Line 276** [VERBAL] OK — "As Y→∞, the fixed component vanishes" since F/Y → 0. Correct.
- **Line 276** [ARITHMETIC] OK — "AI owners' gains are (1−ω̃)Y − (1−ω)Y = (ω−ω̃)Y" correct algebra
- **Lines 278–280** [VERBAL] OK — Remark 2: if Y→∞, fixed-cost friction F/Y → 0, Coase theorem applies, displacement risk eliminated, hedging premium vanishes. Logically sound (given implicit assumption that proportional cost τ is manageable, which is acknowledged in the preceding paragraph).
- **Line 279** [VERBAL] OK — "hedging premium is largest for moderate singularities" follows from two limits: premium → 0 as displacement → 0, and premium → 0 as Y → ∞ (Remark 2) or g̃ → ∞ (Remark 1). Premium peaks in between.
- **Line 282** [VERBAL] OK — summary accurately connects GKP displacement to Jones singularity analysis

## Conclusion (lines 287–302)
- **Line 287** — section header
- **Line 289** [VERBAL] OK — "publicly traded AI stocks command a hedging premium under incomplete markets" supported by Proposition 4 (eq 14)
- **Line 289** [VERBAL] OK — "unable to invest in private AI capital" confirmed at line 124
- **Line 289** [VERBAL] OK — "they pay relatively more in singularity states when the household's marginal utility is high" supported by line 185: Δ^{−γ} > 1 and θ̃/θ > 1
- **Line 289** [VERBAL] OK — "When displacement is sufficiently severe, the price-dividend ratio of AI stocks increases with singularity probability" supported by Proposition 3, qualifier correctly preserved
- **Line 289** [VERBAL] OK — "the valuation spread between AI and non-AI stocks widens" supported by Proposition 2 and line 198
- **Line 289** [VERBAL] OK — "Under complete markets, the premium vanishes" supported by Proposition 4 (Δ^{−γ} replaced by 1)
- **Line 291** [VERBAL] OK — cross-sectional prediction follows from Proposition 2
- **Line 291** [VERBAL] OK — "consistent with the elevated valuations of AI-related firms" appropriately hedged qualitative claim
- **Line 293** [REFERENCE] OK — "curvature of utility (γ>1) makes marginal utility negligible at high consumption levels (Remark 1)" accurately summarizes Remark 1 (line 254–256)
- **Line 293** [REFERENCE] OK — "fixed costs of intergenerational transfers become negligible relative to the surplus, enabling Coasean risk-sharing (Remark 2)" accurately summarizes Remark 2 (line 278–280)
- **Line 293** [VERBAL] OK — "hedging premium is largest for moderate singularities" correctly synthesizes both remarks
- **Line 295** [VERBAL] OK — policy implication (expanding tradeable AI assets could reduce premium) follows from Proposition 4: completing markets eliminates premium

## Proofs (lines 303–318)
- **Line 303** — appendix header
- **Line 306** [DEFINITION] OK — A(p) = (1−p)R + pΦ^A(1+V_1) and B(p) = 1−(1−p)R correctly decompose eq (5)
- **Line 310** [ARITHMETIC] OK — A'(p) = −R + Φ^A(1+V_1). Correct derivative.
- **Line 310** [ARITHMETIC] OK — B'(p) = R. Correct derivative.
- **Line 308** [ARITHMETIC] OK — quotient rule applied correctly
- **Lines 312–314** [ARITHMETIC] OK — numerator expansion verified by full algebra:
  - A'B = [−R + Φ^A(1+V_1)][1−(1−p)R] = −R + (1−p)R² + Φ^A(1+V_1) − (1−p)RΦ^A(1+V_1)
  - AB' = [(1−p)R + pΦ^A(1+V_1)]R = (1−p)R² + pRΦ^A(1+V_1)
  - A'B − AB' = −R + Φ^A(1+V_1) − [(1−p)+p]RΦ^A(1+V_1) = −R + Φ^A(1+V_1)(1−R)
  - Matches line 314 exactly.
- **Line 316** [ARITHMETIC] OK — sign condition: Φ^A(1+V_1)(1−R) − R > 0 iff Φ^A(1+V_1) > R/(1−R), since R < 1 (required for finite PD ratio). Correct.
- **Line 316** [ARITHMETIC] OK — R/(1−R) = V_0^A|_{p=0}: setting p=0 in eq (5) gives R/(1−R). Correct. This is the Gordon growth PD ratio.
- **Line 205** [VERBAL] OK — comparative statics on condition: Δ small makes Δ^{−γ} large (increases Φ^A); θ̃/θ large directly increases Φ^A; γ large increases Δ^{−γ} (dominates (1+g̃)^{1−γ} for sufficiently severe displacement). All correct.
