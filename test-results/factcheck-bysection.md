# tests/factcheck-bysection.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 4m 24s
[ralph-garage/agent-logs/20260402T184535.059792-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260402T184535.059792-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All claims verified across all sections; no arithmetic, verbal, or reference errors found.

## Introduction (lines 41–71)

- **Line 41** — section header
- **Line 43** [VERBAL] OK — "recent surge in AI stock valuations" is a well-known factual claim
- **Line 43** [VERBAL] OK — "trillions of dollars in market value, trading at price-dividend ratios far above historical norms" consistent with public data and the paper's CRSP figure
- **Line 43** [FIGURE/TABLE] OK — Figure 1 references CRSP data for AI vs non-AI P/D ratios; underlying code queries exactly the five tickers named in the caption
- **Line 43** [VERBAL] OK — "We propose an additional channel: publicly traded AI stocks command a valuation premium because they serve as a hedge against a negative AI singularity" matches Proposition 4
- **Line 48** [FIGURE/TABLE] OK — caption lists NVDA, MSFT, GOOGL, META, AMZN and trailing 12-month dividends; matches code
- **Line 52** [VERBAL] OK — "representative investor whose wealth is largely tied to existing firms" matches model (household holds only public stocks)
- **Line 52** [VERBAL] OK — "displacing traditional businesses and reducing the investor's share of total output" matches Assumption 1 (Delta < 1)
- **Line 52** [VERBAL] OK — "Private AI ventures...the typical investor cannot buy these assets" matches model exclusion of private AI capital
- **Line 54** [VERBAL] OK — "infinite-horizon, discrete-time asset pricing model" matches Section 2
- **Line 54** [VERBAL] OK — "Two publicly traded assets" matches model
- **Line 54** [REFERENCE] OK — "following GKP (2012), can be interpreted as future innovators" consistent with GKP's unborn-cohorts mechanism
- **Line 54** [VERBAL] OK — "AI stocks gain a larger share...non-AI stocks shrink" matches Assumption 2
- **Line 54** [VERBAL] OK — "household is displaced---its consumption share falls" matches Assumption 1
- **Line 56** [REFERENCE] OK — "derive the price-dividend ratio of AI stocks in closed form" confirmed by Proposition 1
- **Line 56** [VERBAL] OK — "ratio increases with probability of singularity" matches Proposition 3
- **Line 56** [VERBAL] OK — hedging premium mechanism description matches model: Delta^{-gamma} > 1 and theta_tilde/theta > 1
- **Line 56** [VERBAL] OK — "valuation spread...widens with singularity probability" matches Proposition 2
- **Line 56** [VERBAL] OK — "Under complete markets...hedging premium" matches Proposition 4
- **Line 58** [REFERENCE] OK — "connect to Jones (2024) on the trade-off between AI-driven growth and existential risk" confirmed in Section 4
- **Line 58** [VERBAL] OK — "frictions that sustain displacement risk can be overcome" matches Section 4.2 and Remark 2
- **Line 58** [VERBAL] OK — "Even modest transfer mechanisms suffice when the surplus is enormous" matches eq. (28): F/Y → 0
- **Line 58** [VERBAL] OK — "most extreme AI singularity reduces displacement risk" matches Remark 1
- **Line 58** [VERBAL] OK — "extinction risk...hedging premium is attenuated" matches Section 4.1 eq. (18)
- **Line 60** [VERBAL] OK — "All analysis and writing were performed by AI agents working from a human-written specification" consistent with project structure
- **Line 60** [VERBAL] OK — "approximately 80 lines of instructions" — paper spec is 85 lines, consistent with "approximately 80"
- **Line 63** [REFERENCE] OK — "GKP (2012), who introduce displacement risk in an overlapping-generations economy with innovation" matches GKP
- **Line 63** [REFERENCE] OK — "innovation creates a systematic risk factor because new entrants capture rents that existing agents cannot share" matches GKP
- **Line 63** [VERBAL] OK — "Our contribution relative to GKP is purposefully modest" matches spec item I.6.d
- **Line 63** [REFERENCE] OK — "Kogan, Papanikolaou, and Stoffman (2020)" — JPE 2020 on creative destruction and inequality
- **Line 63** [REFERENCE] OK — "Kogan and Papanikolaou (2014)" — JF 2014 on technology shocks and asset prices
- **Line 65** [REFERENCE] OK — rare disasters literature (Rietz 1988, Barro 2006, Wachter 2013) correctly cited
- **Line 65** [VERBAL] OK — "asymmetric effects across sectors" is the correct distinction from standard disaster models
- **Line 67** [REFERENCE] OK — Jones (2024) description matches: curvature of utility central to growth vs existential risk trade-off
- **Line 67** [REFERENCE] OK — Korinek and Suh (2024) on AGI transition scenarios
- **Line 67** [REFERENCE] OK — Acemoglu and Restrepo (2018) on automation and labor
- **Line 67** [REFERENCE] OK — Pastor and Veronesi (2009) on technological revolutions and stock prices
- **Line 67** [REFERENCE] OK — Hobijn and Jovanovic (2001) on negative impact of IT innovation on incumbents

## Model (lines 72–153)

- **Line 72** — section header
- **Line 76** [DEFINITION] OK — discrete time, absorbing singularity with probability p each period
- **Lines 77–79** [DEFINITION] OK — normal growth equation Y_{t+1} = (1+g)Y_t
- **Lines 80–83** [DEFINITION] OK — post-singularity growth g_tilde > g
- **Line 84** [VERBAL] OK — "extension explores the limit g_tilde → ∞" confirmed by Remark 1
- **Line 86** [REFERENCE] OK — GKP interpretation as future innovators; paper correctly distinguishes its own extension
- **Lines 90–94** [ARITHMETIC] OK — output shares theta + nu + (1-theta-nu) = 1
- **Lines 96–99** [ARITHMETIC] OK — post-singularity shares sum to 1
- **Lines 103–105** [ASSUMPTION] OK — Assumption 1: tilde_theta + tilde_nu < theta + nu; verified with parameters (0.45 < 0.60)
- **Lines 107–109** [ASSUMPTION] OK — Assumption 2: tilde_theta > theta and tilde_nu < nu; verified (0.15 > 0.05, 0.30 < 0.55)
- **Lines 111–114** [DEFINITION] OK — omega = 0.60, tilde_omega = 0.45, Delta = 0.75 < 1
- **Line 115** [VERBAL] OK — correct restatement of Assumption 1 in terms of Delta
- **Lines 119–122** [DEFINITION] OK — standard CRRA utility with gamma > 1, beta in (0,1)
- **Lines 124–128** [DEFINITION] OK — standard budget constraint for Lucas-tree economy with ex-dividend pricing
- **Lines 130–134** [ARITHMETIC] OK — market clearing yields c_t = omega Y_t pre-singularity, tilde_omega Y_t post
- **Lines 136–139** [DEFINITION] OK — standard Euler equation
- **Line 143** [VERBAL] OK — PD ratio constant within each regime because growth rates are i.i.d.
- **Lines 145–147** [ASSUMPTION] OK — Assumption 3 ensures finite PD ratios; verified numerically ((1-0.01)(0.9224) = 0.913 < 1; 0.871 < 1)
- **Line 149** [VERBAL] OK — "automatically satisfied for gamma > 1" is correct since (1+g)^{1-gamma} ≤ 1 for g ≥ 0, gamma > 1

## Results (lines 154–239)

- **Line 154** — section header
- **Line 159** [ARITHMETIC] OK — formula (9) for V0^A correctly derived from Euler equation
- **Line 163** [ARITHMETIC] OK — formula (10) for V0^N identical structure with Phi^N
- **Line 167** [DEFINITION] OK — R = beta(1+g)^{1-gamma}
- **Line 168** [DEFINITION] OK — Phi^A = beta · Delta^{-gamma} · (1+g_tilde)^{1-gamma} · (theta_tilde/theta)
- **Line 169** [DEFINITION] OK — Phi^N analogous with nu_tilde/nu
- **Line 170** [DEFINITION] OK — V1 = beta(1+g_tilde)^{1-gamma} / (1 - beta(1+g_tilde)^{1-gamma})
- **Line 176** [ARITHMETIC] OK — post-singularity Euler equation solved correctly to yield V1
- **Line 182** [ARITHMETIC] OK — no-singularity branch contributes (1-p)R(1+V0^A); singularity branch contributes p·Phi^A·(1+V1); solved correctly
- **Line 185** [VERBAL] OK — Delta^{-gamma} > 1 because Delta < 1; theta_tilde/theta > 1; nu_tilde/nu < 1
- **Line 190** [ARITHMETIC] OK — cross-section formula from subtracting (10) from (9); positive since theta_tilde/theta > 1 > nu_tilde/nu
- **Line 198** [VERBAL] OK — spread increases with p and with displacement severity
- **Line 203** [ARITHMETIC] OK — comparative static condition derived correctly; R/(1-R) = V0^A at p=0
- **Line 205** [VERBAL] OK — condition holds when Delta small, gamma large, or theta_tilde/theta large
- **Line 215** [ASSUMPTION] OK — complete markets: c_t = Y_t, eliminating displacement
- **Line 219** [DEFINITION] OK — Phi^A_CM = beta(1+g_tilde)^{1-gamma}(theta_tilde/theta), i.e., Phi^A without Delta^{-gamma}
- **Line 221** [ARITHMETIC] OK — hedging premium formula verified: positive because Delta^{-gamma} > 1
- **Line 223** [VERBAL] OK — premium increasing in p, theta_tilde/theta, and 1-Delta

### Numerical illustration (line 233 and Table 1)

Parameters: beta=0.96, gamma=3, g=0.02, g_tilde=0.05, theta=0.05, theta_tilde=0.15, nu=0.55, nu_tilde=0.30.
Intermediate values: omega=0.60, tilde_omega=0.45, Delta=0.75, R≈0.9224, V1≈6.737, Delta^{-gamma}≈2.370.

- **Line 233** [ARITHMETIC] OK — omega=0.60 falling to tilde_omega=0.45, Delta=0.75
- **Line 233** [ARITHMETIC] OK — "At p=0.01, V0^A ≈ 16.1" — recomputed: 16.1
- **Line 233** [ARITHMETIC] OK — "V0^N ≈ 11.6" — recomputed: 11.6
- **Line 233** [ARITHMETIC] OK — "a ratio of roughly 1.4" — 16.1/11.6 ≈ 1.39, consistent
- **Line 233** [ARITHMETIC] OK — "Without singularity risk (p=0), both equal approximately 11.9" — recomputed: 11.9
- **Line 233** [ARITHMETIC] OK — "Under complete markets, V0^A_CM ≈ 12.9" — recomputed: 12.9
- **Line 233** [ARITHMETIC] OK — "hedging premium of about 25%" — recomputed: 24.8%, consistent with "about 25%"
- **Table row p=0.000** [FIGURE/TABLE] OK — V0^A=11.9, V0^N=11.9, V0^A_CM=11.9, Spread=0.0, Hedge Prem=0.0%
- **Table row p=0.005** [FIGURE/TABLE] OK — V0^A=14.1, V0^N=11.7, V0^A_CM=12.4, Spread=2.4, Hedge Prem=13.6%
- **Table row p=0.010** [FIGURE/TABLE] OK — V0^A=16.1, V0^N=11.6, V0^A_CM=12.9, Spread=4.5, Hedge Prem=24.8%
- **Table row p=0.020** [FIGURE/TABLE] OK — V0^A=19.5, V0^N=11.3, V0^A_CM=13.7, Spread=8.2, Hedge Prem=42.3%
- **Table row p=0.050** [FIGURE/TABLE] OK — V0^A=26.5, V0^N=10.6, V0^A_CM=15.3, Spread=15.9, Hedge Prem=73.4%

## Extension: Singularity, Extinction, and Frictions (lines 240–280)

- **Line 240** — section header
- **Line 242** [VERBAL] OK — correctly states baseline treats singularity with certainty of survival
- **Lines 246–248** [ARITHMETIC] OK — extinction risk formula: singularity contribution multiplied by (1-q); correctly derived from modifying baseline
- **Line 250** [VERBAL] OK — "Extinction risk reduces the singularity-state contribution by the factor (1-q)"
- **Line 250** [VERBAL] OK — limit q→1: singularity term vanishes
- **Line 252** [REFERENCE] OK — Jones (2024) on curvature of utility and AI growth vs existential risk
- **Line 252** [VERBAL] OK — "With gamma > 1, utility is bounded, even infinite consumption generates finite utility" — correct: u(c) = c^{1-gamma}/(1-gamma) → 0 as c → ∞
- **Line 252** [VERBAL] OK — "AI owners enjoy unbounded consumption" while household gets fixed fraction tilde_omega
- **Lines 254–256** [ARITHMETIC] OK — Remark 1: as g_tilde → ∞ with gamma > 1, (1+g_tilde)^{1-gamma} → 0, so Phi^A → 0 and V1 → 0
- **Line 255** [ARITHMETIC] OK — for gamma = 1: (1+g_tilde)^0 = 1, so premium is independent of g_tilde
- **Line 258** [VERBAL] OK — parallel to Jones correctly drawn
- **Line 262** [REFERENCE] OK — GKP's assumption of intergenerational risk-sharing failure accurately described
- **Line 262** [REFERENCE] OK — GKP's discussion of bequests, government debt, and dynasty case accurately characterized; claim that GKP do not formally analyze scaling with output is accurate
- **Lines 266–268** [ARITHMETIC] OK — friction cost formula: [F + tau(omega-tilde_omega)Y]/Y = F/Y + tau(omega-tilde_omega)
- **Line 270** [ARITHMETIC] OK — AI owners' gains: (1-tilde_omega)Y - (1-omega)Y = (omega-tilde_omega)Y
- **Lines 272–274** [VERBAL] OK — Remark 2: as Y → ∞, F/Y → 0; Coase theorem applies; displacement risk eliminated
- **Line 273** [VERBAL] OK — "hedging premium is largest for moderate singularities" follows from Remarks 1 and 2

## Conclusion (lines 281–296)

- **Line 281** — section header
- **Line 283** [VERBAL] OK — "hedging premium under incomplete markets" proven in Proposition 4
- **Line 283** [VERBAL] OK — "unable to invest in private AI capital" matches model setup
- **Line 283** [VERBAL] OK — "pay relatively more in singularity states when marginal utility is high" supported by Delta^{-gamma} > 1 and theta_tilde/theta > 1
- **Line 283** [VERBAL] OK — "When displacement is sufficiently severe, PD ratio increases with singularity probability" matches Proposition 3 condition
- **Line 283** [VERBAL] OK — "valuation spread widens" matches Proposition 2
- **Line 283** [VERBAL] OK — "Under complete markets, the premium vanishes" matches Proposition 4
- **Line 285** [VERBAL] OK — cross-sectional prediction follows from Proposition 2
- **Line 285** [VERBAL] OK — "consistent with elevated valuations" appropriately hedged
- **Line 287** [REFERENCE] OK — Remark 1 channel (utility curvature) accurately summarized
- **Line 287** [REFERENCE] OK — Remark 2 channel (Coasean bargaining) accurately summarized
- **Line 287** [VERBAL] OK — "hedging premium is largest for moderate singularities" follows from both channels
- **Line 289** [VERBAL] OK — "expanding tradeable AI-related assets could reduce the displacement premium" follows from complete-markets result

## Proofs (lines 297–313)

- **Line 297** — section header; label `app:proofs` matches reference on line 209
- **Line 300** [DEFINITION] OK — A(p) and B(p) correctly decompose equation (9)
- **Line 302** [ARITHMETIC] OK — standard quotient rule correctly applied
- **Line 304** [ARITHMETIC] OK — A'(p) = -R + Phi^A(1+V1); B'(p) = R; both correct
- **Line 306** [ARITHMETIC] OK — numerator A'B - AB' correctly expanded
- **Line 307** [ARITHMETIC] OK — simplifies to -R + Phi^A(1+V1) - R·Phi^A(1+V1); verified by full expansion
- **Line 308** [ARITHMETIC] OK — factors to Phi^A(1+V1)(1-R) - R
- **Line 310** [ARITHMETIC] OK — positive iff Phi^A(1+V1) > R/(1-R); division valid since 1-R > 0 by Assumption 3
- **Line 310** [ARITHMETIC] OK — R/(1-R) = V0^A at p=0: setting p=0 in eq. (9) gives V0^A = R/(1-R)
