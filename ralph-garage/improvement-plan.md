# Improvement Plan

## Status

All tests pass. Referee report (referee-top3) raises two issues.

## Key Issues

1. **Testable-implications section is too long and defensive.** Section 3.4 runs ~2 pages plus Figure 2, proposes a test, then immediately concedes it can't be executed and proxies don't exist. The referee reads this as identifying the paper's vulnerability and declining to address it.

2. **Hedging channel is 13–23% at empirical calibrations.** The novel mechanism is second-order at baseline. The paper needs a stronger affirmative case for why this matters.

## Plan

### Change 1: Compress testable-implications section (addresses referee comment 1)

Take **Option B** from the referee: compress Section 3.4's testability discussion to a single short paragraph. Cut Figure 2 (the AI-premium time-series plot). This frees ~1.5 pages and removes the paper's most defensive passage.

Keep:
- The core prediction (premium responds to λ conditional on earnings expectations)
- The self-limiting mechanism as a dynamic prediction
- The expected-returns / business-cycle subsection (this is formal and not defensive)

Cut:
- The extended discussion of why proxies don't exist
- The "we do not execute this test" paragraph
- Figure 2 (suggestive but not dispositive)
- The Bayesian-learning extension suggestion

Rewrite as: one paragraph stating the identifying prediction, acknowledging the empirical challenge in a sentence, and pointing to future work.

### Change 2: Strengthen the value proposition of the hedging channel (addresses referee comment 2)

Add 2–3 sentences in the introduction and/or conclusion making the following explicit arguments (currently left implicit):

- **Policy relevance**: The hedging channel is the *only* component that depends on incomplete markets, so it's the part policy can affect. The welfare gains (ω up to 3.4%) flow entirely through this channel.
- **Qualitative distinctiveness**: The hedging channel generates different predictions (response to singularity-risk shocks vs. earnings revisions), making it empirically distinguishable even if quantitatively modest. A theory paper's contribution can rest on identifying a new mechanism.
- **Lower bound**: The 13–23% range uses conservative φ_L. Evidence from rapid LLM adoption in white-collar tasks since 2023 suggests labor displacement may be higher, pushing φ_L toward values where the hedging channel dominates (>50% at γ=5, φ_L=0.35).

### Change 3: Reallocate freed space

Use the ~1.5 pages freed from compressing Section 3.4 to:
- Expand the policy/welfare discussion (connect welfare gains explicitly to the hedging channel)
- Strengthen the "why this matters" framing from Change 2
- Potentially tighten other prose to stay well within 20 pages
