# Improvement Plan
AUTHOR PLAN — 2026-04-02 18:25:11 EDT

**Status:** 6/16 tests pass, 10 fail. Build OK. No overhaul needed — model section is sound (factcheck-theory, quality-formalism, spec-economic all pass). Focus on infrastructure gaps and content fixes.

---

## Priority 1: Infrastructure (blocks 4+ tests)

### 1a. Create `code/` pipeline and `paper/exhibits/` directory
**Fixes:** factcheck-code, factcheck-exhibits, spec-paper, visual-figures

- Create `paper/exhibits/` directory.
- Write R scripts in `code/` with a single canonical entry point that:
  - Computes the numerical illustration from Section 3 (P/D ratios for given parameters) and outputs a table to `paper/exhibits/`.
  - Generates a CRSP-based figure comparing AI vs. non-AI stock valuations (spec I.8.b / IV.8.b) and outputs a PDF to `paper/exhibits/`.
- Add `\input` / `\includegraphics` calls in `paper.tex` for the new exhibits.
- The pipeline must run from scratch in under 180 seconds.

### 1b. Fix hyperref red boxes
**Fixes:** visual-pages

- Add `hidelinks` option to the `\usepackage[...]{hyperref}` line in `paper.tex`.

---

## Priority 2: Unproven or overstated claims (blocks 3 tests)

### 2a. Non-AI valuation claim
**Fixes:** factcheck-bysection, factcheck-narrative

- The introduction and conclusion assert unconditionally that non-AI valuations *fall* with singularity probability. The paper only proves the AI case (Proposition 3) and the cross-sectional spread (Proposition 2), not the non-AI comparative static.
- **Fix:** Either (a) add a Proposition/Corollary proving $\partial V_0^N / \partial p < 0$ under stated conditions, or (b) qualify the intro/conclusion claims to say the *spread* widens rather than asserting non-AI stocks fall unconditionally.

### 2b. "Moderate singularity" claim
**Fixes:** factcheck-bysection

- The conclusion asserts the hedging premium is "largest for moderate singularities." This is stated in Remark 2 but never formally proved.
- **Fix:** Either add a brief formal argument (e.g., show the premium is hump-shaped in singularity severity by combining Remark 1 and Remark 2) or soften the language to "suggests" / "the preceding analysis indicates."

### 2c. Conclusion conflation
**Fixes:** factcheck-bysection

- The conclusion paragraph conflates two distinct mechanisms: (i) utility curvature making marginal utility negligible at extreme consumption (Remark 1) and (ii) friction costs becoming negligible relative to surplus (Remark 2).
- **Fix:** Distinguish the two channels clearly in the conclusion.

---

## Priority 3: Citation accuracy (blocks 2 tests)

### 3a. GKP characterization
**Fixes:** quality-gkp-cites

Three passages need revision:
1. **Line ~79 (model, AI owners):** Don't equate "illiquid private ventures" with GKP's unborn-cohorts mechanism as if they are the same thing. Present them as the paper's interpretation, inspired by GKP.
2. **Line ~253 (extension, "do not analyze further"):** GKP devote a paragraph and footnote to transfers. Revise to something like "GKP discuss these mechanisms but do not conduct a formal analysis of how they scale with output."
3. **Line ~273 (extension, "incremental innovation"):** GKP never restrict their framework to incremental innovation. Remove or restate.

### 3b. Missing literature
**Fixes:** element-lit-review

- Add Kogan, Papanikolaou, and Stoffman (2020, JPE) — the published version of the displacement risk theory — and Kogan and Papanikolaou (2014) to the lit review and bibliography.

---

## Priority 4: Minor content fixes

### 4a. Anaphora overgloss (line 108)
**Fixes:** factcheck-anaphora

- The sentence after the definition of $\Delta$ says "the singularity displaces the household by shifting output toward private AI capital." Assumption 1 only states the household share falls; the mechanism (shifting toward private AI) is interpretive. Remove the causal gloss or attribute it as interpretation.

### 4b. Extension: infinite consumption asymmetry
**Fixes:** spec-paper

- Spec I.5.b requires explicitly stating that infinite consumption in the extension applies only to AI owners. Add a sentence in Section 4.1 or 4.2 making this explicit.
