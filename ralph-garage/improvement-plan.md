# Improvement Plan
AUTHOR PLAN — 2026-04-11 10:12:09 EDT

## Current State

- **Tests:** 23/25 pass. Two failures: `visual-figures-image-only`, `writing-intro`.
- **Referees:** Disabled (not run).
- **Model section:** Sound — no overhaul needed. Propositions, proofs, and quantitative analysis are clean and internally consistent.
- **Code:** Generates all three exhibits correctly. Single entry point, runs from scratch.

## Failing Tests

### 1. `visual-figures-image-only` — Panel (a) annotation contrast

**Problem:** The annotation `$P/D \to \infty$ as $\tau \to 0$` in Panel (a) of `fig-extension-panels` is rendered in light gray (`color = "#1B4F99"` at `size = 3.5` with `fontface = "italic"`). The test requires all drawn elements to have strong contrast. The color itself is dark blue, but the small size + italic face makes it appear faint against the gray grid.

**Fix in `code/generate-exhibits.R`:**
- Increase annotation `size` from 3.5 to 5.
- Change `fontface` from `"italic"` to `"bold"`.
- Ensure the annotation color is the same dark blue (`#1B4F99`) but stands out against the `gray75` grid by optionally adding a white background via `annotate("label", ...)` instead of `annotate("text", ...)`.

### 2. `writing-intro` — Flow and unfulfilled promise

**Problem (flow):** The test identifies five specific issues:
1. Para 2 front-loads too much (reads like a second abstract).
2. Abrupt transition from para 3 (incomplete markets) to para 4 (GKP/model).
3. Para 6 (veto) appears without signaling a pivot to a second contribution.
4. Para 7 near-verbatim repeats para 2's closer.
5. Meta-commentary ("product of displacement") is a tonal break before the roadmap.

**Problem (promise):** The intro says "financial market solutions are under-discussed, though frictions limit their effectiveness" — implying the paper analyzes financial hedging instruments. The body doesn't deliver this; Section 4 jumps to government transfers and the only financial-market treatment is the qualitative $\phi_\text{eff} \to 1$ argument in Section 2.3.

**Fix in `paper/paper.tex` (introduction):**
- **Para 2:** Strip the dense four-idea preview. Instead, state the paper's core claim (hedging motive) and one supporting reason (incomplete markets). Let the details emerge paragraph by paragraph.
- **Para 3 → 4 transition:** Add a bridging sentence: something like "To formalize this mechanism, we build on [GKP]..."
- **Para 6 pivot:** Open with a clear signal: "The model has a second implication for real decisions, not just prices."
- **Para 7 repetition:** Rewrite the closing paragraph so it advances the idea (e.g., highlight the policy implication) rather than echoing para 2.
- **Meta-commentary placement:** Move the AI-authorship sentence to immediately after the roadmap, or integrate it into the abstract reference so it's not a tonal break mid-argument.
- **Financial market solutions promise:** Downgrade the intro claim to match what the body delivers. Replace "financial market solutions are under-discussed, though frictions limit their effectiveness" with a more accurate framing: the paper focuses on why the ideal solution (broader trading) is infeasible and how government transfers can substitute. The financial-market point is already adequately handled in Section 2.3's discussion; the intro just oversells it.

## Priority Order

1. Fix Panel (a) annotation contrast (code change, quick).
2. Rewrite introduction for flow and promise alignment (paper change, main effort).
3. Regenerate exhibits after code fix.
4. Recompile paper after tex changes.
