# tests/factcheck-bysection.py
Started: 2026-04-02 22:39:49 EDT
Runtime: 12m 38s
[ralph-garage/agent-logs/20260402T223949.798378-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260402T223949.798378-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: FAIL
REASON: Line 238 incorrectly describes the household's post-singularity output share as "shrinking" when it is a fixed constant in the model.

## Introduction (lines 41–67)
- **Line 41** — section header
- **Line 43** [VERBAL] OK — AI valuation surge claim is qualitative and supported by Figure 1
- **Line 43** [VERBAL] OK — hedging channel claim is the paper's thesis, formalized in Sections 2–3
- **Lines 45–50** [FIGURE/TABLE] OK — caption lists tickers NVDA, MSFT, GOOGL, META, AMZN and trailing 12-month dividends; confirmed against code/ai-valuations-figure.R which queries CRSP for exactly these tickers with a rolling 365-day dividend window
- **Line 52** [VERBAL] OK — incomplete-markets intuition (private AI ventures illiquid/nonexistent) is formalized in Section 2.3 (household excluded from private AI capital)
- **Line 54** [VERBAL] OK — model description (infinite-horizon, discrete-time, two public assets, representative household, AI owners as GKP-style future innovators, singularity shifts shares) matches Section 2
- **Line 56** [VERBAL] OK — "ratio increases with singularity probability" supported by Proposition 2; "positive covariance between SDF and AI dividends lowers the required return and raises valuation" is the correct direction (standard asset pricing: positive Cov(M, payoff) lowers expected return, raises price)
- **Line 56** [VERBAL] OK — "valuation spread widens with singularity probability" supported by the common-denominator comparison of V_pre^A and V_pre^N
- **Line 56** [VERBAL] OK — "under complete markets, hedging premium vanishes" supported by Proposition 3
- **Line 58** [VERBAL] OK — extension claims (frictions overcome by abundance, extinction attenuates premium) supported by Remarks 1–2 and Section 4.1
- **Line 58** [REFERENCE] OK — Jones (2024) accurately described as analyzing AI-driven growth vs. existential risk trade-off
- **Line 58** [REFERENCE] OK — GKP (2012) accurately described as emphasizing barriers to intergenerational risk-sharing
- **Line 60** [VERBAL] OK — "approximately 80 lines" for the paper spec; actual file is 85 lines, but "approximately" is adequate cover
- **Line 63** [REFERENCE] OK — GKP (2012): accurately described as introducing displacement risk in an OLG economy with innovation and incomplete intergenerational risk-sharing
- **Line 63** [REFERENCE] OK — Garleanu and Panageas (2015): described as OLG asset pricing with incomplete risk-sharing; consistent with paper title and topic
- **Line 63** [REFERENCE] OK — Kogan, Papanikolaou, and Stoffman (2020): described as OLG asset pricing with incomplete risk-sharing; consistent with paper topic (creative destruction, inequality, stock market)
- **Line 63** [REFERENCE] OK — Kogan and Papanikolaou (2014): described as analyzing technology shocks and growth opportunities; matches paper title exactly
- **Line 63** [REFERENCE] OK — Knesl (2023): described as modeling automation-driven displacement risk premia; consistent with paper title (automation and displacement of labor by capital)
- **Line 63** [REFERENCE] OK — Zhang (2019): described as modeling automation-driven displacement risk premia; consistent with paper title (labor-technology substitution, asset pricing)
- **Line 63** [REFERENCE] OK — Rietz (1988), Barro (2006), Wachter (2013): rare disasters literature citations; all confirmed in bib with correct journals
- **Line 63** [VERBAL] OK — "asymmetric sectoral effects that generate cross-sectional predictions absent from standard disaster models" is supported by the AI vs. non-AI valuation distinction
- **Line 63** [REFERENCE] OK — Babina et al. (2024): described as providing evidence that AI adoption drives firm growth; consistent with paper title
- **Line 63** [REFERENCE] OK — Pastor and Veronesi (2009): described as studying technological revolutions and stock prices; matches title exactly
- **Line 63** [REFERENCE] OK — Hobijn and Jovanovic (2001): described as documenting negative impact of IT innovation on incumbents; consistent with paper topic

## Model (lines 68–152)
- **Line 68** — section header
- **Line 74** [DEFINITION] OK — discrete time, absorbing singularity with probability p each period; well-defined
- **Lines 75–77** [DEFINITION] OK — pre-singularity growth equation Y_{t+1} = (1+g)Y_t
- **Lines 78–81** [DEFINITION] OK — post-singularity growth Y_{t+1} = (1+g̃)Y_t with g̃ > g
- **Line 82** [VERBAL] OK — "algebra holds for any g̃ > g" is accurate; propositions require only g̃ > g through existence conditions
- **Line 84** [VERBAL] OK — two-agent structure described consistently; GKP unborn-cohorts parallel is appropriately hedged as "inspired by"
- **Lines 88–92** [ARITHMETIC] OK — three output shares θ, ν, 1−θ−ν sum to 1; D^A + D^N + D^P = Y_t
- **Lines 94–97** [ARITHMETIC] OK — post-singularity shares θ̃, ν̃, 1−θ̃−ν̃ sum to 1
- **Lines 101–103** [ASSUMPTION] OK — Assumption 1: θ̃+ν̃ < θ+ν correctly formalizes household share falling
- **Lines 105–107** [ASSUMPTION] OK — Assumption 2: θ̃ > θ and ν̃ < ν; consistent with Assumption 1 (requires non-AI loss exceeds AI gain)
- **Lines 109–112** [DEFINITION] OK — ω ≡ θ+ν, ω̃ ≡ θ̃+ν̃, Δ ≡ ω̃/ω < 1 follows from Assumption 1
- **Line 113** [VERBAL] OK — correctly restates Assumption 1 in terms of Δ
- **Lines 117–120** [DEFINITION] OK — standard CRRA preferences with γ > 1, β ∈ (0,1)
- **Lines 122–126** [DEFINITION] OK — standard budget constraint with ex-dividend prices
- **Lines 128–132** [ARITHMETIC] OK — market clearing n^A = n^N = 1 implies c_t = D^A + D^N = (θ+ν)Y_t = ωY_t; post-singularity c_t = ω̃Y_t
- **Lines 134–137** [DEFINITION] OK — standard Euler equation P_t^i = E_t[β(c_{t+1}/c_t)^{−γ}(D_{t+1}^i + P_{t+1}^i)]
- **Line 138** [VERBAL] OK — hedging premium intuition is correct: Δ < 1 raises SDF in singularity states; AI stocks pay more in those states
- **Line 142** [VERBAL] OK — PD ratios constant within each regime because growth rates and transition probabilities are time-invariant
- **Line 145** [ARITHMETIC] OK — (1−p)β(1+g)^{1−γ} < 1 ensures pre-singularity PD denominator > 0; β(1+g̃)^{1−γ} < 1 ensures post-singularity PD denominator > 0
- **Line 148** [VERBAL] OK — for γ > 1 and positive growth: (1+g)^{1−γ} < 1, so β(1+g)^{1−γ} < 1 and (1−p)β(1+g)^{1−γ} < 1; similarly for g̃

## Results (lines 153–225)
- **Line 153** — section header
- **Lines 155–172** [DEFINITION] OK — Proposition 1 defines V_pre^A, V_pre^N, R, Φ^A, Φ^N, V_post
- **Line 158** [ARITHMETIC] OK — V_pre^A formula verified by solving Euler equation fixed point
- **Line 162** [ARITHMETIC] OK — V_pre^N formula identical structure with Φ^N replacing Φ^A
- **Line 166** [ARITHMETIC] OK — R = β(1+g)^{1−γ}; numerically 0.96×(1.02)^{−2} ≈ 0.9227
- **Line 167** [ARITHMETIC] OK — Φ^A = β·Δ^{−γ}·(1+g̃)^{1−γ}·(θ̃/θ); verified from Euler equation singularity branch
- **Line 168** [ARITHMETIC] OK — Φ^N = β·Δ^{−γ}·(1+g̃)^{1−γ}·(ν̃/ν)
- **Line 169** [ARITHMETIC] OK — V_post = β(1+g̃)^{1−γ}/[1−β(1+g̃)^{1−γ}]; verified from post-singularity Euler equation
- **Line 171** [VERBAL] OK — "V_post is the common post-singularity PD ratio": correct, both AI and non-AI stocks satisfy the same Euler equation post-singularity since dividend and consumption growth are both (1+g̃)
- **Line 175** [ARITHMETIC] OK — post-singularity proof: V_post = β(1+g̃)^{1−γ}(1+V_post) solves to eq (9)
- **Line 181** [ARITHMETIC] OK — no-singularity branch: SDF×dividend_growth = β(1+g)^{−γ}·(1+g) = R; singularity branch: SDF×dividend_growth = β[Δ(1+g̃)]^{−γ}·(θ̃/θ)(1+g̃) = Φ^A; fixed-point solution yields eq (8)
- **Line 184** [VERBAL] OK — Δ^{−γ} > 1 since Δ < 1 and γ > 0
- **Line 184** [VERBAL] OK — V_pre^A > V_pre^N: same denominator, Φ^A > Φ^N because θ̃/θ > ν̃/ν by Assumption 2
- **Line 184** [VERBAL] OK — "valuation spread increases with p": spread = p(Φ^A−Φ^N)(1+V_post)/[1−(1−p)R], derivative w.r.t. p is positive
- **Line 184** [VERBAL] OK — "spread increases with displacement severity (1−Δ)": Φ^A−Φ^N is proportional to Δ^{−γ}, which increases as Δ decreases
- **Line 189** [ARITHMETIC] OK — ∂V_pre^A/∂p > 0 iff Φ^A(1+V_post)(1−R) − R > 0 iff Φ^A(1+V_post) > R/(1−R); verified by quotient rule, numerator simplifies to expression independent of p
- **Line 191** [ARITHMETIC] OK — R/(1−R) = V_pre^A|_{p=0} by direct substitution into eq (8)
- **Line 191** [VERBAL] OK — comparative statics on Δ (small → LHS large), θ̃/θ (large → LHS large), g̃ (very large → LHS → 0 for γ > 1) are all correct
- **Line 198** [VERBAL] OK — economic interpretation consistent with the iff condition
- **Line 201** [VERBAL] OK — under complete markets c_t = Y_t (household consumes all output)
- **Line 205** [ARITHMETIC] OK — Φ^{A,CM} = β(1+g̃)^{1−γ}(θ̃/θ) is Φ^A with Δ^{−γ} replaced by 1 (no displacement under CM)
- **Line 207** [ARITHMETIC] OK — hedging premium = p·β·(1+g̃)^{1−γ}·(θ̃/θ)·(Δ^{−γ}−1)·(1+V_post)/[1−(1−p)R] > 0; verified algebraically and numerically
- **Line 209** [VERBAL] OK — premium increasing in p, θ̃/θ, and 1−Δ; all three hold analytically
- **Line 213** [VERBAL] OK — complete-markets proof logic is correct
- **Line 219** [ARITHMETIC] OK — ω = 0.60, ω̃ = 0.45, Δ = 0.75; all correct
- **Line 219** [ARITHMETIC] OK — V_pre^A ≈ 16.1 at p=0.01; recomputed ≈ 16.10
- **Line 219** [ARITHMETIC] OK — V_pre^N ≈ 11.6 at p=0.01; recomputed ≈ 11.57
- **Line 219** [ARITHMETIC] OK — ratio ≈ 1.4; recomputed 16.10/11.57 ≈ 1.39
- **Line 219** [ARITHMETIC] OK — both ≈ 11.9 at p=0; recomputed R/(1−R) ≈ 11.94
- **Line 219** [ARITHMETIC] OK — V_pre^{A,CM} ≈ 12.9; recomputed ≈ 12.90
- **Line 219** [ARITHMETIC] OK — hedging premium ≈ 25% of CM valuation; recomputed (16.10−12.90)/12.90 ≈ 24.8%
- **Line 221** [FIGURE/TABLE] OK — all five rows of Table 1 match recomputed values to 1 decimal place

## Extension: Singularity, Extinction, and Frictions (lines 226–266)
- **Line 226** — section header
- **Line 228** [VERBAL] OK — accurately describes the two extension directions (extinction risk, overcoming frictions)
- **Line 234** [ARITHMETIC] OK — extinction formula verified: singularity branch splits into survival (prob p(1−q), contributes p(1−q)Φ^A(1+V_post)) and extinction (prob pq, contributes 0); solving the fixed point yields eq (15)
- **Line 236** [VERBAL] OK — as q→1, (1−q)→0, singularity term vanishes; SDF/payoff convention in extinction (0·∞ = 0) is standard
- **Line 238** [VERBAL] ERROR — states "the household's consumption, though growing, remains a shrinking fraction ω̃ of total output." In the model, ω̃ ≡ θ̃+ν̃ is a fixed constant, not a shrinking fraction. Post-singularity, the household's share of output is permanently ω̃ each period. The word "shrinking" is incorrect; the correct description is that ω̃ is a fixed fraction smaller than ω.
- **Line 238** [VERBAL] OK — "with γ > 1, utility is bounded, and even infinite consumption generates finite utility": for CRRA with γ > 1, u(c) = c^{1−γ}/(1−γ) → 0 as c → ∞, which is finite
- **Line 241** [ARITHMETIC] OK — for γ > 1: (1+g̃)^{1−γ} → 0 as g̃ → ∞, so Φ^A → 0, V_post → 0, and hedging premium vanishes
- **Line 241** [ARITHMETIC] OK — for γ = 1: (1+g̃)^{1−γ} = 1 for all g̃, so Φ^A = β·Δ^{−1}·(θ̃/θ) and V_post = β/(1−β), both independent of g̃; premium is independent of g̃
- **Line 248** [REFERENCE] OK — GKP discuss bequests, government debt, intergenerational transfers affecting displacement factor magnitude (confirmed in GKP Section 3 discussion); GKP note representative dynasty with perfect altruism gives displacement factor = 1 (confirmed in GKP footnote 14); GKP do not formally analyze how these mechanisms scale with output (confirmed: they defer extensions to future work)
- **Lines 252–254** [ARITHMETIC] OK — transfer T = (ω−ω̃)Y; cost/output = F/Y + τ(ω−ω̃); algebra is correct
- **Line 256** [VERBAL] OK — as Y → ∞, F/Y → 0; qualitative claim about small τ is reasonable
- **Lines 258–260** [VERBAL] OK — Remark 2 correctly synthesizes: unbounded output makes fixed costs negligible, Coase theorem applies, displacement risk eliminated; "hedging premium largest for moderate singularities" follows from Remarks 1 and 2 jointly

## Conclusion (lines 267–278)
- **Line 267** — section header
- **Line 269** [VERBAL] OK — "expanding tradeable AI claims could reduce displacement premium" supported by Proposition 3
- **Line 269** [VERBAL] OK — "any mechanism that allows the household to share in AI upside reduces the hedging premium" is a qualitative paraphrase of Proposition 3's complete-markets result; the model formally proves only the polar cases (incomplete vs. complete), not partial mechanisms, but the claim is directionally supported
- **Line 269** [VERBAL] OK — "sufficiently abundant post-singularity output can make even modest transfer mechanisms effective" supported by Remark 2
- **Line 271** [VERBAL] OK — "omits heterogeneous households": model has one representative household
- **Line 271** [VERBAL] OK — "omits production-side frictions": no production function in the model
- **Line 271** [VERBAL] OK — "omits endogenous innovation": singularity probability p is exogenous
- **Line 271** [VERBAL] OK — "hedging premium is largest for moderate singularities" supported by Remarks 1 (utility saturation for extreme g̃) and 2 (abundance overcomes frictions)

## Proofs (lines 279–294)
- **Line 279** — appendix header
- **Line 282** [DEFINITION] OK — N(p) and D(p) match numerator and denominator of eq (8)
- **Line 286** [ARITHMETIC] OK — N'(p) = −R + Φ^A(1+V_post); D'(p) = R; both correct by direct differentiation
- **Lines 288–290** [ARITHMETIC] OK — quotient-rule numerator expands and simplifies to Φ^A(1+V_post)(1−R) − R; verified: cross-terms in (1−p) and p cancel because (1−p)+p = 1
- **Line 292** [ARITHMETIC] OK — sign condition Φ^A(1+V_post) > R/(1−R) follows from the numerator expression; R/(1−R) = V_pre^A|_{p=0} by direct substitution
