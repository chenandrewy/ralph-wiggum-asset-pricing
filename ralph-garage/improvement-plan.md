# Improvement Plan

## Current State

All tests pass. The referee-top3 review identifies two substantive issues.

## Key Issues

### Issue 1: Common growth rate assumption creates a narrative–model gap (referee-top3 comment 1)

The model assumes $g^A = g^N = g$, so the AI share $s$ is constant pre-singularity. This causes two problems:

1. **Self-limiting mechanism is a comparative static, not a dynamic prediction.** Proposition 2(ii) and Section 3.4 describe the premium eroding "as the AI share rises," but $s$ never rises in the model. The testable implication points to variation the model cannot generate.

2. **Growth decomposition is informal.** The "approximately multiplicative" claim (Section 3.2) that combines the model's 29% singularity premium with a 3–5pp secular growth differential is not derived. With differential growth, $s_t$ rises over time and feeds back into $J$ and the hedging amplifier, making the interaction potentially non-multiplicative.

### Issue 2: No welfare quantification of the policy lever $\alpha$ (referee-top3 comment 2)

Corollary 1 shows the premium decreases in $\alpha$, but the paper never answers: how much does the household *gain* from increased market access? A consumption-equivalent welfare calculation would make the policy lever concrete and distinguish between "better hedged" and "less risk."

## Plan

### Priority 1: Introduce differential pre-singularity growth (addresses Issue 1)

This is the highest-value change. It resolves the narrative–model gap with a single modeling extension.

**Changes:**

1. **Section 2.2 (The AI Singularity):** Replace the common growth rate $g$ with asset-specific rates $g^A$ and $g^N$ in eq. (4). The AI share $s_t$ now evolves deterministically pre-singularity: $s_{t+1} = s_t (1+g^A) / [s_t(1+g^A) + (1-s_t)(1+g^N)]$.

2. **Section 3.2 (Main Results):** Re-derive Propositions 1–2 with time-varying $s_t$. The P/D ratio becomes a recursive but closed-form expression (standard in dividend-share models). The premium decomposition (eq. 12) still holds at each $t$ with $J(s_t)$ replacing $J(s)$.

3. **Section 3.2 (Calibration):** Replace the informal "approximately multiplicative" decomposition with the model's own combined premium. Calibrate $g^A - g^N = 3\text{–}5$ pp and show the model matches the 2–2.7x data range directly.

4. **Section 3.4 (Testable Implications):** The self-limiting mechanism is now a genuine dynamic prediction: as $s_t$ rises deterministically, the hedging amplifier $J(s_t)^{-\gamma}$ falls. Rewrite this subsection to emphasize the time-series prediction the model now generates.

5. **Tables 1–2:** Recompute with differential growth. Show both the $g^A = g^N$ special case (for comparison) and the general case.

### Priority 2: Add welfare quantification of market access (addresses Issue 2)

**Changes:**

1. **After Corollary 1:** Add a short paragraph (or a new corollary) computing the consumption-equivalent welfare gain from increasing $\alpha$ from 0 to some target value. With CRRA utility, this is closed-form: $\Delta_{CE} = [\tilde{s}(\alpha)/s]^{1/(1-\gamma)} - 1$ type expression from the change in the effective share.

2. **Calibration table:** Add a column to Table 2 showing the welfare gain (in consumption-equivalent units) alongside the premium reduction for each $\alpha$ value.

3. **Conclusion:** Add one sentence noting the welfare quantification.

### Priority 3: Minor polish

1. Ensure the testable-implications figure caption and text are consistent with the new dynamic $s_t$ story.
2. Check that all comparative statics in Proposition 2 still hold with time-varying $s_t$ (they should, since the results hold pointwise at each $t$).
