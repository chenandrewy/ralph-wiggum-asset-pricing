# tests/factcheck-bysection.py
Started: 2026-04-04 23:45:08 EDT
Runtime: 5m 2s
[ralph-garage/agent-logs/20260404T234508.982982-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260404T234508.982982-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic, formulas, and table values are correct; a few minor verbal imprecisions do not rise to material errors.

## Introduction (lines 41–74)
- **Line 41** — section header
- **Line 43** [FIGURE/TABLE] OK — "under 10%" at start: opening figure shows ~8% in early 2015
- **Line 43** [FIGURE/TABLE] OK — "nearly 30%": figure shows ~30% by end-2024
- **Line 43** [VERBAL] CAUTION — "in less than a decade": data covers Jan 2015–Dec 2024, which is exactly 10 years (one decade), not strictly "less than." Borderline; consider "in about a decade."
- **Line 43** [VERBAL] OK — "financial market solutions remain under-discussed" supported by spec and absence of cited asset-pricing work on AI singularity risk
- **Line 43** [VERBAL] OK — main argument (AI stocks hedge displacement) matches spec I.3.a
- **Line 55** [VERBAL] OK — singularity increases total output (G > 1) and displaces household (phi > 0) consistent with model
- **Line 55** [VERBAL] OK — AI stocks partially hedge because alpha_S > alpha
- **Line 57** [VERBAL] OK — "infinite-horizon, discrete-time model" matches spec I.4.a
- **Line 57** [VERBAL] OK — two agents, two public assets match spec I.4.b–c
- **Line 57** [REFERENCE] OK — GKP2012 analogy to unborn innovators confirmed in spec/lit/GKP-2012.md
- **Line 57** [VERBAL] OK — "closed-form expressions" confirmed by Proposition 2
- **Line 59** [VERBAL] OK — hedging premium (AI P/D > non-AI P/D for p > 0) confirmed by table
- **Line 59** [VERBAL] OK — spread increases with p and displacement severity confirmed by table
- **Line 59** [VERBAL] OK — incomplete markets amplify premium confirmed by Proposition 4
- **Line 61** [ARITHMETIC] OK — "5% annual singularity probability produces a P/D spread of 2.1": Panel A at p = 0.05 shows spread = 2.1
- **Line 61** [ARITHMETIC] OK — "spreads exceeding 20": Panel B at p = 0.05 shows spread = 20.7
- **Line 61** [VERBAL] OK — "AI stocks can trade at P/D ratios several times higher": Panel B at p = 0.10 gives 41.6 vs 11.4 (3.65×)
- **Line 63** [REFERENCE] OK — Jones (2024) reference for potentially infinite output growth matches spec I.5.a.iii
- **Line 63** [VERBAL] OK — "transfers that waste 90% of their value" claim supported by Figure 3 (delta = 0.9 curve)
- **Line 63** [VERBAL] OK — household may block singularity under incomplete markets matches spec I.5.b
- **Line 63** [VERBAL] OK — extinction dilutes hedging premium matches spec I.5.c
- **Line 65** [VERBAL] OK — AI-agent production claim matches spec IV.5.d
- **Line 65** [VERBAL] CAUTION — "600-word economic specification": spec Section I is ~679 words; "600" is a modest understatement but within reasonable rounding
- **Line 65** [VERBAL] OK — self-referential displacement argument consistent with spec
- **Line 68** [REFERENCE] OK — GKP2012 "show that innovation creates a systematic risk factor through incomplete intergenerational risk sharing" confirmed in GKP-2012.md
- **Line 68** [REFERENCE] OK — GKP note transfers would affect displacement magnitude but don't pursue formally; confirmed in GKP-2012.md
- **Line 68** [VERBAL] OK — contribution characterization (three extensions) matches spec I.6
- **Line 70** [REFERENCE] OK — Jones (2024) AI growth and existential risk characterization consistent with spec
- **Line 70** [REFERENCE] OK — all other literature citations (Pastor & Veronesi, Hobijn & Jovanovic, Barro, Nordhaus, Aghion et al., Acemoglu & Restrepo, Blanchard, Garleanu & Panageas) have standard characterizations

## Model (lines 75–153)
- **Line 75** — section header
- **Line 79** [DEFINITION] OK — discrete time, representative household and AI capital owners
- **Line 82** [ASSUMPTION] OK — CRRA preferences with gamma > 1
- **Lines 84–86** [DEFINITION] OK — utility function is standard CRRA
- **Line 88** [ASSUMPTION] OK — beta in (0,1), gamma > 1, household is marginal investor
- **Lines 93–95** [DEFINITION] OK — deterministic output growth Y_t = Y_0(1+g)^t
- **Line 97** [ASSUMPTION] OK — g > 0, alpha in (0,1) is AI share of publicly traded output
- **Line 100** [REFERENCE] OK — analogy to GKP2012 unborn innovators confirmed
- **Line 100** [VERBAL] OK — AI owners not marginal investors, don't appear in Euler equation
- **Line 104** [ASSUMPTION] OK — geometric arrival probability p in (0,1), one-time permanent event
- **Line 108** [ASSUMPTION] OK — output jumps by factor G > 1
- **Line 109** [ASSUMPTION] OK — AI owners capture fraction phi in (0,1)
- **Line 110** [ASSUMPTION] OK — AI share increases from alpha to alpha_S > alpha
- **Line 111** [ASSUMPTION] OK — post-singularity growth continues at rate g
- **Line 117** [ARITHMETIC] OK — C_{tau+1} = (1-phi)*G*(1+g)*C_tau = Lambda*(1+g)*C_tau verified from output and dividend definitions
- **Line 123** [DEFINITION] OK — Lambda = (1-phi)*G consistent with consumption jump and code
- **Line 126** [VERBAL] OK — Lambda < 1 means household consumption falls (negative singularity)
- **Line 132** [DEFINITION] OK — AI stock dividend D_t^A = alpha_t * Y_t^pub
- **Line 133** [DEFINITION] OK — non-AI stock dividend D_t^N = (1-alpha_t) * Y_t^pub
- **Line 135** [DEFINITION] OK — Y_t^pub definitions pre- and post-singularity are consistent; dividends sum to Y_t^pub
- **Line 137** [REFERENCE] OK — GKP2012 reference for impossibility of trading unborn capital confirmed
- **Line 141** [DEFINITION] OK — equilibrium definition
- **Line 144** [ARITHMETIC] OK — Euler equation is standard CRRA asset pricing equation
- **Line 146** [ASSUMPTION] OK — market clearing: household holds all publicly traded shares
- **Line 149** [VERBAL] OK — household's SDF prices all assets; post-singularity is Gordon growth; pre-singularity has singularity uncertainty

## Results (lines 154–235)
- **Line 154** — section header
- **Line 158** [VERBAL] OK — "stationary structure yields closed-form P/D ratios" is correct
- **Lines 160–164** [ARITHMETIC] OK — P/D = (1-H^i)*V_0 + H^i*V_inf formula verified; all 30 table entries recompute correctly
- **Lines 166–167** [ARITHMETIC] OK — V_0, V_inf, R definitions verified; R = beta*(1+g)^(1-gamma) ≈ 0.9227, V_inf ≈ 11.94
- **Lines 170–171** [ARITHMETIC] OK — H^A = (alpha_S/alpha)*Lambda^(1-gamma), H^N = ((1-alpha_S)/(1-alpha))*Lambda^(1-gamma) verified
- **Line 173** [VERBAL] OK — R < 1 required for finite P/D ratios
- **Line 180** [VERBAL] OK — interpretation of V_0 (no-singularity P/D), V_inf (post-singularity P/D), and H^i (hedge factor as product of dividend jump and marginal utility) all correct
- **Lines 182–185** [ARITHMETIC] OK — spread formula verified: (alpha_S - alpha)/(alpha*(1-alpha)) * Lambda^(1-gamma) * pR/((1-R)(1-(1-p)R))
- **Line 187** [VERBAL] OK — spread increasing in p and decreasing in Lambda (for gamma > 1) verified
- **Lines 191–192** [ARITHMETIC] OK — inline proof: V_inf - V_0 = pR/((1-R)(1-(1-p)R)) verified algebraically
- **Line 194** [VERBAL] OK — correct summary of premium drivers
- **Line 198** [ARITHMETIC] OK — complete markets uses Lambda^CM = G (household consumes total output)
- **Lines 200–203** [ARITHMETIC] OK — amplification ratio (1-phi)^(1-gamma) verified: ratio of Lambda^(1-gamma) under IM vs CM
- **Line 211** [VERBAL] OK — amplification large when phi close to 1 and gamma high
- **Line 215** [ASSUMPTION] OK — parameters beta=0.96, g=0.02, gamma=3, alpha=0.15, alpha_S=0.50 match table and code
- **Lines 218–227** [TABLE] OK — all table entries verified against code output; Lambda values check out (Panel A: (1-0.5)*5=2.5; Panel B: (1-0.6)*2=0.8)
- **Line 229** [VERBAL] OK — "both P/D ratios decline with p" in Panel A confirmed
- **Line 229** [ARITHMETIC] OK — "spread that reaches 3.1 at p = 0.10" matches table
- **Line 231** [VERBAL] CAUTION — "reduces the household's consumption to 80% of its pre-singularity level": Lambda=0.8 means consumption is 80% of the *counterfactual* (what it would have been without singularity), but 81.6% of the actual pre-singularity consumption C_tau (since C_{tau+1} = 0.8*1.02*C_tau = 0.816*C_tau). The phrase "pre-singularity level" is ambiguous; the counterfactual reading supports 80%.
- **Line 231** [ARITHMETIC] OK — "rising from 11.9 to 41.6": Panel B AI stocks go from 11.9 (p=0) to 41.6 (p=0.10)
- **Line 231** [ARITHMETIC] OK — "spread exceeds 30 at p = 0.10": Panel B spread = 30.2

## Extensions (lines 236–309)
- **Line 236** — section header
- **Line 238** [VERBAL] OK — baseline leaves household with no recourse; extensions are independent of one another (confirmed: three separate subsections, no cross-references)
- **Line 242** [REFERENCE] OK — GKP2012 reference for capital that may not yet exist confirmed
- **Line 244** [ASSUMPTION] OK — tax rate theta in [0,1], deadweight cost delta in [0,1]
- **Line 247** [ARITHMETIC] OK — Lambda(theta, delta) = [(1-phi) + (1-delta)*theta*phi]*G verified
- **Line 250** [ARITHMETIC] OK — theta=0 gives (1-phi)*G (baseline); theta=1, delta=0 gives G (complete markets); theta=1, delta>0 gives (1-delta*phi)*G. All three verified by substitution.
- **Line 252** [VERBAL] OK — Jones (2024) reference for explosive output growth; "even transfers that waste 90%" supported by Figure 3
- **Lines 255–262** [FIGURE/TABLE] OK — Figure 3 caption, notes, and parameters all match the code; four curves (no transfer, delta=0.9, delta=0.5, delta=0) verified against code logic; V_0 and V_inf reference lines confirmed
- **Line 264** [VERBAL] OK — "For low G, no-transfer P/D is very high" verified (e.g. G=1.5: Lambda=0.75, H^A≈5.93, P/D≈35.5)
- **Line 264** [VERBAL] OK — "all curves converge to V_0" as G→∞: Lambda→∞, Lambda^(1-gamma)→0, H→0, P/D→V_0
- **Line 264** [VERBAL] OK — "delta=0.9 P/D drops substantially" visible in figure
- **Line 264** [VERBAL] OK — "For very large G, all transfer policies converge" correct (all H→0)
- **Line 268** [ASSUMPTION] OK — veto mechanism: household blocks singularity at cost kappa*C_t
- **Line 270** [VERBAL] OK — under complete markets, Lambda=G>1 so household never vetoes
- **Line 272** [VERBAL] OK — under incomplete markets with Lambda<1, veto is rational for small kappa
- **Lines 274–276** [VERBAL] OK — Proposition 5 parts (a) and (b) correctly stated
- **Line 282** [VERBAL] OK — transfers raising Lambda above 1 removes veto incentive; verified: with theta=1, delta=0.9, phi=0.5, need G > 1/0.55 ≈ 1.82
- **Line 286** [ASSUMPTION] OK — extinction probability q in [0,1), all assets worthless in extinction
- **Line 288** [VERBAL] OK — hedge factor scaled by (1-q): effective weight on V_inf becomes (1-q)*H^i
- **Line 291** [ARITHMETIC] OK — P/D with extinction = [1-(1-q)*H^i]*V_0 + (1-q)*H^i*V_inf verified
- **Lines 294–298** [ARITHMETIC] OK — spread = (1-q)*(H^A - H^N)*(V_inf - V_0), strictly decreasing in q, verified algebraically
- **Line 305** [VERBAL] OK — extinction destroys all assets equally, diluting differential hedge; tension with displacement noted as qualitative observation

## Conclusion (lines 310–326)
- **Line 310** — section header
- **Line 312** [VERBAL] OK — main argument restated accurately; "in part" qualifier preserved from spec I.3.a
- **Line 312** [REFERENCE] OK — "direct application of the displacement risk logic in GKP2012" is accurate; GKP introduce displacement risk from innovation under incomplete intergenerational risk sharing
- **Line 312** [VERBAL] OK — three extensions (transfers, deployment efficiency, extinction risk) match spec I.5
- **Line 314** [VERBAL] OK — "intentionally compact" matches spec IV.8; "illustrative parameterizations rather than formal calibration" matches spec IV.8.d
- **Line 316** [VERBAL] OK — AI-agent production claim matches spec IV.5.d
- **Line 316** [VERBAL] OK — forward-looking statement about displacement risk is consistent with model logic

## Proofs (lines 327–364)
- **Line 327** — appendix header
- **Line 329** — proof of Proposition 2 header
- **Line 333** [ARITHMETIC] OK — Gordon growth P/D: pi_S = sum_{s=1}^inf R^s = R/(1-R) = V_inf. Geometric series verified.
- **Line 338** [ARITHMETIC] OK — pre-singularity Euler equation: pi_N^i = (1-p)*R*(pi_N^i + 1) + p*R*H^i*(pi_S + 1). No-singularity term verified (SDF*dividend ratio = R). Singularity term verified: beta*[Lambda*(1+g)]^{-gamma} * (alpha_S/alpha)*Lambda*(1+g) = R*H^A.
- **Line 340** [ARITHMETIC] OK — (pi_S + 1) = R/(1-R) + 1 = 1/(1-R) verified
- **Line 344** [ARITHMETIC] OK — rearrangement: pi_N^i[1-(1-p)R] = (1-p)R + pRH^i/(1-R) verified
- **Line 345** [ARITHMETIC] OK — division yields V_0 + H^i * pR/((1-R)(1-(1-p)R)) verified
- **Line 346** [ARITHMETIC] OK — decomposition pi_N^i = (1-H^i)*V_0 + H^i*V_inf verified using V_inf - V_0 = pR/((1-R)(1-(1-p)R))
- **Line 348** [ARITHMETIC] OK — V_inf - V_0 = pR/((1-R)(1-(1-p)R)) verified algebraically
- **Line 350** — proof of Proposition 5 header
- **Line 352** [ARITHMETIC] OK — Part (a): Lambda^CM = G > 1, consumption G*(1+g)*C_t > (1+g)*C_t, so household never vetoes
- **Lines 354–358** [ARITHMETIC] OK — Part (b): flow utility without veto = (1-p)*u((1+g)C_t) + p*u(Lambda*(1+g)*C_t) < u((1+g)*C_t) by strict concavity when Lambda < 1
- **Lines 359–360** [ARITHMETIC] OK — threshold kappa_bar defined by indifference condition; kappa_bar > 0 follows from RHS < u((1+g)*C_t)
- **Line 362** [ARITHMETIC] OK — household vetoes for all kappa < kappa_bar by monotonicity of u
