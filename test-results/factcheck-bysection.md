# tests/factcheck-bysection.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 8m 26s
[ralph-garage/agent-logs/20260411T103039.158237-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.158237-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic, verbal claims, and cross-references verified; no material errors found.

## Introduction (lines 38–72)

- **Line 38** — section header
- **Line 40** [VERBAL] OK — claims NASDAQ has "dramatically outpaced" S&P 500 since 2015, with gap widening since 2023; confirmed by Figure 1
- **Line 44** [FIGURE/TABLE] OK — caption states NASDAQ (solid) and S&P 500 (dashed) normalized to Jan 2015 = 100; figure confirms line styles and normalization; sources (NASDAQ from FRED, S&P 500 from Shiller) match code lines 328, 337
- **Line 49** [DEFINITION] OK — defines negative AI singularity as sudden AI improvement that displaces investor consumption
- **Line 51** [REFERENCE] OK — cites GKP2012 for insight that displacing capital belongs to future innovators; consistent with spec/lit/GKP-2012.md
- **Line 53** [VERBAL] OK — "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks": Table 1 shows ratio = 2.0 at p=1%, ξ=0%
- **Line 53** [VERBAL] OK — "If markets were complete... the displacement-driven premium would largely vanish": with φ_eff→1, the φ^{-γ} term disappears from the SDF, collapsing the spread; a small residual from Γ^AI ≠ Γ^N remains, consistent with "largely"
- **Line 53** [VERBAL] OK — "Extinction risk attenuates this gap": supported by Proposition 2(iii) and Table 1 (ratios decrease with ξ)
- **Line 55** [REFERENCE] OK — cites Proposition 3 for claim that veto reflects inability to share upside; Proposition 3 (line 217) contains this result
- **Line 57** [VERBAL] OK — "Financial market solutions to AI disaster risk are under-discussed": qualitative literature claim, reasonable
- **Line 59** [REFERENCE] OK — section roadmap references Sections 2–5; all section labels verified present
- **Line 59** [VERBAL] OK — "all analysis, code, and prose were produced by AI agents from a human-authored economic specification and test scripts": consistent with spec/paper-spec.md §IV.5.c
- **Line 64** [REFERENCE] OK — cites GKP2012 for displacement risk under incomplete markets; accurate characterization
- **Line 66** [REFERENCE] OK — cites Jones2024 for extinction channel; claims "attenuates rather than amplifies," supported by Proposition 2(iii)
- **Line 68** [REFERENCE] OK — literature citations (KoganPapanikolaou2014, KoganPapanikolaouStoffman2020, Knesl2023, AghionJonesJones2019, Acemoglu2025, Barro2006, Wachter2013, PastorVeronesi2009) are standard references for the topics described

## Model (lines 73–184)

- **Line 73** — section header
- **Line 75** — subsection header (Setup)
- **Line 77** [DEFINITION] OK — representative household as marginal investor, AI owners hold private capital
- **Line 77** [REFERENCE] OK — cites GKP2012 for analogy of AI owners as future capital owners
- **Line 77** [VERBAL] OK — "we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group": consistent with model structure
- **Line 80** [DEFINITION] OK — aggregate consumption growth at rate g > 0
- **Line 82–84** [DEFINITION] OK — equation (1): C_{t+1} = (1+g)C_t
- **Line 86** [DEFINITION] OK — household share α_t, consumption c_t^H = α_t C_t; AI owners get (1−α_t)C_t
- **Line 89** [DEFINITION] OK — singularity probability p per period
- **Line 92–94** [DEFINITION] OK — non-extinction singularity: consumption jumps by 1+η, share displaces to φα_t
- **Line 96** [VERBAL] OK — "smaller φ means larger displacement": correct since α_{t+1} = φα_t
- **Line 97** [DEFINITION] OK — extinction probability ξ conditional on singularity; C_{t+1}=0
- **Line 97** [REFERENCE] OK — cites Jones2024 for extinction channel
- **Line 100** [VERBAL] OK — singularities can occur repeatedly, progressively displacing household
- **Line 102–108** [DEFINITION] OK — AI stocks: D^AI = θC, update rule θ_{t+1}=θ+Δθ(1−θ); Non-AI stocks: D^N = (1−θ)C
- **Line 110** [ARITHMETIC] OK — D^AI + D^N = θC + (1−θ)C = C; verified
- **Line 110** [VERBAL] OK — α_t and θ_t are distinct parameters governing different splits; modeling clarification is accurate
- **Line 112** [DEFINITION] OK — restricted equity as source of market incompleteness
- **Line 114** [VERBAL] OK — φ_eff → 1 under complete markets; "displacement-driven valuation premium largely collapses" with "small residual spread from differential dividend growth": verified that with φ_eff=1, Γ^AI=3.2 ≠ Γ^N=1.2 still creates a (much smaller) spread
- **Line 117** [DEFINITION] OK — CRRA preferences with γ > 1, discount factor β
- **Line 119–121** [DEFINITION] OK — equation (3): standard CRRA utility
- **Line 123** — subsection header (Equilibrium prices)
- **Line 125** [VERBAL] OK — SDF reflects household's own consumption growth, not aggregate, due to incomplete markets
- **Line 127–139** [ARITHMETIC] OK — Proposition 1 P/D formulas verified by deriving from Euler equation (Appendix A); Γ^AI = [θ+Δθ(1−θ)]/θ × (1+η); Γ^N = [1−θ−Δθ(1−θ)]/(1−θ) × (1+η) = (1−Δθ)(1+η); with baseline params: Γ^AI=3.2, Γ^N=1.2
- **Line 145–150** [ARITHMETIC] OK — Remark 1: existence condition A^j < 1 verified; baseline A^AI ≈ 0.94 < 1, A^N ≈ 0.92 < 1
- **Line 150** [REFERENCE] OK — "As we discuss in Section 4.2": Section 4.2 (line 242) does discuss existence condition violation
- **Line 153** [VERBAL] OK — closed-form approximation is exact when Δθ→0; Table 1 uses numerically exact values via backward recursion; code confirms both approaches
- **Line 155** [ARITHMETIC] OK — Γ^AI > 1+η since [θ+Δθ(1−θ)]/θ > 1 for Δθ>0, θ<1; Γ^N < 1+η since (1−Δθ) < 1
- **Line 155** [ARITHMETIC] OK — "φ(1+η) < 1 when φ is sufficiently small": with baseline φ=0.5, η=0.5: φ(1+η) = 0.75 < 1
- **Line 157–163** [VERBAL] OK — Proposition 2 comparative statics: (i) decreasing φ widens spread, (ii) increasing p widens spread for large γ, (iii) increasing ξ narrows spread; all supported by Table 1
- **Line 167–171** [ARITHMETIC] OK — Proof of Proposition 2: (i) φ^{-γ} increases when φ decreases, amplifying AI more because Γ^AI > Γ^N; (ii) more weight on singularity states favors AI; (iii) A^j/(1−A^j) is convex in A^j, and equal multiplicative reduction in the singularity term reduces A^AI/(1−A^AI) more than A^N/(1−A^N) because A^AI > A^N
- **Line 174** — subsection header (Discussion)
- **Line 176** [REFERENCE] OK — cites GKP2012 for growth stocks hedging displacement risk; accurate characterization
- **Line 178** [VERBAL] OK — complete markets → φ_eff → 1; "valuation spread would collapse" with residual from Γ^AI ≠ Γ^N; echoes GKP2012's point about future innovators' untradeable rents
- **Line 180** [VERBAL] OK — existence condition violation has no analog in GKP's continuous-displacement framework; discrete singularity creates discontinuity from finite to infinite hedging demand; verified that large singularity violates A^j < 1

## Quantitative Analysis (lines 185–202)

- **Line 185** — section header
- **Line 187–192** [FIGURE/TABLE] OK — Table 1 (table-pd-ratios.tex) confirmed present in exhibits/
- **Line 194** [ASSUMPTION] OK — β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2; all match code lines 18–24
- **Line 194** [ARITHMETIC] OK — "household retains half of its consumption share" (φ=0.5 → α_{t+1}=0.5α_t): correct
- **Line 194** [ARITHMETIC] OK — "φ(1+η) = 0.75": 0.5 × 1.5 = 0.75; verified
- **Line 194** [ARITHMETIC] OK — "household consumption falls by 25%": consumption growth factor = 0.75, so falls by 25%; verified
- **Line 194** [VERBAL] OK — "aggregate consumption rises by 50% in a singularity" (η=0.5): correct
- **Line 194** [VERBAL] OK — "AI stocks are initially 15% of the economy" (θ=0.15): correct
- **Line 194** [VERBAL] OK — "AI's share jumps by 20% of the non-AI remainder" (Δθ=0.2): correct
- **Line 196** [ARITHMETIC] OK — "AI stocks trade at a P/D of about 15.5" at p=0.5%, ξ=0%: Table shows 15.5; recomputed exact value confirms
- **Line 196** [ARITHMETIC] OK — "non-AI stocks trade near 11": Table shows 11.1 at p=0.5%, ξ=0%
- **Line 196** [ARITHMETIC] OK — "ratio of about 1.4": Table shows 1.4 at p=0.5%, ξ=0%
- **Line 196** [ARITHMETIC] OK — "At p=1%, the ratio rises to 2": Table shows 2.0 at p=1%, ξ=0%
- **Line 196** [VERBAL] OK — "extinction risk compresses the AI premium": Table confirms ratios decrease with ξ across all p values
- **Line 196** [REFERENCE] OK — "as Proposition 2(iii) predicts": Proposition 2(iii) states the spread is decreasing in ξ
- **Line 198** [FIGURE/TABLE] OK — "the AI-heavy NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015": Figure 1 shows NASDAQ normalized index ≈ 480 vs S&P ≈ 320 at end of sample, a ratio of ~1.5; "roughly 50% more" is defensible as describing the 50% gap in normalized index levels
- **Line 198** [VERBAL] OK — caveats acknowledged: "NASDAQ is broader than AI stocks," "return differences partly reflect earnings growth," "S&P 500 itself has substantial AI exposure"
- **Line 198** [ARITHMETIC] OK — "AI stock P/D ratios are 1.3 to 2 times those of non-AI stocks across annual singularity probabilities in the 0.5–1% range": Table confirms ratios of 1.3–1.4 at p=0.5% and 1.7–2.0 at p=1%

## Extensions: Market Incompleteness and the Singularity (lines 203–287)

- **Line 203** — section header
- **Line 205** [VERBAL] OK — accurate summary of section content
- **Line 207** — subsection header (Extension 1)
- **Line 209** [DEFINITION] OK — positive singularity: α_{t+1} = min(1, α_t/φ), negative: α_{t+1} = φα_t; q > 1/2
- **Line 211** [VERBAL] OK — "socially efficient in the Kaldor-Hicks sense" when (1+η) > 1: aggregate consumption rises by factor (1+η) in both singularity types, so total surplus is positive regardless of distribution
- **Line 213** [DEFINITION] OK — veto cost κ > 0; permanent fraction of consumption lost
- **Line 213** [ARITHMETIC] OK — "CRRA utility is negative for all c > 0 when γ > 1": u(c) = c^{1−γ}/(1−γ), with 1−γ < 0, so u(c) < 0; extinction utility = 0 > u(c), making veto result conservative (extinction is less bad in utility terms)
- **Line 215** [ASSUMPTION] OK — complete markets consumption = α(1+η)C_t(1+g) in both singularity states: household fully hedges displacement, retaining share α of post-singularity aggregate consumption
- **Line 217–221** [VERBAL] OK — Proposition 3: (i) threshold γ̄ exists for veto under incomplete markets; (ii) no veto under complete markets for small κ
- **Line 225–231** [ARITHMETIC] OK — Proof (i): Δu(γ) formula verified; as γ→∞, the term [φ(1+η)]^{1−γ} → ∞ because φ(1+η) < 1 and 1−γ → −∞, so the negative-singularity cost dominates; formally Δu(γ)/u(α) → +∞
- **Line 233** [ARITHMETIC] OK — Proof (ii): under complete markets, utility gain u(α(1+η)) − u(α) > 0 since η > 0 and u is increasing; household strictly prefers development
- **Line 236** [ASSUMPTION] OK — numerical example parameters: φ=0.5, η=0.5, ξ=5%, p=1%, γ=10, α=0.70, q=0.70, κ=1%; all match code lines 395–399
- **Line 236** [ARITHMETIC] OK — "household vetoes under incomplete markets": V_veto = −15.32 > V_develop = −15.53; verified via code
- **Line 236** [ARITHMETIC] OK — "Under complete markets... household does not veto": V_develop_CM = −13.46 > V_veto = −15.32; verified
- **Line 236** [ARITHMETIC] OK — "positive singularity is more than twice as likely as the negative one": q=0.70 vs 1−q=0.30, ratio = 2.33 > 2
- **Line 236** [VERBAL] OK — "treating the singularity as a one-shot event": code confirms post-singularity values are PVs of deterministic streams
- **Line 236** [VERBAL] OK — "Allowing repeated singularities would reinforce the veto motive": repeated negative singularities compound displacement, worsening expected utility
- **Line 238** [VERBAL] OK — higher ξ reduces veto incentive under conservative normalization (U_ext=0) by reducing weight on non-extinction states; with more severe extinction penalty, higher ξ would amplify veto
- **Line 240** [REFERENCE] OK — cites Jones2024 for wealth-dependent attitudes toward AI risk; complementary channel through financial markets
- **Line 242** — subsection header (Extension 2)
- **Line 244** [REFERENCE] OK — cites GKP2012 for constraint that displacing capital does not yet exist
- **Line 246** [REFERENCE] OK — cites GKP2012 for intergenerational transfers affecting displacement risk
- **Line 248** [DEFINITION] OK — tax rate τ on AI owners' post-singularity consumption; deadweight cost fraction δτ
- **Line 251** [ARITHMETIC] OK — equation (7) verified: c^H_post = φα(1+η)C_t(1+g) + τ(1−δτ)(1−φα)(1+η)C_t(1+g); first term is displaced consumption, second is net transfer from AI owners' share (1−φα)
- **Line 254** [VERBAL] OK — clarifies transfer uses consumption share α, not dividend share θ
- **Line 259** [ARITHMETIC] OK — equation (8) φ_eff = φ + τ(1−δτ)(1−φα)/α; derived by dividing eq (7) by α(1+η)(1+g)C_t; verified numerically (e.g., τ=0.20 gives φ_eff=0.667)
- **Line 262** [VERBAL] OK — φ_eff enters SDF same way as φ, so Proposition 1 applies with substitution
- **Line 264** [VERBAL] OK — "In standard settings (moderate η), deadweight costs eat into the transfer": correct, the net transfer scales with (1−δτ)
- **Line 267** [ARITHMETIC] OK — equation (9): c_post/c_no_transfer = 1 + τ(1−δτ)(1−φα)/(φα); verified by dividing eq (7) by φα(1+η)(1+g)C_t; η cancels, confirming independence from productivity jump
- **Line 270** [ARITHMETIC] OK — "This ratio exceeds one whenever τ > 0": for τ ∈ (0,1) and δ=0.5, (1−δτ) = (1−0.5τ) > 0, so second term is positive
- **Line 272** [ASSUMPTION] OK — figure parameters: γ=4, α=0.70, p=0.5%, ξ=5%, δ=0.5; baseline η=0.5, φ=0.5; large η=9, φ=0.05; all match code lines 183–186, 140
- **Line 272** [ARITHMETIC] OK — "consumption halves under the large singularity (φ(1+η)=0.5)": 0.05×10 = 0.5; verified
- **Line 272** [ARITHMETIC] OK — "falls by 25% under the baseline (φ(1+η)=0.75)": 0.5×1.5 = 0.75; verified
- **Line 272** [FIGURE/TABLE] OK — Figure 2 panel (b) shows catastrophe markers at τ=0 with "50% loss" (large) and "25% loss" (baseline); confirmed in figure
- **Line 274** [ARITHMETIC] OK — "P/D ratio is undefined at τ=0" for large singularity: A^AI = 2.37 > 1, existence condition violated; verified
- **Line 274** [ARITHMETIC] OK — "φ^{-γ} = 160,000": 0.05^{-4} = 20^4 = 160,000; verified
- **Line 274** [FIGURE/TABLE] OK — Figure 2 panel (a) shows "P/D → ∞ as τ → 0" annotation for large singularity; baseline P/D decreases with τ; confirmed in figure
- **Line 274** [VERBAL] OK — "As τ increases... finite P/D ratios emerge": Figure 2 panel (a) confirms large singularity P/D becomes finite at moderate τ
- **Line 283** [REFERENCE] OK — cites Jones2024 for explosive output growth and Nordhaus2021 for critical examination

## Conclusion (lines 288–298)

- **Line 288** — section header
- **Line 290** [VERBAL] OK — summary accurately recapitulates main results: hedging motive, market incompleteness as key driver, extinction risk attenuation, veto distortion, government transfers effective under large singularity growth
- **Line 292** [VERBAL] OK — acknowledges model is "deliberately simple," abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details; accurate characterization of model scope

## Proof of Proposition 1 (lines 299–330)

- **Line 299** — section header (Appendix A)
- **Line 301–305** [ARITHMETIC] OK — standard Euler equation for asset pricing; P_t = E_t[β(c_{t+1}/c_t)^{-γ}(P_{t+1}+D_{t+1})]
- **Line 307** [DEFINITION] OK — v^AI = P^AI/D^AI constant in stationary equilibrium
- **Line 310** [ARITHMETIC] OK — no singularity: consumption growth = 1+g, dividend growth = 1+g; both correct
- **Line 311** [ARITHMETIC] OK — non-extinction singularity: consumption growth = φ(1+g)(1+η); verified from c_{t+1}^H/c_t^H = φα(1+η)(1+g)C_t/(αC_t) = φ(1+η)(1+g). Dividend growth = Γ^AI(1+g); verified from D_{t+1}^AI/D_t^AI = [θ+Δθ(1−θ)](1+η)(1+g)C_t/(θC_t) = Γ^AI(1+g)
- **Line 312** [ARITHMETIC] OK — extinction: c_{t+1}^H = 0, payoff is zero
- **Line 316–321** [ARITHMETIC] OK — Euler equation expansion verified: v^AI D = β(1+g)^{-γ}[(1−p)(1+g)(v+1)D + p(1−ξ)[φ(1+η)]^{-γ}(1+g)Γ^AI(v+1)D]; all SDF and payoff terms correctly substituted
- **Line 323** [ARITHMETIC] OK — "Γ^N = (1−Δθ)(1+η) is θ-independent": algebraically (1−θ−Δθ(1−θ))/(1−θ) = (1−θ)(1−Δθ)/(1−θ) = 1−Δθ; verified numerically (both give 1.2)
- **Line 323** [VERBAL] OK — "so the non-AI closed form is exact": because Γ^N is θ-independent, the post-singularity P/D ratio equals the pre-singularity ratio exactly
- **Line 323** [VERBAL] OK — backward recursion procedure: "starting from a terminal state where θ is close to one and the approximation error vanishes"; code confirms n_steps=60 iterations
- **Line 326–327** [ARITHMETIC] OK — solved closed form v = A/(1−A) where A = β(1+g)^{1−γ}[(1−p)+p(1−ξ)(1+η)^{-γ}φ^{-γ}Γ^AI]; matches equation (4) from Proposition 1
- **Line 329** [VERBAL] OK — "derivation for non-AI stocks is identical, replacing Γ^AI with Γ^N": correct, same structure
