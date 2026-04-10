# Improvement Plan
AUTHOR PLAN — 2026-04-09 19:43:43 EDT

## Status: 17/25 tests passing, 8 failing. No overhaul needed.

The model section is sound (factcheck-theory, theory-clarity, factcheck-code all pass). Issues are in exposition, citations, figure quality, and formatting. Plan prioritizes failing tests, then addresses remaining quality.

---

## 1. Fix bib: wrong authors on Kogan et al. (2020) [factcheck-freely]

**File:** `paper/references.bib` lines 134-142

The entry `KoganPapanikolaouStoffman2020` lists Kogan, Papanikolaou, and Stoffman. The correct authors are Kogan, Papanikolaou, **Schmidt**, and **Song**. Rename the bib key to `KoganPapanikolaouSchmidtSong2020` and fix the author field. Update the cite key in `paper/paper.tex` line 71 accordingly.

---

## 2. Fix "shrink" language for non-AI dividends [factcheck-bysection]

**File:** `paper/paper.tex` ~line 152

The text says non-AI stocks' dividends "shrink" upon singularity. With baseline parameters, $\Gamma^N = 1.2 > 1$ so non-AI dividends grow in absolute terms; they only shrink as a share of the economy. Change "shrink" to "shrink as a share of the economy" or "grow less than aggregate consumption."

---

## 3. Fix GKP characterization in Extension 2 opening [element-gkp-cites]

**File:** `paper/paper.tex` ~line 248

Three issues in the sentence "\citet{GKP2012} note that intergenerational transfers affect the magnitude of displacement risk but treat such mechanisms as inessential extensions to their framework. We take a closer look."

- "note" minimizes a substantive GKP passage (their Section 3.2 paragraph).
- "inessential extensions" misrepresents GKP's technical usage — they mean the SDF functional form is unchanged, not that transfers are unimportant.
- "We take a closer look" implies examining the same mechanism, when Extension 2 operates in a different model.

Rewrite to: accurately convey GKP's point (transfers don't change the SDF form but affect displacement magnitude), and frame Extension 2 as studying transfers in a different setting (AI singularity) rather than as a deeper look at GKP's mechanism.

---

## 4. Add Knesl (2023, JFE) to lit review [element-lit-review]

**File:** `paper/references.bib`, `paper/paper.tex` (lit review paragraph)

Add: Knesl, Peter (2023). "Automation and the Displacement of Labor by Capital: Asset Pricing Theory and Empirical Evidence." *JFE* 147(2), 271-296. This paper directly models and tests automation-driven displacement risk in asset prices — squarely on topic and in a target journal. Integrate a brief mention in the lit review paragraph alongside the Kogan-Papanikolaou citations.

---

## 5. Add appendix section-number comment [spec-paper]

**File:** `paper/paper.tex` ~line 293

The appendix section `\section{Proof of Proposition~\ref{prop:pd-ratios}}` lacks a section-number comment. Add `% Appendix A` after it, consistent with the comment style used for all other sections.

---

## 6. Fix extension figure contrast and scale compression [visual-figures-image-only]

**File:** `code/generate-exhibits.R` (Panel b of extension figure)

Two issues:
- **Contrast:** The baseline (salmon) line is too light, especially in Panel (b). Use darker, more saturated colors (e.g., dark red/orange for baseline, dark blue for large singularity).
- **Scale compression in Panel (b):** Baseline peaks at ~1.0 while large singularity reaches ~6.5, crushing baseline into bottom 15%. Use a log scale on the y-axis, or use `facet_wrap` with free y-scales to give each scenario adequate visual weight.

Also apply the same color improvements to Panel (a) for consistency.

---

## 7. Fix page 8 blank space (table float placement) [visual-pages]

**File:** `paper/paper.tex` ~lines 192-197

Page 8 has Section 3 header + short paragraph followed by ~80% whitespace, with Table 1 on page 9. Fix by either:
- Adding `[!htbp]` or `[H]` to the table float (already uses `[H]` — check if the `float` package is loaded).
- Restructuring to place the table immediately after the parameter description, or moving the parameter discussion below the table reference.

Likely the issue is that the table is too large to fit on the same page as the preceding Section 2 content. Rearrange so Section 3's text and table appear together without a nearly empty page.

---

## 8. Improve introduction flow [writing-intro]

**File:** `paper/paper.tex` introduction (lines 39-72)

Four structural issues identified:
- **Paragraph 3** ("Despite a growing literature...") stalls momentum. It says "not much work has been done" without advancing the argument. Fold the under-discussed point into the motivation or delete.
- **Paragraph 4** (singularity overcomes frictions) introduces extension logic too early and too cryptically. Move this preview to after the model description paragraph, or make it more concrete.
- **Paragraph 6** (GKP positioning) comes after the model description rather than before. Move GKP positioning to immediately after the motivation, before the model machinery paragraph.
- **Paragraph 8** (AI-authorship disclosure) creates a tonal rupture after quantitative results. Integrate the disclosure more smoothly — perhaps as a brief final sentence of the preceding paragraph rather than a standalone shift.

Restructure introduction paragraph order: (1) opening/figure, (2) hedging motive + incompleteness, (3) GKP positioning, (4) model description, (5) extensions preview, (6) quantitative results + AI disclosure, (7) lit review.
