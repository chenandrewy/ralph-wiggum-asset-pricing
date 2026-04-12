# Improvement Plan
AUTHOR PLAN — 2026-04-11 21:24:19 EDT

## Current Status

- **Tests**: 24/25 pass. One failure: `writing-intro`.
- **Model section**: Sound. No overhaul needed.
- **Code**: Clean, single entry point, all exhibits generated correctly.
- **Referee report**: Addressed via Extensions (veto + transfers).

## Key Issue: `writing-intro` Failure

The introduction's first three paragraphs are strong (vivid opening, clear mechanism, natural formalization). Paragraphs 4-7 lose coherence with abrupt transitions and disconnected summaries.

Specific problems identified by the test:

| Location | Problem |
|---|---|
| P3 -> P4 | Extinction channel appears without preparation |
| P4 -> P5 | Abrupt pivot from extinction to development distortions |
| P6 | Generic "frictions are severe" paragraph reads as filler |
| P6 -> P7 | "But if..." conjunction is jarring for introducing a new mechanism |
| P7 -> Roadmap | Jones/redistribution result orphaned before roadmap |

## Plan

### Step 1: Restructure introduction paragraphs 4-7

Goal: Make the second half of the introduction flow as naturally as the first half.

Changes to `paper/paper.tex`, introduction section only:

1. **Fold extinction into P3 (the model results paragraph).** The extinction attenuation is a model result, not a separate idea. Add one sentence at the end of P3 noting that extinction risk attenuates the premium (Prop 2), rather than giving it a standalone paragraph.

2. **Merge current P4 (incomplete markets as key driver) with the extinction content.** After folding extinction into P3, repurpose the incomplete-markets framing as a bridge sentence: "Market incompleteness is the key driver---and its consequences extend beyond valuations."

3. **Combine P5 (development distortions) and P6 (frictions) into one paragraph on extensions.** The current P6 is filler. Instead, write a single paragraph that (a) introduces market incompleteness distorting AI development (veto), (b) notes the natural fix is blocked by restricted ownership, and (c) pivots to government transfers as the alternative. This creates a clean narrative: incompleteness -> veto -> transfers.

4. **Integrate the Jones/singularity-growth result into the extensions paragraph** rather than orphaning it in its own paragraph before the roadmap. The key insight (explosive growth overwhelms deadweight costs) belongs with the transfer discussion.

5. **End with the roadmap paragraph**, which currently works fine and just needs the preceding material to flow into it.

Target structure after revision:
- P1: AI stocks are highly valued (Figure 1)
- P2: Hedging motive mechanism
- P3: Model formalization + quantitative results + extinction attenuation
- P4: Incomplete markets as key driver; consequences beyond valuations
- P5: Extensions — veto distortion, government transfers, singularity growth enabling redistribution
- P6: Summary + roadmap + footnote

### Step 2: Precision fix on "roughly twice" language

The test flagged that "roughly twice...across plausible singularity probabilities" slightly overstates breadth (2x at p=1%, ~1.4x at p=0.5%). Tighten the language in P3 to be more precise about where the 2x ratio holds.

### Step 3: Recompile and verify

- Recompile `paper.tex` to PDF
- Regenerate page images
- Re-run `writing-intro` test to confirm fix
