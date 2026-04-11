# tests/theory-unmodeled-channels.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 1m 8s
[ralph-garage/agent-logs/20260411T103039.152104-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.152104-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, flagging each limitation clearly and avoiding overclaiming.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging motive / displacement risk**: Core mechanism. Household consumption share drops by factor phi upon singularity.
2. **Market incompleteness**: Household cannot trade restricted AI equity (founder stakes, pre-IPO shares). Drives the valuation premium.
3. **Extinction risk**: With probability xi, singularity triggers extinction. Attenuates the hedging premium.
4. **Veto / blocking AI development** (Extension 1): Household can block AI at cost kappa. Incomplete markets cause inefficient vetoes.
5. **Government transfers** (Extension 2): Tax rate tau with quadratic deadweight costs. Explosive growth can overwhelm waste.
6. **Positive singularity** (Extension 1): With probability q, household share increases rather than decreases.

### Discussed but Not Explicitly Modeled
1. **Entry of new cohorts / creative destruction (GKP channel)**: The paper's AI owners play an analogous role to GKP's future innovators but are a static group.
2. **Continuous displacement**: GKP models gradual displacement from expanding technological variety; this paper models a discrete singularity instead.
3. **Continuous-time dynamics**: Acknowledged as absent in the conclusion.
4. **Heterogeneous beliefs**: Acknowledged as absent in the conclusion.
5. **Production-side details**: Acknowledged as absent in the conclusion.
6. **Wealth heterogeneity and differential AI attitudes**: Discussed in connection with Jones (2024) as a "complementary channel" but not formally derived.
7. **Broader trading of AI capital**: Discussed as the ideal but infeasible solution due to non-existent future capital.

## Cautiousness Assessment

The paper handles unmodeled channels with consistent care:

- **Entry dynamics (GKP)**: Flagged explicitly twice. Line 77: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 178: "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."

- **Conclusion disclaimer**: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

- **Empirical hedging**: The NASDAQ/S&P comparison is explicitly called "imperfect" with three specific caveats (NASDAQ broader than AI stocks, return vs. valuation differences, S&P has AI exposure). Magnitudes are described as "broadly suggestive" rather than as evidence.

- **Closed-form approximation**: Transparently noted as exact only when Delta-theta approaches zero, with numerically exact values reported separately.

- **GKP attribution**: Contribution is characterized modestly throughout. Key displacement/incomplete-markets insights are credited to GKP. The paper says it "builds on" and "parallels" GKP rather than claiming novelty.

- **Policy implications**: Described as "nuanced" with explicit caveat that transfers are "blunt and wasteful" in normal times.

- **Jones (2024) wealth channel**: Presented as a "complementary channel" rather than something the model derives.

No instance was found where the paper claims a result or insight from an unmodeled channel without appropriate hedging.
