# tests/factcheck-bysection.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 5m 42s
[ralph-garage/agent-logs/20260411T100208.992695-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260411T100208.992695-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct; two minor verbal imprecisions found but no materially wrong claims.

## Introduction (lines 38–74)

- **Line 38** — section header
- **Line 40** [FIGURE/TABLE] OK — NASDAQ "dramatically outpaced" S&P 500 since 2015 with gap widening post-2023; confirmed by Figure 1
- **Line 40** [VERBAL] OK — NASDAQ described as "solid" line, S&P 500 as "dashed"; matches figure
- **Line 44** [FIGURE/TABLE] OK — caption states normalization to Jan 2015 = 100; matches figure and R code
- **Line 44** [REFERENCE] OK — sources stated as "NASDAQ from FRED; S&P 500 from the Shiller dataset"; matches R code (`download_fred("NASDAQCOM")` and datahub Shiller CSV)
- **Line 49** [DEFINITION] OK — definition of "negative AI singularity" consistent with model in Section 2 (lines 91–98)
- **Line 49** [VERBAL] OK — "part of this premium reflects a hedging motive" supported by Proposition 1 and discussion at lines 157–158
- **Line 51** [VERBAL] OK — restricted equity description consistent with Section 2 (lines 114–116) and GKP2012 framing
- **Line 53** [REFERENCE] OK — GKP2012 cited for technological displacement as systematic risk under incomplete markets; accurate characterization confirmed against spec/lit/GKP-2012.md
- **Line 55** [VERBAL] OK — "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks" supported by Table 1 (p=1.0%, xi=0%: ratio=2.0)
- **Line 55** [VERBAL] OK — "extinction risk attenuates this gap" supported by Proposition 2(iii) and table data (ratios decrease as xi increases)
- **Line 55** [REFERENCE] OK — Jones (2024) attribution for extinction risk characterization matches line 99 and source material
- **Line 57** [VERBAL] IMPRECISION — states "when the positive singularity is more likely than the negative one, AI development is socially efficient." Section 4.1 (line 213) defines Kaldor-Hicks efficiency as holding when (1+eta)>1, which is true by assumption regardless of q. The q>1/2 assumption governs expected household gains, not the KH condition. The introduction conflates these two conditions. Not materially wrong but imprecise.
- **Line 57** [REFERENCE] OK — "Proposition 3 shows calls to slow AI may reflect inability to share upside" confirmed by Proposition 3 (lines 219–224) and line 240
- **Line 59** [REFERENCE] OK — government transfers discussion confirmed by Section 4.2 (lines 246–248, 266–272)
- **Line 61** [REFERENCE] OK — all section cross-references resolve correctly (sec:model at line 75, sec:quant at line 187, sec:extensions at line 205, sec:conclusion at line 290)
- **Line 61** [VERBAL] OK — AI-produced paper disclosure is a statement of process, not a verifiable empirical claim
- **Line 66** [REFERENCE] OK — GKP2012 characterization as modeling displacement from innovation under incomplete markets confirmed against source
- **Line 66** [VERBAL] OK — "simplify their overlapping-generations structure" confirmed by line 79 (no explicit entry dynamics)
- **Line 68** [REFERENCE] OK — Jones (2024) trade-off characterization accurate; attenuation result confirmed by Proposition 2(iii)
- **Line 70** [REFERENCE] OK — literature citations (KoganPapanikolaou2014, Barro2006, Wachter2013, PastorVeronesi2009, etc.) with standard characterizations; no inconsistencies

## Model (lines 75–186)

- **Line 75** — section header
- **Line 79** [DEFINITION] OK — discrete-time, infinite-horizon setup with representative household and AI owners
- **Line 79** [REFERENCE] OK — GKP2012 analogy to future capital owners is a fair interpretive gloss confirmed against source
- **Line 79** [VERBAL] OK — "we do not explicitly model the entry of new cohorts" disclaimer consistent with model structure
- **Line 82** [ASSUMPTION] OK — constant consumption growth rate g>0 in absence of singularity
- **Line 85** [DEFINITION] OK — equation C_{t+1} = (1+g)C_t consistent throughout paper and appendix
- **Line 88** [DEFINITION] OK — household share alpha_t, consumption c_t^H = alpha_t C_t; remainder to AI owners
- **Line 91** [ASSUMPTION] OK — singularity probability p per period; three outcomes with correct probabilities
- **Line 94** [DEFINITION] OK — aggregate consumption jump factor 1+eta in non-extinction singularity
- **Line 96** [DEFINITION] OK — displacement equation alpha_{t+1} = phi * alpha_t, phi in (0,1)
- **Line 98** [VERBAL] OK — "smaller phi means larger displacement" correct since alpha_{t+1}/alpha_t = phi
- **Line 99** [DEFINITION] OK — extinction: C_{t+1} = 0; consistent with Appendix A (line 314)
- **Line 99** [REFERENCE] OK — Jones (2024) extinction risk characterization confirmed against source material
- **Line 102** [VERBAL] OK — repeated singularities progressively displace household; consistent with phi-compounding
- **Line 108** [DEFINITION] OK — AI stock dividends D_t^{AI} = theta_t C_t with theta update rule
- **Line 109** [DEFINITION] OK — non-AI dividends D_t^N = (1-theta_t) C_t
- **Line 112** [ARITHMETIC] OK — D^{AI} + D^N = theta C + (1-theta)C = C; verified
- **Line 112** [VERBAL] OK — distinction between alpha_t (consumption split) and theta_t (dividend split) clearly stated and consistent
- **Line 114** [VERBAL] OK — restricted equity as source of market incompleteness; consistent with model mechanism
- **Line 116** [VERBAL] OK — displacement parameter phi discussion; hedging channel description consistent with Proposition 1
- **Line 119** [ASSUMPTION] OK — CRRA with gamma>1 and beta in (0,1); baseline gamma=4 satisfies gamma>1
- **Line 122** [DEFINITION] OK — standard CRRA utility function
- **Line 127** [VERBAL] OK — SDF reflects household consumption growth under incomplete markets; confirmed by Appendix A
- **Line 132–134** [DEFINITION] OK — P/D formula for AI stocks; verified algebraically in Appendix A
- **Line 136–138** [DEFINITION] OK — P/D formula for non-AI stocks; identical structure with Gamma^N
- **Line 140** [ARITHMETIC] OK — Gamma^{AI} = [theta + Dtheta(1-theta)]/theta * (1+eta) = [0.15+0.17]/0.15 * 1.5 = 3.2
- **Line 140** [ARITHMETIC] OK — Gamma^N = [1-theta-Dtheta(1-theta)]/(1-theta) * (1+eta) = (1-Dtheta)(1+eta) = 0.8*1.5 = 1.2
- **Line 144** [REFERENCE] OK — proof reference to Appendix A (app:proof-pd at line 301) resolves correctly
- **Line 148** [VERBAL] OK — existence condition A^j < 1 for positive finite P/D ratios; follows from v = A/(1-A) formula
- **Line 150** [DEFINITION] OK — A^j definition consistent with P/D formula numerator
- **Line 152** [ARITHMETIC] OK — baseline satisfies A^j < 1: at p=1%, xi=0%, AI P/D=26.5 implies A=26.5/27.5=0.964<1
- **Line 152** [REFERENCE] OK — cross-reference to sec:ext2 (line 244) for existence violation discussion resolves correctly
- **Line 155** [VERBAL] OK — closed-form approximation caveat (post-singularity P/D = pre-singularity); exact when Dtheta->0
- **Line 155** [REFERENCE] OK — Table 1 described as "numerically exact"; backward recursion procedure described in Appendix A (line 325)
- **Line 157** [ARITHMETIC] OK — Gamma^{AI} > 1+eta: 3.2 > 1.5; confirmed
- **Line 157** [ARITHMETIC] OK — Gamma^N < 1+eta: 1.2 < 1.5; confirmed
- **Line 157** [ARITHMETIC] OK — phi(1+eta) < 1 when phi sufficiently small: 0.5*1.5 = 0.75 < 1; threshold is phi < 1/(1+eta) = 0.667
- **Line 157** [VERBAL] OK — hedging channel description: AI stocks pay off when household consumption falls; logically correct
- **Line 162** [VERBAL] OK — spread increasing in displacement severity (decreasing phi); phi^{-gamma} increases as phi falls
- **Line 163** [VERBAL] OK — spread increasing in p for gamma sufficiently large; conditional claim, proof consistent
- **Line 164** [VERBAL] OK — spread decreasing in xi; proof uses convexity of A/(1-A) with A^{AI} > A^N
- **Line 173** [VERBAL] OK — convexity argument for ratio decrease in xi; stated as parameterization-specific, which is honest
- **Line 178** [REFERENCE] OK — GKP2012 mechanism: growth stocks earn lower expected returns by hedging displacement; confirmed
- **Line 178** [REFERENCE] OK — GKP: "continuous displacement from expanding technological variety" vs. discrete singularity; accurate
- **Line 180** [VERBAL] OK — phi_eff -> 1 under complete markets; valuation spread vanishes; consistent with Extension 2
- **Line 180** [REFERENCE] OK — GKP point about non-tradeable future innovator rents confirmed against source
- **Line 182** [VERBAL] OK — existence condition violation unique to discrete singularity; cannot arise under GKP's gradual displacement; logically correct

## Quantitative Analysis (lines 187–204)

- **Line 187** — section header
- **Line 192** [DEFINITION] OK — table label tab:pd-ratios matches exhibit file
- **Line 196** [ASSUMPTION] OK — parameters beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, Dtheta=0.2; all match R code and table footnote
- **Line 196** [ARITHMETIC] OK — phi(1+eta) = 0.5*1.5 = 0.75; stated correctly
- **Line 196** [VERBAL] OK — "household consumption falls by 25%": post-singularity = 0.75 * pre-singularity, a 25% fall
- **Line 196** [VERBAL] OK — "aggregate consumption rises by 50%": (1+eta)=1.5, a 50% rise
- **Line 196** [VERBAL] OK — "AI stocks are initially 15% of the economy": theta=0.15
- **Line 196** [VERBAL] OK — "AI's share jumps by 20% of the non-AI remainder": Dtheta=0.2
- **Line 198** [ARITHMETIC] OK — "P/D of about 15.5" for p=0.5%, xi=0%: table gives 15.5; exact match
- **Line 198** [ARITHMETIC] OK — "non-AI stocks trade near 11": table gives 11.1; correct
- **Line 198** [ARITHMETIC] OK — "ratio of about 1.4": table gives 1.4; exact match
- **Line 198** [ARITHMETIC] OK — "At p=1%, the ratio rises to 2": table gives 2.0; exact match
- **Line 198** [VERBAL] OK — "increasing singularity probability raises AI stock premium": confirmed across all xi levels in table
- **Line 198** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium": confirmed in table (all P/D ratios decrease as xi increases, and ratio column decreases)
- **Line 198** [REFERENCE] OK — "as Proposition 2(iii) predicts": prop:comp-statics part (iii) at line 164 explicitly states this
- **Line 200** [VERBAL] IMPRECISION — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015." Figure shows NASDAQ at ~490 and S&P 500 at ~340 (both normalized to Jan 2015 = 100), so NASDAQ is ~44% higher in level terms. "Roughly 50%" overstates slightly. Not materially wrong given the "roughly" qualifier and the approximate nature of the comparison, but ~44% is closer to "roughly 40-45%."
- **Line 200** [VERBAL] OK — "comparison is imperfect" caveat is appropriate and honest
- **Line 200** [ARITHMETIC] OK — "AI stock P/D ratios are 1.3 to 2 times those of non-AI stocks across p in 0.5–1%": table confirms ratios range from 1.3 (p=0.5%, xi=10–20%) to 2.0 (p=1.0%, xi=0%)

## Extensions: Market Incompleteness and the Singularity (lines 205–289)

- **Line 205** — section header
- **Line 207** [VERBAL] OK — framing of extensions as examining distortions and policy; accurate summary
- **Line 211** [ASSUMPTION] OK — positive singularity: alpha_{t+1} = min(1, alpha_t/phi), aggregate jump 1+eta; q>1/2 assumed
- **Line 213** [VERBAL] OK — "socially efficient in Kaldor-Hicks sense" when (1+eta)>1: total surplus positive since aggregate consumption rises; condition always satisfied by assumption (eta>0)
- **Line 215** [DEFINITION] OK — veto at cost kappa: permanent fraction of consumption lost; extinction utility normalized to zero
- **Line 215** [VERBAL] OK — "CRRA utility is negative for all c>0 when gamma>1": u(c) = c^{1-gamma}/(1-gamma), and 1-gamma<0, so u(c)<0 for c>0; normalizing extinction to 0 makes veto result conservative
- **Line 217** [ARITHMETIC] OK — complete markets consumption = alpha(1+eta)C_t(1+g); household hedges displacement fully so share stays alpha
- **Line 221** [VERBAL] OK — Proposition 3(i): threshold gamma-bar exists for veto; proof logic at lines 227–233 is sound
- **Line 222** [VERBAL] OK — Proposition 3(ii): household never vetoes under complete markets; proof at lines 235–236 is correct
- **Line 233** [ARITHMETIC] OK — phi(1+eta) < 1 condition: 0.5*1.5=0.75<1; negative-singularity term dominates as gamma->infinity
- **Line 238** [ARITHMETIC] OK — veto numerical example verified against R code: V_develop=-15.53, V_veto=-15.32, so household vetoes under incomplete markets; V_develop^{CM}=-13.46 > V_veto, so no veto under complete markets
- **Line 238** [ARITHMETIC] OK — "positive singularity more than twice as likely": q=0.70, 1-q=0.30, ratio=2.33>2
- **Line 238** [ASSUMPTION] OK — parameters (phi=0.5, eta=0.5, xi=5%, p=1%, gamma=10, alpha=0.70, q=0.70, kappa=1%) match R code exactly
- **Line 240** [VERBAL] OK — extinction risk interaction with veto: conservative normalization (U_ext=0) reduces veto incentive; more severe penalty would amplify it; logically correct
- **Line 242** [REFERENCE] OK — Jones (2024) on attitudes toward AI risk depending on consumption levels; accurate characterization
- **Line 250** [DEFINITION] OK — tax rate tau on AI owners' post-singularity consumption; deadweight cost fraction delta*tau
- **Line 253** [ARITHMETIC] OK — transfer consumption formula: c^H_post = phi*alpha*(1+eta)*C_t*(1+g) + tau*(1-delta*tau)*(1-phi*alpha)*(1+eta)*C_t*(1+g); verified term by term
- **Line 261** [ARITHMETIC] OK — phi_eff = phi + tau(1-delta*tau)(1-phi*alpha)/alpha; derived correctly by dividing c^H_post by alpha*(1+eta)*(1+g)*C_t
- **Line 264** [VERBAL] OK — phi_eff enters SDF same way as phi, so Proposition 1 formula applies with substitution; correct
- **Line 269** [ARITHMETIC] OK — transfer ratio = 1 + tau(1-delta*tau)(1-phi*alpha)/(phi*alpha); (1+eta) cancels, ratio is eta-independent
- **Line 272** [VERBAL] OK — "transfers always improve household's position" whenever tau>0; ratio exceeds 1; correct
- **Line 274** [ARITHMETIC] OK — large singularity: phi=0.05, eta=9, so phi(1+eta)=0.05*10=0.50; "consumption halves" (50% loss)
- **Line 274** [ARITHMETIC] OK — baseline: phi=0.5, eta=0.5, so phi(1+eta)=0.5*1.5=0.75; "falls by 25%"
- **Line 276** [ARITHMETIC] OK — phi^{-gamma} = 0.05^{-4} = 20^4 = 160,000; exact match
- **Line 276** [VERBAL] OK — existence condition violated at tau=0 for large singularity; pricing sum diverges; confirmed by R code (compute_pd_with_transfer returns NA at tau=0 with phi=0.05)
- **Line 280** [ASSUMPTION] OK — figure caption parameters: alpha=0.70, p=0.5%, xi=5%, delta=0.5; all match R code (alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50)
- **Line 285** [REFERENCE] OK — Jones (2024) and Nordhaus (2021) cited for explosive output growth; appropriate references

## Conclusion (lines 290–300)

- **Line 290** — section header
- **Line 292** [VERBAL] OK — "AI stocks trade at high valuations": supported by Table 1 and Figure 1
- **Line 292** [VERBAL] OK — "hedging motive": supported by Proposition 1 and Section 2.3 discussion (line 157)
- **Line 292** [VERBAL] OK — "requires market incompleteness": supported by Section 2.3 (line 180, phi_eff->1 eliminates spread)
- **Line 292** [VERBAL] OK — "attenuated by extinction risk": supported by Proposition 2(iii) (line 164)
- **Line 292** [VERBAL] OK — "risk-averse households may inefficiently block AI development": supported by Proposition 3
- **Line 292** [VERBAL] OK — "government transfers can become effective if singularity-driven growth is large enough": supported by Extension 2 (lines 266–276)
- **Line 294** [VERBAL] OK — "model is deliberately simple": accurate self-characterization; abstractions listed are indeed absent from the model

## Proof of Proposition 1 (lines 301–332)

- **Line 301** — section header
- **Line 306** [DEFINITION] OK — Euler equation P_t^j = E_t[beta(c'/c)^{-gamma}(P'+D')]; standard
- **Line 309** [VERBAL] OK — P/D ratio constant in stationary pre-singularity equilibrium; consistent with model
- **Line 312** [ARITHMETIC] OK — no-singularity case: c'/c = 1+g and D'/D = 1+g; both verified from model definitions
- **Line 313** [ARITHMETIC] OK — non-extinction singularity: c'/c = phi(1+g)(1+eta); verified: alpha'=phi*alpha, C'=(1+g)(1+eta)C
- **Line 313** [ARITHMETIC] OK — D^{AI}'/D^{AI} = Gamma^{AI}(1+g); verified from theta update and consumption jump
- **Line 314** [ARITHMETIC] OK — extinction: c'=0, payoff is zero; consistent with model
- **Line 318–323** [ARITHMETIC] OK — Euler equation substitution verified term by term; no-singularity and non-extinction terms match
- **Line 325** [ARITHMETIC] OK — Gamma^N = (1-Dtheta)(1+eta) is theta-independent; algebraic simplification [1-theta-Dtheta(1-theta)]/(1-theta) = (1-theta)(1-Dtheta)/(1-theta) = 1-Dtheta; confirmed
- **Line 325** [VERBAL] OK — approximation caveat: post-singularity P/D treated as pre-singularity; exact as Dtheta->0; explicitly disclosed
- **Line 325** [VERBAL] OK — backward recursion for numerically exact values; procedure described and implemented in R code
- **Line 328** [ARITHMETIC] OK — final formula v = A/(1-A) where A = beta(1+g)^{1-gamma}[(1-p)+p(1-xi)(1+eta)^{-gamma}phi^{-gamma}Gamma^{AI}]; derived from Euler equation by dividing by D and solving; algebraically verified
- **Line 331** [VERBAL] OK — "derivation for non-AI stocks is identical, replacing Gamma^{AI} with Gamma^N"; SDF is the same, only dividend growth factor differs; correct
