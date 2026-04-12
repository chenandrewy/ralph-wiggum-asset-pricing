# Improvement Plan
AUTHOR PLAN — 2026-04-11 21:14:22 EDT

## Current State

- **Tests:** 24/25 pass. One failure: `writing-intro`.
- **Model section:** All theory tests pass (clarity, deadweight, factcheck-theory, unmodeled-channels). No overhaul needed.
- **Code:** Runs cleanly, all exhibits verified, parameters match paper.
- **Referee concerns (CFR-R1):** Addressed—GKP relationship is handled modestly, Jones extinction channel incorporated, extensions on veto and transfers differentiate the paper.

## Failing Test: `writing-intro`

**Issue:** Argument (d) from the spec—"if the singularity occurs, then market frictions can be overcome due to the abundance of resources"—is buried in the body of paragraph 6 of the introduction. A skimming reader who reads only first sentences would miss it. The first sentence of paragraph 6 leads with the severity of frictions, which signals the opposite.

**Fix:** Restructure the introduction's paragraph 6 (the one beginning "Financial market solutions to AI displacement risk are under-discussed...") so the resource-abundance mechanism is prominent in the opening sentence. The simplest approach:

1. Split paragraph 6 into two paragraphs:
   - **Para 6a** (keep current opening): "Financial market solutions to AI displacement risk are under-discussed, and the frictions that limit them are severe..." — covers the under-discussed point and the nature of the friction.
   - **Para 6b** (new paragraph, new opening sentence): Lead with the resource-abundance insight: something like "But if the singularity produces explosive output growth, even grossly inefficient government transfers become effective because the resource base overwhelms deadweight costs." Then continue with the Jones citation and the closing sentence about the same explosive growth providing the means to overcome the problem.

2. This split also addresses the secondary note from the test that the Para 6 → Para 7 (roadmap) transition is slightly abrupt: the new Para 6b ends on the resource-abundance point, which connects naturally to the roadmap's third linked result (redistribution).

## No Other Changes Needed

All other tests pass. The model, extensions, figures, code, and factual content are verified. No overhaul required. Focus this iteration entirely on the introduction paragraph restructuring.
