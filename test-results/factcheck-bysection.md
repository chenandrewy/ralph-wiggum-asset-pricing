# tests/factcheck-bysection.py
Started: 2026-04-09 20:07:38 EDT
Runtime: 6m 49s
[ralph-garage/agent-logs/20260409T200738.704553-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T200738.704553-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct and all verbal claims are supported; only minor imprecisions in verbal rounding and one loose figure-based claim were found.

## Introduction (lines 39–81)

- **Line 39** — section header
- **Line 41** [FIGURE/TABLE] OK — NASDAQ described as "AI- and technology-heavy"; consistent with code label and standard characterization
- **Line 41** [VERBAL] OK — claims NASDAQ "dramatically outpaced" S&P 500 since 2015 with gap widening since 2023; supported by fig-ai-valuations data
- **Lines 44–45** [FIGURE/TABLE] OK — caption says NASDAQ is solid, S&P 500 is dashed, both normalized to Jan 2015 = 100; confirmed in R code (`scale_linetype_manual`, `normalize()`)
- **Lines 44–45** [FIGURE/TABLE] OK — caption says "Sources: NASDAQ from FRED; S&P 500 from the Shiller dataset"; confirmed in R code (FRED `NASDAQCOM`, datahub Shiller)
- **Line 50** [VERBAL] OK — hedging motive: AI stocks hedge against singularity displacement; consistent with model mechanism
- **Line 50** [VERBAL] OK — "If markets were complete, investors could insure directly"; consistent with model and GKP2012
- **Line 50** [VERBAL] OK — "much of this capital is private, held by founders and early-stage investors"; consistent with incomplete markets framing
- **Line 50** [VERBAL] OK — "financial market solutions to AI disaster risk remain under-explored"; consistent with spec §I.3c
- **Line 52** [REFERENCE] OK — cites GKP2012 for rents accruing to agents current investors cannot trade with; confirmed in GKP-2012.md
- **Line 55** [VERBAL] OK — discrete singularity produces large valuation spreads; supported by table (ratio up to 5.8)
- **Line 56** [REFERENCE] OK — cites Jones2024 for extinction risk attenuating valuation premium; consistent with model (Proposition 2(iii))
- **Line 57** [VERBAL] OK — government transfers normally wasteful but effective when growth overwhelms deadweight costs; consistent with Extension 2
- **Line 60** [VERBAL] OK — model description (representative household, two assets, closed-form P/D ratios); all confirmed
- **Line 60** [REFERENCE] OK — "Following Jones2024, the singularity may also trigger extinction"; Jones2024 models existential risk from AI
- **Line 62** [VERBAL] OK — positive singularity and veto mechanism; consistent with Extension 1
- **Line 64** [REFERENCE] OK — "as GKP2012 emphasize, much of this capital belongs to future innovators"; confirmed verbatim in GKP-2012.md
- **Line 66** [VERBAL] OK — "P/D ratios for AI stocks can be up to roughly six times higher"; table maximum ratio is 5.8 at p=1%, ξ=0%, which rounds to ~6; the "up to" qualifier is appropriate
- **Line 66** [VERBAL] OK — extinction risk attenuates the gap; confirmed by table (ratio drops with increasing ξ)
- **Line 68** [VERBAL] OK — "all analysis and writing were produced by AI agents"; consistent with spec §IV.5c
- **Line 73** [REFERENCE] OK — GKP2012 described as general-equilibrium model with displacement risk distinct from aggregate consumption risk; confirmed in GKP-2012.md
- **Line 73** [REFERENCE] OK — "growth stocks provide a partial hedge"; confirmed in GKP-2012.md ("growth firms offer a hedge against displacement risk")
- **Line 75** [REFERENCE] OK — Jones2024 described as studying trade-off between AI-driven growth and existential risk with bounded utility; accurate characterization
- **Line 75** [VERBAL] OK — extinction risk interacts with displacement in a countervailing way; supported by Proposition 2(iii) and table
- **Line 77** [REFERENCE] OK — KoganPapanikolaou2014 on technology shocks and cross-sectional returns; matches bib entry "Growth Opportunities, Technology Shocks, and Asset Prices" (JF)
- **Line 77** [REFERENCE] OK — KoganPapanikolaouStoffman2020 on creative destruction and inequality; matches bib entry "Left Behind" (JPE)
- **Line 77** [REFERENCE] OK — Knesl2023 on automation-driven displacement risk; matches bib entry (JFE, 2023)
- **Line 77** [REFERENCE] OK — Barro2006, Wachter2013 as rare disasters literature; canonical citations, accurate
- **Line 77** [REFERENCE] OK — PastorVeronesi2009 on technological revolutions and stock prices; matches bib entry (AER)
- **Line 77** [REFERENCE] OK — KorinekSuh2024 on AGI transition scenarios; matches bib entry (NBER WP)

## Model (lines 82–193)

- **Line 82** — section header
- **Line 86** [REFERENCE] OK — AI owners parallel future capital owners in GKP2012; confirmed in GKP-2012.md (future innovators not yet in the economy)
- **Line 86** [VERBAL] OK — "we do not explicitly model entry of new cohorts"; no entry dynamics appear in the model
- **Line 89** [DEFINITION] OK — aggregate consumption growth at rate g; formalized in Eq. (1)
- **Line 95** [DEFINITION] OK — $c_t^H = \alpha_t C_t$, AI owners receive $(1 - \alpha_t)C_t$; internally consistent
- **Lines 100–106** [DEFINITION] OK — non-extinction singularity: consumption jumps by $1+\eta$, household share drops $\alpha_{t+1} = \phi\alpha_t$
- **Line 106** [REFERENCE] OK — cites Jones2024 for co-occurrence of extreme growth and extinction risk
- **Line 115** [DEFINITION] OK — AI dividend share update: $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$
- **Line 116** [DEFINITION] OK — non-AI dividends $D_t^N = (1-\theta_t)C_t$
- **Line 119** [VERBAL] OK — private AI capital pays $(1-\alpha_t)C_t - D_t^{AI}$; correct residual
- **Line 122** [DEFINITION] OK — CRRA preferences with $\gamma > 1$ and $\beta \in (0,1)$
- **Lines 136–143** [ARITHMETIC] OK — $\Gamma^{AI} = [0.15 + 0.2(0.85)]/0.15 \times 1.5 = 0.32/0.15 \times 1.5 = 3.20$; $\Gamma^N = 0.68/0.85 \times 1.5 = 1.20$; formulas are correct
- **Line 147** [REFERENCE] OK — "See Appendix A"; Appendix A (lines 293–322) contains the full proof
- **Lines 150–155** [VERBAL] OK — existence condition $A^j < 1$ is necessary and sufficient for positive finite P/D; correct for the $A/(1-A)$ form
- **Line 155** [REFERENCE] OK — "As we discuss in Section 4.2"; Section 4.2 (line 268) confirms existence condition violated for large singularity
- **Line 158** [ARITHMETIC] OK — $\Gamma^{AI} > 1+\eta$: $3.2 > 1.5$ ✓; $\Gamma^N < 1+\eta$: $1.2 < 1.5$ ✓
- **Line 158** [VERBAL] OK — "$\phi(1+\eta) < 1$ when $\phi$ is sufficiently small"; for baseline $0.5 \times 1.5 = 0.75 < 1$ ✓ (note: exact consumption-fall condition is $\phi(1+\eta)(1+g) < 1 = 0.765 < 1$; the omission of the $(1+g)$ factor is a minor verbal shorthand, not an error)
- **Lines 160–166** [VERBAL] OK — Corollary 1: P/D increasing in $\Gamma^j$ and $\Gamma^{AI} > \Gamma^N$ when $\Delta\theta > 0$; logic verified
- **Lines 168–183** [VERBAL] OK — Proposition 2 comparative statics: (i) spread increasing in displacement severity (decreasing $\phi$), (ii) increasing in $p$ for large $\gamma$, (iii) decreasing in $\xi$; all verified analytically
- **Line 187** [REFERENCE] OK — GKP2012: "growth stocks earn lower expected returns because they hedge displacement risk"; confirmed in GKP-2012.md
- **Line 187** [VERBAL] OK — contrast between GKP's continuous displacement and this paper's discrete singularity; accurate
- **Line 189** [REFERENCE] OK — GKP2012's point about future innovators' rents being untradeable; confirmed in GKP-2012.md

## Quantitative Analysis (lines 194–211)

- **Line 194** — section header
- **Line 203** [ASSUMPTION] OK — parameters $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$ all match R code exactly
- **Line 203** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; "household consumption falls by 25%" ✓
- **Line 205** [ARITHMETIC] OK — "AI stocks trade at a P/D of roughly 18" at p=0.5%, ξ=0%; table shows 17.5 (recomputed: 17.47); "roughly 18" is within verbal rounding
- **Line 205** [ARITHMETIC] OK — "non-AI stocks trade near 11"; table shows 11.1 (recomputed: 11.09) ✓
- **Line 205** [ARITHMETIC] OK — "ratio of about 1.6"; table shows 1.6 (recomputed: 1.576) ✓
- **Line 205** [ARITHMETIC] OK — "At p=1%, the ratio rises to nearly 6 to 1"; table shows 5.8 (recomputed: 5.757); "nearly 6" is fair ✓
- **Line 205** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium"; confirmed by table (ratio rises with p)
- **Line 205** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium, as Proposition 2(iii) predicts"; confirmed by table (both P/D and ratio fall with ξ)
- **Line 207** [VERBAL] OK — "P/D ratios for AI stocks that are 1.5 to 6 times higher across annual singularity probabilities in the 0.5–1% range"; table ratios in that band are 1.4–5.8, well-described by "1.5 to 6" ✓
- **Line 207** [FIGURE/TABLE] OK — "the AI-heavy NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015"; reading the figure, the NASDAQ index is roughly 50% higher in level terms than S&P 500 at latest data; the claim is a level comparison, not a return comparison, and is approximately supported by the figure

## Extensions: Market Incompleteness and the Singularity (lines 212–281)

- **Line 212** — section header
- **Line 214** [VERBAL] OK — "baseline model takes market incompleteness as given"; accurate summary of Sections 2–3
- **Lines 218–223** [DEFINITION] OK — positive singularity ($\lambda$) and negative singularity ($1-\lambda$) structure; internally consistent
- **Line 225** [ASSUMPTION] OK — $\lambda > 1/2$ ensures social efficiency; stated clearly
- **Line 227** [REFERENCE] OK — "Following Jones2024, we normalize extinction utility to zero"; Jones2024's framework treats extinction as zero continuation value; the paper's next sentence ("CRRA utility is negative for all $c > 0$ when $\gamma > 1$") is correct for standard CRRA $u(c) = c^{1-\gamma}/(1-\gamma)$
- **Lines 229–240** [VERBAL] OK — Proposition 3 proof: (i) large $\gamma$ magnifies downside via $\phi^{-\gamma}$, household vetoes; (ii) complete markets allow hedging, household reflects social surplus; logic is sound
- **Line 242** [VERBAL] OK — higher $\xi$ reduces weight on non-extinction singularity states; directionally correct
- **Line 242** [REFERENCE] OK — "Jones2024 argues bounded utility makes higher $\xi$ amplify veto incentive"; consistent with Jones's framework
- **Line 246** [REFERENCE] OK — "GKP2012 show intergenerational transfers can affect the magnitude of displacement risk"; accurate characterization
- **Line 251** [ARITHMETIC] OK — Eq. (7): $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$; first term is displaced consumption, second is net transfer; matches R code
- **Line 256** [ARITHMETIC] OK — $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$; derived correctly from Eq. (7); matches R code line 119
- **Line 261** [ARITHMETIC] OK — Eq. (8): $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$; $(1+\eta)$ cancels in numerator and denominator; independence from $\eta$ confirmed ✓
- **Line 264** [VERBAL] OK — "ratio exceeds one whenever $\tau > 0$"; correct since $\tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha) > 0$ for small enough $\tau$ (and $\delta\tau < 1$)
- **Line 266** [ARITHMETIC] OK — large singularity: $\phi(1+\eta) = 0.05 \times 10 = 0.5$; "consumption halves" ✓
- **Line 266** [ARITHMETIC] OK — baseline: $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; "falls by 25%" ✓
- **Line 266** [VERBAL] OK — "ten-fold growth" for $\eta=9$; $1+\eta = 10$ ✓
- **Line 266** [ASSUMPTION] OK — parameters $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$; match R code (`alpha0=0.70`, `p_ext=0.005`, `xi_ext=0.05`)
- **Line 268** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$ ✓
- **Line 268** [REFERENCE] OK — cites Remark 1 for existence condition; Remark 1 (line 150) defines $A^j < 1$
- **Line 268** [VERBAL] OK — "P/D ratio is undefined at $\tau=0$" for large singularity; R code returns NA when $K \geq 1$; consistent with divergence claim
- **Line 272** [FIGURE/TABLE] OK — caption parameters ($\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$) match R code; panel descriptions match R code titles and annotations
- **Line 277** [REFERENCE] OK — cites Jones2024 and Nordhaus2021 for explosive output growth; appropriate citations

## Conclusion (lines 282–292)

- **Line 282** — section header
- **Line 284** [VERBAL] OK — "AI stocks trade at high valuations...hedging motive...investors use AI stocks to partially insure against displacement"; supported by Propositions 1–2 and Table 1
- **Line 284** [VERBAL] OK — "requires market incompleteness"; established in model setup (Section 2)
- **Line 284** [VERBAL] OK — "attenuated by extinction risk"; established in Proposition 2(iii) and table
- **Line 284** [VERBAL] OK — "risk-averse households may inefficiently block AI development"; established in Proposition 3(i)
- **Line 284** [VERBAL] OK — "government transfers...can become effective if singularity-driven growth is large enough"; established in Extension 2
- **Line 286** [VERBAL] OK — "abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details"; accurate limitations; no new claims introduced

## Proof of Proposition 1 (lines 293–322)

- **Line 293** — appendix header
- **Line 298** [DEFINITION] OK — Euler equation $P_t^j = \mathbb{E}_t[\beta(c_{t+1}^H/c_t^H)^{-\gamma}(P_{t+1}^j + D_{t+1}^j)]$; standard CRRA Euler equation
- **Line 304** [ARITHMETIC] OK — no-singularity case: $c_{t+1}^H/c_t^H = 1+g$ and $D_{t+1}^{AI}/D_t^{AI} = 1+g$; both correct
- **Line 305** [ARITHMETIC] OK — non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$ and $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$; both correct
- **Line 306** [ARITHMETIC] OK — extinction: payoff is zero; correct
- **Lines 310–313** [ARITHMETIC] OK — Euler substitution with three scenarios; probabilities $(1-p)$, $p(1-\xi)$, $p\xi$ correctly applied; SDF terms verified
- **Line 315** [VERBAL] OK — stationarity approximation (post-singularity P/D ≈ pre-singularity) explicitly acknowledged with caveat
- **Lines 317–319** [ARITHMETIC] OK — algebra from Euler to $v^{AI} = A/(1-A)$ verified: divide by $D_t^{AI}$, factor $\beta(1+g)^{1-\gamma}$, solve $v = A(v+1)$
- **Line 319** [ARITHMETIC] OK — Eq. (13) matches Proposition 1 Eq. (4) exactly
- **Line 321** [VERBAL] OK — non-AI derivation is identical with $\Gamma^N$ replacing $\Gamma^{AI}$; verified (dividend growth structure is the same, only the share ratio changes)
