# tests/factcheck-bysection.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 5m 54s
[ralph-garage/agent-logs/20260412T093252.143443-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.143443-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic, verbal, and reference claims verified across all sections with no material errors.

## Introduction (lines 38–70)
- **Line 38** — section header
- **Line 40** [FIGURE/TABLE] OK — Figure 1 confirms S&P 500 P/D at historically elevated levels and NASDAQ outpacing S&P 500 since 2015
- **Line 49** [VERBAL] OK — "restricted equity held by founders, early-stage investors" supported by Section 2.1 (line 110)
- **Line 49** [REFERENCE] OK — GKP2012 characterization ("displacing capital belongs to future innovators") consistent with Section 2.3 (line 167)
- **Line 51** [REFERENCE] OK — "representative household is the marginal investor" confirmed at line 75
- **Line 51** [REFERENCE] OK — "closed-form price-dividend ratios" confirmed by Proposition 1 (line 125)
- **Line 51** [ARITHMETIC] OK — "P/D ratios roughly double at p=1%": Table 1 row p=1%, ξ=0% gives ratio=2.0
- **Line 51** [REFERENCE] OK — "extinction risk attenuates the premium": Proposition 2 (line 157) proves spread decreasing in ξ; Table 1 confirms (ratio falls from 2.0 to 1.7 as ξ rises from 0% to 20% at p=1%)
- **Line 51** [REFERENCE] OK — "under complete markets the premium would largely vanish": Section 2.3 (line 169) confirms φ_eff → 1 collapses the premium
- **Line 53** [REFERENCE] OK — "risk-averse household may rationally choose to block" supported by Proposition 3 (line 208)
- **Line 53** [REFERENCE] OK — "positive singularity more likely than negative": Section 4.1 assumes q > 1/2 (line 200)
- **Line 55** [REFERENCE] OK — "deadweight costs scale with transfer size" confirmed by Section 4.2 (lines 237–238)
- **Line 57** [ARITHMETIC] OK — "grossly inefficient transfers become effective": verified numerically (3.5× consumption at δ=0.9, τ=0.30 under large singularity)
- **Line 59** [REFERENCE] OK — section roadmap (Sections 2–5) all labels verified
- **Line 59** [VERBAL] OK — footnote disclosure about AI authorship is a procedural statement, not a verifiable factual claim
- **Line 64** [REFERENCE] OK — GKP2012 characterized as modeling displacement risk under incomplete markets; consistent with Section 2.3
- **Line 66** [REFERENCE] OK — Jones2024 characterized as studying AI growth vs. existential risk; consistent throughout

## Model (lines 71–175)
- **Line 71** — section header
- **Line 75** [DEFINITION] OK — representative household as marginal investor; AI owners hold private capital
- **Line 75** [REFERENCE] OK — GKP2012 analogy (future capital owners) consistent with paper's characterization
- **Line 78** [DEFINITION] OK — aggregate consumption growth at rate g > 0
- **Line 84** [DEFINITION] OK — household share α_t, consumption c_t^H = α_t C_t, AI owners receive (1−α_t)C_t
- **Lines 90–93** [DEFINITION] OK — non-extinction singularity: aggregate jump 1+η, displacement α_{t+1} = φα_t
- **Line 95** [DEFINITION] OK — extinction: C_{t+1}=0; attributed to Jones (2024)
- **Line 104** [DEFINITION] OK — AI dividend dynamics: θ_{t+1} = θ_t + Δθ(1−θ_t)
- **Line 105** [DEFINITION] OK — non-AI dividend D_t^N = (1−θ_t)C_t
- **Line 108** [VERBAL] OK — total public dividends equal aggregate consumption (D^AI + D^N = C_t)
- **Line 136** [ARITHMETIC] OK — Γ^AI = [θ+Δθ(1−θ)]/θ·(1+η) = [0.15+0.17]/0.15·1.5 = 3.2; Γ^N = [1−θ−Δθ(1−θ)]/(1−θ)·(1+η) = 0.68/0.85·1.5 = 1.2
- **Lines 128–134** [DEFINITION] OK — P/D formulas have standard A/(1−A) form with correct A^j definition
- **Lines 144–147** [ARITHMETIC] OK — existence condition A^j < 1 correctly stated for positive finite P/D
- **Line 148** [ARITHMETIC] OK — baseline calibration satisfies A^j < 1: at p=0.5%, ξ=0%, A^AI=0.946, A^N=0.917
- **Line 151** [VERBAL] OK — closed-form approximation (post-singularity v ≈ pre-singularity v) exact as Δθ→0
- **Line 151** [REFERENCE] OK — Table 1 for numerically exact values; Appendix A for derivation
- **Line 153** [ARITHMETIC] OK — Γ^AI=3.2 > 1+η=1.5 > Γ^N=1.2: AI dividends grow faster, non-AI slower
- **Line 153** [ARITHMETIC] OK — φ(1+η)=0.75 < 1: household consumption falls in singularity states
- **Line 155** [VERBAL] OK — spread widens with decreasing φ (higher MU via φ^{−γ}) and increasing p
- **Lines 157–163** [ARITHMETIC] OK — Proposition 2 proof: f(A)=A/(1−A) convex with f″=2/(1−A)³>0; semi-elasticity 1/[A(1−A)] increasing in A for A>1/2; since A^AI>A^N and both >1/2, ratio decreases in ξ. Verified numerically.
- **Line 167** [REFERENCE] OK — GKP2012 comparison (continuous displacement from variety expansion vs. discrete singularity)
- **Line 169** [VERBAL] OK — complete markets: φ_eff→1 collapses displacement premium; residual spread from Γ^AI≠Γ^N acknowledged
- **Line 171** [REFERENCE] OK — existence condition violation cross-references Remark 1 (line 143) correctly
- **Line 171** [VERBAL] OK — discontinuity cannot arise under GKP's gradual displacement (economically sound)

## Quantitative Analysis (lines 176–193)
- **Line 176** — section header
- **Line 185** [ASSUMPTION] OK — parameters β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2 match table footnote exactly
- **Line 185** [ARITHMETIC] OK — φ(1+η)=0.5×1.5=0.75; "household consumption falls by 25%" (1−0.75=0.25)
- **Line 185** [ARITHMETIC] OK — "aggregate consumption rises by 50%": η=0.5 → 1+η=1.5
- **Line 185** [DEFINITION] OK — "AI stocks are initially 15% of the economy" (θ=0.15)
- **Line 185** [DEFINITION] OK — "AI's share jumps by 20% of the non-AI remainder" (Δθ=0.2)
- **Line 187** [FIGURE/TABLE] OK — p=0.5%, ξ=0%: AI P/D=15.5, non-AI P/D=11.1, ratio=1.4; text says "about 15.5", "near 11", "about 1.4" — all confirmed by table
- **Line 187** [FIGURE/TABLE] OK — p=1%, ξ=0%: ratio=2.0; text says "ratio rises to 2" — exact match
- **Line 187** [VERBAL] OK — "increasing singularity probability raises AI premium": confirmed across all ξ columns in table (AI P/D rises faster than non-AI P/D as p increases)
- **Line 187** [VERBAL] OK — "extinction risk compresses the AI premium": at fixed p, ratio falls as ξ increases (e.g., p=1%: 2.0→1.9→1.8→1.7); consistent with Proposition 2
- **Line 189** [FIGURE/TABLE] OK — "NASDAQ appreciated roughly 50% more than S&P 500 since 2015": references Figure 1 Panel (b), which normalizes NASDAQ/S&P ratio to Jan 2015=100
- **Line 189** [VERBAL] OK — "AI stock P/D ratios are 1.3 to 2 times those of non-AI stocks across 0.5–1% range": table confirms range spans 1.3 (p=0.5%, ξ=10–20%) to 2.0 (p=1%, ξ=0%)

## Extensions: Market Incompleteness and the Singularity (lines 194–278)
- **Line 194** — section header
- **Line 200** [DEFINITION] OK — positive singularity: α_{t+1}=min(1, α_t/φ); with φ=0.5, α=0.70 gives min(1,1.4)=1
- **Line 200** [ASSUMPTION] OK — q > 1/2 stated as assumption
- **Line 202** [VERBAL] OK — Kaldor-Hicks efficiency holds when (1+η)>1; since η>0, aggregate consumption rises in both outcomes
- **Line 204** [DEFINITION] OK — veto cost κ > 0, permanent consumption fraction lost
- **Line 204** [ARITHMETIC] OK — "CRRA utility is negative for all c>0 when γ>1": u(c)=c^(1−γ)/(1−γ), numerator positive, denominator negative → u<0. Extinction normalized to zero is conservative.
- **Line 206** [ARITHMETIC] OK — complete markets consumption = α(1+η)C_t(1+g) in both singularity states; R code confirms (line 439)
- **Lines 218–219** [DEFINITION] OK — Δu(γ) = q·u(α⁺(1+η)) + (1−q)·u(φα(1+η)) − u(α); terms correctly specified
- **Line 222** [ARITHMETIC] OK — φ(1+η)=0.75<1: negative singularity is worse than pre-singularity, so utility cost grows without bound as γ→∞
- **Line 224** [ARITHMETIC] OK — complete markets: utility gain u(α(1+η))−u(α)>0 since η>0; household prefers development for any γ>1 with small κ
- **Line 227** [ARITHMETIC] OK — veto example parameters (γ=10, p=1%, κ=1%, φ=0.5, η=0.5, ξ=5%, α=0.70, q=0.70) verified against R code (lines 407–456); R code confirms VETO under incomplete markets, develop under complete markets
- **Line 227** [ARITHMETIC] OK — "positive singularity more than twice as likely": q/(1−q)=0.70/0.30=2.33>2
- **Line 242** [ARITHMETIC] OK — transfer consumption formula: c^H_post = φα(1+η)C_t(1+g) + τ(1−δτ)(1−φα)(1+η)C_t(1+g); matches R code consumption_growth function (lines 145–147)
- **Line 250** [ARITHMETIC] OK — φ_eff = φ + τ(1−δτ)(1−φα)/α; derived by dividing eq(10) by α(1+η)(1+g)C_t; matches R code (line 152)
- **Line 258** [ARITHMETIC] OK — transfer ratio = 1 + τ(1−δτ)(1−φα)/(φα); independent of η as claimed; derived by dividing eq(10) by φα(1+η)C_t(1+g)
- **Line 261** [ARITHMETIC] OK — δ=0.9, τ=0.30: net transfer per dollar = 0.30×(1−0.27)=0.219
- **Line 261** [ARITHMETIC] OK — consumption multiple under large singularity (η=9, φ=0.05): φ(1+η) + τ(1−δτ)(1−φα)/α·(1+η) = 0.5 + 0.219×0.965/0.70×10 = 0.5+3.02 = 3.52 ≈ 3.5×
- **Line 261** [ARITHMETIC] OK — "0.5× catastrophe without transfers": φ(1+η)=0.05×10=0.5
- **Line 261** [ARITHMETIC] OK — "50% consumption loss into 250% gain": 0.5× is 50% loss; 3.5× is 250% gain above baseline
- **Line 261** [VERBAL] OK — δ=0.9 illustration is separate from figure (δ=0.5); text explicitly states "raising the deadweight cost parameter to δ=0.9"
- **Line 263** [ASSUMPTION] OK — figure parameters: γ=4, α=0.70, p=0.5%, ξ=5%; baseline η=0.5/φ=0.5, large η=9/φ=0.05; all match R code
- **Line 263** [ARITHMETIC] OK — "consumption halves under large singularity (φ(1+η)=0.5)": 0.05×10=0.5
- **Line 263** [ARITHMETIC] OK — "falls by 25% under baseline (φ(1+η)=0.75)": 0.5×1.5=0.75
- **Line 265** [ARITHMETIC] OK — "φ^{−γ}=160,000": 0.05^{−4}=20^4=160,000
- **Line 269** [ASSUMPTION] OK — figure caption parameters (α=0.70, p=0.5%, ξ=5%, δ=0.5) match R code globals

## Conclusion (lines 279–289)
- **Line 279** — section header
- **Line 281** [VERBAL] OK — "AI stocks trade at high valuations": supported by Figure 1 and Table 1
- **Line 281** [VERBAL] OK — "hedging motive": central mechanism established in Section 2 (lines 153–154)
- **Line 281** [VERBAL] OK — "requires market incompleteness": established in Section 2.1 (lines 110–112)
- **Line 281** [VERBAL] OK — "attenuated by extinction risk": restates Proposition 2 (line 157)
- **Line 281** [VERBAL] OK — "risk-averse households may inefficiently block AI development": restates Proposition 3 (line 208)
- **Line 281** [VERBAL] OK — "government transfers can become effective if singularity-driven growth is large enough": restates Extension 2 findings (lines 255–261)
- **Line 283** [VERBAL] OK — "model is deliberately simple" and listed abstractions (continuous-time, heterogeneous beliefs, production-side) are accurate self-descriptions of scope

## Proof of Proposition~\ref{prop:pd-ratios} (lines 290–321)
- **Line 290** — section header
- **Lines 292–296** [DEFINITION] OK — Euler equation is standard CRRA asset-pricing condition using household's own consumption growth as SDF
- **Line 298** [VERBAL] OK — v^AI constant in stationary pre-singularity equilibrium: α and θ fixed, so ratio P/D is time-invariant
- **Line 301** [ARITHMETIC] OK — no singularity: c_{t+1}^H/c_t^H = 1+g, D_{t+1}^{AI}/D_t^{AI} = 1+g (α, θ unchanged)
- **Line 302** [ARITHMETIC] OK — non-extinction singularity: c_{t+1}^H/c_t^H = φ(1+g)(1+η); D_{t+1}^{AI}/D_t^{AI} = Γ^{AI}(1+g). Verified from model definitions.
- **Line 303** [ARITHMETIC] OK — extinction: C_{t+1}=0, payoff is zero
- **Lines 309–311** [ARITHMETIC] OK — Euler equation expansion verified: substituting three states yields displayed equation exactly
- **Line 314** [ARITHMETIC] OK — Γ^N = (1−Δθ)(1+η) is θ-independent: (1−θ)(1−Δθ)/(1−θ) = 1−Δθ. Numerically: (1−0.2)×1.5=1.2
- **Line 314** [VERBAL] OK — Γ^{AI} depends on θ (= 1+Δθ(1/θ−1))×(1+η)), necessitating the stationarity approximation for AI stocks
- **Lines 316–318** [ARITHMETIC] OK — dividing by D_t^{AI}: v=A(v+1), solving gives v=A/(1−A). Matches eq(4).
- **Line 320** [VERBAL] OK — non-AI derivation identical with Γ^N replacing Γ^{AI}; same Euler equation, same SDF, only dividend growth factor differs
