# Improvement Plan
AUTHOR PLAN — 2026-04-02 18:14:05 EDT

## Status: 8/16 tests passing

No overhaul needed. The model and proofs are mathematically correct. The failures are targeted issues: false comparative statics claims, missing code/exhibits infrastructure, and notation/spec inconsistencies.

---

## Priority 1: Fix false gamma comparative statics claims

**Tests:** factcheck-bysection, factcheck-narrative, factcheck-freely

The paper claims in four places that valuations/spreads/premiums increase with risk aversion gamma. This is **numerically false** — the spread V0^A - V0^N actually *decreases* with gamma for the paper's own parameters (6.82 at gamma=2, 4.53 at gamma=3, 3.19 at gamma=5). The hedging premium is non-monotone in gamma.

The root cause: gamma appears in Delta^{-gamma} (increasing) but also in (1+g_tilde)^{1-gamma}, V1, and the denominator (all decreasing). The net effect is ambiguous.

**Fixes:**
1. **Abstract (line 30):** Remove "and with risk aversion" from the sentence about what increases the P/D ratio.
2. **After Proposition 2 (line 190):** Remove the claim about gamma. Keep the correct claims about p and (1-Delta).
3. **Proposition 4 (line 215):** Remove "increasing in risk aversion gamma" from the comparative statics list. Keep p, theta-tilde/theta, and 1-Delta which are straightforward from the formula.
4. **Conclusion (line 279):** Remove "with risk aversion" from the summary of comparative statics.

## Priority 2: Fix Remark 1 gamma < 1 claim

**Tests:** factcheck-bysection, factcheck-freely

Remark 1 (line 245) claims the hedging premium grows without bound when gamma < 1 and g_tilde -> infinity. But gamma < 1 violates Assumption 3 (existence condition) in this limit, so the P/D formulas are undefined. The paper draws conclusions outside its valid parameter space.

**Fix:** Remove the gamma < 1 case from Remark 1 entirely, or add a brief note that the existence condition fails. The gamma > 1 and gamma = 1 cases are fine.

## Priority 3: Fix conditional vs. unconditional p claim

**Test:** factcheck-narrative

The abstract and introduction state unconditionally that the P/D ratio increases with p. Proposition 3 establishes this only under condition (12). The condition is natural but the verbal claims should match the formal result.

**Fix:** Add a qualifier in the abstract and introduction — e.g., "when displacement is sufficiently severe" or "under natural parameter restrictions." Alternatively, state the result holds "for empirically relevant parameters."

## Priority 4: Fix singularity definition (g_tilde >= g vs. strict)

**Test:** spec-economic

The spec says a singularity "vastly increases productivity and output" but the model uses weak inequality g_tilde >= g, allowing g_tilde = g (no increase). The numerical illustration uses g_tilde = 0.05 vs g = 0.02, which is modest, not "vast."

**Fix:** Change the weak inequality to strict: g_tilde > g. Add a sentence noting the model allows for any magnitude of productivity increase, with the extension exploring the limit of vast increases (g_tilde -> infinity). The verbal descriptions in the abstract/intro should mention the productivity increase alongside displacement.

## Priority 5: Fix GKP quote

**Tests:** factcheck-bysection, factcheck-freely

Line 252 presents a direct quote from GKP but omits material without ellipses and changes "or" to "[and]."

**Fix:** Either convert to a paraphrase (remove quotation marks) or use the full quote with proper ellipses for omitted material.

## Priority 6: Fix Delta notation collision

**Test:** factcheck-theory

Delta is defined as tilde-omega/omega in eq. (5), then silently redefined as Delta(lambda) in Section 4.2 eq. (11).

**Fix:** Add a bridging sentence when introducing Delta(lambda): "We now generalize the displacement ratio to depend on the transfer parameter lambda, with the earlier definition corresponding to lambda = 0."

## Priority 7: Create exhibits and code pipeline

**Tests:** factcheck-exhibits, visual-figures, spec-paper

The paper has zero exhibits. The spec calls for "ideally a single figure in the introduction illustrating the valuation of publicly traded AI stocks compared with non-AI stocks using CRSP data." The code/ directory is empty, and paper/exhibits/ does not exist.

**Fixes:**
1. Create `paper/exhibits/` directory.
2. Write R code in `code/` with a single entry point that:
   - Downloads AI vs non-AI stock P/D data from CRSP/WRDS
   - Produces a single PDF figure comparing valuations
   - Outputs to `paper/exhibits/`
3. Include the figure in the introduction.
4. Runs in under 180 seconds.

## Priority 8: Minor cleanup

**Tests:** factcheck-freely (minor items)

- Fix Assumption 3 commentary: "automatically satisfied for gamma > 1" — remove "and sufficiently large g or g_tilde" since any g >= 0 suffices.
- Remove unused bibliography entries (MehraPrescott1985, CampbellCochrane1999, Blanchard1985).
