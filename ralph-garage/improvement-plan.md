# Improvement Plan
AUTHOR PLAN — 2026-04-11 09:58:23 EDT

## Current Status

**Tests: 21/25 passing.** Four failures, all fixable without structural changes. No overhaul needed — the model section is mathematically sound and well-structured.

## Failing Tests (Priority)

### 1. factcheck-freely — Wrong sign in Proposition 3 proof
**Issue:** Line 233 states $\lim_{\gamma \to \infty} \Delta u(\gamma) / u(\alpha) = -\infty$, but the correct limit is $+\infty$ (both numerator and denominator are negative for $\gamma > 1$, so their ratio is positive and diverges).
**Fix:** Change "$-\infty$" to "$+\infty$" in the proof of Proposition 3(i). The surrounding economic argument is correct — just the sign on the formal limit statement is wrong.

Also fix minor bib issue: `Acemoglu2024` cite key has `year = {2025}` — update year to 2024 or key to 2025 for consistency.

### 2. spec-economic — Arrow-Debreu language in Extension 1
**Issue:** Line 217 says "the household can trade state-contingent claims with AI owners." The spec requires complete markets to be framed as access to currently unavailable assets (restricted equity), not Arrow-Debreu securities.
**Fix:** Rewrite line 217 to say the household can trade the restricted AI equity (founder stakes, pre-IPO shares) directly, consistent with the framing used everywhere else in the paper (e.g., line 179).

### 3. visual-figures-image-only — Low-contrast reference line
**Issue:** The "No change" dashed gray line at y=1 in Panel (b) of fig-extension-panels blends with background gridlines.
**Fix:** In `code/generate-exhibits.R`, change the `geom_hline` for the "No change" line to use a darker color (e.g., `"gray10"` or `"black"`) or a distinct style (e.g., `"dotted"` with thicker linewidth) so it stands out from the gray gridlines.

### 4. writing-intro — Two arguments not visible to skimmers
**Issue:** Spec arguments (c) "financial market solutions are under-discussed; frictions limit effectiveness" and (d) "singularity abundance overcomes frictions" are buried in later paragraphs.
**Fix:** Add a preview sentence in paragraph 2 (after the hedging motive claim) that briefly lists all five contributions, so a skimmer sees them early. Something like: "Market incompleteness drives not only the valuation premium but also distortions in AI development, and the abundance of resources in a singularity can overcome the very frictions that make displacement catastrophic." Also improve the Para 6→7 transition with a bridge clause.

## Passing Tests — Minor Issues Worth Addressing

### 5. writing-intro (partial fulfillments)
- **Claim 3:** The body never formally shows P/D spread collapses under complete markets. Add a brief remark after Proposition 1 or in the discussion (Section 2.3) noting that if the household could trade restricted equity, $\phi_\text{eff} \to 1$ and the spread vanishes.
- **Claim 11:** "Calls to slow AI reflect inability to share upside" is stated as a model-derived insight but only supported verbally. Frame it explicitly as an implication of Proposition 3.

## Execution Order

1. Fix the four failing tests (items 1–4) — these are all surgical edits.
2. Address the partial fulfillment issues (item 5) if space permits.
