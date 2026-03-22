# Improvement Plan

## Current Status

- **Tests**: 2/2 pass (spec-compliance, theory-correctness)
- **Referee**: referee-top3 completed with two substantive comments
- **No overhaul needed**: Model is correct, spec-compliant, and well-structured at 13 pages / 4 exhibits

## Issues

### 1. Misleading parenthetical in Prop 5(ii) proof (theory-correctness minor note)

The proof states "where the singularity becomes more harmful" as theta increases. This is wrong: increasing theta raises J, making the singularity *less* harmful to the household. The hump shape arises because the dividend-differential factor (theta + phi) grows faster than J^{-gamma} declines for small theta. Fix the parenthetical to reflect the correct mechanism.

### 2. Referee: No distinguishing empirical test for the hedging channel (Comment 1)

The paper's only empirical content is Figure 1, which documents the AI valuation premium but doesn't distinguish the hedging channel from a pure growth-expectations story. The referee asks: what observable pattern would be present if hedging operates and absent if only growth drives the premium? The paper has room for one more exhibit (currently 4/6) and is well under the page limit (13/20).

### 3. Referee: Friction-resolution microfoundation disconnected from friction rationale (Comment 2)

Section 2.3 gives three compelling reasons the friction persists (information asymmetry, control/incentives, regulatory barriers). Section 4.3 ignores all three and introduces a generic fixed cost k. The referee wants pi microfounded through at least one of the three stated forces, and wants alpha connected to specific policy levers.

## Plan

### Step 1: Fix Prop 5(ii) proof parenthetical

In the proof of Proposition 5(ii), replace the parenthetical "where the singularity becomes more harmful" with language reflecting the correct mechanism: for small theta, the dividend-differential factor (theta + phi) grows faster than the hedging amplifier J^{-gamma} declines, so the hedging component increases. This is a one-line fix.

### Step 2: Microfound friction resolution through adverse selection (Comment 2)

Replace the generic fixed-cost microfoundation in Section 4.3 with one tied to information asymmetry (the first force in Section 2.3). Specifically:

- AI owners selling private capital face an adverse-selection discount: outsiders cannot evaluate proprietary technology, so they demand a lemon's discount d relative to true value V.
- AI owners share only if the gains from trade exceed the adverse-selection loss: they share when output Y_O is large enough that d/Y_O becomes negligible.
- This gives pi(Y_O) = 1 - d/Y_O (structurally similar but now d is the adverse-selection discount, not a generic cost).
- Add a sentence connecting alpha to specific policy levers: securitization standards reduce information asymmetry (increasing alpha), accredited-investor reform addresses regulatory barriers, and IPO incentives weaken the control motive.

This closes the gap between Sections 2.3 and 4.3 without changing any propositions or proofs (the functional form is the same).

### Step 3: Add a testable implication exhibit (Comment 1)

Add one empirical exhibit (Figure or Table) showing that the AI valuation premium co-moves with a proxy for perceived singularity probability lambda. Candidate approach:

- Construct a time series of AI premium (P/D ratio of AI stocks / P/D ratio of S&P 500) from the existing CRSP/Compustat data.
- Construct a proxy for lambda using AI capability announcement dates or AI-related news intensity (e.g., Google Trends for "artificial general intelligence" or counts of major AI announcements).
- Show a scatter plot or time-series overlay demonstrating that the AI premium spikes around periods of heightened perceived singularity risk, controlling for earnings revisions.
- Add a brief paragraph in Section 3 (after the calibration) interpreting the evidence.

This moves the paper from "consistent with" to "suggestive evidence for" the hedging channel. The key testable distinction: a pure growth story predicts the premium rises with earnings revisions; the hedging story predicts it also rises with perceived singularity risk *conditional on* earnings expectations.
