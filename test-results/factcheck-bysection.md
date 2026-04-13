# tests/factcheck-bysection.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 8m 20s
[ralph-garage/agent-logs/20260412T200023.695053-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.695053-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong; a few minor imprecisions are noted but none rise to the level of error.

## Introduction (lines 38–70)

- **Line 38** — section header
- **Line 40** [VERBAL] OK — Claims S&P 500 P/D has reached "historically elevated levels" and NASDAQ has "sharply outpaced the broader market since 2015, with the valuation gap widening since 2023." Consistent with fig-ai-valuations.pdf data.
- **Line 40** [VERBAL] OK — "advances in generative AI have accelerated expectations" is a contextual motivating claim; no specific statistic asserted.
- **Line 44** [FIGURE/TABLE] OK — Caption accurately describes Panel (a) as S&P 500 trailing P/D from Shiller dataset and Panel (b) as NASDAQ/S&P 500 normalized to Jan 2015 = 100. Sources ("NASDAQ from FRED; S&P 500 from Shiller dataset") match the code.
- **Line 49** [DEFINITION] OK — Definition of negative AI singularity matches spec §I.2b.
- **Line 49** [VERBAL] OK — "relevant AI equity is restricted—held by founders, early-stage investors, and firms that may not yet exist" consistent with model setup (line 110).
- **Line 49** [REFERENCE] OK — GKP2012 citation: "displacing capital often belongs to future innovators who have not yet entered the economy." GKP (p. 492) states: "future innovators, who are yet to enter the economy, are not able to trade with the current population of agents." Accurate paraphrase.
- **Line 49** [VERBAL] OK — "premium that would vanish if markets were complete" is the paper's core mechanism; supported by the discussion at line 169.
- **Line 51** [VERBAL] OK — "closed-form price-dividend ratios" — the paper derives closed-form expressions (Proposition 1) and acknowledges they are approximate for AI stocks; the table uses numerically exact values. Minor imprecision: AI P/D is solved by backward recursion, not purely closed-form. The paper discloses this clearly at line 151, so this is not an error.
- **Line 51** [ARITHMETIC] OK — "at a singularity probability of one percent, P/D ratios for AI stocks roughly double relative to non-AI stocks." Table: p=1%, xi=0 gives AI P/D=26.5, Non-AI P/D=13.3, Ratio=2.0. Verified.
- **Line 51** [REFERENCE] OK — "Extinction risk (Jones 2024) partially offsets this premium": Jones (2024) models AI growth vs. existential risk; Proposition 2 confirms higher xi reduces the valuation ratio. "Partially offsets" is accurate.
- **Line 51** [REFERENCE] OK — "(Proposition~\ref{prop:comp-statics})" — label exists at line 157 and matches the described content.
- **Line 53** [VERBAL] OK — "market incompleteness distorts real decisions—it can distort the development of AI itself" supported by Proposition 3 (prop:veto, line 208).
- **Line 53** [VERBAL] OK — "positive singularity is more likely than the negative one, AI development is socially efficient, yet a risk-averse household may rationally choose to block it" — all supported by Extension 1 setup (q > 1/2) and Proposition 3(i).
- **Line 53** [REFERENCE] OK — "(Proposition~\ref{prop:veto})" — label exists at line 208 and matches.
- **Line 55** [VERBAL] OK — "financial approaches to AI disaster risk are strikingly under-discussed" is a motivating claim consistent with spec §I.3c.
- **Line 55** [VERBAL] OK — "broader trading of AI equity—is blocked by restricted ownership and non-existent future capital" consistent with GKP and model.
- **Line 57** [REFERENCE] OK — "explosive output growth modeled by Jones (2024)" — Jones (2024) explicitly models singularity/explosive growth scenarios.
- **Line 57** [VERBAL] OK — "even grossly inefficient transfers become effective, because the resource base overwhelms the deadweight costs" supported by Extension 2 analysis.
- **Line 59** [REFERENCE] OK — Section references (sec:model, sec:quant, sec:extensions) all exist and match descriptions.
- **Line 59** [VERBAL] OK — Footnote: "All analysis, code, and prose were produced by AI agents; the human contribution was limited to the economic specification and test scripts." Consistent with spec §IV.5c and README.
- **Line 64** [REFERENCE] OK — GKP2012 described as modeling "how innovation displaces existing agents and creates a systematic risk factor under incomplete markets." Accurate summary.
- **Line 64** [VERBAL] OK — "The main insights about displacement risk and incomplete markets originate in their work" — purposefully modest attribution consistent with spec §I.6c.
- **Line 66** [REFERENCE] OK — "Jones (2024) studies the trade-off between AI-driven growth and existential risk." Title is "The AI Dilemma: Growth versus Existential Risk." Accurate.
- **Line 66** [REFERENCE] OK — "We incorporate his extinction channel and show it attenuates rather than amplifies the valuation premium." Proposition 2 confirms attenuation. Correct direction.
- **Line 66** [REFERENCE] OK — Citations to Kogan-Papanikolaou (2014), Kogan-Papanikolaou-Stoffman (2020), Knesl (2023) for "creative destruction and displacement risk premia" — standard grouping in asset pricing literature.
- **Line 66** [REFERENCE] OK — Aghion-Jones-Jones (2019) and Acemoglu (2025) for "macroeconomics of AI growth" — standard citations.
- **Line 66** [REFERENCE] OK — Barro (2006) and Wachter (2013) for "rare disasters literature" — canonical papers.
- **Line 66** [REFERENCE] OK — Pastor-Veronesi (2009) for "technological revolutions" — well-known JF paper.

## Model (lines 71–175)

- **Line 71** — section header
- **Line 75** [REFERENCE] OK — "AI owners can be thought of as future capital owners who do not yet participate in markets, as in GKP2012." GKP (p. 492) confirmed. Caveat about not modeling entry dynamics is stated correctly.
- **Lines 78–82** [DEFINITION] OK — Aggregate consumption growth $C_{t+1} = (1+g)C_t$ absent singularity. Consistent with $g = 0.02$.
- **Line 84** [DEFINITION] OK — $c_t^H = \alpha_t C_t$; AI owners receive $(1-\alpha_t)C_t$. Internally consistent.
- **Lines 87–96** [DEFINITION] OK — Singularity structure: prob $p$; conditional on singularity, non-extinction (prob $1-\xi$, jump $1+\eta$, share $\phi\alpha_t$) or extinction (prob $\xi$, $C=0$ permanently). Well-posed.
- **Line 95** [REFERENCE] OK — Jones (2024) citation for "states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest." Matches Jones (2024, p. 575–576) nearly verbatim.
- **Lines 104–106** [DEFINITION] OK — AI dividends $D_t^{AI} = \theta_t C_t$ with update rule; Non-AI dividends $D_t^N = (1-\theta_t)C_t$. Totals: $D^{AI}+D^N = C_t$. Verified.
- **Lines 108–112** [VERBAL] OK — Explanation of why $\alpha_t \neq \theta_t$, restricted equity as source of market incompleteness, and hedging channel. Economically coherent.
- **Lines 115–119** [DEFINITION] OK — CRRA utility with $\gamma > 1$, $\beta \in (0,1)$. Standard; matches parameters $\gamma=4$, $\beta=0.96$.
- **Line 123** [VERBAL] OK — "Because markets are incomplete, the household's SDF reflects its own consumption growth, not aggregate consumption growth." Standard and correct.
- **Lines 128–134** [DEFINITION] OK — P/D formula structure $A^j/(1-A^j)$. Correct closed-form from geometric Euler equation under stationarity approximation.
- **Line 136** [ARITHMETIC] OK — $\Gamma^{AI} = (0.15+0.2\times0.85)/0.15 \times 1.5 = 0.32/0.15 \times 1.5 = 3.2$. Verified.
- **Line 136** [ARITHMETIC] OK — $\Gamma^N = (0.85-0.17)/0.85 \times 1.5 = 0.68/0.85 \times 1.5 = 1.2$. Verified.
- **Lines 143–148** [VERBAL] OK — Remark 1: $A^j < 1$ required for finite P/D; when $A^j \geq 1$ the geometric sum diverges. Correct. Baseline satisfies condition (all table P/D values finite and positive).
- **Line 148** [REFERENCE] OK — "As we discuss in Section~\ref{sec:ext2}" — sec:ext2 label exists at line 233 and contains the referenced discussion of government transfers restoring the existence condition.
- **Line 151** [VERBAL] OK — Approximation disclosure: post-singularity P/D treated as equal to pre-singularity; exact as $\Delta\theta \to 0$; table reports numerically exact values. Honest and clear.
- **Line 153** [ARITHMETIC] OK — $\Gamma^{AI} > 1+\eta$: $3.2 > 1.5$. Verified. $\Gamma^N < 1+\eta$: $1.2 < 1.5$. Verified.
- **Line 153** [ARITHMETIC] OK — "$\phi(1+\eta) < 1$ when $\phi$ is sufficiently small": at baseline, $0.5 \times 1.5 = 0.75 < 1$. Condition requires $\phi < 1/(1+\eta) \approx 0.667$. Verified.
- **Line 153** [VERBAL] OK — "AI stocks' payoffs are especially valuable, pushing their P/D ratio above that of non-AI stocks. This is the hedging channel." Supported by the mathematical structure and table data.
- **Lines 155–156** [VERBAL] OK — Spread widens with decreasing $\phi$ (via $\phi^{-\gamma}$) and increasing $p$. Immediate from P/D expressions and confirmed by table.
- **Lines 157–163** [ARITHMETIC] OK — Proposition 2 proof verified step by step:
  - $f(A)=A/(1-A)$ is increasing and convex on $(0,1)$: $f'=1/(1-A)^2>0$, $f''=2/(1-A)^3>0$. Correct.
  - Semi-elasticity $f'(A)/f(A)=1/[A(1-A)]$ increasing in $A$ for $A>1/2$. Correct.
  - Higher $\xi$ reduces $A^{AI}$ more than $A^N$ in absolute terms because $\Gamma^{AI}>\Gamma^N$. Correct.
  - Combined with higher semi-elasticity at $A^{AI}>A^N$: ratio of P/D ratios decreases in $\xi$. Correct.
  - $A^j>1/2$ (P/D>1) satisfied across all table parameterizations (min P/D = 9.7). Correct.
  - Table confirms ratio decreases in $\xi$ at every $p$ level (e.g., p=1%: 2.0→1.9→1.8→1.7). Verified.
- **Line 167** [REFERENCE] OK — "GKP2012 show that growth stocks earn lower expected returns because they hedge displacement risk from innovation." Accurate summary of GKP's main result.
- **Line 167** [VERBAL] OK — Contrast between GKP's continuous displacement (expanding variety) vs. this paper's discrete singularity. Accurate characterization of both frameworks.
- **Line 169** [VERBAL] OK — Under complete markets, $\phi_\text{eff} \to 1$: "displacement is fully hedged, the SDF no longer overweights singularity states, and the displacement-driven valuation premium largely collapses—though a small residual spread from differential dividend growth ($\Gamma^{AI} \neq \Gamma^N$) remains." Economically correct. Numerically verified: with $\phi_\text{eff}=1$, a small spread persists from $\Gamma^{AI}\neq\Gamma^N$.
- **Line 169** [REFERENCE] OK — "This echoes GKP2012's point that future innovators' rents cannot be traded because the innovators have not yet entered the economy." GKP (p. 492) confirmed verbatim.
- **Line 171** [VERBAL] OK — "sufficiently severe displacement can violate the existence condition" follows from Remark 1: small $\phi$ drives $\phi^{-\gamma}$ and hence $A^j$ above 1.
- **Line 171** [VERBAL] OK — "cannot arise under GKP's gradual displacement" — GKP use continuous Brownian shocks with no discrete jumps; the pricing kernel remains bounded. Accurate.

## Quantitative Analysis (lines 176–193)

- **Line 176** — section header
- **Lines 178–183** [FIGURE/TABLE] OK — Table structure matches table-pd-ratios.tex: columns for $p$, $\xi$, AI P/D, Non-AI P/D, Ratio.
- **Line 185** [ASSUMPTION] OK — Parameters: $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$. All match code and table footnote exactly.
- **Line 185** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$. Verified.
- **Line 185** [VERBAL] OK — "household consumption falls by 25%": $1 - 0.75 = 0.25$. Verified.
- **Line 185** [VERBAL] OK — "aggregate consumption rises by 50% in a singularity": $\eta = 0.5$ by definition. Verified.
- **Line 187** [FIGURE/TABLE] OK — "AI stocks trade at a P/D of about 15.5" at p=0.5%, xi=0. Table: 15.5. Verified.
- **Line 187** [FIGURE/TABLE] OK — "non-AI stocks trade near 11" at p=0.5%, xi=0. Table: 11.1. Verified.
- **Line 187** [FIGURE/TABLE] OK — "a ratio of about 1.4" at p=0.5%, xi=0. Table: 1.4. Verified.
- **Line 187** [ARITHMETIC] OK — "At $p=1\%$, the ratio rises to 2." Table: p=1%, xi=0, Ratio=2.0. Verified.
- **Line 187** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium." Table confirms: ratio rises monotonically from 1.1 (p=0.1%) to 2.0 (p=1%) at xi=0. Verified.
- **Line 187** [VERBAL] OK — "extinction risk compresses the AI premium, as Proposition 2 predicts." Table confirms: at every $p$, the ratio falls as $\xi$ increases. Verified.
- **Line 187** [VERBAL] OK — "even AI stocks lose value" at high extinction: at p=1%, AI P/D falls from 26.5 (xi=0) to 20.5 (xi=20%). Verified.
- **Line 189** [FIGURE/TABLE] OK — "S&P 500 P/D ratio has reached historically elevated levels." fig-ai-valuations Panel (a) confirms recent values near historical highs.
- **Line 189** [VERBAL] OK — "the AI-heavy NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015." Panel (b) shows the NASDAQ/S&P ratio (Jan 2015=100) peaking near 150, indicating ~50% relative appreciation at peak. The ratio has since partially retreated; this is a minor imprecision (peak vs. sustained level) but not materially wrong — the paper uses "has appreciated" which can describe the peak outperformance.
- **Line 189** [VERBAL] OK — Caveats about NASDAQ vs. AI stocks mapping being imperfect. Appropriate qualifications.
- **Line 189** [FIGURE/TABLE] OK — "AI stock P/D ratios are 1.3 to 2 times those of non-AI stocks across annual singularity probabilities in the 0.5–1% range." Table: ratios span 1.3 (p=0.5%, xi=10–20%) to 2.0 (p=1%, xi=0). Exactly correct.

## Extensions: Market Incompleteness and the Singularity (lines 194–278)

- **Line 194** — section header
- **Line 196** [VERBAL] OK — "This section examines two further consequences: how incompleteness distorts the development of AI, and how government policy might address it." Accurate roadmap.
- **Line 200** [DEFINITION] OK — Positive singularity: household share rises to $\min(1, \alpha_t/\phi)$; negative: $\phi\alpha_t$. $q > 1/2$ assumed. Consistent with code ($\alpha^+ = \min(1, 0.70/0.5) = 1.4 \to 1$).
- **Line 202** [VERBAL] OK — "socially efficient in the Kaldor-Hicks sense" when $(1+\eta)>1$: aggregate consumption rises by $1+\eta$ regardless of distribution. Correct.
- **Line 204** [DEFINITION] OK — Veto cost $\kappa>0$ as permanent consumption fraction. Extinction utility normalized to zero; CRRA utility is negative for $c>0, \gamma>1$, making veto result conservative. Correct.
- **Line 206** [VERBAL] OK — Under complete markets, consumption in both singularity states is $\alpha(1+\eta)C_t(1+g)$. Consistent with code and economically correct.
- **Lines 208–225** [VERBAL] OK — Proposition 3: (i) sufficiently risk-averse household vetoes under incomplete markets; (ii) never vetoes under complete markets for small $\kappa$. Proof logic verified: as $\gamma\to\infty$, negative-singularity CRRA utility cost dominates because $\phi(1+\eta)<1$ ($0.75<1$). Under complete markets, utility gain is strictly positive since $\eta>0$.
- **Line 227** [ARITHMETIC] OK — Veto numerical example: $\phi=0.5$, $\eta=0.5$, $\xi=5\%$, $p=1\%$, $\gamma=10$, $\alpha=0.70$, $q=0.70$, $\kappa=1\%$. All match code. Code output confirms: incomplete markets $V_\text{veto} > V_\text{develop}$ (household vetoes); complete markets $V_\text{develop}^{CM} > V_\text{veto}$ (no veto). Verified.
- **Line 227** [ARITHMETIC] OK — "positive singularity is more than twice as likely as the negative one": $q/(1-q) = 0.70/0.30 = 2.33 > 2$. Verified.
- **Line 229** [VERBAL] OK — "higher $\xi$ reduces the weight on non-extinction singularity states" — mechanically correct since singularity term is weighted by $p(1-\xi)$.
- **Line 229** [REFERENCE] OK — Jones (2024) reference for bounded utility and extinction penalty is consistent with Jones's framework.
- **Line 231** [REFERENCE] OK — "Jones (2024) identifies two distinct channels: higher $\gamma$ agents less willing to accept existential gambles; agents with higher consumption levels value current standards more." Jones (2024) Section C discusses exactly these two dimensions. Accurate.
- **Line 235** [REFERENCE] OK — "same constraint GKP2012 identify: much of the displacing capital does not yet exist." GKP (p. 492) confirmed.
- **Line 237** [REFERENCE] OK — "GKP discuss: in altruistically-linked dynasty, bequests/gifts ensure equal consumption, displacement factor = 1." GKP (p. 498) states this verbatim. Verified.
- **Line 237** [REFERENCE] OK — "GKP explicitly mention 'intergenerational transfers mandated by the government' as a channel." GKP (p. 498) confirmed verbatim: "intergenerational transfers mandated by the government." Verified.
- **Line 237** [REFERENCE] OK — Paper says GKP "leave quantitative analysis of such transfers to future work." GKP states: "We leave such extensions for future work." Accurate.
- **Line 242** [ARITHMETIC] OK — Transfer consumption formula: $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. First term: displaced consumption. Second: net transfer (fraction $\tau$ of AI surplus, reduced by $\delta\tau$ waste). Algebraically verified; matches code.
- **Line 245** [VERBAL] OK — "$(1-\phi\alpha)$ represents the AI owners' share of post-singularity aggregate consumption." Household has $\phi\alpha$; remainder is $1-\phi\alpha$. Correct.
- **Line 250** [ARITHMETIC] OK — $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$. Derived by dividing eq (10) by $\alpha(1+\eta)(1+g)C_t$. Verified algebraically and matches code.
- **Line 255** [VERBAL] OK — "ratio of post-transfer to pre-transfer household consumption is independent of the productivity jump $\eta$." $(1+\eta)$ cancels in the ratio. Algebraically verified.
- **Line 258** [ARITHMETIC] OK — $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$. Derived by dividing eq (10) by $\phi\alpha(1+\eta)C_t(1+g)$. Verified.
- **Line 261** [ARITHMETIC] OK — $\delta=0.9$, $\tau=0.30$: net transfer factor $= 0.30 \times (1-0.9\times0.30) = 0.30 \times 0.73 = 0.219$. Verified.
- **Line 261** [ARITHMETIC] OK — "consumption multiple of 3.5x at $\tau=0.30$" under large singularity ($\eta=9$, $\phi=0.05$): this is relative to pre-singularity consumption. $c^H_{post}/c^H_{pre} = \phi_\text{eff}(1+\eta) = [0.05 + 0.219\times(1-0.05\times0.70)/0.70]\times 10 = [0.05 + 0.219\times0.965/0.70]\times10 = [0.05 + 0.302]\times10 = 3.52$. Rounds to $3.5\times$. Verified.
- **Line 261** [ARITHMETIC] OK — "$0.5\times$ catastrophe without transfers": $\phi(1+\eta) = 0.05\times10 = 0.5$. Verified.
- **Line 261** [VERBAL] OK — "transforms a 50% consumption loss into a 250% gain": $0.5\times$ is a 50% loss; $3.5\times$ is a 250% gain above pre-singularity baseline ($3.5-1=2.5=250\%$). Verified.
- **Line 263** [ASSUMPTION] OK — Figure parameters: $\gamma=4$, $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$. All match code. Verified.
- **Line 263** [ARITHMETIC] OK — Baseline: $\eta=0.5$, $\phi=0.5$, $\phi(1+\eta)=0.75$; "falls by 25%": $1-0.75=0.25$. Verified.
- **Line 263** [ARITHMETIC] OK — Large singularity: $\eta=9$, $\phi=0.05$, $\phi(1+\eta)=0.5$; "consumption halves." Verified.
- **Line 265** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$. Verified.
- **Line 265** [VERBAL] OK — "existence condition is violated" at large singularity with $\tau=0$: $\phi_\text{eff}=0.05$, $\phi^{-\gamma}=160{,}000$ makes $A^j$ exceed 1. Code returns NA in this region. Verified.
- **Line 269** [FIGURE/TABLE] OK — Figure caption parameters match code and text: $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$.
- **Line 274** [REFERENCE] OK — Jones (2024) for explosive output growth; Nordhaus (2021) for critical examination. Standard citations in the singularity growth literature.

## Conclusion (lines 279–289)

- **Line 279** — section header
- **Line 281** [VERBAL] OK — "AI stocks trade at high valuations" supported by Figure 1 and introduction data.
- **Line 281** [VERBAL] OK — "hedging motive: investors use AI stocks to partially insure against an AI singularity that would displace their consumption" is the paper's central mechanism, formalized in Proposition 1.
- **Line 281** [VERBAL] OK — "requires market incompleteness—the inability to trade restricted AI equity" stated in model (lines 110–112) and shown to collapse the premium under complete markets (line 169).
- **Line 281** [VERBAL] OK — "attenuated by extinction risk, which reduces the weight on the non-extinction states where the hedging channel operates" proven in Proposition 2 (lines 157–163).
- **Line 281** [VERBAL] OK — "risk-averse households may inefficiently block AI development" is the content of Proposition 3(i).
- **Line 281** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough to overwhelm deadweight costs" is the content of Extension 2.
- **Line 283** [VERBAL] OK — "abstracts from continuous-time dynamics" — model is discrete-time (line 72). Correct.
- **Line 283** [VERBAL] OK — "heterogeneous beliefs, production-side details" are indeed absent from the model.
- **Line 283** [VERBAL] OK — "goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel" consistent with spec §IV.8.

## Proof of Proposition 1 (lines 290–321)

- **Line 290** — section header
- **Line 295** [ARITHMETIC] OK — Euler equation $P_t^j = \mathbb{E}_t[\beta(c_{t+1}^H/c_t^H)^{-\gamma}(P_{t+1}^j + D_{t+1}^j)]$ is the standard CRRA Euler equation.
- **Line 298** [VERBAL] OK — "constant in the stationary equilibrium before any singularity" — $\alpha_t, \theta_t$ unchanged in no-singularity state, so P/D is stationary. Correct.
- **Line 301** [ARITHMETIC] OK — No-singularity: $c_{t+1}^H/c_t^H = 1+g$ and $D_{t+1}^{AI}/D_t^{AI} = 1+g$. Both verified from definitions.
- **Line 302** [ARITHMETIC] OK — Non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$ and $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$. Both verified from model definitions.
- **Line 303** [ARITHMETIC] OK — Extinction: $c_{t+1}^H = 0$, payoff is zero. Correct.
- **Lines 309–311** [ARITHMETIC] OK — Euler expansion verified: substituting $P_{t+1}+D_{t+1} = (v^{AI}+1)D_{t+1}^{AI}$ with the three-case dividend growth and SDF terms. Each term algebraically correct.
- **Line 314** [ARITHMETIC] OK — $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is theta-independent: $\frac{(1-\theta)(1-\Delta\theta)}{1-\theta}(1+\eta) = (1-\Delta\theta)(1+\eta)$. Theta cancels. Verified.
- **Line 314** [VERBAL] OK — "This approximation becomes exact as $\Delta\theta \to 0$" — when $\Delta\theta=0$, $\Gamma^{AI}$ is also theta-independent, making the post-singularity P/D equal the pre-singularity P/D exactly. Correct.
- **Line 314** [VERBAL] OK — Backward recursion over the chain $\theta_0, \theta_1 = \theta_0+\Delta\theta(1-\theta_0), \ldots$ matches the model's update rule (line 104) and code implementation.
- **Line 317** [ARITHMETIC] OK — Solving $v^{AI} = X(v^{AI}+1)$ where $X = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$ gives $v^{AI} = X/(1-X)$. Matches eq (5) from line 129 exactly. Verified.
- **Line 320** [VERBAL] OK — "The derivation for non-AI stocks is identical, replacing $\Gamma^{AI}$ with $\Gamma^N$." Correct; the Euler equation structure is the same, and the household's consumption growth is asset-independent.
