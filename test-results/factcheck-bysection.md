# tests/factcheck-bysection.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 7m 35s
[ralph-garage/agent-logs/20260409T212047.337310-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.337310-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong; minor imprecisions in proof argumentation and reference characterizations do not rise to the level of errors.

## Introduction (lines 38–72)
- **Line 38** — section header
- **Line 40** [VERBAL] OK — "publicly traded stocks most exposed to AI have reached remarkable valuations" is qualitative framing consistent with Figure 1
- **Line 40** [FIGURE/TABLE] OK — "since 2015, the NASDAQ Composite has dramatically outpaced the S&P 500" is supported by Figure 1
- **Line 40** [VERBAL] OK — "gap widening sharply since 2023" is consistent with publicly known generative AI timeline
- **Line 44** [FIGURE/TABLE] OK — caption correctly describes figure contents: monthly closing prices, NASDAQ solid, S&P dashed, normalized to Jan 2015 = 100
- **Line 44** [REFERENCE] OK — "Sources: NASDAQ from FRED; S&P 500 from the Shiller dataset" matches R code (FRED series NASDAQCOM; datahub Shiller CSV)
- **Line 49** [VERBAL] OK — thesis statement ("hedging motive") is the paper's own argument, consistently developed
- **Line 49** [VERBAL] OK — "if markets were complete, investors could insure directly" consistent with spec §I.3b and model Section 2.3
- **Line 49** [VERBAL] OK — "much of this equity is restricted" consistent with GKP2012 mechanism and model setup
- **Line 51** [REFERENCE] OK — "The idea that technological displacement creates a systematic risk factor under incomplete markets originates with GKP2012, who show that rents from new technologies accrue to agents that current investors cannot trade with" — verified against GKP2012 (agents are future cohorts who cannot trade with current population)
- **Line 51** [VERBAL] OK — "We build on their framework by modeling a discrete AI singularity" — accurate self-description
- **Line 53** [ARITHMETIC] OK — "P/D ratios for AI stocks can reach roughly six times those of non-AI stocks" — table shows ratio of 5.8 at p=1%, ξ=0%; "can reach roughly six" is accurate at the upper end
- **Line 53** [REFERENCE] OK — "Extinction risk (Jones 2024) attenuates this gap" — table confirms increasing ξ reduces AI P/D ratio and ratio; Jones 2024 attribution for extinction risk is appropriate
- **Line 55** [VERBAL] OK — veto argument ("risk-averse household that cannot hedge may rationally choose to block") consistent with Proposition 3
- **Line 55** [VERBAL] OK — "Complete markets would eliminate this distortion" consistent with Proposition 3(ii)
- **Line 57** [REFERENCE] OK — "as GKP2012 emphasize, much of this capital belongs to future innovators and cannot yet be traded" — verified: GKP p. 492 states "future innovators, who are yet to enter the economy, are not able to trade"
- **Line 57** [VERBAL] OK — "explosive growth makes even grossly inefficient redistribution deliver large consumption gains" supported by equation (8) and Section 4.2 analysis
- **Line 59** [VERBAL] OK — AI authorship description consistent with spec §IV.5c
- **Line 64** [REFERENCE] OK — GKP2012 characterized as "general-equilibrium model in which innovation displaces existing agents and creates a systematic risk factor under incomplete markets" — accurate
- **Line 64** [REFERENCE] OK — "displacement risk is distinct from aggregate consumption risk and that growth stocks provide a partial hedge" — verified against GKP2012
- **Line 66** [REFERENCE] OK — Jones 2024 characterized as studying "trade-off between AI-driven growth and existential risk, showing that bounded utility functions make agents conservative about extinction" — verified against Jones 2024
- **Line 66** [VERBAL] OK — "extinction risk interacts with displacement in a countervailing way, attenuating rather than amplifying the valuation premium" — confirmed by table data
- **Line 68** [REFERENCE] OK — KoganPapanikolaou2014 and KoganPapanikolaouSeruStoffman2020 characterized as showing technology shocks and creative destruction generate cross-sectional return differences — reasonable compression of two related papers
- **Line 68** [REFERENCE] OK — Knesl2023 characterized as providing "direct empirical evidence that automation-driven displacement commands a risk premium" — consistent with JFE 2023 paper title
- **Line 68** [REFERENCE] OK — Barro2006 and Wachter2013 cited for rare disasters methodology — standard citations
- **Line 68** [REFERENCE] OK — PastorVeronesi2009 cited for technological revolutions and stock prices — accurate

## Model (lines 73–176)
- **Line 73** — section header
- **Line 77** [REFERENCE] OK — AI owners as analogous to GKP2012's future innovators — verified; paper correctly flags that it does not model entry dynamics
- **Line 77** [VERBAL] OK — "AI owners are a static group whose share changes only through the singularity mechanism" — consistent with model setup
- **Lines 80–84** [DEFINITION] OK — aggregate consumption growth $C_{t+1} = (1+g)C_t$ with $g > 0$
- **Line 86** [DEFINITION] OK — $c_t^H = \alpha_t C_t$; AI owners receive $(1-\alpha_t)C_t$; shares sum to 1
- **Lines 92–96** [DEFINITION] OK — non-extinction singularity: consumption jumps by $(1+\eta)$, household share becomes $\phi\alpha_t$ with $\phi \in (0,1)$
- **Line 97** [REFERENCE] OK — extinction ($C_{t+1}=0$) following Jones 2024 — verified: Jones emphasizes existential risk is highest precisely when AI is most powerful
- **Lines 106–108** [DEFINITION] OK — AI dividend share update rule $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ ensures $\theta_{t+1} \in (\theta_t, 1)$; non-AI dividends $(1-\theta_t)C_t$
- **Line 113** [ASSUMPTION] OK — CRRA with $\gamma > 1$ and $\beta \in (0,1)$; $\gamma > 1$ is used for negative utility (Jones normalization) and Prop 2(ii)
- **Lines 127–132** [ARITHMETIC] OK — P/D ratio formulas verified from Euler equation; $A^j/(1-A^j)$ form is correct
- **Line 134** [ARITHMETIC] OK — $\Gamma^{AI} = [\theta + \Delta\theta(1-\theta)]/\theta \cdot (1+\eta)$; with baseline params: $\Gamma^{AI} = 3.2$, $\Gamma^N = (1-\Delta\theta)(1+\eta) = 1.2$
- **Lines 141–146** [ARITHMETIC] OK — existence condition $A^j < 1$ is necessary and sufficient for positive finite P/D ratio
- **Line 149** [ARITHMETIC] OK — $\Gamma^{AI} > 1+\eta$ since $\Delta\theta(1-\theta) > 0$; $\Gamma^N < 1+\eta$ since $\Delta\theta > 0$
- **Line 149** [VERBAL] OK — "$\phi(1+\eta) < 1$ when $\phi$ is sufficiently small" — condition is $\phi < 1/(1+\eta)$; baseline $0.5 < 0.667$ satisfies this
- **Line 149** [VERBAL] OK — hedging channel explanation: AI stocks pay off in states where household consumption falls, pushing P/D above non-AI
- **Lines 154–157** [VERBAL] OK — Proposition 2 comparative statics: (i) spread increasing in displacement severity, (ii) increasing in $p$ for large $\gamma$, (iii) decreasing in $\xi$ — all directionally confirmed by table
- **Line 161** [ARITHMETIC] OK — proof of (i): $\phi^{-\gamma}$ increases as $\phi$ decreases; amplification benefits AI more since $\Gamma^{AI} > \Gamma^N$
- **Line 163** [VERBAL] OK — proof of (ii): higher $p$ weights singularity states more; for large $\gamma$, marginal utility effect dominates
- **Line 165** [VERBAL] OK (minor imprecision) — proof of (iii): the convexity argument is directionally correct but slightly incomplete — $A^{AI}$ falls by a larger *absolute* amount than $A^N$ (since the singularity term is larger), and convexity at the higher starting point amplifies this. The proof attributes the result solely to convexity, omitting the first effect. The conclusion is correct; the attribution is compressed but not wrong.
- **Line 170** [REFERENCE] OK — GKP2012 characterized correctly: growth stocks earn lower expected returns hedging displacement from new cohort entry; contrast with discrete singularity is accurate
- **Line 172** [REFERENCE] OK — "future innovators' rents cannot be traded because the innovators have not yet entered the economy" — exact match to GKP2012

## Quantitative Analysis (lines 177–194)
- **Line 177** — section header
- **Line 186** [ASSUMPTION] OK — all parameter values ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$) match R code exactly
- **Line 186** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; household consumption falls by 25%
- **Line 188** [FIGURE/TABLE] OK — "AI stocks trade at a P/D of roughly 18" at $p=0.5\%$, $\xi=0\%$ — table shows 17.5; "roughly 18" is appropriate rounding
- **Line 188** [FIGURE/TABLE] OK — "non-AI stocks trade near 11" — table shows 11.1
- **Line 188** [FIGURE/TABLE] OK — "a ratio of about 1.6" — table shows exactly 1.6
- **Line 188** [FIGURE/TABLE] OK — "At $p=1\%$, the ratio rises to nearly 6 to 1" — table shows 5.8 at $\xi=0\%$; "nearly 6" is accurate
- **Line 188** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium" — confirmed across all $\xi$ rows: ratio rises monotonically with $p$
- **Line 188** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium" — confirmed: at $p=1\%$, AI drops 76.4→31.0, Non-AI drops 13.3→12.0, ratio drops 5.8→2.6 as $\xi$ rises from 0% to 20%
- **Line 188** [REFERENCE] OK — "as Proposition 2(iii) predicts" — cross-reference verified: Prop 2(iii) states the spread and ratio decrease in $\xi$
- **Line 190** [FIGURE/TABLE] OK — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015" — actual outperformance is approximately 55%; "roughly 50%" is a reasonable round figure
- **Line 190** [ARITHMETIC] OK — "1.5 to 6 times higher … across annual singularity probabilities in the 0.5–1% range" — table confirms: minimum ratio is 1.4 (at $p=0.5\%$, $\xi=20\%$) and maximum is 5.8 (at $p=1\%$, $\xi=0\%$); the stated "1.5 to 6" accurately spans this range

## Extensions: Market Incompleteness and the Singularity (lines 195–257)
- **Line 195** — section header
- **Line 197** [VERBAL] OK — accurately previews two extensions: AI development distortions and government policy
- **Line 201** [DEFINITION] OK — positive singularity: $\alpha_{t+1} = \min(1, \alpha_t/\phi)$; negative: $\alpha_{t+1} = \phi\alpha_t$; positive is more likely; social efficiency defined
- **Line 203** [ARITHMETIC] OK — CRRA utility is negative for $c > 0$ when $\gamma > 1$: $u(c) = c^{1-\gamma}/(1-\gamma)$ with $(1-\gamma) < 0$, so $u(c) < 0$. Normalization $U_{ext} = 0$ makes veto result conservative (extinction less bad than continued negative utility)
- **Line 203** [REFERENCE] OK — Jones 2024 normalization attribution is appropriate
- **Lines 205–208** [VERBAL] OK — Proposition 3: (i) veto under incomplete markets with high $\gamma$; (ii) no veto under complete markets — both logically sound
- **Lines 212–216** [VERBAL] OK — proof logic: under incomplete markets, high $\gamma$ makes downside dominate; under complete markets, household internalizes social surplus
- **Line 218** [VERBAL] OK — extinction risk interaction with veto correctly characterized under conservative normalization
- **Line 222** [REFERENCE] OK (mild imprecision) — "GKP note that intergenerational transfers could in principle affect the magnitude of displacement risk, while observing that such transfers do not alter the functional form of the SDF" — GKP abstract from transfers entirely; the paper's characterization is a reasonable economic inference but not a direct GKP claim. Not materially wrong.
- **Line 224** [DEFINITION] OK — tax rate $\tau \in [0,1)$, deadweight cost fraction $\delta\tau$ — internally consistent
- **Lines 226–228** [ARITHMETIC] OK — equation (7) verified: first term is displaced household consumption $\phi\alpha(1+\eta)C_t(1+g)$; second term is net transfer $\tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$
- **Line 232** [ARITHMETIC] OK — $\phi_{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$ verified: factoring $\alpha(1+\eta)(1+g)C_t$ out of equation (7) yields this exactly
- **Lines 236–238** [ARITHMETIC] OK — equation (8): $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$ verified; $(1+\eta)$ cancels, making ratio independent of $\eta$
- **Line 240** [VERBAL] OK — "ratio exceeds one whenever $\tau > 0$" — for $\tau \in (0,1)$ and $\delta = 0.5$: $(1-\delta\tau) > 0$, $(1-\phi\alpha) > 0$, $\phi\alpha > 0$, so added term is strictly positive
- **Line 242** [ASSUMPTION] OK — $\alpha = 0.70$, $p = 0.5\%$, $\xi = 5\%$ confirmed against R code (lines 108, 127–128)
- **Line 242** [ASSUMPTION] OK — baseline $\eta = 0.5$, $\phi = 0.5$; large singularity $\eta = 9$, $\phi = 0.05$ — confirmed against R code
- **Line 242** [ARITHMETIC] OK — "ten-fold growth": $(1+\eta) = 10$ for $\eta = 9$
- **Line 242** [ARITHMETIC] OK — large singularity $\phi(1+\eta) = 0.05 \times 10 = 0.5$; "consumption halves" — 50% drop, correct
- **Line 242** [ARITHMETIC] OK — baseline $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; "falls by 25%" — correct
- **Line 244** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 160{,}000$ — verified
- **Line 244** [VERBAL] OK — "P/D ratio is undefined at $\tau=0$" for the large singularity — R code returns NA when $K \geq 1$; confirmed by figure annotation "$P/D \to \infty$ as $\tau \to 0$"
- **Line 244** [VERBAL] OK — "existence condition is violated because the household's marginal utility in the singularity state is so extreme that the pricing sum diverges" — correct economic interpretation of $A^j \geq 1$
- **Lines 248–249** [FIGURE/TABLE] OK — caption parameters ($\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$) all confirmed against R code
- **Line 253** [REFERENCE] OK — Jones 2024 and Nordhaus 2021 cited for explosive output growth — appropriate

## Conclusion (lines 258–268)
- **Line 258** — section header
- **Line 260** [VERBAL] OK — "AI stocks trade at high valuations … hedging motive" — established in Sections 2–3
- **Line 260** [VERBAL] OK — "requires market incompleteness" — established in Section 2.3 (line 172: "valuation spread would collapse" under complete markets)
- **Line 260** [VERBAL] OK — "attenuated by extinction risk" — established by Proposition 2(iii) and table data
- **Line 260** [VERBAL] OK — "risk-averse households may inefficiently block AI development" — established by Proposition 3(i)
- **Line 260** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough" — established by equation (8) and Section 4.2
- **Line 262** [VERBAL] OK — self-characterization of model simplicity; consistent with actual model (discrete-time, representative household, no production side)

## Proof of Proposition 1 (lines 269–298)
- **Line 269** — appendix header
- **Lines 271–274** [DEFINITION] OK — Euler equation $P_t^j = \mathbb{E}_t[\beta(c_{t+1}^H/c_t^H)^{-\gamma}(P_{t+1}^j + D_{t+1}^j)]$ is standard CRRA; uses household SDF consistent with Section 2.2
- **Line 277** [VERBAL] OK — stationarity of P/D ratio before any singularity: $\alpha$ and $\theta$ are constant, so the problem is time-homogeneous
- **Line 280** [ARITHMETIC] OK — no singularity: $c_{t+1}^H/c_t^H = (1+g)$ since $\alpha$ unchanged, $C_{t+1} = (1+g)C_t$; $D_{t+1}^{AI}/D_t^{AI} = (1+g)$ since $\theta$ unchanged
- **Line 281** [ARITHMETIC] OK — non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$ since $\alpha_{t+1}=\phi\alpha_t$, $C_{t+1}=(1+\eta)(1+g)C_t$; $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$ since $\theta_{t+1} = \theta+\Delta\theta(1-\theta)$, $C_{t+1} = (1+\eta)(1+g)C_t$
- **Line 282** [VERBAL] OK — extinction: payoff is zero; handled through Jones normalization ($U_{ext}=0$)
- **Lines 286–288** [ARITHMETIC] OK — Euler equation expansion verified: each state's contribution correctly computed with SDF and dividend growth
- **Line 291** [VERBAL] OK — approximation $v^{AI}_{post} \approx v^{AI}$ is honestly disclosed; exact when $\Delta\theta \to 0$; accurate for small $\Delta\theta$
- **Lines 293–294** [ARITHMETIC] OK — solving $v = A(v+1)$ gives $v = A/(1-A)$; formula matches equation (4) from Proposition 1
- **Line 297** [VERBAL] OK — non-AI derivation is identical by symmetry, replacing $\Gamma^{AI}$ with $\Gamma^N$
