# Improvement Plan
AUTHOR PLAN — 2026-04-10 23:07:26 EDT

## Current State

22/25 tests pass. No overhaul needed — model section is clean and correct. Three tests fail, all related to writing/formatting issues in the introduction.

## Failing Tests

### 1. `element-lit-review` + `spec-paper` (same root cause)
**Issue:** Lit review is ~20 lines (~65-75% of a page), exceeding the half-page limit (~13-15 lines). Previous iteration (rloop-16) attempted trimming but didn't cut enough.

### 2. `writing-intro`
**Issue A:** Paragraph 6's topic sentence is about redistribution as a policy lever, not about resource abundance overcoming frictions. The "abundance overcomes frictions" idea (spec argument 3d) is buried in interior sentences.
**Issue B:** The self-demonstration device (spec requirement IV.5.c) appears only in a footnote. The spec says it should be used in the abstract *and* introduction — a footnote doesn't count for skimmability.

## Plan

### Step 1: Cut the lit review to under half a page
- The third paragraph (lines 66 in tex, the "broader literature" sweep) is the longest at ~8 lines. Compress it aggressively: combine KP (2014), KPS (2020), and Knesl (2023) into a single parenthetical list with one shared sentence about creative destruction and displacement risk premia. Reduce AJJ (2019) and Acemoglu (2025) to parenthetical cites. Keep Barro/Wachter/PV as a parenthetical cluster.
- Target: 3 paragraphs totaling ~12-13 lines of rendered text (safely under half a page).
- The first two paragraphs (GKP, Jones) are important and well-written but can each lose 1-2 lines of detail.

### Step 2: Fix paragraph 6 topic sentence
- Rewrite the opening of paragraph 6 (currently "If blocking AI is costly, another policy lever is redistribution.") to lead with the abundance-overcomes-frictions idea.
- Something like: "The abundance of resources in a singularity can overcome the market frictions that make displacement catastrophic." Then pivot to redistribution as the mechanism.

### Step 3: Elevate self-demonstration device from footnote to body text
- Move the self-demonstration content from the footnote (line 57) into a brief sentence in the introduction body text — either at the end of the opening paragraph or in a short closing paragraph before the lit review.
- Keep it to one sentence. The abstract already contains the device; this ensures the intro body does too.

## Sequencing

Do Steps 1-3 in a single edit pass to the introduction. No code or exhibit changes needed. All three fixes are localized to `paper/paper.tex` lines 40-67.
