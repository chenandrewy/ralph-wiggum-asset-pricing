# Improvement Plan
AUTHOR PLAN — 2026-04-02 21:58:06 EDT

## Status
- **Build:** Compiles cleanly (13 pages).
- **Tests:** 15/16 pass. One failure: `quality-writing`.
- **Referees:** Disabled (no referee outputs).

## Key Issue

The `quality-writing` test fails on the "compelling throughout" criterion. Two problems identified:

1. **Conclusion (primary failure).** Three of four paragraphs are mechanical recap that restate the abstract and results. The test calls this out explicitly: "a reader scanning a JF issue would stop reading here." Only the final sentence ("Financial market solutions to AI disaster risk are under-discussed") adds forward-looking content.

2. **Model section (secondary concern).** Opens with textbook-style exposition ("Time is discrete...") and proceeds mechanically through subsections without narrative connecting the formalism to the economic story. The test notes the contrast with the introduction's tone. The section's brevity partly mitigates this, but it still falls short of the paper's own "between academic paper and blog post" target.

## Plan

### 1. Rewrite the conclusion (Section 5)

This is where the test fails. Changes:

- **Cut the recap.** Remove the first two paragraphs that restate the abstract. The reader just read the paper — they don't need a summary of it.
- **Lead with the forward-looking insight.** Open with the under-discussed policy point: expanding tradeable AI claims (public listings, derivatives, government risk-sharing) could reduce the displacement premium. This is the conclusion's only genuinely new content — make it the lead.
- **Add a "what's left unsaid" paragraph.** Briefly note what the model deliberately omits and why — e.g., the model is intentionally stylized, avoids calibration, and does not generate a broad menu of testable predictions. Frame these as scope choices, not apologies.
- **End with the paradox.** Close on the extension's punchline: the most extreme singularity eliminates displacement risk, so the hedging premium is largest for moderate singularities. This is the paper's most memorable result — let it be the last thing the reader sees.
- **Target: 2 paragraphs max.** A compact conclusion that leaves the reader thinking, not skimming.

### 2. Add narrative connective tissue to the model section (Section 2)

This is the secondary concern flagged by the test. Changes:

- **Add a brief motivating sentence at the top of Section 2** that connects back to the introduction's intuition before diving into formalism. Something like: "We now translate the intuition from the introduction into a formal environment."
- **Add a one-sentence forward pointer after the household's problem** (Section 2.3) linking the setup to the results: what will the Euler equation deliver?
- **Keep it light.** The model section is already short (~1.5 pages). Do not pad it — just add the connective sentences that make it feel less like a textbook appendix.
