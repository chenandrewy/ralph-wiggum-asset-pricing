# tests/factcheck-bysection.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 12m 45s
[ralph-garage/agent-logs/20260409T194838.523084-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T194838.523084-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct; all verbal claims are supported; no materially wrong claims found (two minor reference-characterization concerns noted).

## Introduction (lines 39–71)
- **Line 39** — section header
- **Line 41** [FIGURE/TABLE] OK — Claim that NASDAQ has "dramatically outpaced" S&P 500 since 2015 with gap widening since 2023 is supported by the figure generated from live FRED/Shiller data in `code/generate-exhibits.R`.
- **Line 45** [FIGURE/TABLE] OK — Caption states NASDAQ is solid, S&P 500 is dashed, normalized to January 2015 = 100; R code confirms `scale_linetype_manual` assigns solid to NASDAQ and dashed to S&P 500; normalization to first common month (January 2015) = 100. Sources (FRED for NASDAQ, Shiller for S&P 500) match code download URLs.
- **Line 50** [VERBAL] OK — Hedging motive argument (AI stocks as imperfect substitute for private AI capital) is the paper's main thesis, developed formally in Section 2.
- **Line 52** [REFERENCE] OK — GKP2012 characterized as showing "innovation creates a systematic risk factor because the rents from new technologies accrue to agents that current investors cannot trade with." Accurately paraphrases GKP's abstract and introduction.
- **Line 52** [REFERENCE] OK — Jones2024 correctly cited for extinction risk from AI.
- **Line 54** [VERBAL] OK — Model description (closed-form solutions, representative household, stochastic singularity, two public assets, extinction) all match Section 2.
- **Line 56** [VERBAL] OK — Extension summaries (veto distortion, government transfers) match Sections 4.1 and 4.2. "Both extensions branch directly off the baseline model" is confirmed by the paper structure.
- **Line 58** [ARITHMETIC] OK — "Up to roughly six times higher": table maximum ratio is 5.8 (at $p=1\%$, $\xi=0\%$), which rounds naturally to "roughly six."
- **Line 58** [REFERENCE] OK — Proposition 2(iii) explicitly states the spread and ratio are decreasing in $\xi$, supporting "extinction risk attenuates this gap."
- **Line 58** [VERBAL] OK — Self-referential claim about AI agents writing the paper is a meta-statement about the authorship process.
- **Line 63** [REFERENCE] OK — GKP2012 lit review characterization is accurate: general-equilibrium model, innovation displaces existing agents, systematic risk factor under incomplete markets, displacement risk distinct from aggregate consumption risk, growth stocks provide partial hedge.
- **Line 65** [REFERENCE] OK — Jones2024 characterization ("bounded utility functions make agents conservative about extinction even when consumption gains are enormous") accurately reflects the paper's key result.
- **Line 65** [VERBAL] OK — "Attenuating rather than amplifying" is consistent with Proposition 2(iii): higher $\xi$ shrinks weight on non-extinction states, compressing the spread.
- **Line 67** [REFERENCE] OK — KoganPapanikolaou2014: "technology shocks generate cross-sectional differences in stock returns through firms' heterogeneous exposures to growth opportunities" is an accurate summary of the JF 2014 paper.
- **Line 67** [REFERENCE] OK — KoganPapanikolaouSchmidtSong2020: "creative destruction generates inequality and valuations" is a reasonable compression of the JPE 2020 paper's contribution.
- **Line 67** [REFERENCE] OK — Knesl2023: "models and tests automation-driven displacement risk in asset prices" is accurate for the JFE paper.
- **Line 67** [REFERENCE] OK — Barro2006 and Wachter2013 as "rare disasters literature" providing "methodological foundation for pricing discrete catastrophic events" are canonical references.
- **Line 67** [REFERENCE] OK — PastorVeronesi2009: "technological revolutions affect stock prices through uncertainty about long-run productivity" accurately describes the AER paper.
- **Line 67** [REFERENCE] OK — KorinekSuh2024: "scenarios for the transition to AGI and their implications for wages, output, and welfare" matches the paper's content.

## Model (lines 72–183)
- **Line 72** — section header
- **Line 76** [DEFINITION] OK — Representative household and AI owners introduced. AI owners as analogous to future capital owners in GKP2012.
- **Line 76** [REFERENCE] OK — GKP2012 for future capital owners not yet participating in markets.
- **Line 79–83** [DEFINITION] OK — Aggregate consumption growth: $C_{t+1} = (1+g)C_t$ with $g > 0$.
- **Line 85** [DEFINITION] OK — Household share $\alpha_t \in (0, 1-\theta_t]$, consumption $c_t^H = \alpha_t C_t$. Upper bound ensures private AI capital dividends are non-negative.
- **Line 88** [ASSUMPTION] OK — Singularity probability $p$ per period.
- **Line 91–94** [ASSUMPTION] OK — Non-extinction singularity (prob $1-\xi$): consumption jumps by $1+\eta$, household share drops to $\phi\alpha_t$ with $\phi \in (0,1)$.
- **Line 95** [VERBAL] OK — "Smaller $\phi$ means larger displacement." Correct by definition.
- **Line 96** [REFERENCE] OK — Jones2024 for extinction risk: "the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest" matches Jones's key insight.
- **Line 99** [VERBAL] OK — Singularities can recur, progressively displacing the household.
- **Line 105** [DEFINITION] OK — AI stock dividends $D_t^{AI} = \theta_t C_t$; upon singularity $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$.
- **Line 106** [DEFINITION] OK — Non-AI stock dividends $D_t^N = (1-\theta_t)C_t$.
- **Line 109** [DEFINITION] OK — Private AI capital dividends $(1-\alpha_t)C_t - D_t^{AI}$; household cannot trade. Source of market incompleteness.
- **Line 112** [ASSUMPTION] OK — CRRA with $\gamma > 1$, $\beta \in (0,1)$.
- **Line 120** [VERBAL] OK — Under incomplete markets, household's SDF reflects its own consumption growth, not aggregate. Standard result.
- **Lines 126–127** [ARITHMETIC] OK — P/D formula for AI stocks verified via Euler equation derivation in appendix. Independent recomputation confirms table values (e.g., $p=0.5\%$, $\xi=0\%$: $K_{AI} \approx 0.946$, P/D $\approx 17.5$).
- **Lines 130–131** [ARITHMETIC] OK — P/D formula for non-AI stocks; same structure with $\Gamma^N$.
- **Line 133** [ARITHMETIC] OK — $\Gamma^{AI} = [\theta + \Delta\theta(1-\theta)]/\theta \cdot (1+\eta)$. With baseline parameters: $(0.15+0.17)/0.15 \times 1.5 = 3.2$. $\Gamma^N = (1-\Delta\theta)(1+\eta) = 0.8 \times 1.5 = 1.2$.
- **Lines 141–144** [VERBAL] OK — Existence condition $A^j < 1$ is correct. Since all terms are positive, $A^j > 0$ automatically; the binding constraint is $A^j < 1$.
- **Line 145** [REFERENCE] OK — Section 4.2 (line 264) confirms the existence condition is violated under large-singularity parameters ($\phi^{-\gamma} = 160{,}000$).
- **Line 148** [VERBAL] OK — $\Gamma^{AI} > 1+\eta$: verified ($3.2 > 1.5$). $\Gamma^N < 1+\eta$: verified ($1.2 < 1.5$).
- **Line 148** [VERBAL] OK — "$\phi(1+\eta) < 1$ when $\phi$ is sufficiently small": true for $\phi < 1/(1+\eta)$. With baseline $\phi=0.5$, $\eta=0.5$: $0.75 < 1$.
- **Lines 150–155** [VERBAL] OK — Corollary 1 proof: $K/(1-K)$ is increasing in $K$; $K$ is increasing in $\Gamma^j$; $\Gamma^{AI} > \Gamma^N$ when $\Delta\theta > 0$. Logic is correct.
- **Lines 158–163** [VERBAL] OK — Proposition 2 comparative statics: (i) decreasing $\phi$ raises $\phi^{-\gamma}$, amplifying AI stocks more; (ii) increasing $p$ weights singularity states more, requires $\gamma$ large; (iii) increasing $\xi$ shrinks weight on non-extinction states, compressing both spread and ratio.
- **Lines 168–172** [VERBAL] OK — Proof arguments for all three parts are logically sound.
- **Line 177** [REFERENCE] OK — GKP2012 mechanism comparison: "continuous displacement from expanding technological variety" vs. discrete AI singularity. Accurate characterization.
- **Line 179** [VERBAL] OK — Complete markets would eliminate valuation spread; echoes GKP2012's point about untradeable future innovator rents.

## Quantitative Analysis (lines 184–201)
- **Line 184** — section header
- **Line 188** [FIGURE/TABLE] OK — Table caption correctly describes content.
- **Line 193** [ASSUMPTION] OK — All seven parameter values ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$) match the R code exactly.
- **Line 193** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$. Confirmed.
- **Line 193** [ARITHMETIC] OK — "Household consumption falls by 25%": $1 - 0.75 = 0.25$. Confirmed.
- **Line 193** [VERBAL] OK — "$\eta=0.5$: aggregate consumption rises by 50%." Confirmed.
- **Line 193** [VERBAL] OK — "$\theta=0.15$: AI stocks initially 15% of the economy." Confirmed.
- **Line 193** [VERBAL] OK — "$\Delta\theta=0.2$: AI's share jumps by 20% of the non-AI remainder." Confirmed.
- **Line 195** [ARITHMETIC] OK — "P/D of roughly 18" at $p=0.5\%$, $\xi=0\%$: table shows 17.5. Acceptable rounding.
- **Line 195** [ARITHMETIC] OK — "Non-AI stocks trade near 11": table shows 11.1. Confirmed.
- **Line 195** [ARITHMETIC] OK — "A ratio of about 1.6": table shows 1.6. Confirmed.
- **Line 195** [ARITHMETIC] OK — "At $p=1\%$, the ratio rises to nearly 6 to 1": table shows 5.8. "Nearly 6" is accurate.
- **Line 195** [VERBAL] OK — "Increasing singularity probability raises AI stock premium": confirmed by all rows of the table (ratio strictly increases with $p$ for each $\xi$).
- **Line 195** [VERBAL] OK — "Extinction risk reduces both valuations and compresses the AI premium": confirmed by all columns (both P/Ds and ratio decrease as $\xi$ increases for each $p$).
- **Line 195** [REFERENCE] OK — Proposition 2(iii) predicts exactly this pattern.
- **Line 197** [VERBAL] OK — "NASDAQ has appreciated roughly 50% more than S&P 500 since 2015": approximate empirical claim tied to the figure, consistent with well-known market data.
- **Line 197** [ARITHMETIC] OK — "1.5 to 6 times higher" across $p = 0.5\text{--}1\%$: actual table range is 1.4 to 5.8. Minor rounding (lower bound 1.4 rounded to 1.5, upper bound 5.8 rounded to 6). Acceptable approximation for narrative text.

## Extensions: Market Incompleteness and the Singularity (lines 202–277)
- **Line 202** — section header
- **Line 204** [VERBAL] OK — Accurate framing of the two extensions.
- **Line 208** [ASSUMPTION] OK — Setup with positive/negative singularity conditional on non-extinction is internally consistent.
- **Line 211** [DEFINITION] OK — Positive singularity: $\alpha_{t+1} = \phi^+\alpha_t$ with $\phi^+ > 1$.
- **Line 212** [DEFINITION] OK — Negative singularity mirrors baseline ($\phi < 1$).
- **Line 215** [ASSUMPTION] OK — $\lambda > 1/2$ as condition for social efficiency.
- **Line 217** [ASSUMPTION] OK — Veto costs $\kappa > 0$ in utility terms.
- **Line 220** [DEFINITION] OK — Period utility $u(c) = c^{1-\gamma}/(1-\gamma)$.
- **Line 223** [ARITHMETIC] OK — $\Delta U^H$ formula correctly weights non-extinction singularity states ($p(1-\xi)$), splits by $\lambda/(1-\lambda)$, and subtracts baseline singularity utility $p \cdot u(\alpha(1+g)C_t)$. Extinction normalized to zero drops out.
- **Line 226** [VERBAL] OK — $u(c) < 0$ for $\gamma > 1$: since $1-\gamma < 0$, $c^{1-\gamma} > 0$, so $u(c) = c^{1-\gamma}/(1-\gamma) < 0$. Confirmed.
- **Line 226** [VERBAL] OK — "Normalization makes veto result conservative": setting $u_\text{ext}=0 > u(c)$ treats extinction as less bad than any finite consumption, making the household more willing to allow development. Finding a veto despite this is conservative.
- **Line 226** [REFERENCE] OK — Attribution to Jones (2024) for the extinction-utility normalization approach. Jones discusses bounded utility with extinction risk; the normalization is consistent with his framework.
- **Line 229** [VERBAL] OK — Part (i): for $\gamma$ large, negative singularity utility diverges to $-\infty$ and dominates. Mathematically sound.
- **Line 231** [VERBAL] OK — Part (ii): complete markets allow full hedging; expected utility reflects positive social surplus.
- **Line 240** [VERBAL] OK — Higher $\xi$ under $u_\text{ext}=0$ reduces weight on non-extinction states, reducing veto incentive. More severe extinction penalty would amplify veto incentive. Both claims are logically correct.
- **Line 244** [REFERENCE] OK — GKP2012 characterized as showing intergenerational transfers can affect displacement risk magnitude. GKP's Section VII discusses how intergenerational risk sharing through bequests and dynasties affects displacement. The paper's characterization that "such transfers do not alter the functional form of the stochastic discount factor" is consistent with GKP's complete-markets framework where the SDF form is invariant to redistribution.
- **Line 246** [DEFINITION] OK — Tax rate $\tau$, deadweight cost $\delta_0\tau$, transfer mechanics are internally consistent.
- **Line 249** [ARITHMETIC] OK — Post-transfer consumption formula verified: household displaced consumption plus net transfer $\tau(1-\delta_0\tau)$ of AI surplus $(1-\phi\alpha)(1+\eta)C_t(1+g)$. Matches R code.
- **Line 257** [ARITHMETIC] OK — Ratio $c^H_\text{post}/c^H_\text{no-transfer} = 1 + \tau(1-\delta_0\tau)(1-\phi\alpha)/(\phi\alpha)$. Derived by dividing line 249 by $\phi\alpha(1+\eta)C_t(1+g)$; $(1+\eta)$ and $C_t(1+g)$ cancel. Independent of $\eta$. Confirmed.
- **Line 260** [VERBAL] OK — Ratio exceeds one for $\tau > 0$: requires $1-\delta_0\tau > 0$, which holds since $\tau < 1$ and $\delta_0 = 0.5$ gives $\delta_0\tau < 0.5$.
- **Line 262** [ARITHMETIC] OK — Large singularity: $\phi_\text{large}(1+\eta_\text{large}) = 0.05 \times 10 = 0.5$. "Consumption halves." Confirmed.
- **Line 262** [ARITHMETIC] OK — Baseline: $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$. "Falls by 25%." Confirmed.
- **Line 262** [VERBAL] OK — "Ten-fold growth": $1+\eta = 10$. Confirmed.
- **Line 264** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$. Confirmed.
- **Line 264** [VERBAL] OK — Existence condition violated at $\tau=0$ under large-singularity parameters. Confirmed by R code returning NA for these parameters. As $\tau$ increases, $\phi_\text{eff}$ rises, restoring finite P/D ratios.
- **Line 268** [FIGURE/TABLE] OK — Caption parameters ($p=0.5\%$, $\xi=5\%$, $\delta_0=0.5$) match R code (`p_ext=0.005`, `xi_ext=0.05`, `delta0=0.50`).
- **Line 273** [REFERENCE] OK — Jones2024 for explosive output growth; Nordhaus2021 ("Are We Approaching an Economic Singularity?") for critical examination. Both characterizations are accurate.

## Conclusion (lines 278–288)
- **Line 278** — section header
- **Line 280** [VERBAL] OK — "Part of this premium reflects a hedging motive": supported by Proposition 1 and Corollary 1.
- **Line 280** [VERBAL] OK — "Requires market incompleteness": established at line 109; counterfactual at line 179.
- **Line 280** [VERBAL] OK — "Attenuated by extinction risk": Proposition 2(iii).
- **Line 280** [VERBAL] OK — "Reduces the weight on non-extinction states": precise paraphrase of Proposition 2(iii) proof mechanism.
- **Line 280** [VERBAL] OK — "Risk-averse households may inefficiently block AI development": Proposition 3(i).
- **Line 280** [VERBAL] OK — "Government transfers, normally wasteful, can become effective": Extension 2 analysis.
- **Line 282** [VERBAL] OK — "Abstracts from continuous-time dynamics": model is discrete-time (line 76).
- **Line 282** [VERBAL] OK — "Heterogeneous beliefs": not modeled; representative household.
- **Line 282** [VERBAL] OK — "Production-side details": endowment economy, no production function.

## Proof of Proposition 1 (lines 289–318)
- **Line 289** — section header
- **Line 294** [DEFINITION] OK — Standard CRRA Euler equation for the household as marginal investor.
- **Line 297** [VERBAL] OK — $v^{AI} = P^{AI}/D^{AI}$ is constant in the pre-singularity stationary equilibrium (both $\alpha_t$ and $\theta_t$ are fixed).
- **Line 300** [ARITHMETIC] OK — No-singularity case: $c_{t+1}^H/c_t^H = 1+g$ and $D_{t+1}^{AI}/D_t^{AI} = 1+g$. Verified from model primitives.
- **Line 301** [ARITHMETIC] OK — Non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$ and $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$. Verified from $\alpha_{t+1}=\phi\alpha_t$, $C_{t+1}=(1+\eta)(1+g)C_t$, and $\theta_{t+1}=\theta+\Delta\theta(1-\theta)$.
- **Line 302** [ARITHMETIC] OK — Extinction: $C_{t+1}=0$ implies payoff is zero. Standard convention in rare-disasters literature.
- **Lines 307–308** [ARITHMETIC] OK — Euler equation substitution verified: $(1+g)^{-\gamma}$ correctly factored from both states; singularity SDF $[\phi(1+\eta)]^{-\gamma}$ correctly applied.
- **Line 311** [VERBAL] OK — Tractability approximation (post-singularity P/D $\approx v^{AI}$) transparently disclosed; exact when economy is stationary conditional on new share.
- **Line 314** [ARITHMETIC] OK — Solution $v^{AI} = A_\text{full}/(1-A_\text{full})$ where $A_\text{full} = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$. Algebra verified step by step: $v = A(v+1) \Rightarrow v(1-A) = A \Rightarrow v = A/(1-A)$. Matches Proposition 1 (line 126).
- **Line 317** [VERBAL] OK — Non-AI derivation identical with $\Gamma^{AI} \to \Gamma^N$. Confirmed: household SDF is the same; only dividend growth factor differs.
