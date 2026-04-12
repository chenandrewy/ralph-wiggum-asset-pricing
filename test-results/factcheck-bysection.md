# tests/factcheck-bysection.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 5m 33s
[ralph-garage/agent-logs/20260412T095842.938360-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260412T095842.938360-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic, verbal, and reference claims verified; no material errors found.

## Introduction (lines 38–70)

- **Line 38** — section header
- **Line 40** [VERBAL] OK — "S&P 500's price-dividend ratio has reached historically elevated levels" is supported by Figure 1 Panel (a), sourced from Shiller data
- **Line 40** [VERBAL] OK — "AI- and technology-heavy NASDAQ Composite has sharply outpaced the broader market since 2015" — recomputed from FRED: NASDAQ outperformed S&P 500 by ~54% since Jan 2015, consistent with "sharply outpaced"
- **Line 40** [VERBAL] OK — "valuation gap widening since 2023" — consistent with Figure 1 Panel (b) construction (NASDAQ/S&P ratio normalized to Jan 2015 = 100)
- **Line 44** [FIGURE/TABLE] OK — Figure 1 caption correctly describes Panel (a) as S&P 500 trailing P/D from Shiller, Panel (b) as NASDAQ/S&P normalized to Jan 2015 = 100; sources match code (`generate-exhibits.R` lines 316, 346)
- **Line 49** [VERBAL] OK — "investors use AI stocks to partially insure against displacement" — accurately summarizes the model mechanism (hedging channel from Proposition 1)
- **Line 49** [REFERENCE] OK — cites GKP2012 for the claim that displacing capital often belongs to future innovators; consistent with spec item I.4.d
- **Line 51** [REFERENCE] OK — "build on GKP2012's framework" — the model structure follows GKP's displacement-risk/incomplete-markets logic (spec I.6)
- **Line 51** [ARITHMETIC] OK — "at a singularity probability of one percent, P/D ratios for AI stocks roughly double relative to non-AI stocks" — Table 2 at p=1%, ξ=0%: ratio = 2.0; at ξ=5%: ratio = 1.9. "Roughly double" is accurate
- **Line 51** [REFERENCE] OK — "extinction risk (Jones 2024) attenuates the premium" — Proposition 2 proves this; Table 2 confirms ratio decreases as ξ rises
- **Line 51** [VERBAL] OK — "Proposition 2 quantifies this attenuation, showing that the valuation spread narrows as extinction probability rises" — directly stated and proved in Proposition 2 (lines 157–163)
- **Line 51** [VERBAL] OK — "Under complete markets the displacement-driven premium would largely vanish" — discussed in Section 2.3 (line 169), where φ_eff → 1 eliminates the SDF overweighting
- **Line 53** [REFERENCE] OK — "Proposition 3" referenced for veto result — Proposition 3 (lines 208–213) establishes the veto threshold
- **Line 53** [VERBAL] OK — "When the positive singularity is more likely than the negative one, AI development is socially efficient, yet a risk-averse household...may rationally choose to block it" — proved in Proposition 3(i) and illustrated numerically (line 227)
- **Line 55** [VERBAL] OK — "Financial market solutions to AI disaster risk are strikingly under-discussed" — qualitative claim consistent with the paper's positioning
- **Line 57** [REFERENCE] OK — cites Jones2024 for explosive output growth — consistent with spec I.4.e and I.5.d.iii
- **Line 57** [VERBAL] OK — "even grossly inefficient transfers become effective" — supported by Extension 2 analysis (line 261: 3.5× consumption multiple even with δ=0.9)
- **Line 59** [VERBAL] OK — "three linked results" accurately summarized: hedging valuation premium, veto distortion, singularity-driven redistribution
- **Line 59** [REFERENCE] OK — section references (Sections 2–5) correctly point to the sections as described
- **Line 59** [VERBAL] OK — footnote about AI-produced paper — consistent with spec IV.5.c
- **Line 64** [REFERENCE] OK — "builds most directly on GKP2012" — consistent with spec I.6 and the modest characterization in spec I.6.c
- **Line 66** [REFERENCE] OK — cites Jones2024 for growth/existential-risk trade-off and extinction channel — consistent with spec I.4.e
- **Line 66** [REFERENCE] OK — ancillary citations (KoganPapanikolaou2014, Barro2006, Wachter2013, PastorVeronesi2009, etc.) — correctly categorized as related literature on displacement risk, rare disasters, and technological revolutions

## Model (lines 71–175)

- **Line 71** — section header
- **Line 75** [DEFINITION] OK — representative household as marginal investor, AI owners holding private capital, not marginal in public stocks — matches spec I.4.b
- **Line 75** [REFERENCE] OK — "as in GKP2012" for analogy to future capital owners — consistent with spec I.4.d
- **Line 75** [VERBAL] OK — "we do not explicitly model the entry of new cohorts" — correctly disclaims per spec I.4.d
- **Line 78** [DEFINITION] OK — aggregate consumption growth C_{t+1} = (1+g)C_t
- **Line 84** [DEFINITION] OK — household share α_t, consumption c_t^H = α_t C_t; AI owners get remainder
- **Line 87** [DEFINITION] OK — singularity probability p per period; conditional structure correct
- **Line 90–91** [DEFINITION] OK — non-extinction singularity: consumption jumps by (1+η), share drops to φα_t
- **Line 94** [DEFINITION] OK — displacement parameter φ ∈ (0,1); smaller φ = larger displacement
- **Line 95** [DEFINITION] OK — extinction: C_{t+1} = 0 for all subsequent dates
- **Line 95** [REFERENCE] OK — cites Jones2024 for extinction channel
- **Line 101–106** [DEFINITION] OK — AI stocks: D^AI = θ_t C_t, θ updates by Δθ(1−θ_t); Non-AI: D^N = (1−θ_t)C_t
- **Line 108** [DEFINITION] OK — total dividends = aggregate consumption; α_t and θ_t are distinct
- **Line 110** [DEFINITION] OK — restricted equity as source of market incompleteness
- **Line 112** [VERBAL] OK — "Holding AI stocks allows the household to smooth marginal utility across states" — correct description of hedging channel
- **Line 115** [DEFINITION] OK — CRRA preferences with γ > 1, discount factor β
- **Line 123** [VERBAL] OK — "SDF reflects its own consumption growth, not aggregate" — correct for incomplete markets
- **Line 126–137** [DEFINITION] OK — Proposition 1 P/D formulas. Verified: Γ^AI = [(θ+Δθ(1−θ))/θ](1+η) and Γ^N = [(1−θ−Δθ(1−θ))/(1−θ)](1+η). With baseline parameters: Γ^AI = 3.2, Γ^N = 1.2
- **Line 143–149** [DEFINITION] OK — Remark 1: existence condition A^j < 1. Correctly identifies divergence when SDF-weighted growth exceeds discount rate
- **Line 148** [REFERENCE] OK — "As we discuss in Section 4.2, sufficiently severe displacement can violate this condition" — confirmed: Extension 2 shows φ_large^(−γ) = 160,000 violates existence at τ=0
- **Line 151** [VERBAL] OK — closed-form approximation becomes exact as Δθ → 0; numerically exact values computed by backward recursion
- **Line 151** [REFERENCE] OK — "Table 2 reports numerically exact P/D ratios" — confirmed: code uses backward recursion (`compute_pd_ai_exact`)
- **Line 153** [ARITHMETIC] OK — Γ^AI > 1+η since Δθ > 0: (θ+Δθ(1−θ))/θ > 1, so Γ^AI = share_ratio × (1+η) > 1+η. Verified: 3.2 > 1.5
- **Line 153** [ARITHMETIC] OK — Γ^N < 1+η: Γ^N = (1−Δθ)(1+η) = 0.8 × 1.5 = 1.2 < 1.5
- **Line 153** [VERBAL] OK — "AI stocks' payoffs are especially valuable" in singularity states due to high marginal utility (φ^{−γ}) — correct mechanism
- **Line 155** [VERBAL] OK — spread widens with decreasing φ (raises φ^{−γ}) and increasing p — confirmed by Table 2
- **Line 157–163** [ARITHMETIC] OK — Proposition 2 proof verified:
  - A^j decomposition correct: A^j = B[(1−p) + p(1−ξ)SΓ^j]
  - Higher ξ scales down singularity component by (1−ξ) — correct
  - Since Γ^AI > Γ^N, absolute reduction in A^AI is larger — correct
  - f(A) = A/(1−A): f''(A) = 2/(1−A)^3 > 0 — verified
  - Semi-elasticity f'(A)/f(A) = 1/[A(1−A)]: verified; increasing in A for A > 1/2 — verified (derivative is (2A−1)/[A(1−A)]^2 > 0)
  - A^j > 1/2 ⟺ P/D > 1: all Table 2 entries exceed 1 — confirmed (minimum is 9.7)
- **Line 167** [REFERENCE] OK — GKP2012 parallel correctly described: continuous displacement from expanding variety vs. discrete singularity
- **Line 169** [VERBAL] OK — under complete markets, φ_eff → 1 eliminates displacement premium; small residual from Γ^AI ≠ Γ^N remains — logically correct
- **Line 169** [REFERENCE] OK — "echoes GKP2012's point that future innovators' rents cannot be traded" — consistent with spec I.4.d
- **Line 171** [VERBAL] OK — discrete singularity can violate existence (Remark 1), unlike GKP's continuous displacement — logically correct; extreme φ^{−γ} diverges the pricing sum

## Quantitative Analysis (lines 176–193)

- **Line 176** — section header
- **Line 180–183** [FIGURE/TABLE] OK — Table 2 sourced from `exhibits/table-pd-ratios.tex`, generated by `generate-exhibits.R`
- **Line 185** [ASSUMPTION] OK — parameters match code: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2
- **Line 185** [ARITHMETIC] OK — "φ(1+η) = 0.75": 0.5 × 1.5 = 0.75 ✓
- **Line 185** [ARITHMETIC] OK — "household consumption falls by 25%": consumption multiple is 0.75, so 25% fall ✓
- **Line 185** [ARITHMETIC] OK — "aggregate consumption rises by 50%": η = 0.5 means (1+η) = 1.5, i.e., 50% rise ✓
- **Line 185** [VERBAL] OK — "AI stocks are initially 15% of the economy" (θ=0.15) and "AI's share jumps by 20% of the non-AI remainder" (Δθ=0.2) — correctly stated
- **Line 187** [ARITHMETIC] OK — "AI stocks trade at a P/D of about 15.5" at p=0.5%, ξ=0%: recomputed 15.5 ✓
- **Line 187** [ARITHMETIC] OK — "non-AI stocks trade near 11": recomputed 11.1 ✓
- **Line 187** [ARITHMETIC] OK — "ratio of about 1.4": recomputed 1.40 ✓
- **Line 187** [ARITHMETIC] OK — "At p=1%, the ratio rises to 2": recomputed 2.00 (at ξ=0%) ✓
- **Line 187** [VERBAL] OK — "increasing the singularity probability raises the AI stock premium" — confirmed by all rows of Table 2
- **Line 187** [VERBAL] OK — "extinction risk compresses the AI premium, as Proposition 2 predicts" — confirmed: ratio decreases as ξ rises in every p row
- **Line 189** [FIGURE/TABLE] OK — "AI-heavy NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015" — recomputed from FRED/Shiller data: NASDAQ outperformed by ~54%, consistent with "roughly 50%"
- **Line 189** [VERBAL] OK — caveats about imperfect mapping (NASDAQ broader than AI, S&P has AI exposure) are appropriate
- **Line 189** [ARITHMETIC] OK — "AI stock P/D ratios are 1.3 to 2 times those of non-AI stocks across annual singularity probabilities in the 0.5–1% range" — Table 2 confirms: at p=0.5% ratios range 1.3–1.4; at p=1% ratios range 1.7–2.0. The overall range 1.3–2.0 is correct

## Extensions: Market Incompleteness and the Singularity (lines 194–278)

- **Line 194** — section header
- **Line 196** [VERBAL] OK — "baseline model takes market incompleteness as given and studies its pricing implications" — accurate summary
- **Line 200** [DEFINITION] OK — positive singularity: α_{t+1} = min(1, α_t/φ); negative: α_{t+1} = φα_t; q > 1/2 assumed
- **Line 202** [DEFINITION] OK — Kaldor-Hicks efficiency: total surplus positive when (1+η) > 1, which holds since η > 0
- **Line 204** [DEFINITION] OK — veto cost κ: permanent fraction of consumption lost; extinction utility normalized to zero
- **Line 204** [VERBAL] OK — "CRRA utility is negative for all c > 0 when γ > 1" — correct: u(c) = c^{1−γ}/(1−γ) < 0 for γ > 1
- **Line 204** [VERBAL] OK — normalizing extinction to zero "makes the veto result conservative" — correct: since u < 0, setting extinction to 0 (better than any finite consumption utility) makes it harder to veto, not easier
- **Line 206** [DEFINITION] OK — complete markets: household consumption = α(1+η)C_t(1+g) in both singularity states — correct hedging characterization
- **Line 208–213** [DEFINITION] OK — Proposition 3: threshold γ̄ for veto under incomplete markets; no veto under complete markets for small κ
- **Line 216–225** [ARITHMETIC] OK — Proof of Proposition 3:
  - Part (i): Δu(γ) formula correct; as γ→∞, negative term dominates when φ(1+η) < 1 — logically sound
  - Part (ii): complete-markets gain u(α(1+η)) − u(α) > 0 since η > 0 — correct
- **Line 227** [ASSUMPTION] OK — veto numerical example parameters: φ=0.5, η=0.5, ξ=5%, p=1%, γ=10, α=0.70, q=0.70, κ=1% — match code (`generate-exhibits.R` lines 420–425)
- **Line 227** [ARITHMETIC] OK — "the household vetoes under incomplete markets": recomputed V_develop = −15.533, V_veto = −15.322, so V_veto > V_develop ✓ (note: both negative, so −15.322 > −15.533)
- **Line 227** [ARITHMETIC] OK — "Under complete markets...the household does not veto": recomputed V_develop^CM = −13.462 > V_veto = −15.322 ✓
- **Line 227** [VERBAL] OK — "positive singularity is more than twice as likely as the negative one": q=0.70 vs 1−q=0.30, ratio 2.33 > 2 ✓
- **Line 229** [VERBAL] OK — extinction interaction under conservative normalization: higher ξ reduces veto incentive — logically correct since it reduces weight on non-extinction states driving veto
- **Line 231** [REFERENCE] OK — Jones2024 observation about wealth and attitudes toward AI risk — consistent with spec
- **Line 233** — subsection header (Extension 2)
- **Line 235** [REFERENCE] OK — cites GKP2012 for constraint that displacing capital does not yet exist
- **Line 237** [REFERENCE] OK — cites GKP2012 on intergenerational transfers affecting displacement factor magnitude — consistent with spec I.5.d.i–ii
- **Line 239–243** [DEFINITION] OK — transfer model: tax rate τ, deadweight cost δτ, household post-transfer consumption formula. Equation (8) correctly specifies both displaced consumption and net transfer terms
- **Line 245** [VERBAL] OK — notes that (1−φα) is AI owners' share, and transfer is on consumption allocation not dividends — important clarification
- **Line 247–253** [ARITHMETIC] OK — φ_eff derivation: dividing eq (8) by α(1+η)(1+g)C_t yields φ_eff = φ + τ(1−δτ)(1−φα)/α — independently verified algebraically
- **Line 255** [VERBAL] OK — "In standard settings (moderate η), the deadweight costs eat into the transfer" — correct qualitative claim
- **Line 256–259** [ARITHMETIC] OK — transfer ratio c^H_post/c^H_no-transfer = 1 + τ(1−δτ)(1−φα)/(φα) — verified algebraically; (1+η) cancels from numerator and denominator, confirming independence from η
- **Line 261** [ARITHMETIC] OK — "δ = 0.9...net transfers per dollar taxed are only τ(1−δτ), e.g., 0.219 at τ = 0.30": 0.30 × (1 − 0.9 × 0.30) = 0.30 × 0.73 = 0.219 ✓
- **Line 261** [ARITHMETIC] OK — "consumption multiple of 3.5× at τ = 0.30": recomputed 3.52, rounds to 3.5 ✓
- **Line 261** [ARITHMETIC] OK — "0.5× catastrophe without transfers": φ_large × (1+η_large) = 0.05 × 10 = 0.5 ✓
- **Line 261** [ARITHMETIC] OK — "transforms a 50% consumption loss into a 250% gain": from 0.5× to 3.5× (250% above pre-singularity baseline) ✓
- **Line 263** [ASSUMPTION] OK — figure parameters: γ=4, α=0.70, p=0.5%, ξ=5%, baseline η=0.5/φ=0.5, large η=9/φ=0.05 — match code (`generate-exhibits.R` lines 183–186, 140–141)
- **Line 263** [ARITHMETIC] OK — "consumption halves under the large singularity (φ(1+η) = 0.5)": 0.05 × 10 = 0.5 ✓
- **Line 263** [ARITHMETIC] OK — "falls by 25% under the baseline (φ(1+η) = 0.75)": 0.5 × 1.5 = 0.75 ✓
- **Line 265** [ARITHMETIC] OK — "φ^{−γ} = 160,000": 0.05^{−4} = (1/0.05)^4 = 20^4 = 160,000 ✓
- **Line 265** [VERBAL] OK — "pricing sum diverges" at τ=0 for large singularity — correct: extreme φ^{−γ} violates existence condition
- **Line 265** [VERBAL] OK — "As τ increases...existence condition is restored, and finite P/D ratios emerge" — correct: φ_eff increases, reducing φ_eff^{−γ}
- **Line 269** [FIGURE/TABLE] OK — Figure 2 caption accurately describes both panels; parameters match code (δ=0.5 in caption matches `delta <- 0.50` in code line 141)
- **Line 274** [VERBAL] OK — policy implication appropriately nuanced: transfers wasteful normally, but effective under explosive growth
- **Line 274** [REFERENCE] OK — cites Jones2024 and Nordhaus2021 for explosive output growth modeling

## Conclusion (lines 279–289)

- **Line 279** — section header
- **Line 281** [VERBAL] OK — correctly summarizes three main results: hedging premium, veto distortion, transfer effectiveness under singularity growth — all supported by the model and analysis
- **Line 281** [VERBAL] OK — "attenuated by extinction risk, which reduces the weight on non-extinction states" — consistent with Proposition 2
- **Line 283** [VERBAL] OK — "model is deliberately simple" — accurately characterizes the paper's scope per spec IV.8

## Proof of Proposition 1 (lines 290–321)

- **Line 290** — section header
- **Line 292–296** [DEFINITION] OK — Euler equation correctly stated
- **Line 298** [DEFINITION] OK — P/D ratio v^AI constant in stationary pre-singularity equilibrium
- **Line 301** [ARITHMETIC] OK — no singularity: consumption growth = 1+g, dividend growth = 1+g ✓
- **Line 302** [ARITHMETIC] OK — non-extinction singularity: consumption growth = φ(1+g)(1+η); dividend growth = Γ^AI(1+g). Verified: c_{t+1}^H/c_t^H = (φα_t)(1+η)(1+g)C_t / (α_t C_t) = φ(1+η)(1+g) ✓; D_{t+1}^AI/D_t^AI = [θ+Δθ(1−θ)](1+η)(1+g)C_t / (θ C_t) = Γ^AI(1+g) ✓
- **Line 303** [ARITHMETIC] OK — extinction: c_{t+1}^H = 0, payoff is zero ✓
- **Line 307–312** [ARITHMETIC] OK — Euler equation expansion: correctly substitutes the three states with their probabilities and SDF weights
- **Line 314** [VERBAL] OK — post-singularity P/D ratio generally differs due to θ-dependence of Γ^AI; approximation treats it as constant
- **Line 314** [ARITHMETIC] OK — Γ^N = (1−Δθ)(1+η) is θ-independent: (1−θ−Δθ(1−θ))/(1−θ) = (1−θ)(1−Δθ)/(1−θ) = 1−Δθ ✓, so non-AI closed form is exact
- **Line 314** [VERBAL] OK — backward recursion over chain θ_0, θ_1, ... for numerically exact AI P/D — matches code implementation
- **Line 316–318** [ARITHMETIC] OK — solving for v^AI: dividing expanded Euler by D_t^AI, collecting terms with (v^AI+1), yields v^AI = A^AI/(1−A^AI) where A^AI = β(1+g)^{1−γ}[(1−p)+p(1−ξ)(1+η)^{−γ}φ^{−γ}Γ^AI] — matches equation (5) in Proposition 1
- **Line 320** [VERBAL] OK — "derivation for non-AI stocks is identical, replacing Γ^AI with Γ^N" ✓
