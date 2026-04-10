# Improvement Plan
AUTHOR PLAN — 2026-04-09 21:31:55 EDT

## Current State

- **Tests**: 23/25 passing. Two failures: `factcheck-lit`, `visual-figures-image-only`.
- **Model**: Core structure is sound. No overhaul needed.
- **Code**: Pipeline runs; generates 3 exhibits to `paper/exhibits/`.

---

## Priority 1: Fix Failing Tests

### 1a. `factcheck-lit` — Ghost author in bib entry

The entry `KoganPapanikolaouSeruStoffman2020` lists four authors (Kogan, Papanikolaou, **Seru**, Stoffman) but the actual JPE 2020 paper "Left Behind: Creative Destruction, Inequality, and the Stock Market" has only three: Kogan, Papanikolaou, and Stoffman. Amit Seru is a coauthor on a different paper (QJE 2017).

**Fix:**
- `paper/references.bib`: Remove "Seru, Amit" from the author field. Rename key to `KoganPapanikolaouStoffman2020`.
- `paper/paper.tex`: Update all `\citet`/`\citep` calls referencing the old key.

### 1b. `visual-figures-image-only` — Extension figure contrast and headroom

`fig-extension-panels.pdf` fails on: (a) light-gray grid lines with insufficient contrast, and (b) Panel (a) y-axis headroom >20%.

**Fix in `code/generate-exhibits.R`:**
- Darken `panel.grid.major` from `"gray35"` to `"gray20"` or darker in `theme_paper`.
- Tighten `y_cap_a` (currently 20) to bring headroom within 20% of the data span. If data tops out near 18, cap at ~19.

---

## Priority 2: Paper Improvements

### 2a. Literature coverage — unused but relevant bib entries

Eight bib entries exist but are never cited. Several are highly relevant:
- Acemoglu (2024) — important AI economics counterpoint
- Korinek & Suh (2024) — AGI transition scenarios
- Aghion, Jones & Jones (2019) — AI and economic growth

**Fix:** Integrate the most relevant 2–3 of these into the related-literature paragraph (Section 1). Keep the lit review under half a page per spec.

### 2b. Transfers formula — clarify α vs θ relationship

Section 4.2 uses $(1 - \phi\alpha)$ as the AI owners' surplus in the transfer formula (Eq. 6), but the model defines both $\alpha_t$ (household consumption share) and $\theta_t$ (AI dividend share) as separate objects. The transfer formula implicitly conflates them.

**Fix:** Add a brief sentence in Section 4.2 stating the simplifying assumption that $\alpha = \theta$ (household consumption share equals AI dividend share) for the transfer analysis, or derive the formula explicitly in terms of both parameters.

### 2c. $\phi_\text{eff}$ substitution — add brief derivation

The paper states $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$ and says P/D follows by replacing $\phi$, but provides no derivation. 

**Fix:** Add 2–3 lines showing how the post-transfer household consumption maps back to the effective displacement factor $\phi_\text{eff}$ in the SDF.

### 2d. Proposition 1 approximation — surface in main text

The approximation that post-singularity P/D equals pre-singularity P/D (exact only as $\Delta\theta \to 0$) is disclosed only in the Appendix A proof. With baseline $\Delta\theta = 0.2$, this merits a brief remark in the main text near Proposition 1.

**Fix:** Add a sentence after Proposition 1 or in the discussion (Section 2.3) noting the approximation and its accuracy condition.

---

## Sequencing

1. Fix bib ghost author (1a) — straightforward text edit.
2. Fix extension figure (1b) — code change + regenerate exhibits.
3. Rebuild paper PDF and page images after 1–2.
4. Address 2a–2d in paper.tex as a batch.
5. Rebuild paper PDF and page images again.
