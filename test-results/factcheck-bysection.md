# tests/factcheck-bysection.py
Started: 2026-04-11 16:10:24 EDT
Runtime: 6m 30s
[ralph-garage/agent-logs/20260411T161024.922705-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260411T161024.922705-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic, verbal claims, references, and formulas verified correct across all sections with no material errors.

## Introduction (lines 38–72)
- **Line 38** — section header
- **Line 40** [VERBAL] OK — Claims S&P 500 P/D has reached historically elevated levels and NASDAQ has outpaced the broader market since 2015; consistent with Figure 1 and well-known market data
- **Line 44** [FIGURE/TABLE] OK — Caption correctly describes Panel (a) as S&P 500 trailing P/D from Shiller dataset and Panel (b) as NASDAQ/S&P 500 price relative normalized to Jan 2015 = 100; sources correctly identified; figure file exists
- **Line 49** [REFERENCE] OK — GKP2012 reference: "displacing capital often belongs to future innovators who have not yet entered the economy" is consistent with GKP2012's core mechanism as described in the Discussion section (line 171)
- **Line 49** [VERBAL] OK — Definition of negative AI singularity as "sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption" matches model setup (lines 88–98)
- **Line 51** [VERBAL] OK — "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks" is appropriately hedged; table confirms ratio = 2.0 at p=1%, xi=0%
- **Line 51** [ARITHMETIC] OK — "ratio of about 1.4" at p=0.5%: table row p=0.5%, xi=0% shows Ratio=1.4 (exact: 15.5/11.1=1.396)
- **Line 51** [ARITHMETIC] OK — "ratio rises to 2" at p=1%: table row p=1.0%, xi=0% shows Ratio=2.0 (exact: 26.5/13.3=1.992)
- **Line 53** [REFERENCE] OK — "Proposition 2 quantifies this attenuation" correctly references prop:comp-statics (line 159), which states the valuation spread is decreasing in xi
- **Line 53** [VERBAL] OK — "Under complete markets the displacement-driven premium would largely vanish" is supported by Discussion (line 171) with appropriate residual-spread caveat
- **Line 53** [VERBAL] OK — Extinction risk "attenuates the hedging channel" matches Proposition 2 and the model mechanism
- **Line 55** [REFERENCE] OK — Proposition 3 reference: "calls to slow or halt AI development may partly reflect investors' inability to hedge" matches Proposition 3(i) at line 210
- **Line 55** [VERBAL] OK — "Complete markets would eliminate this distortion entirely" matches Proposition 3(ii)
- **Line 57** [REFERENCE] OK — Jones2024 reference for explosive output growth and redistribution is consistent with Section 4.2
- **Line 57** [VERBAL] OK — "even grossly inefficient government transfers become effective" matches Extension 2 results
- **Line 59** [REFERENCE] OK — All section cross-references (sec:model, sec:quant, sec:extensions, sec:conclusion) point to correct labeled sections
- **Line 64** [VERBAL] OK — GKP2012 lit review characterization is accurate
- **Line 66** [VERBAL] OK — Jones2024 characterization and "attenuates rather than amplifies" matches Proposition 2
- **Line 68** [VERBAL] OK — Literature citations are standard attributions with no specific contested claims

## Model (lines 73–177)
- **Line 73** — section header
- **Line 77** [DEFINITION] OK — Household as marginal investor, AI owners as non-marginal, static group. Consistent with model structure
- **Line 80** [DEFINITION] OK — Consumption growth at constant rate g > 0 absent singularity
- **Line 83** [DEFINITION] OK — Equation (1): $C_{t+1} = (1+g)C_t$
- **Line 86** [DEFINITION] OK — $c_t^H = \alpha_t C_t$, AI owners get $(1-\alpha_t)C_t$; sums to $C_t$
- **Line 89** [ASSUMPTION] OK — Singularity probability p per period; alpha unchanged absent singularity
- **Line 92–95** [DEFINITION] OK — Non-extinction singularity: $\alpha_{t+1} = \phi\alpha_t$, aggregate jumps by $(1+\eta)$
- **Line 97** [DEFINITION/REFERENCE] OK — Extinction: $C_{t+1}=0$; Jones2024 cited for the rationale
- **Line 100** [VERBAL] OK — Repeated singularities progressively displace household; consistent with $\alpha_{t+k} = \phi^k\alpha_t$
- **Line 106** [DEFINITION] OK — AI dividend share dynamics: $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$; keeps $\theta\in(0,1)$
- **Line 107** [DEFINITION] OK — Non-AI dividends $D_t^N = (1-\theta_t)C_t$
- **Line 110** [ARITHMETIC] OK — $D^{AI}+D^N = \theta_t C_t + (1-\theta_t)C_t = C_t$
- **Line 112** [VERBAL] OK — Restricted equity as source of market incompleteness
- **Line 114** [VERBAL] OK — Role of phi in displacement; hedging channel inflates AI valuations but does not eliminate displacement
- **Line 117** [DEFINITION] OK — CRRA preferences with $\gamma > 1$, $\beta\in(0,1)$
- **Line 120** [DEFINITION] OK — Equation (3): standard CRRA utility
- **Line 125** [VERBAL] OK — SDF reflects household's own consumption growth under incomplete markets
- **Lines 130–136** [ARITHMETIC] OK — P/D formulas verified algebraically from Euler equation in Appendix; $v = A/(1-A)$ follows from $v = A(v+1)$
- **Line 138** [ARITHMETIC] OK — $\Gamma^{AI} = (0.15+0.2\times0.85)/0.15\times1.5 = 3.20$; $\Gamma^{N} = (1-0.2)\times1.5 = 1.20$
- **Line 146–150** [VERBAL/ARITHMETIC] OK — Remark 1: existence requires $A^j < 1$; verified numerically for all table parameterizations (max $A^{AI} = 0.987$ at p=1%, xi=0%)
- **Line 153** [VERBAL] OK — Closed-form approximation treats post-singularity P/D as equal to pre-singularity; exact when $\Delta\theta\to0$; table reports numerically exact values via backward recursion
- **Line 155** [ARITHMETIC] OK — $\Gamma^{AI} = 3.20 > 1+\eta = 1.50$ and $\Gamma^{N} = 1.20 < 1.50$; $\phi(1+\eta) = 0.75 < 1$
- **Line 157** [VERBAL] OK — Spread widens with decreasing phi (via $\phi^{-\gamma}$) and increasing p; verified from table
- **Lines 159–161** [VERBAL] OK — Proposition 2: valuation spread decreasing in xi; ratio also decreasing in xi; verified numerically for all table rows
- **Lines 163–165** [ARITHMETIC] OK — Proof of Proposition 2: decomposition $A^j = B[(1-p)+p(1-\xi)S\Gamma^j]$ is correct; $\Gamma^{AI}>\Gamma^{N}$ implies larger absolute reduction in $A^{AI}$; $f(A)=A/(1-A)$ has $f''(A)=2/(1-A)^3>0$; condition $A^j>1/2$ (equivalently P/D>1) verified for all table entries (minimum P/D is 9.7)
- **Line 169** [VERBAL/REFERENCE] OK — GKP2012 comparison: continuous displacement from technological variety vs. discrete AI singularity; accurate characterization
- **Line 171** [VERBAL] OK — Complete markets: $\phi_\text{eff}\to1$ collapses premium; residual spread from $\Gamma^{AI}\neq\Gamma^{N}$ acknowledged
- **Line 173** [VERBAL] OK — Extreme displacement can violate existence condition; correct that $\phi\to0$ sends $\phi^{-\gamma}\to\infty$ and $A^j\to\infty>1$

## Quantitative Analysis (lines 178–195)
- **Line 178** — section header
- **Lines 180–185** [FIGURE/TABLE] OK — Table inclusion references correct file; table footnote parameters match text
- **Line 187** [ASSUMPTION] OK — All seven parameters ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$) match R code (generate-exhibits.R lines 18–24) exactly
- **Line 187** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5\times1.5 = 0.75$; household consumption falls by 25% ($1-0.75=0.25$)
- **Line 187** [ARITHMETIC] OK — $\eta=0.5$ means aggregate consumption rises by 50%
- **Line 187** [VERBAL] OK — "AI stocks are initially 15% of the economy" matches $\theta=0.15$; "AI's share jumps by 20% of the non-AI remainder" matches $\Delta\theta=0.2$
- **Line 189** [ARITHMETIC] OK — "P/D of about 15.5" matches table (p=0.5%, xi=0%: AI=15.5)
- **Line 189** [ARITHMETIC] OK — "non-AI stocks trade near 11" matches table value 11.1
- **Line 189** [ARITHMETIC] OK — "ratio of about 1.4" matches table Ratio=1.4
- **Line 189** [ARITHMETIC] OK — "At p=1%, the ratio rises to 2" matches table Ratio=2.0 at p=1.0%, xi=0%
- **Line 189** [VERBAL] OK — "extinction risk compresses the AI premium" verified: ratio decreases monotonically in xi for every p value in the table
- **Line 189** [REFERENCE] OK — "as Proposition 2 predicts" correctly references prop:comp-statics
- **Line 191** [VERBAL] OK — "AI stock P/D ratios are 1.3 to 2 times" across p=0.5–1%: verified from table (ratios range 1.3–2.0 in that range)
- **Line 191** [VERBAL] OK — "NASDAQ has appreciated roughly 50% more than S&P 500 since 2015" is an empirical claim from downloaded data, appropriately qualified with "roughly" and caveated in the surrounding text

## Extensions: Market Incompleteness and the Singularity (lines 196–280)
- **Line 196** — section header
- **Line 198** [VERBAL] OK — Accurate summary of the two extensions
- **Line 202** [DEFINITION] OK — Positive singularity: $\alpha_{t+1} = \min(1, \alpha_t/\phi)$; with $\alpha=0.70$, $\phi=0.5$: $\alpha^+=\min(1,1.40)=1.00$; $q>1/2$ assumed
- **Line 204** [VERBAL] OK — Kaldor-Hicks efficiency: total surplus positive when $(1+\eta)>1$ since aggregate consumption rises by $1+\eta$ regardless of distribution; correct
- **Line 206** [VERBAL] OK — CRRA utility is negative for $c>0$ when $\gamma>1$; extinction utility = 0 is conservative for the veto
- **Line 208** [ARITHMETIC] OK — Complete markets consumption = $\alpha(1+\eta)C_t(1+g)$; consistent with R code
- **Lines 210–215** [VERBAL] OK — Proposition 3 structure: (i) veto under incomplete markets for high gamma; (ii) no veto under complete markets
- **Line 221** [ARITHMETIC] OK — $\Delta u(\gamma)$ formula correctly specified
- **Line 224** [ARITHMETIC] OK — Limit argument: $\phi(1+\eta)=0.75<1$ ensures $\phi\alpha(1+\eta)=0.525<\alpha=0.70$; negative-singularity term dominates as $\gamma\to\infty$
- **Line 226** [ARITHMETIC] OK — Complete markets utility gain $u(\alpha(1+\eta))-u(\alpha)>0$ since $\eta>0$ and CRRA is increasing
- **Line 229** [ARITHMETIC] OK — Numerical example parameters ($\phi=0.5$, $\eta=0.5$, $\xi=5\%$, $p=1\%$, $\gamma=10$, $\alpha=0.70$, $q=0.70$, $\kappa=1\%$) all match R code exactly
- **Line 229** [ARITHMETIC] OK — Veto outcome verified: incomplete markets V_veto > V_develop; complete markets V_develop^CM > V_veto
- **Line 229** [VERBAL] OK — "positive singularity is more than twice as likely": $P(\text{pos})/P(\text{neg}) = 0.70/0.30 = 2.33$
- **Line 241–245** [ARITHMETIC] OK — Transfer consumption formula (eq. 8) correctly decomposes into displaced consumption plus net transfer
- **Line 247** [VERBAL] OK — $(1-\phi\alpha)$ is AI owners' share of post-singularity aggregate consumption; transfer levied on consumption allocation, not publicly traded dividends
- **Lines 249–253** [ARITHMETIC] OK — $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$ verified by dividing eq. (8) by $\alpha(1+\eta)(1+g)C_t$; matches R code line 152
- **Lines 257–261** [ARITHMETIC] OK — Transfer ratio $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$ verified algebraically; contains no $\eta$
- **Line 263** [VERBAL] OK — "independent of the productivity jump $\eta$" confirmed: formula has no $\eta$ term
- **Line 265** [ASSUMPTION] OK — Parameters match R code: $\gamma=4$, $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$; baseline $\eta=0.5$/$\phi=0.5$; large $\eta=9$/$\phi=0.05$
- **Line 265** [ARITHMETIC] OK — Large singularity: $\phi(1+\eta)=0.05\times10=0.50$ (consumption halves); baseline: $\phi(1+\eta)=0.75$ (25% fall)
- **Line 267** [ARITHMETIC] OK — $\phi^{-\gamma}=0.05^{-4}=160{,}000$
- **Line 267** [VERBAL] OK — P/D undefined at $\tau=0$ for large singularity: with $\phi_\text{eff}=0.05$, the existence condition is violated ($A>1$); transfers restore finite prices
- **Line 271** [ASSUMPTION] OK — $\delta=0.5$ in figure caption matches R code
- **Line 276** [REFERENCE] OK — Nordhaus2021 cited alongside Jones2024 for explosive output growth

## Conclusion (lines 281–291)
- **Line 281** — section header
- **Line 283** [VERBAL] OK — "hedging motive" supported by Proposition 1 and the hedging channel discussion (line 155)
- **Line 283** [VERBAL] OK — "requires market incompleteness" supported by Section 2.3 (line 171): $\phi_\text{eff}\to1$ collapses premium
- **Line 283** [VERBAL] OK — "attenuated by extinction risk" supported by Proposition 2
- **Line 283** [VERBAL] OK — "risk-averse households may inefficiently block AI development" supported by Proposition 3(i)
- **Line 283** [VERBAL] OK — "government transfers... can become effective if singularity-driven growth is large enough" supported by Extension 2 and Figure 3
- **Line 285** [VERBAL] OK — "abstracts from continuous-time dynamics" correct; model is discrete-time
- **Line 285** [VERBAL] OK — "heterogeneous beliefs" correctly identified as absent from the model
- **Line 285** [VERBAL] OK — "production-side details" correctly identified as abstracted away

## Proof of Proposition 1 (lines 292–323)
- **Line 292** — section header; correctly references prop:pd-ratios
- **Lines 294–298** [ARITHMETIC] OK — Euler equation $P_t^j = \mathbb{E}_t[\beta(c_{t+1}^H/c_t^H)^{-\gamma}(P_{t+1}^j+D_{t+1}^j)]$ is standard CRRA; consistent with preferences at line 120
- **Lines 302–306** [ARITHMETIC] OK — Three cases correctly enumerate probability-weighted states: no singularity ($1-p$, growth $1+g$), non-extinction singularity ($p(1-\xi)$, consumption growth $\phi(1+g)(1+\eta)$, dividend growth $\Gamma^{AI}(1+g)$), extinction ($p\xi$, payoff 0)
- **Lines 310–314** [ARITHMETIC] OK — Euler equation expansion verified: substitution of three cases into $v^{AI}D_t^{AI} = \mathbb{E}[\cdot]$ is algebraically correct; $[\phi(1+g)(1+\eta)]^{-\gamma}\cdot(1+g) = (1+g)^{1-\gamma}[\phi(1+\eta)]^{-\gamma}$
- **Line 316** [ARITHMETIC] OK — $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is theta-independent: $(1-\theta-\Delta\theta(1-\theta))/(1-\theta) = (1-\theta)(1-\Delta\theta)/(1-\theta) = 1-\Delta\theta$
- **Line 316** [VERBAL] OK — Post-singularity P/D approximation acknowledged; exact for non-AI (theta-independent Gamma^N); numerically exact values via backward recursion for AI
- **Lines 318–320** [ARITHMETIC] OK — Closed-form $v^{AI} = A/(1-A)$ with $A = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$ follows from solving $v=A(v+1)$; matches Proposition 1 (line 131)
- **Line 322** [VERBAL] OK — Non-AI derivation identical with $\Gamma^N$ replacing $\Gamma^{AI}$; SDF factor unchanged since it depends on household consumption, not dividends
