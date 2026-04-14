# Improvement Plan
AUTHOR PLAN — 2026-04-14 10:32:36 EDT

## Current State

- **Tests**: 24/25 pass. All factcheck, theory, writing, spec, and element tests pass.
- **Failing test**: `visual-figures-image-only` — grid lines in `fig-extension-panels` use `gray75`, which fails the contrast requirement. Both panels flagged.

## Plan

### 1. Fix failing test: fig-extension-panels grid contrast

**File**: `code/generate-exhibits.R`, line 210  
**Change**: Replace `gray75` with `gray55` in `theme_paper`'s `panel.grid.major` setting.  
**Why**: The `visual-figures-image-only` test requires all drawn elements to have strong contrast. `gray75` is too light; `gray55` provides sufficient contrast while remaining subordinate to data lines.

After the code change, regenerate exhibits with `Rscript code/generate-exhibits.R`.

### 2. No overhaul needed

The model section is correct and well-structured:
- All theoretical derivations verified (factcheck-theory, factcheck-freely, factcheck-bysection all pass).
- Notation is consistent across all 26 symbol families.
- Propositions are correctly proved.
- Numerical claims match code output exactly.
- The introduction flows well and fulfills all promises.
- GKP citations are accurate and appropriately modest.
- Paper meets all spec requirements.

No section requires an overhaul. The single remaining issue is the visual fix above.
