# Improvement Plan
AUTHOR PLAN — 2026-04-09 20:49:40 EDT

## Current State

- **Tests:** 21/25 pass, 4 fail
- **Model/theory:** No overhaul needed. Derivations are correct, comparative statics are sound, and the economic logic is consistent with the spec.
- **Referee report:** Already addressed via Extension 1 (veto) and Extension 2 (transfers).

## Failing Tests (Priority 1)

### 1. `factcheck-freely` — Missing author in bib entry
**Issue:** `references.bib` entry `KoganPapanikolaouStoffman2020` is missing coauthor **Amit Seru**. The published JPE paper has four authors: Kogan, Papanikolaou, Seru, Stoffman.
**Fix:**
- Update bib key to `KoganPapanikolaouSeruStoffman2020`.
- Add `Seru, Amit` to the author field.
- Update all `\citet` references in `paper.tex` (currently line 68).

### 2. `visual-figures` — Extension panels readability
**Issue:** Figure 2 tick labels and legend text are too small; legend uses raw parameter strings instead of verbal labels ("Baseline", "Large singularity").
**Fix in `code/generate-exhibits.R`:**
- The code already uses verbal scenario labels (`scenario_labels`). The test sees raw parameter strings, suggesting the legend labels are not rendering correctly or the `expression()` labels are being truncated. Investigate and fix the legend label rendering—likely need to simplify from `expression()` to plain strings with Unicode or paste, or increase the plot `width` to prevent truncation.
- Increase `base_size` in `theme_paper` (e.g., from 16 to 18) or explicitly set larger tick label sizes.

### 3. `visual-figures-image-only` — Panel (b) contrast and legend truncation
**Issue:** (a) "No change" reference line in Panel (b) is light gray, low contrast. (b) Legend text for "Large singularity" is truncated (missing closing parenthesis).
**Fix in `code/generate-exhibits.R`:**
- Darken the reference line: change `color = "gray40"` to `"gray20"` or `"black"` and increase `linewidth`.
- Fix legend truncation: same root cause as test 2 above—simplify `expression()` labels or widen the figure.

### 4. `writing-intro` — Introduction flow breaks
**Issue:** Three flow problems:
1. Paragraph 3 (policy meta-commentary) is a non sequitur after the hedging mechanism in paragraph 2.
2. Paragraph 6→7 transition (redistribution → self-referential anecdote) is abrupt.
3. Paragraph 6 trails off without crisp resolution.

**Fix in `paper.tex`:**
- Merge paragraph 3's policy-gap observation into paragraph 4 as a setup sentence (e.g., "Although financial market solutions remain largely absent from AI risk discussions, understanding where market limits bind requires a framework..."). This restores the motivation→mechanism→model flow.
- Add a bridging sentence before the self-referential paragraph 7 connecting the theoretical displacement to observable displacement in knowledge production.
- Tighten paragraph 6's ending with a crisper concluding sentence.

## Post-Fix Improvements (Priority 2)

No further changes needed. All other tests pass, including spec compliance, theory checks, lit review, and referee-related elements. The model section does not need an overhaul.
