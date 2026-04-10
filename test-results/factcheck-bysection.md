# tests/factcheck-bysection.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 6m 21s
[ralph-garage/agent-logs/20260409T215056.132121-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T215056.132121-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong.

## Introduction (lines 38–68)

- **Line 38** — section header
- **Line 40** [FIGURE/TABLE] OK — NASDAQ outpacing S&P 500 since 2015 is confirmed by Figure 1 (fig-ai-valuations.pdf), which shows NASDAQ (solid) ending near ~500 vs S&P 500 (dashed) near ~330, both normalized to Jan 2015 = 100
- **Line 40** [VERBAL] OK — "gap widening sharply since 2023" is visible in the figure, consistent with the generative AI boom timeline
- **Line 44** [FIGURE/TABLE] OK — caption correctly describes the figure content (NASDAQ solid, S&P 500 dashed, normalized to Jan 2015 = 100, sources FRED and Shiller)
- **Line 49** [VERBAL] OK — "AI stocks serve as a hedge against a negative AI singularity" is the paper's main argument, supported by Proposition 1 and the comparison of Γ^AI > Γ^N
- **Line 49** [VERBAL] OK — "If markets were complete, investors could insure directly" supported by model (Section 2.3, line 170) and Proposition 3(ii)
- **Line 49** [VERBAL] OK — "Market incompleteness forces investors into publicly traded AI stocks as an imperfect substitute" supported by model mechanism throughout
- **Line 51** [REFERENCE] OK — GKP2012 correctly cited for the idea that technological displacement creates a systematic risk factor under incomplete markets
- **Line 51** [REFERENCE] OK — GKP2012 correctly described as showing rents accrue to agents current investors cannot trade with
- **Line 53** [VERBAL] OK — "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks" supported by Table 1 (ratio = 2.0 at p=1%, ξ=0%); "can reach" appropriately hedges the claim
- **Line 53** [REFERENCE] OK — Jones2024 correctly cited for extinction risk; the characterization that powerful-AI states carry highest existential risk matches Jones's central thesis
- **Line 53** [VERBAL] OK — "extinction risk attenuates this gap" confirmed by Proposition 2(iii) and Table 1 (ratios decrease as ξ increases)
- **Line 53** [VERBAL] OK — "risk-averse household that cannot hedge displacement may rationally choose to block it" supported by Proposition 3(i)
- **Line 53** [VERBAL] OK — "Complete markets would eliminate this distortion" supported by Proposition 3(ii)
- **Line 55** [REFERENCE] OK — GKP2012 correctly cited for the point that future innovators' capital cannot yet be traded
- **Line 55** [REFERENCE] OK — Jones2024 correctly cited for explosive output growth in a singularity
- **Line 55** [VERBAL] OK — "even grossly inefficient redistribution delivers large consumption gains" supported by Extension 2 analysis (equation 7 and surrounding discussion)
- **Line 55** [VERBAL] OK — footnote accurately describes the paper's production process (AI agents produced analysis and writing from human-authored specification)
- **Line 60** [REFERENCE] OK — GKP2012 correctly described as developing a general-equilibrium model with displacement risk under incomplete markets and OLG structure
- **Line 60** [REFERENCE] OK — "displacement risk is distinct from aggregate consumption risk" and "growth stocks provide a partial hedge" are accurate characterizations of GKP2012
- **Line 62** [REFERENCE] OK — Jones2024 correctly described as studying the trade-off between AI-driven growth and existential risk with bounded utility functions
- **Line 62** [VERBAL] OK — "extinction risk interacts with displacement in a countervailing way, attenuating rather than amplifying the valuation premium" confirmed by Proposition 2(iii)
- **Line 64** [REFERENCE] OK — KoganPapanikolaou2014 and KoganPapanikolaouStoffman2020 correctly cited for technology shocks, creative destruction, and cross-sectional return differences
- **Line 64** [REFERENCE] OK — Knesl2023 correctly cited for empirical evidence on automation-driven displacement risk premium
- **Line 64** [REFERENCE] OK — AghionJonesJones2019 correctly cited for studying whether AI can sustain exponential growth
- **Line 64** [REFERENCE] OK — Acemoglu2024 correctly cited as arguing aggregate AI productivity gains may be modest
- **Line 64** [REFERENCE] OK — Barro2006 and Wachter2013 correctly cited for rare disasters methodology
- **Line 64** [REFERENCE] OK — PastorVeronesi2009 correctly cited for technological revolutions and stock prices

## Model (lines 69–174)

- **Line 69** — section header
- **Line 73** [VERBAL] OK — AI owners described as analogous to GKP2012's future capital owners; paper correctly notes it does not model entry dynamics
- **Line 76–80** [DEFINITION] OK — aggregate consumption growth $C_{t+1} = (1+g)C_t$ absent singularity; standard and internally consistent
- **Line 82** [DEFINITION] OK — household consumption $c_t^H = \alpha_t C_t$; AI owners receive $(1-\alpha_t)C_t$; partitions aggregate consumption
- **Line 85** [ASSUMPTION] OK — singularity probability $p$ per period; $\alpha_t$ unchanged absent singularity
- **Line 88–91** [DEFINITION] OK — non-extinction singularity: aggregate consumption jumps by $1+\eta$; household share drops to $\phi\alpha_t$
- **Line 93** [REFERENCE] OK — Jones2024 correctly cited for the connection between AI power and existential risk
- **Line 102** [DEFINITION] OK — AI dividends $D_t^{AI} = \theta_t C_t$; upon singularity $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$
- **Line 103** [DEFINITION] OK — non-AI dividends $D_t^N = (1-\theta_t)C_t$; dividends sum to aggregate consumption ($D^{AI}+D^N = C_t$)
- **Line 106** [VERBAL] OK — market incompleteness from restricted AI equity correctly described
- **Line 109** [DEFINITION] OK — CRRA preferences with $\gamma > 1$, $\beta \in (0,1)$; equation (3) is standard
- **Line 123–124** [ARITHMETIC] OK — P/D ratio for AI stocks (eq. 4) matches derivation in Appendix A; form is $A^{AI}/(1-A^{AI})$
- **Line 127–128** [ARITHMETIC] OK — P/D ratio for non-AI stocks (eq. 5) identical structure with $\Gamma^N$ replacing $\Gamma^{AI}$
- **Line 130** [ARITHMETIC] OK — $\Gamma^{AI} = [\theta + \Delta\theta(1-\theta)]/\theta \cdot (1+\eta)$; with baseline parameters: $(0.15+0.17)/0.15 \times 1.5 = 3.2$
- **Line 130** [ARITHMETIC] OK — $\Gamma^N = [1-\theta-\Delta\theta(1-\theta)]/(1-\theta) \cdot (1+\eta)$; simplifies to $(1-\Delta\theta)(1+\eta) = 0.8 \times 1.5 = 1.2$; is $\theta$-independent
- **Line 138–142** [VERBAL] OK — existence condition $A^j < 1$ correctly stated; when $A^j \geq 1$ the pricing sum diverges
- **Line 142** [VERBAL] OK — baseline calibration satisfies $A^j < 1$ confirmed by all finite P/D values in Table 1
- **Line 142** [REFERENCE] OK — cross-reference to Section 4.2 (label sec:ext2) correctly points to Government transfers subsection
- **Line 145** [VERBAL] OK — closed-form approximation (post-singularity P/D = pre-singularity P/D) correctly disclosed; exact when $\Delta\theta \to 0$
- **Line 145** [REFERENCE] OK — Table 1 described as numerically exact via backward recursion; confirmed by code implementation
- **Line 147** [ARITHMETIC] OK — $\Gamma^{AI} > 1+\eta$: since $\Delta\theta > 0$, AI dividend share grows, so $\Gamma^{AI} = 3.2 > 1.5 = 1+\eta$
- **Line 147** [ARITHMETIC] OK — $\Gamma^N < 1+\eta$: non-AI share shrinks, $\Gamma^N = 1.2 < 1.5 = 1+\eta$
- **Line 147** [VERBAL] OK — "high marginal utility in singularity states due to displacement, $\phi(1+\eta) < 1$ when $\phi$ is sufficiently small": with baseline $\phi=0.5$, $\phi(1+\eta) = 0.75 < 1$, confirmed
- **Line 147** [VERBAL] OK — hedging channel explanation: AI stocks pay off when household consumption falls; economically sound and consistent with the formulas
- **Line 152** [VERBAL] OK — Proposition 2(i): spread increasing in displacement severity (decreasing $\phi$); proof logic is sound (lower $\phi$ raises $\phi^{-\gamma}$, amplifying AI stocks more since $\Gamma^{AI} > \Gamma^N$)
- **Line 153** [VERBAL] OK — Proposition 2(ii): spread increasing in $p$ for $\gamma$ sufficiently large; proof logic is sound
- **Line 154** [VERBAL] OK — Proposition 2(iii): spread decreasing in $\xi$; proof uses convexity of $A/(1-A)$
- **Line 163** [ARITHMETIC] OK — $f(A) = A/(1-A)$ is increasing and convex for $A \in (0,1)$: $f''(A) = 2/(1-A)^3 > 0$
- **Line 163** [VERBAL] OK — since $A^{AI} > A^N$ (because $\Gamma^{AI} > \Gamma^N$), convexity implies $f(A^{AI})$ falls more, narrowing the spread; confirmed by Table 1 (at p=1%: ratio falls from 2.0 to 1.7 as $\xi$ goes 0% to 20%)
- **Line 168** [REFERENCE] OK — GKP2012 correctly described for growth stocks hedging displacement risk
- **Line 168** [VERBAL] OK — distinction between GKP's continuous displacement from expanding variety vs. this paper's discrete singularity is accurate
- **Line 170** [REFERENCE] OK — GKP2012's point about future innovators' rents correctly echoed
- **Line 170** [VERBAL] OK — correctly notes the paper does not model entry dynamics central to GKP's framework

## Quantitative Analysis (lines 175–192)

- **Line 175** — section header
- **Line 184** [ASSUMPTION] OK — parameters $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$ match Table 1 footnote exactly
- **Line 184** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; correctly stated
- **Line 184** [VERBAL] OK — "household consumption falls by 25%": $1 - 0.75 = 0.25$; correct
- **Line 184** [VERBAL] OK — "aggregate consumption rises by 50%": $\eta = 0.5$ means factor $1.5$; correct
- **Line 184** [ASSUMPTION] OK — "AI stocks are initially 15% of the economy": $\theta = 0.15$; correct
- **Line 184** [ASSUMPTION] OK — "AI's share jumps by 20% of the non-AI remainder": $\Delta\theta = 0.2$; correct
- **Line 186** [FIGURE/TABLE] OK — "P/D of roughly 16" for AI at $p=0.5\%$, $\xi=0\%$: Table 1 shows 15.5; "roughly 16" is at the edge but defensible (15.5 rounds to 16)
- **Line 186** [FIGURE/TABLE] OK — "non-AI stocks trade near 11": Table 1 shows 11.1 at $p=0.5\%$, $\xi=0\%$; correct
- **Line 186** [FIGURE/TABLE] OK — "ratio of about 1.4": Table 1 shows 1.4; exact match
- **Line 186** [FIGURE/TABLE] OK — "At $p=1\%$, the ratio rises to 2": Table 1 shows 2.0 at $p=1\%$, $\xi=0\%$; exact match
- **Line 186** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium": confirmed by Table 1 (ratio monotonically increases from 1.1 to 2.0 across $p$ values at $\xi=0\%$)
- **Line 186** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium": confirmed by Table 1 (at $p=1\%$: AI P/D falls 26.5→20.5, non-AI 13.3→12.0, ratio 2.0→1.7 as $\xi$ goes 0%→20%)
- **Line 186** [REFERENCE] OK — "as Proposition 2(iii) predicts" correctly references the extinction comparative static
- **Line 188** [FIGURE/TABLE] OK — "NASDAQ has appreciated roughly 50% more than S&P 500 since 2015": Figure 1 shows NASDAQ ending near ~500 and S&P 500 near ~330 (normalized to 100); ratio ≈ 1.52, so "roughly 50% more" is accurate
- **Line 188** [FIGURE/TABLE] OK — "P/D ratios 1.3 to 2 times" for $p \in [0.5\%, 1\%]$: Table 1 confirms range from 1.3 (at $p=0.5\%$, $\xi=10\%$ or $20\%$) to 2.0 (at $p=1\%$, $\xi=0\%$)

## Extensions: Market Incompleteness and the Singularity (lines 193–261)

- **Line 193** — section header
- **Line 195** [VERBAL] OK — framing correctly previews Extension 1 (distortion of AI development) and Extension 2 (government policy)
- **Line 199** [DEFINITION] OK — positive singularity: $\alpha_{t+1} = \min(1, \alpha_t/\phi)$; negative singularity: $\alpha_{t+1} = \phi\alpha_t$; internally consistent inverses
- **Line 199** [ASSUMPTION] OK — "The positive singularity is the more likely outcome" and "AI development is socially efficient" stated as modeling assumptions
- **Line 201** [VERBAL] OK — veto cost described as "significant" representing deadweight loss from government intervention
- **Line 201** [REFERENCE] OK — Jones2024 cited for normalizing extinction utility to zero; consistent with his framework using bounded utility
- **Line 201** [VERBAL] OK — "CRRA utility is negative for all $c > 0$ when $\gamma > 1$" is mathematically correct ($u(c) = c^{1-\gamma}/(1-\gamma) < 0$ for $\gamma > 1$), making the zero-normalization conservative
- **Line 205** [VERBAL] OK — Proposition 3(i): household vetoes even when development is socially efficient; proof logic is sound (concavity of utility makes downside dominate for large $\gamma$)
- **Line 207** [VERBAL] OK — Proposition 3(ii): complete markets eliminates veto; proof logic is sound (household can hedge displacement and participate in full surplus)
- **Line 216** [VERBAL] OK — "higher $\xi$ reduces the weight on non-extinction singularity states, which are the states driving the veto" is logically correct
- **Line 216** [VERBAL] OK — connection to AI regulation debates is appropriately hedged
- **Line 220** [REFERENCE] OK — GKP2012 cited for noting intergenerational transfers could affect displacement risk; this is consistent with GKP's discussion of model abstractions
- **Line 225** [ARITHMETIC] OK — equation (5): $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$; first term is displaced consumption, second is net transfer; algebraically correct
- **Line 228** [VERBAL] OK — "$(1-\phi\alpha)$ represents the AI owners' share of post-singularity aggregate consumption": household gets $\phi\alpha$, remainder is $1-\phi\alpha$; correct
- **Line 233** [ARITHMETIC] OK — equation (6): $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$; verified by factoring equation (5) as $\phi_\text{eff} \cdot \alpha \cdot (1+\eta)(1+g)C_t$
- **Line 236** [VERBAL] OK — "P/D formula from Proposition 1 applies with $\phi$ replaced by $\phi_\text{eff}$" is correct since $\phi_\text{eff}$ enters the SDF identically
- **Line 241** [ARITHMETIC] OK — equation (7): transfer ratio $= 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$; verified by dividing equation (5) by $\phi\alpha(1+\eta)(1+g)C_t$
- **Line 244** [VERBAL] OK — ratio is independent of $\eta$: confirmed algebraically ($\eta$ cancels in numerator and denominator)
- **Line 244** [VERBAL] OK — "as $\eta$ grows, both terms grow without bound, so even inefficient transfers deliver arbitrarily large consumption gains relative to the pre-singularity baseline"; correct in levels
- **Line 246** [ASSUMPTION] OK — extension parameters $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$ stated; match code
- **Line 246** [ASSUMPTION] OK — baseline $\eta=0.5$, $\phi=0.5$; large singularity $\eta=9$, $\phi=0.05$; match code
- **Line 246** [ARITHMETIC] OK — large singularity: $\phi(1+\eta) = 0.05 \times 10 = 0.5$, "consumption halves"; correct
- **Line 246** [ARITHMETIC] OK — baseline: $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$, "falls by 25%"; correct
- **Line 246** [VERBAL] OK — "ten-fold growth" for $\eta=9$: factor is $1+9=10$; correct
- **Line 246** [FIGURE/TABLE] OK — "right panel" refers to Panel (b) for consumption; matches code layout (panel_a left, panel_b right)
- **Line 248** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$; exactly correct
- **Line 248** [VERBAL] OK — P/D undefined at $\tau=0$ under large singularity because existence condition violated ($\phi^{-\gamma}$ so extreme the pricing sum diverges); confirmed by code returning NA
- **Line 248** [VERBAL] OK — "As $\tau$ increases and transfers cushion the displacement, effective displacement falls, the existence condition is restored, and finite P/D ratios emerge"; consistent with code and figure
- **Line 252** [FIGURE/TABLE] OK — caption parameters ($\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$) match code exactly
- **Line 257** [REFERENCE] OK — Jones2024 correctly cited for explosive output growth; Nordhaus2021 correctly cited as examining the economic singularity hypothesis critically

## Conclusion (lines 262–272)

- **Line 262** — section header
- **Line 264** [VERBAL] OK — "AI stocks trade at high valuations" supported by Figure 1 and Table 1
- **Line 264** [VERBAL] OK — "part of this premium reflects a hedging motive" is the paper's main argument, supported by Proposition 1 and the Γ^AI > Γ^N comparison; "part" is appropriately hedged
- **Line 264** [VERBAL] OK — "requires market incompleteness---the inability to trade restricted AI equity" supported by Section 2.1 (line 106) and Section 2.3 (line 170)
- **Line 264** [VERBAL] OK — "attenuated by extinction risk, which reduces the weight on the non-extinction states where the hedging channel operates" supported by Proposition 2(iii) and Table 1
- **Line 264** [VERBAL] OK — "risk-averse households may inefficiently block AI development" supported by Proposition 3(i); "may" correctly reflects the condition ($\gamma$ sufficiently large)
- **Line 264** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough to overwhelm deadweight costs" supported by Extension 2 analysis (equations 5–7 and Figure 2)
- **Line 266** [VERBAL] OK — "Our model is deliberately simple" and listed abstractions (continuous-time dynamics, heterogeneous beliefs, production-side details) are accurate descriptions of what the model omits

## Proof of Proposition 1 (lines 273–302)

- **Line 273** — section header; cross-reference labels (prop:pd-ratios, app:proof-pd) match those in Proposition 1 and the proof stub
- **Line 278** [DEFINITION] OK — Euler equation $P_t^j = \mathbb{E}_t[\beta(c_{t+1}^H/c_t^H)^{-\gamma}(P_{t+1}^j + D_{t+1}^j)]$ is standard CRRA, consistent with preferences in equation (3)
- **Line 281** [VERBAL] OK — P/D ratio $v^{AI}$ constant in stationary pre-singularity equilibrium; correct since all state variables are stationary
- **Line 284** [ARITHMETIC] OK — no singularity: $c_{t+1}^H/c_t^H = 1+g$ (α unchanged, C grows by $1+g$); $D_{t+1}^{AI}/D_t^{AI} = 1+g$ (θ unchanged, C grows by $1+g$)
- **Line 285** [ARITHMETIC] OK — non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$ (α→φα, C→$(1+g)(1+\eta)$C); $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$ (θ→θ+Δθ(1-θ), C→$(1+g)(1+\eta)$C)
- **Line 286** [VERBAL] OK — extinction: $c_{t+1}^H = 0$, payoff is zero; correct
- **Lines 290–293** [ARITHMETIC] OK — Euler equation expansion verified: $\beta(1+g)^{-\gamma}$ correctly factored out; no-singularity contribution $(1-p)(1+g)(v+1)D$ correct; non-extinction contribution $p(1-\xi)[\phi(1+\eta)]^{-\gamma}(1+g)\Gamma^{AI}(v+1)D$ correct
- **Line 295** [ARITHMETIC] OK — $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is $\theta$-independent: $[(1-\theta)(1-\Delta\theta)]/(1-\theta) = 1-\Delta\theta$; verified. Implication that non-AI closed form is exact is correct.
- **Line 295** [VERBAL] OK — post-singularity P/D approximated by $v^{AI}$; exact as $\Delta\theta \to 0$ since $\Gamma^{AI} \to 1+\eta$ becomes $\theta$-independent
- **Line 295** [VERBAL] OK — backward recursion over chain $\theta_0, \theta_1, \ldots$ for numerically exact values; terminal approximation error vanishes as $\theta \to 1$; standard and correct
- **Lines 297–299** [ARITHMETIC] OK — solved P/D ratio $v = A/(1-A)$ where $A = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$; derivation verified: $v = A(v+1) \Rightarrow v(1-A) = A \Rightarrow v = A/(1-A)$
- **Line 301** [VERBAL] OK — equation (12) is algebraically identical to equation (4) in Proposition 1
- **Line 301** [VERBAL] OK — non-AI derivation identical with $\Gamma^N$ replacing $\Gamma^{AI}$; straightforward and exact (since $\Gamma^N$ is $\theta$-independent)
