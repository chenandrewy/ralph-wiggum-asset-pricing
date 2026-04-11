# tests/factcheck-bysection.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 8m 21s
[ralph-garage/agent-logs/20260411T101504.819902-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260411T101504.819902-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic, verbal, and reference claims verified; no material errors found.

## Introduction (lines 38–72)
- **Line 38** — section header
- **Line 40** [FIGURE/TABLE] OK — References fig:ai-valuations (Exhibit 3), which shows NASDAQ vs S&P 500 normalized to Jan 2015 = 100. Description is consistent with the figure.
- **Line 40** [VERBAL] OK — NASDAQ characterized as "AI- and technology-heavy" is accurate.
- **Line 49** [DEFINITION] OK — "Negative AI singularity" defined consistently with the formal model (lines 89–98).
- **Line 49** [VERBAL] OK — Incomplete markets / hedging motive claim is the paper's central mechanism, confirmed in model (lines 112–114) and Proposition 1.
- **Line 51** [REFERENCE] OK — GKP2012 cited for future innovators whose capital cannot be traded. Consistent with model section (line 77).
- **Line 53** [VERBAL] OK — "P/D ratios can reach roughly twice those of non-AI stocks" confirmed by Table 1: at p=1%, ξ=0%, ratio = 2.0.
- **Line 53** [REFERENCE] OK — Jones2024 cited for extinction risk. Consistent with model (line 97).
- **Line 53** [VERBAL] OK — "Extinction risk attenuates this gap" confirmed by Proposition 2(iii) and Table 1 (ratios decline as ξ increases).
- **Line 55** [REFERENCE] OK — Proposition 3 (prop:veto) at lines 217–222 states exactly the claimed result: household vetoes under incomplete markets for γ large enough; never vetoes under complete markets.
- **Line 55** [VERBAL] OK — "When the positive singularity is more likely than the negative one, AI development is socially efficient" matches line 211 (Kaldor-Hicks efficiency when (1+η)>1) and the assumption q > 1/2.
- **Line 57** [REFERENCE] OK — Jones2024 cited for explosive output growth, consistent with Extension 2 analysis.
- **Line 57** [VERBAL] OK — "Grossly inefficient redistribution delivers large consumption gains" confirmed by eq (12): transfer ratio independent of η, but levels grow without bound.
- **Line 59** [REFERENCE] OK — All section references verified: sec:model → Section 2, sec:quant → Section 3, sec:extensions → Section 4, sec:conclusion → Section 5.
- **Line 64** [REFERENCE] OK — GKP2012 described as modeling displacement from innovation under incomplete markets with OLG structure; accurate characterization.
- **Line 66** [REFERENCE] OK — Jones2024 described as studying AI growth vs. existential risk trade-off; accurate.
- **Line 66** [VERBAL] OK — "Attenuates rather than amplifies" confirmed by Proposition 2(iii) and Table 1.
- **Line 68** [REFERENCE] OK — All citations (KoganPapanikolaou2014, KoganPapanikolaouStoffman2020, Knesl2023, AghionJonesJones2019, Acemoglu2025, Barro2006, Wachter2013, PastorVeronesi2009) accurately characterized in context.

## Model (lines 73–184)
- **Line 73** — section header
- **Line 77** [ASSUMPTION] OK — AI owners as static group, not modeling entry dynamics, with GKP2012 analogy noted.
- **Line 80–84** [DEFINITION] OK — Aggregate consumption growth equation $C_{t+1} = (1+g)C_t$ correctly stated.
- **Line 86** [DEFINITION] OK — $c_t^H = \alpha_t C_t$, AI owners get $(1-\alpha_t)C_t$; sums to $C_t$.
- **Lines 92–96** [DEFINITION] OK — Non-extinction singularity: aggregate jumps by $(1+\eta)$, household share $\alpha_{t+1} = \phi\alpha_t$ with $\phi \in (0,1)$.
- **Line 97** [REFERENCE] OK — Jones2024 cited for extinction risk when AI is powerful. Consistent.
- **Line 106** [DEFINITION] OK — $D_t^{AI} = \theta_t C_t$; post-singularity $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$. With θ=0.15, Δθ=0.2: θ_new = 0.15 + 0.2×0.85 = 0.32.
- **Line 107** [DEFINITION] OK — $D_t^N = (1-\theta_t)C_t$.
- **Line 110** [VERBAL] OK — $D^{AI} + D^N = C_t$ follows directly.
- **Line 117** [ASSUMPTION] OK — CRRA with γ > 1, β ∈ (0,1).
- **Lines 130–138** [ARITHMETIC] OK — P/D ratio formula $v^j = A^j/(1-A^j)$ verified from Euler equation derivation in Appendix (lines 299–327).
- **Line 138** [ARITHMETIC] OK — $\Gamma^{AI} = (0.15 + 0.2×0.85)/0.15 × 1.5 = 0.32/0.15 × 1.5 = 3.2$; $\Gamma^N = (1-0.2) × 1.5 = 1.2$. Both confirmed.
- **Lines 145–151** [VERBAL] OK — Remark 1: P/D well-defined iff $A^j < 1$; follows from $v = A/(1-A)$ requiring $A < 1$ for positive finite values.
- **Line 153** [VERBAL] OK — Approximation (post-singularity P/D = pre-singularity) correctly noted as exact only as Δθ → 0; numerically exact values use backward recursion.
- **Line 153** [ARITHMETIC] OK — $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is θ-independent: $(1-\theta)(1-\Delta\theta)/(1-\theta) = (1-\Delta\theta)$. θ cancels.
- **Line 155** [ARITHMETIC] OK — $\Gamma^{AI} = 3.2 > 1.5 = 1+\eta$. $\Gamma^N = 1.2 < 1.5 = 1+\eta$.
- **Line 155** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 × 1.5 = 0.75 < 1$.
- **Line 155** [VERBAL] OK — Hedging channel logic: high marginal utility in singularity states (consumption falls) combined with higher AI dividend growth produces higher AI P/D ratio. Follows from $A^{AI} > A^N$.
- **Lines 159–160** [VERBAL] OK — Comparative statics (i): spread increasing in displacement severity (decreasing in φ). Confirmed numerically.
- **Line 161** [VERBAL] OK — Comparative statics (ii): spread increasing in p when γ sufficiently large. Confirmed numerically.
- **Lines 162–163** [VERBAL] OK — Comparative statics (iii): spread decreasing in ξ, and ratio also decreasing. Confirmed by Table 1.
- **Lines 167–172** [VERBAL] OK — Proof logic for all three parts of Proposition 2 verified algebraically and numerically.
- **Line 176** [REFERENCE] OK — GKP2012 characterized as modeling continuous displacement from expanding technological variety vs. paper's discrete singularity.
- **Line 178** [VERBAL] OK — "If household could trade restricted equity, φ_eff → 1 and P/D spread vanishes." Economically correct as an intuitive claim: at φ=1, the hedging amplification φ^{-γ} = 1, greatly compressing the spread. Not presented as a formal proposition.
- **Line 180** [VERBAL] OK — Existence-condition discontinuity cannot arise in GKP's gradual displacement framework. Correct by construction.

## Quantitative Analysis (lines 185–202)
- **Line 185** — section header
- **Lines 187–192** [FIGURE/TABLE] OK — Table environment for tab:pd-ratios (Exhibit 1).
- **Line 194** [ASSUMPTION] OK — Parameters (β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2) match the table footnote and code.
- **Line 194** [ARITHMETIC] OK — φ(1+η) = 0.5 × 1.5 = 0.75; "household consumption falls by 25%" is correct (consumption growth factor = 0.75, a 25% decline).
- **Line 194** [ARITHMETIC] OK — η = 0.5 means aggregate consumption rises by 50%.
- **Line 196** [FIGURE/TABLE] OK — "AI stocks trade at a P/D of about 15.5" at p=0.5%, ξ=0%: table shows 15.5.
- **Line 196** [FIGURE/TABLE] OK — "non-AI stocks trade near 11": table shows 11.1.
- **Line 196** [FIGURE/TABLE] OK — "ratio of about 1.4": table shows 1.4.
- **Line 196** [FIGURE/TABLE] OK — "At p=1%, the ratio rises to 2": table shows 2.0 at p=1%, ξ=0%.
- **Line 196** [VERBAL] OK — "Increasing the singularity probability raises the AI stock premium": ratio goes 1.1 → 1.1 → 1.4 → 1.7 → 2.0 across p values at ξ=0%.
- **Line 196** [REFERENCE] OK — "as Proposition 2(iii) predicts": Proposition 2(iii) states the spread decreases in ξ, consistent with the extinction risk discussion.
- **Line 196** [FIGURE/TABLE] OK — "Extinction risk reduces both valuations": at p=1%, as ξ goes 0→5→10→20%, AI goes 26.5→24.8→23.2→20.5, Non-AI goes 13.3→12.9→12.6→12.0.
- **Line 196** [FIGURE/TABLE] OK — "Compresses the AI premium": ratios go 2.0→1.9→1.8→1.7.
- **Line 198** [FIGURE/TABLE] OK — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015": figure shows NASDAQ ~480–490 vs S&P ~330–340 (both normalized to 100), giving a level ratio of ~1.45. "Roughly 50% more" is a reasonable approximation.
- **Line 198** [FIGURE/TABLE] OK — "AI stock P/D ratios are 1.3 to 2 times": table confirms minimum ratio 1.3 (p=0.5%, ξ≥10%) and maximum 2.0 (p=1%, ξ=0%) in the 0.5–1% range.

## Extensions: Market Incompleteness and the Singularity (lines 203–287)
- **Line 203** — section header
- **Line 209** [DEFINITION] OK — Positive singularity: α_{t+1} = min(1, α_t/φ). With α=0.70, φ=0.5: α/φ = 1.4, min(1, 1.4) = 1.0.
- **Line 209** [ASSUMPTION] OK — q > 1/2 assumed (positive singularity more likely).
- **Line 211** [VERBAL] OK — Kaldor-Hicks efficiency holds when (1+η)>1 since aggregate consumption rises in both singularity outcomes.
- **Line 213** [VERBAL] OK — CRRA utility is negative for all c > 0 when γ > 1; normalizing extinction to zero is conservative (understates veto motive).
- **Line 215** [DEFINITION] OK — Complete markets consumption = α(1+η)C_t(1+g) in both singularity states.
- **Lines 228–229** [ARITHMETIC] OK — Δu(γ) formula verified numerically: γ=4 gives Δu > 0 (develop preferred); γ=10 gives Δu < 0 (veto preferred).
- **Line 231** [ARITHMETIC] OK — φα(1+η) = 0.5×0.70×1.5 = 0.525 < 0.70 = α when φ(1+η) = 0.75 < 1.
- **Line 233** [ARITHMETIC] OK — Under complete markets, u(α(1+η)) - u(α) > 0 since u is increasing; household never vetoes.
- **Line 236** [ARITHMETIC] OK — Veto example independently recomputed with all stated parameters (β=0.96, g=0.02, γ=10, φ=0.5, η=0.5, ξ=5%, p=1%, α=0.70, q=0.70, κ=1%): V_veto > V_develop under incomplete markets; V_develop^CM > V_veto under complete markets. Both results confirmed.
- **Line 236** [ARITHMETIC] OK — "Positive singularity more than twice as likely": q/(1-q) = 0.70/0.30 = 2.33 > 2.
- **Lines 250–252** [ARITHMETIC] OK — Transfer consumption formula correctly derived. Deadweight structure (fraction δτ of transferred amount is wasted) is internally consistent.
- **Line 254** [VERBAL] OK — (1-φα) = 1 - 0.5×0.70 = 0.65 is AI owners' post-singularity share.
- **Lines 258–260** [ARITHMETIC] OK — φ_eff = φ + τ(1-δτ)(1-φα)/α follows from dividing eq (6) by α(1+η)(1+g)C_t.
- **Lines 266–268** [ARITHMETIC] OK — Transfer ratio = 1 + τ(1-δτ)(1-φα)/(φα) is η-independent; exceeds 1 for any τ > 0. Verified.
- **Line 272** [ARITHMETIC] OK — Large singularity: φ(1+η) = 0.05×10 = 0.5 (consumption halves). Baseline: φ(1+η) = 0.5×1.5 = 0.75 (falls by 25%).
- **Line 274** [ARITHMETIC] OK — φ^{-γ} = 0.05^{-4} = 20^4 = 160,000.
- **Line 278** [FIGURE/TABLE] OK — Figure parameters (α=0.70, p=0.5%, ξ=5%, δ=0.5) match the code. Baseline (η=0.5, φ=0.5) and large singularity (η=9, φ=0.05) match.
- **Line 283** [REFERENCE] OK — Jones2024 cited for explosive output growth; Nordhaus2021 for critical examination. Consistent with Extension 2 analysis.

## Conclusion (lines 288–298)
- **Line 288** — section header
- **Line 290** [VERBAL] OK — "Hedging motive" is the central thesis, established via Proposition 1 and the model discussion.
- **Line 290** [VERBAL] OK — "Requires market incompleteness" confirmed: line 178 shows spread vanishes under complete markets.
- **Line 290** [VERBAL] OK — "Attenuated by extinction risk" confirmed by Proposition 2(iii) and Table 1.
- **Line 290** [VERBAL] OK — "Risk-averse households may inefficiently block AI development" confirmed by Proposition 3(i).
- **Line 290** [VERBAL] OK — "Government transfers can become effective if singularity-driven growth is large enough" confirmed by Extension 2.
- **Line 292** [VERBAL] OK — "Abstracts from continuous-time dynamics": model is discrete-time.
- **Line 292** [VERBAL] OK — "Heterogeneous beliefs" not modeled.
- **Line 292** [VERBAL] OK — "Production-side details" not modeled; consumption growth and singularity shocks are exogenous.

## Proof of Proposition 1 (lines 299–330)
- **Line 299** — section header
- **Line 304** [ARITHMETIC] OK — Standard CRRA Euler equation correctly stated.
- **Line 310** [ARITHMETIC] OK — No-singularity case: consumption growth = (1+g), AI dividend growth = (1+g). Both correct.
- **Line 311** [ARITHMETIC] OK — Non-extinction singularity: consumption growth = φ(1+g)(1+η), AI dividend growth = Γ^{AI}(1+g). Both verified from model definitions.
- **Line 312** [ARITHMETIC] OK — Extinction case: payoff is zero. Correct.
- **Lines 316–321** [ARITHMETIC] OK — Euler equation substitution correctly assembles SDF × payoff for each state, using the post-singularity P/D approximation.
- **Line 323** [ARITHMETIC] OK — Γ^N = (1-Δθ)(1+η) is θ-independent: (1-θ)(1-Δθ)/(1-θ) = (1-Δθ). θ cancels.
- **Line 326** [ARITHMETIC] OK — Solving v = A(v+1) gives v = A/(1-A). Formula matches equation (2) in Proposition 1.
- **Line 329** [VERBAL] OK — Non-AI derivation identical with Γ^{AI} replaced by Γ^N. Correct by symmetry.
