# tests/theory-unmodeled-channels.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 57s
[ralph-garage/agent-logs/20260409T212047.313253-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.313253-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently hedges claims about channels it does not explicitly model and clearly flags modeling boundaries.

## Channels Identified

### Explicitly Modeled
1. **Hedging channel** — AI stocks hedge displacement risk via the household's SDF. Core mechanism with closed-form P/D ratios (Proposition 1).
2. **Displacement / singularity** — Modeled via parameter $\phi$ governing how the household's consumption share drops upon singularity.
3. **Market incompleteness** — Household cannot trade restricted AI equity. Modeled as a constraint on tradeable assets.
4. **Extinction risk** — Modeled via probability $\xi$, following Jones (2024). Integrated into pricing formulas.
5. **Veto / blocking AI development** — Extension 1 explicitly models the household's option to block AI at a cost.
6. **Government transfers with deadweight costs** — Extension 2 models tax-and-transfer with waste parameter $\delta$.

### Discussed but Not Explicitly Modeled
7. **Entry of new cohorts / creative destruction (GKP 2012)** — AI owners serve as analogue to GKP's future innovators, but entry dynamics are not modeled.
8. **Financial market frictions (illiquidity, restricted ownership, non-existence of future capital)** — Listed as sources of incompleteness but collapsed into a single trading restriction.
9. **Continuous-time dynamics** — Acknowledged as absent in the conclusion.
10. **Heterogeneous beliefs** — Acknowledged as absent in the conclusion.
11. **Production-side details** — Acknowledged as absent in the conclusion.
12. **Technology policy and labor market channels** — Mentioned as dominant in public discourse but not modeled; the paper focuses on financial markets instead.

## Cautiousness Assessment

### Entry dynamics (GKP) — Cautious
The paper is particularly careful here, flagging the boundary twice:
- Section 2.1 (line 77): "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism."
- Section 2.3 (line 172): "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."

### Financial market frictions — Cautious
Line 49: "Financial markets could in principle provide hedging instruments, but frictions---illiquidity, restricted ownership, the non-existence of future capital---limit their effectiveness." Lists specific frictions without claiming to model each one individually.

### Hedging claim — Cautious
Line 49: "Part of this premium, we argue, reflects a hedging motive." Uses "part of" to avoid overclaiming.

### Policy implications — Cautious
- Line 253: "The policy implication is nuanced."
- Lines 55-56 and 218: "calls to slow or halt AI development may partly reflect" — uses "may partly."

### Scope limitations — Cautious
Conclusion (line 262): "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

### Quantitative claims — Cautious
Line 190: "The magnitudes are broadly consistent with observed valuation spreads." Uses "broadly consistent" rather than asserting a precise match.

## Summary
Every channel that is discussed but not explicitly modeled is flagged as such. The paper uses appropriately hedged language ("part of," "may partly," "broadly consistent," "deliberately simple") and does not overclaim what its model delivers. The treatment of GKP's entry dynamics is especially careful, with two explicit disclaimers.
