# tests/factcheck-bysection.py
Started: 2026-04-02 22:13:44 EDT
Runtime: 4m 54s
[ralph-garage/agent-logs/20260402T221344.370061-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260402T221344.370061-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong.

## Introduction (lines 41–68)

- **Line 41** — section header
- **Line 43** [VERBAL] OK — stylized fact about AI stock valuations 2023–2025 is well-known and supported by Figure 1
- **Line 43** [VERBAL] OK — "we propose an additional channel: publicly traded AI stocks command a valuation premium because they serve as a hedge" — supported by Proposition 3
- **Line 48** [FIGURE/TABLE] OK — caption lists NVDA, MSFT, GOOGL, META, AMZN and trailing 12-month dividends; matches code in `code/ai-valuations-figure.R`
- **Line 52** [VERBAL] OK — "singularity could dramatically increase productivity while shifting the economy's structure, displacing traditional businesses" — supported by Assumptions 1–2
- **Line 52** [VERBAL] OK — "the typical investor cannot buy these assets" — supported by model setup (household cannot invest in private AI capital)
- **Line 54** [VERBAL] OK — "infinite-horizon, discrete-time asset pricing model" — confirmed at line 78, eq (7)
- **Line 54** [REFERENCE] OK — "following GKP2012, can be interpreted as future innovators" — GKP line 23 confirms future innovators who cannot trade with current agents
- **Line 54** [VERBAL] OK — "each period, with some probability, a singularity occurs" — confirmed by model at line 78
- **Line 56** [VERBAL] OK — "we derive the price-dividend ratio of AI stocks in closed form" — Proposition 1 provides explicit formula
- **Line 56** [VERBAL] OK — "the ratio increases with the probability of a singularity" — Proposition 2 proves this under condition (13)
- **Line 56** [VERBAL] OK — "hedging premium" mechanism described (high MU in singularity states, AI stocks pay more) — confirmed by Delta^{-gamma} > 1 and theta_tilde/theta > 1
- **Line 56** [VERBAL] OK — "Under complete markets, the household could invest in private AI capital, eliminating displacement risk and the hedging premium" — Proposition 3
- **Line 58** [REFERENCE] OK — "connect to Jones2024 on the trade-off between AI-driven growth and existential risk" — Jones (2024) summary confirms this topic
- **Line 58** [REFERENCE] OK — "the barriers to intergenerational risk-sharing emphasized by GKP2012" — GKP confirms intergenerational risk-sharing failure is central
- **Line 58** [VERBAL] OK — "the most extreme AI singularity reduces displacement risk" — Remark 1 confirms hedging premium vanishes as g_tilde → ∞ for gamma > 1
- **Line 58** [VERBAL] OK — "extinction risk attenuates the hedging premium" — eq (14) confirms factor (1-q)
- **Line 60** [VERBAL] OK — "paper specification—approximately 80 lines" — spec is 84 lines; "approximately 80" is accurate
- **Line 60** [VERBAL] OK — "the AI performed all economic modeling, derivations, writing, and typesetting" — consistent with spec section II.5.d
- **Line 63** [REFERENCE] OK — "GKP2012, who introduce displacement risk in an overlapping-generations economy with innovation" — confirmed by GKP abstract
- **Line 63** [REFERENCE] OK — "innovation creates a systematic risk factor because new entrants capture rents that existing agents cannot share" — GKP line 23 confirms
- **Line 63** [VERBAL] OK — "our contribution relative to GKP is purposefully modest" — matches spec requirement 6d
- **Line 63** [REFERENCE] OK — "KoganPapanikolaouStoffman2020 extend the displacement risk framework" — standard characterization
- **Line 63** [REFERENCE] OK — "KoganPapanikolaou2014 analyze how investment-specific technology shocks affect asset prices" — standard characterization
- **Line 65** [REFERENCE] OK — rare disasters literature citations (Rietz1988, Barro2006, Wachter2013) are canonical
- **Line 65** [VERBAL] OK — "asymmetric effects across sectors" distinguishes from standard disaster models — confirmed by the model
- **Line 67** [REFERENCE] OK — "Jones2024 analyzes the trade-off between AI-driven growth and existential risk, showing that the curvature of utility is central" — Jones summary line 25 confirms
- **Line 67** [REFERENCE] OK — remaining lit review citations (KorinekSuh2024, AcemogluRestrepo2018, PastorVeronesi2009, HobijnJovanovic2001) — standard characterizations; HobijnJovanovic2001 confirmed via GKP line 41

## Model (lines 72–153)

- **Line 72** — section header
- **Line 74** [VERBAL] OK — accurately describes section purpose
- **Line 78** [DEFINITION] OK — discrete time, absorbing singularity with probability p each period
- **Line 80** [DEFINITION] OK — pre-singularity growth equation
- **Line 84** [ASSUMPTION] OK — g_tilde > g stated; code uses 0.05 > 0.02
- **Line 86** [REFERENCE] OK — "the extension explores the limit g_tilde → ∞" — confirmed at lines 244–245
- **Line 88** [REFERENCE] OK — GKP interpretation of AI owners as future innovators confirmed by GKP
- **Line 88** [VERBAL] OK — carefully distinguishes paper's own modeling choice from GKP's mechanism
- **Line 92** [DEFINITION] OK — three dividend streams with shares theta, nu, 1-theta-nu summing to 1
- **Line 94** [ARITHMETIC] OK — D^A + D^N + D^P = theta*Y + nu*Y + (1-theta-nu)*Y = Y
- **Line 100** [ARITHMETIC] OK — post-singularity shares sum to 1
- **Line 106** [DEFINITION] OK — Assumption 1: tilde_theta + tilde_nu < theta + nu; code: 0.45 < 0.60
- **Line 110** [DEFINITION] OK — Assumption 2: tilde_theta > theta and tilde_nu < nu; code: 0.15 > 0.05, 0.30 < 0.55
- **Line 113** [ARITHMETIC] OK — omega = theta + nu = 0.60, tilde_omega = tilde_theta + tilde_nu = 0.45
- **Line 115** [ARITHMETIC] OK — Delta = 0.45/0.60 = 0.75 < 1
- **Line 117** [VERBAL] OK — correct restatement that Assumption 1 is equivalent to Delta < 1
- **Line 123** [DEFINITION] OK — CRRA utility with gamma > 1, beta in (0,1); code: gamma=3, beta=0.96
- **Line 128** [DEFINITION] OK — standard budget constraint with ex-dividend prices
- **Line 132** [VERBAL] OK — market clearing n^A = n^N = 1 follows from household being sole public investor
- **Line 134** [ARITHMETIC] OK — c_t = D^A + D^N = (theta + nu)*Y = omega*Y
- **Line 136** [VERBAL] OK — post-singularity: c_t = tilde_omega * Y
- **Line 140** [DEFINITION] OK — standard CRRA Euler equation
- **Line 142** [VERBAL] OK — correctly explains hedging mechanism: SDF high when AI stocks pay well
- **Line 146** [VERBAL] OK — P/D ratios constant within each regime because growth rates are constant
- **Line 149** [DEFINITION] OK — Assumption 3: existence conditions for finite P/D ratios
- **Line 152** [VERBAL] OK — "automatically satisfied for gamma > 1" — correct since all factors are strictly < 1 when gamma > 1, g > 0, g_tilde > 0, beta < 1, p > 0

## Results (lines 157–226)

- **Line 157** — section header
- **Line 160** [DEFINITION] OK — subscripts 0,1 on V denote pre- and post-singularity regimes, not time
- **Line 162** [ARITHMETIC] OK — V_0^A formula verified by re-derivation from Euler equation
- **Line 166** [ARITHMETIC] OK — V_0^N formula identical structure with nu_tilde/nu
- **Line 170** [DEFINITION] OK — R = beta*(1+g)^{1-gamma}; computed R = 0.9227
- **Line 171** [DEFINITION] OK — Phi^A = beta * Delta^{-gamma} * (1+g_tilde)^{1-gamma} * (theta_tilde/theta)
- **Line 172** [DEFINITION] OK — Phi^N analogous with nu_tilde/nu
- **Line 173** [DEFINITION] OK — V_1 = beta*(1+g_tilde)^{1-gamma} / [1 - beta*(1+g_tilde)^{1-gamma}]; computed V_1 = 6.737
- **Line 175** [VERBAL] OK — verbal descriptions of R, Phi^A, Phi^N, V_1 are accurate
- **Line 179** [ARITHMETIC] OK — post-singularity Euler equation V_1 = beta*(1+g_tilde)^{1-gamma}*(1+V_1) rearranges correctly
- **Line 185** [ARITHMETIC] OK — pre-singularity expansion: normal state contributes (1-p)*R*(1+V_0^A), singularity state contributes p*Phi^A*(1+V_1); solving yields eq (5)
- **Line 188** [VERBAL] OK — Delta < 1 ⟹ Delta^{-gamma} > 1; theta_tilde/theta = 3 > 1 > nu_tilde/nu = 0.545; hence V_0^A > V_0^N
- **Line 188** [VERBAL] OK — "valuation spread increases with singularity probability p" — confirmed by numerical table (Spread: 0.0, 2.4, 4.5, 8.2, 15.9)
- **Line 193** [ARITHMETIC] OK — condition Phi^A(1+V_1) > R/(1-R): LHS ≈ 47.9 > 11.9 ≈ RHS
- **Line 195** [VERBAL] OK — R/(1-R) = V_0^A|_{p=0} confirmed by substituting p=0 into eq (5)
- **Line 195** [VERBAL] OK — comparative statics in Delta, gamma, theta_tilde/theta are directionally correct
- **Line 207** [ARITHMETIC] OK — complete-markets formula with Phi^{A,CM} replacing Phi^A
- **Line 209** [DEFINITION] OK — Phi^{A,CM} = beta*(1+g_tilde)^{1-gamma}*(theta_tilde/theta) = Phi^A without Delta^{-gamma}
- **Line 211** [ARITHMETIC] OK — hedging premium formula V_0^A - V_0^{A,CM} verified; at p=0.01 gives ≈ 3.20
- **Line 213** [VERBAL] OK — hedging premium increasing in p, theta_tilde/theta, and (1-Delta) — all enter numerator positively
- **Line 217** [VERBAL] OK — under complete markets, consumption growth at singularity is (1+g_tilde) not Delta*(1+g_tilde), eliminating Delta^{-gamma}
- **Line 220** [VERBAL] OK — correctly identifies hedging premium as arising entirely from displacement channel
- **Line 223** [ARITHMETIC] OK — omega = 0.05 + 0.55 = 0.60
- **Line 223** [ARITHMETIC] OK — tilde_omega = 0.15 + 0.30 = 0.45
- **Line 223** [ARITHMETIC] OK — Delta = 0.45/0.60 = 0.75
- **Line 223** [ARITHMETIC] OK — V_0^A ≈ 16.1 at p=0.01; recomputed 16.098
- **Line 223** [ARITHMETIC] OK — V_0^N ≈ 11.6 at p=0.01; recomputed 11.567
- **Line 223** [ARITHMETIC] OK — "ratio of roughly 1.4"; 16.098/11.567 = 1.392 ≈ 1.4
- **Line 223** [ARITHMETIC] OK — "both equal approximately 11.9" at p=0; R/(1-R) = 11.940
- **Line 223** [ARITHMETIC] OK — V_0^{A,CM} ≈ 12.9 at p=0.01; recomputed 12.896
- **Line 223** [ARITHMETIC] OK — "hedging premium of about 25%"; (16.098-12.896)/12.896 = 24.8% ≈ 25%
- **Line 225** [FIGURE/TABLE] OK — all five rows of Table 1 verified against recomputation; Spread and Hedge Premium columns correct

## Extension: Singularity, Extinction, and Frictions (lines 230–267)

- **Line 230** — section header
- **Line 232** [REFERENCE] OK — accurately describes baseline model and two extension directions; Jones (2024) reference appropriate
- **Line 236** [DEFINITION] OK — extinction probability q conditional on singularity
- **Line 238** [ARITHMETIC] OK — extinction formula correctly modifies baseline by factor (1-q) on singularity term only
- **Line 240** [VERBAL] OK — "extinction risk reduces the singularity-state contribution by (1-q)" — directly from formula
- **Line 240** [VERBAL] OK — "in the limit q→1, singularity contributes nothing" — numerator term → 0, leaving no-singularity P/D ratio
- **Line 242** [REFERENCE] OK — Jones (2024) confirms that gamma > 1 means utility is bounded and infinite consumption generates finite utility
- **Line 242** [VERBAL] OK — "AI owners enjoy unbounded consumption" — their consumption (1-tilde_omega)*Y grows without bound
- **Line 242** [VERBAL] OK — "household's consumption...remains a shrinking fraction tilde_omega of total output" — tilde_omega < omega is a one-time drop at singularity; the fraction tilde_omega is fixed post-singularity, not progressively shrinking. Reading is slightly ambiguous but refers to the level shift from omega to tilde_omega.
- **Line 245** [ARITHMETIC] OK — for gamma > 1: (1+g_tilde)^{1-gamma} → 0 as g_tilde → ∞, so Phi^A → 0 and V_1 → 0
- **Line 245** [VERBAL] OK — "hedging premium vanishes" — follows from Phi^A → 0 and V_1 → 0 in eq (16)
- **Line 245** [VERBAL] OK — "household's marginal utility in singularity states becomes negligible because consumption is so high" — correct economic intuition
- **Line 245** [ARITHMETIC] OK — "for gamma = 1 (log utility), the premium is independent of g_tilde" — (1+g_tilde)^0 = 1, so Phi^A and V_1 do not depend on g_tilde. Note: gamma = 1 is outside the model's stated assumption gamma > 1, but the remark is a valid mathematical observation about the formula.
- **Line 248** [VERBAL] OK — correctly summarizes parallel with Jones (2024) on curvature of utility
- **Line 252** [REFERENCE] OK — "GKP assume that intergenerational risk-sharing fails due to frictions" — confirmed by GKP
- **Line 252** [REFERENCE] OK — "GKP discuss how mechanisms such as bequests, government debt, and intergenerational transfers would affect the magnitude of the displacement factor" — confirmed by GKP p.16–17: "extensions of the model that would allow for bequests and gifts across generations, government debt, intergenerational transfers mandated by the government...would only affect the magnitude of the displacement factor"
- **Line 252** [REFERENCE] OK — "in a representative dynasty with perfect altruism the displacement factor equals one" — confirmed by GKP footnote 14
- **Line 252** [VERBAL] OK — GKP "do not conduct a formal analysis of how these mechanisms scale with output" — correct; GKP's treatment is in a footnote
- **Line 254** [VERBAL] OK — Coase theorem statement is standard and correctly applied
- **Line 254** [ARITHMETIC] OK — "with full transfers, Delta = 1 and the hedging premium vanishes" — eq (16) has (Delta^{-gamma} - 1) = 0 when Delta = 1
- **Line 258** [ARITHMETIC] OK — friction cost formula F/Y + tau*(omega - tilde_omega) verified
- **Line 260** [ARITHMETIC] OK — AI owners' gains: (1-tilde_omega)Y - (1-omega)Y = (omega - tilde_omega)Y; algebra correct
- **Line 260** [VERBAL] OK — "as Y → ∞, fixed component vanishes" — F/Y → 0
- **Line 260** [VERBAL] OK — net surplus positive when tau is small — (1-tau)*(omega - tilde_omega)*Y - F > 0 for large Y and tau < 1
- **Line 263** [VERBAL] OK — Remark 2: "hedging premium is largest for moderate singularities" — correct: extreme singularities eliminate premium via utility saturation (Remark 1) or abundance-enabled risk-sharing (this remark)

## Conclusion (lines 271–276)

- **Line 271** — section header
- **Line 273** [VERBAL] OK — "expanding the set of tradeable AI-related claims...could reduce the displacement premium" — supported by Proposition 3 (complete markets eliminate hedging premium)
- **Line 273** [VERBAL] OK — "sufficiently abundant post-singularity output can make even modest transfer mechanisms effective" — supported by Remark 2
- **Line 275** [VERBAL] OK — "the model is intentionally stylized" and acknowledged omissions (heterogeneous households, production frictions, endogenous innovation) — accurate self-assessment
- **Line 275** [VERBAL] OK — "hedging premium is largest for moderate singularities" — supported by Remarks 1 and 2

## Proofs (lines 283–297)

- **Line 283** — appendix header
- **Line 286** [ARITHMETIC] OK — N(p) = (1-p)R + p*Phi^A(1+V_1), D(p) = 1-(1-p)R match eq (5)
- **Line 290** [ARITHMETIC] OK — N'(p) = -R + Phi^A(1+V_1), D'(p) = R are correct derivatives
- **Line 292** [ARITHMETIC] OK — quotient rule expansion N'D - ND' correctly stated
- **Line 293** [ARITHMETIC] OK — intermediate simplification: (1-p)R^2 terms cancel, (1-p)+p=1 collapse in Phi^A coefficient
- **Line 294** [ARITHMETIC] OK — final numerator Phi^A(1+V_1)(1-R) - R is correct factoring
- **Line 296** [ARITHMETIC] OK — R/(1-R) = V_0^A|_{p=0} confirmed by substituting p=0 into eq (5)
- **Line 296** [VERBAL] OK — positive iff Phi^A(1+V_1) > R/(1-R) follows since 1-R > 0 by Assumption 3
