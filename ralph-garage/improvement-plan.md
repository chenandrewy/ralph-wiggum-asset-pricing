# Improvement Plan

## Current Status

- **Tests:** 2/2 pass (spec-compliance, theory-correctness)
- **Referee (referee-top3):** 2 substantive comments — narrative framing and model-data gap

No section needs an overhaul. The model is correct, the spec is satisfied, and the extensions already address the CFR-R1 referee report. The two referee-top3 comments are targeted and addressable without structural changes.

---

## Issues and Changes

### 1. Reframe the hedging channel's quantitative role (referee-top3 comment 1)

**Problem:** The introduction says "incomplete markets roughly double the premium relative to expected cash flows alone," which is true at baseline ($g^A = g^N$) but misleading for the calibrations that actually match the data (Table 2), where the hedging share is only 13–23%. The narrative frames hedging as the headline mechanism, but growth differentials do most of the quantitative work.

**Changes:**

- **Introduction (paragraph 2, ~line 39):** Replace "incomplete markets roughly double the premium relative to expected cash flows alone" with language that positions hedging as a *distinct, additional* channel operating on top of growth, identifiable because it responds to singularity risk rather than earnings expectations. Something like: "We decompose the AI valuation premium into a cash-flow component and a hedging amplification component. The hedging channel is a distinct force that operates on top of growth expectations and is identifiable because it responds to perceived singularity risk, not earnings forecasts."

- **Introduction (paragraph starting ~line 52):** Adjust the sentence about approaching the observed 2–2.7× gap. Currently it buries the hedging share in Table 2. Add a brief acknowledgment: "At these calibrations, the growth differential accounts for most of the premium, but the hedging channel contributes a distinct 13–23% that is driven by singularity risk rather than earnings expectations—a qualitatively different and independently testable force."

- **Conclusion (~line 525):** Align the concluding framing with the reframed introduction. Currently says "The hedging channel is quantitatively significant because the singularity devastates labor income." Add nuance: the hedging channel is quantitatively meaningful and qualitatively distinct, providing a testable prediction that separates singularity risk from growth expectations.

### 2. Acknowledge the constant-λ gap in the testable implications section (referee-top3 comment 2)

**Problem:** Section 3.4 and Figure 2 argue that AI valuation spikes at GPT-3 and ChatGPT milestones are "consistent with the hedging channel, in which a perceived increase in singularity risk bids up AI stocks." But the model has constant λ—there is no learning or belief updating. The model's sharpest testable implication (AI premium co-moves with perceived singularity risk) is not a formal prediction of the model.

**Changes:**

- **Section 3.4 (Testable Implications, ~line 362–373):** Add a paragraph explicitly acknowledging the limitation. The current model delivers comparative statics in λ (Proposition 2(i)), which motivate the testable prediction, but does not endogenize λ dynamics. A natural extension would introduce Bayesian learning about λ—even a simple conjugate-prior setup—to generate time-varying risk premia and formal event-study predictions. Frame this as a direction for future work that would tighten the link between the formal model and the empirical patterns.

- **Section 3.4 (~line 364):** Soften "consistent with the hedging channel" to "consistent with the comparative statics of the hedging channel (Proposition 2(i)), which predict that a perceived increase in singularity risk bids up AI stocks—though the current model takes λ as fixed."

### 3. Strengthen the quantitative case for hedging with plausible high-hedging calibrations (referee-top3 comment 1, constructive suggestion)

**Problem:** The referee suggests showing calibrations where the hedging share is larger while remaining empirically plausible, and discussing what parameter values make the hedging channel first-order.

**Changes:**

- **Section 3.2 (Sensitivity, ~line 324–352):** Add 1–2 sentences noting that under more severe but plausible calibrations ($\gamma = 5$, $\phi_L = 0.35$), the hedging amplifier $J^{-\gamma}$ rises substantially (Table 3 already shows $v^A/v^N = 1.89$ for $\gamma = 5$, $\phi = 0.50$, $\phi_L = 0.35$). Explicitly state the hedging share at these calibrations to show it can be first-order. This is already implicit in Table 3 but should be made explicit in the text.
