# tests/factcheck-bysection.py
Started: 2026-04-02 18:07:23 EDT
Runtime: 5m 7s
[ralph-garage/agent-logs/20260402T180723.871986-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260402T180723.871986-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: FAIL
REASON: Comparative statics claims about risk aversion (lines 190, 215) are unsupported by the formulas, gamma<1 limit claim (line 245) is outside valid parameter space, and a GKP quote (line 252) is inaccurate.

## Introduction (lines 41–64)
- **Line 41** — section header
- **Line 43** [VERBAL] OK — background claim about AI stock valuations; general and uncontroversial
- **Line 43** [VERBAL] OK — "trillions of dollars in market value, trading at price-dividend ratios far above historical norms" is well-known factual background
- **Line 43** [VERBAL] OK — thesis statement ("publicly traded AI stocks command a valuation premium because they serve as a hedge against a negative AI singularity") supported by Propositions 1 and 4
- **Line 45** [VERBAL] OK — description of representative investor consistent with model (Section 2.3, eq. 7)
- **Line 45** [VERBAL] OK — displacement at singularity consistent with Assumption 1 (tilde-omega < omega)
- **Line 45** [VERBAL] OK — private AI ventures inaccessible, consistent with model structure and GKP interpretation (line 78)
- **Line 47** [VERBAL] OK — "infinite-horizon, discrete-time" confirmed by Section 2.1 (line 69) and utility (eq. 6)
- **Line 47** [VERBAL] OK — two publicly traded assets confirmed by Section 2.2
- **Line 47** [REFERENCE] OK — GKP2012 interpretation as "future innovators who do not yet participate in public markets" confirmed by GKP text
- **Line 47** [VERBAL] OK — singularity mechanics (AI stocks gain share, non-AI shrink, household displaced) confirmed by Assumptions 1-2
- **Line 49** [VERBAL] OK — closed-form P/D ratio confirmed by Proposition 1 (eq. 10)
- **Line 49** [VERBAL] OK — "ratio increases with probability of singularity" is a simplification of the conditional result in Proposition 3; condition holds easily for reasonable parameters
- **Line 49** [VERBAL] OK — hedging premium mechanism (high marginal utility + higher AI payoff) confirmed by discussion after Proposition 1 (line 177)
- **Line 49** [VERBAL] OK — non-AI valuations fall with singularity probability; confirmed numerically (V0^N = 11.57 < V0(p=0) = 11.94)
- **Line 49** [VERBAL] OK — complete markets eliminate displacement risk; confirmed by Proposition 4
- **Line 51** [REFERENCE] OK — Jones (2024) connection on growth vs. existential risk confirmed by Section 4
- **Line 51** [VERBAL] OK — frictions overcome when surplus enormous; confirmed by Section 4.2 Coase argument
- **Line 51** [VERBAL] OK — "most extreme AI singularity reduces displacement risk" confirmed by Remark 1 (line 245, gamma > 1 case)
- **Line 51** [VERBAL] OK — extinction risk attenuates hedging premium; confirmed by Section 4.1 (eq. 16)
- **Line 53** [VERBAL] OK — AI authorship claim consistent with project structure; "80 lines" matches spec (paper-spec.md line 77)
- **Line 56** [REFERENCE] OK — GKP2012 introduces displacement risk in OLG economy with innovation; confirmed by GKP abstract
- **Line 56** [VERBAL] OK — "our contribution relative to GKP is purposefully modest" matches spec requirement
- **Line 56** [VERBAL] OK — contributions (comparative statics in p, conditions for overcoming frictions) confirmed by Proposition 3 and Section 4.2
- **Line 58** [REFERENCE] OK — Rietz (1988), Barro (2006), Wachter (2013) are canonical rare disasters references; bib entries correct
- **Line 58** [VERBAL] OK — sectoral asymmetry distinguishes model from standard disaster models; confirmed by Assumption 2 and Proposition 2
- **Line 60** [REFERENCE] OK — Jones (2024) on curvature of utility confirmed by Jones summary
- **Line 60** [REFERENCE] OK — Korinek and Suh (2024), Acemoglu and Restrepo (2018), Pastor and Veronesi (2009), Hobijn and Jovanovic (2001) all correctly characterized; bib entries verified

## Model (lines 65–145)
- **Line 65** — section header
- **Line 67** — subsection header "Environment"
- **Line 69** [DEFINITION] OK — discrete time, aggregate output Y_t, singularity absorbing with probability p in (0,1)
- **Line 71** [DEFINITION] OK — eq. (1): normal growth Y_{t+1} = (1+g)Y_t
- **Line 75** [DEFINITION] OK — eq. (2): post-singularity growth Y_{t+1} = (1+g_tilde)Y_t, g_tilde >= g
- **Line 78** [DEFINITION] OK — two agent types: representative household (marginal investor) and AI owners (private capital, outside public markets)
- **Line 78** [REFERENCE] OK — GKP interpretation of AI owners as future innovators confirmed by GKP text
- **Line 80** — subsection header "Assets and dividends"
- **Line 82** [DEFINITION] OK — three dividend streams with shares theta, nu, 1-theta-nu summing to 1
- **Line 84** [ARITHMETIC] OK — shares sum to 1: theta + nu + (1-theta-nu) = 1
- **Line 90** [ARITHMETIC] OK — post-singularity shares also sum to 1
- **Line 96** [ASSUMPTION] OK — Assumption 1: tilde-theta + tilde-nu < theta + nu; verified numerically (0.45 < 0.60)
- **Line 100** [ASSUMPTION] OK — Assumption 2: tilde-theta > theta and tilde-nu < nu; verified (0.15 > 0.05, 0.30 < 0.55)
- **Line 103** [DEFINITION] OK — omega = theta + nu, tilde-omega = tilde-theta + tilde-nu, displacement ratio Delta = tilde-omega/omega
- **Line 105** [ARITHMETIC] OK — Delta < 1 follows from Assumption 1; verified (0.75 < 1)
- **Line 107** [VERBAL] OK — "singularity displaces household by shifting output toward private AI capital" correct: private share rises from 1-omega to 1-tilde-omega
- **Line 109** — subsection header "Household's problem"
- **Line 111** [DEFINITION] OK — CRRA preferences with gamma > 1, beta in (0,1)
- **Line 113** [DEFINITION] OK — standard CRRA utility function
- **Line 116** [DEFINITION] OK — household trades AI and non-AI stocks, cannot invest in private AI capital
- **Line 118** [DEFINITION] OK — standard budget constraint with ex-dividend prices
- **Line 122** [ARITHMETIC] OK — market clearing n_t^A = n_t^N = 1; consumption c_t = D_t^A + D_t^N = omega Y_t
- **Line 126** [ARITHMETIC] OK — post-singularity consumption c_t = tilde-omega Y_t
- **Line 130** [DEFINITION] OK — standard CRRA Euler equation for ex-dividend price
- **Line 133** — subsection header "Equilibrium"
- **Line 135** [VERBAL] OK — P/D ratio constant within each regime because growth rates are deterministic within regimes
- **Line 138** [ASSUMPTION] OK — Assumption 3 (existence): (1-p)beta(1+g)^{1-gamma} < 1 and beta(1+g_tilde)^{1-gamma} < 1; verified numerically (0.913 < 1 and 0.871 < 1)
- **Line 141** [VERBAL] OK — "automatically satisfied for gamma > 1" is correct (though "sufficiently large g or g_tilde" is imprecise; any g >= 0 suffices)

## Results (lines 146–229)
- **Line 146** — section header
- **Line 148–165** [DEFINITION] OK — Proposition 1 defines V0^A, V0^N, R, Phi^A, Phi^N, V1
- **Line 151** [ARITHMETIC] OK — V0^A formula verified numerically: V0^A = [(0.99)(0.9227) + (0.01)(6.192)(1+6.737)] / [1-(0.99)(0.9227)] = 16.098
- **Line 155** [ARITHMETIC] OK — V0^N formula verified numerically: V0^N = 11.567
- **Line 159** [ARITHMETIC] OK — R = 0.96 * (1.02)^(-2) = 0.9227
- **Line 160** [ARITHMETIC] OK — Phi^A = 0.96 * (0.75)^(-3) * (1.05)^(-2) * 3 = 6.192
- **Line 161** [ARITHMETIC] OK — Phi^N = 0.96 * (0.75)^(-3) * (1.05)^(-2) * (0.30/0.55) = 1.126
- **Line 162** [ARITHMETIC] OK — V1 = 0.96*(1.05)^(-2) / (1 - 0.96*(1.05)^(-2)) = 0.8707/0.1293 = 6.737
- **Line 167–175** [ARITHMETIC] OK — Proof of Proposition 1: Euler equation expansion verified; algebra for both no-singularity and singularity branches correct
- **Line 177** [VERBAL] OK — Delta^{-gamma} > 1 because Delta < 1 and gamma > 0; tilde-theta/theta = 3 > 1; tilde-nu/nu = 0.545 < 1
- **Line 182–183** [ARITHMETIC] OK — Cross-section formula verified: V0^A - V0^N = 4.531; matches direct subtraction 16.098 - 11.567
- **Line 186–188** [ARITHMETIC] OK — Proof by subtraction; Phi^A - Phi^N positive by Assumption 2
- **Line 190** [VERBAL] **ERROR** — Claims "The valuation spread V0^A - V0^N increases with ... risk aversion gamma." Numerical check: spread = 6.82 at gamma=2, 4.53 at gamma=3, 3.19 at gamma=5, 3.05 at gamma=8. The spread DECREASES with gamma for these parameters because higher gamma shrinks (1+g_tilde)^{1-gamma}, V1, and the denominator, offsetting the increase in Delta^{-gamma}. Claims about increasing in p and (1-Delta) are correct.
- **Line 193–197** [ARITHMETIC] OK — Proposition 3 condition Phi^A(1+V1) > R/(1-R) verified: 47.9 >> 11.9
- **Line 197** [VERBAL] OK — sufficient conditions (Delta small, gamma large, tilde-theta/theta large) are qualitatively correct
- **Line 200–202** [REFERENCE] OK — proof deferred to Appendix; appendix proof verified
- **Line 204** [VERBAL] OK — economic interpretation consistent with formal condition
- **Line 209–211** [ARITHMETIC] OK — complete-markets formula: Phi^{A,CM} = beta(1+g_tilde)^{1-gamma}(tilde-theta/theta) = 2.612; V0^{A,CM} = 12.896
- **Line 213** [ARITHMETIC] OK — hedging premium formula verified: V0^A - V0^{A,CM} = 3.202
- **Line 215** [VERBAL] **ERROR** — Claims hedging premium is "increasing in risk aversion gamma." Numerical check: premium = 3.65 at gamma=2, 3.20 at gamma=3, 3.02 at gamma=4, 2.97 at gamma=5, then rising to 3.35 at gamma=8. The hedging premium is non-monotone in gamma. Same competing forces as line 190: Delta^{-gamma}-1 grows with gamma, but (1+g_tilde)^{1-gamma} and (1+V1) shrink.
- **Line 218–220** [ARITHMETIC] OK — complete-markets proof: Delta^{-gamma} replaced by 1; verified
- **Line 222** [VERBAL] OK — "gap isolates the hedging premium... arises entirely from the displacement channel" confirmed by eq. (13)
- **Line 225** [ARITHMETIC] OK — all numerical values verified:
  - omega = 0.60 (0.05+0.55)
  - tilde-omega = 0.45 (0.15+0.30)
  - Delta = 0.75 (0.45/0.60)
  - V0^A ≈ 16.1 (computed 16.098)
  - V0^N ≈ 11.6 (computed 11.567)
  - ratio ≈ 1.4 (computed 1.392)
  - no-singularity P/D ≈ 11.9 (R/(1-R) = 11.940)
  - V0^{A,CM} ≈ 12.9 (computed 12.896)
  - hedging premium ≈ 25% of CM valuation (computed 24.83%)

## Extension: Singularity, Extinction, and Frictions (lines 230–276)
- **Line 230** — section header
- **Line 232** [REFERENCE] OK — Jones (2024) on growth vs. existential risk verified
- **Line 236–239** [ARITHMETIC] OK — extinction formula (eq. 16) correctly multiplies singularity term by (1-q); normal-state and denominator unchanged
- **Line 240** [VERBAL] OK — "extinction risk reduces singularity-state contribution by factor (1-q)" directly visible from eq. 16; limit q->1 sends contribution to zero
- **Line 242** [REFERENCE] OK — Jones (2024) on curvature of utility confirmed; "gamma > 1 implies bounded utility" confirmed by Jones summary
- **Line 245** [ARITHMETIC] OK (gamma > 1) — as g_tilde -> infinity, (1+g_tilde)^{1-gamma} -> 0, so Phi^A -> 0 and V1 -> 0; hedging premium vanishes
- **Line 245** [ARITHMETIC] **ERROR** (gamma < 1) — claims "the hedging premium grows without bound" as g_tilde -> infinity. When gamma < 1, (1+g_tilde)^{1-gamma} -> infinity, violating Assumption 3 (beta(1+g_tilde)^{1-gamma} < 1). The P/D formulas are undefined in this limit. The claim reasons outside the model's valid parameter space without noting this.
- **Line 245** [ARITHMETIC] OK (gamma = 1) — with log utility, (1+g_tilde)^0 = 1, so Phi^A and V1 are independent of g_tilde; premium independent of g_tilde
- **Line 252** [REFERENCE] **ERROR** — presents as a direct quote: "bequests and gifts across generations, government debt, [and] intergenerational transfers." The actual GKP text reads: "bequests and gifts across generations, government debt, intergenerational transfers mandated by the government, or adjustable and depreciable physical and human capital." The quote omits "mandated by the government" and the entire last clause ("or adjustable and depreciable physical and human capital"), and changes the conjunction from "or" to "[and]." This should be a paraphrase (without quotes) or the quote should include ellipses for omitted material.
- **Line 256–258** [ARITHMETIC] OK — Delta(lambda) formula: Delta(0) = Delta_0 and Delta(1) = 1; boundary conditions verified
- **Line 258** [VERBAL] OK — "eliminating the hedging premium" when Delta = 1 gives Delta^{-gamma} - 1 = 0 in eq. (13)
- **Line 262–265** [ARITHMETIC] OK — friction cost F/Y + tau(omega - tilde-omega); as Y -> infinity, F/Y -> 0
- **Line 266** [ARITHMETIC] OK — AI owners' gains = (1-tilde-omega)Y - (1-omega)Y = (omega - tilde-omega)Y; algebra correct
- **Line 268–269** [VERBAL] OK — Remark 2: unbounded output makes fixed costs negligible; Coase theorem applies; premium largest for moderate singularities
- **Line 272** [VERBAL] OK — GKP framework most relevant for incremental innovation; abundance overcomes frictions for singularity-level events

## Conclusion (lines 277–292)
- **Line 277** — section header
- **Line 279** [VERBAL] OK — "hedging premium under incomplete markets" traces to Proposition 4, eq. (13)
- **Line 279** [VERBAL] OK — insurance properties of AI stocks trace to discussion after Proposition 1 (line 177)
- **Line 279** [VERBAL] OK — "premium increases with probability of singularity... severity of displacement" traces to Proposition 4; "increases with risk aversion" inherits the error from line 215 but is not independently checkable here
- **Line 279** [VERBAL] OK — "under complete markets, premium vanishes" traces to Proposition 4, Delta^{-gamma} -> 1
- **Line 281** [VERBAL] OK — "AI stocks should trade at higher P/D" traces to Proposition 2, eq. (11)
- **Line 281** [VERBAL] OK — "spread increasing in perceived singularity risk" traces to eq. (11) numerator containing p
- **Line 281** [VERBAL] OK — empirical consistency claim appropriately hedged
- **Line 283** [VERBAL] OK — "most extreme singularities reduce displacement risk" traces to Remark 2
- **Line 283** [VERBAL] OK — "hedging premium largest for moderate singularities" traces to Remarks 1 and 2 jointly
- **Line 285** [VERBAL] OK — policy implication follows logically from Proposition 4 (market completion eliminates premium)

## Proofs (lines 293–309)
- **Line 293** — appendix header
- **Line 295–296** [DEFINITION] OK — A(p) and B(p) correctly extracted from eq. (7)
- **Line 298** [ARITHMETIC] OK — quotient rule for dV0^A/dp
- **Line 300** [ARITHMETIC] OK — A'(p) = -R + Phi^A(1+V1) verified by direct differentiation
- **Line 300** [ARITHMETIC] OK — B'(p) = R verified by direct differentiation
- **Line 301–302** [ARITHMETIC] OK — numerator A'B - AB' correctly stated
- **Line 303** [ARITHMETIC] OK — cancellations verified: (1-p)R^2 terms cancel; (1-p) and p terms in Phi^A combine to -R*Phi^A(1+V1)
- **Line 304** [ARITHMETIC] OK — factored form Phi^A(1+V1)(1-R) - R verified
- **Line 306** [ARITHMETIC] OK — condition Phi^A(1+V1) > R/(1-R) equivalent to positive numerator (requires R < 1, which is implicit but standard)
- **Line 306** [ARITHMETIC] OK — R/(1-R) = V0^A|_{p=0} verified by substituting p=0 into eq. (7)
