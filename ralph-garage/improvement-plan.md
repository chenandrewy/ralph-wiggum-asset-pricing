# Improvement Plan

## Key Issues

1. **Introduction figure uses model output, not data (spec violation).** Spec I.6 requires "a single figure illustrating the valuation of publicly traded AI stocks compared with the market portfolio using CRSP and Compustat data." Figure 1 currently plots model-implied P/D ratios against lambda. It must be replaced with an empirical exhibit.

2. **GKP contribution is overclaimed and misses the required angle (spec I.7, referee comment 1).** The referee says the model is "largely subsumed" by GKP. The current paper lists three differences (asset inaccessibility vs intergenerational, infinite-horizon vs OLG, concentrated risk), but these are largely interpretive reframings, not non-trivial modeling contributions. The cfr-r1 test will reject any hint of immodesty. Spec I.7 specifically requires engaging with GKP footnote 14: in GKP, bequests/gifts between generations would eliminate the displacement factor entirely. Our friction (private untradeable capital) is NOT resolvable by intergenerational transfers — it requires securitization or regulatory reform. This is the genuine, modest differentiator. The current paper does not mention this.

3. **Jones (2024) extension is too thin (referee comment 2, cfr-r1 test).** The extinction result is trivial (multiply by 1-delta). The infinite output discussion is purely verbal with no formal model. The cfr-r1 test requires at least two key features of Jones captured with meaningful results tied to the main argument.

## Plan

### Change 1: Replace Figure 1 with empirical data exhibit

- Write an R script in `code/` that computes the market-cap-weighted P/E (or P/D) ratio of AI-related stocks vs. the overall market portfolio using CRSP and Compustat data.
- Define AI stocks using SIC/NAICS codes or a curated list of major AI firms (NVDA, MSFT, GOOG, META, etc.).
- Plot a time series (or recent cross-section) showing AI stock valuations vs. market valuations.
- Replace the current TikZ figure with `\includegraphics` referencing the generated plot.
- Move the current model-implied P/D figure into the calibration subsection (Section 3.3) as a second exhibit, or drop it if the table suffices.

### Change 2: Rewrite GKP differentiation to be modest and engage with footnote 14

- Shorten the current GKP paragraph in the introduction to 2-3 sentences max.
- Frame the contribution modestly: our model applies the displacement-risk intuition of GKP to the specific context of an AI singularity. The modeling is similar, but the friction differs.
- Add one sentence engaging with GKP footnote 14: in GKP, intergenerational transfers (bequests, government debt) can in principle eliminate displacement risk. In our model, the friction is asset inaccessibility — private AI capital is untradeable — which cannot be resolved by intergenerational transfers but could be resolved by broadening capital access (securitization, regulation). This distinction matters for policy.
- Remove the three-point enumeration of differences. Do not overclaim.

### Change 3: Deepen the Jones (2024) extension

- **Feature 1 (already present but strengthen):** Extinction risk. The current Proposition 3 is fine but mechanical. Add a brief calibration using Jones's VSL estimates (value of a statistical life ~6x consumption). Show how the premium varies with delta for a plausible range of extinction probabilities. This ties the extension to quantitative predictions.
- **Feature 2 (new modeling):** Heterogeneous views on existential risk, following Jones (2024). Rich households (AI owners in our framing) may be more concerned about extinction than poor households, because they have more to lose. Model this by allowing AI owners to have a different subjective extinction probability than the representative household. Show that disagreement about extinction probability affects the equilibrium hedging premium — if AI owners believe extinction is likely, they value their private capital less, potentially loosening the incomplete-markets friction.
- Keep the infinite-output discussion verbal but tighten it to 1-2 paragraphs connecting back to the main result.

### Change 4: Minor fixes

- Verify abstract is under 100 words (currently ~90, OK).
- Ensure the model P/D figure (if kept) or calibration table numerics are consistent with the formulas. Spot-check: at lambda=0, v = a/(1-a) = 0.92272/0.07728 = 11.94 ~ 11.9. Checks out.
- Confirm paper stays under 20 pages after changes.

## Priority Order

1. Change 2 (GKP differentiation) — addresses the referee's main critique and the cfr-r1 test.
2. Change 1 (empirical figure) — fixes a spec violation.
3. Change 3 (Jones extension) — addresses the referee's second comment and deepens the contribution.
4. Change 4 (minor fixes) — cleanup.
