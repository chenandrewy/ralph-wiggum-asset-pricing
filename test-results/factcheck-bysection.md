# tests/factcheck-bysection.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 6m 42s
[ralph-garage/agent-logs/20260409T210608.999265-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T210608.999265-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All claims across all sections are accurate; no arithmetic, verbal, reference, or figure/table errors found.

## Introduction (lines 38–72)
- **Line 38** — section header
- **Line 40** [VERBAL] OK — qualitative framing supported by Figure 1
- **Line 40** [FIGURE/TABLE] OK — NASDAQ (solid) dramatically outpaces S&P 500 (dashed) from shared base of 100 in Jan 2015, confirmed in fig-ai-valuations.pdf
- **Line 40** [VERBAL] OK — gap widening since 2023 visible in figure, consistent with generative AI timeline
- **Line 44** [FIGURE/TABLE] OK — caption correctly describes monthly closing prices, normalization to Jan 2015 = 100, line styles (solid/dashed)
- **Line 44** [REFERENCE] OK — sources verified in code: NASDAQ from FRED (series NASDAQCOM), S&P 500 from Shiller dataset (datahub.io)
- **Line 49** [VERBAL] OK — hedging motive is the paper's core thesis, supported by Proposition 1 (AI stocks have higher P/D due to hedging value)
- **Line 49** [VERBAL] OK — complete markets claim supported by Proposition 3(ii) and Section 2.3 discussion
- **Line 49** [VERBAL] OK — private capital held by founders/early-stage investors consistent with model setup (line 110) and GKP analogy (line 77)
- **Line 51** [REFERENCE] OK — GKP2012 displacement risk origination verified: "innovation creates a risk factor, which we call the 'displacement risk factor'" (GKP p.491)
- **Line 51** [REFERENCE] OK — GKP2012 rents accruing to untradeable agents verified: "future innovators, who are yet to enter the economy, are not able to trade"
- **Line 51** [VERBAL] OK — accurately describes building on GKP with discrete AI singularity
- **Line 53** [VERBAL] OK — closed-form P/D ratios confirmed in Proposition 1
- **Line 53** [ARITHMETIC] OK — "roughly six times": at p=1%, xi=0, ratio is 76.4/13.3 = 5.74, rounds to ~6
- **Line 53** [REFERENCE] OK — Jones (2024) extinction risk attenuation verified in table and Proposition 2(iii)
- **Line 53** [VERBAL] OK — "states in which AI is powerful enough..." matches Jones 2024 language verbatim
- **Line 55** [VERBAL] OK — market incompleteness distorting AI development supported by Proposition 3
- **Line 55** [VERBAL] OK — positive singularity more likely / socially efficient matches Extension 1 setup (line 201)
- **Line 55** [VERBAL] OK — risk-averse household vetoing matches Proposition 3(i)
- **Line 55** [VERBAL] OK — complete markets eliminating distortion matches Proposition 3(ii)
- **Line 57** [REFERENCE] OK — GKP2012 future innovators' capital cannot be traded, verified in source
- **Line 57** [VERBAL] OK — transfers with deadweight costs matches Extension 2 model (line 224)
- **Line 57** [REFERENCE] OK — Jones (2024) explosive output growth verified in source
- **Line 57** [VERBAL] OK — enormous resource base making redistribution effective supported by equation (7) and Extension 2 analysis
- **Line 59** [VERBAL] OK — meta-claim about AI-authored production consistent with project spec (Quality Req 5c)
- **Line 59** [VERBAL] OK — footnote on human author / AI agents division consistent with spec
- **Line 64** [REFERENCE] OK — GKP2012 general-equilibrium model with displacement risk factor verified
- **Line 64** [REFERENCE] OK — GKP2012 displacement risk distinct from aggregate consumption risk verified (GKP p.491)
- **Line 64** [REFERENCE] OK — GKP2012 growth stocks as partial hedge verified: "growth firms offer a hedge against displacement risk"
- **Line 64** [REFERENCE] OK — GKP2012 overlapping-generations structure verified
- **Line 66** [REFERENCE] OK — Jones (2024) trade-off between AI growth and existential risk verified
- **Line 66** [REFERENCE] OK — Jones (2024) bounded utility / conservative about extinction verified
- **Line 66** [VERBAL] OK — extinction risk attenuating (not amplifying) valuation premium confirmed by Proposition 2(iii) and table
- **Line 68** [REFERENCE] OK — KoganPapanikolaou2014 (JF) and KoganPapanikolaouStoffman2020 (JPE) correctly characterized
- **Line 68** [REFERENCE] OK — Knesl2023 (JFE) automation displacement risk premium verified by title
- **Line 68** [REFERENCE] OK — Barro2006 (QJE) and Wachter2013 (JF) rare disasters foundation verified
- **Line 68** [REFERENCE] OK — PastorVeronesi2009 (AER) technological revolutions and stock prices verified

## Model (lines 73–176)
- **Line 73** — section header
- **Line 75** — subsection header (Setup)
- **Line 77** [DEFINITION] OK — discrete infinite time, representative household as marginal investor, AI owners with private capital
- **Line 77** [REFERENCE] OK — GKP2012 analogy to future capital owners verified
- **Line 77** [ASSUMPTION] OK — "we do not explicitly model the entry of new cohorts" correctly stated; AI owners are static
- **Lines 79–84** [DEFINITION] OK — aggregate consumption $C_t$ growing at rate $g > 0$; equation (1) internally consistent
- **Line 86** [DEFINITION] OK — household share $\alpha_t \in (0,1)$, $c_t^H = \alpha_t C_t$, AI owners receive remainder
- **Lines 88–98** [DEFINITION] OK — singularity with probability $p$; non-extinction ($1-\xi$) with displacement $\phi$; extinction ($\xi$)
- **Line 97** [REFERENCE] OK — Jones (2024) "powerful AI ↔ existential risk" verified in source
- **Line 96** [VERBAL] OK — "smaller $\phi$ means larger displacement" correct from $\alpha_{t+1} = \phi \alpha_t$
- **Line 100** [VERBAL] OK — repeated singularities progressively displacing household, consistent with recursive structure
- **Lines 102–108** [DEFINITION] OK — AI stocks ($D_t^{AI} = \theta_t C_t$), non-AI stocks ($D_t^N = (1-\theta_t)C_t$), $\theta$ update rule
- **Line 110** [VERBAL] OK — private AI capital as source of market incompleteness correctly stated
- **Lines 112–117** [DEFINITION] OK — CRRA preferences with $\gamma > 1$, $\beta \in (0,1)$; standard utility formulation
- **Lines 119–121** [VERBAL] OK — household SDF reflects own consumption growth, not aggregate; consistent with incomplete markets
- **Lines 123–135** [ARITHMETIC] OK — P/D ratio formulas verified; $\Gamma^{AI} = (\theta + \Delta\theta(1-\theta))/\theta \cdot (1+\eta)$, $\Gamma^N = (1-\theta-\Delta\theta(1-\theta))/(1-\theta) \cdot (1+\eta)$; with baseline parameters: $\Gamma^{AI} = 3.2$, $\Gamma^N = 1.2$
- **Lines 137–139** [REFERENCE] OK — proof reference to Appendix A confirmed
- **Lines 141–147** [ARITHMETIC] OK — existence condition $A^j < 1$ correct; baseline $A^{AI} = 0.946$, $A^N = 0.917$ at $p=0.005$, $\xi=0$
- **Line 146** [REFERENCE] OK — reference to Section 4.2 for violation of existence condition confirmed (line 244)
- **Line 149** [VERBAL] OK — $\Gamma^{AI} > 1+\eta$ verified (3.2 > 1.5); $\Gamma^N < 1+\eta$ verified (1.2 < 1.5)
- **Line 149** [VERBAL] OK — $\phi(1+\eta) < 1$ when $\phi$ sufficiently small; baseline $0.5 \times 1.5 = 0.75 < 1$
- **Line 149** [VERBAL] OK — hedging channel explanation correct: AI stocks pay off when household consumption falls
- **Lines 151–158** [VERBAL] OK — Proposition 2 comparative statics: (i) increasing in displacement severity, (ii) increasing in $p$ for large $\gamma$, (iii) decreasing in $\xi$
- **Lines 160–166** [ARITHMETIC] OK — Proof of Proposition 2 verified: (i) $\phi^{-\gamma}$ increasing as $\phi$ decreases; (ii) more weight on singularity states; (iii) $f(A) = A/(1-A)$ is convex ($f'' = 2/(1-A)^3 > 0$), so higher $A^{AI}$ falls proportionally more when $\xi$ increases
- **Lines 168–170** [REFERENCE] OK — GKP2012 growth stocks / lower expected returns verified; continuous vs discrete displacement correctly characterized
- **Lines 172–173** [VERBAL] OK — market incompleteness centrality; complete markets would collapse valuation spread
- **Line 172** [REFERENCE] OK — GKP2012 future innovators cannot trade verified

## Quantitative Analysis (lines 177–194)
- **Lines 177–184** — table environment, no claims beyond exhibit reference
- **Line 186** [ASSUMPTION] OK — $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$; all seven values match code (generate-exhibits.R lines 18–24) and table footnote
- **Line 186** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; correct
- **Line 186** [ARITHMETIC] OK — "household consumption falls by 25%": $0.75 - 1 = -0.25$; correct
- **Line 186** [VERBAL] OK — "$\eta = 0.5$ (aggregate consumption rises by 50%)"; correct by definition
- **Line 186** [VERBAL] OK — "$\theta = 0.15$ (AI stocks are initially 15% of the economy)"; matches model and code
- **Line 186** [VERBAL] OK — "$\Delta\theta = 0.2$ (AI's share jumps by 20% of the non-AI remainder)"; matches formula
- **Line 188** [ARITHMETIC] OK — at $p=0.5\%$, $\xi=0$: AI P/D = 17.5, non-AI P/D = 11.1, ratio = 1.6; independently recomputed and matches table; "roughly 18" and "near 11" are fair roundings
- **Line 188** [ARITHMETIC] OK — at $p=1\%$, $\xi=0$: AI P/D = 76.4, non-AI P/D = 13.3, ratio = 5.8; "nearly 6 to 1" is a reasonable approximation of 5.8
- **Line 188** [VERBAL] OK — "increasing singularity probability raises AI stock premium" confirmed by table (ratio increases monotonically with $p$)
- **Line 188** [VERBAL] OK — "extinction risk reduces both valuations and compresses AI premium" confirmed by table
- **Line 188** [REFERENCE] OK — "as Proposition 2(iii) predicts" — direction consistent with the proposition
- **Line 190** [FIGURE/TABLE] OK — "NASDAQ appreciated roughly 50% more than S&P 500 since 2015": figure shows NASDAQ ~460 vs S&P ~340 (indexed to 100); cumulative returns 360% vs 240%, ratio 1.5; correct
- **Line 190** [VERBAL] OK — "P/D ratios 1.5 to 6 times higher across 0.5–1% range" matches table values

## Extensions: Market Incompleteness and the Singularity (lines 195–257)
- **Line 195** — section header
- **Line 197** [VERBAL] OK — accurately summarizes section purpose
- **Line 199** — subsection header (Extension 1)
- **Line 201** [DEFINITION] OK — positive singularity ($\alpha_{t+1} = \min(1, \alpha_t/\phi)$), negative singularity ($\alpha_{t+1} = \phi\alpha_t$); positive is more likely; social efficiency defined
- **Line 203** [REFERENCE] OK — Jones (2024) normalization of extinction utility to zero verified
- **Line 203** [ARITHMETIC] OK — CRRA utility negative for $c > 0$ when $\gamma > 1$: $u(c) = c^{1-\gamma}/(1-\gamma)$, with $1-\gamma < 0$ and $c^{1-\gamma} > 0$, so $u(c) < 0$; normalizing $U_\text{ext} = 0$ makes veto result conservative
- **Lines 205–209** [VERBAL] OK — Proposition 3: (i) household vetoes under incomplete markets for large $\gamma$ even when development is efficient; (ii) no veto under complete markets
- **Lines 212–216** [VERBAL] OK — proof sketch logically sound: concavity + risk aversion makes downside dominate under incomplete markets; complete markets allow full hedging
- **Line 218** [REFERENCE] OK — Jones (2024) bounded utility / conservatism about extinction consistent with source
- **Line 218** [VERBAL] OK — connection to AI regulation debates appropriately hedged ("may partly reflect")
- **Line 222** [REFERENCE] OK — GKP2012 on intergenerational transfers: "Such extensions would not change the functional form of Eq. (25) and would only affect the magnitude of the displacement factor" (GKP p.500); accurately characterized
- **Lines 224–228** [ARITHMETIC] OK — transfer consumption formula verified: household's own displaced consumption + net transfer (tax on AI surplus minus deadweight costs)
- **Line 232** [ARITHMETIC] OK — $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$; verified by factoring $c^H_{post}$
- **Lines 234–238** [ARITHMETIC] OK — transfer ratio $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$; $(1+\eta)$ terms cancel, confirming independence from $\eta$
- **Line 240** [VERBAL] OK — ratio exceeds 1 whenever $\tau > 0$; levels grow with $\eta$; both correct
- **Line 242** [ASSUMPTION] OK — $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$; baseline $\eta=0.5$, $\phi=0.5$; large $\eta=9$, $\phi=0.05$; all match code
- **Line 242** [ARITHMETIC] OK — large singularity $\phi(1+\eta) = 0.05 \times 10 = 0.5$; baseline $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$
- **Line 242** [VERBAL] OK — "consumption halves" ($\phi(1+\eta)=0.5$, i.e., 50% of pre-singularity) and "falls by 25%" ($\phi(1+\eta)=0.75$); both correct
- **Line 242** [VERBAL] OK — "ten-fold growth" ($1+\eta = 10$); correct
- **Line 242** [FIGURE/TABLE] OK — figure annotations show "50% loss" and "25% loss" at $\tau=0$; large singularity line rises dramatically; confirmed
- **Line 244** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$; verified
- **Line 244** [VERBAL] OK — P/D undefined at $\tau=0$ for large singularity: existence condition violated ($A^j > 1$); confirmed in code and figure (annotation "P/D → ∞ as τ → 0")
- **Line 244** [VERBAL] OK — "hedge value becomes infinite" / finite P/D emerges as $\tau$ increases; confirmed in figure
- **Line 248** [FIGURE/TABLE] OK — caption parameters ($\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$) all match code
- **Line 248** [VERBAL] OK — panel descriptions match figure content
- **Line 253** [REFERENCE] OK — Jones (2024) explosive growth and Nordhaus (2021) critical examination both correctly characterized

## Conclusion (lines 258–268)
- **Line 258** — section header
- **Line 260** [VERBAL] OK — "hedging motive" is the model's central result (Proposition 1)
- **Line 260** [VERBAL] OK — "requires market incompleteness" supported by Section 2.1 (line 110) and Section 2.3 (line 172)
- **Line 260** [VERBAL] OK — "attenuated by extinction risk" supported by Proposition 2(iii)
- **Line 260** [VERBAL] OK — "risk-averse households may inefficiently block AI development" supported by Proposition 3(i)
- **Line 260** [VERBAL] OK — "government transfers... can become effective" supported by Extension 2 analysis
- **Lines 261–263** [VERBAL] OK — model limitations correctly described (discrete time, representative household, reduced-form production)

## Proof of Proposition 1 (lines 269–298)
- **Line 269** — section header
- **Lines 271–274** [DEFINITION] OK — Euler equation is standard CRRA form, consistent with preferences at line 116
- **Line 277** [DEFINITION] OK — $v^{AI} = P^{AI}/D^{AI}$ constant in stationary equilibrium
- **Line 280** [ARITHMETIC] OK — no singularity: $c_{t+1}^H/c_t^H = 1+g$, $D_{t+1}^{AI}/D_t^{AI} = 1+g$; verified from model setup
- **Line 281** [ARITHMETIC] OK — non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$; $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$; verified
- **Line 282** [VERBAL] OK — extinction: $c_{t+1}^H = 0$, payoff is zero; verified from line 97
- **Lines 286–289** [ARITHMETIC] OK — Euler equation expansion verified: no-singularity term $\beta(1+g)^{-\gamma}(1-p)(1+g)(v^{AI}+1)D_t^{AI}$; non-extinction term $\beta(1+g)^{-\gamma} p(1-\xi)[\phi(1+\eta)]^{-\gamma}(1+g)\Gamma^{AI}(v^{AI}+1)D_t^{AI}$; extinction term zero
- **Line 291** [VERBAL] OK — stationarity approximation caveat correct: post-singularity $v^{AI}$ changes with $\theta$; exact as $\Delta\theta \to 0$
- **Lines 293–294** [ARITHMETIC] OK — solving $v = A(v+1)$ gives $v = A/(1-A)$ where $A = \beta(1+g)^{1-\gamma}[(1-p) + p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$; matches eq. (4) from Proposition 1
- **Line 297** [REFERENCE] OK — eq. (12) matches eq. (4); non-AI derivation identical by symmetry with $\Gamma^N$
