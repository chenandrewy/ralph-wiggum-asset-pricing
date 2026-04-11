# Improvement Plan
AUTHOR PLAN — 2026-04-10 22:25:36 EDT

## Current State

22/25 tests pass. Three failures, all fixable without structural changes.

## Failing Tests

### 1. element-gkp-cites (FAIL)

**Issue:** Line 228 in Extension 2 opening uses "note that" and "Building on this suggestion" to describe GKP's transfer discussion. The test flags this as minimizing GKP's substantive analytical paragraph (GKP Section 3.2), where they work through the altruistic dynasty example and discuss multiple transfer mechanisms. "Note" implies a passing remark; "suggestion" implies a hint rather than analysis.

**Fix in paper.tex (line 228):** Replace the opening of Extension 2 with language that properly credits GKP's analytical treatment. Something like: "\citet{GKP2012} analyze how intergenerational transfers affect the magnitude of displacement risk, showing that under altruistic dynasties bequests can eliminate displacement entirely, while observing that such transfers do not alter the functional form of the stochastic discount factor. Building on their analysis, we study transfers in the specific setting of an AI singularity..." Key changes: "note that" -> "analyze how"; "suggestion" -> "their analysis."

### 2. spec-paper (FAIL)

**Issue:** Style Requirement 8 requires all display equations be numbered. The `align` environment at lines 298-301 in the appendix uses `\nonumber` on the first line.

**Fix in paper.tex (lines 298-301):** Replace the `align` with `equation` + `split` (single number for the whole equation), or remove the `\nonumber` and let both lines get numbered. The `equation`+`split` approach is cleaner since this is one equation broken across two lines.

### 3. visual-figures-image-only (FAIL)

**Issue:** fig-ai-valuations has grid lines in gray50 (too dark, competes with data lines).

**Fix in code/generate-exhibits.R (line 380):** Change `panel.grid.major = element_line(color = "gray50")` to `panel.grid.major = element_line(color = "gray80")`. This is a fig-ai-valuations-specific theme override; the extension figure already uses gray75 from theme_paper and passes.

## Execution Order

1. Fix code/generate-exhibits.R grid color (line 380): gray50 -> gray80.
2. Regenerate exhibits: `Rscript code/generate-exhibits.R`.
3. Fix paper.tex line 228: reword GKP transfer attribution.
4. Fix paper.tex lines 298-301: replace align+nonumber with equation+split.
5. Rebuild paper PDF and page images.
6. Run tests to verify.
