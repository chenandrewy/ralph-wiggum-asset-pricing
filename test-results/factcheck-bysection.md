# tests/factcheck-bysection.py
Started: 2026-04-04 23:59:28 EDT
Runtime: 6m 54s
[ralph-garage/agent-logs/20260404T235928.976577-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260404T235928.976577-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic recomputed correctly; all verbal claims supported by formulas and tables; no material errors found.

## Introduction (lines 41–71)
- **Line 41** — section header
- **Line 43** [VERBAL] OK — "grown from under 10% to nearly 30%" describes Figure 1 (Magnificent 7 market cap share); consistent with CRSP data 2015–2024 and the code that generates fig-opening.pdf
- **Line 43** [REFERENCE] OK — no specific literature claim; general motivation
- **Line 46–53** [FIGURE/TABLE] OK — Figure 1 caption matches code: Magnificent 7 (Apple, Amazon, Alphabet, Meta, Microsoft, Nvidia, Tesla), monthly CRSP data Jan 2015–Dec 2024, NYSE/AMEX/NASDAQ common stocks
- **Line 55** [VERBAL] OK — describes the displacement mechanism: singularity increases total output but private AI capital owners capture gains, leaving the representative household displaced. Consistent with the model (equations 3–4)
- **Line 57** [VERBAL] OK — "infinite-horizon, discrete-time model" matches Section 2; "two assets trade publicly" matches Section 2.3; "closed-form expressions" confirmed by Proposition 2
- **Line 57** [REFERENCE] OK — cites GKP2012 for the analogy to unborn innovators; consistent with spec/lit context
- **Line 59** [VERBAL] OK — "hedging premium" established by Corollary 3 (eq. 7); "spread increases with singularity probability and severity of displacement" confirmed by Corollary 3 proof (increasing in p, decreasing in Lambda)
- **Line 59** [VERBAL] OK — "under incomplete markets, the premium is strictly larger" confirmed by Proposition 4 (eq. 9): amplification factor (1-phi)^(1-gamma) > 1
- **Line 61** [ARITHMETIC] OK — "5% annual singularity probability produces a P/D spread of 2.1": Panel A, p=0.05, spread = 2.12 rounds to 2.1
- **Line 61** [VERBAL] OK — "P/D ratios several times higher than non-AI stocks, with spreads exceeding 20": Panel B at p=0.05 gives spread 20.7; at p=0.10 gives 30.2. AI P/D of 41.6 vs Non-AI 11.4 at p=0.10 (ratio ~3.6x)
- **Line 63** [VERBAL] OK — summary of three extensions matches Sections 4.1–4.3
- **Line 63** [REFERENCE] OK — cites Jones2024 for "potentially infinite" output growth; consistent with paper-spec reference to Jones-2024-AERI
- **Line 63** [VERBAL] OK — "transfers that waste 90% of their value dramatically reduce displacement risk" supported by Figure 2 and the transfer formula (eq. 8): even with delta=0.9, Lambda = (1-0.9*phi)*G can exceed 1 for moderate G
- **Line 65** [VERBAL] OK — self-referential claim about AI-produced research; consistent with paper-spec IV.5.d
- **Line 68** [REFERENCE] OK — cites GKP2012 for displacement risk framework; describes their contribution as "innovation creates a systematic risk factor through incomplete intergenerational risk sharing"
- **Line 68** [REFERENCE] OK — "GKP note that government transfers would affect the magnitude of displacement but do not pursue this formally" — consistent with paper-spec VI.6.a
- **Line 68** [REFERENCE] OK — cites KoganPapanikolaouStoffman2020 and KoganPapanikolaou2014 for extensions of GKP framework
- **Line 70** [REFERENCE] OK — cites Jones2024 for AI growth and existential risk; PastorVeronesi2009/2006 for tech revolutions and stock prices; HobijnJovanovic2001 for IT displacement; Barro2006 for rare disasters; Nordhaus2021 for economic singularity; AghionJonesJones2019 and AcemogluRestrepo2018 for AI growth; Blanchard1985 and GarleanuPanageas2015 for OLG asset pricing. All are standard references in this literature.

## Model (lines 75–151)
- **Line 75** — section header
- **Line 80** [DEFINITION] OK — discrete time, t=0,1,2,...; representative household and AI capital owners
- **Line 84–90** [DEFINITION] OK — CRRA utility with discount factor beta, risk aversion gamma > 1, standard formulation
- **Line 93–99** [DEFINITION] OK — deterministic pre-singularity output Y_t = Y_0(1+g)^t; AI fraction alpha of publicly traded output
- **Line 101–102** [DEFINITION] OK — AI capital owners hold private, non-traded capital; not marginal investors
- **Line 102** [REFERENCE] OK — cites GKP2012 for analogy to unborn innovators
- **Line 106** [DEFINITION] OK — singularity probability p per period, one-time permanent event, constant hazard rate
- **Line 110** [DEFINITION] OK — output jumps by factor G > 1
- **Line 111** [DEFINITION] OK — AI owners capture fraction phi of post-singularity output
- **Line 112** [DEFINITION] OK — AI share increases from alpha to alpha_S > alpha
- **Line 113** [DEFINITION] OK — post-singularity growth continues at rate g
- **Line 118–119** [ARITHMETIC] OK — C_{tau+1} = (1-phi)*G*(1+g)*C_tau = Lambda*(1+g)*C_tau where Lambda = (1-phi)*G. Verified: household gets fraction (1-phi) of post-singularity output, which is G times pre-singularity output, growing at (1+g).
- **Line 124–126** [DEFINITION] OK — Lambda = (1-phi)*G
- **Line 128** [VERBAL] OK — "When Lambda < 1, the household's consumption falls despite a massive increase in total output" — correct since C_{tau+1}/C_tau = Lambda*(1+g); if Lambda < 1 and (1+g) is close to 1, consumption falls
- **Line 134–137** [DEFINITION] OK — AI stock dividend = alpha_t * Y_t^pub; Non-AI dividend = (1-alpha_t)*Y_t^pub; Y_t^pub defined correctly for pre- and post-singularity regimes
- **Line 139** [REFERENCE] OK — cites GKP2012 for the impossibility-of-trade friction
- **Line 143–149** [DEFINITION] OK — equilibrium definition: Euler equations (eq. 5) for both assets, market clearing
- **Line 151** [VERBAL] OK — "Post-singularity, the economy is a standard Gordon growth world" — correct since growth is deterministic at rate g after the singularity

## Results (lines 156–233)
- **Line 156** — section header
- **Line 160** [VERBAL] OK — "constant arrival probability" admits "clean closed form" — confirmed by Proposition 2
- **Line 162–176** [ARITHMETIC] OK — Proposition 2 (P/D ratios):
  - Eq. 6: P^i/D^i = (1-H^i)*V_0 + H^i*V_inf — verified by solving the Euler equation (Appendix proof)
  - Eq. 7: V_0 = (1-p)*R / (1-(1-p)*R), V_inf = R/(1-R), R = beta*(1+g)^(1-gamma) — all verified numerically: R=0.9227, V_inf=11.94
  - Eq. 7: H^A = (alpha_S/alpha)*Lambda^(1-gamma), H^N = ((1-alpha_S)/(1-alpha))*Lambda^(1-gamma) — verified
  - Condition R < 1: with beta=0.96, g=0.02, gamma=3: R=0.9227 < 1 ✓
- **Line 182** [VERBAL] OK — "weighted average of two benchmarks: V_0 (H=0 case) and V_inf (no singularity risk)" — at H=0: P/D = V_0; at H such that it equals 1: P/D = V_inf. Correct interpretation.
- **Line 182** [VERBAL] OK — "product of two forces: (i) dividend jump and (ii) Lambda^(1-gamma) reflecting marginal utility" — H^i is exactly this product
- **Line 182** [VERBAL] OK — "When gamma > 1 and Lambda < 1, marginal utility is very high in the singularity state" — Lambda^(1-gamma) with 1-gamma < 0 and Lambda < 1 gives Lambda^(negative) > 1, i.e., high SDF weight ✓
- **Line 184–194** [ARITHMETIC] OK — Corollary 3 (Hedging premium):
  - Eq. 7 spread formula: verified algebraically that (H^A - H^N) = (alpha_S - alpha)/(alpha*(1-alpha)) * Lambda^(1-gamma)
  - V_inf - V_0 = pR/((1-R)(1-(1-p)R)) — verified numerically
  - Full spread formula matches direct computation to 4+ decimal places
- **Line 189** [VERBAL] OK — "increasing in p": V_inf - V_0 is increasing in p (verified: derivative is positive). "Decreasing in Lambda" for gamma > 1: Lambda^(1-gamma) is decreasing in Lambda when 1-gamma < 0 ✓
- **Line 193** [ARITHMETIC] OK — inline proof: H^A - H^N > 0 when alpha_S > alpha ✓; V_inf - V_0 > 0 for p > 0 ✓; monotonicity arguments correct
- **Line 196** [VERBAL] OK — "premium grows with p" and "grows with displacement severity (lower Lambda)" — both confirmed by Corollary 3
- **Line 200** [ARITHMETIC] OK — under complete markets, Lambda^CM = G (household gets all output); SDF uses G instead of (1-phi)*G ✓
- **Line 202–211** [ARITHMETIC] OK — Proposition 4: Spread^IM/Spread^CM = Lambda^(1-gamma) / (Lambda^CM)^(1-gamma) = ((1-phi)*G)^(1-gamma) / G^(1-gamma) = (1-phi)^(1-gamma). For gamma > 1 and phi > 0: (1-phi)^(1-gamma) > 1 ✓
- **Line 213** [VERBAL] OK — "amplification factor can be very large when phi close to 1 and risk aversion is high" — e.g., phi=0.6, gamma=3: (0.4)^(-2) = 6.25 ✓
- **Line 217** [ASSUMPTION] OK — "baseline parameterization: beta=0.96, g=0.02, gamma=3, alpha=0.15, alpha_S=0.50" — matches code parameters (lines 107–111 of run-all.R) and table header
- **Line 225** [FIGURE/TABLE] OK — table-pd-ratios.tex matches recomputed values exactly (all numbers verified to 1 d.p.)
- **Line 228** [VERBAL] OK — table notes correctly describe the two panels and the spread definition
- **Line 231** [VERBAL] OK — "both P/D ratios decline with p" in Panel A: AI 11.9→8.7, Non-AI 11.9→5.6, both declining ✓
- **Line 231** [VERBAL] OK — "AI stocks decline much less": AI drops 3.3, Non-AI drops 6.3 ✓
- **Line 231** [ARITHMETIC] OK — "spread that reaches 3.1 at p=0.10": table shows 3.1 ✓ (recomputed: 3.09)
- **Line 233** [VERBAL] OK — "With Lambda=0.8, the singularity reduces the household's consumption to 80% of its pre-singularity level": Lambda=0.8 means consumption jump factor is 0.8, so consumption is 80% of counterfactual ✓
- **Line 233** [VERBAL] OK — "AI stocks' P/D ratio now increases with p": Panel B AI goes 11.9, 17.7, 22.4, 32.3, 41.6 ✓
- **Line 233** [ARITHMETIC] OK — "rising from 11.9 to 41.6": matches table endpoints at p=0 and p=0.10 ✓
- **Line 233** [ARITHMETIC] OK — "spread exceeds 30 at p=0.10": table shows 30.2 ✓ (recomputed: 30.21)

## Extensions (lines 238–307)
- **Line 238** — section header
- **Line 240** [VERBAL] OK — "extensions are independent of one another" — confirmed: each modifies baseline along one dimension
- **Line 244** [REFERENCE] OK — cites GKP2012 for the point that relevant capital may not yet exist
- **Line 246** [DEFINITION] OK — tax rate theta, deadweight cost delta, standard transfer mechanism
- **Line 248–249** [ARITHMETIC] OK — Lambda(theta,delta) = [(1-phi) + (1-delta)*theta*phi]*G. Verified:
  - theta=0: (1-phi)*G ✓
  - theta=1, delta=0: [(1-phi)+phi]*G = G ✓
  - theta=1, delta>0: [(1-phi)+(1-delta)*phi]*G = (1-delta*phi)*G ✓
- **Line 252** [ARITHMETIC] OK — all three special cases verified above
- **Line 254** [REFERENCE] OK — cites Jones2024 for "potentially infinite" output growth
- **Line 254** [VERBAL] OK — "even transfers that waste 90% of their value can dramatically reduce displacement risk" — with delta=0.9, phi=0.5: Lambda = (1-0.45)*G = 0.55*G; for G > 1/0.55 ≈ 1.82, Lambda > 1. Confirmed by Figure 2 code.
- **Line 257–264** [FIGURE/TABLE] OK — Figure 2 caption matches code: Proposition 2 with eq. 8 Lambda, theta=1, parameters beta=0.96, g=0.02, gamma=3, alpha=0.15, alpha_S=0.50, phi=0.50, p=0.05. Code confirms "No transfers" uses Lambda=(1-phi)*G. V_0 and V_inf reference lines present.
- **Line 266** [VERBAL] OK — "For low G, the no-transfer P/D ratio is very high": when G is small and (1-phi)*G < 1, Lambda^(1-gamma) is very large, pushing P/D far above V_inf ✓
- **Line 266** [VERBAL] OK — "all curves converge to V_0": as G→infinity, Lambda→infinity, so H→0, and P/D→V_0 ✓
- **Line 266** [VERBAL] OK — "even with delta=0.9, the P/D drops substantially relative to no-transfer baseline" — confirmed by the transfer formula: delta=0.9 gives a materially different Lambda from no-transfers for moderate G
- **Line 270** [DEFINITION] OK — veto mechanism: household blocks singularity at cost kappa*C_t per period
- **Line 272** [VERBAL] OK — "Under complete markets... the household never vetoes": Lambda^CM = G > 1, so singularity benefits household ✓ (Proposition 5a)
- **Line 274** [VERBAL] OK — "Under incomplete markets with Lambda < 1, the singularity reduces the household's consumption": by definition of Lambda < 1 ✓
- **Line 276–278** [VERBAL] OK — Proposition 5 statement matches the proof in the appendix (lines 354–366)
- **Line 284** [VERBAL] OK — "If government transfers raise Lambda above 1, the household no longer finds it rational to block" — follows from Proposition 5(a) logic: if Lambda > 1, consumption rises at singularity ✓
- **Line 288** [REFERENCE] OK — cites Jones2024 for existential risk from AI
- **Line 288** [DEFINITION] OK — extinction probability q conditional on singularity, q in [0,1)
- **Line 290** [VERBAL] OK — "hedge factor H^i is scaled by (1-q)" — equation 11 shows (1-q)*H^i replacing H^i ✓
- **Line 292–294** [ARITHMETIC] OK — equation 11 verified by re-deriving the Euler equation with extinction: the singularity term is multiplied by (1-q), giving (1-q)*H^i. Matches derivation.
- **Line 296–301** [ARITHMETIC] OK — Proposition 6: spread = (1-q)*(H^A - H^N)*(V_inf - V_0). Verified: this is exactly the original spread times (1-q), so strictly decreasing in q ✓
- **Line 307** [VERBAL] OK — "extinction destroys all assets equally, adding a state that provides no differential hedge" — in extinction, all payoffs are zero, so no differential valuation ✓

## Conclusion (lines 312–318)
- **Line 312** — section header
- **Line 314** [VERBAL] OK — summary of main result: "AI stocks hedge against a negative AI singularity under incomplete markets" — supported by Corollary 3 and Proposition 4
- **Line 314** [REFERENCE] OK — cites GKP2012 for displacement risk logic
- **Line 316** [VERBAL] OK — "illustrative parameterizations rather than formal calibration" — consistent with Table 1 usage and paper-spec IV.8.d
- **Line 318** [VERBAL] OK — self-referential claim about AI-produced paper; consistent with paper-spec IV.5.d. "Every equation, every line of code, and every paragraph was produced by AI agents working from a human specification" — accurate description per spec.

## Proofs (lines 329–367)
- **Line 329** — appendix header
- **Line 331–352** [ARITHMETIC] OK — Proof of Proposition 2:
  - Eq. 12: Gordon growth P/D = sum_{s=1}^inf beta^s (1+g)^{(1-gamma)s} = R/(1-R) = V_inf ✓
  - Eq. 13: Euler equation pi_N^i = (1-p)*R*(pi_N^i + 1) + p*R*H^i*(pi_S + 1) — verified: no-singularity term uses SDF beta*(1+g)^{-gamma} and dividend growth (1+g), giving R; singularity term uses SDF beta*(Lambda*(1+g))^{-gamma} and dividend growth (share_ratio)*Lambda*(1+g), giving R*H^i ✓
  - Line 342: "(pi_S + 1) = 1/(1-R)" — pi_S = R/(1-R), so pi_S + 1 = 1/(1-R) ✓
  - Eq. 14 solution: pi_N^i = V_0 + H^i*(V_inf - V_0) = (1-H^i)*V_0 + H^i*V_inf ✓
  - Line 352: V_inf - V_0 = pR/((1-R)(1-(1-p)R)) — verified algebraically and numerically ✓
- **Line 354–366** [ARITHMETIC] OK — Proof of Proposition 5:
  - Part (a): Lambda^CM = G > 1 implies consumption rises at singularity; household prefers not to veto ✓
  - Part (b): With Lambda < 1, eq. 17 defines kappa-bar via indifference condition. By strict concavity of u and Lambda < 1, the RHS of eq. 17 is strictly less than u((1+g)C_t), so kappa-bar > 0 ✓. Household vetoes for kappa < kappa-bar ✓
