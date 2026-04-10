# Improvement Plan
AUTHOR PLAN — 2026-04-09 21:17:29 EDT

## Status: 21/25 tests passing. 4 failing.

## Failing Tests

### 1. factcheck-theory (CRITICAL — model section)
**Issue:** Dividend definitions A7–A8 set $D^{AI} + D^{N} = C_t$, exhausting aggregate consumption through public stocks. A9 then claims private AI capital pays "the residual accruing to AI owners beyond the public AI dividend" — but that residual is zero. This is an accounting inconsistency.

**Impact on math:** None. Private capital never enters pricing equations. Fix is purely narrative.

**Fix:** Reframe private AI capital as *restricted shares of the AI stock* that the household cannot purchase (founder stakes, pre-IPO equity, etc.), not as a separate dividend stream. Delete the "residual" language. The incomplete-markets friction becomes: the household can only trade a portion of AI equity, not all of it. Alternatively, clarify that the household's consumption share $\alpha_t$ is determined by its portfolio, and AI owners receive $(1-\alpha_t)C_t$ from their combined public and private holdings — but do not claim private capital pays dividends on top of the public dividend structure.

**Where:** `paper.tex` lines 103–111 (Assets paragraph, especially the private AI capital sentence).

### 2. factcheck-freely
**Issue:** Bib entry `KoganPapanikolaouStoffman2020` omits Amit Seru as co-author. The 2020 JPE paper has four authors: Kogan, Papanikolaou, Seru, and Stoffman.

**Fix:**
- `paper/references.bib`: Add "Seru, Amit" to author list, rename key to `KoganPapanikolaouSeruStoffman2020`.
- `paper/paper.tex` line 68: Update `\citet` to new key.

### 3. visual-figures-image-only (figure formatting)
**Issues:**
- **fig-ai-valuations:** (a) Y-axis label clipped — closing parenthesis cut off. (b) Grid lines too light.
- **fig-extension-panels:** (a) Panel A y-axis range 5–25 wastes space (data spans ~9–18); tighten to ~7–20. (b) Panel B: "No change" reference line at y=1 blends with grid; make it darker/thicker.

**Fix in `code/generate-exhibits.R`:**
- fig-ai-valuations: Add `plot.margin` to prevent label clipping. Grid lines already use `gray50`; verify after regeneration.
- Panel A: Change `y_min_a`/`y_cap_a` calculation to tighten y-axis (~7–20).
- Panel B: Darken reference line (already `gray20` + linewidth 1.0 — may need `"black"` + linewidth 1.2).

### 4. writing-intro (introduction flow)
**Issues:**
- Spec argument (c) — financial market solutions being under-discussed — not visible on skimming surface.
- Broken transition P4→P5 (quantitative results → veto): P4 ends on extinction, P5 jumps to real distortions.
- Broken transition P6→P7 (transfers → self-demonstration): jarring conceptual leap.

**Fix in `paper.tex` introduction:**
- Add a sentence near the start of the framework paragraph (P3 area) explicitly flagging that financial-market hedging solutions are under-studied.
- Add a bridge sentence at the end of P4 or start of P5 connecting extinction risk to broader distortions from incomplete markets.
- Add a bridge sentence between P6 and P7 linking the policy discussion to the broader question of what AI displaces — including the research process itself.

## Execution Order

1. Fix bib entry (factcheck-freely) — trivial, do first.
2. Fix model narrative for private AI capital (factcheck-theory) — careful rewrite of one paragraph.
3. Fix figures (visual-figures-image-only) — code changes + regenerate.
4. Fix introduction flow (writing-intro) — paragraph-level edits.
5. Recompile paper and verify.
