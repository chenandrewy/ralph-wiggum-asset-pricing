# tests/factcheck-bysection.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 4m 37s
[ralph-garage/agent-logs/20260409T205235.726445-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T205235.726445-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong; two minor verbal imprecisions noted as warnings.

## Introduction (lines 38–70)

- **Line 38** — section header
- **Line 40** [VERBAL] OK — NASDAQ outpacing S&P 500 since 2015 with gap widening since 2023; supported by Figure 1
- **Line 40** [VERBAL] OK — "advances in generative AI have accelerated expectations" is a widely accepted characterization
- **Line 44** [FIGURE/TABLE] OK — caption correctly describes NASDAQ as solid, S&P 500 as dashed, normalized to Jan 2015 = 100; confirmed against R code (lines 304–305, 285–288)
- **Line 44** [REFERENCE] OK — data sources (NASDAQ from FRED, S&P 500 from Shiller dataset) match R code (lines 257, 266)
- **Line 49** [VERBAL] OK — hedging motive and market incompleteness claims are supported by the model (Proposition 1, Section 2.2)
- **Line 49** [VERBAL] OK — "much of this capital is private" is consistent with the GKP2012 framework
- **Line 51** [REFERENCE] OK — GKP2012 attribution for displacement risk under incomplete markets is accurate
- **Line 51** [VERBAL] OK — "rents from new technologies accrue to agents that current investors cannot trade with" is a standard characterization of GKP2012
- **Line 51** [VERBAL] OK — "closed-form price-dividend ratios" confirmed in Proposition 1 and Appendix A
- **Line 51** [ARITHMETIC] OK — "roughly six times" supported by table maximum ratio of 5.8 at p=1.0%, xi=0%
- **Line 51** [REFERENCE] OK — Jones2024 citation for extinction risk is correct (bib entry confirmed)
- **Line 51** [VERBAL] OK — "attenuates this gap" confirmed by table: higher xi reduces AI/Non-AI ratio
- **Line 53** [VERBAL] OK — veto result supported by Proposition 3 in Section 4.1
- **Line 55** [VERBAL] OK — transfer effectiveness under explosive growth supported by Section 4.2 analysis
- **Line 55** [REFERENCE] OK — GKP2012 and Jones2024 citations are accurate
- **Line 57** [VERBAL] OK — AI production claims about the paper are internally consistent with footnote
- **Line 62** [REFERENCE] OK — GKP2012 described accurately as general-equilibrium model with displacement risk
- **Line 64** [REFERENCE] OK — Jones2024 described accurately re: bounded utility and extinction risk trade-off
- **Line 64** [VERBAL] OK — "attenuating rather than amplifying" confirmed by table (higher xi reduces ratio)
- **Line 66** [REFERENCE] OK — KoganPapanikolaou2014 (JF), KoganPapanikolaouSeruStoffman2020 (JPE), Knesl2023 (JFE), Barro2006 (QJE), Wachter2013 (JF), PastorVeronesi2009 (AER) all confirmed in bib
- **Line 66** [VERBAL] OK — characterizations of all cited papers are accurate

## Model (lines 71–174)

- **Line 71** — section header
- **Line 73** — subsection header
- **Line 75** [DEFINITION] OK — discrete infinite-horizon model, representative household, AI owners with private capital
- **Line 75** [REFERENCE] OK — GKP2012 analogy for AI owners as future capital owners; disclaimer that entry is not modeled
- **Line 78** [ASSUMPTION] OK — aggregate consumption grows at rate g > 0 absent singularity
- **Line 80–82** [DEFINITION] OK — $C_{t+1} = (1+g)C_t$ correctly stated
- **Line 84** [DEFINITION] OK — household gets $\alpha_t C_t$, AI owners get $(1-\alpha_t)C_t$
- **Line 87** [ASSUMPTION] OK — singularity with probability p; with prob 1-p, alpha unchanged
- **Line 90–91** [ASSUMPTION] OK — non-extinction singularity: consumption jumps by $(1+\eta)$, share drops to $\phi\alpha_t$
- **Line 94** [VERBAL] OK — "smaller phi means larger displacement" is correct
- **Line 95** [ASSUMPTION/REFERENCE] OK — extinction: $C_{t+1}=0$; Jones2024 citation accurate
- **Line 98** [VERBAL] OK — singularities can recur; consistent with model structure
- **Line 104–106** [DEFINITION] OK — AI dividends $\theta_t C_t$, non-AI dividends $(1-\theta_t)C_t$; share dynamics correct
- **Line 108** [VERBAL] OK — private AI capital is the source of market incompleteness
- **Line 111–115** [DEFINITION] OK — CRRA preferences with $\gamma > 1$, $\beta \in (0,1)$
- **Line 119** [VERBAL] OK — SDF reflects household's own consumption growth due to incomplete markets
- **Line 121–132** [ARITHMETIC] OK — P/D ratio formulas verified; $\Gamma^{AI} = 3.2$, $\Gamma^N = 1.2$ with baseline parameters
- **Line 132** [ARITHMETIC] OK — $\Gamma^{AI} = \frac{\theta + \Delta\theta(1-\theta)}{\theta}(1+\eta)$ and $\Gamma^N = \frac{1-\theta-\Delta\theta(1-\theta)}{1-\theta}(1+\eta)$ verified
- **Line 136** [REFERENCE] OK — Appendix A proof exists and is valid
- **Line 139–144** [VERBAL] OK — existence condition $A^j < 1$ is correct for positive finite P/D; reference to Section 4.2 confirmed
- **Line 147** [ARITHMETIC] OK — $\Gamma^{AI} = 3.2 > 1.5 = 1+\eta$ confirmed; $\Gamma^N = 1.2 < 1.5$ confirmed
- **Line 147** [ARITHMETIC] OK — $\phi(1+\eta) = 0.75 < 1$ confirmed
- **Line 147** [VERBAL] OK — hedging channel explanation: AI stocks pay off when household consumption falls
- **Line 152** [VERBAL] OK — comp static (i): spread increasing in displacement severity (decreasing phi); proof logic correct
- **Line 153** [VERBAL] OK — comp static (ii): spread increasing in p for gamma sufficiently large; proof logic correct
- **Line 154** [VERBAL] OK — comp static (iii): spread and ratio decrease in xi; proof logic correct
- **Line 159** [VERBAL] OK — proof of (i): phi^{-gamma} increases as phi decreases, amplifying singularity term more for AI stocks
- **Line 161** [VERBAL] OK — proof of (ii): more weight on singularity states where AI pays off more
- **Line 163** [VERBAL] OK — proof of (iii): higher xi shrinks weight on non-extinction states where divergence occurs
- **Line 168** [REFERENCE] OK — GKP2012 parallel correctly described; distinction (continuous vs. discrete displacement) accurate
- **Line 170** [VERBAL] OK — if household could trade private AI capital, spread would collapse; accurate characterization of GKP2012

## Quantitative Analysis (lines 175–192)

- **Line 175** — section header
- **Line 184** [ASSUMPTION] OK — all parameter values ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$) match table footnote and R code
- **Line 184** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; household consumption falls by 25%
- **Line 184** [VERBAL] OK — parameter descriptions accurate ("50% increase," "15% of the economy," "20% of non-AI remainder")
- **Line 186** [ARITHMETIC] WARNING — "AI stocks trade at a P/D of roughly 18" for p=0.5%, xi=0%; table value is 17.5. Independent recomputation confirms 17.47. "Roughly 18" overstates by ~3%; not materially wrong but imprecise
- **Line 186** [ARITHMETIC] OK — "non-AI stocks trade near 11"; table says 11.1
- **Line 186** [ARITHMETIC] OK — "a ratio of about 1.6"; table says 1.6
- **Line 186** [ARITHMETIC] OK — "At p=1%, the ratio rises to nearly 6 to 1"; table shows 5.8 at p=1%, xi=0%
- **Line 186** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium" confirmed across all xi columns
- **Line 186** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium" confirmed in table
- **Line 188** [ARITHMETIC] OK — "1.5 to 6 times higher" for p in 0.5–1% range is supported (ratios span 1.4–5.8)
- **Line 188** [VERBAL] WARNING — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015"; figure shows NASDAQ ~500 vs S&P ~340 at latest data point, a relative premium closer to ~47% (500/340 ≈ 1.47). The claim is defensible but the absolute gap in appreciation (~400% vs ~240%) is much larger than 50 percentage points. The "50% more" phrasing is ambiguous but not materially wrong as a ratio statement

## Extensions: Market Incompleteness and the Singularity (lines 193–255)

- **Line 193** — section header
- **Line 195** [VERBAL] OK — accurate summary of section purpose
- **Line 199** [DEFINITION] OK — positive singularity: $\alpha_{t+1} = \min(1, \alpha_t/\phi)$ increases household share since $\phi < 1$
- **Line 199** [VERBAL] OK — "positive singularity is the more likely outcome" and "AI development is socially efficient" are modeling assumptions
- **Line 201** [ARITHMETIC] OK — CRRA utility is negative for all $c > 0$ when $\gamma > 1$: $c^{1-\gamma}/(1-\gamma)$, numerator positive, denominator negative
- **Line 201** [REFERENCE] OK — Jones2024 normalization of extinction utility to zero
- **Line 211** [VERBAL] OK — proof of veto (i): with gamma large, concavity makes downside dominate even though positive singularity is more likely
- **Line 213** [VERBAL] OK — proof of veto (ii): complete markets allow hedging, household reflects social surplus
- **Line 216** [VERBAL] OK — extinction risk interaction correctly described
- **Line 220** [REFERENCE] OK — GKP2012 on intergenerational transfers
- **Line 222–228** [ARITHMETIC] OK — transfer consumption formula verified algebraically; consistent with R code
- **Line 230** [ARITHMETIC] OK — $\phi_{\text{eff}} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$ verified by factoring eq (5)
- **Line 234–236** [ARITHMETIC] OK — transfer ratio $= 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$ verified; independent of $\eta$ confirmed
- **Line 238** [VERBAL] OK — "exceeds one whenever $\tau > 0$" holds since $1-\delta\tau > 0$ for $\tau < 1/\delta = 2$ and $\tau \in [0,1)$
- **Line 240** [ARITHMETIC] OK — large singularity: $\phi(1+\eta) = 0.05 \times 10 = 0.5$ (consumption halves)
- **Line 240** [ARITHMETIC] OK — baseline: $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$ (falls by 25%)
- **Line 240** [ASSUMPTION] OK — parameters ($\alpha=0.70$, $p=0.5\%$, $\xi=5\%$) match R code
- **Line 242** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$
- **Line 242** [VERBAL] OK — existence condition violated at $\tau=0$ for large singularity; consistent with R code returning NA
- **Line 246** [ASSUMPTION] OK — caption parameters ($\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$) match R code
- **Line 251** [REFERENCE] OK — Jones2024 and Nordhaus2021 both in references.bib

## Conclusion (lines 256–266)

- **Line 256** — section header
- **Line 258** [VERBAL] OK — "AI stocks trade at high valuations" supported by Figure 1 and Table 1
- **Line 258** [VERBAL] OK — "hedging motive" supported by Proposition 1 and discussion at line 147
- **Line 258** [VERBAL] OK — "requires market incompleteness" supported by lines 108, 170, and Proposition 3(ii)
- **Line 258** [VERBAL] OK — "attenuated by extinction risk" supported by Proposition 2(iii) and table
- **Line 258** [VERBAL] OK — "risk-averse households may inefficiently block AI development" supported by Proposition 3(i)
- **Line 258** [VERBAL] OK — "government transfers...can become effective" supported by Section 4.2
- **Line 260** [VERBAL] OK — limitations ("continuous-time dynamics, heterogeneous beliefs, production-side details") are indeed absent from the model

## Proof of Proposition 1 (lines 267–296)

- **Line 267** — appendix header
- **Line 269–272** [DEFINITION] OK — standard Euler equation for CRRA preferences
- **Line 275** [VERBAL] OK — P/D ratio constant in pre-singularity stationary equilibrium; correct since singularity is i.i.d.
- **Line 278** [ARITHMETIC] OK — no singularity: $c_{t+1}^H/c_t^H = 1+g$ and $D_{t+1}^{AI}/D_t^{AI} = 1+g$; verified
- **Line 279** [ARITHMETIC] OK — non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$ and $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$; verified
- **Line 280** [ARITHMETIC] OK — extinction: payoff is zero; standard treatment
- **Line 284–287** [ARITHMETIC] OK — Euler equation expansion verified algebraically; all terms match
- **Line 289** [VERBAL] OK — approximation (post-singularity P/D ≈ $v^{AI}$) is properly flagged and justified
- **Line 291–293** [ARITHMETIC] OK — solving $v = A(v+1)$ yields $v = A/(1-A)$; matches equation (5) exactly
- **Line 295** [VERBAL] OK — non-AI derivation is identical with $\Gamma^N$ replacing $\Gamma^{AI}$
