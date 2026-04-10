# Improvement Plan
AUTHOR PLAN — 2026-04-09 20:02:59 EDT

## Status: 19/25 tests pass, 6 failing

No section overhaul needed. The baseline model is clean and load-bearing. Issues are localized: bibliography errors, notational loose ends, ceremonial formalism in Extension 1, a figure use-of-space problem, a missing spec argument, and introduction flow.

---

## Failing Tests (priority order)

### 1. factcheck-lit — Bibliography errors
**Issues:**
- `KoganPapanikolaouSchmidtSong2020`: Wrong authors. The JPE 2020 paper is Kogan, Papanikolaou, and **Stoffman**, not Schmidt and Song. Fix bib key to `KoganPapanikolaouStoffman2020`, correct authors.
- `Knesl2023`: First name is **Jiri**, not Peter.

**Fix:** Edit `paper/references.bib` to correct both entries. Update all `\citet`/`\citep` calls in `paper.tex` to use the corrected key.

### 2. factcheck-theory — Notation and traceability
**Issues (medium severity):**
- `$U_0$` lacks the `$H$` superscript used elsewhere (`$\Delta U^H$`). Change to `$U_0^H$`.
- `$u_\text{ext}$` should be `$U_\text{ext}$` (lifetime utility, not period).
- `$\delta_0$` subscript is unexplained — simplify to `$\delta$`.
- `$\alpha_0 = 0.70$` used in R code for Figure 2 but never stated in the paper. Add it to the figure caption or the Extension 2 parameterization text.
- Effective-$\phi$ formula for P/D with transfers is used in code but not derived in paper. Add a one-line derivation or state it explicitly.

**Fix:** Make targeted edits to `paper.tex` notation and add the missing parameter disclosure. Update code variable name from `delta0` to `delta` if the paper notation changes.

### 3. spec-paper — Missing argument I.3c
**Issue:** The paper never argues that "financial market solutions to AI disaster risk are under-discussed, though frictions can limit their effectiveness."

**Fix:** Add 1–2 sentences to the introduction (around the incomplete-markets discussion) noting that financial market solutions — such as broader trading of AI-linked securities — are under-explored in the AI risk discourse, though market frictions limit their reach. This naturally bridges from the hedging argument (3a) to the model setup.

### 4. theory-deadweight — Ceremonial formalism in Extension 1
**Issue:** Extension 1 introduces $\kappa$, $\phi^+$, and Eq. (6) but the proof of Proposition 3 never manipulates them analytically. The entire argument is qualitative, making the formal apparatus deadweight.

**Fix:** Streamline Extension 1:
- Remove Eq. (6) ($\Delta U^H$). State Proposition 3 in plain economic terms.
- Drop $\kappa$ as a named parameter; describe the veto cost verbally ("a per-period utility cost of blocking").
- Keep $\phi^+$ only in the itemized setup for clarity but do not name it as a formal parameter.
- Keep $\lambda$ and the condition $\lambda > 1/2$ since they are economically meaningful.
- The proof becomes a self-contained qualitative argument (which it already is).

### 5. visual-figures-image-only — Panel (a) asymptotic spike
**Issue:** The large-singularity P/D line shoots up near $\tau \approx 5\%$, compressing meaningful variation into the bottom third.

**Fix:** In `code/generate-exhibits.R`, cap the y-axis on Panel (a) at a reasonable ceiling (e.g., 25–30) or use a log scale. A y-axis cap with a clear annotation ("P/D → ∞ as τ → 0") is the simplest fix and preserves the economic message. Also check that `y_min_a` logic still works.

### 6. writing-intro — Flow and clarity
**Issues:**
- Missing argument 3c (addressed in #3 above).
- P2→P3 transition is abrupt (citation-first sentence).
- P3 (contribution list) tells *what* but not *why it matters*.
- P5 is overloaded (two extensions + policy in one paragraph).
- "Proposition 2(iii)" reference is jarring for intro readers.
- AI-authorship disclosure is buried.

**Fix:** Rewrite the introduction with these changes:
- Add a bridge sentence before the GKP contribution paragraph.
- Expand the contribution list to briefly explain *why* each point matters.
- Split P5 into two paragraphs: one on the veto/development distortion, one on transfers.
- Replace "Proposition 2(iii)" with plain English ("extinction risk attenuates this gap by reducing the weight on...").
- Give the AI-authorship disclosure its own closing sentence or brief paragraph.
- Integrate the "under-discussed" argument (from #3) naturally into the flow.

---

## Execution Order

1. **Bib fixes** (#1) — quick, no dependencies.
2. **Notation/traceability** (#2) — quick edits to paper.tex and code.
3. **Extension 1 streamlining** (#4) — reduces formalism, may shorten paper.
4. **Figure fix** (#5) — code change + regenerate exhibits.
5. **Intro rewrite** (#6 + #3) — depends on all above being settled first, since intro references model content.
