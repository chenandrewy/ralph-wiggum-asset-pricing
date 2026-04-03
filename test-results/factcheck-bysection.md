# tests/factcheck-bysection.py
Started: 2026-04-02 22:28:07 EDT
Runtime: 6m 11s
[ralph-garage/agent-logs/20260402T222807.268780-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260402T222807.268780-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct and all material claims are supported; only minor verbal imprecisions and one broken figure reference remain.

## Introduction (lines 41–71)

- **Line 41** — section header
- **Line 43** [VERBAL] OK — "AI-related companies collectively gained trillions of dollars in market value, trading at price-dividend ratios far above historical norms" is a broadly acknowledged market fact, though stated without a supporting citation.
- **Line 43** [FIGURE/TABLE] WARNING — `Figure~\ref{fig:ai-valuations}` is cited in running text but the entire figure environment (lines 45–50) is commented out. This produces an unresolved `??` reference in the compiled PDF. The text claims the figure "illustrates this pattern" but the figure does not appear.
- **Line 52** [VERBAL] OK — "displacing traditional businesses and reducing the investor's share of total output" supported by Assumption 1 (line 106) and the dividend-share definitions (eqs. 3–4).
- **Line 52** [VERBAL] OK — "the typical investor cannot buy these assets" matches Section 2.3 (line 126): household cannot invest in private AI capital.
- **Line 54** [REFERENCE] OK — GKP (2012) interpretation of AI owners as future innovators confirmed at line 88.
- **Line 54** [VERBAL] OK — "AI stocks gain a larger share… non-AI stocks shrink… household is displaced" matches Assumptions 1–2 and eq. (6).
- **Line 56** [REFERENCE] OK — "closed form" confirmed by Proposition 1 (line 159). "ratio increases with probability of a singularity" confirmed by Proposition 2 (line 190).
- **Line 56** [VERBAL] OK — hedging mechanism description (high marginal utility + high AI payoff) supported by Δ^{-γ} > 1 and θ̃/θ > 1 in Φ^A.
- **Line 56** [REFERENCE] OK — complete-markets claim confirmed by Proposition 3 (lines 204–218).
- **Line 58** [REFERENCE] OK — frictions-overcome claim confirmed by Remark 2 (line 262) and friction-cost equation (line 258).
- **Line 58** [REFERENCE] OK — extinction risk attenuating premium confirmed by eq. (13) in Section 4.1 (line 238).
- **Line 60** [VERBAL] OK — meta-claim about AI authorship; not verifiable from paper internals but consistent with spec.
- **Line 63** [REFERENCE] OK — GKP (2012) described as showing "innovation creates a systematic risk factor because new entrants capture rents"; consistent with bibliography entry (JFE 2012, "Displacement Risk and Asset Returns").
- **Line 63** [REFERENCE] OK — Garleanu–Panageas (2015) described as OLG asset pricing with heterogeneous agents and finite lives; confirmed by bibliography (JPE 2015).
- **Line 63** [REFERENCE] OK — Kogan–Papanikolaou–Stoffman (2020) described as creative destruction and inequality; confirmed by bibliography (JPE 2020, "Left Behind").
- **Line 63** [REFERENCE] OK — Kogan–Papanikolaou (2014) described as technology shocks and asset prices; confirmed by bibliography (JF 2014, "Growth Opportunities, Technology Shocks, and Asset Prices").
- **Line 63** [REFERENCE] OK — Knesl (2023) described as automation displacing labor with displacement risk premium; confirmed by bibliography (JFE 2023).
- **Line 65** [REFERENCE] OK — Rietz (1988), Barro (2006), Wachter (2013) all present in bibliography.
- **Line 65** [VERBAL] OK — "asymmetric effects across sectors" matches Assumption 2 (θ̃ > θ, ν̃ < ν).
- **Line 67** [REFERENCE] OK — Jones (2024) described as analyzing growth vs. existential risk with curvature of utility; confirmed by bibliography (AER: Insights 2024).
- **Line 67** [REFERENCE] OK — Babina et al. (2024), Pastor–Veronesi (2009), Hobijn–Jovanovic (2001) all confirmed in bibliography with consistent descriptions.

## Model (lines 72–156)

- **Line 72** — section header
- **Line 74** [VERBAL] OK — transition sentence references introduction's intuition about incomplete markets; accurate.
- **Line 78** [DEFINITION] OK — singularity as absorbing event with probability p ∈ (0,1) each period.
- **Lines 79–81** [DEFINITION] OK — normal growth equation Y_{t+1} = (1+g)Y_t.
- **Lines 82–85** [DEFINITION] OK — post-singularity growth g̃ > g. Consistent with calibration (g = 0.02 < g̃ = 0.05).
- **Line 88** [REFERENCE] OK — GKP interpretation of AI owners as future innovators. Paper correctly distinguishes its own "private AI ventures" interpretation from GKP's unborn-cohorts mechanism.
- **Lines 92–96** [DEFINITION] OK — output shares θ, ν, 1−θ−ν with dividend definitions. Self-consistent.
- **Lines 98–101** [DEFINITION] OK — post-singularity shares θ̃, ν̃, 1−θ̃−ν̃.
- **Lines 105–107** [ASSUMPTION] OK — Assumption 1: θ̃+ν̃ < θ+ν. Verified: 0.15+0.30 = 0.45 < 0.05+0.55 = 0.60.
- **Lines 109–111** [ASSUMPTION] OK — Assumption 2: θ̃ > θ and ν̃ < ν. Verified: 0.15 > 0.05 and 0.30 < 0.55.
- **Lines 113–116** [DEFINITION] OK — ω ≡ θ+ν, ω̃ ≡ θ̃+ν̃, Δ ≡ ω̃/ω. Verified: ω = 0.60, ω̃ = 0.45, Δ = 0.75.
- **Line 117** [VERBAL] OK — Assumption 1 equivalent to Δ < 1; definitionally correct.
- **Lines 121–124** [DEFINITION] OK — CRRA utility with γ > 1, β ∈ (0,1). Standard.
- **Lines 126–130** [DEFINITION] OK — budget constraint with two public assets; household excluded from private AI capital.
- **Lines 132–136** [ARITHMETIC] OK — market clearing n_t^A = n_t^N = 1 implies c_t = D_t^A + D_t^N = (θ+ν)Y_t = ωY_t. Arithmetic: 0.05+0.55 = 0.60 = ω. Correct.
- **Lines 138–141** [DEFINITION] OK — standard Euler equation.
- **Line 142** [VERBAL] OK — SDF is high when AI stocks pay well because Δ < 1 lowers c_{t+1}, raising (c_{t+1}/c_t)^{-γ}.
- **Line 146** [VERBAL] OK — P/D ratios constant within each regime because growth rates are deterministic within regime.
- **Lines 148–150** [ASSUMPTION] OK — Assumption 3: (1−p)β(1+g)^{1−γ} < 1 and β(1+g̃)^{1−γ} < 1. Verified: β(1+g)^{1−γ} = 0.96·1.02^{−2} = 0.9227; β(1+g̃)^{1−γ} = 0.96·1.05^{−2} = 0.8707. Both < 1.
- **Line 152** [VERBAL] OK — "automatically satisfied for γ > 1 with positive growth rates" is correct: (1+g)^{1−γ} < 1 when γ > 1 and g > 0.

## Results (lines 157–229)

- **Line 157** — section header
- **Lines 159–176** [DEFINITION] OK — Proposition 1 defines closed-form P/D ratios V_pre^A, V_pre^N, and components R, Φ^A, Φ^N, V_post. Formulas are self-consistent.
- **Lines 178–179** [ARITHMETIC] OK — V_post derivation: V_post = β(1+g̃)^{1−γ}(1+V_post) solves to β(1+g̃)^{1−γ}/[1−β(1+g̃)^{1−γ}]. Correct.
- **Lines 181–185** [ARITHMETIC] OK — Pre-singularity Euler expansion verified step by step. No-singularity state: consumption growth (1+g), dividend growth (1+g), contributes (1−p)R(1+V_pre^A). Singularity state: consumption growth Δ(1+g̃), dividend growth (θ̃/θ)(1+g̃), contributes pΦ^A(1+V_post). Solving gives eq. (7). Derivation for V_pre^N identical with ν̃/ν.
- **Line 188** [VERBAL] OK — Δ^{−γ} > 1 because Δ < 1. Verified: 0.75^{−3} = 2.370.
- **Line 188** [VERBAL] OK — θ̃/θ > 1: verified 0.15/0.05 = 3.
- **Line 188** [VERBAL] OK — ν̃/ν < 1: verified 0.30/0.55 = 0.545.
- **Line 188** [VERBAL] OK — V_pre^A > V_pre^N: verified numerically at p = 0.01 (16.1 > 11.6). Algebraically follows from Φ^A > Φ^N since θ̃/θ > ν̃/ν and same denominator.
- **Line 188** [VERBAL] OK — spread increases with p: confirmed by table (spread = 0.0, 2.4, 4.5, 8.2, 15.9 for increasing p).
- **Lines 190–196** [ARITHMETIC] OK — Proposition 2 condition: ∂V/∂p > 0 iff Φ^A(1+V_post) > R/(1−R). RHS = V_pre^A|_{p=0}. Verified: R/(1−R) = 0.9227/0.0773 = 11.94 = V_A at p = 0. Condition holds at calibration: Φ^A(1+V_post) ≈ 47.9 >> 11.9.
- **Line 195** [VERBAL] OK — condition holds when Δ small, γ large, or θ̃/θ large. All three increase Φ^A(1+V_post) relative to R/(1−R).
- **Lines 204–213** [ARITHMETIC] OK — Proposition 3 hedging premium formula verified. At p = 0.01: V_A − V_CM = 16.098 − 12.896 = 3.202, matching the formula's output exactly.
- **Line 213** [VERBAL] OK — premium increasing in p, θ̃/θ, and 1−Δ. Confirmed numerically (hedge prem = 0%, 13.6%, 24.8%, 42.3%, 73.4%).
- **Line 217** [VERBAL] OK — proof of Proposition 3: complete markets replace Δ^{−γ} with 1 because c_{t+1}/c_t = (1+g̃) instead of Δ(1+g̃). Correct.
- **Line 223** [ARITHMETIC] OK — ω = 0.05+0.55 = 0.60; ω̃ = 0.15+0.30 = 0.45; Δ = 0.45/0.60 = 0.75. All correct.
- **Line 223** [ARITHMETIC] OK — "V_pre^A ≈ 16.1" at p = 0.01: recomputed 16.098. Correct.
- **Line 223** [ARITHMETIC] OK — "V_pre^N ≈ 11.6": recomputed 11.567. Correct.
- **Line 223** [ARITHMETIC] OK — "ratio of roughly 1.4": 16.098/11.567 = 1.392 ≈ 1.4. Correct.
- **Line 223** [ARITHMETIC] OK — "both equal approximately 11.9" at p = 0: recomputed 11.940. Correct.
- **Line 223** [ARITHMETIC] OK — "V_pre^{A,CM} ≈ 12.9": recomputed 12.896. Correct.
- **Line 223** [ARITHMETIC] OK — "hedging premium of about 25%": (16.098−12.896)/12.896 = 24.83% ≈ 25%. Correct.
- **Line 225** [FIGURE/TABLE] OK — Table (Exhibit 2) values independently verified for all five rows:
  - p=0: 11.9/11.9/11.9/0.0/0.0% — recomputed 11.940/11.940/11.940/0.00/0.0%
  - p=0.005: 14.1/11.7/12.4/2.4/13.6% — recomputed 14.136/11.743/12.445/2.393/13.59%
  - p=0.01: 16.1/11.6/12.9/4.5/24.8% — recomputed 16.098/11.567/12.896/4.531/24.83%
  - p=0.02: 19.5/11.3/13.7/8.2/42.3% — recomputed 19.454/11.266/13.668/8.189/42.33%
  - p=0.05: 26.5/10.6/15.3/15.9/73.4% — recomputed 26.512/10.632/15.291/15.880/73.38%
  - All values correct to stated rounding (1 decimal place).

## Extension: Singularity, Extinction, and Frictions (lines 230–270)

- **Line 230** — section header
- **Line 232** [REFERENCE] OK — two extensions (extinction, frictions) drawing on Jones (2024); both delivered.
- **Line 236** [ASSUMPTION] OK — extinction probability q ∈ [0,1) introduced.
- **Lines 237–239** [ARITHMETIC] OK — extinction formula V_pre^{A,q} independently derived: no-singularity contributes (1−p)R(1+V_pre^{A,q}); singularity-no-extinction contributes p(1−q)Φ^A(1+V_post); extinction contributes 0. Solving gives eq. (13). Correct.
- **Line 240** [VERBAL] OK — "reduces the singularity-state contribution by factor (1−q)" directly visible in formula.
- **Line 240** [VERBAL] OK — "In the limit q→1, the singularity contributes nothing" since p(1−q)Φ^A(1+V_post) → 0.
- **Line 240** [VERBAL] OK — extinction-state convention (product of divergent SDF and zero payoff defined as zero) consistent with rare-disasters literature.
- **Line 242** [REFERENCE] OK — Jones (2024) curvature-of-utility characterization consistent with introduction (line 67).
- **Line 242** [VERBAL] OK — "household's consumption… remains a shrinking fraction ω̃ of total output." Minor imprecision: ω̃ is fixed post-singularity, not continuing to shrink. The intended meaning is "remains at the reduced fraction ω̃." Not a material error.
- **Lines 244–246** [ARITHMETIC] OK — Remark 1 limits verified: for γ > 1, (1+g̃)^{1−γ} → 0 as g̃ → ∞, so Φ^A → 0 and V_post → 0. For γ = 1 (log), Φ^A = β·(θ̃/θ)/Δ and V_post = β/(1−β), both independent of g̃. Correct.
- **Line 248** [REFERENCE] OK — connection to Jones (2024) consistent with paper's characterization throughout.
- **Line 252** [REFERENCE] OK — GKP characterized as assuming intergenerational risk-sharing fails due to frictions; consistent with introduction (lines 54, 63).
- **Line 254** [VERBAL] OK — "With no transfers, Δ = ω̃/ω < 1" matches model. "With full transfers, Δ = 1" uses Δ informally to mean effective displacement ratio rather than the model primitive; economically correct.
- **Lines 256–259** [ARITHMETIC] OK — friction cost formula: cost = F + τ(ω−ω̃)Y, fraction of output = F/Y + τ(ω−ω̃). Correct.
- **Line 260** [VERBAL] OK — "As Y→∞, the fixed component vanishes." F/Y → 0. Correct. The condition for positive net surplus (τ < 1) is stated imprecisely as "τ small relative to the transfer amount" but the direction of the argument is correct.
- **Lines 262–264** [VERBAL] OK — Remark 2: "hedging premium is largest for moderate singularities" supported by two limiting cases (small singularity → small premium; extreme singularity → Coase eliminates premium). The inverted-U shape is asserted rather than formally proved, but the two boundary conditions are established.
- **Line 266** [VERBAL] OK — summary connecting GKP displacement risk to Jones singularity analysis; consistent with preceding analysis.

## Conclusion (lines 271–282)

- **Line 271** — section header
- **Line 273** [VERBAL] OK — "Financial market solutions to AI disaster risk are under-discussed" is an editorial claim consistent with introduction framing.
- **Line 273** [VERBAL] OK — "expanding tradeable AI-related claims could reduce the displacement premium" supported by Proposition 3 (hedging premium vanishes under complete markets).
- **Line 273** [VERBAL] OK — "sufficiently abundant post-singularity output can make even modest transfer mechanisms effective" supported by Remark 2 and eq. (15).
- **Line 275** [VERBAL] OK — "omits heterogeneous households, production-side frictions, and endogenous innovation" confirmed by model structure.
- **Line 275** [VERBAL] OK — "hedging premium is largest for moderate singularities" supported by Remarks 1–2 (extreme singularities eliminate premium via utility saturation or abundance).

## Proofs (lines 283–299)

- **Line 283** — appendix header
- **Line 286** [ARITHMETIC] OK — N(p) = (1−p)R + pΦ^A(1+V_post) and D(p) = 1−(1−p)R correctly extracted from eq. (7).
- **Line 288** [ARITHMETIC] OK — quotient rule ∂V/∂p = [N'D−ND']/D² correctly stated.
- **Line 290** [ARITHMETIC] OK — N'(p) = −R + Φ^A(1+V_post) and D'(p) = R. Both correct.
- **Lines 292–294** [ARITHMETIC] OK — numerator expansion verified step by step. Let Φ = Φ^A(1+V_post). Expanding: [−R+Φ][1−(1−p)R] − [(1−p)R+pΦ]R = −R+Φ−RΦ = Φ(1−R)−R. Correct.
- **Line 296** [ARITHMETIC] OK — sign condition Φ^A(1+V_post) > R/(1−R) follows from dividing by (1−R) > 0. The step assumes R < 1, which is implied by the economic requirement that V_pre^A|_{p=0} = R/(1−R) > 0 but is not stated as a separate assumption. Minor gap in exposition, not an error.
- **Line 296** [ARITHMETIC] OK — R/(1−R) = V_pre^A|_{p=0} verified by setting p = 0 in eq. (7).
