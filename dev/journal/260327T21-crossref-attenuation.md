# Anaphora resolution under semantic similarity: problem and solution
**Date:** 2026-03-27, 9:45 PM ET
**Updated:** 2026-03-27, 10:15 PM ET

## The problem

Line 425 of `paper/paper.tex` contains a cross-reference that is subtly inaccurate:

> If the singularity also accelerates growth \citep{jones2024ai}, AI owners' resources could grow large enough to make the cost of compensating the household negligible---the friction becomes self-resolving. Section~\ref{sec:scg} quantifies this attenuation.

The phrase "this attenuation" is ambiguous. In context, it refers to the **friction becoming self-resolving** — i.e., abundance making the cost of compensating the household negligible. But `sec:scg` (Section 3.4, "State-contingent growth") quantifies a **different** attenuation: the attenuation of the **hedging premium** caused by faster post-singularity growth. Specifically, sec:scg shows that when $G_H/G_L > 1$, the growth-rate term $(G_H/G_L)^{1-\gamma}$ shrinks the singularity factor, causing the hedging premium to drop (e.g., only 12% survives at $G_H/G_L = 1.25$).

These are related but distinct phenomena:
- **What sec:scg quantifies:** the hedging premium attenuates because faster growth raises household consumption in the singularity state, lowering marginal utility and thus lowering the pricing premium on AI stocks.
- **What the paragraph claims sec:scg quantifies:** the friction (incomplete markets preventing trade) self-resolves because abundance makes the cost of compensating the household negligible.

The first is a pricing/SDF effect. The second is a political economy / market structure claim about frictions dissolving. Sec:scg never addresses whether frictions self-resolve — it takes the market structure as given and shows how growth acceleration shrinks the premium within that structure.

## Attempted solutions

We tried to catch this with automated tests. Three approaches were attempted:

1. **`factcheck-bysection.py`** — the existing section-by-section factcheck. It checks cross-references as part of its REFERENCE claim type, but marked line 425 as OK. The agent saw "attenuation" in both the reference site and the target and concluded they matched.

2. **`factcheck-crossref.py`** — a dedicated cross-reference test designed specifically for this class of problem. The prompt instructs the agent to (a) extract the specific claim the prose makes about the target, (b) read the target, and (c) compare. The agent still marked line 425 as OK, again conflating the two senses of "attenuation."

3. **Considered but rejected: anaphora resolution prompt.** We discussed adding a prompt step requiring the agent to "resolve every pronoun and demonstrative ('this', 'that', 'these') to its concrete antecedent before comparing with the target." This was rejected as fragile and likely to produce false positives.

## Why this is hard to catch

The core difficulty is **anaphora resolution under semantic similarity**. The word "attenuation" appears in both the reference site and the target, but refers to different economic mechanisms. The agent needs to:

1. Resolve "this attenuation" to its antecedent: "the friction becomes self-resolving"
2. Read sec:scg and understand it quantifies hedging premium attenuation, not friction resolution
3. Recognize these are distinct claims despite sharing the word "attenuation"

Step 1 is the bottleneck. General-purpose prompts consistently fail here because the surface-level match is strong enough to satisfy the check.

## Outcome of initial attempts

Deleted `factcheck-crossref.py` as redundant — it catches the same issues `factcheck-bysection` already catches and fails on the same subtle issue. Accepted the limitation for now.

## The class of problem

This is an **anaphora resolution problem under semantic similarity**. The defining characteristics:

1. A demonstrative phrase ("this attenuation") appears near a cross-reference.
2. The demonstrative resolves to one meaning based on local context (friction self-resolving).
3. The cross-reference target contains a *different* mechanism that shares the same vocabulary (hedging premium attenuating).
4. Because the vocabulary matches, a reader — or an LLM agent — can satisfy the cross-reference check without noticing that the resolved antecedent and the target describe different things.

The semantic similarity is what makes it hard. If the target section discussed something obviously unrelated (say, calibration methodology), any reasonable check would catch it. The failure mode is specifically when the target *is* related and *does* use the same word, but for a different mechanism.

In this case:
- **Local antecedent of "this attenuation":** the friction (incomplete markets) becomes self-resolving because abundance makes compensation costs negligible. This is a claim about market structure dissolving.
- **What sec:scg actually quantifies:** the hedging premium attenuates because faster post-singularity growth raises household consumption, lowering marginal utility. The friction *persists* — sec:scg explicitly says "despite the distributional shift" (line 323). The market structure is held fixed; only the pricing effect changes.

Same word ("attenuation"), related economic context (both involve post-singularity growth), but fundamentally different mechanisms (market structure dissolving vs. pricing premium shrinking within a fixed market structure).

## Solution

A simple, direct prompt asking the agent to check for anaphora resolution problems caught the issue on the first try:

> Read lines 371-471 of paper/paper.tex. Check for anaphora resolution problems: any place where a demonstrative ("this", "that", "these", "such") near a cross-reference could resolve to a different meaning than what the referenced target actually contains. Report any cases where the prose and the target describe different mechanisms despite sharing vocabulary.

The agent correctly identified the line 425 problem:

> "this attenuation" resolves to "the friction goes away" in the local paragraph, but the target section shows "the premium shrinks while the friction remains." Same word ("attenuation"), different mechanisms.

### Why this prompt works when the others didn't

The earlier prompts (`factcheck-bysection`, `factcheck-crossref`) asked the agent to verify cross-references as one task among many. The agent would read the reference site and the target together, see "attenuation" in both places, and move on. The anaphora resolution prompt works because it:

1. **Names the specific failure mode** — "anaphora resolution" — which primes the agent to treat demonstratives as objects requiring explicit resolution rather than transparent pointers.
2. **Describes the error pattern** — "could resolve to a different meaning than what the referenced target actually contains" — which tells the agent what to look for rather than just asking "is this reference correct?"
3. **Warns about the trap** — "different mechanisms despite sharing vocabulary" — which directly counteracts the surface-level vocabulary match that fooled the other prompts.

### Next step

Build this into a proper test in `tests/`.
