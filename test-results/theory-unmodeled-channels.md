# tests/theory-unmodeled-channels.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 59s
[ralph-garage/agent-logs/20260411T100208.985805-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260411T100208.985805-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently uses cautious language for channels it does not explicitly model, and explicitly flags its modeling boundaries.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging/displacement channel** — AI stocks hedge consumption displacement via the singularity mechanism. Fully modeled: CRRA preferences, SDF, closed-form P/D ratios (Proposition 1).
2. **Extinction risk** — Singularity can cause extinction, attenuating valuations. Modeled with probability ξ (Proposition 2(iii)).
3. **Market incompleteness** — Household cannot trade restricted AI equity. Modeled: household trades only public AI and non-AI stocks; displacement parameter φ captures non-tradeable component.
4. **Veto/development distortion** — Household can block AI development under incomplete markets. Modeled in Extension 1 with positive/negative singularity probabilities, veto cost κ (Proposition 3).
5. **Government transfers** — Tax on AI owners' surplus with deadweight costs. Modeled in Extension 2 with tax rate τ and waste parameter δ.

### Discussed but NOT Explicitly Modeled
1. **Entry dynamics / new cohorts of firms** — GKP (2012)'s OLG structure where displacement comes from new entrants.
2. **Heterogeneous beliefs** — Mentioned in conclusion as abstracted away.
3. **Continuous-time dynamics** — Mentioned in conclusion as abstracted away.
4. **Production-side details** — Mentioned in conclusion as abstracted away.
5. **Earnings growth vs. valuation multiples** — Relevant to empirical comparison but not modeled separately.
6. **Wealth heterogeneity and differential attitudes toward AI risk** — Discussed in connection to Jones (2024); partially captured through α but not fully modeled with heterogeneous agents.

## Assessment of Caution

The paper is consistently cautious about unmodeled channels:

- **Entry dynamics**: Explicitly flagged twice. Line 79: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 180: "though we do not model the entry dynamics that are central to their framework."
- **Scope limitations**: The conclusion (line 294) explicitly states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis."
- **Empirical claims**: Line 200 hedges the NASDAQ comparison: "This comparison is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure."
- **Policy claims**: Uses cautious language throughout. Line 57: "calls to slow or halt AI development **may partly** reflect investors' inability to share in its upside." Line 285: "This **suggests** that contingent transfer policies...may be worth designing in advance."
- **Overall framing**: Line 294-295: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **GKP relationship**: The paper is modest about its contribution relative to GKP, noting that "the main insights about displacement risk and incomplete markets are already in GKP" (per the spec, and reflected in the paper's framing throughout Section 2.3).

No instance was found where the paper makes strong claims about a channel it does not explicitly model.
