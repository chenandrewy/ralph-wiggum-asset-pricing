# Improvement Plan

## Status

All tests pass (spec-compliance, theory-correctness). One referee review (referee-top3) with two comments.

## Referee Comments Summary

1. **Event study identification**: The six events don't cleanly identify singularity-risk shocks. Most events simultaneously signal AI economic importance (bullish for growth), not just tail risk. The CAIS extinction statement is the cleanest event; the others are confounded. The referee wants either sharper identification or honest reframing.

2. **AI-specificity vs generic disaster risk**: A 19% consumption drop looks like a generic rare disaster. Why does the hedging premium accrue to AI stocks specifically, rather than Treasuries, gold, or defensive equities? The two-asset model makes AI stocks mechanically the only hedge. The referee also asks how the premium scales if the singularity is gradual (many small steps) rather than one large jump.

## Plan

### Change 1: Reframe the event study as suggestive evidence with an explicit identification caveat

**Where**: Section 3.3, the paragraph introducing the event study and the paragraph interpreting Table 4.

**What to do**:
- Add 1-2 sentences acknowledging the confound: most events simultaneously signal AI economic importance, which revises growth expectations upward, not just singularity probabilities. Only the CAIS extinction statement is a clean singularity-risk shock.
- Reframe the event study from a "preliminary test" to "suggestive evidence consistent with" the hedging channel. Do not claim it identifies the channel.
- Add a sentence describing what *would* constitute a clean test: events that are unambiguously bad news for AI (safety incidents, capability failures) yet generate positive AI abnormal returns. That would be a smoking gun.
- Remove or soften the claim that "none of the six events coincided with earnings announcements or analyst forecast revisions" as sufficient for identification—acknowledge that absence of concurrent analyst revisions does not mean the events are uninformative about future cash flows.

### Change 2: Add a short discussion distinguishing AI singularity risk from generic disaster risk

**Where**: After the "Level Effects on Non-AI Stocks" subsubsection (end of Section 3.2), or as a new paragraph within Section 3.3.

**What to do**:
- Add a paragraph (4-6 sentences) addressing why the hedging premium is AI-specific. The key distinction: standard rare disasters (recessions, pandemics) destroy value broadly—Treasuries and gold hedge those. The AI singularity is *asymmetric by construction*: it devastates labor and non-AI dividends while enriching AI capital. Only assets correlated with the AI upside can hedge this specific risk. Treasuries and gold do not appreciate when AI advances; AI stocks do. The two-asset structure is not a limitation—it reflects the economic reality that the hedging instrument must be positively exposed to the shock that harms the household.
- Briefly address gradual vs sudden singularity: if displacement is gradual (many small shocks), each shock produces a smaller marginal-utility surge and the hedging amplifier $J^{-\gamma}$ is smaller per event. The model's one-shot structure is a simplification, but the qualitative mechanism (asymmetric exposure generating hedging demand) survives; the quantitative magnitude scales with the size of each discrete jump. This is consistent with the self-limiting mechanism already in the paper (rising $s_t$ erodes $J^{-\gamma}$).
