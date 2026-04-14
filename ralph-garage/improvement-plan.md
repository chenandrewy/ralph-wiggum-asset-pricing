# Improvement Plan
AUTHOR PLAN — 2026-04-14 10:18:19 EDT

## Current State

25 tests: 23 pass, 2 fail. No overhaul needed — the model section is correct, well-structured, and passes all theory/factcheck tests. Focus on fixing the two failures and polishing.

## Failing Tests

### 1. `theory-deadweight` — FAIL
**Problem:** Proposition 2's inline proof is a ~12-line formal detour proving a ratio claim that the paper never uses. Every downstream reference (Section 3, intro, conclusion) relies only on the direction result ("valuation spread decreasing in xi"). The proof introduces six auxiliary constructs (B, S, f, f'', semi-elasticity, A > 1/2 domain) that appear nowhere else — violating the spec's ban on auxiliary formal detours (spec IV.8a).

**Fix:** 
- Drop the ratio clause from Proposition 2. State only the direction result.
- Replace the inline proof with a 1–2 sentence argument: higher xi reduces the weight on non-extinction singularity states; since these are the only states where AI stocks' dividend advantage (Gamma^AI > Gamma^N) operates, the valuation spread shrinks.
- Optionally move the ratio result to a remark or footnote if desired for completeness.

### 2. `visual-figures-image-only` — FAIL
**Problem:** `fig-extension-panels` fails on two issues:
- (a) Grid lines (`gray30`) are too dark and compete with data series in both panels. The dashed blue line's gaps can be confused with dark vertical grid lines.
- (b) Panel (b) y-axis compression: log-scale runs 0.5–5.0, but baseline (red) series spans only 0.50–1.30, compressing it into the bottom ~40% of the plot. Also, Panel (a) x-axis ends at 40% while Panel (b) extends to ~55%, creating inconsistency.

**Fix in `code/generate-exhibits.R`:**
- Change `panel.grid.major` from `gray30` to `gray70` (or lighter) in `theme_paper`.
- Align x-axis ranges: use 0–50% for both panels (or 0–40% for both).
- Address Panel (b) compression: tighten y-axis limits (e.g., 0.4 to 5.5 is already close; consider whether a different break structure or annotation placement helps the baseline series readability). Alternatively, add a secondary inset or adjust log-scale breaks to give the baseline more visual room.

## Additional Polish (from passing tests with notes)

### 3. Introduction precision on complete markets
**Source:** `factcheck-bysection` line 18 notes a minor imprecision: intro says premium "would vanish" under complete markets, but Section 2.3 says it "largely collapses" with a small residual from Gamma^AI != Gamma^N.
**Fix:** Change "would vanish" to "would largely vanish" or "would collapse" in the introduction (line 49 of paper.tex).

### 4. Proposition 2 could be stated more generally
**Source:** `factcheck-freely` note 2: the proof actually establishes the ratio result for all P/D > 1, not just "parameterizations considered." If keeping any ratio language (even in a remark), state it generally rather than qualifying with "parameterizations considered."

### 5. Panel (b) y-axis label clarity
**Source:** `factcheck-freely` note 1: y-axis reads "Household Consumption Growth in Singularity" but plots a consumption ratio (level relative to pre-singularity). Consider "Consumption Multiple in Singularity" or "Consumption Ratio (Post/Pre-Singularity)."

## Priority Order

1. Fix Proposition 2 proof (theory-deadweight) — paper.tex
2. Fix fig-extension-panels visuals (visual-figures-image-only) — generate-exhibits.R
3. Introduction "would vanish" fix — paper.tex
4. Panel (b) y-axis label — generate-exhibits.R
