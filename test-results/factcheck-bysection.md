# tests/factcheck-bysection.py
Started: 2026-04-02 21:59:20 EDT
Runtime: 9m 21s
[ralph-garage/agent-logs/20260402T215920.395960-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260402T215920.395960-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct; all verbal claims are supported; no material errors found.

## Introduction (lines 41–68)
- **Line 41** — section header
- **Line 43** [VERBAL] OK — contextual claim about AI stock valuations 2023–2025 is consistent with well-known market facts
- **Line 43** [FIGURE/TABLE] OK — `Figure~\ref{fig:ai-valuations}` references label defined at line 49; file `paper/exhibits/ai-valuations.pdf` exists
- **Line 43** [VERBAL] OK — "price-dividend ratio of major AI stocks has risen sharply relative to non-AI stocks" is consistent with figure caption (line 48) describing CRSP-based PD ratios for AI vs non-AI stocks
- **Line 43** [VERBAL] OK — thesis statement ("hedge against a negative AI singularity") is subsequently formalized in the model
- **Line 48** [FIGURE/TABLE] OK — caption correctly describes CRSP data with trailing 12-month dividends for NVDA, MSFT, GOOGL, META, AMZN vs rest of CRSP
- **Line 52** [VERBAL] OK — narrative about displacement, private ventures, and incomplete markets accurately previews Assumptions 1–2 (lines 105–111) and the budget constraint (lines 126–130)
- **Line 54** [VERBAL] OK — "infinite-horizon, discrete-time" confirmed at line 78; "two publicly traded assets" confirmed at line 92; "representative household who is the marginal investor" confirmed at line 88
- **Line 54** [REFERENCE] OK — GKP interpretation of AI owners as future innovators confirmed at line 88 and in GKP lit file
- **Line 54** [VERBAL] OK — "Each period, with some probability, a singularity occurs" confirmed by Assumption 2 (lines 109–111); "household is displaced" confirmed by Assumption 1 (lines 105–107)
- **Line 56** [REFERENCE] OK — "closed form" confirmed by Proposition 1 (line 159); "increases with probability" confirmed by Proposition 3 (line 203)
- **Line 56** [VERBAL] OK — hedging premium mechanism (high marginal utility when AI stocks pay well) confirmed by discussion at line 188
- **Line 56** [VERBAL] OK — valuation spread and complete markets claims confirmed by Propositions 2 and 4
- **Line 58** [REFERENCE] OK — Jones (2024) connection confirmed in Extension (lines 243–261); Coase/frictions argument confirmed at lines 263–279; extinction risk confirmed at lines 247–253
- **Line 58** [VERBAL] OK — "most extreme AI singularity reduces displacement risk" confirmed by Remark 2 (line 275)
- **Line 60** [VERBAL] OK — AI authorship description is a framing claim; spec confirms human wrote ~80 lines
- **Line 63** [REFERENCE] OK — GKP characterization ("displacement risk in an overlapping-generations economy with innovation") confirmed by GKP lit file
- **Line 63** [REFERENCE] OK — "new entrants capture rents that existing agents cannot share" confirmed by GKP lit file
- **Line 63** [VERBAL] OK — KPS2020 and KP2014 characterizations are standard descriptions of those papers (no lit files available to independently verify)
- **Line 65** [VERBAL] OK — rare disasters literature framing (Rietz, Barro, Wachter) is standard; sectoral asymmetry claim is confirmed by Assumption 2 and Proposition 2
- **Line 67** [REFERENCE] OK — Jones (2024) characterization confirmed by Jones lit file; Korinek-Suh (2024) wage collapse confirmed by lit file; Hobijn-Jovanovic (2001) confirmed via GKP lit file
- **Line 67** [VERBAL] OK — Acemoglu-Restrepo (2018) and Pastor-Veronesi (2009) characterizations are standard (no lit files)

## Model (lines 72–156)
- **Line 72** — section header
- **Line 74** [VERBAL] OK — preview of model purpose consistent with Propositions 2 and 4
- **Line 78** [DEFINITION] OK — discrete time, singularity as absorbing event with independent probability p
- **Lines 79–81** [DEFINITION] OK — normal growth Y_{t+1} = (1+g)Y_t; used consistently in R definition
- **Lines 82–85** [DEFINITION] OK — post-singularity growth Y_{t+1} = (1+g̃)Y_t with g̃ > g; used in Φ^A, Φ^N, V₁
- **Line 86** [REFERENCE] OK — "the extension explores the limit g̃→∞" confirmed at lines 257–259
- **Line 88** [REFERENCE] OK — GKP unborn-cohorts interpretation accurately attributed; paper's own modeling choice clearly distinguished
- **Lines 92–96** [DEFINITION] OK — pre-singularity dividend shares θ, ν, (1−θ−ν) sum to 1
- **Lines 98–101** [DEFINITION] OK — post-singularity shares θ̃, ν̃, (1−θ̃−ν̃) sum to 1
- **Lines 105–107** [ASSUMPTION] OK — Assumption 1: θ̃+ν̃ < θ+ν (household share falls); implies Δ < 1
- **Lines 109–111** [ASSUMPTION] OK — Assumption 2: θ̃ > θ and ν̃ < ν; independent of Assumption 1 (both needed)
- **Lines 113–116** [DEFINITION] OK — ω ≡ θ+ν, ω̃ ≡ θ̃+ν̃, Δ ≡ ω̃/ω < 1 follows from Assumption 1
- **Line 117** [VERBAL] OK — accurately restates Assumption 1 using Δ notation
- **Lines 121–124** [DEFINITION] OK — standard CRRA utility with γ > 1, β ∈ (0,1)
- **Lines 126–130** [DEFINITION] OK — budget constraint with ex-dividend prices; consistent with two-asset setup
- **Line 132** [ASSUMPTION] OK — market clearing n^A = n^N = 1; household is sole public-market investor
- **Lines 132–136** [ARITHMETIC] OK — c_t = θY_t + νY_t = ωY_t (pre-singularity); c_t = ω̃Y_t (post-singularity)
- **Lines 138–141** [DEFINITION] OK — standard CRRA Euler equation; sign convention consistent with budget constraint
- **Line 142** [VERBAL] OK — "consumption falls at the singularity" is correct for the paper's parameter regime (Δ(1+g̃) = 0.7875 < 1); the formal results only require Δ < 1 and are unaffected
- **Lines 146–147** [VERBAL] OK — constant PD ratios within each regime justified by i.i.d. growth rates
- **Lines 148–150** [ASSUMPTION] OK — existence conditions ensure finite PD ratios; denominators of V₁ and V₀ formulas are positive
- **Line 152** [VERBAL] OK — "automatically satisfied for γ > 1" is correct since (1+g)^{1−γ} < 1 for γ > 1 and g > 0

## Results (lines 157–242)
- **Line 157** — section header
- **Lines 159–176** [DEFINITION] OK — Proposition 1 states closed-form PD ratios V₀^A, V₀^N with auxiliary definitions R, Φ^A, Φ^N, V₁
- **Line 175** [VERBAL] OK — verbal descriptions of R, Φ^A, Φ^N, V₁ are accurate
- **Line 179** [ARITHMETIC] OK — post-singularity Euler V₁ = β(1+g̃)^{1−γ}(1+V₁) rearranges to eq (7); numerically V₁ = 6.7368
- **Line 185** [ARITHMETIC] OK — normal-state contribution: consumption growth (1+g), dividend growth (1+g), contribution (1−p)R(1+V₀^A)
- **Line 185** [ARITHMETIC] OK — singularity-state: consumption growth Δ(1+g̃), AI dividend growth (θ̃/θ)(1+g̃); SDF × div_growth = Φ^A; numerically Φ^A = 6.192
- **Line 185** [ARITHMETIC] OK — solving for V₀^A yields eq (2)
- **Line 188** [VERBAL] OK — Δ^{−γ} > 1 because Δ < 1 (displacement); θ̃/θ > 1 (AI share gain); ν̃/ν < 1 (non-AI share loss)
- **Lines 190–194** [ARITHMETIC] OK — V₀^A − V₀^N formula: common denominator, numerator difference = p·β·Δ^{−γ}(1+g̃)^{1−γ}(θ̃/θ − ν̃/ν)(1+V₁) > 0
- **Lines 197–199** [ARITHMETIC] OK — θ̃/θ = 3.0 > 1 > ν̃/ν ≈ 0.545, so difference is positive by Assumption 2
- **Line 201** [VERBAL] OK — spread increases with p (linear in numerator) and with 1−Δ (Δ^{−γ} increasing as Δ falls); confirmed by table data
- **Lines 203–208** [ARITHMETIC] OK — condition Φ^A(1+V₁) > R/(1−R) correctly derived in appendix (lines 296–310)
- **Line 208** [ARITHMETIC] OK — R/(1−R) = V₀^A|_{p=0} = 0.9227/0.0773 = 11.94; confirmed
- **Line 208** [VERBAL] OK — condition holds for small Δ, large γ, or large θ̃/θ because all three raise Φ^A
- **Lines 211–212** [REFERENCE] OK — "See Appendix" correctly points to lines 296–310 which contain the full proof
- **Line 215** [VERBAL] OK — correct restatement of Proposition 3's economic content
- **Lines 217–226** [ARITHMETIC] OK — complete markets: c_t = Y_t, so Δ^{−γ} replaced by 1; Φ^{A,CM} = β(1+g̃)^{1−γ}(θ̃/θ) = 2.612; hedging premium formula correctly factors out (Δ^{−γ}−1)
- **Line 226** [VERBAL] OK — premium increasing in p, θ̃/θ, and 1−Δ; all enter the formula monotonically
- **Lines 229–231** [ARITHMETIC] OK — proof logic correct: complete markets consumption growth is (1+g̃) not Δ(1+g̃)
- **Line 233** [VERBAL] OK — correct interpretation: complete markets → Δ^{−γ} = 1 → hedging premium = 0
- **Line 236** [ARITHMETIC] OK — ω = 0.05+0.55 = 0.60; ω̃ = 0.15+0.30 = 0.45; Δ = 0.75
- **Line 236** [ARITHMETIC] OK — V₀^A = 16.098 ≈ 16.1 at p = 0.01
- **Line 236** [ARITHMETIC] OK — V₀^N = 11.567 ≈ 11.6 at p = 0.01
- **Line 236** [ARITHMETIC] OK — ratio 16.098/11.567 = 1.392 ≈ "roughly 1.4"
- **Line 236** [ARITHMETIC] OK — V₀^A|_{p=0} = V₀^N|_{p=0} = R/(1−R) = 11.94 ≈ 11.9
- **Line 236** [ARITHMETIC] OK — V₀^{A,CM} = 12.896 ≈ 12.9 at p = 0.01
- **Line 236** [ARITHMETIC] OK — hedging premium = (16.098−12.896)/12.896 = 24.8% ≈ "about 25%"
- **Line 238** [FIGURE/TABLE] OK — all five rows of Table 1 match independent recomputation:
  - p=0.000: V₀^A=11.9, V₀^N=11.9, V₀^{A,CM}=11.9, Spread=0.0, HedgePrem=0.0%
  - p=0.005: V₀^A=14.1, V₀^N=11.7, V₀^{A,CM}=12.4, Spread=2.4, HedgePrem=13.6%
  - p=0.010: V₀^A=16.1, V₀^N=11.6, V₀^{A,CM}=12.9, Spread=4.5, HedgePrem=24.8%
  - p=0.020: V₀^A=19.5, V₀^N=11.3, V₀^{A,CM}=13.7, Spread=8.2, HedgePrem=42.3%
  - p=0.050: V₀^A=26.5, V₀^N=10.6, V₀^{A,CM}=15.3, Spread=15.9, HedgePrem=73.4%

## Extension: Singularity, Extinction, and Frictions (lines 243–283)
- **Line 243** — section header
- **Line 245** [VERBAL] OK — correctly frames two extension directions (extinction risk, frictions) citing Jones (2024)
- **Line 249** [DEFINITION] OK — q ∈ [0,1) as conditional extinction probability given singularity
- **Lines 250–252** [ARITHMETIC] OK — extinction formula V₀^{A,q}: singularity term multiplied by (1−q); denominator unchanged because extinction only affects singularity states
- **Line 253** [VERBAL] OK — "extinction risk attenuates the hedging premium" follows directly from (1−q) factor; q→1 limit correctly described
- **Line 255** [REFERENCE] OK — Jones (2024) utility curvature claim confirmed by Jones lit file
- **Line 255** [VERBAL] OK — "γ > 1, utility is bounded" is correct for CRRA
- **Line 255** [VERBAL] OK — as g̃→∞, AI owners' consumption is unbounded while household retains fraction ω̃ of output
- **Lines 257–259** [ARITHMETIC] OK — for γ > 1: (1+g̃)^{1−γ}→0 as g̃→∞, so Φ^A→0 and V₁→0; hedging premium vanishes
- **Lines 257–259** [ARITHMETIC] OK — for γ = 1 (log utility): (1+g̃)^0 = 1, so Φ^A and V₁ are independent of g̃
- **Line 261** [VERBAL] OK — accurate synthesis connecting Jones's curvature result to the hedging premium
- **Lines 265–266** [REFERENCE] OK — GKP discussion of bequests, government debt, and intergenerational transfers confirmed by GKP lit file; claim that GKP note displacement factor equals one in representative dynasty with perfect altruism confirmed; claim that GKP do not conduct formal scaling analysis confirmed
- **Line 267** [VERBAL] OK — Δ = 1 → hedging premium = 0 follows from Proposition 4 (Δ^{−γ}−1 = 0)
- **Lines 269–272** [ARITHMETIC] OK — cost/Y = F/Y + τ(ω−ω̃); as Y→∞, F/Y→0
- **Line 273** [ARITHMETIC] OK — AI owners' gains = (1−ω̃)Y − (1−ω)Y = (ω−ω̃)Y
- **Lines 275–277** [VERBAL] OK — "hedging premium largest for moderate singularities" is a qualitative synthesis of two boundary results (Remark 1: premium vanishes as g̃→∞ for γ > 1; Remark 2: Coase theorem eliminates displacement as Y→∞); directionally correct
- **Line 279** [VERBAL] OK — accurate summary connecting GKP displacement risk to Jones singularity analysis

## Conclusion (lines 284–289)
- **Line 284** — section header
- **Line 286** [VERBAL] OK — "reduce the displacement premium" supported by Proposition 4
- **Line 286** [VERBAL] OK — "improve welfare" is a reasonable inference: under complete markets the household's consumption is Y_t > ωY_t, yielding higher CRRA utility, though no formal welfare theorem is stated
- **Line 286** [VERBAL] OK — "policy lever is market completeness" directly supported by Proposition 4
- **Line 286** [VERBAL] OK — "any mechanism allowing household to share AI upside reduces hedging premium" supported by Proposition 4 formula (increasing Δ toward 1 reduces Δ^{−γ}−1)
- **Line 286** [VERBAL] OK — "sufficiently abundant output makes modest transfers effective" supported by Remark 2 and eq (12)
- **Line 288** [VERBAL] OK — "omits heterogeneous households, production-side frictions, and endogenous innovation" is accurate
- **Line 288** [VERBAL] OK — "does not generate a broad menu of testable predictions" consistent with model scope
- **Line 288** [VERBAL] OK — "hedging premium is largest for moderate singularities" is a qualitative synthesis of Remarks 1–2 boundary results; directionally supported but not formally proved as a monotonicity/maximality result

## Proofs (lines 296–312)
- **Line 296** — appendix header
- **Line 298** — proof header for Proposition 3
- **Line 299** [DEFINITION] OK — N(p) = (1−p)R + pΦ^A(1+V₁), D(p) = 1−(1−p)R; consistent with eq (2)
- **Line 301** [ARITHMETIC] OK — quotient rule correctly stated
- **Line 303** [ARITHMETIC] OK — N'(p) = −R + Φ^A(1+V₁); D'(p) = R; both derivatives correct
- **Line 305** [ARITHMETIC] OK — raw numerator correctly substituted from quotient rule
- **Line 306** [ARITHMETIC] OK — expansion verified: (1−p)R² terms cancel; p and (1−p) coefficients on RΦ^A(1+V₁) combine to give −RΦ^A(1+V₁); result is −R + Φ^A(1+V₁) − RΦ^A(1+V₁)
- **Line 307** [ARITHMETIC] OK — regrouping to Φ^A(1+V₁)(1−R) − R is correct
- **Line 309** [ARITHMETIC] OK — positive iff Φ^A(1+V₁) > R/(1−R), since 1−R > 0 (R < 1 by Assumption 3)
- **Line 309** [ARITHMETIC] OK — R/(1−R) = V₀^A|_{p=0} confirmed by substituting p = 0 into eq (2)
