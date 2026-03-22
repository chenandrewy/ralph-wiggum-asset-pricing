# Improvement Plan

## Status
All tests pass. One referee review (referee-top3) with two substantive comments.

## Key Issues

### Referee Comment 1: Hedging channel is second-order at empirical calibrations
At the calibrations that approach the data (Table 2), the hedging amplifier contributes only 13–23% of the combined premium. The paper's framing (title, abstract, intro) foregrounds hedging as the main story, but the calibration tells a growth-differential-dominant story. The referee flags this as a framing tension, not a fatal flaw.

### Referee Comment 2: "Independently testable" claim is unsubstantiated
Section 3.4 proposes a regression but doesn't run it. The referee says either (a) run at least a reduced-form test, or (b) downgrade the language from "independently testable" to "in principle testable" and be transparent about data limitations.

## Plan

### 1. Reframe the hedging channel's quantitative role (addresses Comment 1)

**Goal:** Own the result that the hedging channel is a meaningful but minority contributor at empirical calibrations, rather than toggling between the common-growth showcase and the differential-growth reality.

Changes:
- **Introduction (¶ starting "Our main result"):** Restructure so the differential-growth model (Table 2) is presented as the primary empirical case. The common-growth result (Table 1) should be introduced as the "mechanism isolation" case that shows the hedging channel in pure form. Current text already does this partially but leads with "the hedging channel alone generates a 30% premium" before pivoting to differential growth—flip the ordering.
- **Introduction:** Add 1–2 sentences noting that under more severe but plausible calibrations (γ=5, φ_L=0.35), the hedging share rises substantially and can become the dominant force, with an explicit statement of what parameter combinations make it first-order (high risk aversion + high labor displacement).
- **Calibration section (§3.3):** After Table 1, add a transitional sentence making clear that Table 1 isolates the mechanism; Table 2 is the empirically relevant case.
- **Conclusion:** Adjust "quantitatively meaningful" language to be more precise: "contributes 13–23% of the valuation gap at empirical calibrations, rising substantially under higher risk aversion or labor displacement."

### 2. Downgrade testability language (addresses Comment 2)

**Goal:** Replace "independently testable" with "in principle testable" and be transparent that the paper does not execute the test.

Changes:
- **Introduction:** Change "independently testable force" to "in principle independently testable" or "qualitatively distinct force with testable implications."
- **Section 3.4 (Testable Implications):** Add an explicit caveat paragraph after the regression description acknowledging that (a) the paper does not execute the test, (b) suitable proxies for perceived singularity risk are not yet well-established, and (c) the current evidence (Figure 2) is suggestive but does not isolate the hedging channel from growth revisions. This is mostly already present in the "These patterns are suggestive, not causal" paragraph, but should be strengthened.
- **Section 3.4:** Remove or soften the claim that the hedging channel is "identifiable because it responds to perceived singularity risk, not earnings forecasts"—this is the identifying *restriction*, not something the paper has *demonstrated*.

### 3. Minor tightening

- **Abstract:** If any wording changes from above push the abstract over 100 words, trim accordingly.
- Verify paper stays at ≤ 20 pages after edits.
