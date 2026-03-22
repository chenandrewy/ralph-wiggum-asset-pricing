# Improvement Plan

## Status Summary

- **Tests**: 2/2 pass (spec-compliance, theory-correctness)
- **Referee (top3)**: 2 comments, both substantive

## Key Issues

### 1. P/D vs P/E mismatch (Referee Comment 1)
The model derives price-dividend ratios, but Figure 1 plots price-earnings ratios. The text claims the model's 29% premium is "broadly consistent with" Figure 1, but P/D and P/E are different objects—AI firms retain most earnings and many pay no dividends, so P/D >> P/E. The paper's central quantitative claim lacks a valid empirical benchmark.

### 2. Section 4.3 is informal (Referee Comment 2)
The "intermediate regime" insight—that the premium is largest when the singularity is harmful but not so extreme as to resolve the friction—is stated informally in two paragraphs. The parameter π is not microfounded as a function of output scale. Section 4.3 reads as a promissory note.

### 3. Table 2 computational error (Theory-correctness test, note)
Individual P/D levels in Table 2 (extinction) are wrong: $(1-\delta)$ is applied outside the bracket instead of inside. Premiums and ratios are unaffected, but the v^A and v^N columns are overstated for δ > 0.

### 4. Proposition 4 implicit assumption (Theory-correctness test, note)
The proof assumes friction resolution neutralizes dividend asymmetry (θ, φ don't apply). This is economically reasonable but should be stated explicitly.

## Plan

### A. Fix P/D vs P/E comparison (addresses Referee Comment 1)
**Option chosen**: Recast Figure 1 to show P/D ratios instead of P/E ratios.
- Update `code/figure-ai-valuations.R` to compute trailing price-dividend ratios (price / trailing 12-month dividends per share) for both the AI basket and S&P 500.
- Update the figure caption and axis labels accordingly.
- Revise the calibration discussion paragraph (around line 248) to compare model P/D ratios directly to empirical P/D ratios. Remove "broadly consistent with" hand-waving; state the comparison precisely.

### B. Formalize Section 4.3 (addresses Referee Comment 2)
- Microfound π as a function of post-singularity AI output scale Y_O. Define π(Y_O) as a simple increasing function (e.g., π = 1 − k/Y_O for some cost parameter k, so π → 1 as Y_O → ∞).
- Add a **Proposition 5** that states: as Y_O → ∞, π → 1 and the hedging premium → 0. Show that the premium is hump-shaped in the severity of the singularity (increasing in θ for small θ, decreasing for large θ where π dominates).
- Rewrite Section 4.3 around this new proposition. Keep it tight—one proposition, one short proof, one paragraph of interpretation.

### C. Fix Table 2 values
- Recompute v^A and v^N for each δ using the correct formula where (1−δ) multiplies only J^{−γ}(1+θ) inside the bracket.
- Update Table 2 in paper.tex.

### D. State Proposition 4 assumption explicitly
- Add one sentence before or within Proposition 4 stating that when the friction resolves, the household rebalances into private AI capital so that the singularity is consumption-neutral (J = 1), and thus the dividend asymmetry (θ, φ) does not generate a premium in that state.

## Priority Order

1. **C** — Fix Table 2 (quick, correctness issue)
2. **D** — State Prop 4 assumption (quick, correctness issue)
3. **A** — Fix P/D vs P/E (substantive, addresses main referee concern)
4. **B** — Formalize Section 4.3 (substantive, addresses second referee concern)
