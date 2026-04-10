# Improvement Plan
AUTHOR PLAN — 2026-04-09 21:01:44 EDT

## Current Status

**20 pass / 5 fail** out of 25 tests. No section needs an overhaul — the model is structurally sound (factcheck-theory, theory-clarity both pass). All issues are fixable incrementally.

## Failing Tests and Fixes

### 1. factcheck-lit (CRITICAL) — Phantom author in bibliography

**Issue:** `references.bib` lists four authors for `KoganPapanikolaouSeruStoffman2020`: Kogan, Papanikolaou, **Seru**, Stoffman. The actual JPE 2020 paper has only three authors: Kogan, Papanikolaou, Stoffman. Seru is from a different paper by overlapping authors (QJE 2017).

**Fix:**
- Remove `Seru, Amit` from the author field in `references.bib`.
- Rename the bib key to `KoganPapanikolaouStoffman2020` throughout `references.bib` and `paper.tex`.

### 2. factcheck-freely — Proof issues in Propositions 1 and 2

**Issue A:** Appendix A (line 289) claims the post-singularity P/D ratio equals the pre-singularity one and calls this "exact when the economy is stationary conditional on the new share." This is self-contradictory — after a singularity, θ changes, so Γ^AI and Γ^N change, and the P/D ratio differs.

**Fix A:** Rewrite the parenthetical to be honest about the approximation. State that treating the post-singularity P/D ratio as approximately equal to the pre-singularity one is an approximation that becomes exact only when Δθ → 0, and that the approximation is good for small Δθ. Remove the false stationarity claim.

**Issue B:** Proposition 2(iii) states the *ratio* (P^AI/D^AI)/(P^N/D^N) decreases in ξ without qualification, but the proof only gives intuition. The ratio involves convex functions and monotonicity isn't guaranteed for all parameters.

**Fix B:** Add a qualifier "for the parameterizations considered" or prove it more carefully. The simplest fix: note that both P/D ratios have the form A/(1−A), which is increasing and convex in A. Since ξ enters only through the singularity term and reduces the weight on that term proportionally, the ratio narrows. Add a brief analytical argument or restrict the claim.

**Issue C (borderline):** Section 4.2 says "AI owners' surplus" but the formula taxes total post-singularity consumption.

**Fix C:** Change "surplus" to "post-singularity consumption" or "post-singularity income" in line 222.

### 3. visual-figures and visual-figures-image-only — Figure 2 readability

**Issue A:** Greek letters η and φ in legend labels render as ".." placeholders in PDF. The code uses Unicode characters (`\u03b7`, `\u03c6`) which don't embed in the default R PDF device.

**Fix A:** In `generate-exhibits.R`, replace Unicode strings in `scenario_labels` with R `expression()` or `bquote()` calls so Greek letters render properly in PDF.

**Issue B:** Axis labels, tick labels, panel titles, and legend text are too small in both panels of Figure 2.

**Fix B:** The code already uses `base_size = 18` and explicit sizes (15–17pt). The issue is likely the wide output dimensions (`width = 14, height = 6`) diluting the font sizes. Either increase `base_size` further (e.g., 20–22) or reduce figure width. Also ensure `ggsave` dimensions match the `\includegraphics[width=\textwidth]` scaling in the paper.

### 4. writing-intro — Argument clarity and flow

**Issue A:** The argument that financial market solutions are under-discussed and frictions limit their effectiveness (spec argument c) is not articulated as a crisp, skimmable claim. It's buried in scene-setting.

**Fix A:** Add a sentence to paragraph 2 or create a short bridging sentence that explicitly states: financial markets could in principle provide hedging, but frictions — illiquidity, private ownership, the non-existence of future capital — limit their effectiveness. Make this a distinct claim, not scene-setting.

**Issue B:** Paragraph 3 is overloaded (5 ideas: GKP lineage, model setup, closed-form solutions, quantitative result, extinction attenuation).

**Fix B:** Split paragraph 3. Move the GKP intellectual-lineage sentence into a new short paragraph or integrate it earlier. Keep the model description, results, and extinction mechanism in separate logical units.

**Issue C:** P3→P4 transition is abrupt; P5→P6 transition is jarring (economic argument to meta-commentary).

**Fix C:** Add a bridge sentence at P4 opening connecting pricing distortion to real distortion. For P5→P6, add a transitional sentence that connects the transfer result to the broader theme before pivoting to the meta-commentary.

## Execution Order

1. **factcheck-lit fix** — bib key correction (quick, high-confidence)
2. **visual-figures fixes** — Greek letter rendering + font sizes in R code, then regenerate exhibits
3. **factcheck-freely fixes** — proof corrections in paper.tex
4. **writing-intro fixes** — introduction restructuring
