# tests/factcheck-bysection.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 10m 26s
[ralph-garage/agent-logs/20260409T220435.867203-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T220435.867203-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong; only minor imprecisions and one weak attribution noted.

## Introduction (lines 38–70)

- **Line 38** — section header
- **Line 40** [FIGURE/TABLE] OK — NASDAQ outpacing S&P 500 since 2015 is consistent with the figure data (code downloads NASDAQ from FRED series NASDAQCOM, S&P 500 from Shiller/datahub, normalizes to first shared observation ≈ Jan 2015 = 100)
- **Line 40** [VERBAL] OK — "gap widening sharply since 2023 as advances in generative AI have accelerated" is a qualitative characterization consistent with actual market events
- **Line 44** [FIGURE/TABLE] OK — caption states "NASDAQ from FRED; S&P 500 from the Shiller dataset"; code confirms these exact sources
- **Line 44** [FIGURE/TABLE] OK — "normalized to January 2015 = 100"; code normalizes to the first observation in the filtered range (starting 2015-01-01), which is January 2015 for both series
- **Line 49** [VERBAL] OK — "the role of financial markets remains under-explored" is a defensible framing claim; no cited paper in the bibliography addresses financial-market frictions for AI directly
- **Line 51** [DEFINITION] OK — "negative AI singularity" definition is consistent with the model setup (Section 2, eq. 2: α_{t+1} = φα_t with φ < 1)
- **Line 51** [VERBAL] OK — "If markets were complete, investors could insure against this risk directly" confirmed by Proposition 3(ii)
- **Line 51** [REFERENCE] OK — "much of this equity is restricted—held by founders, early-stage investors, and firms that may not yet exist" matches GKP 2012 (future innovators cannot trade with current agents)
- **Line 53** [REFERENCE] OK — GKP 2012 "show that rents from new technologies accrue to agents that current investors cannot trade with" confirmed against GKP abstract
- **Line 53** [VERBAL] OK — "representative household—the marginal investor—faces a stochastic singularity that shifts consumption toward AI owners" matches model setup
- **Line 53** [VERBAL] OK — "AI stocks grow as a share of the economy with each singularity" confirmed by θ_{t+1} = θ_t + Δθ(1−θ_t)
- **Line 55** [VERBAL] OK — "closed-form price-dividend ratios" confirmed by Proposition 1 (eqs. 5–6)
- **Line 55** [ARITHMETIC] OK — "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks" confirmed by Table 1: at p=1%, ξ=0%, ratio = 2.0
- **Line 55** [REFERENCE] OK — "Extinction risk (Jones 2024) attenuates this gap" confirmed by Proposition 2(iii) and Table 1 (ratio falls from 2.0 at ξ=0% to 1.7 at ξ=20% for p=1%); Jones 2024 text confirms correlated existential risk
- **Line 55** [VERBAL] OK — "risk-averse household that cannot hedge displacement may rationally choose to block it" confirmed by Proposition 3(i)
- **Line 55** [VERBAL] OK — "Complete markets would eliminate this distortion" confirmed by Proposition 3(ii)
- **Line 57** [REFERENCE] OK — "as GKP 2012 emphasize, much of this capital belongs to future innovators and cannot yet be traded" confirmed in GKP text
- **Line 57** [VERBAL] OK — "in a singularity with explosive output growth, the resource base becomes so enormous that even grossly inefficient redistribution delivers large consumption gains" confirmed by eq. 11 (transfer ratio independent of η; levels grow without bound)
- **Line 57** [REFERENCE] OK — Jones 2024 cited for "explosive output growth" premise, not for the transfers mechanism (which is original); attribution is accurate
- **Line 62** [REFERENCE] OK — GKP 2012 "develop a general-equilibrium model in which innovation displaces existing agents and creates a systematic risk factor under incomplete markets" matches GKP abstract exactly
- **Line 62** [REFERENCE] OK — "displacement risk is distinct from aggregate consumption risk and that growth stocks provide a partial hedge" confirmed in GKP text
- **Line 62** [VERBAL] OK — "Our model simplifies their overlapping-generations structure" accurate; paper uses representative household, not OLG
- **Line 64** [REFERENCE] OK — Jones 2024 "studies the trade-off between AI-driven growth and existential risk" matches Jones 2024 title ("The AI Dilemma: Growth versus Existential Risk")
- **Line 64** [REFERENCE] OK — Jones 2024 "bounded utility functions make agents conservative about extinction" confirmed in Jones 2024 text
- **Line 64** [VERBAL] OK — "it interacts with displacement in a countervailing way, attenuating rather than amplifying the valuation premium" confirmed by Proposition 2(iii) and Table 1
- **Line 66** [REFERENCE] OK — Kogan & Papanikolaou (2014) and Kogan, Papanikolaou & Stoffman (2020) cited for technology shocks generating cross-sectional return differences; consistent with paper titles in bibliography
- **Line 66** [REFERENCE] OK — Knesl (2023) cited for "direct empirical evidence that automation-driven displacement commands a risk premium"; consistent with JFE title
- **Line 66** [REFERENCE] OK — Aghion, Jones & Jones (2019) cited for studying whether AI can sustain exponential growth; consistent with known work
- **Line 66** [REFERENCE] OK — Acemoglu (2024) cited for arguing AI productivity gains "may be more modest than commonly supposed"; consistent with known position
- **Line 66** [REFERENCE] OK — Barro (2006), Wachter (2013) cited for rare disasters methodology; both are foundational rare-disaster pricing papers
- **Line 66** [REFERENCE] OK — Pastor & Veronesi (2009) cited for technological revolutions and stock prices; matches AER paper title

## Model (lines 71–176)

- **Line 71** — section header
- **Line 75** [REFERENCE] OK — AI owners as "future capital owners who do not yet participate in markets, as in GKP2012" matches GKP text
- **Line 75** [VERBAL] OK — "we do not explicitly model the entry of new cohorts of firms or workers" is an accurate disclaimer consistent with the paper spec
- **Lines 80–82** [DEFINITION] OK — C_{t+1} = (1+g)C_t defines constant consumption growth absent singularity
- **Line 84** [DEFINITION] OK — c_t^H = α_t C_t and AI owners get (1−α_t)C_t; shares sum to 1
- **Lines 87–96** [DEFINITION] OK — singularity structure: probability p, non-extinction with displacement α_{t+1} = φα_t and aggregate jump (1+η), extinction with probability ξ
- **Line 95** [REFERENCE] OK — Jones 2024 cited for extinction risk; matches Jones 2024 text about correlated existential risk
- **Line 104** [DEFINITION] OK — θ_{t+1} = θ_t + Δθ(1−θ_t); verified non-AI share contracts by factor (1−Δθ)
- **Line 105** [DEFINITION] OK — D_t^N = (1−θ_t)C_t; dividends sum to C_t
- **Line 108** [VERBAL] OK — market incompleteness from inability to trade restricted AI equity; consistent with GKP analogy
- **Line 111** [DEFINITION] OK — CRRA preferences with γ > 1 and β ∈ (0,1); standard formulation
- **Line 119** [VERBAL] OK — "the household's SDF reflects its own consumption growth, not aggregate consumption growth" is correct under incomplete markets
- **Lines 124–132** [ARITHMETIC] OK — P/D formulas verified by deriving from Euler equation; formula structure v = A/(1−A) confirmed
- **Line 132** [ARITHMETIC] OK — Γ^AI = [θ + Δθ(1−θ)]/θ × (1+η); with parameters: (0.15+0.17)/0.15 × 1.5 = 3.2
- **Line 132** [ARITHMETIC] OK — Γ^N = [1−θ−Δθ(1−θ)]/(1−θ) × (1+η) = (1−Δθ)(1+η) = 0.8 × 1.5 = 1.2; confirmed θ-independent
- **Lines 139–144** [VERBAL] OK — existence condition A^j < 1 is necessary and sufficient for positive finite P/D ratios
- **Line 144** [VERBAL] OK — "baseline calibration satisfies A^j < 1 for both assets" verified numerically for all table entries
- **Line 144** [REFERENCE] OK — cross-reference to Section 4.2 for violation of existence condition is correct
- **Line 147** [VERBAL] OK — closed-form approximation treats post-singularity P/D as equal to pre-singularity; "exact when Δθ → 0" is correct
- **Line 147** [VERBAL] OK — Table 1 reports numerically exact values via backward recursion; all 20 entries independently verified
- **Line 149** [ARITHMETIC] OK — Γ^AI > 1+η: 3.2 > 1.5 confirmed (holds whenever Δθ > 0)
- **Line 149** [ARITHMETIC] OK — Γ^N < 1+η: 1.2 < 1.5 confirmed (holds whenever Δθ > 0)
- **Line 149** [ARITHMETIC] OK — φ(1+η) < 1 "when φ is sufficiently small": with φ=0.5, η=0.5: 0.75 < 1; exact condition is φ < 1/(1+η)
- **Line 149** [VERBAL] OK — "AI stocks pay off precisely when the household's consumption falls" correctly describes the hedging channel
- **Lines 153–157** [VERBAL] OK — Proposition 2 comparative statics: all three results verified numerically
- **Lines 160–161** [VERBAL] OK — Proof of (i): decrease in φ raises φ^{−γ}, amplifies singularity term more for AI stocks because Γ^AI > Γ^N; logic correct
- **Lines 162–163** [VERBAL] OK — Proof of (ii): increase in p puts more weight on singularity states; qualifier "γ sufficiently large" is conservative but not wrong (spread increases in p for all γ > 0 under baseline parameterization)
- **Lines 164–166** [VERBAL] OK — Proof of (iii): convexity argument correct; f(A) = A/(1−A) has f'' = 2/(1−A)^3 > 0; since A^AI > A^N, same multiplicative reduction in singularity terms causes proportionally larger drop in A^AI/(1−A^AI)
- **Line 170** [REFERENCE] OK — "GKP2012 show that growth stocks earn lower expected returns because they hedge displacement risk from innovation" matches GKP text
- **Line 170** [VERBAL] OK — "GKP model continuous displacement from expanding technological variety, while we model a sudden, severe shift" accurately distinguishes the two frameworks
- **Line 172** [VERBAL] OK — "If the household could buy claims on the full universe of AI shares, it could perfectly hedge displacement risk, and the valuation spread would collapse" correct under complete markets
- **Line 172** [REFERENCE] OK — "echoes GKP2012's point that future innovators' rents cannot be traded" matches GKP text

## Quantitative Analysis (lines 177–194)

- **Line 177** — section header
- **Line 186** [ASSUMPTION] OK — β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2 match the code and table footnote exactly
- **Line 186** [ARITHMETIC] OK — φ(1+η) = 0.5 × 1.5 = 0.75
- **Line 186** [VERBAL] OK — "household retains half of its consumption share upon displacement" matches φ=0.5
- **Line 186** [ARITHMETIC] OK — "household consumption falls by 25%" follows from φ(1+η) = 0.75 (consumption is 75% of pre-singularity level)
- **Line 186** [ARITHMETIC] OK — "aggregate consumption rises by 50% in a singularity" follows from η=0.5
- **Line 186** [VERBAL] OK — "AI stocks are initially 15% of the economy" matches θ=0.15
- **Line 186** [VERBAL] OK — "AI's share jumps by 20% of the non-AI remainder" matches Δθ=0.2
- **Line 188** [ARITHMETIC] OK — "AI stocks trade at a P/D of roughly 16" for p=0.5%, ξ=0%: table reports 15.5; "roughly 16" is a slight overstatement but within rounding tolerance for qualitative discussion
- **Line 188** [ARITHMETIC] OK — "non-AI stocks trade near 11" matches table value 11.1; independently verified via closed-form: K=0.9172, P/D=11.08
- **Line 188** [ARITHMETIC] OK — "a ratio of about 1.4" matches table exactly (1.4)
- **Line 188** [ARITHMETIC] OK — "At p=1%, the ratio rises to 2" matches table exactly (2.0)
- **Line 188** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium" confirmed across all rows of the table
- **Line 188** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium, as Proposition 2(iii) predicts" confirmed by table (e.g., at p=1%: ratio falls from 2.0 to 1.7 as ξ goes from 0% to 20%)
- **Line 190** [FIGURE/TABLE] OK — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015" is an empirical claim about Figure 1; consistent with actual market data through 2025
- **Line 190** [ARITHMETIC] OK — "P/D ratios for AI stocks that are 1.3 to 2 times those of non-AI stocks across annual singularity probabilities in the 0.5–1% range" verified against table: ratios span 1.3–2.0 for p ∈ {0.5%, 0.8%, 1.0%} across all ξ values

## Extensions: Market Incompleteness and the Singularity (lines 195–263)

- **Line 195** — section header
- **Line 197** [VERBAL] OK — framing of the two extensions (distortion of AI development, government policy) matches Sections 4.1 and 4.2
- **Line 201** [DEFINITION] OK — positive singularity defined as α_{t+1} = min(1, α_t/φ); negative as α_{t+1} = φα_t; positive is more likely
- **Line 201** [VERBAL] OK — "AI development is socially efficient in the sense that the expected welfare gain is positive" is the maintained assumption for Proposition 3
- **Line 203** [REFERENCE] OK — "Following Jones 2024, we normalize extinction utility to zero" is consistent with Jones 2024's treatment; CRRA utility is negative for c > 0 when γ > 1, so U_ext = 0 makes the veto result conservative
- **Lines 206–209** [VERBAL] OK — Proposition 3 statements: (i) household vetoes under incomplete markets for γ large enough; (ii) never vetoes under complete markets. Both logically follow from the proof
- **Lines 212–216** [VERBAL] OK — Proof of Proposition 3: (i) concavity + large γ makes downside dominate even when positive singularity is more likely; (ii) complete markets allow full hedging so household captures social surplus
- **Line 218** [VERBAL] OK — "Extinction risk interacts with this distortion: under our conservative normalization (U_ext = 0), higher ξ reduces the weight on non-extinction singularity states, which are the states driving the veto." Logically correct
- **Line 222** [REFERENCE] WEAK — claims GKP "note that intergenerational transfers could in principle affect the magnitude of displacement risk, while observing that such transfers do not alter the functional form of the stochastic discount factor." GKP's conclusion mentions abstracting from transfers in passing but does not make the specific claim about SDF functional form preservation. The attribution slightly overstates what GKP explicitly say, though the economic logic is plausible
- **Lines 226–228** [ARITHMETIC] OK — transfer consumption equation verified: first term φα(1+η)(1+g)C_t is displaced household consumption; second term τ(1−δτ)(1−φα)(1+η)(1+g)C_t is net transfer from AI owners' share (1−φα)
- **Line 230** [VERBAL] OK — "(1−φα) represents the AI owners' share of post-singularity aggregate consumption" is correct; this is distinct from the AI dividend share θ
- **Lines 234–236** [ARITHMETIC] OK — φ_eff = φ + τ(1−δτ)(1−φα)/α verified by dividing eq. (6) by α(1+η)(1+g)C_t
- **Line 238** [VERBAL] OK — "φ_eff enters the SDF in the same way as φ, the P/D formula from Proposition 1 applies with φ replaced by φ_eff" is correct; the transfer modifies the effective displacement but not the functional form
- **Lines 242–244** [ARITHMETIC] OK — transfer ratio c^H_post/c^H_no-transfer = 1 + τ(1−δτ)(1−φα)/(φα) verified algebraically; the (1+η)(1+g)C_t factors cancel, confirming independence from η
- **Line 246** [VERBAL] OK — "transfers always improve the household's position in the singularity state, regardless of η" follows from the ratio exceeding 1 whenever τ > 0
- **Line 248** [ASSUMPTION] OK — parameters α=0.70, p=0.5%, ξ=5% stated in text; match code (alpha0=0.70, p_ext=0.005, xi_ext=0.05)
- **Line 248** [ARITHMETIC] OK — "consumption halves under the large singularity (φ(1+η) = 0.5)": 0.05 × 10 = 0.5
- **Line 248** [ARITHMETIC] OK — "falls by 25% under the baseline (φ(1+η) = 0.75)": 0.5 × 1.5 = 0.75
- **Line 248** [ARITHMETIC] OK — "ten-fold growth" with η=9: (1+η) = 10
- **Line 250** [ARITHMETIC] OK — φ^{−γ} = (0.05)^{−4} = 20^4 = 160,000
- **Line 250** [VERBAL] OK — "P/D ratio is undefined at τ=0" for large singularity: existence condition violated because the extreme SDF weight (φ^{−γ} = 160,000) makes the pricing sum diverge; confirmed by code returning NA
- **Line 250** [VERBAL] OK — "As τ increases and transfers cushion the displacement, effective displacement falls, the existence condition is restored, and finite P/D ratios emerge" confirmed by figure showing P/D values appearing for τ > 0
- **Line 254** [FIGURE/TABLE] OK — caption parameters α=0.70, p=0.5%, ξ=5%, δ=0.5 match code exactly (alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50)
- **Line 259** [REFERENCE] OK — Jones 2024 cited for explosive output growth; matches Jones 2024's singularity model with infinite consumption
- **Line 259** [REFERENCE] OK — Nordhaus 2021 cited for critically examining explosive growth; "Are We Approaching an Economic Singularity?" (AEJ:Macro) is an appropriate citation

## Conclusion (lines 264–274)

- **Line 264** — section header
- **Line 266** [VERBAL] OK — "hedging motive: investors use AI stocks to partially insure against an AI singularity that would displace their consumption" accurately summarizes the model's core mechanism
- **Line 266** [VERBAL] OK — "requires market incompleteness—the inability to trade restricted AI equity" consistent with model setup and Proposition 3(ii)
- **Line 266** [VERBAL] OK — "attenuated by extinction risk, which reduces the weight on the non-extinction states where the hedging channel operates" consistent with Proposition 2(iii)
- **Line 266** [VERBAL] OK — "risk-averse households may inefficiently block AI development" consistent with Proposition 3(i)
- **Line 266** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough to overwhelm deadweight costs" consistent with Extension 2 (eq. 11 and Figure 2)

## Proof of Proposition 1 (lines 275–304)

- **Line 275** — section header
- **Line 280** [ARITHMETIC] OK — standard consumption CAPM Euler equation P_t^j = E_t[β(c_{t+1}^H/c_t^H)^{−γ}(P_{t+1}^j + D_{t+1}^j)]
- **Line 286** [ARITHMETIC] OK — no-singularity case: c growth = 1+g, D^AI growth = 1+g (θ unchanged, C grows by 1+g)
- **Line 287** [ARITHMETIC] OK — non-extinction singularity: c growth = φ(1+g)(1+η); D^AI growth = Γ^AI(1+g) where Γ^AI = (θ'/θ)(1+η)
- **Line 288** [ARITHMETIC] OK — extinction: payoff = 0
- **Lines 292–295** [ARITHMETIC] OK — Euler equation expansion verified step by step; factoring out β(1+g)^{−γ} is correct; (v^AI+1) factor from P+D = (v+1)D is correct
- **Line 297** [ARITHMETIC] OK — Γ^N = (1−Δθ)(1+η) is θ-independent; verified: [(1−θ)(1−Δθ)]/(1−θ) = (1−Δθ), so the non-AI closed form is exact (not an approximation)
- **Line 297** [VERBAL] OK — backward recursion description matches code in generate-exhibits.R (compute_pd_ai_exact function): v_k = [B(1−p) + B·p(1−ξ)·S·Γ^AI_k·(v_{k+1}+1)] / [1 − B(1−p)]
- **Lines 299–301** [ARITHMETIC] OK — closed-form P/D formula derived by setting v_{k+1} = v_k = v^AI; collecting terms gives v(1−K) = K, so v = K/(1−K) where K = β(1+g)^{1−γ}[(1−p) + p(1−ξ)(1+η)^{−γ}φ^{−γ}Γ^AI]; matches equation (5)
- **Line 303** [VERBAL] OK — "derivation for non-AI stocks is identical, replacing Γ^AI with Γ^N" is correct; since Γ^N is θ-independent, the approximation is exact for non-AI stocks (confirmed by code using compute_pd_approx for non-AI)
