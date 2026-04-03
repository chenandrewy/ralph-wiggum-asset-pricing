# Improvement Plan
AUTHOR PLAN — 2026-04-02 22:23:43 EDT

## Current Status: 11/16 tests pass, 5 fail. No build issues. Referees disabled.

---

## Failing Tests (priority order)

### 1. factcheck-theory — Subscript overload (time vs regime)

**Problem:** `V_0^A` uses 0 for "pre-singularity regime" while `E_0` uses 0 for "time zero." Same numeral, different semantics.

**Fix:** Rename regime subscripts on V to text labels. Use `V_{\mathrm{pre}}^A`, `V_{\mathrm{post}}` (or similar) throughout. This touches Proposition 1, its proof, Propositions 2–3, the appendix proof, the numerical illustration paragraph, and the extension equations. Keep `E_0`, `E_t` as-is (standard notation).

---

### 2. factcheck-anaphora — "this" at line 202 points to wrong content

**Problem:** After Proposition 2, "When this holds, adding singularity risk increases the AI stock's price because the hedging benefit outweighs the direct effect of the regime change on discount rates." The demonstrative "this" points to eq (13), which is just a threshold inequality — it says nothing about two competing forces.

**Fix:** Rewrite the sentence so it doesn't attribute the two-force decomposition to the equation. E.g.: "When this condition holds, the singularity-state contribution to valuation exceeds the no-singularity baseline, so adding singularity risk raises the AI stock's price."

---

### 3. factcheck-freely — Three issues

**(a) AI owners' "gains" mislabeled (Section 4.2):** The expression `(ω − ω̃)Y` is the transfer needed to restore the household's share, not the AI owners' gains from the singularity. Fix: relabel as "the transfer amount" or compute the actual AI-owner surplus correctly, accounting for the output-level change.

**(b) Assumption 3 claim incomplete:** "automatically satisfied for γ > 1" is only true when g > 0 and g̃ > 0. Fix: add ", given positive growth rates" or state g > 0 explicitly.

**(c) Extinction ∞×0 indeterminacy (Section 4.1):** When consumption drops to zero, the SDF → ∞ while the asset payoff → 0. The paper implicitly treats this as zero without justification. Fix: add a brief sentence noting the convention (standard in rare-disasters literature) or define the extinction state as yielding zero asset value by assumption.

---

### 4. spec-economic — Model definitions broader than spec

**Problem:** Spec says "singularity" means AI "vastly increases" productivity and "negative singularity" is "devastating." Model allows any g̃ > g and any Δ < 1, including trivially small changes.

**Fix:** Add parameter restrictions that anchor the model to the spec's intent. Options:
- Add language in Section 2.1 that the model nests mild and extreme cases but the paper's focus is on large disruptions, with the numerical illustration calibrated to a devastating scenario.
- Alternatively, tighten Assumption 1 to require Δ sufficiently below 1 (e.g., "substantially" displaced), and note that the singularity is intended to capture a large productivity shift. The extension already handles g̃ → ∞.

The lightest fix: add qualifying language in the environment section making clear the paper's economic focus is on large disruptions, even though the algebra holds more generally.

---

### 5. element-lit-review — Missing citations

**Problem:** Missing Knesl (2023 JFE) on automation displacement and asset pricing (critical), Garleanu-Panageas (2015 JPE) on OLG asset pricing with incomplete risk-sharing (important), and Babina et al (2024 JFE) on AI and firm growth (important).

**Fix:** Add these three citations to `references.bib` and integrate brief mentions into the Related Literature paragraph. Knesl is the most urgent — a referee would flag it. Keep the lit review within the half-page limit; may need to tighten existing sentences to make room.

---

## Execution Order

1. **Notation fix** (factcheck-theory) — most mechanical, touches many equations, do first to avoid merge conflicts.
2. **Anaphora fix** (factcheck-anaphora) — one-sentence rewrite.
3. **Factcheck-freely fixes** (a), (b), (c) — three localized edits.
4. **Spec-economic alignment** — add qualifying language in Section 2.1.
5. **Lit review additions** — add citations and update bib.
