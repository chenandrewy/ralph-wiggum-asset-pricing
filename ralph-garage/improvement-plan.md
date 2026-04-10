# Improvement Plan
AUTHOR PLAN — 2026-04-09 20:18:06 EDT

## Current State

22/25 tests pass. No overhaul needed — the model section is solid and passes all theory tests. The three failures are in presentation and writing.

## Failing Tests

### 1. `element-rhetoric-meta` — AI authorship device is too blunt

The meta-rhetorical device (paper about AI displacement is itself AI-written) appears in the abstract and introduction as a direct confession: "This paper was written entirely by AI agents." The test says this is too blunt and risks triggering hostile evaluation. It should be reframed as an economic observation woven into the argument, not a standalone disclosure.

**Fix:** Rewrite both occurrences (abstract final sentence, intro paragraph before lit review) to frame AI authorship as an economic data point — e.g., the production of this analysis itself required zero labor income, illustrating displacement in the production of economic research. Keep it subtle: one sentence each, same locations, but framed as evidence rather than confession.

### 2. `visual-figures` — Figure 2 legend and tick labels too small

The extension figure (fig-extension-panels) has: (a) legend text too small across both panels, (b) y-axis tick labels in Panel (a) too small, (c) cramped legend placement.

**Fix in `code/generate-exhibits.R`:**
- Increase `base_size` in `theme_paper` from 14 to 16.
- Set explicit `legend.text` size in `theme_paper` (e.g., `element_text(size = 12)`).
- Increase figure dimensions in `ggsave` for the extension figure (e.g., width 12, height 5.5) to give more room.
- Consider moving the legend inside one of the panels or adjusting `legend.position` for better spacing.

### 3. `writing-intro` — Three sub-failures in the introduction

**(a) Skimmer clarity:** Arguments (c) "financial market solutions under-discussed" and (d) "singularity abundance overcomes frictions" are buried mid-paragraph. Each needs a topic-sentence home.

**(b) Flow problems:**
- Bullet list breaks narrative momentum → convert to flowing prose.
- Paragraphs 5–6 are redundant with the bullet list → eliminate duplication by merging.
- Transition from paragraph 2 → 3 is abrupt → add a bridge.
- "Both extensions branch directly off the baseline" appears before the reader knows what they are → move or remove.
- P/D ~6× result appears too late → move earlier to anchor the hedging claim.
- Meta-sentence is a non-sequitur before lit review → integrate with surrounding text.

**(c) Unfulfilled promise:** The AI authorship claim ("all analysis and writing were produced by AI agents") has no supporting documentation. Add a brief methodological note — either a footnote or a short paragraph at the end of the conclusion — describing the division of labor (human wrote spec and tests; AI agents produced all code, analysis, and prose).

## Execution Order

1. **Introduction rewrite** (`paper/paper.tex` Section 1): Address all three `writing-intro` sub-failures and the `element-rhetoric-meta` failure simultaneously, since both involve the introduction text. Key changes:
   - Replace bullet list with flowing prose that naturally sequences the contributions.
   - Give arguments (c) and (d) from the spec their own topic sentences.
   - Move the quantitative headline result (P/D ~6×) earlier.
   - Reframe the meta-rhetorical device as economic observation in both abstract and intro.
   - Add a methodological footnote documenting the AI authorship process.
   - Smooth transitions throughout.

2. **Figure 2 formatting** (`code/generate-exhibits.R`): Fix legend size, tick label size, and figure dimensions. Regenerate exhibits.

3. **Rebuild paper and verify** — Recompile LaTeX, regenerate page images, re-run tests.
