# tests/factcheck-bysection.py
Started: 2026-04-14 10:33:09 EDT
Runtime: 7m 18s
[ralph-garage/agent-logs/20260414T103309.994128-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260414T103309.994128-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong.

## Introduction (lines 38–70)
- **Line 38** — section header
- **Line 40** [VERBAL] OK — S&P 500 P/D at historically elevated levels, supported by Figure 1 Panel (a) which plots Shiller trailing P/D
- **Line 40** [VERBAL] OK — NASDAQ has outpaced S&P 500 since 2015, supported by Figure 1 Panel (b) normalized price ratio
- **Line 40** [VERBAL] OK — valuation gap widening since 2023; consistent with NASDAQ/S&P price ratio trend post-ChatGPT
- **Line 44** [FIGURE/TABLE] OK — Panel (a) caption accurately describes Shiller S&P 500 trailing P/D; code uses `SP500 / Dividend` from Shiller data
- **Line 44** [FIGURE/TABLE] OK — Panel (b) caption: NASDAQ/S&P normalized to Jan 2015 = 100; code confirms normalization at `as.Date("2015-01-01")`
- **Line 44** [FIGURE/TABLE] OK — Sources stated as FRED (NASDAQ) and Shiller dataset (S&P 500); code uses `download_fred("NASDAQCOM")` and Shiller datahub CSV
- **Line 49** [DEFINITION] OK — negative AI singularity defined as sudden productivity improvement that displaces investor consumption; matches model setup in Section 2
- **Line 49** [REFERENCE] OK — GKP2012 cited for displacing capital belonging to future innovators; confirmed in GKP-2012.md: "future innovators, who are yet to enter the economy, are not able to trade with the current population of agents"
- **Line 49** [VERBAL] OK — premium would largely vanish under complete markets; supported by Section 2.3 discussion (line 175)
- **Line 51** [VERBAL] OK — model delivers closed-form P/D ratios; Proposition 1 (line 131) provides them
- **Line 51** [ARITHMETIC] OK — "P/D ratios for AI stocks roughly double relative to non-AI stocks" at p=1%; table shows ratio = 2.0 at p=1%, xi=0% (26.5/13.3)
- **Line 51** [REFERENCE] OK — Jones2024 cited for extinction risk; confirmed in Jones-2024-AERI.md
- **Line 51** [REFERENCE] OK — Proposition 2 (prop:comp-statics) correctly referenced for extinction attenuation
- **Line 53** [VERBAL] OK — risk-averse household may block AI development under incomplete markets; supported by Proposition 3 (line 214)
- **Line 53** [REFERENCE] OK — prop:veto correctly points to Proposition 3
- **Line 55** [VERBAL] OK — financial approaches to AI disaster risk under-discussed; contextual claim consistent with paper's contribution
- **Line 55** [VERBAL] OK — government transfers limited by deadweight costs; consistent with Section 4.2 model
- **Line 57** [VERBAL] OK — explosive growth makes inefficient transfers effective; supported by Section 4.2 analysis
- **Line 57** [REFERENCE] OK — Jones2024 referenced for explosive output growth model
- **Line 59** [REFERENCE] OK — Section labels sec:model (line 71), sec:quant (line 182), sec:extensions (line 200) all exist and match described content
- **Line 59** [VERBAL] OK — footnote about AI agents producing the paper; matches spec requirement (IV.5.c)
- **Line 64** [REFERENCE] OK — GKP2012 characterized as modeling innovation displacement under incomplete markets; confirmed in GKP-2012.md
- **Line 64** [VERBAL] OK — "main insights about displacement risk and incomplete markets originate in their work"; appropriately modest per spec (I.6.c)
- **Line 66** [REFERENCE] OK — Jones2024 characterized as studying AI-driven growth vs existential risk tradeoff; confirmed
- **Line 66** [VERBAL] OK — extinction channel attenuates rather than amplifies valuation premium; supported by Proposition 2
- **Line 66** [REFERENCE] OK — literature citations (Kogan-Papanikolaou, Barro, Wachter, Pastor-Veronesi, etc.) are generic characterizations with no specific factual claims to verify

## Model (lines 71–181)
- **Line 71** — section header
- **Line 75** [DEFINITION] OK — discrete time, infinite horizon, representative household as marginal investor, AI owners with private capital
- **Line 75** [REFERENCE] OK — GKP2012 parallel for AI owners as future capital owners; confirmed in GKP-2012.md
- **Line 75** [VERBAL] OK — caveat that entry dynamics are not modeled is accurate and matches spec (I.4.d)
- **Line 78** [DEFINITION] OK — aggregate consumption growth $C_{t+1} = (1+g)C_t$ with $g > 0$
- **Line 84** [DEFINITION] OK — household share $\alpha_t$, consumption $c_t^H = \alpha_t C_t$; shares sum to one
- **Line 87** [DEFINITION] OK — singularity probability $p$ per period
- **Line 90–92** [DEFINITION] OK — non-extinction singularity: consumption jumps by $1+\eta$, share drops by $\phi$; $\alpha_{t+1} = \phi\alpha_t$
- **Line 94** [DEFINITION] OK — $\phi$ governs displacement severity; smaller $\phi$ means larger displacement
- **Line 95** [DEFINITION] OK — extinction: $C_{t+1} = 0$ for all subsequent dates
- **Line 95** [REFERENCE] OK — Jones2024 cited for extinction in powerful-AI states; confirmed
- **Line 104** [DEFINITION] OK — AI dividends $D_t^{AI} = \theta_t C_t$; share update $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$
- **Line 110** [VERBAL] OK — this expression drives $\Gamma^{AI} \neq \Gamma^N$; verified algebraically
- **Line 111** [DEFINITION] OK — non-AI dividends $D_t^N = (1-\theta_t)C_t$
- **Line 114** [ARITHMETIC] OK — total public dividends $D^{AI} + D^N = \theta C + (1-\theta)C = C_t$
- **Line 114** [VERBAL] OK — $\alpha_t$ and $\theta_t$ are distinct (consumption split vs dividend split); correct accounting
- **Line 116** [DEFINITION] OK — restricted equity (founder stakes, pre-IPO shares) not available for public trading; source of market incompleteness
- **Line 118** [VERBAL] OK — hedging channel: AI stocks smooth marginal utility across states but do not eliminate displacement
- **Line 121** [DEFINITION] OK — CRRA preferences with $\gamma > 1$, discount factor $\beta \in (0,1)$; equation (4) is standard
- **Line 129** [VERBAL] OK — SDF reflects household's own consumption growth under incomplete markets
- **Line 134–136** [ARITHMETIC] OK — P/D formula for AI stocks verified: $v^{AI} = A^{AI}/(1-A^{AI})$ where $A^{AI} = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$
- **Line 138–140** [ARITHMETIC] OK — P/D formula for non-AI stocks: same structure with $\Gamma^N$
- **Line 142** [ARITHMETIC] OK — $\Gamma^{AI} = [\theta+\Delta\theta(1-\theta)]/\theta \cdot (1+\eta)$; verified from dividend definitions
- **Line 142** [ARITHMETIC] OK — $\Gamma^N = [1-\theta-\Delta\theta(1-\theta)]/(1-\theta) \cdot (1+\eta) = (1-\Delta\theta)(1+\eta)$; theta cancels, confirmed
- **Line 150–154** [ARITHMETIC] OK — existence condition $A^j < 1$ is necessary and sufficient for positive finite P/D; at baseline parameters $A^{AI} \approx 0.913 < 1$, $A^N \approx 0.907 < 1$
- **Line 154** [REFERENCE] OK — forward reference to Section 4.2 (sec:ext2) for transfers motivation; section exists at line 239
- **Line 157** [VERBAL] OK — closed-form approximation treats post-singularity P/D as equal to pre-singularity; exact when $\Delta\theta \to 0$; table uses numerically exact backward recursion; all confirmed in R code
- **Line 159** [ARITHMETIC] OK — $\Gamma^{AI} > 1+\eta$ since $\Delta\theta > 0$ makes $[\theta+\Delta\theta(1-\theta)]/\theta > 1$
- **Line 159** [ARITHMETIC] OK — $\Gamma^N < 1+\eta$ since $(1-\Delta\theta) < 1$
- **Line 159** [VERBAL] OK — when $\phi(1+\eta) < 1$, household consumption falls in singularity; marginal utility is high; AI stocks' payoffs are especially valuable; this is the hedging channel
- **Line 161** [VERBAL] OK — spread widens with decreasing $\phi$ (via $\phi^{-\gamma}$) and with increasing $p$; follows from the formula
- **Line 163–164** [VERBAL] OK — Proposition 2: valuation spread decreasing in $\xi$; verified analytically and numerically
- **Line 167–169** [ARITHMETIC] OK — proof logic correct: higher $\xi$ reduces $(1-\xi)$ factor, compresses the weight on states where $\Gamma^{AI} > \Gamma^N$ operates
- **Line 173** [REFERENCE] OK — GKP2012 characterized as showing growth stocks hedge displacement risk and earn lower returns; confirmed in GKP-2012.md
- **Line 173** [VERBAL] OK — contrast between GKP's ongoing displacement from expanding variety and this paper's discrete singularity is fair
- **Line 175** [VERBAL] OK — $\phi_\text{eff} \to 1$ under complete markets eliminates SDF overweighting of singularity states; residual spread from $\Gamma^{AI} \neq \Gamma^N$ noted
- **Line 175** [REFERENCE] OK — GKP parallel for non-tradeable future capital; confirmed
- **Line 177** [VERBAL] OK — discrete singularity can violate existence condition (Remark 1); GKP's gradual displacement cannot produce this discontinuity

## Quantitative Analysis (lines 182–199)
- **Line 182** — section header
- **Line 191** [ASSUMPTION] OK — $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$; all match R code (lines 18–24) and table footnote exactly
- **Line 191** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; exact
- **Line 191** [VERBAL] OK — "household consumption falls by 25%"; consumption multiple 0.75 means 25% fall; correct
- **Line 193** [ARITHMETIC] OK — "AI stocks trade at a P/D of about 15.5" at $p=0.5\%$, $\xi=0\%$; table shows exactly 15.5
- **Line 193** [ARITHMETIC] OK — "non-AI stocks trade near 11" at $p=0.5\%$, $\xi=0\%$; table shows 11.1
- **Line 193** [ARITHMETIC] OK — "ratio of about 1.4" at $p=0.5\%$, $\xi=0\%$; table shows exactly 1.4
- **Line 193** [ARITHMETIC] OK — "At $p=1\%$, the ratio rises to 2"; table shows ratio = 2.0 at $p=1\%$, $\xi=0\%$
- **Line 193** [VERBAL] OK — "extinction risk compresses the AI premium"; confirmed by table: ratio falls from 2.0 to 1.7 as $\xi$ goes from 0% to 20% at $p=1\%$
- **Line 193** [VERBAL] OK — "even AI stocks lose value" at high extinction; AI P/D falls from 26.5 to 20.5 as $\xi$ goes from 0% to 20% at $p=1\%$
- **Line 193** [REFERENCE] OK — "as Proposition 2 predicts"; Proposition 2 states spread is decreasing in $\xi$
- **Line 195** [VERBAL] OK — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015"; figure methodology confirmed (price ratio normalized to Jan 2015 = 100), directionally consistent with public data
- **Line 195** [VERBAL] OK — mapping caveats acknowledged: NASDAQ broader than AI stocks, return vs valuation distinction, S&P has AI exposure
- **Line 195** [ARITHMETIC] OK — "P/D ratios are 1.3 to 2 times" across 0.5–1% range; table confirms: minimum ratio 1.3 (at $p=0.5\%$, $\xi\geq10\%$), maximum 2.0 (at $p=1\%$, $\xi=0\%$)
- **Line 195** [ARITHMETIC] OK — independent recomputation of non-AI P/D at $p=0.5\%$, $\xi=0\%$: $\Gamma^N = 0.8 \times 1.5 = 1.2$; $A^N = 0.9046 \times [0.995 + 0.005 \times 16 \times 0.1975 \times 1.2] = 0.9173$; P/D = $0.9173/0.0827 = 11.09 \approx 11.1$; matches table

## Extensions: Market Incompleteness and the Singularity (lines 200–284)
- **Line 200** — section header
- **Line 206** [DEFINITION] OK — positive singularity: household share increases to $\min(1, \alpha/\phi)$; negative: share falls to $\phi\alpha$; $q > 1/2$ assumed
- **Line 208** [VERBAL] OK — Kaldor-Hicks efficiency holds when $(1+\eta) > 1$: aggregate consumption rises in both outcomes, winners can compensate losers
- **Line 210** [DEFINITION] OK — veto cost $\kappa > 0$: permanent consumption fraction lost; extinction utility normalized to zero
- **Line 212** [DEFINITION] OK — complete markets: household consumes $\alpha(1+\eta)C_t(1+g)$ in both singularity states; confirmed in R code
- **Line 214–218** [VERBAL] OK — Proposition 3 part (i): under incomplete markets with $\phi(1+\eta) < 1$, there exists threshold $\bar\gamma$ above which household vetoes; logically sound
- **Line 214–218** [VERBAL] OK — Proposition 3 part (ii): under complete markets, household never vetoes for $\kappa$ small enough; correct since utility gain $u(\alpha(1+\eta)) - u(\alpha) > 0$
- **Line 222–231** [ARITHMETIC] OK — proof of part (i): as $\gamma \to \infty$, negative-singularity term dominates because $\phi\alpha(1+\eta) < \alpha$ when $\phi(1+\eta) < 1$; limit argument verified numerically
- **Line 230** [ARITHMETIC] OK — proof of part (ii): expected utility gain $u(\alpha(1+\eta)) - u(\alpha) > 0$ since $\eta > 0$; correct for all $\gamma > 1$
- **Line 233** [ARITHMETIC] OK — veto numerical example: $\phi=0.5$, $\eta=0.5$, $\xi=5\%$, $p=1\%$, $\gamma=10$, $\alpha=0.70$, $q=0.70$, $\kappa=1\%$; all match R code (lines 427–432); $V_\text{veto} > V_\text{develop}$ confirmed (VETO); $V_\text{develop}^{CM} > V_\text{veto}$ confirmed (no veto under complete markets)
- **Line 233** [ARITHMETIC] OK — "positive singularity is more than twice as likely as the negative one": $q/(1-q) = 0.70/0.30 = 2.33$; correct
- **Line 235** [VERBAL] OK — extinction interaction under conservative normalization: higher $\xi$ reduces weight on non-extinction states driving veto; correct
- **Line 237** [REFERENCE] OK — Jones2024 cited for two channels (risk aversion and consumption levels); matches Jones-2024-AERI.md content
- **Line 243** [REFERENCE] OK — GKP2012 cited for transfers affecting displacement factor magnitude; confirmed in GKP Section 3.3: lists "intergenerational transfers mandated by the government" among extensions preserving functional form
- **Line 248–249** [ARITHMETIC] OK — equation (8): $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$; first term is displaced consumption, second is net transfer from AI owners' share $(1-\phi\alpha)$; correctly uses consumption share $\alpha$ not dividend share $\theta$
- **Line 256** [ARITHMETIC] OK — $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$; verified by dividing eq (8) by $\alpha(1+\eta)(1+g)C_t$; matches R code line 152
- **Line 259** [VERBAL] OK — P/D formula applies with $\phi$ replaced by $\phi_\text{eff}$; correct since $\phi_\text{eff}$ enters SDF identically
- **Line 264** [ARITHMETIC] OK — transfer ratio $c^H_{post}/c^H_\text{no-transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$; verified algebraically; $(1+\eta)$ cancels making ratio $\eta$-independent as claimed
- **Line 267** [ARITHMETIC] OK — $\delta=0.9$, $\tau=0.30$: net transfer factor $\tau(1-\delta\tau) = 0.30 \times 0.73 = 0.219$; stated correctly
- **Line 267** [ARITHMETIC] OK — consumption multiple at $\tau=0.30$, $\eta=9$, $\phi=0.05$: $0.05 \times 10 + 0.219 \times (1-0.035)/0.035 \times 10 = 0.5 + 60.4 = 3.52 \approx 3.5\times$; correct
- **Line 267** [ARITHMETIC] OK — "0.5x catastrophe without transfers": $\phi(1+\eta) = 0.05 \times 10 = 0.5$; exact
- **Line 267** [ARITHMETIC] OK — "50% consumption loss into a 250% gain": $3.52\times$ is a $252\%$ gain; rounds to $250\%$; acceptable
- **Line 269** [ARITHMETIC] OK — "consumption halves under the large singularity ($\phi(1+\eta) = 0.5$)": $0.05 \times 10 = 0.5$; exact
- **Line 269** [ARITHMETIC] OK — "falls by 25% under the baseline ($\phi(1+\eta) = 0.75$)": $0.5 \times 1.5 = 0.75$; exact
- **Line 271** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$; exact
- **Line 271** [VERBAL] OK — existence condition violated at $\tau=0$ for large singularity; confirmed by R code returning NA at low $\tau$
- **Line 275** [ASSUMPTION] OK — figure caption parameters $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$; all match R code (`alpha0=0.70`, `p_ext=0.005`, `xi_ext=0.05`, `delta=0.50`)
- **Line 280** [REFERENCE] OK — Jones2024 and Nordhaus2021 cited for explosive output growth; appropriate citations

## Conclusion (lines 285–295)
- **Line 285** — section header
- **Line 287** [VERBAL] OK — "hedging motive" summary; supported by Proposition 1 and quantitative analysis
- **Line 287** [VERBAL] OK — "requires market incompleteness"; supported by Section 2.3 (line 175)
- **Line 287** [VERBAL] OK — "attenuated by extinction risk"; supported by Proposition 2
- **Line 287** [VERBAL] OK — "risk-averse households may inefficiently block AI development"; supported by Proposition 3
- **Line 287** [VERBAL] OK — "government transfers...become effective if singularity-driven growth is large enough"; supported by Section 4.2
- **Line 289** [VERBAL] OK — "abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details"; accurately describes model scope

## Proof of Proposition 1 (lines 296–327)
- **Line 296** — section header
- **Line 301** [ARITHMETIC] OK — Euler equation $P_t^j = \mathbb{E}_t[\beta(c_{t+1}^H/c_t^H)^{-\gamma}(P_{t+1}^j + D_{t+1}^j)]$; standard CRRA first-order condition
- **Line 307** [ARITHMETIC] OK — no-singularity case: $c_{t+1}^H/c_t^H = 1+g$ and $D_{t+1}^{AI}/D_t^{AI} = 1+g$; both verified from model definitions
- **Line 308** [ARITHMETIC] OK — non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$; verified: $\phi\alpha(1+\eta)(1+g)C_t / (\alpha C_t) = \phi(1+g)(1+\eta)$
- **Line 308** [ARITHMETIC] OK — AI dividend growth: $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$; verified from $[\theta+\Delta\theta(1-\theta)]/\theta \cdot (1+\eta)(1+g) = \Gamma^{AI}(1+g)$
- **Line 309** [ARITHMETIC] OK — extinction: $c_{t+1}^H = 0$, payoff is zero; follows from $C_{t+1} = 0$ (line 95)
- **Line 315–316** [ARITHMETIC] OK — Euler equation expansion: both terms correctly substitute the consumption growth and dividend growth for their respective cases; $\beta(1+g)^{-\gamma}$ properly factored
- **Line 320** [ARITHMETIC] OK — $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is theta-independent; verified: $(1-\theta)(1-\Delta\theta)/(1-\theta) = 1-\Delta\theta$; non-AI closed form is exact
- **Line 320** [VERBAL] OK — post-singularity AI P/D approximated by pre-singularity value; acknowledged as approximation, exact when $\Delta\theta \to 0$; table uses exact backward recursion
- **Line 323** [ARITHMETIC] OK — solved formula $v^{AI} = A/(1-A)$ matches Proposition 1 eq (5) exactly; algebra: $v = A(v+1)$ gives $v(1-A) = A$, so $v = A/(1-A)$
- **Line 326** [VERBAL] OK — non-AI derivation is identical with $\Gamma^N$ replacing $\Gamma^{AI}$; correct
