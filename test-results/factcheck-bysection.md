# tests/factcheck-bysection.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 7m 42s
[ralph-garage/agent-logs/20260410T225642.533609-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260410T225642.533609-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong; only minor wording imprecisions were found.

## Introduction (lines 38–70)
- **Line 38** — section header
- **Line 40** [VERBAL] OK — "remarkable valuations" is a motivating observation with no precise number asserted
- **Line 40** [FIGURE/TABLE] OK — claims about NASDAQ vs S&P 500 since 2015 are consistent with Figure 1 data (FRED NASDAQ, Shiller S&P 500, normalized to Jan 2015 = 100); caption correctly describes NASDAQ as solid, S&P as dashed, matching code
- **Line 44** [REFERENCE] OK — caption sources ("NASDAQ from FRED; S&P 500 from the Shiller dataset") match the code's data downloads
- **Line 49** [VERBAL] OK — hedging motive, under-explored financial markets role, and distortion of valuations and AI development are all consistent with spec §I.3a–e
- **Line 51** [DEFINITION] OK — "negative AI singularity" definition consistent with spec §I.2a–b
- **Line 51** [VERBAL] OK — complete markets would allow full insurance; restricted equity prevents this; household uses public AI stocks as imperfect substitute — all consistent with model (lines 110–111)
- **Line 53** [REFERENCE] OK — GKP2012 characterization ("rents from new technologies accrue to agents that current investors cannot trade with") verified against spec/lit/GKP-2012.md (p.492: "future innovators...are not able to trade with the current population")
- **Line 53** [VERBAL] OK — "discrete AI singularity with severe displacement" accurately contrasts with GKP's continuous innovation framework
- **Line 53** [VERBAL] OK — model description (representative household, stochastic singularity, AI stocks grow as share of economy) matches Section 2
- **Line 55** [VERBAL] OK — "closed-form price-dividend ratios" supported by Proposition 1
- **Line 55** [ARITHMETIC] OK — "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks": table confirms ratio = 2.0 at p = 1%, xi = 0%; "can reach" is accurate for the maximum
- **Line 55** [VERBAL] OK — "consistent with observed valuation spreads" is a loose qualitative claim, appropriately hedged
- **Line 55** [REFERENCE] OK — Jones2024 extinction risk attenuation: table confirms ratios fall with xi (e.g., at p = 1%, ratio goes from 2.0 at xi = 0% to 1.7 at xi = 20%); Jones2024 lit file confirms the correlation between AI power and existential risk
- **Line 55** [VERBAL] OK — incomplete markets distort real decisions (veto), consistent with Extension 1 and spec §I.5c
- **Line 55** [VERBAL] OK — "positive singularity more likely... socially efficient... yet household may block" matches Proposition 3 and the 70/30 numerical example
- **Line 55** [VERBAL] OK — "complete markets would eliminate this distortion" matches Proposition 3(ii)
- **Line 57** [REFERENCE] OK — GKP2012 on future innovators' capital not yet tradeable: verified against lit file
- **Line 57** [VERBAL] OK — "transfers ordinarily incur deadweight costs" consistent with model (delta = 0.5) and spec §I.5d.ii
- **Line 57** [REFERENCE] OK — Jones2024 on explosive output growth: Jones models singularity delivering unbounded consumption
- **Line 57** [VERBAL] OK — "abundance of resources... overcomes market frictions" consistent with spec §I.3d
- **Line 57** [VERBAL] OK — footnote on AI-produced paper accurately describes workflow per spec §IV.5c
- **Line 62** [REFERENCE] OK — GKP2012 lit review characterization (displacement risk distinct from aggregate consumption risk, growth stocks as partial hedge, OLG structure) all verified against lit file
- **Line 64** [REFERENCE] OK — Jones2024 on bounded utility and extinction conservatism verified against lit file (p.575: "CRRA with risk aversion of two or more... quite conservative")
- **Line 64** [VERBAL] OK — "attenuating rather than amplifying" matches Proposition 2(iii) and table data
- **Line 66** [REFERENCE] OK — KoganPapanikolaou2014 (JF), KoganPapanikolaouStoffman2020 (JPE), Knesl2023 (JFE) characterizations consistent with paper titles and venues
- **Line 66** [REFERENCE] OK — AghionJonesJones2019 on AI and growth, Acemoglu2024 on modest productivity gains: characterizations accurate
- **Line 66** [REFERENCE] OK — Barro2006 (QJE) and Wachter2013 (JF) as rare disasters foundation; PastorVeronesi2009 (AER) on tech revolutions and stock prices: all accurate

## Model (lines 71–178)
- **Line 71** — section header
- **Line 75** [ASSUMPTION] OK — representative household as marginal investor, AI owners with private capital, analogy to GKP2012 future capital owners all consistent with spec §I.4b,d
- **Line 75** [REFERENCE] OK — GKP2012 analogy to "future capital owners who do not yet participate in markets" verified against lit file
- **Line 75** [VERBAL] OK — "we do not explicitly model the entry of new cohorts" consistent with spec §I.4d
- **Line 78** [ASSUMPTION] OK — constant consumption growth rate g > 0 absent singularity is a stated modeling assumption
- **Line 81** [DEFINITION] OK — eq:agg-consumption-growth is standard discrete-time growth
- **Line 84** [ARITHMETIC] OK — household gets alpha_t * C_t, AI owners get (1 - alpha_t) * C_t; these sum to C_t
- **Line 87** [ASSUMPTION] OK — singularity with probability p, no singularity leaves alpha unchanged
- **Line 91–92** [DEFINITION] OK — non-extinction singularity: consumption jumps by (1 + eta), household share drops to phi * alpha_t
- **Line 94** [VERBAL] OK — "smaller phi means larger displacement" is correct
- **Line 95** [REFERENCE] OK — extinction modeled as C_{t+1} = 0; Jones2024 citation for correlation between AI power and existential risk verified
- **Line 98** [VERBAL] OK — singularities can recur, progressively displacing household
- **Line 104** [DEFINITION] OK — D^AI = theta * C; theta updates by theta + dtheta * (1 - theta) upon singularity
- **Line 105** [DEFINITION] OK — D^N = (1 - theta) * C
- **Line 108** [ARITHMETIC] OK — D^AI + D^N = theta * C + (1 - theta) * C = C
- **Line 108** [VERBAL] OK — distinction between alpha (consumption split) and theta (public dividend split) correctly explained
- **Line 110** [ASSUMPTION] OK — restricted AI equity as source of market incompleteness
- **Line 113** [ASSUMPTION] OK — CRRA with gamma > 1 and beta in (0,1)
- **Line 116** [DEFINITION] OK — standard CRRA utility function
- **Line 121** [VERBAL] OK — household prices assets via Euler equation; SDF reflects household (not aggregate) consumption growth due to incomplete markets
- **Lines 127–128** [ARITHMETIC] OK — AI P/D formula matches appendix derivation (line 308)
- **Lines 130–132** [ARITHMETIC] OK — Non-AI P/D formula identical structure with Gamma^N replacing Gamma^AI
- **Line 134** [ARITHMETIC] OK — Gamma^AI = (0.15 + 0.2 * 0.85) / 0.15 * 1.5 = 0.32/0.15 * 1.5 = 3.2; Gamma^N = (1 - 0.2) * 1.5 = 1.2
- **Line 134** [VERBAL] OK — correctly described as dividend growth factors conditional on non-extinction singularity
- **Lines 142–146** [ARITHMETIC] OK — existence condition A^j < 1 ensures positive finite P/D; P/D = A/(1-A) diverges when A >= 1
- **Line 146** [REFERENCE] OK — forward reference to Section 4.2 for discussion of existence condition violation
- **Line 149** [VERBAL] OK — approximation is exact when dtheta -> 0 because theta barely shifts; less accurate as dtheta grows for AI stocks. Note: the non-AI P/D is actually exact for all dtheta since Gamma^N = (1 - dtheta)(1 + eta) is theta-independent (as the appendix states at line 305); the text does not distinguish this but is not wrong as stated
- **Line 151** [ARITHMETIC] OK — Gamma^AI = 3.2 > 1 + eta = 1.5; Gamma^N = 1.2 < 1.5
- **Line 151** [ARITHMETIC] OK — phi(1 + eta) = 0.5 * 1.5 = 0.75 < 1, so household consumption falls in singularity
- **Line 151** [VERBAL] OK — hedging channel correctly described: AI stocks pay off when household consumption falls
- **Line 156** [VERBAL] OK — Proposition 2(i): spread increasing in displacement severity (decreasing phi)
- **Line 157** [VERBAL] OK — Proposition 2(ii): spread increasing in p for gamma sufficiently large
- **Line 158** [VERBAL] OK — Proposition 2(iii): spread decreasing in xi
- **Line 163** [ARITHMETIC] OK — proof of (i): lower phi raises phi^{-gamma}, amplifies singularity term more for AI (Gamma^AI > Gamma^N)
- **Line 165** [VERBAL] OK — proof of (ii): higher p puts more weight on singularity states where AI outperforms
- **Line 167** [ARITHMETIC] OK — proof of (iii): convexity of A/(1-A) means higher A^AI falls proportionally more when xi increases; conclusion correct though wording "same multiplicative factor on their singularity terms" is slightly loose (means same factor on (1-xi), not same absolute change in A^j)
- **Line 172** [REFERENCE] OK — GKP2012 comparison (growth stocks hedge displacement, continuous vs discrete displacement) verified against lit file
- **Line 174** [VERBAL] OK — complete markets would collapse valuation spread; AI owners analogous to GKP's future innovators; paper disclaims modeling entry dynamics

## Quantitative Analysis (lines 179–196)
- **Line 179** — section header
- **Lines 181–186** [FIGURE/TABLE] OK — table correctly labeled, \input points to exhibits/table-pd-ratios.tex which exists
- **Line 188** [ASSUMPTION] OK — beta = 0.96, g = 0.02, gamma = 4, phi = 0.5, eta = 0.5, theta = 0.15, dtheta = 0.2 all match code and table footnote
- **Line 188** [ARITHMETIC] OK — phi(1 + eta) = 0.5 * 1.5 = 0.75
- **Line 188** [VERBAL] OK — "household consumption falls by 25%": retains 75%, loses 25%
- **Line 188** [VERBAL] OK — "aggregate consumption rises by 50%": eta = 0.5
- **Line 188** [VERBAL] OK — "AI stocks are initially 15% of the economy": theta = 0.15
- **Line 188** [VERBAL] OK — "AI's share jumps by 20% of the non-AI remainder": dtheta = 0.2
- **Line 190** [ARITHMETIC] OK — "P/D of about 15.5" at p = 0.5%, xi = 0%: table says 15.5
- **Line 190** [ARITHMETIC] OK — "non-AI stocks trade near 11": table says 11.1
- **Line 190** [ARITHMETIC] OK — "ratio of about 1.4": table says 1.4
- **Line 190** [ARITHMETIC] OK — "At p = 1%, the ratio rises to 2": table says 2.0 at p = 1%, xi = 0%
- **Line 190** [VERBAL] OK — "increasing singularity probability raises AI stock premium": ratios rise monotonically from 1.1 (p = 0.1%) to 2.0 (p = 1%) at xi = 0%
- **Line 190** [VERBAL] OK — "extinction risk reduces both valuations": at p = 1%, AI falls from 26.5 (xi = 0%) to 20.5 (xi = 20%); non-AI falls from 13.3 to 12.0
- **Line 190** [VERBAL] OK — "compresses the AI premium": at p = 1%, ratio falls from 2.0 (xi = 0%) to 1.7 (xi = 20%)
- **Line 190** [REFERENCE] OK — "as Proposition 2(iii) predicts": Proposition 2(iii) states spread is decreasing in xi, consistent with table
- **Line 192** [FIGURE/TABLE] OK — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015": directionally correct and conservatively stated based on FRED data; appropriately hedged with caveats
- **Line 192** [VERBAL] OK — caveats about NASDAQ breadth, earnings vs multiples, and S&P AI exposure are appropriate
- **Line 192** [ARITHMETIC] OK — "1.3 to 2 times" across p = 0.5–1%: table confirms ratios span 1.3 (p = 0.5%, xi = 10–20%) to 2.0 (p = 1%, xi = 0%)

## Extensions: Market Incompleteness and the Singularity (lines 197–269)
- **Line 197** — section header
- **Line 199** [VERBAL] OK — section scope description consistent with content
- **Line 203** [DEFINITION] OK — positive singularity alpha_{t+1} = min(1, alpha_t / phi) correctly reverses displacement
- **Line 203** [VERBAL] OK — "positive singularity is more likely" consistent with 70/30 split; "socially efficient" is a framing assumption
- **Line 205** [DEFINITION] OK — extinction utility normalized to zero; simplifies Jones2024's bounded utility framework
- **Line 205** [ARITHMETIC] OK — "CRRA utility is negative for all c > 0 when gamma > 1": u(c) = c^{1-gamma}/(1-gamma), with 1-gamma < 0, so u(c) < 0
- **Line 205** [VERBAL] OK — normalization makes veto result conservative: U_ext = 0 is above the true negative CRRA value, making extinction less bad, reducing veto incentive
- **Lines 209–210** [VERBAL] OK — Proposition 3(i) and (ii) statements are internally consistent with the proof
- **Lines 215–218** [VERBAL] OK — proof logic: (i) gamma large makes downside dominate despite positive singularity being more likely; (ii) complete markets allow full hedging so household welfare reflects positive social surplus
- **Line 220** [ARITHMETIC] OK — "positive singularity more than twice as likely": 70/30 = 2.33 > 2
- **Line 220** [ARITHMETIC] OK — "household vetoes under incomplete markets": V_veto = -15.3222 > V_develop = -15.5327 (VETO confirmed by code)
- **Line 220** [ARITHMETIC] OK — "Under complete markets... does not veto": V_develop_complete = -13.4615 > V_veto = -15.3222 (DEVELOP confirmed by code)
- **Line 220** [VERBAL] OK — parenthetical about one-shot tractability and compounding displacement is economically sound
- **Line 222** [VERBAL] OK — "higher xi reduces weight on non-extinction states": mechanically correct, non-extinction term weighted by p(1 - xi)
- **Line 222** [REFERENCE] OK — Jones2024 on bounded utility and conservatism about extinction risk verified; paper's inference about amplified veto incentive under more severe extinction penalty is a reasonable extension
- **Line 224** [REFERENCE] OK — Jones2024 observation about wealth heterogeneity and risk attitudes verified against Jones Section C: "people who are rich or very risk averse would be much less willing to take such gambles"
- **Line 228** [REFERENCE] OK — GKP2012 on intergenerational transfers: verified (p.498: "altruistically-linked dynasty, bequests...would ensure...same consumption...displacement factor is identically equal to one")
- **Line 228** [REFERENCE] OK — GKP2012 on transfers not altering SDF functional form: verified (p.498: "would not change the functional form of Eq. (25)")
- **Lines 232–234** [ARITHMETIC] OK — transfer consumption equation verified: first term is displaced household consumption phi * alpha * (1+eta) * C_t * (1+g); second term is tax tau on AI surplus (1 - phi*alpha) * (1+eta) * C_t * (1+g) net of deadweight delta*tau
- **Line 236** [VERBAL] OK — distinction between consumption share alpha and dividend share theta for transfer base correctly explained
- **Lines 240–242** [ARITHMETIC] OK — phi_eff = phi + tau(1 - delta*tau)(1 - phi*alpha)/alpha verified by dividing eq(7) by alpha*(1+eta)*(1+g)*C_t; matches code line 152
- **Line 244** [VERBAL] OK — phi_eff enters SDF identically to phi, so Proposition 1 applies with substitution
- **Lines 248–250** [ARITHMETIC] OK — transfer ratio = 1 + tau(1 - delta*tau)(1 - phi*alpha)/(phi*alpha); (1+eta) cancels, confirming independence from eta
- **Line 249** [VERBAL] OK — ratio exceeds 1 when tau > 0: all factors positive since delta*tau < 1 for tau in (0,1) with delta = 0.5
- **Line 252** [VERBAL] OK — absolute consumption gains grow without bound as eta grows, even though ratio is constant
- **Line 254** [FIGURE/TABLE] OK — parameters match code: alpha = 0.70, p = 0.5%, xi = 5%, delta = 0.5; baseline eta = 0.5, phi = 0.5; large eta = 9, phi = 0.05
- **Line 254** [ARITHMETIC] OK — "consumption halves under large singularity": phi(1+eta) = 0.05 * 10 = 0.5
- **Line 254** [ARITHMETIC] OK — "falls by 25% under baseline": phi(1+eta) = 0.5 * 1.5 = 0.75
- **Line 256** [ARITHMETIC] OK — phi^{-gamma} = 0.05^{-4} = 20^4 = 160,000
- **Line 256** [VERBAL] OK — P/D undefined at tau = 0 for large singularity: existence condition A >= 1 confirmed computationally (code returns NA for large singularity at tau = 0)
- **Line 256** [VERBAL] OK — "hedge value becomes infinite... no finite price can compensate" follows from A >= 1 divergence
- **Lines 258–263** [FIGURE/TABLE] OK — caption parameters match code; panel descriptions consistent with generated figure
- **Line 265** [REFERENCE] OK — Jones2024 for explosive output growth; Nordhaus2021 "Are We Approaching an Economic Singularity?" (AEJ: Macro) as critical examination; both accurate

## Conclusion (lines 270–280)
- **Line 270** — section header
- **Line 272** [VERBAL] OK — "AI stocks trade at high valuations" supported by Figure 1 and Section 3
- **Line 272** [VERBAL] OK — "hedging motive: investors use AI stocks to partially insure" is the model's central mechanism (Proposition 1, line 151)
- **Line 272** [VERBAL] OK — "requires market incompleteness" supported by lines 110–111, 174
- **Line 272** [VERBAL] OK — "attenuated by extinction risk" matches Proposition 2(iii) and table data
- **Line 272** [VERBAL] OK — "risk-averse households may inefficiently block AI development" matches Proposition 3(i)
- **Line 272** [VERBAL] OK — "government transfers... can become effective if singularity-driven growth is large enough to overwhelm deadweight costs" matches Extension 2 (lines 246–252, 265)
- **Line 274** [VERBAL] OK — "abstracts from continuous-time dynamics" accurate (model is discrete-time, line 72)
- **Line 274** [VERBAL] OK — "heterogeneous beliefs" accurately listed as omission (single representative agent)
- **Line 274** [VERBAL] OK — "production-side details" accurately listed as omission (no production function)
- **Line 274** [VERBAL] OK — goal statement ("highlight a specific channel... hedging against displacement under incomplete markets") consistent with abstract and introduction

## Proof of Proposition~\ref{prop:pd-ratios} (lines 281–312)
- **Line 281** — section header; label app:proof-pd matches reference at line 138
- **Line 286** [ARITHMETIC] OK — standard CRRA Euler equation correctly stated
- **Line 289** [VERBAL] OK — stationarity approximation (v^AI constant) correctly flagged; exact when dtheta -> 0
- **Line 292** [ARITHMETIC] OK — no-singularity case: c_{t+1}^H / c_t^H = (1+g), D_{t+1}^AI / D_t^AI = (1+g)
- **Line 293** [ARITHMETIC] OK — non-extinction singularity: c_{t+1}^H / c_t^H = phi(1+g)(1+eta), D_{t+1}^AI / D_t^AI = Gamma^AI * (1+g)
- **Line 294** [ARITHMETIC] OK — extinction: c_{t+1}^H = 0, payoff is zero (SDF * 0 = 0)
- **Lines 300–301** [ARITHMETIC] OK — Euler equation expansion verified: beta(1+g)^{-gamma} factored out; no-singularity term (1-p)(1+g)(v+1)D correct; singularity term p(1-xi)[phi(1+eta)]^{-gamma}(1+g) Gamma^AI (v+1)D correct; extinction term contributes zero
- **Line 305** [ARITHMETIC] OK — Gamma^N = [(1-theta)(1-dtheta)/(1-theta)](1+eta) = (1-dtheta)(1+eta) is theta-independent; non-AI closed form is exact
- **Line 305** [VERBAL] OK — backward recursion over theta chain for numerically exact AI P/D correctly described
- **Line 308** [ARITHMETIC] OK — solving v = A(v+1) gives v = A/(1-A) where A = beta(1+g)^{1-gamma}[(1-p) + p(1-xi)(1+eta)^{-gamma} phi^{-gamma} Gamma^AI]; matches Proposition 1 formula
- **Line 311** [VERBAL] OK — "derivation for non-AI stocks is identical, replacing Gamma^AI with Gamma^N"
