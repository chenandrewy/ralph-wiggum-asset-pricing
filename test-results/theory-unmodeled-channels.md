# tests/theory-unmodeled-channels.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 52s
[ralph-garage/agent-logs/20260409T205235.720571-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T205235.720571-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently flags unmodeled channels with explicit disclaimers and hedged language, never claiming more than its formal apparatus delivers.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging/displacement channel** — Core mechanism. Household's consumption share drops upon singularity; AI stocks pay off in those states.
2. **Market incompleteness** — Household cannot trade private AI capital. Central assumption driving all results.
3. **Extinction risk** — Parameter ξ; follows Jones (2024). Modeled as probability of zero consumption.
4. **Veto / blocking AI development** — Extension 1. Household can block socially efficient AI at a cost.
5. **Government transfers with deadweight costs** — Extension 2. Tax on AI surplus with quadratic waste.
6. **Positive singularity** — Extension 1. Household share can increase.

### Discussed but Not Explicitly Modeled
7. **Entry of new cohorts / creative destruction (GKP mechanism)** — The paper draws an analogy between AI owners and GKP's future innovators but explicitly disclaims the entry dynamics: "we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group" (Section 2.1) and "we do not model the entry dynamics that are central to their framework" (Section 2.3).
8. **Labor market mechanisms** — Displacement is captured through consumption shares (α), not through a labor market. The paper does not claim to model labor markets.
9. **AI regulation / technology policy** — The veto mechanism is modeled, but broader regulatory debates are discussed only as an implication, hedged with "may partly reflect" (Section 4.1).
10. **AI displacing knowledge production** — The self-referential device (AI wrote the paper) is framed as "a small-scale illustration" and "a concrete, if modest, instance" — not as a modeled channel.
11. **Continuous-time dynamics, heterogeneous beliefs, production-side details** — The conclusion explicitly lists these as abstractions: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features."

## Assessment of Caution

The paper is consistently cautious about unmodeled channels:

- **GKP entry dynamics**: Two separate, clear disclaimers (Sections 2.1 and 2.3) prevent the reader from thinking entry is modeled. This directly satisfies the spec requirement (I.4.d).
- **Scope of claims**: The conclusion states "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel" (Section 5).
- **Hedged language throughout**: "Part of this premium, we argue" (Introduction); "may partly reflect" (Section 4.1); "nuanced" (Section 4.2 policy discussion).
- **GKP citations**: Contribution is characterized modestly — "We build on their framework" and "inherits their central economic logic" (lit review).
- **Quantitative claims**: Framed as illustrative ("broadly consistent with observed valuation spreads") rather than as calibration or estimation.

No instance was found where the paper discusses an unmodeled channel without appropriate caution.
