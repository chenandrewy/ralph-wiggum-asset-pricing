# Improvement Plan
AUTHOR PLAN — 2026-04-09 20:32:33 EDT

## Status: 18/25 tests pass. No overhaul needed.

## Failing Tests — Fixes

### 1. theory-deadweight (formalism bloat)
Five pieces of ceremonial or unused formalism to cut:
- **Remove Corollary 1** — its content is already stated in the preceding prose paragraph; the proof adds nothing.
- **Remove parameter λ** — introduced for a single qualitative inequality, never appears in any equation, proposition, proof, calibration, or figure. Replace its role with plain English ("the positive singularity is more likely than the negative one").
- **Remove private AI capital dividend formula** `(1-α_t)C_t - D_t^{AI}` from the Setup — it is defined and never referenced again. Describe the residual in words only.
- **Specify positive-singularity displacement** — the negative case has `α_{t+1} = φα_t` but the positive case says "the household's share increases" with no formula. Either give a symmetric formula (e.g., `α_{t+1} = min(1, α_t/φ)`) or explicitly state that the precise law of motion is not needed for the qualitative result.
- **Simplify constraint** `α_t ∈ (0, 1-θ_t]` → `α_t ∈ (0,1)` — the tighter bound never binds and is never checked.

### 2. element-gkp-cites (misattribution)
- Extension 2 opening says GKP "show that intergenerational transfers can affect the magnitude of displacement risk." GKP merely noted transfers as a possible extension in passing. Change verb from "show" to "note" or "suggest," and make clear that the transfers analysis is *our* contribution building on their remark.

### 3. element-lit-review (length)
- Lit review is ~245 words; spec requires ≤ half a page (~175–200 words at current formatting). Cut the third paragraph (six rapid-fire citations) by ~50 words. Consolidate Kogan–Papanikolaou and Kogan–Papanikolaou–Stoffman into one sentence; drop or shorten the Korinek–Suh mention.

### 4. element-rhetoric-meta (footnote tone)
- The AI-authorship footnote is ~80 words of overbearing detail ("mathematical derivations, quantitative code, figures, tables, and every sentence of prose… no human editing"). Trim to ~30–40 words: state the division of labor concisely without the itemized list that triggers skepticism.

### 5. writing-intro (paragraph transitions)
Three abrupt transitions to fix:
- **P3→P4**: P3 ends on policy; P4 opens cold with GKP citation and model mechanics. Add a bridge sentence connecting the policy gap to GKP's framework.
- **P5→P6**: P5 ends on AI regulation; P6 opens on singularity transfers. Bridge: "If blocking AI is costly, another policy lever is redistribution."
- **P6→P7**: P6 ends on "distinctive feature of singularity economics"; P7 pivots to the meta-observation about AI production. Bridge: connect the displacement theme to the paper's own production process.

### 6. visual-figures + visual-figures-image-only (figure formatting)
Changes in `code/generate-exhibits.R`:
- **fig-ai-valuations**: Expand y-axis limits so the "500" tick label is not clipped. Add `expand = expansion(mult = c(0.02, 0.05))` or increase top margin.
- **fig-extension-panels Panel (b)**: Fix truncated legend label — add closing parenthesis to `"Large singularity (eta = 9, phi = 0.05)"`. Make "No change" reference line thicker and darker (e.g., `color = "gray40", linewidth = 0.8`).
- **fig-extension-panels both panels**: Increase axis tick label size (`axis.text` to 13–14pt) and legend text size. Differentiate Panel (a) line styles more clearly (e.g., solid vs. longdash with different widths).

## Order of Operations
1. Fix `code/generate-exhibits.R` (tests 6) → regenerate exhibits
2. Fix `paper/paper.tex`: theory-deadweight, element-gkp-cites, element-lit-review, element-rhetoric-meta, writing-intro (tests 1–5)
3. Rebuild paper PDF and page images
4. Re-run tests
