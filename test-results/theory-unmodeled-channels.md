# tests/theory-unmodeled-channels.py
Started: 2026-04-09 19:33:01 EDT
Runtime: 1m 15s
[ralph-garage/agent-logs/20260409T193302.024585-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T193302.024585-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently uses cautious language and explicit disclaimers for channels it does not formally model.

## Channels and Modeling Status

| Channel | Modeled? | Discussion |
|---------|----------|------------|
| Hedging/displacement via singularity | Yes | Core model: consumption share displacement (φ), P/D ratios |
| Market incompleteness (private AI capital) | Yes | Household cannot trade private AI capital |
| Extinction risk | Yes | Probability ξ conditional on singularity |
| Positive singularity | Yes | Extension 1: probability λ of positive outcome |
| Veto / blocking AI development | Yes | Extension 1: household can block at cost κ |
| Government transfers with deadweight costs | Yes | Extension 2: tax rate τ with waste parameter δ₀ |
| Entry of new cohorts / creative destruction (GKP) | No | Clearly disclaimed at lines 80 and 183 |
| Labor income channel | No | Intro mentions "labor income" (line 51) but model uses consumption shares; reasonable interpretation |
| Continuous-time dynamics | No | Acknowledged in conclusion (line 286) |
| Heterogeneous beliefs | No | Acknowledged in conclusion (line 286) |
| Production-side details | No | Acknowledged in conclusion (line 286) |
| AI regulation implications | No | Discussed with cautious "may partly reflect" (line 244) |
| Contingent transfer policy design | No | Suggested with hedged "suggests" and "may be worth" (line 277) |

## Assessment

The paper handles unmodeled channels well:

1. **GKP entry dynamics**: Disclaimed twice. Line 80: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 183: "we do not model the entry dynamics that are central to their framework."

2. **Scope limitations**: The conclusion (line 286) explicitly states: "It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis."

3. **Hedging language throughout**: The paper uses "part of this premium" (line 50), "may partly reflect" (line 244), "suggests" and "may be worth" (line 277) when discussing implications beyond the model.

4. **Model described as deliberately simple**: Line 286: "Our model is deliberately simple." Line 286-287: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

No instances found where the paper overstates or makes unqualified claims about channels it does not formally capture.
