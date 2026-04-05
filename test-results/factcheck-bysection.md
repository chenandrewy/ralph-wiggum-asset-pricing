# tests/factcheck-bysection.py
Started: 2026-04-04 23:25:45 EDT
Runtime: 10m 56s
[ralph-garage/agent-logs/20260404T232545.923845-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260404T232545.923845-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic recomputed and correct; all verbal claims supported; no materially wrong claims; minor source-comment numbering issues do not affect rendered paper.

## Introduction (lines 41–62)

- **Line 41** — section header
- **Line 43** [VERBAL] OK — main argument (AI stocks hedge displacement risk) supported by Corollary 1 and Table 1
- **Line 45** [VERBAL] OK — "vastly increase total economic output" consistent with G > 1 (line 96)
- **Line 45** [VERBAL] OK — "much of this new output would accrue to the owners of private AI capital" consistent with phi capture (line 97)
- **Line 45** [VERBAL] OK — "her share of total output shrinks" consistent with Lambda = (1-phi)G framework
- **Line 45** [VERBAL] OK — "dividends grow relative to other stocks" consistent with alpha_S > alpha (line 98)
- **Line 47** [VERBAL] OK — "infinite-horizon, discrete-time model" confirmed at line 67
- **Line 47** [VERBAL] OK — "two assets trade publicly" confirmed at lines 118-123
- **Line 47** [REFERENCE] OK — GKP2012 analogy to "future innovators who cannot trade" accurately represents GKP p. 492
- **Line 47** [VERBAL] OK — "closed-form expressions" confirmed by Proposition 1 (line 148)
- **Line 47** [VERBAL] OK — "spread increases with singularity probability and severity" confirmed by Corollary 1 (line 175)
- **Line 47** [VERBAL] OK — "premium is strictly larger under incomplete markets" confirmed by Proposition 2 (line 188-192)
- **Line 49** [ARITHMETIC] OK — "5% singularity probability produces a P/D spread of 2.1" matches Table Panel A (p=0.05, Spread=2.1)
- **Line 49** [ARITHMETIC] OK — "spreads exceeding 20" matches Table Panel B (p=0.05 Spread=20.7, p=0.10 Spread=30.2)
- **Line 49** [ARITHMETIC] OK — "P/D ratios several times higher" confirmed: Panel B p=0.10 gives 41.6/11.4 = 3.6x
- **Line 49** [VERBAL] OK — "singularity reduces the household's consumption despite massive output growth" confirmed by Lambda=0.8 < 1 with G=2 > 1
- **Line 51** [VERBAL] OK — "each branching directly from the baseline model" confirmed at line 226
- **Line 51** [REFERENCE] OK — Jones (2024) "potentially infinite" output growth accurately represents Jones's singularity model
- **Line 51** [VERBAL] OK — "transfers that waste 90%" supported by figure and formula (delta=0.9 still reduces P/D)
- **Line 51** [VERBAL] OK — "household may find it rational to block" confirmed by Proposition 3 (line 262)
- **Line 51** [VERBAL] OK — "under complete markets, the household never blocks" confirmed by Proposition 3 part (a)
- **Line 51** [REFERENCE] OK — Jones (2024) extinction risk accurately characterized
- **Line 51** [VERBAL] OK — "reduces the hedging premium" confirmed by Proposition 4 (line 282)
- **Line 53** [ASSUMPTION] OK (MINOR NOTE) — "600-word economic specification" is a round-number approximation; actual Section I of spec is ~673 words. Consistent with project documentation.
- **Line 56** [REFERENCE] OK — GKP2012 "innovation creates a systematic risk factor through incomplete intergenerational risk sharing" accurately represents GKP abstract
- **Line 56** [REFERENCE] OK — "displacement risk is priced, market incompleteness amplifies, certain assets hedge" all present in GKP
- **Line 56** [REFERENCE] OK — "GKP2012 note that government transfers would affect the magnitude of displacement but do not pursue this formally" accurately represents GKP remark (their p. 492/line 368 in lit file)
- **Line 58** [REFERENCE] OK — Jones (2024) "tradeoff between AI-driven growth and existential risk" matches his title and framework
- **Line 58** [REFERENCE] OK — Barro (2006) rare disasters and equity premium is well-established
- **Line 58** [REFERENCE] OK — Hobijn and Jovanovic (2001) displacement of incumbents during IT revolution confirmed via GKP citation
- **Line 58** [REFERENCE] OK — remaining lit review citations (Korinek-Suh, Pastor-Veronesi, Nordhaus, Aghion-Jones-Jones, Acemoglu-Restrepo, Blanchard, Garleanu-Panageas) are well-known papers with accurate one-line characterizations

## Model (lines 63–141)

- **Line 63** — section header
- **Line 67** [DEFINITION] OK — discrete time, representative household and AI capital owners
- **Lines 70–76** [DEFINITION] OK — standard CRRA utility with beta in (0,1), gamma > 1
- **Lines 79–85** [DEFINITION] OK — deterministic output growth Y_t = Y_0(1+g)^t, AI share alpha
- **Line 88** [REFERENCE] OK — GKP2012 "unborn innovators" analogy accurate (GKP p. 492)
- **Line 88** [VERBAL] OK — "AI owners are not marginal investors" consistent with equilibrium definition (lines 129-134)
- **Line 92** [DEFINITION] OK — geometric (memoryless) singularity arrival with probability p, one-time permanent event
- **Lines 96–99** [ASSUMPTION] OK — G > 1 output jump, phi in (0,1) capture, alpha_S > alpha, post-singularity growth g
- **Line 105** [ARITHMETIC] OK — C_{tau+1} = (1-phi)G(1+g)C_tau verified from model assumptions: post-singularity public output at tau+1 is (1-phi)G Y_tau(1+g), household consumes all public output
- **Lines 110–112** [DEFINITION] OK — Lambda = (1-phi)G consistent with line 105
- **Line 114** [VERBAL] OK — Lambda < 1 means consumption falls despite G > 1; correctly identified as displacement scenario
- **Lines 120–123** [DEFINITION] OK — dividend definitions consistent; post-singularity public output formula verified
- **Line 125** [REFERENCE] OK — GKP2012 incomplete markets friction accurately characterized
- **Line 129** [DEFINITION] ERROR (SOURCE COMMENT ONLY) — comment says "% Proposition 1" but this is a Definition environment sharing the proposition counter, so it renders as "Definition 1". This causes all downstream comment numbers to be off by one. The rendered PDF uses \ref{} labels and is unaffected.
- **Lines 131–133** [DEFINITION] OK — standard consumption-based Euler equation with CRRA SDF
- **Line 134** [DEFINITION] OK — market clearing condition consistent with household being sole public investor
- **Line 137** [VERBAL] OK — post-singularity Gordon growth and pre-singularity singularity uncertainty both correct

## Results (lines 142–223)

- **Line 142** — section header
- **Line 146** [VERBAL] OK — model is stationary, closed-form P/D ratios confirmed by Proposition 1
- **Lines 148–161 (Proposition 1)** [DEFINITION] OK — formulas internally consistent. R = 0.96 x 1.02^(-2) = 0.92274 < 1 confirmed.
- **Line 148** [DEFINITION] ERROR (SOURCE COMMENT ONLY) — comment says "% Proposition 1" but shared counter makes this Proposition 2 in rendered output. No effect on PDF cross-references.
- **Line 168** [VERBAL] OK (MINOR NOTE) — calls the P/D formula "a weighted average of V_0 and V_\infty." When H^i < 1 (Panel A), this is a convex combination. When H^i > 1 (Panel B, H^A = 5.21), this is an affine combination/extrapolation. "Weighted average" is imprecise but the economic interpretation (product of dividend-jump and marginal-utility forces) is correct.
- **Line 170** [DEFINITION] ERROR (SOURCE COMMENT ONLY) — comment says "% Corollary 1" but renders as Corollary 3 due to shared counter.
- **Lines 172–174 (Corollary equation)** [ARITHMETIC] OK — H^A - H^N = (alpha_S - alpha)/(alpha(1-alpha)) x Lambda^(1-gamma) verified. V_inf - V_0 = pR/((1-R)(1-(1-p)R)) verified. Product gives stated spread formula.
- **Line 175** [VERBAL] OK — spread increasing in p confirmed by table monotonicity and analytically. Decreasing in Lambda for gamma > 1 confirmed: d/dLambda of Lambda^(1-gamma) = (1-gamma)Lambda^(-gamma) < 0.
- **Lines 178–179 (Proof)** [ARITHMETIC] OK — all algebraic identities verified
- **Line 182** [VERBAL] OK — accurate summary of corollary
- **Line 186** [VERBAL] OK — under complete markets Lambda^CM = G (household gets all output, no phi displacement)
- **Line 188** [DEFINITION] ERROR (SOURCE COMMENT ONLY) — comment says "% Proposition 2" but renders as Proposition 4 due to shared counter.
- **Lines 189–192 (Proposition 2)** [ARITHMETIC] OK — ratio of spreads = ((1-phi)G)^(1-gamma) / G^(1-gamma) = (1-phi)^(1-gamma) > 1 for gamma > 1 and phi > 0. Verified.
- **Lines 195–196 (Proof)** [ARITHMETIC] OK — algebraic steps correct
- **Line 199** [VERBAL] OK — accurate interpretation of amplification factor
- **Line 203** [ASSUMPTION] OK — baseline parameters beta=0.96, g=0.02, gamma=3, alpha=0.15, alpha_S=0.50 match table header
- **Lines 206–215 (Table)** [FIGURE/TABLE] OK — all 30 cells recomputed from formulas and match to 1 decimal place:
  - Panel A (G=5, phi=0.5, Lambda=2.5): V_inf=11.94, H^A=0.533, H^N=0.094. All P/D values and spreads confirmed.
  - Panel B (G=2, phi=0.6, Lambda=0.8): V_inf=11.94, H^A=5.208, H^N=0.980. All P/D values and spreads confirmed.
- **Line 217** [VERBAL] OK — "both P/D ratios decline with p" in Panel A confirmed (AI: 11.9, 11.3, 10.8, 9.7, 8.7; Non-AI: 11.9, 10.7, 9.7, 7.6, 5.6)
- **Line 217** [ARITHMETIC] OK — "spread that reaches 3.1 at p=0.10" matches table (computed 3.09, rounds to 3.1)
- **Line 219** [VERBAL] OK (MINOR NOTE) — "reduces the household's consumption to 80% of its pre-singularity level" refers to Lambda=0.8 as the displacement factor; the total ratio C_{tau+1}/C_tau = 0.8 x 1.02 = 0.816, so 80% describes the displacement component abstracting from deterministic growth. Standard convention but could be more precise.
- **Line 219** [ARITHMETIC] OK — "rising from 11.9 to 41.6" matches table (p=0 to p=0.10)
- **Line 219** [ARITHMETIC] OK — "spread exceeds 30 at p=0.10" confirmed (table: 30.2)

## Extensions (lines 224–297)

- **Line 224** — section header
- **Line 226** [VERBAL] OK — extensions are independent modifications of the baseline
- **Line 230** [REFERENCE] OK — GKP2012 "relevant capital may not yet exist" accurately represents GKP p. 492
- **Line 232** [DEFINITION] OK — transfer mechanism with tax rate tau and deadweight cost delta clearly stated
- **Line 235** [ARITHMETIC] OK — Lambda(tau,delta) = [(1-phi) + (1-delta)tau phi]G verified: household gets (1-phi) naturally plus net transfer (1-delta)tau phi, times G
- **Line 238** [ARITHMETIC] OK — all three special cases verified:
  - tau=0: Lambda = (1-phi)G (baseline)
  - tau=1, delta=0: Lambda = G (complete markets)
  - tau=1, delta>0: Lambda = (1-delta phi)G
- **Line 240** [REFERENCE] OK — Jones (2024) "potentially infinite" output growth matches his singularity model (Model 2: infinite consumption)
- **Line 240** [VERBAL] OK — "transfers that waste 90% can dramatically reduce displacement risk" verified: delta=0.9, phi=0.5 gives Lambda=0.55G, which exceeds 1 for G > 1.82
- **Lines 242–250 (Figure)** [FIGURE/TABLE] OK — figure parameters (beta=0.96, g=0.02, gamma=3, alpha=0.15, alpha_S=0.50, phi=0.50, p=0.05, tau=1) match caption. V_0(p=0.05) ~= 7.10 and V_inf ~= 11.94 appear as horizontal dotted lines. Four curves (No transfers, delta=0.9, delta=0.5, delta=0) show correct ordering and convergence behavior.
- **Line 252** [VERBAL] OK — "all curves converge to V_0" as G increases: when G is large, Lambda^(1-gamma) -> 0 for gamma > 1, so H -> 0 and P/D -> V_0. Confirmed analytically and visually in figure.
- **Line 252** [VERBAL] OK — "even with delta=0.9 the P/D drops substantially" confirmed by vertical gap between No-transfer and delta=0.9 curves
- **Line 252** [VERBAL] OK — "for very large G, all transfer policies converge" confirmed: all Lambda -> infinity, all H -> 0
- **Line 256** [DEFINITION] OK — veto mechanism clearly stated (cost kappa C_t per period)
- **Line 258** [VERBAL] OK — under complete markets Lambda^CM = G > 1, household consumption rises, never vetoes
- **Line 260** [VERBAL] OK — under Lambda < 1, consumption falls, veto preferred for small kappa
- **Line 262** [DEFINITION] ERROR (SOURCE COMMENT ONLY) — comment says "% Proposition 3" but shared counter makes this Proposition 5 in rendered output. Cross-references via \ref{prop:veto} are unaffected.
- **Line 263** [VERBAL] OK — both parts of proposition verified against proof in appendix (lines 338-350)
- **Line 270** [VERBAL] OK — connection to Extension 1 is logically sound: transfers raising Lambda > 1 removes veto incentive
- **Line 274** [REFERENCE] OK — Jones (2024) existential risk from AI matches his paper's title and framework
- **Line 274** [ASSUMPTION] OK — extinction setup (probability q, zero utility) clearly stated
- **Line 276** [VERBAL] OK — "hedge factor scaled by (1-q)" is correct characterization
- **Line 279** [ARITHMETIC] OK — extinction formula verified: singularity term weighted by (1-q), replacing H^i with (1-q)H^i in the P/D expression
- **Line 282** [DEFINITION] ERROR (SOURCE COMMENT ONLY) — comment says "% Proposition 4" but renders as Proposition 6 due to shared counter.
- **Line 285** [ARITHMETIC] OK — spread = (1-q)(H^A - H^N)(V_inf - V_0), strictly decreasing in q since (1-q) is decreasing and the remaining factors are positive
- **Line 290** [VERBAL] OK — proof is immediate from the formula and H^A > H^N
- **Line 293** [VERBAL] OK — "extinction destroys all assets equally" provides correct intuition; tension between displacement and extinction risk is a valid qualitative observation

## Conclusion (lines 298–314)

- **Line 298** — section header
- **Line 300** [VERBAL] OK — "AI stocks hedge against a negative AI singularity under incomplete markets" accurately summarizes the paper's main result (Corollary 1, Proposition 2)
- **Line 300** [REFERENCE] OK — "direct application of the displacement risk logic in GKP2012" accurately represents the paper's relationship to GKP
- **Line 300** [VERBAL] OK — "extend this logic to study government transfers, deployment efficiency, and extinction risk" matches the three extensions in Section 4
- **Line 302** [VERBAL] OK — "single binary event" matches the model (singularity occurs or not)
- **Line 302** [VERBAL] OK — "illustrative parameterizations rather than formal calibration" accurately describes the quantitative exercise
- **Line 304** [VERBAL] OK — "every equation, every line of code, and every paragraph was produced by AI agents" consistent with spec (IV.5.d)
- **Line 304** [VERBAL] OK — "working from a human specification" consistent with spec description

## Proofs (lines 315–352)

- **Line 315** — appendix header
- **Line 317** [REFERENCE] OK — "Proof of Proposition \ref{prop:pd}" resolves correctly via LaTeX labels
- **Line 319** [VERBAL] OK — post-singularity Gordon growth with rate g confirmed by model (line 99)
- **Line 321** [ARITHMETIC] OK — pi_S = sum_{s=1}^inf R^s = R/(1-R) = V_inf. Geometric series verified.
- **Line 326** [ARITHMETIC] OK — Euler equation decomposition into no-singularity and singularity branches verified:
  - No singularity: (1-p)R(pi+1)
  - Singularity: pRH^i(pi_S+1)
- **Line 328** [ARITHMETIC] OK — SDF x dividend growth = beta[Lambda(1+g)]^(-gamma) x (alpha_S/alpha)Lambda(1+g) = R x H^A. Verified.
- **Line 328** [ARITHMETIC] OK — (pi_S + 1) = R/(1-R) + 1 = 1/(1-R). Verified.
- **Line 332** [ARITHMETIC] OK — pi[1-(1-p)R] = (1-p)R + pRH^i/(1-R). Algebra verified.
- **Line 333** [ARITHMETIC] OK — division by [1-(1-p)R] gives V_0 + pRH^i/[(1-R)(1-(1-p)R)]. Verified.
- **Line 334** [ARITHMETIC] OK — V_inf - V_0 = pR/[(1-R)(1-(1-p)R)] verified algebraically. Final form (1-H^i)V_0 + H^i V_inf confirmed.
- **Line 338** [REFERENCE] OK — "Proof of Proposition \ref{prop:veto}" resolves correctly
- **Line 340** [ARITHMETIC] OK — under CM, Lambda^CM = G > 1, so G(1+g)C_t > (1+g)C_t. Household never vetoes.
- **Line 340** [VERBAL] OK — expected utility without veto exceeds utility with veto: (1-p)u((1+g)C_t) + pu(G(1+g)C_t) > u((1+g)C_t) > u((1-kappa)(1+g)C_t) for kappa > 0.
- **Lines 342–344** [ARITHMETIC] OK — flow utility without veto correctly stated
- **Line 346** [VERBAL] OK — concavity argument for small kappa is sound; by continuity, threshold exists
- **Lines 347–349** [DEFINITION] OK — kappa-bar defined as indifference point
- **Line 350** [ARITHMETIC] OK — by strict concavity and Lambda < 1, RHS < u((1+g)C_t), so kappa-bar > 0. Household vetoes for all kappa < kappa-bar. Verified.
