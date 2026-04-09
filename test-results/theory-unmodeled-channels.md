# tests/theory-unmodeled-channels.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 54s
[ralph-garage/agent-logs/20260409T190308.201960-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T190308.201960-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently flags unmodeled channels with explicit caveats and hedging language, never overclaiming about mechanisms it does not formally capture.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging motive / displacement risk** — Core model: parameter φ governs displacement severity, household uses AI stocks as partial hedge.
2. **Market incompleteness** — Household cannot trade private AI capital; this is the source of the valuation spread.
3. **Extinction risk** — Parameter ξ; follows Jones (2024).
4. **Positive singularity and veto** — Extension 1: household can block socially efficient AI development under incomplete markets.
5. **Government transfers with deadweight costs** — Extension 2: tax-and-transfer with waste parameter δ₀.

### Discussed but Not Modeled
6. **Entry dynamics / overlapping generations (GKP)** — AI owners are analogized to future entrants, but the paper does NOT model entry.
7. **Continuous-time dynamics** — Acknowledged as omitted in the conclusion.
8. **Heterogeneous beliefs** — Acknowledged as omitted in the conclusion.
9. **Production-side details** — Acknowledged as omitted in the conclusion.
10. **Technology uncertainty / technological revolutions** (Pastor & Veronesi) — Referenced in lit review only.
11. **Creative destruction and inequality** (Kogan et al.) — Referenced in lit review only.
12. **AGI transition dynamics** (Korinek & Suh) — Referenced in lit review only.

## Assessment of Caution

The paper is consistently cautious about every unmodeled channel:

- **GKP entry dynamics** (the most critical unmodeled channel): Explicitly flagged twice. Line 77: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 172: "though we do not model the entry dynamics that are central to their framework."
- **Scope limitations**: The conclusion (line 273) explicitly lists omissions: "It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis."
- **Hedging language throughout**: The paper uses "part of this premium" (line 49), "may partly reflect" (line 233), "suggests" and "may be worth" (line 264), avoiding overclaiming.
- **Modest framing**: Line 273–274: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Lit review channels**: Papers cited in the literature review are positioned as related work, not as channels the model captures.

No instance was found where the paper claims to capture a mechanism it does not formally model.
