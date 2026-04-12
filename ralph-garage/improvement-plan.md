# Improvement Plan
AUTHOR PLAN — 2026-04-12 09:42:53 EDT

## Current State

- **Tests**: 22/25 pass, 3 fail
- **Model section**: Sound — no overhaul needed. Propositions are correctly stated and proved, economic intuition is clear, approximation vs exact computation is well-documented.
- **Introduction**: Recently rewritten over many iterations (rloop-17 through rloop-27); writing and narrative tests all pass.
- **Code**: Single `generate-exhibits.R` pipeline generating 3 exhibits; factcheck-code passes.

## Failing Tests

### 1. `element-rhetoric-meta` (FAIL)

**Problem**: The abstract's closing sentence — *"This paper demonstrates the displacement it models: AI agents produced all analysis and writing from a human-authored specification."* — is too blunt and prominent. The introduction footnote is fine. The test says this risks triggering the same aversion that caused the arxiv rejection.

**Fix** (paper/paper.tex, line 32): Soften the abstract sentence to be more allusive and self-referential rather than a direct disclosure. Instead of a flat declaration, lean into the irony — e.g., reference the displacement the paper models without explicitly announcing "AI agents produced all analysis and writing." Keep the explicit disclosure in the introduction footnote only.

### 2. `visual-figures` (FAIL)

**Problem**: Figure 2 (`fig-extension-panels`) has tick labels, legend text, and annotations that are too small to read comfortably. The "Catastrophe" annotation in Panel (b) is also too small.

**Fix** (code/generate-exhibits.R): Increase font sizes for the extension figure:
- Increase annotation `size` parameters (currently 4–6) to 6–8.
- Verify legend text size (currently 22) is adequate at the rendered PDF dimensions (14×8 inches). May need to bump to 24.
- Ensure tick labels (`axis.text`) are at least 22pt (already set, but figure dimensions may make them small — consider increasing `base_size` from 26 to 28 or the figure dimensions).

### 3. `visual-figures-image-only` (FAIL)

**Problem**: Panel (b) baseline curve is compressed into a narrow band near y=1.0, making its trajectory unreadable alongside the large-singularity curve that reaches ~5x. A log scale is already used, but the baseline (ranging ~0.75 to ~1.2) occupies too little visual space relative to the large singularity (ranging ~0.5 to ~5).

**Fix** (code/generate-exhibits.R): Improve the visual separation of the two scenarios in Panel (b). Options ranked by preference:
1. **Tighten y-axis limits and add more log-scale breaks** near the baseline range (e.g., breaks at `c(0.5, 0.75, 1, 1.5, 2, 5)` with limits `c(0.4, 6)`). This spreads the baseline's visual footprint.
2. **Add explicit annotations on the baseline curve** at a few tau values showing the numeric consumption growth (e.g., "1.1×" at tau=0.3), so the baseline's modest gains are readable even when visually compressed.
3. **Increase line width for the baseline** in Panel (b) to make its trajectory more visible.

Combining options 1 + 2 is likely the most effective approach.

## Execution Order

1. Fix Figure 2 readability issues (tests 2 + 3) in `code/generate-exhibits.R` — these are coupled and should be done together.
2. Regenerate exhibits by running `Rscript code/generate-exhibits.R`.
3. Fix the abstract rhetoric in `paper/paper.tex` line 32 (test 1).
4. Recompile the paper and verify.
