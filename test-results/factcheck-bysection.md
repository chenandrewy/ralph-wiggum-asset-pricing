# tests/factcheck-bysection.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 7m 28s
[ralph-garage/agent-logs/20260409T190308.207917-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T190308.207917-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported by tables/figures/formulas, and all references accurately represent cited papers; only minor imprecisions noted.

## Introduction (lines 38–72)

- **Line 38** — section header
- **Line 40** [FIGURE/TABLE] OK — Figure 1 is explicitly labeled "Illustrative" and built from approximate hardcoded P/E values in the R code; the text's caveat "based on approximate values from public sources" is appropriate.
- **Line 40** [VERBAL] OK — "The gap has widened dramatically since 2023" is supported by the illustrative data (AI P/E rises from 42 to 62 to 75 in 2023–2025 while market stays ~20–22).
- **Line 49** [VERBAL] OK — "AI stocks serve as a hedge against... displacement" is the model's core mechanism, formalized in Proposition 1 and Corollary 1.
- **Line 49** [VERBAL] OK — "If markets were complete, investors could insure against this risk directly" is confirmed by Section 2.3 (line 172) and Proposition 3(ii).
- **Line 49** [REFERENCE] OK — GKP2012 cited for "displacement risk from innovation" accurately represents the paper (JFE 2012, "Displacement Risk and Asset Returns").
- **Line 51** [VERBAL] OK — "even inefficient government transfers become effective when the resource base is enormous" accurately previews Extension 2 (Section 4.2).
- **Line 53** [DEFINITION] OK — Model description (representative household, two public assets, stochastic singularity) matches Section 2.1 exactly.
- **Line 53** [REFERENCE] OK — Jones (2024) cited for extinction risk; accurately represents "The AI Dilemma" (AER Insights).
- **Line 53** [VERBAL] OK — "closed-form price-dividend ratios" confirmed by Proposition 1 (eqs. 4–5).
- **Line 55** [REFERENCE] OK — GKP2012 described as showing "innovation creates a systematic risk factor because the rents from new technologies accrue to agents that current investors cannot trade with." Verified against GKP abstract and introduction (p. 492).
- **Line 57** [VERBAL] OK — Veto result previewed here is formalized in Proposition 3(i); complete-markets result in Proposition 3(ii).
- **Line 57** [VERBAL] OK — Government transfers preview matches Extension 2 logic.
- **Line 59** [VERBAL] OK — "P/D ratios for AI stocks can be up to roughly six times higher" — table maximum ratio is 5.8 at p=1%, xi=0%. "Roughly six" is a reasonable description of 5.8.
- **Line 59** [REFERENCE] OK — "Proposition 2(iii) shows" extinction risk attenuates the gap — confirmed by Proposition 2(iii) statement and proof (lines 156, 165), and by monotone decline in table ratios as xi increases.
- **Line 64** [REFERENCE] OK — GKP2012 described as "general-equilibrium model in which innovation displaces existing agents and creates a systematic risk factor under incomplete markets." Accurate.
- **Line 64** [REFERENCE] OK — "We adopt their insight that displacement risk is distinct from aggregate consumption risk and that growth stocks provide a partial hedge." Consistent with GKP (p. 498–499).
- **Line 66** [REFERENCE] OK — Jones (2024) described as showing "bounded utility functions make agents conservative about extinction even when consumption gains are enormous." Accurately represents the paper's core finding.
- **Line 66** [VERBAL] OK — "extinction risk interacts with displacement in a countervailing way, attenuating rather than amplifying the valuation premium." Confirmed by Proposition 2(iii) and table data.
- **Line 68** [REFERENCE] OK — Kogan and Papanikolaou (2014, JF) accurately described for technology shocks and cross-sectional returns.
- **Line 68** [REFERENCE] OK — Kogan, Papanikolaou, Schmidt, and Song (2020, JPE) accurately described for creative destruction, inequality, and valuations.
- **Line 68** [REFERENCE] OK — Barro (2006, QJE) and Wachter (2013, JF) correctly cited as rare disasters foundation.
- **Line 68** [REFERENCE] OK — Pastor and Veronesi (2009, AER) accurately described for technological revolutions and stock prices.
- **Line 68** [REFERENCE] OK — Korinek and Suh (2024, NBER WP) accurately described for AGI transition scenarios.

## Model (lines 73–176)

- **Line 73** — section header
- **Line 77** [REFERENCE] OK — AI owners as "future capital owners who do not yet participate in markets, as in GKP2012." GKP (p. 492) explicitly states future innovators cannot trade with current agents. Accurate.
- **Line 80** [DEFINITION] OK — Aggregate consumption growth $C_{t+1} = (1+g)C_t$ with $g > 0$. Standard, consistent throughout.
- **Line 86** [DEFINITION] OK — Household share $\alpha_t \in (0, 1-\theta_t]$ correctly bounded; AI owners receive $(1-\alpha_t)C_t$. Accounting is consistent.
- **Line 92** [DEFINITION] OK — Non-extinction singularity: consumption jumps by $1+\eta$, share drops to $\phi\alpha_t$.
- **Line 96** [VERBAL] OK — "smaller $\phi$ means larger displacement." Correct by construction.
- **Line 97** [REFERENCE] OK — Jones (2024) cited for "the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest." Matches Jones verbatim (p. 1).
- **Line 106** [DEFINITION] OK — AI dividend share update $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$. Ensures $\theta \in (0,1)$.
- **Line 107** [DEFINITION] OK — Non-AI dividends $D_t^N = (1-\theta_t)C_t$. Consistent with $D_t^{AI} = \theta_t C_t$.
- **Line 110** [ARITHMETIC] OK — Private AI capital = $(1-\alpha_t - \theta_t)C_t \geq 0$ since $\alpha_t \leq 1-\theta_t$.
- **Line 113** [DEFINITION] OK — CRRA with $\gamma > 1$, $\beta \in (0,1)$. Consistent with $\gamma=4$ used later.
- **Line 121** [VERBAL] OK — "SDF reflects household's own consumption growth, not aggregate" is the correct implication of incomplete markets.
- **Lines 127–134** [ARITHMETIC] OK — $\Gamma^{AI} = [\theta + \Delta\theta(1-\theta)](1+\eta)/\theta$. With $\theta=0.15$, $\Delta\theta=0.2$, $\eta=0.5$: $\Gamma^{AI} = (0.15+0.17)/0.15 \times 1.5 = 2.133 \times 1.5 = 3.2$. $\Gamma^N = (1-\Delta\theta)(1+\eta) = 0.8 \times 1.5 = 1.2$. Formulas match appendix proof exactly.
- **Lines 127–134** [ARITHMETIC] OK — P/D formulas (eqs. 4–5) match the appendix derivation (eq. 17, line 305) exactly.
- **Line 141** [VERBAL] OK — "$\Gamma^{AI} > 1+\eta$" since $\Delta\theta > 0$ implies $[\theta+\Delta\theta(1-\theta)]/\theta > 1$. Correct.
- **Line 141** [VERBAL] OK — "$\Gamma^N < 1+\eta$" since $\Gamma^N = (1-\Delta\theta)(1+\eta) < (1+\eta)$. Correct.
- **Line 141** [VERBAL] OK — "$\phi(1+\eta) < 1$ when $\phi$ is sufficiently small." With $\phi=0.5$, $\eta=0.5$: $0.75 < 1$. Correct.
- **Lines 147–149** [VERBAL] OK — Corollary 1 proof: P/D is increasing in $\Gamma^j$ (since $A/(1-A)$ is increasing in $A$ for $A \in (0,1)$), and $\Gamma^{AI} > \Gamma^N$ when $\Delta\theta > 0$. Valid.
- **Line 154** [VERBAL] OK — Proposition 2(i): spread increases as $\phi$ decreases. $\phi^{-\gamma}$ amplifies singularity term; AI benefits more due to higher $\Gamma^{AI}$. Correct.
- **Line 155** [VERBAL] OK — Proposition 2(ii): spread increases in $p$ for $\gamma$ sufficiently large. Mathematically safe sufficient condition.
- **Line 156** [VERBAL] OK — Proposition 2(iii): spread and ratio decrease in $\xi$. Verified numerically from table (e.g., ratio at p=1% falls from 5.8 to 4.3 to 3.5 to 2.6 as xi goes from 0% to 20%).
- **Lines 161–165** [VERBAL] OK — All three proof sketches are logically sound.
- **Line 170** [REFERENCE] OK — GKP2012: "growth stocks earn lower expected returns because they hedge displacement risk." Verified against GKP (pp. 498–499).
- **Line 170** [REFERENCE] OK — "displacement is driven by new cohorts of firms entering the economy" in GKP. Verified (GKP p. 492).
- **Line 172** [REFERENCE] OK — "future innovators' rents cannot be traded because the innovators have not yet entered the economy." Matches GKP (p. 492) almost verbatim.

## Quantitative Analysis (lines 177–194)

- **Line 177** — section header
- **Line 179** [ASSUMPTION] OK — All parameter values ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$) match R code and table footnote exactly.
- **Line 179** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$, so household consumption falls by 25%. Correct.
- **Line 188** [VERBAL] OK — "AI stocks trade at a P/D of roughly 18" at p=0.5%, xi=0%: table shows 17.5. "Roughly 18" is a slight rounding but within editorial tolerance.
- **Line 188** [VERBAL] OK — "non-AI stocks trade near 11": table shows 11.1. Correct.
- **Line 188** [VERBAL] OK — "ratio of about 1.6": table shows exactly 1.6. Correct.
- **Line 188** [VERBAL] OK — "At p=1%, the ratio rises to nearly 6 to 1": table shows 5.8 at xi=0%. "Nearly 6" is reasonable.
- **Line 188** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium." Confirmed: ratio rises monotonically in p across the table for every xi level.
- **Line 188** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium." Confirmed by table: both P/D levels and ratio decline as xi increases. Consistent with Proposition 2(iii).
- **Line 188** [REFERENCE] OK — "as Proposition 2(iii) predicts" — cross-reference correct; Proposition 2(iii) is at line 156.
- **Line 190** [VERBAL] OK — "Leading AI firms have traded at P/E ratios two to five times the market average" — this is a rough empirical claim consistent with the illustrative Figure 1 data and publicly known market patterns.

## Extensions: Market Incompleteness and the Singularity (lines 195–268)

- **Line 195** — section header
- **Line 204** [DEFINITION] OK — Positive singularity: $\alpha_{t+1} = \phi^+\alpha_t$ with $\phi^+ > 1$, aggregate jump $1+\eta$. Clearly defined.
- **Line 205** [DEFINITION] OK — Negative singularity: $\alpha_{t+1} = \phi\alpha_t$ with $\phi < 1$. Matches baseline model.
- **Line 208** [ASSUMPTION] OK — $\lambda > 1/2$: positive singularity is most likely.
- **Line 210** [DEFINITION] OK — Veto costs $\kappa > 0$ in utility terms; prevents singularity if household vetoes.
- **Lines 216–217, Eq. 10** [ARITHMETIC] OK — $\Delta U^H = p(1-\xi)[\lambda u(\phi^+\alpha(1+\eta)(1+g)C_t) + (1-\lambda)u(\phi\alpha(1+\eta)(1+g)C_t)] - p\,u(\alpha(1+g)C_t)$. Correctly reduces from full expected utility minus no-singularity baseline: $[(1-p)u + p(1-\xi)(\cdot) + p\xi \cdot 0] - u = -p\,u + p(1-\xi)[\cdot]$. Valid.
- **Line 219** [REFERENCE] MINOR IMPRECISION — Claims to follow Jones (2024) in normalizing extinction utility to zero. Jones does set $u_{ext}=0$, but his specification adds $\bar{u}>0$ so that life utility exceeds zero. The paper omits $\bar{u}$, so $u(c) = c^{1-\gamma}/(1-\gamma) < 0$ for all $c>0$ when $\gamma>1$, meaning extinction (utility 0) is technically preferred to life. The directional claim that this is "conservative" for the veto result (reducing veto incentive by lowering weight on extinction) is correct, but the mapping to Jones's setup is imprecise.
- **Lines 228–231** [VERBAL] OK — Proposition 3 proof: Part (i) uses CRRA concavity and dominance of downside risk for large $\gamma$; logic is sound. Part (ii) uses standard complete-markets argument; logic is sound.
- **Line 233** [REFERENCE] OK — "Jones2024 argues bounded utility [makes extinction penalty high]" accurately represents Jones's core finding.
- **Line 237** [REFERENCE] OK — "GKP2012 note that intergenerational transfers affect the magnitude of displacement risk but treat such mechanisms as inessential extensions." Verified against GKP conclusion (p. 693): transfers listed among elements abstracted from.
- **Line 242, Eq. 11** [ARITHMETIC] OK — Transfer consumption formula matches R code's `consumption_growth` function exactly when normalized by $\alpha C_t(1+g)$.
- **Line 247** [VERBAL] OK — "ratio of post-transfer to pre-transfer household consumption is independent of the productivity jump $\eta$." Confirmed algebraically: $(1+\eta)$ cancels from numerator and denominator in eq. 12.
- **Line 250, Eq. 12** [ARITHMETIC] OK — $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta_0\tau)(1-\phi\alpha)/(\phi\alpha)$. Correctly derived from eq. 11. Exceeds 1 for $\tau > 0$.
- **Line 253** [VERBAL] OK — "as $\eta$ grows, both $c^H_{post}$ and $c^H_{no\text{-}transfer}$ grow without bound, so even inefficient transfers deliver arbitrarily large consumption gains relative to the pre-singularity baseline." Correct: both scale linearly in $(1+\eta)$.
- **Line 255** [ASSUMPTION] OK — "p=0.5% and xi=5%" match code values p_ext=0.005, xi_ext=0.05.
- **Line 255** [ASSUMPTION] OK — "baseline uses eta=0.5 and phi=0.5; the large singularity uses eta=9 with phi=0.05." Match code parameters exactly.
- **Line 255** [ARITHMETIC] OK — Large singularity: $\phi(1+\eta) = 0.05 \times 10 = 0.5$, so "consumption halves." Correct.
- **Line 255** [ARITHMETIC] OK — Baseline: $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$, so "falls by 25%." Correct.
- **Line 255** [VERBAL] OK — "ten-fold growth" for $\eta=9$ means $1+\eta=10$, i.e., output is 10x. Correct.
- **Line 264** [REFERENCE] OK — Nordhaus (2021) cited generically for explosive output growth. Consistent with standard characterization.

## Conclusion (lines 269–279)

- **Line 269** — section header
- **Line 271** [VERBAL] OK — "part of this premium reflects a hedging motive" — supported by Proposition 1, Corollary 1, and quantitative analysis.
- **Line 271** [VERBAL] OK — "requires market incompleteness" — supported by Section 2.3 (line 172) and Proposition 3(ii).
- **Line 271** [VERBAL] OK — "attenuated by extinction risk" — supported by Proposition 2(iii) and table data.
- **Line 271** [VERBAL] OK — "risk-averse households may inefficiently block AI development" — supported by Proposition 3(i).
- **Line 271** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough" — supported by Extension 2 analysis and figure.
- **Line 273** [VERBAL] OK — Self-description of model limitations is accurate.

## Proof of Proposition 1 (lines 280–309)

- **Line 280** — section header
- **Line 285** [DEFINITION] OK — Standard CRRA Euler equation. Correct for utility in eq. 3.
- **Line 288** [VERBAL] OK — P/D ratio is constant pre-singularity due to scale-invariance and stationary parameters.
- **Line 291** [ARITHMETIC] OK — No singularity: $c_{t+1}^H/c_t^H = (1+g)$ and $D_{t+1}^{AI}/D_t^{AI} = (1+g)$. Correct since $\alpha$ and $\theta$ unchanged.
- **Line 292** [ARITHMETIC] OK — Non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$ and $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$. Correct from model definitions.
- **Line 293** [ARITHMETIC] OK — Extinction: $C_{t+1}=0$ implies zero payoff. Correct.
- **Lines 297–300** [ARITHMETIC] OK — Euler equation expansion verified. SDF in singularity state: $[\phi(1+g)(1+\eta)]^{-\gamma} = \phi^{-\gamma}(1+g)^{-\gamma}(1+\eta)^{-\gamma}$. Combined with dividend growth $(1+g)\Gamma^{AI}$, yields $\beta(1+g)^{1-\gamma}\phi^{-\gamma}(1+\eta)^{-\gamma}\Gamma^{AI}$. Correct.
- **Line 302** [VERBAL] OK — Approximation of post-singularity P/D as $v^{AI}$ is honestly flagged; exactness condition stated.
- **Lines 304–306** [ARITHMETIC] OK — Solving $v = A(v+1)$ gives $v = A/(1-A)$ where $A = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$. Matches eq. 4 exactly.
- **Line 308** [VERBAL] OK — Non-AI derivation is identical with $\Gamma^N$ replacing $\Gamma^{AI}$. Correct since consumption growth is the same across assets; only dividend growth differs.
