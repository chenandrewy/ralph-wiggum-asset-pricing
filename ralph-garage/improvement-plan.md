# Improvement Plan
AUTHOR PLAN — 2026-04-02 17:48:30 EDT

## Status: Overhaul Required

The paper (`paper/paper.tex`) is a placeholder with lorem ipsum text, a placeholder title/abstract, and fake citations. No test results exist yet. The entire paper must be written from scratch.

## Key Issues

1. **No content exists.** Every section is lorem ipsum or placeholder text.
2. **No model.** The paper spec requires an infinite-horizon, discrete-time model with two agents (representative household and AI owners), two publicly traded assets (AI stocks and non-AI stocks), and analysis of the price/dividend ratio of public AI stocks.
3. **No bibliography.** `references.bib` has only fake entries. Real citations (GKP 2012, Jones 2024, etc.) are needed.
4. **Missing structure.** Spec requires: unnumbered "Preface (TBC)" section, Introduction, Model, Results, Extension (Jones 2024 ideas), Conclusion, Appendix with proofs.
5. **No exhibits or code.** Spec calls for at most 6 exhibits, ideally including an empirical figure of AI vs non-AI stock valuations from CRSP.

## Overhaul Plan

The entire plan focuses on building the paper from the ground up. Each step below is a single author iteration.

### Step 1: Structure and Model Section

Write the core of the paper, focusing on the model:

- **Title and abstract**: Short, evocative title; abstract under 100 words capturing the hedging/displacement argument.
- **Preface (TBC)**: Unnumbered, left blank per spec.
- **Introduction**: Motivate the paper — AI stocks have high valuations partly because they hedge against a negative AI singularity. Incomplete markets are key. Keep engaging, direct, plain English. Include a brief lit review (≤ half page) at the end, centered on GKP (2012), Jones (2024), and other top-journal displacement/innovation risk papers.
- **Model**: This is the hardest and most important section.
  - Infinite-horizon, discrete-time setup.
  - Two agents: representative household (marginal investor) and AI owners (hold private AI capital, not marginal in public stocks).
  - Two public assets: AI stocks and non-AI stocks. AI stocks grow as share of economy with each singularity.
  - Derive the price/dividend ratio of public AI stocks and show how it changes with the probability of a negative AI singularity.
  - Keep formalism minimal — every equation must advance the economic argument. No ceremonial math.
  - Number all display equations. Comment-tag all sections and propositions per spec.
- **Results**: State and prove propositions. Main result: AI stock P/D ratio increases with singularity probability under incomplete markets. Short proofs inline, long proofs in appendix.
- **Conclusion**: Brief summary, mention financial market solutions to AI disaster risk are under-discussed.
- **Bibliography**: Add real entries for GKP (2012 WP and published), Jones (2024), Korinek-Suh (2024), and other relevant papers.

### Step 2: Extension and Refinement

- **Extension section**: Incorporate Jones (2024) ideas — singularity may cause extinction; consumption may become infinite for AI owners; analyze how infinite output affects the Coase theorem / friction assumptions from GKP.
- **GKP contribution framing**: Modest characterization — main insights are in GKP; this paper contributes formal analysis of how government debt / intergenerational transfers affect the displacement factor, and how singularity-level output might overcome frictions.
- **Self-referential AI discussion**: Note that the paper itself demonstrates AI displacement risk, since all analysis and writing is done by AI agents (human wrote only the spec and tests).

### Step 3: Empirical Exhibit and Code

- Write R code in `code/` to generate a single introductory figure: AI stock valuations vs. non-AI stock valuations using CRSP data.
- Output to `paper/exhibits/` in PDF format.
- Ensure the canonical pipeline runs from scratch in < 180 seconds.

### Step 4: Polish and Test Compliance

- Run all tests and iterate on failures.
- Ensure page numbers on every page, ≤ 20 pages, ≤ 6 exhibits.
- Verify all citations are accurate per the referenced papers.
- Ensure writing is compelling, conversational, yet rigorous.
