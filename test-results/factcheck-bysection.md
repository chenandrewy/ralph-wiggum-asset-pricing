# tests/factcheck-bysection.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 7m 28s
[ralph-garage/agent-logs/20260412T154740.739691-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.739691-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic and proofs are correct; no material errors found; minor verbal imprecisions flagged but none affect the paper's claims.

## Introduction (lines 38–70)

- **Line 38** — section header
- **Line 40** [VERBAL] OK — "S&P 500 P/D has reached historically elevated levels" and "NASDAQ has sharply outpaced the broader market since 2015" supported by Figure 1
- **Line 44** [FIGURE/TABLE] OK — caption accurately describes Panel (a) as S&P 500 trailing P/D from Shiller dataset and Panel (b) as NASDAQ/S&P normalized to Jan 2015 = 100; sources correctly attributed
- **Line 49** [REFERENCE] OK — GKP2012 citation ("displacing capital often belongs to future innovators who have not yet entered the economy") matches their text exactly
- **Line 49** [VERBAL] OK — hedging motive, restricted equity, and valuation premium are all consistent with the model mechanism in Section 2
- **Line 51** [ARITHMETIC] OK — "at a singularity probability of one percent, P/D ratios for AI stocks roughly double relative to non-AI stocks" confirmed by Table 1: at p=1%, ξ=0%, ratio = 2.0
- **Line 51** [REFERENCE] OK — Proposition 2 (prop:comp-statics) confirms extinction attenuates the valuation spread
- **Line 51** [REFERENCE] OK — Jones (2024) citation accurately paraphrased: states with powerful AI have highest existential risk
- **Line 51** [VERBAL] MINOR — "The model delivers closed-form price-dividend ratios" does not note the closed form is an approximation (exact only as Δθ→0); the model section (line 151) discloses this, and Table 1 uses numerically exact values
- **Line 53** [REFERENCE] OK — Proposition 3 (prop:veto) confirms risk-averse household may veto socially efficient AI development under incomplete markets
- **Line 55** [VERBAL] OK — "broader trading of AI equity is blocked by restricted ownership" supported by model setup (line 110); deadweight costs of transfers supported by Extension 2
- **Line 57** [VERBAL] OK — "explosive output growth makes even grossly inefficient transfers effective" supported by Extension 2 analysis (eq. 10 and line 261 numerical illustration)
- **Line 59** [REFERENCE] OK — all three section cross-references resolve correctly (sec:model → Section 2, sec:quant → Section 3, sec:extensions → Section 4)
- **Line 59** [VERBAL] OK — footnote on AI-produced paper accurately describes human contribution as "economic specification and test scripts"
- **Line 64** [REFERENCE] OK — GKP2012 description ("model how innovation displaces existing agents and creates a systematic risk factor under incomplete markets") matches their abstract
- **Line 66** [REFERENCE] OK — Jones (2024) description ("trade-off between AI-driven growth and existential risk") matches his paper; extinction attenuation confirmed by Proposition 2
- **Line 66** [REFERENCE] OK — secondary citations (Kogan-Papanikolaou, Barro, Wachter, Pastor-Veronesi, etc.) attributed to standard topics in the literature

## Model (lines 71–175)

- **Line 71** — section header
- **Line 75** [DEFINITION] OK — discrete-time, infinite horizon, representative household as marginal investor, AI owners hold private capital
- **Line 75** [REFERENCE] OK — GKP2012 analogy (future capital owners) correctly stated; limitation ("we do not explicitly model entry of new cohorts") honestly acknowledged
- **Line 78–81** [DEFINITION] OK — aggregate consumption growth at rate g; equation (1) standard
- **Line 84** [DEFINITION] OK — household share α_t, AI owners get remainder; clean partition
- **Line 87–96** [ASSUMPTION] OK — singularity structure (probability p, non-extinction prob 1−ξ with displacement φ, extinction prob ξ) internally consistent
- **Line 90** [ASSUMPTION] OK — aggregate consumption jumps by (1+η) upon non-extinction singularity
- **Line 95** [REFERENCE] OK — Jones (2024) cited for correlated existential risk; paraphrase accurate
- **Line 104–105** [DEFINITION] OK — AI dividends D^AI = θC_t; post-singularity θ update rule; non-AI dividends D^N = (1−θ)C_t
- **Line 108** [ARITHMETIC] OK — D^AI + D^N = θC_t + (1−θ)C_t = C_t confirmed
- **Line 108** [VERBAL] OK — distinction between α_t (consumption split) and θ_t (dividend split) correctly explained
- **Line 110–112** [VERBAL] OK — market incompleteness from restricted equity; displacement parameter φ governs total consumption share including non-tradeable components
- **Line 115–119** [DEFINITION] OK — CRRA utility with γ>1, discount factor β; standard formulation
- **Line 123** [VERBAL] OK — household SDF reflects its own consumption growth, not aggregate; correct under incomplete markets
- **Line 128–136** [ARITHMETIC] OK — P/D formulas (eqs 4–5) verified: follow from Euler equation with SDF = β[φ(1+η)(1+g)]^{−γ} in singularity states
- **Line 136** [ARITHMETIC] OK — Γ^AI = [θ+Δθ(1−θ)]/θ × (1+η) = [0.15+0.17]/0.15 × 1.5 = 3.2; Γ^N = (1−Δθ)(1+η) = 0.8×1.5 = 1.2
- **Line 143–148** [DEFINITION] OK — existence condition A^j < 1 correctly stated; P/D = A/(1−A) requires A ∈ (0,1)
- **Line 148** [VERBAL] OK — "baseline calibration satisfies A^j < 1 for both assets" confirmed across all 20 table entries
- **Line 148** [REFERENCE] OK — cross-reference to Section 4.2 (sec:ext2) for discussion of transfers when existence condition is violated
- **Line 151** [VERBAL] OK — approximation (post-singularity P/D ≈ pre-singularity) disclosed; exact as Δθ→0; table uses numerically exact backward recursion
- **Line 153** [ARITHMETIC] OK — Γ^AI > 1+η since [θ+Δθ(1−θ)]/θ > 1 when Δθ>0; Γ^N = (1−Δθ)(1+η) < 1+η confirmed
- **Line 153** [VERBAL] OK — "φ(1+η)<1 when φ is sufficiently small" — baseline: 0.5×1.5 = 0.75 < 1
- **Line 153** [VERBAL] OK — hedging channel explanation: AI stocks pay off when household consumption falls, providing partial hedge
- **Line 155** [VERBAL] OK — spread widens with decreasing φ (via φ^{−γ}) confirmed numerically
- **Line 155** [VERBAL] MINOR — "for sufficiently risk-averse households" qualifier on p-effect is conservative; numerically, spread increases with p for all γ tested, so qualifier is unnecessary but not wrong
- **Line 157–163** [ARITHMETIC] OK — Proposition 2 proof verified: (1) higher ξ scales down p(1−ξ)SΓ^j by same factor; (2) |dA^AI/dξ| > |dA^N/dξ| since Γ^AI > Γ^N; (3) f(A) = A/(1−A) has f″ > 0; (4) semi-elasticity increasing in A for A > 1/2; (5) A^j > 1/2 confirmed for all table entries
- **Line 167** [REFERENCE] OK — GKP2012 parallel accurately described; key difference (continuous vs discrete displacement) correctly stated
- **Line 169** [VERBAL] OK — complete markets: with φ_eff→1, P/D ratio ≈ 9.31 vs 9.12 (ratio 1.02), confirming small residual spread from Γ^AI ≠ Γ^N
- **Line 169** [REFERENCE] OK — GKP2012 limitation ("future innovators' rents cannot be traded") accurately attributed
- **Line 171** [VERBAL] OK — existence condition can be violated with severe displacement (confirmed: at φ=0.4, p=0.5%, ξ=0, A^AI > 1); contrast with GKP's continuous displacement is valid

## Quantitative Analysis (lines 176–193)

- **Line 176** — section header
- **Line 185** [ASSUMPTION] OK — all stated parameters (β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2) match table footnote exactly
- **Line 185** [ARITHMETIC] OK — "φ(1+η)=0.75 and household consumption falls by 25%": 0.5×1.5=0.75, so consumption is 75% → 25% fall
- **Line 185** [ARITHMETIC] OK — "η=0.5 (aggregate consumption rises by 50%)" correct
- **Line 185** [ASSUMPTION] OK — "θ=0.15 (AI stocks initially 15%)" and "Δθ=0.2 (share jumps by 20% of non-AI remainder)" match table
- **Line 187** [ARITHMETIC] OK — "p=0.5% with no extinction risk, AI stocks trade at P/D of about 15.5" — table: 15.5 exact
- **Line 187** [ARITHMETIC] OK — "non-AI stocks trade near 11" — table: 11.1
- **Line 187** [ARITHMETIC] OK — "ratio of about 1.4" — table: 1.4
- **Line 187** [ARITHMETIC] OK — "At p=1%, the ratio rises to 2" — table at p=1%, ξ=0%: ratio = 2.0
- **Line 187** [VERBAL] OK — "increasing singularity probability raises the AI stock premium" confirmed: ratio monotonically increases with p across the table
- **Line 187** [VERBAL] OK — "extinction risk compresses the AI premium, as Proposition 2 predicts" confirmed: ratio decreases with ξ in every p-row of the table
- **Line 189** [VERBAL] OK — "NASDAQ has appreciated roughly 50% more than S&P 500 since 2015" — figure Panel (b) is normalized to Jan 2015=100; the exact reading depends on data vintage but is broadly consistent with NASDAQ outperformance
- **Line 189** [VERBAL] OK — mapping caveats ("NASDAQ is broader than AI stocks," "return differences partly reflect earnings growth," "S&P 500 itself has substantial AI exposure") appropriately noted
- **Line 189** [ARITHMETIC] OK — "AI stock P/D ratios are 1.3 to 2 times those of non-AI stocks across probabilities in 0.5–1% range" — table confirms: ranges from 1.3 (p=0.5%, ξ=20%) to 2.0 (p=1%, ξ=0%)

## Extensions: Market Incompleteness and the Singularity (lines 194–278)

- **Line 194** — section header
- **Line 196** [VERBAL] OK — "each extension branches directly off the baseline model" consistent with paper structure
- **Line 200** [DEFINITION] OK — positive singularity: α_{t+1} = min(1, α_t/φ); with α=0.70, φ=0.5: min(1, 1.4) = 1.0; q > 1/2 assumed
- **Line 202** [VERBAL] OK — "socially efficient in Kaldor-Hicks sense" when (1+η) > 1, since aggregate consumption rises; correct as η > 0
- **Line 204** [VERBAL] OK — extinction utility = 0; CRRA utility negative for c > 0 when γ > 1 (since (1−γ) < 0); veto result is conservative
- **Line 206** [DEFINITION] OK — complete markets: household hedges fully, consumes α(1+η)C_t(1+g) in both singularity states
- **Line 208–213** [VERBAL] OK — Proposition 3 structure: (i) veto under incomplete markets for γ large enough; (ii) no veto under complete markets for κ small enough
- **Line 222** [ARITHMETIC] OK — proof logic: as γ→∞, negative-singularity utility dominates because φ(1+η)<1; Δu(γ)→−∞ while veto cost κ is fixed
- **Line 224** [ARITHMETIC] OK — under complete markets, utility gain u(α(1+η))−u(α) > 0 since η > 0; household prefers development
- **Line 227** [ARITHMETIC] OK — numerical veto example verified: γ=10, p=1%, κ=1%, φ=0.5, η=0.5, ξ=5%, α=0.70, q=0.70
  - Incomplete markets: V_veto > V_develop (household vetoes) ✓
  - Complete markets: V_develop^CM > V_veto (no veto) ✓
  - "Positive singularity more than twice as likely": q/(1−q) = 0.70/0.30 = 2.33 > 2 ✓
- **Line 229** [VERBAL] OK — extinction risk interaction with veto correctly described; conservative normalization reduces veto incentive
- **Line 231** [REFERENCE] OK — Jones (2024) two channels (risk aversion and consumption levels) accurately described; complementary channel through financial markets correctly framed
- **Line 237** [REFERENCE] OK — GKP2012 observation about bequests and gifts correctly attributed; the paper extends beyond this by analyzing government transfers with deadweight costs
- **Line 239** [DEFINITION] OK — tax rate τ on AI owners' post-singularity consumption; deadweight cost fraction δτ
- **Line 242** [ARITHMETIC] OK — eq (8): c^H_post = φα(1+η)C_t(1+g) + τ(1−δτ)(1−φα)(1+η)C_t(1+g); first term is displaced consumption, second is net transfer; (1−φα) correctly represents AI owners' share
- **Line 250** [ARITHMETIC] OK — eq (9): φ_eff = φ + τ(1−δτ)(1−φα)/α; follows from dividing eq (8) by α(1+η)(1+g)C_t
- **Line 253** [VERBAL] OK — φ_eff enters SDF same way as φ; P/D formula applies with φ replaced by φ_eff
- **Line 258** [ARITHMETIC] OK — eq (10): transfer ratio = 1 + τ(1−δτ)(1−φα)/(φα); derived by dividing eq (8) by no-transfer consumption φα(1+η)C_t(1+g); (1+η) cancels, making ratio η-independent
- **Line 258** [VERBAL] OK — "ratio exceeds one whenever τ > 0 and δτ < 1": since (1−φα) > 0 and φα > 0, the added term is positive
- **Line 261** [ARITHMETIC] OK — δ=0.9 illustrative example (separate from figure which uses δ=0.5):
  - "net transfers per dollar taxed are τ(1−δτ), e.g., 0.219 at τ=0.30": 0.30×(1−0.9×0.30) = 0.30×0.73 = 0.219 ✓
  - "consumption multiple of 3.5× at τ=0.30": φ(1+η) + τ(1−δτ)(1−φα)/α × (1+η) = 0.5 + 0.219×0.965/0.70×10 = 0.5 + 3.02 = 3.52 ≈ 3.5 ✓
  - "0.5× catastrophe without transfers": φ(1+η) = 0.05×10 = 0.5 ✓
  - "50% consumption loss into 250% gain": 0.5× = 50% loss; 3.5× = 350% of pre-singularity = 250% gain ✓
- **Line 263** [ARITHMETIC] OK — "ten-fold growth": (1+η)=10 ✓; "consumption halves (φ(1+η)=0.5)": 0.05×10=0.5 ✓; "falls by 25% (φ(1+η)=0.75)": 0.5×1.5=0.75 ✓
- **Line 263** [ASSUMPTION] OK — figure parameters (γ=4, α=0.70, p=0.5%, ξ=5%) match code exactly
- **Line 265** [ARITHMETIC] OK — φ^{−γ} = 0.05^{−4} = 20^4 = 160,000 ✓
- **Line 265** [VERBAL] OK — "hedge value of AI stocks becomes infinite—no finite price can compensate" consistent with existence condition violation when A^j ≥ 1
- **Line 269** [FIGURE/TABLE] OK — caption parameters δ=0.5 match code (delta <- 0.50); Panel (a) description of undefined P/D at low τ confirmed by code (returns NA); Panel (b) catastrophe markers confirmed
- **Line 274** [REFERENCE] OK — Jones (2024) and Nordhaus (2021) citations in policy discussion; appropriately hedged

## Conclusion (lines 279–289)

- **Line 279** — section header
- **Line 281** [VERBAL] OK — "AI stocks trade at high valuations" supported by Figure 1 and Table 1
- **Line 281** [VERBAL] OK — "hedging motive" is the paper's core mechanism from Proposition 1
- **Line 281** [VERBAL] OK — "requires market incompleteness" stated in model (line 110)
- **Line 281** [VERBAL] OK — "attenuated by extinction risk" proved in Proposition 2
- **Line 281** [VERBAL] OK — "risk-averse households may inefficiently block AI development" proved in Proposition 3
- **Line 281** [VERBAL] OK — "government transfers can become effective if singularity-driven growth is large enough" supported by Extension 2 analysis
- **Line 283** [VERBAL] OK — "abstracts from continuous-time dynamics": model is discrete-time (line 75) ✓; "heterogeneous beliefs": no belief heterogeneity modeled ✓; "production-side details": aggregate consumption is exogenous ✓

## Proof of Proposition 1 (lines 290–321)

- **Line 290** — section header
- **Line 292–296** [DEFINITION] OK — Euler equation standard for CRRA household pricing
- **Line 298** [ASSUMPTION] OK — v^AI = P^AI/D^AI treated as constant; correctly labeled as approximation
- **Line 301** [ARITHMETIC] OK — no-singularity: c_{t+1}^H/c_t^H = (1+g); D_{t+1}^AI/D_t^AI = (1+g)
- **Line 302** [ARITHMETIC] OK — non-extinction singularity: c_{t+1}^H/c_t^H = φ(1+g)(1+η); D_{t+1}^AI/D_t^AI = Γ^AI(1+g)
- **Line 303** [ARITHMETIC] OK — extinction: payoff zero
- **Lines 309–311** [ARITHMETIC] OK — Euler equation expansion verified: no-singularity term = (1−p)β(1+g)^{−γ}(v^AI+1)(1+g)D_t^AI; singularity term = p(1−ξ)β(1+g)^{−γ}[φ(1+η)]^{−γ}(1+g)Γ^AI(v^AI+1)D_t^AI; factoring β(1+g)^{−γ} is correct
- **Lines 316–318** [ARITHMETIC] OK — dividing by D_t^AI, letting A = β(1+g)^{1−γ}[(1−p)+p(1−ξ)(1+η)^{−γ}φ^{−γ}Γ^AI]: v = A(v+1) → v = A/(1−A); matches eq (4)
- **Line 314** [ARITHMETIC] OK — Γ^N = [(1−θ)(1−Δθ)]/(1−θ)×(1+η) = (1−Δθ)(1+η) is θ-independent; non-AI closed form is exact
- **Line 314** [ARITHMETIC] OK — Γ^AI = [θ+Δθ(1−θ)]/θ×(1+η) depends on θ; approximation exact as Δθ→0
- **Line 320** [VERBAL] OK — non-AI derivation identical with Γ^N replacing Γ^AI
