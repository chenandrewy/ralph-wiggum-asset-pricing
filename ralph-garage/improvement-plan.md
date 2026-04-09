# Improvement Plan
AUTHOR PLAN — 2026-04-09 19:15:07 EDT

## Status: 19/25 tests pass, 6 fail

## Critical Issue: Extension 2 Calibration Breaks P/D Formula

The P/D formula (Proposition 1) has the form $A/(1-A)$ and requires $A < 1$ for a valid price. This condition is **never stated** in the paper. Worse, the Extension 2 large-singularity calibration ($\eta = 9$, $\phi = 0.05$) violates it: $A = 2.37$ for AI stocks, producing undefined P/D ratios. The code silently returns NA, and the figure only plots where defined, but the paper never acknowledges the constraint or explains why P/D is undefined at $\tau = 0$ for the large singularity.

This is not an overhaul — the model is structurally sound — but it is the highest-priority fix.

## Plan (ordered by priority)

### 1. Fix P/D existence condition and Extension 2 calibration
**Test:** `factcheck-theory`

- Add an explicit existence condition to Proposition 1: the P/D ratio is well-defined iff $A < 1$, where $A$ is the numerator. State this as a remark or assumption.
- Recalibrate Extension 2's large-singularity parameters so that P/D is defined at $\tau = 0$. Options:
  - **Option A (preferred):** Reduce $\gamma$ or increase $\phi$ for the large-singularity scenario so that $A < 1$. E.g., $\phi = 0.15$ with $\eta = 9$ gives $\phi(1+\eta) = 1.5$ and $\phi^{-\gamma} = 1975$, which may work.
  - **Option B:** Keep current parameters but explicitly discuss that P/D diverges (prices go to infinity) as a feature — the hedge value is so extreme that AI stocks are infinitely valuable, making the case for transfers even stronger. The figure then starts from the first $\tau$ where P/D is finite.
- Regenerate table and figure with `code/generate-exhibits.R`.
- Update paper text in Section 4.2 to match the new calibration or the new discussion.

### 2. Fix citation errors
**Test:** `factcheck-lit`

- **references.bib:** Change `KoganPapanikolaouSchmidtSong2020` authors to `Kogan, Leonid and Papanikolaou, Dimitris and Stoffman, Noah`. Update the citation key to `KoganPapanikolaouStoffman2020`. Update all `\citet`/`\citep` references in `paper.tex`.
- **Nordhaus framing:** Change "the kind of explosive output growth discussed by \citet{Jones2024} and \citet{Nordhaus2021}" to something like "the kind of explosive output growth modeled by \citet{Jones2024} and examined critically by \citet{Nordhaus2021}" to accurately reflect Nordhaus's skeptical stance.

### 3. Fix opening figure — use real data
**Test:** `element-opening-fig`

- Replace hardcoded P/E values in `code/generate-exhibits.R` with actual data. The spec (paper-spec.md IV.8.b) says empirical content should be "very limited, ideally to a single figure." Use a simple, documentable source.
- Check `ralph/code-templates/` for WRDS access patterns. Download P/E data for an AI-exposed portfolio vs. S&P 500 from WRDS (or use a simple publicly verifiable approach).
- Remove "(Illustrative)" from the figure caption and the hedge phrase "based on approximate values" from the intro text.
- Update `code/generate-exhibits.R` so the pipeline runs from scratch as required by spec III.3.c.

### 4. Improve Extension 2 figure
**Tests:** `element-transfers-fig`, `visual-figures-image-only`

- **Catastrophe visibility:** Add an annotation or marker at $\tau = 0$ in Panel (b) highlighting the household's consumption loss (e.g., annotate "Catastrophe: 50% loss" with an arrow at the y-intercept of the large-singularity line).
- **Grid contrast:** Change `panel.grid.major` from `"gray70"` to `"gray50"` or darker in `theme_paper`.
- **Panel (a) vertical space:** Set `scale_y_continuous(limits = c(NA, NA))` or adjust y-axis lower bound to reduce whitespace below data.
- **Caption:** Add a brief note connecting panels (a) and (b) — transfers reduce hedge value (panel a) while improving consumption (panel b).

### 5. Fix intro paragraph structure
**Test:** `writing-intro`

- Make argument (d) — that singularity abundance can overcome market frictions — visible to a skim-reader. Currently buried mid-paragraph.
- Option: Split paragraph 3 so that the abundance-overcomes-frictions idea leads its own sentence or short paragraph. E.g., start a new paragraph with something like "And if the singularity actually occurs, the explosive growth in output may itself overcome these frictions."

### 6. Remaining figure polish
**Test:** `visual-figures-image-only`

- Fix `fig-ai-valuations` caption: add brief description of which firms and what P/E measure.
- These visual fixes apply to both figures and are partially addressed in steps 3-4 above.
