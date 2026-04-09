# tests/theory-unmodeled-channels.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 47s
[ralph-garage/agent-logs/20260409T184838.245668-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T184838.245668-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, using clear disclaimers, hedging language, and explicit acknowledgment of abstractions.

## Channels and Modeling Status

### Explicitly Modeled Channels
1. **Hedging/displacement channel** (baseline model) -- AI stocks hedge against singularity-driven displacement of household consumption share. Core mechanism with closed-form P/D ratios.
2. **Market incompleteness** (baseline model) -- Household cannot trade private AI capital; this is the source of the valuation premium.
3. **Extinction risk** (baseline model) -- Singularity may trigger extinction following Jones (2024). Modeled as probability $\xi$.
4. **Positive singularity and veto** (Extension 1) -- Household may block socially efficient AI development under incomplete markets due to risk aversion.
5. **Government transfers with deadweight costs** (Extension 2) -- Tax on AI owners' income with wasteful redistribution; becomes effective when singularity growth overwhelms costs.

### Discussed but Not Modeled Channels
6. **Entry dynamics / creative destruction** (GKP 2012) -- New cohorts of firms entering the economy. Paper explicitly disclaims modeling this.
7. **Continuous-time dynamics** -- Acknowledged as abstracted away in the conclusion.
8. **Heterogeneous beliefs** -- Acknowledged as abstracted away in the conclusion.
9. **Production-side details** -- Acknowledged as abstracted away in the conclusion.
10. **Cross-sectional displacement risk factor** (Kogan & Papanikolaou 2014) -- Referenced in lit review only.
11. **Creative destruction and inequality** (Kogan, Papanikolaou, Stoffman 2020) -- Referenced in lit review only.
12. **Technological revolutions and uncertainty** (Pastor & Veronesi 2009) -- Referenced in lit review only.
13. **Task automation vs. aggregate productivity** (Acemoglu 2024) -- Referenced as a skeptical counterpoint.

## Assessment of Caution

The paper demonstrates consistent caution about unmodeled channels through several devices:

1. **Explicit disclaimers about entry dynamics**: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1). Reinforced in Section 2.3: "we do not model the entry dynamics that are central to their framework."

2. **Hedging language about the main claim**: "Part of this premium, we argue, reflects a hedging motive" (Introduction) -- uses "part of," not claiming to be the whole explanation.

3. **Cautious quantitative language**: "The magnitudes are broadly consistent with observed valuation spreads" (Section 3) -- avoids claiming precise calibration.

4. **Cautious policy language**: "calls to slow or halt AI development may partly reflect the inability of most investors to share in the upside" (Section 4.1) -- "may partly" is appropriately hedged.

5. **Explicit scope acknowledgment in conclusion**: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

6. **Modest framing of contribution relative to GKP**: The paper consistently positions itself as connecting GKP's existing insights to AI, not as originating the displacement/incompleteness logic.

No instances were found where the paper makes strong claims about channels it does not model.
