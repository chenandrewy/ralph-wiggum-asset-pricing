# tests/factcheck-bysection.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 6m 17s
[ralph-garage/agent-logs/20260411T211526.531903-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.531903-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong.

## Introduction (lines 38–74)
- **Line 38** — section header, no claim
- **Line 40** [VERBAL] OK — "S&P 500 P/D has reached historically elevated levels" and "NASDAQ has sharply outpaced the broader market since 2015" supported by Figure 1 panels (a) and (b)
- **Lines 42–47** [FIGURE/TABLE] OK — figure caption accurately describes Panel (a) as S&P 500 trailing P/D (Shiller dataset) and Panel (b) as NASDAQ/S&P 500 price ratio normalized to Jan 2015 = 100; sources (FRED, Shiller) match the R code downloads
- **Line 49** [VERBAL] OK — hedging motive, restricted equity held by founders/early-stage investors, market incompleteness all supported by Model section (lines 114, 116, 157)
- **Line 51** [VERBAL] OK — "closed-form price-dividend ratios" confirmed by Proposition 1; "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks" supported by table (ratio = 2.0 at p=1%, xi=0%); "results on how displacement risk distorts AI development decisions and how fiscal policy can substitute for missing markets" confirmed by Extensions section
- **Line 51** [ARITHMETIC] OK — claim that P/D ratio can reach "roughly twice" is confirmed at p=1%, xi=0 (ratio=2.0); note the quant section (line 193) gives the more precise "1.3 to 2 times" range
- **Line 53** [VERBAL] OK — "under complete markets the displacement-driven premium would largely vanish" supported by line 173; caveat "largely" is appropriate (residual spread from differential dividend growth remains)
- **Line 53** [REFERENCE] OK — "Proposition 2 quantifies this attenuation, showing that the valuation spread narrows as extinction probability rises" confirmed by Proposition 2 (line 161–163)
- **Line 55** [VERBAL] OK — "when the positive singularity is more likely than the negative one, development is socially efficient" supported by Extension 1 (lines 204, 206); "risk-averse household may rationally choose to block it" confirmed by Proposition 3 (lines 212–217)
- **Line 55** [REFERENCE] OK — Proposition 3 reference resolves correctly; "complete markets would eliminate this distortion entirely" confirmed by Prop 3(ii) (line 215)
- **Line 57** [VERBAL] OK — "broader trading of AI equity is blocked by restricted ownership and non-existent future capital" supported by lines 114, 241; "deadweight costs that scale with the size of transfers" supported by Section 4.2 (line 243, cost fraction delta*tau)
- **Line 59** [VERBAL] OK — "explosive output growth makes even grossly inefficient transfers effective" supported by Section 4.2 (line 265); Jones (2024) reference for unbounded output growth is appropriate
- **Line 61** [REFERENCE] OK — all four section cross-references resolve correctly: sec:model (line 75), sec:quant (line 180), sec:extensions (line 198), sec:conclusion (line 283)
- **Lines 63–65** — formatting (lit review header), no claim
- **Line 66** [REFERENCE] OK — GKP2012 characterization (innovation displaces existing agents, systematic risk factor, incomplete markets, overlapping generations) is consistent with how GKP is described throughout the paper
- **Line 68** [REFERENCE] OK — Jones (2024) characterization (AI-driven growth vs. existential risk) is consistent; "attenuates rather than amplifies" confirmed by Proposition 2
- **Line 70** [REFERENCE] OK — citation groupings (creative destruction, AI macroeconomics, rare disasters, technological revolutions) are standard and internally consistent
- **Lines 72–74** — formatting, no claim

## Model (lines 75–179)
- **Line 75** — section header
- **Lines 77–79** [DEFINITION] OK — discrete infinite-horizon model, representative household as marginal investor, AI owners hold private capital; GKP2012 analogy correctly characterized; explicit disclaimer about not modeling entry dynamics
- **Lines 81–86** [DEFINITION] OK — aggregate consumption growth equation C_{t+1} = (1+g)C_t, standard formulation
- **Line 88** [DEFINITION] OK — household consumption c_t^H = alpha_t C_t, AI owners get (1-alpha_t)C_t; shares sum to 1
- **Lines 90–100** [DEFINITION] OK — singularity structure: probability p, non-extinction (prob 1-xi) with consumption jump 1+eta and displacement phi, extinction (prob xi) with C=0; Jones (2024) reference for extinction channel
- **Line 98** [VERBAL] OK — "smaller phi means larger displacement" is correct since phi < 1 and lower phi means household retains less
- **Line 102** [VERBAL] OK — repeated singularities progressively displace; consistent with alpha_{t+1} = phi*alpha_t < alpha_t
- **Lines 104–110** [DEFINITION] OK — AI stock dividends D^AI = theta_t C_t; theta updates: theta_{t+1} = theta_t + Delta_theta(1-theta_t); non-AI dividends D^N = (1-theta_t)C_t; total dividends = C_t (verified: theta*C + (1-theta)*C = C)
- **Line 112** [VERBAL] OK — total public dividends equal aggregate consumption; alpha_t and theta_t are distinct (consumption split vs. dividend split); internally consistent
- **Lines 113–114** [DEFINITION] OK — restricted equity is the source of market incompleteness; household cannot purchase restricted shares
- **Lines 115–116** [VERBAL] OK — phi governs total consumption share; AI stocks allow marginal utility smoothing but do not eliminate displacement; if restricted equity were tradeable, phi_eff -> 1 and valuation spread collapses
- **Lines 118–123** [DEFINITION] OK — CRRA preferences with gamma > 1 and beta in (0,1); standard infinite-horizon expected utility
- **Lines 125–127** [VERBAL] OK — household prices assets via Euler equation; SDF reflects household (not aggregate) consumption growth under incomplete markets
- **Lines 129–141** [ARITHMETIC] OK — P/D formulas verified algebraically; Gamma^AI = [0.15+0.2*0.85]/0.15 * 1.5 = 3.2; Gamma^N = [0.85-0.17]/0.85 * 1.5 = 1.2; formulas match Euler equation derivation in appendix
- **Lines 143–145** [REFERENCE] OK — proof deferred to Appendix A (app:proof-pd at line 294); appendix contains the derivation
- **Lines 147–153** [ARITHMETIC] OK — existence condition A^j < 1 is correct (A^j >= 1 makes denominator <= 0); baseline calibration satisfies A^j < 1 for both assets (all table entries have finite P/D > 9, implying A^j > 0.9 but < 1)
- **Line 152** [REFERENCE] OK — reference to Section 4.2 (sec:ext2, line 237) for government transfers motivation is correct
- **Line 155** [VERBAL] OK — closed-form approximation treats post-singularity P/D as equal to pre-singularity; exact when Delta_theta -> 0; table reports numerically exact values via backward recursion; the non-AI closed form is actually exact (since Gamma^N is theta-independent) though the text does not highlight this distinction
- **Line 157** [ARITHMETIC] OK — Gamma^AI > 1+eta (3.2 > 1.5) confirmed; Gamma^N < 1+eta (1.2 < 1.5) confirmed; phi(1+eta) = 0.75 < 1 confirmed
- **Line 157** [VERBAL] OK — "AI stocks' payoffs are especially valuable, pushing their P/D ratio above non-AI" confirmed by table (AI P/D > non-AI P/D in every row); hedging channel description is accurate
- **Line 159** [VERBAL] OK — "valuation spread widens with displacement severity (decreasing phi)" correct: lower phi raises phi^{-gamma}, amplifying singularity component more for AI stocks; "widens with singularity probability p for sufficiently risk-averse households" correct directionally
- **Lines 161–163** [VERBAL] OK — Proposition 2: "valuation spread is decreasing in extinction probability xi" confirmed by table (for every fixed p, ratio decreases as xi increases)
- **Lines 165–167** [ARITHMETIC] OK — proof decomposition A^j = B[(1-p) + p(1-xi)S*Gamma^j] is correct; derivative dA^j/dxi = -BpS*Gamma^j, larger in magnitude for AI since Gamma^AI > Gamma^N; f''(A) = 2/(1-A)^3 > 0 verified; convexity requires A^j > 1/2 (equiv. P/D > 1), satisfied across all table entries (all P/D > 9)
- **Lines 169–175** [VERBAL] OK — GKP comparison accurate (continuous displacement via new firm entry vs. discrete singularity); complete markets discussion correct (phi_eff -> 1 collapses premium, residual spread from Gamma^AI != Gamma^N); existence condition violation under severe displacement logically consistent (phi -> 0 makes phi^{-gamma} -> infinity)

## Quantitative Analysis (lines 180–197)
- **Lines 180–187** — section header and table float; table correctly inputs exhibits/table-pd-ratios.tex
- **Line 189** [ASSUMPTION] OK — all seven parameters (beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, Delta_theta=0.2) match the table footnote and the R code exactly
- **Line 189** [ARITHMETIC] OK — phi(1+eta) = 0.5*1.5 = 0.75; "household consumption falls by 25%" is correct (consumption is 75% of pre-singularity level)
- **Line 189** [VERBAL] OK — "AI stocks are initially 15% of the economy" (theta=0.15) and "AI's share jumps by 20% of the non-AI remainder" (Delta_theta=0.2) are direct readings of parameters
- **Line 191** [ARITHMETIC] OK — at p=0.5%, xi=0: AI P/D = 15.5, non-AI P/D = 11.1, ratio = 1.4; all match table exactly; "about 15.5", "near 11", "about 1.4" are accurate
- **Line 191** [ARITHMETIC] OK — at p=1%, xi=0: ratio = 2.0; "the ratio rises to 2" is exact
- **Line 191** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium" confirmed by table (ratio increases monotonically with p for fixed xi)
- **Line 191** [VERBAL] OK — "extinction risk compresses the AI premium, as Proposition 2 predicts" confirmed by table (for every fixed p, ratio decreases as xi increases)
- **Line 193** [ARITHMETIC] OK — "1.3 to 2 times" across 0.5–1% range confirmed; minimum ratio is 1.3 (at p=0.5%, xi=10% and xi=20%), maximum is 2.0 (at p=1%, xi=0%)
- **Line 193** [VERBAL] OK — description of comparison limitations (NASDAQ broader than AI stocks, return differences partly reflect earnings growth, S&P has AI exposure) are appropriate caveats
- **Line 193** [FIGURE/TABLE] OK — reference to Figure 1 for S&P 500 P/D levels is correct; the "roughly 50% more" NASDAQ appreciation claim depends on live-downloaded data and cannot be independently verified from static files, but is consistent with the figure's construction (NASDAQ/S&P normalized to Jan 2015 = 100)

## Extensions: Market Incompleteness and the Singularity (lines 198–282)
- **Line 198** — section header
- **Line 200** [VERBAL] OK — accurately describes section scope (distortions to development, government policy)
- **Line 204** [DEFINITION] OK — positive singularity (share increases to min(1, alpha/phi), agg consumption jumps 1+eta), negative singularity (share falls to phi*alpha), assumption q > 1/2
- **Line 206** [VERBAL] OK — Kaldor-Hicks efficiency when (1+eta) > 1; since eta > 0 by construction, aggregate consumption rises in both non-extinction singularity states, so winners could compensate losers
- **Line 208** [DEFINITION] OK — veto cost kappa > 0 as permanent consumption fraction; extinction utility normalized to zero; conservatism remark correct (CRRA utility negative for c > 0 when gamma > 1)
- **Line 210** [VERBAL] OK — under complete markets, household consumption in singularity = alpha(1+eta)C_t(1+g); consistent with proof at line 228
- **Lines 212–217** [VERBAL] OK — Proposition 3 correctly states: (i) threshold gamma above which veto occurs under incomplete markets; (ii) under complete markets, no veto for small enough kappa
- **Lines 219–229** [ARITHMETIC] OK — proof algebra is correct; Delta u(gamma) formula consistent; dominance argument as gamma -> infinity when phi(1+eta) < 1 is valid; complete markets proof (utility gain positive since eta > 0) is correct
- **Line 231** [ARITHMETIC] OK — all numerical example parameters (phi=0.5, eta=0.5, xi=5%, p=1%, gamma=10, alpha=0.70, q=0.70, kappa=1%) match R code exactly; code output confirms V_veto > V_develop under incomplete markets and V_develop > V_veto under complete markets
- **Line 231** [ARITHMETIC] OK — "positive singularity is more than twice as likely as the negative one": q/(1-q) = 0.70/0.30 = 2.33 > 2
- **Line 233** [VERBAL] OK — extinction risk interaction under conservative normalization (higher xi reduces weight on non-extinction states driving veto) is logically correct; acknowledgment that bounded utility would amplify veto incentive is appropriate
- **Line 235** [REFERENCE] OK — Jones (2024) characterization of wealth-dependent attitudes toward AI risk is consistent with how the paper describes his work
- **Lines 237–242** [VERBAL] OK — motivation for transfers (ideal solution blocked by GKP constraint, transfers as alternative, dual role of pricing effect and real effect) is internally consistent
- **Lines 243–249** [DEFINITION] OK — transfer model: tax rate tau on AI owners, deadweight cost delta*tau, household post-transfer consumption formula (eq 7); (1-phi*alpha) correctly represents AI owners' share of post-singularity aggregate consumption
- **Lines 251–257** [ARITHMETIC] OK — phi_eff = phi + tau(1-delta*tau)(1-phi*alpha)/alpha; derivation verified by dividing eq (7) by alpha(1+eta)(1+g)C_t: first term yields phi, second term yields the transfer component; matches R code exactly
- **Lines 259–265** [ARITHMETIC] OK — ratio c^H_post / c^H_no-transfer = 1 + tau(1-delta*tau)(1-phi*alpha)/(phi*alpha); the (1+eta)C_t(1+g) cancels from numerator and denominator, confirming independence from eta; "exceeds one whenever tau > 0" is correct
- **Line 267** [ASSUMPTION] OK — figure parameters (gamma=4, alpha=0.70, p=0.5%, xi=5%, delta=0.5; baseline: eta=0.5, phi=0.5; large: eta=9, phi=0.05) all match R code exactly
- **Line 267** [ARITHMETIC] OK — "consumption halves under the large singularity (phi(1+eta)=0.5)": 0.05*10 = 0.5, correct; "falls by 25% under the baseline (phi(1+eta)=0.75)": 0.5*1.5 = 0.75, correct
- **Line 269** [ARITHMETIC] OK — phi^{-gamma} = 0.05^{-4} = 20^4 = 160,000; correct
- **Line 269** [VERBAL] OK — "P/D ratio is undefined at tau=0" for large-singularity case is confirmed by R code (returns NA when existence condition violated); "as tau increases, finite P/D ratios emerge" confirmed by code output
- **Lines 271–276** [FIGURE/TABLE] OK — figure caption parameters (alpha=0.70, p=0.5%, xi=5%, delta=0.5) match code; panel descriptions consistent with code's panel_a (P/D vs tau) and panel_b (consumption growth vs tau)
- **Line 278** [VERBAL] OK — policy conclusion (transfers blunt in normal times, effective under explosive growth) follows from the analysis; Jones (2024) and Nordhaus (2021) citations are appropriate

## Conclusion (lines 283–293)
- **Line 283** — section header
- **Line 285** [VERBAL] OK — "AI stocks trade at high valuations" supported by Figure 1 and table
- **Line 285** [VERBAL] OK — "part of this premium reflects a hedging motive" is the core mechanism from Proposition 1 and line 157
- **Line 285** [VERBAL] OK — "requires market incompleteness—the inability to trade restricted AI equity" confirmed by lines 114, 173
- **Line 285** [VERBAL] OK — "attenuated by extinction risk, which reduces the weight on non-extinction states" is nearly verbatim from Proposition 2 (lines 161–163)
- **Line 285** [VERBAL] OK — "risk-averse households may inefficiently block AI development" confirmed by Proposition 3 (lines 212–217)
- **Line 285** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough to overwhelm deadweight costs" confirmed by Extension 2 (lines 259, 265, 278)
- **Line 287** [VERBAL] OK — stated abstractions (continuous-time dynamics, heterogeneous beliefs, production-side details) accurately describe what the model omits; goal statement consistent with paper framing

## Proof of Proposition 1 (lines 294–325)
- **Line 294** — appendix header, correctly references prop:pd-ratios and labels app:proof-pd
- **Lines 296–300** [ARITHMETIC] OK — Euler equation is the standard Lucas/CCAPM pricing equation with power utility SDF
- **Line 302** [DEFINITION] OK — v^AI = P^AI/D^AI constant in stationary pre-singularity equilibrium
- **Line 305** [ARITHMETIC] OK — no-singularity state: prob 1-p, consumption growth 1+g, dividend growth 1+g; consistent with balanced growth
- **Line 306** [ARITHMETIC] OK — non-extinction state: prob p(1-xi), consumption growth phi(1+g)(1+eta), dividend growth Gamma^AI(1+g); consistent with model setup
- **Line 307** [ARITHMETIC] OK — extinction state: prob p*xi, payoff zero; conventional treatment
- **Lines 311–316** [ARITHMETIC] OK — expanded Euler equation verified: no-singularity term beta(1+g)^{-gamma}(1+g)(v+1)D_t and non-extinction term beta(1+g)^{-gamma}[phi(1+eta)]^{-gamma}(1+g)Gamma^AI(v+1)D_t both correctly derived from SDF times payoff
- **Line 318** [ARITHMETIC] OK — Gamma^N = (1-Delta_theta)(1+eta) is theta-independent; verified: (1-theta')(1+eta)/(1-theta) = (1-theta)(1-Delta_theta)(1+eta)/(1-theta) = (1-Delta_theta)(1+eta); therefore non-AI closed form is exact
- **Line 318** [VERBAL] OK — approximation disclosure (post-singularity AI P/D approximated by v^AI, exact as Delta_theta -> 0) is correct; backward recursion for exact values is described
- **Lines 320–322** [ARITHMETIC] OK — solving v = A(v+1) gives v(1-A) = A, so v = A/(1-A); formula matches equation (4) in Proposition 1
- **Line 324** [VERBAL] OK — non-AI derivation is identical replacing Gamma^AI with Gamma^N; since Gamma^N is theta-independent, the non-AI closed form is exact
