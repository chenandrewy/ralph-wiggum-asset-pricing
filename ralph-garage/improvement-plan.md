# Improvement Plan
AUTHOR PLAN — 2026-04-04 23:56:37 EDT

## Status: 15/21 tests pass, 6 fail

## Failing Tests and Fixes

### 1. factcheck-exhibits + factcheck-freely — V₀ misdescribed (2 tests, same root cause)
**Issue:** Text (line 180) calls V₀ "the P/D ratio in a world where the singularity never occurs." Caption (line 261) says V₀ "marks the P/D ratio with no singularity risk." Both are wrong: V₀ = (1−p)R / [1−(1−p)R] includes p and equals the P/D when the hedge factor H=0, not when p=0. The true no-singularity-risk P/D is V∞ = R/(1−R).

**Fix (paper.tex):**
- Line 180: Replace with accurate language, e.g., V₀ is the P/D ratio when the asset provides no hedge (H=0); V∞ is the P/D with no remaining singularity risk.
- Line 261 (fig-transfers caption): Replace "V₀ marks the P/D ratio with no singularity risk" with "V₀ marks the P/D ratio of an asset with no hedge benefit (H=0)."
- Also fix the code comment in run-all.R line 228 ("V0 (asymptote as G -> infinity)") to match the corrected description.

### 2. spec-paper — \notag violates "all display equations numbered"
**Issue:** Lines 344–345 in paper.tex use `\notag` inside an `align` environment in the appendix proof. Spec style requirement 9 says all display equations must be numbered.

**Fix (paper.tex):** Remove the two `\notag` commands. Alternatively, convert the multi-line derivation to a single `align` with all lines numbered, or use a single `equation` with `split` inside (which numbers the block once). The simplest fix: remove `\notag` so each line gets a number.

### 3. element-lit-review — Missing critical citation
**Issue:** The paper builds directly on GKP (2012) but omits Kogan, Papanikolaou, and Stoffman (2020, JPE), "Left Behind: Creative Destruction, Inequality, and the Stock Market," which directly extends GKP's displacement framework to stock prices and inequality. Also recommended: Kogan and Papanikolaou (2014, JF), "Growth Opportunities, Technology Shocks, and Asset Prices."

**Fix:**
- Add both citations to references.bib.
- Add a sentence in the lit review paragraph citing KPS (2020) as extending GKP's framework to study how creative destruction affects stock prices, and KP (2014) on technology shocks and asset prices.

### 4. element-rhetoric-meta — Introduction AI-production paragraph too heavy-handed
**Issue:** The penultimate introduction paragraph ("This paper demonstrates the very risk it models...") is too assertive. Claims like "produced entirely by AI agents" and "is not a gimmick; it is evidence" invite skepticism rather than intrigue. The abstract handles it well; the intro overplays it.

**Fix (paper.tex):** Soften the paragraph significantly. Remove "entirely" and the defensive "not a gimmick; it is evidence" line. Aim for the understated tone of the abstract: acknowledge the AI production as a quiet fact rather than a loud claim. For example: note that the analysis was produced by AI agents working from a human specification, and let the reader draw conclusions.

### 5. quality-writing — Model section lacks narrative flow
**Issue:** Section 2 reads as a flat checklist of definitions and assumptions. The introduction promises engaging prose "between academic and blog post," but the model section reverts to standard academic template. Results section also follows a monotonous pattern of proposition → one-paragraph interpretation.

**Fix (paper.tex):**
- Add a brief opening paragraph to Section 2 that frames the modeling choices and tells the reader what to watch for (e.g., "We build the simplest model that isolates the hedging mechanism...").
- Add short transitional sentences between subsections linking each piece to the economic question.
- In Section 3, vary the rhythm: some results get longer discussion, some get a forward-looking hook. The quantitative subsection (3.3) could open with a motivating question rather than jumping straight to the table.
- In Section 4, add a brief connective sentence between extensions (the intro previews them as a sequence; the body should echo that structure).

## Priority Order

1. **V₀ description fix** (factcheck-exhibits, factcheck-freely) — factual error, highest priority
2. **\notag fix** (spec-paper) — mechanical, easy
3. **Lit review additions** (element-lit-review) — straightforward
4. **Rhetoric softening** (element-rhetoric-meta) — editorial
5. **Model section narrative** (quality-writing) — most effort, save for last
