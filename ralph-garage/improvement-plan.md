# Improvement Plan
AUTHOR PLAN — 2026-04-02 22:37:05 EDT

**Status**: 9/16 tests pass. 7 failures, but most stem from a single root cause.

## Key Issues

The dominant issue is the **commented-out Figure 1** (Exhibit 1, CRSP valuations figure). This single problem causes cascading failures across 5 tests (factcheck-code, factcheck-freely, factcheck-narrative, spec-paper, visual-figures, visual-pages). The remaining failures are a too-long lit review and imprecise economic claims.

No overhaul is needed. The model section is sound (factcheck-theory and quality-formalism pass). Fixes are surgical.

## Plan

### 1. Uncomment Exhibit 1 (Figure 1) — fixes 5+ tests

Uncomment lines 45–50 of `paper.tex` to restore the CRSP figure (`ai-valuations.pdf`). This resolves:
- Broken `Figure~\ref{fig:ai-valuations}` cross-reference (factcheck-narrative, visual-pages)
- Unused file in `paper/exhibits/` (spec-paper III.1.d)
- Missing exhibit comment (spec-paper III.2.b)
- Empty figure manifest (visual-figures)
- Paper-code inconsistency (factcheck-code)

### 2. Fix `run-all.R` graceful degradation — fixes factcheck-code

The header comment in `run-all.R` claims the numerical table is still generated without WRDS credentials, but the pipeline actually crashes. Either:
- (a) Make the pipeline degrade gracefully (wrap the CRSP script call in tryCatch), or
- (b) Remove the misleading comment.

Option (a) is better since it also fixes spec-paper III.3.c.

### 3. Trim the lit review to ≤ half a page — fixes element-lit-review

The lit review currently spans ~3/4 to 1 page. Condense by:
- Shortening the displacement-risk paragraph: merge the Garleanu-Panageas (2015) and Kogan-Papanikolaou-Stoffman (2020) discussion into a single sentence.
- Trimming the AI economics paragraph: cut Acemoglu-Restrepo (2018) and Korinek-Suh (2024), which are tangential to the asset pricing contribution.
- Consider adding Zhang (2019, JF) on labor-technology substitution in a brief mention, if space permits after trimming.

### 4. Fix imprecise SDF claim at line 142 — fixes factcheck-freely

Change "because the household's consumption falls at the singularity ($\Delta < 1$)" to clarify that the consumption *share* falls, or qualify the claim. For the paper's calibration the consumption *level* also falls (since $\Delta(1+\tilde{g}) < 1$), but the text should not conflate share and level. Suggested fix: "because displacement reduces the household's consumption share ($\Delta < 1$), pushing up marginal utility in singularity states."

### 5. Add $\tilde{g}$ dependence to Proposition 2 verbal characterization — fixes factcheck-freely

Lines 190–196: the verbal characterization of when $\partial V_{\mathrm{pre}}^A / \partial p > 0$ lists $\Delta$ small, $\gamma$ large, $\tilde{\theta}/\theta$ large but omits that the condition *fails* when $\tilde{g}$ is very large (for $\gamma > 1$). Add a clause: "or when post-singularity growth $\tilde{g}$ is not too large."

### 6. Rename Section 2.4 "Equilibrium" — fixes factcheck-narrative

The section only states parameter restrictions for finite PD ratios; the actual equilibrium characterization is in Section 3. Rename to "Parameter Restrictions" or "Existence Conditions."
