# tests/factcheck-bysection.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 8m 13s
[ralph-garage/agent-logs/20260409T182005.683878-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.683878-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: FAIL
REASON: Line 57 overstates the valuation spread relative to the table, and line 307 mischaracterizes the proof of Proposition 3.

## Introduction (lines 38–70)

- **Line 38** — section header
- **Line 40** [VERBAL] OK — describes Figure 1 as illustrative P/E ratios for AI-exposed firms vs. broader market since 2015; hedged with "approximate values from public sources"
- **Lines 42–47** [FIGURE/TABLE] OK — figure environment properly defined; `fig-ai-valuations.pdf` exists and is referenced correctly
- **Line 49** [VERBAL] OK — "AI stocks serve as a hedge against displacement" is the core mechanism of Proposition 1 and Corollary 1
- **Line 49** [REFERENCE] OK — GKP2012 cited for "displacement risk from innovation" under incomplete markets; matches bib entry "Displacement Risk and Asset Returns" (JFE 2012)
- **Line 51** [VERBAL] OK — model description (representative household, stochastic singularity, two public assets) matches Section 2 setup
- **Line 51** [REFERENCE] OK — Jones2024 cited for extinction risk; matches bib entry "The AI Dilemma: Growth versus Existential Risk" (AER:I 2024)
- **Line 53** [REFERENCE] OK — GKP2012 described as showing innovation creates systematic risk from rents accruing to future cohorts; accurate characterization
- **Line 55** [VERBAL] OK — describes two extensions (veto and government transfers) consistent with Section 4
- **Line 57** [VERBAL] ERROR — claims "P/D ratios for AI stocks can be two to six times higher than for non-AI stocks across a range of singularity probabilities"
  - The table's Ratio column ranges from 1.1 to 5.8. Ratios reach 2× only at p ≥ 0.8% (ξ = 0%). The majority of parameter combinations yield ratios of 1.1–1.6. The phrase "two to six times" overstates the lower bound; "up to roughly six times" or "1.1 to nearly 6 times" would be accurate.
- **Line 57** [REFERENCE] OK — "as Proposition 2(iii) shows" correctly references the extinction-compression result at lines 180–181
- **Line 57** [VERBAL] OK — disclosure that paper was produced by AI agents
- **Lines 60–62** [REFERENCE] OK — GKP2012 lit review description accurate: general-equilibrium model, displacement from innovation, growth stocks as partial hedge
- **Line 64** [REFERENCE] OK — Jones2024 described as studying trade-off between AI growth and existential risk with bounded utility; accurate
- **Line 66** [REFERENCE] OK — KoganPapanikolaouStoffman2020 ("Left Behind," JPE 2020), Barro2006 (QJE), Wachter2013 (JF), PastorVeronesi2009 (AER), GarleanuPanageas2015 (JPE), KorinekSuh2024 (NBER WP), Acemoglu2024 (NBER WP) — all descriptions match bib entries
- **Line 66** [REFERENCE] MINOR — KoganPapanikolaou2014 described as "technology shocks create a displacement risk factor"; their paper ("Growth Opportunities, Technology Shocks, and Asset Prices," JF 2014) focuses on growth opportunities and asset prices. The "displacement risk factor" framing is more characteristic of GKP2012. Not materially wrong but slightly imprecise.

## Model (lines 71–200)

- **Line 71** — section header
- **Line 73** — subsection header (Setup)
- **Line 75** [DEFINITION] OK — representative household as marginal investor; AI owners hold private capital; GKP analogy accurate with correct caveat ("we do not explicitly model the entry of new cohorts")
- **Lines 78–82** [DEFINITION] OK — aggregate consumption growth $C_{t+1} = (1+g)C_t$ absent singularity
- **Line 84** [DEFINITION] OK — $\alpha_t \in (0, 1 - \theta_t]$; upper bound ensures AI owners' private residual $(1-\alpha_t - \theta_t)C_t \geq 0$
- **Lines 87–96** [DEFINITION] OK — singularity structure: with prob $p$ singularity occurs; non-extinction (prob $1-\xi$) gives displacement $\alpha_{t+1} = \phi\alpha_t$ and consumption jump $1+\eta$; extinction (prob $\xi$) gives $C_{t+1}=0$. Jones2024 citation for extinction risk accurate.
- **Lines 100–106** [DEFINITION] OK — AI stock dividends $\theta_t C_t$; update rule $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ keeps $\theta < 1$. Non-AI dividends $(1-\theta_t)C_t$.
- **Line 108** [VERBAL] OK — private AI capital residual is $(1-\alpha_t - \theta_t)C_t$; arithmetic correct
- **Lines 111–115** [DEFINITION] OK — CRRA with $\gamma > 1$, $\beta \in (0,1)$
- **Line 117** — subsection header (Equilibrium prices)
- **Line 119** [VERBAL] OK — household SDF reflects own consumption growth due to incomplete markets
- **Line 132** [ARITHMETIC] OK — $\Gamma^{AI} = \frac{\theta + \Delta\theta(1-\theta)}{\theta}(1+\eta) = \frac{0.32}{0.15} \times 1.5 = 3.2$; $\Gamma^N = \frac{1-\theta-\Delta\theta(1-\theta)}{1-\theta}(1+\eta) = \frac{0.68}{0.85} \times 1.5 = 1.2$. Both formulas verified.
- **Line 145** [ARITHMETIC] OK — no-singularity: $c^H$ growth $= 1+g$, $D^{AI}$ growth $= 1+g$
- **Line 146** [ARITHMETIC] OK — non-extinction singularity: $c^H$ growth $= \phi(1+\eta)(1+g)$, $D^{AI}$ growth $= \Gamma^{AI}(1+g)$
- **Line 147** [ARITHMETIC] OK — extinction: payoff is zero
- **Lines 151–154** [ARITHMETIC] OK — Euler equation expansion correct; $(1+g)^{-\gamma}$ factors out properly from both branches; dividend growth combines with SDF to yield $(1+g)^{1-\gamma}$
- **Lines 158–160** [ARITHMETIC] OK — solving $v = X(v+1)$ gives $v = X/(1-X)$ where $X = \beta(1+g)^{1-\gamma}[(1-p) + p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$. Matches eq. (4).
- **Line 165** [VERBAL] OK — "$\phi(1+\eta) < 1$ when $\phi$ is sufficiently small": holds for $\phi < 1/(1+\eta)$. With $\eta = 0.5$, threshold is $\phi < 2/3$. Correct.
- **Line 165** [VERBAL] OK — hedging channel description: AI stocks pay off when household consumption falls. Supported by $\Gamma^{AI} > 1+\eta > \Gamma^N$ and high marginal utility in displacement states.
- **Lines 167–173** [ARITHMETIC] OK — Corollary 1: $P/D = X/(1-X)$ is increasing in $X$; $X$ is increasing in $\Gamma^j$; $\Gamma^{AI} > \Gamma^N$ when $\Delta\theta > 0$. Valid (given equilibrium exists).
- **Line 178** [VERBAL] OK — Prop 2(i): spread increasing in displacement severity (decreasing $\phi$). Correct: $\phi^{-\gamma}$ amplifies the singularity weight where AI and non-AI diverge.
- **Line 179** [VERBAL] OK — Prop 2(ii): spread increasing in $p$ for large $\gamma$. Correct.
- **Lines 180–181** [VERBAL] OK — Prop 2(iii): spread and ratio both decreasing in $\xi$. Verified numerically; higher $\xi$ shrinks weight on non-extinction states where dividends diverge.
- **Line 185** [VERBAL] MINOR — proof says decrease in $\phi$ "makes the divergence between $\Gamma^{AI}$ and $\Gamma^N$ more valuable"; $\Gamma^{AI}$ and $\Gamma^N$ do not depend on $\phi$. The actual mechanism is entirely through $\phi^{-\gamma}$ amplification. Conclusion correct but the second stated channel is mislabeled.
- **Line 192** — subsection header (Discussion)
- **Line 194** [REFERENCE] OK — GKP parallel described accurately: growth stocks hedge displacement from new-entrant innovation; key difference (continuous creative destruction vs. discrete singularity) is correct.
- **Line 196** [VERBAL] OK — market incompleteness argument correct: if household could buy full AI surplus, spread collapses.

## Quantitative Analysis (lines 201–218)

- **Line 201** — section header
- **Line 203** [ASSUMPTION] OK — $\beta = 0.96$, $g = 0.02$, $\gamma = 4$, $\phi = 0.5$, $\eta = 0.5$, $\theta = 0.15$, $\Delta\theta = 0.2$; all match table footnote and R code
- **Line 203** [ARITHMETIC] OK — "$\phi(1+\eta) = 0.75$": $0.5 \times 1.5 = 0.75$
- **Line 203** [ARITHMETIC] OK — "household consumption falls by 25%": $1 - 0.75 = 0.25$
- **Line 203** [ARITHMETIC] OK — "aggregate consumption rises by 50%": $\eta = 0.5$
- **Line 203** [ASSUMPTION] OK — "AI stocks are initially 15% of the economy": $\theta = 0.15$
- **Line 203** [ASSUMPTION] OK — "AI's share jumps by 20% of the non-AI remainder": $\Delta\theta = 0.2$
- **Lines 205–210** [FIGURE/TABLE] OK — table environment correct; `table-pd-ratios.tex` exists and matches
- **Line 212** [ARITHMETIC] OK — "AI stocks trade at a P/D of roughly 18" for $p = 0.5\%$, $\xi = 0\%$: table value 17.5, independently recomputed as 17.47. "Roughly 18" is a slight overstatement (~3% rounding) but defensible in prose.
- **Line 212** [ARITHMETIC] OK — "non-AI stocks trade near 11": table value 11.1, recomputed 11.09
- **Line 212** [ARITHMETIC] OK — "a ratio of about 1.6": table value 1.6, recomputed 1.576
- **Line 212** [ARITHMETIC] OK — "At $p = 1\%$, the ratio rises to nearly 6 to 1": table value 5.8, recomputed 5.757
- **Line 212** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium": ratio column is monotonically increasing in $p$ for every fixed $\xi$
- **Line 212** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium": both P/D values and ratio decrease as $\xi$ increases for every fixed $p$
- **Line 212** [REFERENCE] OK — "as Proposition 2(iii) predicts" correctly references lines 180–181
- **Line 214** [VERBAL] OK — "P/E ratios two to five times the market average" stated as approximate illustrative observation with appropriate hedging language
- **Line 214** [VERBAL] MINOR — "aligns with our model's predictions for annual singularity probabilities in the 0.5–1% range": at $p = 0.5\%$ the model ratio is 1.6×, below the stated empirical lower bound of 2×. The empirical range of 2–5× maps more precisely to $p \approx 0.6\text{–}0.9\%$. The stated range is slightly too wide at the lower end.

## Extensions: Market Incompleteness and the Singularity (lines 219–292)

- **Line 219** — section header
- **Line 223** — subsection header (Extension 1: Veto)
- **Lines 224–230** [DEFINITION] OK — positive singularity ($\phi^+ > 1$) with probability $\lambda$; negative ($\phi < 1$) with probability $1 - \lambda$; $\lambda > 1/2$
- **Line 232** [ASSUMPTION] OK — social efficiency from $\lambda > 1/2$; veto costs $\kappa > 0$
- **Lines 240–241** [ARITHMETIC] OK — $\Delta U^H$ formula: $p(1-\xi)[\lambda u(\phi^+\alpha(1+\eta)(1+g)C_t) + (1-\lambda)u(\phi\alpha(1+\eta)(1+g)C_t)] - p \cdot u(\alpha(1+g)C_t)$. Correctly accounts for extinction branch with $u_{ext} = 0$.
- **Line 243** [ARITHMETIC] OK — "$u(c) < 0$ for all $c > 0$ when $\gamma > 1$": with $u(c) = c^{1-\gamma}/(1-\gamma)$, denominator negative, numerator positive. Correct.
- **Line 243** [VERBAL] OK — "normalization makes the veto result conservative": setting $u_{ext} = 0 > u(c)$ reduces the cost of extinction, making the household less likely to veto. So proving the household vetoes despite this conservative normalization strengthens the result.
- **Line 252** [VERBAL] OK — Proof (i): high $\gamma$ makes utility strongly concave, so loss from $\phi < 1$ dominates gain from $\phi^+ > 1$ even with $\lambda > 1/2$. Standard expected utility logic.
- **Line 254** [VERBAL] OK — Proof (ii): under complete markets, household trades claims on private AI capital, capturing full social surplus (positive by assumption). No veto.
- **Line 257** [VERBAL] OK — discussion of veto distortion from market incompleteness; extinction risk interaction correctly described
- **Line 259** — subsection header (Extension 2: Government transfers)
- **Line 261** [REFERENCE] OK — GKP2012 observation about broader trading of innovation capital; accurate
- **Lines 266–267** [ARITHMETIC] OK — $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta_0\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. First term: displaced household consumption. Second term: net transfer from AI owners' surplus. Dimensionally and economically correct.
- **Lines 271–275** [ARITHMETIC] MISLEADING — limit formula $\lim_{\eta\to\infty} c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta_0\tau)(1-\phi\alpha)/(\phi\alpha)$
  - The formula is **correct**, but the ratio is actually **independent of $\eta$** for all $\eta > 0$ (the $(1+\eta)$ factors cancel exactly). Writing it as a limit and saying it "converges to a finite constant" implies an asymptotic approximation when the expression is in fact exact. The preceding sentence's economic argument—that the transfer base grows with $\eta$ while the deadweight cost rate is fixed—is valid for the **level** of consumption, but not for the **ratio**, which is $\eta$-invariant.
- **Line 277** [VERBAL] OK — "level of post-transfer consumption grows without bound as $\eta \to \infty$": correct, the level grows with $(1+\eta)$
- **Line 279** [ARITHMETIC] OK — "with $\phi = 0.5$ and $\eta = 0.5$, household consumption falls to 75%": $\phi(1+\eta) = 0.75$. Confirmed in R code comment.
- **Line 279** [VERBAL] OK — figure description (two panels: P/D vs. $\tau$; consumption growth vs. $\tau$; baseline vs. large singularity) matches R code structure
- **Line 288** [REFERENCE] OK — Jones2024 and Nordhaus2021 cited for explosive output growth; appropriate

## Conclusion (lines 293–304)

- **Line 293** — section header
- **Line 295** [VERBAL] OK — "hedging motive": established by Proposition 1 and the hedging channel discussion (line 165)
- **Line 295** [VERBAL] OK — "partially insure against displacement": matches model mechanism; "partially" is accurate because private AI capital is untradeable
- **Line 295** [VERBAL] OK — "requires market incompleteness": confirmed at lines 108 and 196 (spread collapses under complete markets)
- **Line 295** [VERBAL] OK — "attenuated by extinction risk": matches Proposition 2(iii)
- **Line 295** [VERBAL] OK — "households may inefficiently block AI development": matches Proposition 3(i)
- **Line 295** [VERBAL] OK — "government transfers can become effective if singularity-driven growth is large enough": matches Extension 2 results (eq. 9 and figure)
- **Line 297** [VERBAL] OK — "abstracts from continuous-time dynamics": model is discrete-time (line 75)
- **Line 297** [VERBAL] OK — "heterogeneous beliefs": model has representative household with single probability measure
- **Line 297** [VERBAL] OK — "production-side details": no production function; consumption growth is exogenous

## Proof Details (lines 305–308)

- **Line 305** — section header (Appendix A)
- **Line 307** [REFERENCE] OK — "Proofs of Propositions 1–2 are given in the main text": Proposition 1 proved at lines 135–163; Proposition 2 proved at lines 184–190. Both contain `\begin{proof}` environments.
- **Line 307** [REFERENCE] ERROR — "Proposition 3 relies on the comparison of expected utility under the household's SDF versus the social planner's SDF, which integrates over both agents' consumption"
  - The actual proof of Proposition 3 (lines 251–255) does not mention SDFs. Part (i) reasons about the household's utility under high $\gamma$; part (ii) reasons about the household trading claims under complete markets to capture the social surplus. The proof is framed entirely in utility/welfare terms. The appendix imports SDF language that is absent from the proof.
- **Line 307** [REFERENCE] ERROR — "The complete-markets result follows because, under complete markets, the household's SDF coincides with the social SDF, and the social surplus is positive by assumption"
  - The actual proof at lines 253–255 says the household "participates in the full surplus" and "the household's expected utility gain under complete markets reflects the social surplus." No SDF-coincidence argument is invoked. This is an inaccurate characterization of the proof's logic.
