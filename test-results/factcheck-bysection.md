# tests/factcheck-bysection.py
Started: 2026-04-11 21:27:07 EDT
Runtime: 8m 30s
[ralph-garage/agent-logs/20260411T212707.780841-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260411T212707.780841-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong.

## Introduction (lines 38–70)
- **Line 38** — section header
- **Line 40** [VERBAL] OK — description of Figure 1 matches figure content (S&P 500 P/D at historically elevated levels; NASDAQ outpacing S&P since 2015, gap widening since 2023)
- **Line 49** [REFERENCE] OK — GKP2012 cited for the insight that displacing capital belongs to future innovators who cannot yet trade; accurate characterization of GKP's incomplete-markets point
- **Line 49** [VERBAL] OK — "investors turn to publicly traded AI stocks as the only available partial hedge" is the paper's own contribution, not attributed to GKP; framing is correct
- **Line 51** [ARITHMETIC] OK — "P/D ratios for AI stocks roughly double relative to non-AI stocks" at p=1%; table confirms AI=26.5, Non-AI=13.3, ratio=2.0
- **Line 51** [VERBAL] OK — "consistent with observed valuation spreads" is a qualitative hedge; Section 3 provides the empirical comparison
- **Line 51** [REFERENCE] OK — Proposition 2 correctly summarized as showing valuation spread narrows as extinction probability rises
- **Line 51** [REFERENCE] OK — Jones2024 cited for extinction channel; accurate
- **Line 53** [VERBAL] OK — complete-markets claim matches Section 2.3 (line 169): premium "largely collapses" with residual from differential dividend growth
- **Line 53** [REFERENCE] OK — Proposition 3 cross-reference accurate: risk-averse household vetoes under incomplete markets
- **Line 53** [VERBAL] OK — "when the positive singularity is more likely than the negative one, AI development is socially efficient" — efficiency requires eta>0 (line 202), and q>1/2 governs probability; introduction compresses but does not misstate
- **Line 55** [REFERENCE] OK — Jones2024 cited for explosive singularity growth; transfers mechanism is the paper's own contribution; attribution is correct
- **Line 57** [REFERENCE] OK — section roadmap cross-references all correct (Sec 2 at line 71, Sec 3 at line 176, Sec 4 at line 194, Sec 5 at line 279)
- **Line 57** [VERBAL] OK — footnote about AI agents producing all analysis and writing; consistent with spec requirement
- **Line 62** [REFERENCE] OK — GKP2012 lit review: "innovation displaces existing agents and creates a systematic risk factor under incomplete markets" matches GKP's contribution; "displacement risk is distinct from aggregate consumption risk" is verbatim from GKP
- **Line 64** [REFERENCE] OK — Jones2024 lit review: "trade-off between AI-driven growth and existential risk" matches Jones's title and content; "attenuates rather than amplifies" is the paper's own result (Proposition 2)
- **Line 66** [REFERENCE] OK — standard lit attributions (Kogan-Papanikolaou, Barro, Wachter, Pastor-Veronesi, Aghion-Jones-Jones, Acemoglu); characterizations are accurate

## Model (lines 71–175)
- **Line 71** — section header
- **Line 75** [DEFINITION] OK — representative household as marginal investor; AI owners hold private capital
- **Line 75** [REFERENCE] OK — GKP2012 analogy for AI owners as future capital owners; paper explicitly disclaims modeling entry dynamics
- **Line 78–81** [DEFINITION] OK — constant consumption growth $C_{t+1} = (1+g)C_t$ absent singularity
- **Line 84** [DEFINITION] OK — $c_t^H = \alpha_t C_t$; AI owners receive $(1-\alpha_t)C_t$; partition is exhaustive
- **Line 87** [ASSUMPTION] OK — singularity probability $p$ per period; no singularity leaves $\alpha_t$ unchanged
- **Line 90–93** [DEFINITION] OK — non-extinction singularity: consumption jumps by $1+\eta$, household share drops by $\phi$
- **Line 94** [VERBAL] OK — smaller $\phi$ means larger displacement
- **Line 95** [DEFINITION] OK — extinction: $C_{t+1}=0$; Jones2024 reference accurate
- **Line 98** [VERBAL] OK — singularities can recur, progressively displacing household
- **Line 104** [DEFINITION] OK — AI dividends $D_t^{AI} = \theta_t C_t$; upon singularity $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$
- **Line 105** [DEFINITION] OK — non-AI dividends $D_t^N = (1-\theta_t)C_t$
- **Line 108** [ARITHMETIC] OK — $D^{AI} + D^N = \theta_t C_t + (1-\theta_t)C_t = C_t$
- **Line 108** [VERBAL] OK — dividends distributed among all investors; $\alpha_t \neq \theta_t$ because consumption split differs from dividend split
- **Line 110** [DEFINITION] OK — market incompleteness: household cannot purchase restricted AI equity
- **Line 112** [VERBAL] OK — $\phi$ governs total consumption share including non-tradeable components; AI stocks provide hedging but do not eliminate displacement
- **Line 115** [DEFINITION] OK — CRRA utility with $\gamma > 1$, $\beta \in (0,1)$; equation correctly stated
- **Line 123** [VERBAL] OK — household's SDF reflects its own consumption growth due to market incompleteness
- **Line 129** [ARITHMETIC] OK — P/D formula for AI stocks: $v = A/(1-A)$ where $A = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$
- **Line 133** [ARITHMETIC] OK — P/D formula for non-AI stocks: same structure with $\Gamma^N$
- **Line 136** [ARITHMETIC] OK — $\Gamma^{AI} = [\theta+\Delta\theta(1-\theta)]/\theta \cdot (1+\eta)$; at baseline $= 0.32/0.15 \times 1.5 = 3.2$
- **Line 136** [ARITHMETIC] OK — $\Gamma^N = [1-\theta-\Delta\theta(1-\theta)]/(1-\theta) \cdot (1+\eta) = (1-\Delta\theta)(1+\eta)$; at baseline $= 0.8 \times 1.5 = 1.2$; theta-independent
- **Line 144–148** [DEFINITION] OK — existence condition $A^j < 1$ correctly stated; verbal explanation accurate
- **Line 148** [REFERENCE] OK — cross-reference to Section 4.2 for transfers motivation; confirmed at line 233
- **Line 151** [VERBAL] OK — closed-form approximation: treats post-singularity P/D as equal to pre-singularity; exact as $\Delta\theta \to 0$; non-AI closed form is exact because $\Gamma^N$ is theta-independent
- **Line 151** [VERBAL] OK — table uses numerically exact backward recursion; confirmed by R code
- **Line 153** [ARITHMETIC] OK — $\Gamma^{AI} > 1+\eta$ ($3.2 > 1.5$); $\Gamma^N < 1+\eta$ ($1.2 < 1.5$)
- **Line 153** [VERBAL] OK — AI stocks pay off when household consumption falls ($\phi(1+\eta) = 0.75 < 1$); hedging channel correctly described
- **Line 155** [VERBAL] OK — spread widens with displacement severity (decreasing $\phi$) and singularity probability $p$
- **Line 158** [VERBAL] OK — Proposition 2: valuation spread decreasing in $\xi$; both level and ratio decrease
- **Line 162** [ARITHMETIC] OK — proof decomposition $A^j = B[(1-p)+p(1-\xi)S\Gamma^j]$ verified; $B = \beta(1+g)^{1-\gamma}$, $S = (1+\eta)^{-\gamma}\phi^{-\gamma}$
- **Line 162** [ARITHMETIC] OK — $f(A) = A/(1-A)$ convexity: $f''(A) = 2/(1-A)^3 > 0$; verified
- **Line 162** [ARITHMETIC] OK — $\Gamma^{AI} > \Gamma^N$ implies larger absolute reduction in $A^{AI}$; convexity plus $A^j > 1/2$ (all table P/D ratios exceed 1) implies larger proportional reduction in AI P/D ratio
- **Line 167** [REFERENCE] OK — GKP2012 parallel: continuous displacement from expanding variety vs. discrete AI singularity; accurate
- **Line 169** [VERBAL] OK — under complete markets $\phi_\text{eff} \to 1$; premium "largely collapses" with residual from $\Gamma^{AI} \neq \Gamma^N$
- **Line 169** [REFERENCE] OK — GKP analogy: future innovators' rents untradeable; paper disclaims modeling entry dynamics
- **Line 171** [VERBAL] OK — severe displacement can violate existence condition; this discontinuity has no analog in GKP's gradual displacement; motivates government transfers

## Quantitative Analysis (lines 176–193)
- **Line 176** — section header
- **Line 185** [ASSUMPTION] OK — parameters match table footnote: $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$
- **Line 185** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; household consumption falls by 25%
- **Line 185** [VERBAL] OK — parameter interpretations all correct (50% consumption jump, 15% AI share, 20% share jump of non-AI remainder)
- **Line 187** [ARITHMETIC] OK — at $p=0.5\%$, $\xi=0\%$: AI P/D = 15.5, Non-AI = 11.1, ratio = 1.4; all match table exactly
- **Line 187** [ARITHMETIC] OK — at $p=1\%$, $\xi=0\%$: ratio = 2.0; matches table
- **Line 187** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium": confirmed across all $\xi$ columns in table
- **Line 187** [VERBAL] OK — "extinction risk compresses the AI premium": confirmed across all $p$ blocks (e.g., at $p=1\%$: ratio falls from 2.0 to 1.7 as $\xi$ goes from 0% to 20%)
- **Line 187** [REFERENCE] OK — "as Proposition 2 predicts": Proposition 2 states spread decreases in $\xi$; table confirms
- **Line 189** [FIGURE/TABLE] OK — S&P 500 P/D described as "historically elevated"; consistent with Figure 1 Panel (a)
- **Line 189** [VERBAL] OK — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015": Figure 1 Panel (b) shows NASDAQ/S&P ratio normalized to Jan 2015=100 reaching ~140-150; "roughly 50%" is at the upper end but defensible with the hedge word "roughly"
- **Line 189** [VERBAL] OK — caveats about NASDAQ breadth, earnings vs. multiples, and S&P AI exposure are accurate and appropriate
- **Line 189** [ARITHMETIC] OK — "1.3 to 2 times" for $p \in [0.5\%, 1\%]$: table confirms range spans from 1.3 (p=0.5%, xi=10-20%) to 2.0 (p=1%, xi=0%)

## Extensions: Market Incompleteness and the Singularity (lines 194–278)
- **Line 194** — section header
- **Line 196** [VERBAL] OK — baseline model takes market incompleteness as given; extensions examine consequences
- **Line 200** [DEFINITION] OK — positive singularity: $\alpha_{t+1} = \min(1, \alpha_t/\phi)$; with $\alpha=0.70$, $\phi=0.5$: $\alpha/\phi = 1.4$, $\min(1,1.4) = 1.0$
- **Line 200** [ASSUMPTION] OK — $q > 1/2$: positive singularity more likely
- **Line 202** [VERBAL] OK — Kaldor-Hicks efficiency holds when $(1+\eta)>1$ since aggregate consumption rises; correct
- **Line 204** [DEFINITION] OK — veto cost $\kappa$: permanent consumption fraction lost; $(1-\kappa)\alpha C_t$
- **Line 204** [VERBAL] OK — extinction utility normalized to zero; CRRA with $\gamma>1$ gives negative utility for $c>0$, making veto result conservative
- **Line 206** [ARITHMETIC] OK — complete-markets consumption: $\alpha(1+\eta)C_t(1+g)$ in both singularity states; confirmed by R code
- **Line 210** [VERBAL] OK — Proposition 3(i): threshold $\bar{\gamma}$ exists for veto under incomplete markets
- **Line 211** [VERBAL] OK — Proposition 3(ii): under complete markets, no veto for small $\kappa$
- **Line 219** [ARITHMETIC] OK — $\Delta u(\gamma)$ formula consistent with the Bellman equation and R code
- **Line 222** [ARITHMETIC] OK — $\phi(1+\eta) = 0.75 < 1$ confirms consumption drops in negative singularity; dominance as $\gamma \to \infty$ is correct
- **Line 224** [ARITHMETIC] OK — complete-markets utility gain $u(\alpha(1+\eta)) - u(\alpha) > 0$ since $\eta > 0$
- **Line 227** [ARITHMETIC] OK — veto example parameters match R code; $q/(1-q) = 0.70/0.30 = 2.33$, so "more than twice as likely" is correct
- **Line 227** [VERBAL] OK — household vetoes under incomplete markets, does not veto under complete markets; confirmed by R code computation
- **Line 229** [VERBAL] OK — extinction risk interaction with veto correctly described under both normalizations
- **Line 231** [REFERENCE] OK — Jones2024 observation about consumption levels and AI risk attitudes; accurate characterization
- **Line 237** [REFERENCE] OK — GKP2012 cited for intergenerational transfers as robustness; accurate characterization of their limiting-case argument
- **Line 242** [ARITHMETIC] OK — transfer consumption equation: $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$; verified algebraically and matches R code
- **Line 245** [VERBAL] OK — $(1-\phi\alpha)$ is AI owners' share of post-singularity consumption, not the dividend share $\theta$; important distinction correctly noted
- **Line 250** [ARITHMETIC] OK — $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$; follows from dividing eq. (transfer-consumption) by $\alpha(1+\eta)(1+g)C_t$; matches R code
- **Line 253** [VERBAL] OK — $\phi_\text{eff}$ substitutes for $\phi$ in P/D formula; confirmed by R code
- **Line 258** [ARITHMETIC] OK — transfer ratio $c^H_{post}/c^H_\text{no-transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$; independent of $\eta$; verified algebraically ($(1+\eta)$ cancels)
- **Line 261** [VERBAL] OK — ratio exceeds one whenever $\tau > 0$; transfers always improve household's singularity-state position
- **Line 263** [ASSUMPTION] OK — figure parameters match R code: $\gamma=4$, $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$
- **Line 263** [ARITHMETIC] OK — baseline $\phi(1+\eta) = 0.75$, 25% loss; large singularity $\phi(1+\eta) = 0.05 \times 10 = 0.5$, 50% loss
- **Line 265** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$; correctly computed
- **Line 265** [VERBAL] OK — P/D undefined at $\tau=0$ for large singularity: existence condition violated ($K \approx 1.59 > 1$); confirmed by R code returning NA
- **Line 265** [VERBAL] OK — transfers restore finite P/D by reducing effective displacement; consistent with figure Panel (a)
- **Line 269** [FIGURE/TABLE] OK — caption accurately describes both panels: Panel (a) shows P/D compression with transfers, undefined at low $\tau$ for large singularity; Panel (b) shows catastrophic consumption loss at $\tau=0$ and gains from transfers
- **Line 274** [VERBAL] OK — policy interpretation: transfers are blunt in normal times but effective if singularity growth overwhelms deadweight costs; consistent with the model
- **Line 274** [REFERENCE] OK — Jones2024 and Nordhaus2021 cited for explosive output growth; appropriate references

## Conclusion (lines 279–289)
- **Line 279** — section header
- **Line 281** [VERBAL] OK — "AI stocks trade at high valuations": motivating observation throughout paper
- **Line 281** [VERBAL] OK — "part of this premium reflects a hedging motive": precisely the mechanism of Proposition 1; "partially insure" correctly qualified
- **Line 281** [VERBAL] OK — "requires market incompleteness": confirmed by Section 2.1 (line 110) and Proposition 3(ii)
- **Line 281** [VERBAL] OK — "attenuated by extinction risk": matches Proposition 2 direction and mechanism
- **Line 281** [VERBAL] OK — "risk-averse households may inefficiently block AI development": matches Proposition 3(i) with correct qualifiers ("may," "risk-averse")
- **Line 281** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough": matches Extension 2 results
- **Line 283** [VERBAL] OK — model limitations accurately stated (discrete-time, no heterogeneous beliefs, no production side); goal correctly described as highlighting a specific channel

## Proof of Proposition 1 (lines 290–321)
- **Line 290** — section header
- **Line 295** [DEFINITION] OK — Euler equation correctly stated for CRRA household
- **Line 298** [ASSUMPTION] OK — constant P/D ratio in stationary pre-singularity equilibrium
- **Line 301** [ARITHMETIC] OK — no-singularity state: $c_{t+1}^H/c_t^H = 1+g$; $D_{t+1}^{AI}/D_t^{AI} = 1+g$; both verified
- **Line 302** [ARITHMETIC] OK — non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+\eta)(1+g)$; $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$; both verified
- **Line 303** [ARITHMETIC] OK — extinction: payoff is zero
- **Line 309–311** [ARITHMETIC] OK — Euler equation expansion verified: $(1+g)^{-\gamma}$ correctly factored; no-singularity term has $(1+g)(v+1)D_t$; non-extinction term has $[\phi(1+\eta)]^{-\gamma}(1+g)\Gamma^{AI}(v+1)D_t$
- **Line 314** [ARITHMETIC] OK — $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is theta-independent: $(1-\theta)(1-\Delta\theta)/(1-\theta) = 1-\Delta\theta$; verified
- **Line 314** [VERBAL] OK — post-singularity P/D approximated as $v^{AI}$; approximation exact as $\Delta\theta \to 0$; non-AI closed form is exact
- **Line 314** [VERBAL] OK — backward recursion over theta chain for numerically exact values; matches R code implementation
- **Line 317** [ARITHMETIC] OK — solving $v = A(v+1)$ gives $v = A/(1-A)$; formula matches Proposition 1 with $A = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$
- **Line 320** [VERBAL] OK — non-AI derivation identical with $\Gamma^N$; correct by symmetry
