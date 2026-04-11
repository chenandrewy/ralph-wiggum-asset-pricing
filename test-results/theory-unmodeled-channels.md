# tests/theory-unmodeled-channels.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 1m 9s
[ralph-garage/agent-logs/20260410T225642.487906-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260410T225642.487906-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, using hedging language and explicit disclaimers throughout.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging motive / displacement risk under incomplete markets** — Core model. Household share drops by φ upon singularity; AI stocks provide partial hedge.
2. **Extinction risk** — Parameter ξ in the singularity structure, following Jones (2024).
3. **Veto / blocking AI development** — Extension 1. Household can block singularity at a cost.
4. **Positive singularity** — Extension 1. Household share can increase.
5. **Government transfers with deadweight costs** — Extension 2. Tax rate τ with waste fraction δτ.

### Discussed but Not Modeled
6. **Entry of new cohorts / creative destruction (GKP-style)** — The paper draws an analogy to GKP's framework where displacement comes from new entrants.
7. **Financial market hedging instruments** — Mentioned as limited by frictions (illiquidity, restricted ownership, non-existence of future capital).
8. **Wealth heterogeneity and AI attitudes** — Discussed as a "complementary channel" to Jones (2024)'s existential-risk channel.
9. **Heterogeneous beliefs** — Listed as an abstraction in the conclusion.
10. **Production-side details** — Listed as an abstraction in the conclusion.
11. **Continuous-time dynamics** — Listed as an abstraction in the conclusion.
12. **AI regulation** — Qualitative interpretation of the veto result.
13. **Intergenerational bequests (GKP)** — Referenced as GKP's result, not claimed as modeled.

## Assessment of Cautiousness

The paper is consistently cautious about every unmodeled channel:

- **GKP entry dynamics** (the most important unmodeled channel): Explicitly disclaimed twice. Line 75: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 174: "though we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."

- **Scope limitations**: The conclusion (line 274) explicitly states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis."

- **Purpose framing**: The conclusion hedges the paper's ambition: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

- **Hedging language throughout**: The main argument uses "in part" (line 49: "Part of this premium, we argue"). Quantitative comparisons are "broadly suggestive" and "imperfect" (line 192). Policy implications are "nuanced" (line 265). Regulatory connections use "may partly reflect" (line 222).

- **Wealth heterogeneity discussion**: When connecting to Jones (2024)'s observation about wealth and risk attitudes, the paper frames its contribution as "a complementary channel" rather than claiming to model wealth heterogeneity directly. The claims stay within the model's scope (different consumption shares α affect veto incentives).

- **GKP transfers**: When discussing GKP's bequest result, the paper attributes the insight to GKP ("observing that...") rather than claiming to replicate it.

No instance was found where the paper makes strong claims about a channel it does not explicitly capture.
