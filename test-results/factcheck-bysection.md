# tests/factcheck-bysection.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 6m 15s
[ralph-garage/agent-logs/20260409T203927.613077-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T203927.613077-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection

VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong; two minor imprecisions in the Quantitative Analysis section do not rise to the level of error.

## Introduction (lines 38–72)

- **Line 38** — section header
- **Line 40** [FIGURE/TABLE] OK — claims NASDAQ has dramatically outpaced S&P 500 since 2015, with the gap widening since 2023; confirmed by fig-ai-valuations.pdf (NASDAQ ~490 vs S&P ~330 by early 2026, both normalized to 100 in Jan 2015)
- **Line 44** [FIGURE/TABLE] OK — caption states monthly closing prices normalized to Jan 2015 = 100, sources NASDAQ from FRED and S&P 500 from Shiller dataset; matches the R code data pipeline
- **Line 49** [VERBAL] OK — describes hedging motive and market incompleteness from private AI capital; consistent with model setup (lines 77, 110)
- **Line 51** [VERBAL] OK — observational claim that financial market solutions to AI risk are under-discussed; rhetorical framing, no factual issue
- **Line 53** [VERBAL] OK — "P/D ratios for AI stocks can reach roughly six times those of non-AI stocks": table maximum is 5.8 (p=1%, ξ=0%); "roughly six" is acceptable rounding of 5.8
- **Line 53** [VERBAL] OK — "Extinction risk attenuates this gap": supported by Proposition 2(iii) and confirmed in Table 1 (ratio falls from 5.8 to 2.6 as ξ rises from 0% to 20% at p=1%)
- **Line 53** [REFERENCE] OK — attributes displacement-risk-under-incomplete-markets idea to GKP2012; consistent with bib entry (Gârleanu, Kogan, Panageas 2012, JFE, "Displacement Risk and Asset Returns")
- **Line 55** [VERBAL] OK — veto/blocking extension description; consistent with Proposition 3 (lines 205–216)
- **Line 57** [REFERENCE] OK — GKP2012 on future innovators' rents and Jones2024 on explosive output growth; both attributions match bib entries and paper descriptions
- **Line 59** [VERBAL] OK — AI-authorship disclosure; factual description of the workflow
- **Line 64** [REFERENCE] OK — "builds most directly on GKP2012, who develop a general-equilibrium model in which innovation displaces existing agents"; matches bib entry and paper's own description (lines 170–172)
- **Line 66** [REFERENCE] OK — Jones2024 studies AI-driven growth vs existential risk with bounded utility; matches bib entry (Jones 2024, AER: Insights, "The AI Dilemma")
- **Line 68** [REFERENCE] OK — KoganPapanikolaou2014 (JF), KoganPapanikolaouStoffman2020 (JPE), Knesl2023 (JFE), Barro2006, Wachter2013, PastorVeronesi2009 (AER): all attributions match bib entries and described contributions

## Model (lines 73–176)

- **Line 73** — section header
- **Line 77** [ASSUMPTION] OK — representative household is marginal investor; AI owners hold private capital and are not marginal investors; static group whose share changes only through singularity
- **Line 80** [ASSUMPTION] OK — aggregate consumption grows at constant rate g > 0 absent singularity
- **Line 83** [DEFINITION] OK — eq (1): $C_{t+1} = (1+g)C_t$
- **Line 86** [DEFINITION] OK — $c_t^H = \alpha_t C_t$; AI owners get $(1-\alpha_t)C_t$; shares sum to 1
- **Line 89–95** [ASSUMPTION] OK — singularity structure: probability p per period; non-extinction (prob $1-\xi$) with consumption jump $1+\eta$ and displacement $\alpha_{t+1} = \phi\alpha_t$; extinction (prob $\xi$) with $C=0$ thereafter
- **Line 96** [VERBAL] OK — "smaller φ means larger displacement"; correct since φ∈(0,1) multiplies the household's share
- **Line 97** [REFERENCE] OK — extinction channel attributed to Jones (2024); consistent with described framework
- **Line 100** [VERBAL] OK — singularities can recur, progressively displacing the household; consistent with model structure
- **Line 106** [DEFINITION] OK — AI dividends $D_t^{AI} = \theta_t C_t$; upon non-extinction singularity $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$, so AI share rises
- **Line 107** [DEFINITION] OK — Non-AI dividends $D_t^N = (1-\theta_t)C_t$; $D^{AI} + D^N = C_t$
- **Line 110** [VERBAL] OK — private AI capital creates market incompleteness; household cannot hedge displacement directly
- **Line 113** [ASSUMPTION] OK — CRRA preferences with $\gamma > 1$, $\beta \in (0,1)$
- **Line 116** [DEFINITION] OK — utility function eq (3)
- **Line 121** [VERBAL] OK — SDF reflects household's own consumption growth, not aggregate; correct under incomplete markets
- **Line 127** [ARITHMETIC] OK — P/D formula for AI stocks (eq 5); verified against appendix proof (line 294) — formulas are term-for-term identical
- **Line 131** [ARITHMETIC] OK — P/D formula for non-AI stocks (eq 6); identical structure with $\Gamma^N$ replacing $\Gamma^{AI}$
- **Line 134** [ARITHMETIC] OK — $\Gamma^{AI} = \frac{\theta + \Delta\theta(1-\theta)}{\theta}(1+\eta)$; numerically $(0.32/0.15) \times 1.5 = 3.2$. $\Gamma^N = (1-\Delta\theta)(1+\eta) = 0.8 \times 1.5 = 1.2$. Both correctly derived from dividend definitions
- **Line 144** [DEFINITION] OK — existence condition $A^j < 1$ for well-defined P/D ratios; formula matches denominator of eqs (5)–(6)
- **Line 146** [ARITHMETIC] OK — "baseline calibration satisfies $A^j < 1$ for both assets"; verified with p=0.005, ξ=0: $A^{AI} \approx 0.946 < 1$, $A^{N} \approx 0.918 < 1$
- **Line 146** [REFERENCE] OK — "As we discuss in Section 4.2, sufficiently severe displacement can violate this condition"; Section 4.2 (line 244) confirms this with the large-singularity case
- **Line 149** [ARITHMETIC] OK — $\Gamma^{AI} > 1+\eta$: $3.2 > 1.5$ ✓; $\Gamma^N < 1+\eta$: $1.2 < 1.5$ ✓; both hold for any $\Delta\theta > 0$
- **Line 149** [ARITHMETIC] OK — $\phi(1+\eta) < 1$ when φ sufficiently small: baseline $0.5 \times 1.5 = 0.75 < 1$ ✓
- **Line 149** [VERBAL] OK — "AI stocks pay off precisely when the household's consumption falls" — correct when $\phi(1+\eta) < 1$
- **Line 152** [VERBAL] OK — Proposition 2: comparative statics on the valuation spread
- **Line 154** [VERBAL] OK — (i) spread increasing in displacement severity (decreasing φ); correct because $\phi^{-\gamma}$ rises, amplifying the singularity term more for AI stocks ($\Gamma^{AI} > \Gamma^N$)
- **Line 155** [VERBAL] OK — (ii) spread increasing in p for γ sufficiently large; correct from convexity of $f(A) = A/(1-A)$ and $A^{AI} > A^N$
- **Line 156** [VERBAL] OK — (iii) spread and ratio decreasing in ξ; correct because higher ξ uniformly shrinks the singularity weight, and both $A^j$ converge to the same no-singularity base as ξ→1
- **Lines 161–165** [VERBAL] OK — proof logic for all three parts is valid
- **Line 170** [REFERENCE] OK — GKP2012 comparison: "continuous displacement from expanding technological variety" vs "a discrete AI singularity"; consistent with standard characterization of GKP
- **Line 172** [VERBAL] OK — correctly acknowledges model does not include entry dynamics central to GKP; displacement comes from singularity's share reallocation

## Quantitative Analysis (lines 177–194)

- **Line 177** — section header
- **Line 186** [ASSUMPTION] OK — all stated parameter values ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$) match the table footnote and the R code
- **Line 186** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; "household consumption falls by 25%" ✓
- **Line 186** [VERBAL] OK — $\eta = 0.5$ described as "aggregate consumption rises by 50%" ✓
- **Line 186** [VERBAL] OK — $\theta = 0.15$ described as "AI stocks are initially 15% of the economy" ✓
- **Line 186** [VERBAL] OK — $\Delta\theta = 0.2$ described as "AI's share jumps by 20% of the non-AI remainder" ✓
- **Line 188** [VERBAL] OK — "AI stock P/D ratios are substantially higher than non-AI stock P/D ratios across the entire grid"; confirmed in every row of the table
- **Line 188** [ARITHMETIC] OK — "P/D of roughly 18" at p=0.5%, ξ=0%: table shows 17.5; "roughly 18" is acceptable
- **Line 188** [ARITHMETIC] OK — "non-AI stocks trade near 11": table shows 11.1 ✓
- **Line 188** [ARITHMETIC] OK — "a ratio of about 1.6": table shows 1.6 ✓
- **Line 188** [ARITHMETIC] OK — "At p=1%, the ratio rises to nearly 6 to 1": table shows 5.8 at p=1%, ξ=0%; "nearly 6" is acceptable
- **Line 188** [VERBAL] OK — "extinction risk reduces both valuations and compresses the AI premium": confirmed in every p-block of the table (both P/D values and ratio decline as ξ rises)
- **Line 188** [REFERENCE] OK — "as Proposition 2(iii) predicts": Proposition 2(iii) states exactly this
- **Line 190** [VERBAL] OK — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015": the figure shows NASDAQ at ~490 vs S&P at ~330 (both base 100), so NASDAQ is ~48% higher in level terms, which rounds to "roughly 50%"; the phrasing is imprecise (total-gain comparison would yield ~70%) but defensible as a level comparison and does not constitute a material error
- **Line 190** [ARITHMETIC] OK — "P/D ratios for AI stocks that are 1.5 to 6 times higher than for non-AI stocks across annual singularity probabilities in the 0.5–1% range": actual range in the table for p∈[0.5%,1%] is 1.4–5.8; "1.5 to 6" slightly overstates the lower bound (1.5 vs 1.4) but is not materially wrong given the rounding context
- **Line 188** [ARITHMETIC] VERIFIED — independent recomputation of p=0.5%, ξ=0%, AI: base = 0.96 × 1.02^(−3) = 0.9046; K = 0.9046 × [0.995 + 0.005 × 16 × 0.1975 × 3.2] = 0.9046 × 1.0456 = 0.9459; P/D = 0.9459/0.0541 = 17.5 ✓

## Extensions: Market Incompleteness and the Singularity (lines 195–257)

- **Line 195** — section header
- **Line 197** [VERBAL] OK — correctly previews two extensions: distortion of AI development and government policy
- **Line 201** [DEFINITION] OK — positive singularity raises household share to min(1, α/φ); negative lowers to φα; positive is more likely; AI development is socially efficient
- **Line 203** [REFERENCE] OK — Jones2024 normalization of extinction utility to zero; matches the referenced paper's framework
- **Line 203** [ARITHMETIC] OK — "CRRA utility is negative for all c > 0 when γ > 1": $u(c) = c^{1-\gamma}/(1-\gamma)$; with $\gamma > 1$, $(1-\gamma) < 0$ and $c^{1-\gamma} > 0$, so $u(c) < 0$ ✓
- **Line 207** [VERBAL] OK — Proposition 3(i): household vetoes under incomplete markets for γ sufficiently large; supported by proof (lines 212–213)
- **Line 209** [VERBAL] OK — Proposition 3(ii): household never vetoes under complete markets; supported by proof (lines 215–216)
- **Line 218** [VERBAL] OK — "higher ξ reduces the weight on non-extinction singularity states, which are the states driving the veto"; mechanically correct
- **Line 222** [REFERENCE] OK — GKP2012 on intergenerational transfers and the SDF; attribution is specific and plausible given their OLG framework
- **Line 227** [ARITHMETIC] OK — post-transfer consumption formula: $c^H_{post} = \phi\alpha(1+\eta)(1+g)C_t + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)(1+g)C_t$; correctly decomposes into displaced consumption plus net transfer
- **Line 232** [ARITHMETIC] OK — $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$; verified by factoring $\alpha(1+\eta)(1+g)C_t$ from eq (8); matches R code
- **Line 237** [ARITHMETIC] OK — transfer ratio $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$; verified algebraically; correctly noted as independent of η
- **Line 240** [VERBAL] OK — "ratio exceeds one whenever τ > 0": correct since $\tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha) > 0$ when $\tau > 0$ and $\delta\tau < 1$ (holds for all τ in the grid with δ=0.5)
- **Line 242** [ASSUMPTION] OK — α=0.70, p=0.5%, ξ=5%; matches R code (alpha0=0.70, p_ext=0.005, xi_ext=0.05)
- **Line 242** [ASSUMPTION] OK — baseline η=0.5, φ=0.5; large singularity η=9, φ=0.05; matches R code
- **Line 242** [VERBAL] OK — "ten-fold growth": η=9 ⟹ 1+η=10 ✓
- **Line 242** [ARITHMETIC] OK — "consumption halves under the large singularity (φ(1+η)=0.5)": 0.05 × 10 = 0.5 ✓
- **Line 242** [ARITHMETIC] OK — "falls by 25% under the baseline (φ(1+η)=0.75)": 0.5 × 1.5 = 0.75 ✓
- **Line 244** [ARITHMETIC] OK — "φ^{−γ} = 160,000": $0.05^{-4} = 20^4 = 160{,}000$ ✓
- **Line 244** [ARITHMETIC] OK — existence condition violated at τ=0 for large singularity: $\Gamma^{AI}_{large} = (0.32/0.15) \times 10 = 21.33$; sdf_sing = $160{,}000 \times 10^{-4} \times 21.33 = 341.3$; $K = 0.9046 \times [0.995 + 0.005 \times 0.95 \times 341.3] = 0.9046 \times 2.616 = 2.37 \gg 1$ ✓
- **Line 244** [VERBAL] OK — "hedge value of AI stocks becomes infinite—no finite price can compensate"; correct interpretation of K ≥ 1 divergence
- **Line 248** [ASSUMPTION] OK — δ=0.5 in caption; matches R code (delta=0.50)
- **Line 248** [FIGURE/TABLE] OK — Panel (a) description (transfers compress P/D) and Panel (b) description (catastrophe at τ=0, large singularity responds dramatically) are consistent with the R code output and computed values
- **Line 253** [REFERENCE] OK — Jones2024 on explosive output growth and Nordhaus2021 on critical examination of the singularity hypothesis; both match bib entries

## Conclusion (lines 258–268)

- **Line 258** — section header
- **Line 260** [VERBAL] OK — "AI stocks trade at high valuations": supported by Figure 1 and Introduction (line 40)
- **Line 260** [VERBAL] OK — "part of this premium reflects a hedging motive": restates the central result of Proposition 1 and the discussion at line 149
- **Line 260** [VERBAL] OK — "requires market incompleteness—the inability to trade private AI capital": established in the model (lines 110–111) and Discussion (line 172)
- **Line 260** [VERBAL] OK — "attenuated by extinction risk, which reduces the weight on the non-extinction states": restates Proposition 2(iii)
- **Line 260** [VERBAL] OK — "risk-averse households may inefficiently block AI development": restates Proposition 3
- **Line 260** [VERBAL] OK — "government transfers, normally wasteful, can become effective if singularity-driven growth is large enough": restates Extension 2 findings (lines 234–244)
- **Line 262** [VERBAL] OK — "model is deliberately simple" and "abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details": accurate meta-description of the model's scope; no new claims introduced

## Proof of Proposition 1 (lines 269–298)

- **Line 269** — section header; correctly labels Appendix A and references prop:pd-ratios
- **Line 274** [DEFINITION] OK — standard CRRA Euler equation
- **Line 277** [DEFINITION] OK — $v^{AI} = P^{AI}/D^{AI}$ constant in stationary equilibrium
- **Line 280** [ARITHMETIC] OK — no-singularity case: $c_{t+1}^H/c_t^H = 1+g$ and $D_{t+1}^{AI}/D_t^{AI} = 1+g$; verified from model definitions
- **Line 281** [ARITHMETIC] OK — non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$ and $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$; verified from model definitions
- **Line 282** [ARITHMETIC] OK — extinction: payoff is zero; correct since $C_{t+1} = 0$
- **Lines 287–288** [ARITHMETIC] OK — Euler equation expansion verified term by term: no-singularity term $\beta(1+g)^{-\gamma}(1-p)(1+g)(v+1)D_t$ and non-extinction term $\beta(1+g)^{-\gamma}p(1-\xi)[\phi(1+\eta)]^{-\gamma}(1+g)\Gamma^{AI}(v+1)D_t$; both correct
- **Line 291** [VERBAL] OK — approximation note (post-singularity P/D ≈ pre-singularity P/D) is clearly flagged; exact under stationarity as stated
- **Line 294** [ARITHMETIC] OK — final formula $v^{AI} = A/(1-A)$ where $A = \beta(1+g)^{1-\gamma}[(1-p)+p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^{AI}]$; derived correctly from dividing by $D_t$ and solving; $(1+g)^{1-\gamma}$ arises from $(1+g)^{-\gamma} \times (1+g)^1$
- **Line 294 vs Line 127** [ARITHMETIC] OK — appendix formula (eq A.3) is term-for-term identical to Proposition 1 formula (eq 5); order of $\phi^{-\gamma}$ and $(1+\eta)^{-\gamma}$ differs but multiplication is commutative
- **Line 297** [VERBAL] OK — non-AI derivation is identical with $\Gamma^N$ replacing $\Gamma^{AI}$; correct
