# Improvement Plan
AUTHOR PLAN — 2026-04-04 23:04:01 EDT

## Current State

The paper is entirely placeholder (lorem ipsum, placeholder title/abstract/citations, no exhibits, no code, no data). This is a full build from scratch.

## Key Issues

1. **No model**: The paper needs an infinite-horizon discrete-time model with a representative household and AI owners, two public assets (AI and non-AI stocks), and incomplete markets.
2. **No code or exhibits**: Need R pipeline producing up to 6 exhibits into `paper/exhibits/`.
3. **No content**: Every section is lorem ipsum.
4. **No bibliography**: Only placeholder bib entries.

## Plan

Since the paper needs a complete overhaul, the entire plan focuses on building the paper from the ground up.

### Step 1: Build the Model and Code

Write the baseline model in `paper/paper.tex` and the R code in `code/`.

**Baseline model (Section 2):**
- Infinite-horizon, discrete-time economy.
- Two agents: representative household (marginal investor) and AI owners (hold private AI capital, not marginal in public stocks). AI owners can also be interpreted as unborn/future capital holders per GKP.
- Two publicly traded assets: AI stocks and non-AI stocks.
- Singularity event: arrives with probability $p$ each period, causes AI stocks to grow as a share of the economy, devastating for the household's consumption from non-AI sources.
- Incomplete markets: household cannot trade private AI capital (the key friction from GKP, adapted to AI setting).
- Derive price/dividend ratios for AI and non-AI stocks as functions of singularity probability $p$.
- Proposition: AI stocks command a higher P/D ratio because they hedge displacement risk under incomplete markets.
- Quantitative table: P/D ratios for AI vs non-AI stocks across plausible $p$ values.

**R code (`code/`):**
- Single entry-point script that generates all exhibits.
- Exhibit 1 (intro figure): CRSP-based figure showing AI stock valuations vs non-AI stocks.
- Exhibit 2 (table): Quantitative parameterization table showing P/D ratios vs singularity probability.
- Exhibit 3 (extension figure): Government transfers -- P/D ratio of AI stocks as function of singularity output growth and deadweight costs.

### Step 2: Write the Extensions (Section 4)

Three independent extensions branching from the baseline:

1. **Government transfers**: Transfers attenuate incomplete markets problem. Deadweight costs make this unattractive normally, but with singularity-level output growth (per Jones 2024), even enormous costs are worth bearing. Figure: P/D vs output growth and deadweight cost.

2. **Veto/deployment**: Household can block the singularity at a consumption cost. Under complete markets, household never vetoes. Under incomplete markets, veto can occur. Informally link to Extension 1: large enough output growth + transfers can restore efficient deployment.

3. **Extinction risk**: Per Jones (2024), singularity may carry existential risk. Show how extinction probability affects AI stock P/D and its relationship with singularity probability.

### Step 3: Write Remaining Sections

- **Title**: Short, evocative, eye-catching.
- **Abstract**: Under 100 words. Mention AI-agent authorship. Rigorous yet eye-catching.
- **Preface (TBC)**: Unnumbered, left blank per spec.
- **Introduction**: Engaging, each paragraph flows to the next. Include the AI-agent authorship device. Lit review (max half page) at end of intro, centered on GKP, Jones, and top finance/econ journals.
- **Results (Section 3)**: Main propositions with proofs (long proofs in appendix). Quantitative table.
- **Extensions (Section 4)**: Three extensions as above.
- **Conclusion**: Brief.
- **Appendix**: Proofs.

### Step 4: Bibliography

Build `references.bib` with real entries:
- Garleanu, Kogan, Panageas (2012 JFE)
- Jones (2024 AERI)
- Korinek and Suh (2024)
- Other relevant papers from top finance/econ journals for the lit review.

### Priorities

1. Get the model right first -- this is the hardest part and everything depends on it.
2. Write the R code to produce exhibits.
3. Draft the full paper text around the model and exhibits.
4. Ensure GKP citations are sensitive, cautious, and modest.
5. Keep scope compact: illustrative quantitative content, minimal empirical content, no calibration exercise.
