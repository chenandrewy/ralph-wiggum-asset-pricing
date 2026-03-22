# Improvement Plan

## Status: Full Overhaul Required

The paper is entirely placeholder text (title, abstract, intro, model, results, conclusion). Every section must be written from scratch. All tests will fail until substantive content exists.

## Key Issues

1. **No content exists.** The paper contains only `PLACEHOLDER` markers.
2. **Referee differentiation from GKP (2012).** The CFR-R1 referee views the model as a special case of GKP. The paper must differentiate by incorporating features unique to an AI singularity — not just generic displacement risk.
3. **Jones (2024) extension needed.** The referee and spec both call for incorporating existential risk and infinite-consumption possibilities from Jones (2024).

## Overhaul Plan

### Phase 1: Model Section (highest priority)

Write the core model in `paper/paper.tex`. This is the hardest section and the foundation for everything else.

**Model design — differentiate from GKP:**
- Two agents: a representative household (marginal investor) and AI owners (hold private AI capital, not marginal).
- Two public assets: AI stocks and non-AI stocks. AI stocks grow as a share of the economy with each singularity event.
- Incomplete markets: the household cannot buy private AI capital. This is the key friction — not OLG displacement as in GKP, but exclusion from private AI wealth.
- Infinite horizon (not OLG like GKP — a deliberate structural difference).
- The negative AI singularity is a sudden event that devastates the household's consumption but benefits AI owners. AI stocks partially hedge this because they appreciate when AI advances.
- Focus on price/dividend ratio of public AI stocks and how it varies with singularity probability.
- Key departure from GKP: GKP's displacement comes from future cohorts of firms that don't yet exist. Here, displacement comes from a *concentrated class of AI owners* who already exist but whose assets are private and untradeable. This makes the incomplete-markets friction about asset accessibility, not intergenerational risk sharing.

**Notation and structure:**
- Define preferences (CRRA, infinite horizon).
- Define endowment/dividend processes for AI and non-AI stocks.
- Define the singularity shock process (Poisson arrival, affects consumption shares).
- Derive equilibrium pricing via the household's Euler equation.
- Show the P/D ratio result: AI stocks command a premium because they hedge the negative singularity.

### Phase 2: Introduction

- Open with the AI valuation puzzle (high P/D ratios for AI stocks vs. market).
- State the main argument: hedging demand against negative AI singularity explains part of the premium.
- Emphasize incomplete markets as the key friction.
- Include one figure: AI stock valuations vs. market portfolio (per spec).
- Position relative to GKP clearly: different friction (private AI capital vs. OLG), different shock (AI singularity vs. generic innovation), different focus (AI stock valuations vs. value-growth spread).
- Concise lit review: GKP (2012), Jones (2024), disaster risk papers (Barro, Rietz, Wachter), AI economics (Korinek and Suh).

### Phase 3: Results

- Present the main proposition: P/D ratio of AI stocks increasing in singularity probability.
- Show comparative statics on key parameters.
- Calibration with reasonable parameter values.
- At most 6 exhibits total (per spec).

### Phase 4: Extension — Jones (2024) Integration

- Singularity may cause extinction (existential risk).
- AI owners may receive infinite consumption.
- Use VSL data to calibrate (following Jones 2024).
- Discuss how infinite output relaxes the incomplete-markets friction (per spec, referencing GKP).
- Keep this in a separate extension section so the main argument stays clean.

### Phase 5: Title, Abstract, Conclusion

- Title: short, evocative, not cringey.
- Abstract: 100 words or less.
- Conclusion: brief, forward-looking.

### Phase 6: Formatting and Compliance

- Page numbers on every page.
- Anonymous author.
- At most 6 exhibits.
- Under 20 pages excluding references.
- Style: between academic paper and blog post — direct, conversational, rigorous.

## Test IDs (for reference)

Non-referee tests: `ai-economics`, `build-latex`, `spec-compliance`, `theory-correctness`, `theory-elegance`, `visual-pages`, `writing-natural`

Referee tests: `referee-top3`, `cfr-r1`
