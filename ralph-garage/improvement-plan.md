# Improvement Plan

## Current Status
- **Tests**: All pass (spec-compliance, theory-correctness).
- **Referee reviews**: referee-top3 completed; CFR-R1 report on file.

## Key Issues

### From referee-top3
1. **Quantitative gap is the central vulnerability.** The model produces a 29% hedging premium at λ=0.02, but Figure 1 shows AI stocks at 2–2.7× the market P/D. The paper hand-waves the residual as "differential growth expectations" without formal analysis. A top journal will reject on this alone.
2. **Incomplete-markets friction is too stark.** The all-or-nothing assumption (AI owners completely absent from public markets) is empirically counterfactual. A graded participation parameter in the main model would improve credibility.

### From CFR-R1
1. **Model is perceived as subsumed by GKP.** The referee views the main model as a special case of GKP where growth stocks fully hedge displacement risk. The paper needs to sharpen the distinction — the friction is about asset accessibility (contemporaneous agents, private capital), not intergenerational non-existence.
2. **Extensions address Jones (2024) well.** The referee's suggestion to incorporate heterogeneous beliefs and existential risk is already implemented in Section 4. This is a strength.

## Plan

### 1. Add heterogeneous growth rates to close the quantitative gap
**Section 3.3 (Calibration) + new content.**
- Extend the calibration to allow differential expected dividend growth ($g^A \neq g^N$) for AI vs. non-AI stocks. This nests the pure-growth benchmark and the pure-hedging benchmark.
- Show a decomposition: at plausible growth differentials (e.g., $g^A - g^N$ = 3–5%), the combined growth + hedging premium can match the 2–2.7× observed ratio.
- Add a back-of-the-envelope calculation: given the 29% hedging premium, what growth differential is implied by the residual? Assess whether it is empirically plausible.
- This directly addresses referee-top3 comment #1 and strengthens the paper's quantitative claim.

### 2. Introduce partial market access (α) in the main model
**Section 2.3 (Incomplete Markets) + Propositions.**
- Parameterize the degree of market incompleteness: the household can access a fraction α ∈ [0,1] of total AI capital, with α=0 recovering the current model and α=1 giving complete markets.
- This adjusts the effective AI share from $s$ to $s + α(1-s)$ or similar, modifying $J(s)$ and the premium continuously.
- Show how the premium degrades gracefully with market access. This gives the policy discussion (broadening access to private AI capital) a formal backbone.
- Addresses referee-top3 comment #2 and strengthens the GKP differentiation (our friction has a natural continuous relaxation; their intergenerational friction does not).

### 3. Sharpen the GKP differentiation
**Section 1 (Introduction) + Section 2.3.**
- Rewrite the GKP discussion to emphasize three concrete differences:
  (a) The friction source: asset accessibility (private capital) vs. non-existence of future cohorts.
  (b) The policy implication: our friction is reducible via financial innovation (securitization, IPOs); GKP's is structural.
  (c) The partial-access parameter α (from item 2 above) gives a continuous policy lever that has no analogue in GKP.
- This directly addresses CFR-R1 comment #1.

### 4. Sensitivity analysis across key parameters
**New Table or expanded Table 1.**
- Show how the premium varies across γ, s, ϕ, θ at the baseline λ=0.02.
- Demonstrate that reasonable alternative calibrations (e.g., higher γ or larger ϕ) bring the model premium substantially closer to the data.
- Complements the growth decomposition in item 1.

### Priority Order
1. Heterogeneous growth rates (item 1) — highest impact, directly addresses the "central vulnerability."
2. Partial market access α (item 2) — strengthens both credibility and GKP differentiation.
3. GKP differentiation prose (item 3) — low effort, high value.
4. Sensitivity analysis (item 4) — supporting evidence for quantitative claims.
