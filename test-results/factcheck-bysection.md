# tests/factcheck-bysection.py
Started: 2026-04-09 21:34:52 EDT
Runtime: 6m 46s
[ralph-garage/agent-logs/20260409T213452.267280-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T213452.267280-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: FAIL
REASON: The paper claims the stationary-P/D approximation error is "small" at Deltaθ=0.2, but the actual error is ~12% for the AI P/D ratio and ~41% for the valuation spread.

## Introduction (lines 38–72)

- **Line 38** — section header
- **Line 40** [VERBAL] OK — NASDAQ outpacing S&P 500 since 2015 is supported by Figure 1 and underlying data (FRED NASDAQCOM, Shiller S&P 500)
- **Line 44** [FIGURE/TABLE] OK — caption accurately describes normalization (Jan 2015 = 100) and data sources (NASDAQ from FRED; S&P 500 from Shiller dataset); confirmed against R code
- **Line 49** [VERBAL] OK — hedging motive and market incompleteness claims are consistent with the model in Section 2
- **Line 51** [REFERENCE] OK — GKP2012 attribution ("rents from new technologies accrue to agents that current investors cannot trade with") is used consistently with model Section 2.1 and Discussion Section 2.3
- **Line 53** [VERBAL] OK — "closed-form price-dividend ratios" confirmed by Proposition 1 (lines 123–135)
- **Line 53** [ARITHMETIC] OK — "roughly six times" supported by table: p=1%, xi=0% gives ratio 5.8; "roughly six" is reasonable rounding
- **Line 53** [VERBAL] OK — "across plausible singularity probabilities" is acceptable phrasing since "can reach" signals a maximum; Section 3 (line 192) gives the precise range of 1.5 to 6
- **Line 53** [REFERENCE] OK — "Extinction risk attenuates this gap" supported by Proposition 2(iii) and Table 1 (e.g., at p=1%, ratio falls from 5.8 at xi=0% to 4.3 at xi=5%)
- **Line 55** [VERBAL] OK — veto result consistent with Extension 1, Proposition 3
- **Line 57** [REFERENCE] OK — GKP2012 characterization consistent with rest of paper
- **Line 57** [VERBAL] OK — explosive growth overwhelming deadweight costs supported by Extension 2 (large-singularity scenario with eta=9)
- **Line 59** [VERBAL] OK — AI-authorship disclosure is a factual statement about the paper's production process, not a model claim
- **Line 64** [REFERENCE] OK — GKP2012 lit review characterization consistent with model Section 2.3 discussion
- **Line 66** [REFERENCE] OK — Jones2024 characterization consistent with how extinction risk is incorporated (line 97)
- **Line 68** [REFERENCE] OK — external citations (Kogan-Papanikolaou, Knesl, Aghion-Jones-Jones, Acemoglu, Barro, Wachter, Pastor-Veronesi) used for context; no internal cross-references to verify

## Model (lines 73–178)

- **Line 73** — section header
- **Line 75** — subsection header (Setup)
- **Line 77** [DEFINITION] OK — representative household as marginal investor, AI owners hold private capital, not marginal in public stocks; consistent with GKP analogy and caveat about not modeling entry dynamics
- **Line 80** [ASSUMPTION] OK — constant consumption growth rate g > 0 absent singularity
- **Line 86** [DEFINITION] OK — household consumption c_t^H = alpha_t * C_t; AI owners get (1-alpha_t)*C_t; consistent with Extension 2 usage of (1-phi*alpha) as AI owners' post-singularity share
- **Line 89** [ASSUMPTION] OK — singularity probability p per period; alpha unchanged absent singularity
- **Line 92** [DEFINITION] OK — non-extinction singularity: aggregate consumption jumps by (1+eta), household share displaced to phi*alpha_t
- **Line 96** [DEFINITION] OK — smaller phi means larger displacement; consistent throughout
- **Line 97** [DEFINITION] OK — extinction sets C_{t+1}=0; attribution to Jones2024 consistent
- **Line 106** [DEFINITION] OK — AI dividends D^AI = theta*C, with theta jumping by Delta_theta*(1-theta) upon singularity; non-AI dividends D^N = (1-theta)*C
- **Line 110** [VERBAL] OK — market incompleteness from restricted equity (founders, pre-IPO, not-yet-existing firms); household cannot purchase restricted shares
- **Line 113** [DEFINITION] OK — CRRA with gamma > 1 and beta in (0,1); consistent with gamma=4, beta=0.96 used in calibration
- **Line 119** — subsection header (Equilibrium prices)
- **Line 121** [VERBAL] OK — household prices assets via its own Euler equation; SDF reflects own consumption growth, not aggregate; follows from market incompleteness
- **Line 127–132** [ARITHMETIC] OK — P/D formulas in Proposition 1 verified against Appendix A proof derivation
- **Line 134** [ARITHMETIC] OK — Gamma^AI = [0.15+0.2*0.85]/0.15 * 1.5 = 0.32/0.15 * 1.5 = 3.2; Gamma^N = [0.85-0.17]/0.85 * 1.5 = 0.68/0.85 * 1.5 = 1.2
- **Line 142** [DEFINITION] OK — existence condition A^j < 1 correctly stated as necessary and sufficient for finite P/D
- **Line 146** [ARITHMETIC] OK — "baseline calibration satisfies A^j < 1 for both assets" verified: at p=0.5%, xi=0%, A^AI=0.946, A^N=0.917, both < 1
- **Line 146** [REFERENCE] OK — "As we discuss in Section 4.2" references sec:ext2 (line 222), which explicitly discusses the existence condition being violated under large-singularity parameters (phi^{-gamma}=160,000)
- **Line 149** [VERBAL] ERROR — claims "the approximation error is small" for Delta_theta=0.2, but independent recomputation shows:
  - Approximate AI P/D = 17.47; exact 2-state AI P/D = 15.62; error = 11.9%
  - Non-AI P/D is unaffected (Gamma^N = (1-Delta_theta)*(1+eta) is theta-independent)
  - Approximate spread = 6.38; exact spread = 4.53; spread error = 40.9%
  - The approximation overstates both the AI P/D ratio and the valuation spread by a material amount
- **Line 151** [ARITHMETIC] OK — Gamma^AI = 3.2 > 1.5 = 1+eta; Gamma^N = 1.2 < 1.5 = 1+eta
- **Line 151** [ARITHMETIC] OK — phi(1+eta) = 0.5*1.5 = 0.75 < 1 at baseline
- **Line 151** [VERBAL] OK — hedging channel narrative (AI stocks pay off when household consumption falls) follows correctly from the algebra
- **Line 153** — Proposition 2 header
- **Line 163** [VERBAL] OK — Proposition 2(i) proof: decrease in phi raises phi^{-gamma}, amplifying singularity weight more for AI stocks since Gamma^AI > Gamma^N
- **Line 165** [VERBAL] OK — Proposition 2(ii) proof: higher p puts more weight on singularity states; for large gamma the marginal utility effect dominates
- **Line 167** [VERBAL] OK (minor imprecision) — Proposition 2(iii) proof: the conclusion is correct (verified numerically: AI P/D falls proportionally more when xi increases). The convexity argument is stated slightly loosely—the dominant effect is that A^AI has a larger singularity term than A^N, so the same multiplicative reduction in (1-xi) produces a larger absolute decrease in A^AI; convexity amplifies this further. The conclusion holds; the proof mechanism is imprecise but not wrong.
- **Line 170** — subsection header (Discussion)
- **Line 172** [VERBAL] OK — GKP comparison is fair: continuous displacement from expanding variety vs. discrete AI singularity
- **Line 174** [VERBAL] OK — market incompleteness discussion correctly identifies the mechanism; analogy to GKP's future innovators is apt with appropriate caveat about not modeling entry dynamics

## Quantitative Analysis (lines 179–196)

- **Line 179** — section header
- **Line 188** [ASSUMPTION] OK — all seven parameter values (beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, Delta_theta=0.2) match the table footnote and R code exactly
- **Line 188** [ARITHMETIC] OK — phi(1+eta) = 0.5*1.5 = 0.75, so "household consumption falls by 25%" is correct
- **Line 190** [FIGURE/TABLE] OK (borderline) — "AI stocks trade at a P/D of roughly 18" for p=0.5%, xi=0%; table shows 17.5 (recomputed: 17.47). "Roughly 18" rounds up by 0.5; acceptable as a rough characterization but closer to 17.5
- **Line 190** [FIGURE/TABLE] OK — "non-AI stocks trade near 11"; table shows 11.1 (recomputed: 11.09)
- **Line 190** [FIGURE/TABLE] OK — "a ratio of about 1.6"; table shows exactly 1.6
- **Line 190** [FIGURE/TABLE] OK — "At p=1%, the ratio rises to nearly 6 to 1"; table shows 5.8 at p=1%, xi=0%
- **Line 190** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium" confirmed by every row group in the table
- **Line 190** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium" confirmed by table: within every p-group, increasing xi lowers both P/D values and the ratio
- **Line 190** [REFERENCE] OK — "as Proposition 2(iii) predicts" is accurately cross-referenced
- **Line 192** [FIGURE/TABLE] OK (minor) — "1.5 to 6 times higher across annual singularity probabilities in the 0.5–1% range"; at p=0.5% with xi=20% the ratio is 1.4, slightly below 1.5; within the stated range for xi <= 10% the bound holds
- **Line 192** [FIGURE/TABLE] OK (imprecision possible) — "the AI-heavy NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015" refers to Figure 1; this was likely accurate when written but may understate the current gap depending on the data download date, as the figure extends to latest available data

## Extensions: Market Incompleteness and the Singularity (lines 197–265)

- **Line 197** — section header
- **Line 199** [VERBAL] OK — framing of extensions as examining consequences of incompleteness beyond pricing
- **Line 201** — subsection header (Extension 1: Veto)
- **Line 203** [DEFINITION] OK — positive singularity raises household share to min(1, alpha/phi), aggregate jumps by (1+eta); negative singularity lowers to phi*alpha; positive outcome is more likely; AI development is socially efficient
- **Line 205** [DEFINITION] OK — veto at significant cost; extinction utility normalized to zero; CRRA utility negative for c>0 when gamma>1, making the normalization conservative
- **Line 209** [VERBAL] OK — Proposition 3(i): under incomplete markets, household vetoes even when development is socially efficient and veto cost is substantial; proof at lines 214–217 is logically sound (large gamma makes downside dominate via extreme concavity)
- **Line 211** [VERBAL] OK — Proposition 3(ii): under complete markets, household never vetoes socially efficient development; proof at lines 217–218 is correct (hedging aligns household utility with social surplus)
- **Line 220** [VERBAL] OK — extinction risk interaction: under conservative normalization (U_ext=0), higher xi reduces weight on non-extinction states driving veto; with more severe extinction penalty, higher xi would amplify veto incentive
- **Line 222** — subsection header (Extension 2: Government transfers)
- **Line 224** [REFERENCE] OK — GKP2012 note about intergenerational transfers is consistent with paper's characterization
- **Line 229** [ARITHMETIC] OK — transfer consumption formula verified: first term is displaced household consumption phi*alpha*(1+eta)(1+g)*C_t; second term is net transfer tau*(1-delta*tau)*(1-phi*alpha)*(1+eta)(1+g)*C_t
- **Line 232** [VERBAL] OK — (1-phi*alpha) correctly identified as AI owners' share of post-singularity aggregate consumption; transfer is on consumption allocation, not public dividends
- **Line 237** [ARITHMETIC] OK — phi_eff = phi + tau(1-delta*tau)(1-phi*alpha)/alpha; verified by dividing eq. (11) by alpha*(1+eta)*(1+g)*C_t
- **Line 240** [VERBAL] OK — phi_eff enters SDF in the same way as phi, so Proposition 1 applies with substitution; correct
- **Line 245** [ARITHMETIC] OK — transfer ratio = 1 + tau(1-delta*tau)(1-phi*alpha)/(phi*alpha); verified algebraically; (1+eta) cancels from numerator and denominator
- **Line 248** [VERBAL] OK — "independent of eta" is correct: both c^H_post and c^H_no-transfer contain (1+eta) which cancels in the ratio
- **Line 248** [VERBAL] OK — "as eta grows, both grow without bound, so even inefficient transfers deliver arbitrarily large consumption gains relative to pre-singularity baseline" is a correct characterization of the levels result
- **Line 250** [ASSUMPTION] OK — alpha=0.70, p=0.5%, xi=5% confirmed against R code (alpha0=0.70, p_ext=0.005, xi_ext=0.05)
- **Line 250** [ARITHMETIC] OK — baseline: eta=0.5, phi=0.5, phi(1+eta)=0.75, consumption falls by 25%
- **Line 250** [ARITHMETIC] OK — large singularity: eta=9, phi=0.05, phi(1+eta)=0.5, consumption halves; "ten-fold growth" = 1+eta=10
- **Line 252** [ARITHMETIC] OK — phi^{-gamma} = 0.05^{-4} = 20^4 = 160,000
- **Line 252** [VERBAL] OK — "pricing sum diverges" / "hedge value becomes infinite" follows from the existence condition being violated when phi_eff is very small
- **Line 252** [VERBAL] OK — "as tau increases, effective displacement falls, existence condition is restored, and finite P/D ratios emerge" is consistent with the figure showing P/D emerging from infinity as tau rises
- **Line 256** [ASSUMPTION] OK — caption states delta=0.5, confirmed against R code (delta=0.50)
- **Line 261** [REFERENCE] OK — Jones2024 and Nordhaus2021 cited for explosive output growth; contextually appropriate

## Conclusion (lines 266–276)

- **Line 266** — section header
- **Line 268** [VERBAL] OK — "AI stocks trade at high valuations" supported by Figure 1 and introduction
- **Line 268** [VERBAL] OK — "hedging motive" summary accurately captures the model mechanism from Proposition 1 and Section 2.3
- **Line 268** [VERBAL] OK — "requires market incompleteness" supported by Section 2.1 and Discussion
- **Line 268** [VERBAL] OK — "attenuated by extinction risk" supported by Proposition 2(iii) and Table 1
- **Line 268** [VERBAL] OK — "risk-averse households may inefficiently block AI development" supported by Proposition 3(i)
- **Line 268** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough" supported by Extension 2 (equation 13 and figure)
- **Line 270** [VERBAL] OK — scope disclaimer ("deliberately simple...abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details") accurately characterizes the model

## Proof of Proposition 1 (lines 277–306)

- **Line 277** — section header (Appendix A)
- **Line 282** [ARITHMETIC] OK — Euler equation is the standard CRRA Euler equation, correct given preferences in eq. (5)
- **Line 285** [VERBAL] OK — P/D ratio is constant in stationary equilibrium before any singularity (theta and alpha unchanged, C grows geometrically)
- **Line 288** [ARITHMETIC] OK — no singularity: c^H_{t+1}/c^H_t = 1+g (alpha unchanged, C grows by 1+g); D^AI_{t+1}/D^AI_t = 1+g (theta unchanged, C grows by 1+g)
- **Line 289** [ARITHMETIC] OK — non-extinction singularity: c^H_{t+1}/c^H_t = phi(1+g)(1+eta); verified from c^H_{t+1} = phi*alpha*(1+eta)(1+g)*C_t, c^H_t = alpha*C_t
- **Line 289** [ARITHMETIC] OK — D^AI_{t+1}/D^AI_t = Gamma^AI*(1+g); verified from D^AI_{t+1} = [theta+Delta_theta*(1-theta)]*(1+eta)*(1+g)*C_t, D^AI_t = theta*C_t
- **Line 290** [ARITHMETIC] OK — extinction: c^H_{t+1}=0, payoff is zero; consistent with C_{t+1}=0
- **Line 294–296** [ARITHMETIC] OK — Euler expansion correctly factors out beta*(1+g)^{-gamma}; SDF in singularity state beta*[phi(1+g)(1+eta)]^{-gamma} combined with dividend growth Gamma^AI*(1+g) gives the singularity term; verified step by step
- **Line 299** [VERBAL] OK — correctly identifies the approximation (post-singularity P/D treated as equal to pre-singularity P/D) and notes it is exact as Delta_theta -> 0
- **Line 302** [ARITHMETIC] OK — solving v = B(v+1) gives v = B/(1-B) where B = beta*(1+g)^{1-gamma}*[(1-p) + p*(1-xi)*(1+eta)^{-gamma}*phi^{-gamma}*Gamma^AI]; matches eq. (10) = eq. (4)
- **Line 305** [VERBAL] OK — non-AI derivation is identical with Gamma^N replacing Gamma^AI; correct since the SDF is the same and only dividend growth differs
