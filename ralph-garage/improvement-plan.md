# Improvement Plan

## Current State

- **spec-compliance**: PASS
- **theory-correctness**: FAIL — inline η-robustness numbers are wrong
- **referee-top3**: two actionable comments

No overhaul needed. The model section is sound (notation consistent, assumptions consistent, all propositions verified). The single failure is an arithmetic error in inline numbers.

---

## Priority 1: Fix Failing Test (theory-correctness)

**Issue.** The η-robustness paragraph (Section 2.3, line 142) claims the effective hedging amplifier $(1-\eta)J^{-\gamma} + \eta J_O^{-\gamma}$ equals 1.50 at η=0.10 and 1.21 at η=0.20. The correct values (with J≈0.82, γ=3, J_O≈1.5) are approximately 1.66 and 1.51. The η=0 value (1.81) is correct.

**Fix.** Recompute the amplifier for η=0.10 and η=0.20 using the stated formula and parameters, and replace the inline numbers with the correct values. Verify the qualitative claim ("premium remains substantial") still holds — it does, since even 1.51 > 1.

---

## Priority 2: Address Referee Comments (referee-top3)

### Comment 1 — Differential-growth calibration needs a table

**Issue.** The paper's central quantitative claim — that with 3–5pp growth differentials the model generates v^A/v^N of 2.0–2.7× — appears only in prose (Section 3.3, "Differential Pre-Singularity Growth"). No exhibit supports it. The paper uses only 5 of 6 allowed exhibits.

**Fix.** Add a table (Table 4 or renumber) showing v^A/v^N for a grid of (g^A − g^N, λ) values, with columns decomposing the premium into hedging-amplifier and cash-flow components. Place it in Section 3.3 after equation (12). This is the 6th and final exhibit.

**Implementation.** Write an R script to compute the recursive v^A formula (eq 12) at t=0 for each (g^A − g^N, λ) combination, decomposing into cash-flow and hedging components. Output a LaTeX table fragment.

### Comment 2 — Derive and discuss expected returns

**Issue.** The model implies AI stocks are insurance assets with low expected excess returns (Cov(M, R^A) > 0), yet AI stocks have delivered high realized returns. The paper never states this implication or addresses the tension.

**Fix.** Add a short subsection (or a paragraph within Section 3) that:
1. Derives the expected return differential in closed form from the existing Euler equation. This is straightforward: E[R^A] = 1/E[M·R^A] adjusted for covariance, yielding a lower risk premium for AI stocks.
2. States the prediction clearly: the hedging channel implies AI stocks earn a *lower* risk premium than non-AI stocks.
3. Discusses the tension with data: high realized returns are consistent with (a) the singularity not having occurred yet (peso problem), and (b) upward revisions in perceived λ driving capital gains — both of which the model accommodates.

Place this after the testable-implications subsection or integrate it there.

---

## Sequencing

1. Fix η numbers (small, surgical edit — unblocks theory-correctness).
2. Build differential-growth table (requires R computation + LaTeX table).
3. Add expected-returns discussion (analytical derivation + prose).
