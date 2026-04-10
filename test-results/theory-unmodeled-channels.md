# tests/theory-unmodeled-channels.py
Started: 2026-04-09 21:34:52 EDT
Runtime: 1m 46s
[ralph-garage/agent-logs/20260409T213452.268667-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T213452.268667-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently uses cautious language about channels it does not explicitly model, clearly disclaiming unmodeled mechanisms and framing its contribution modestly.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging channel**: AI stocks hedge displacement risk via higher dividends in singularity states. Core mechanism with closed-form P/D ratios.
2. **Displacement via singularity**: Consumption share shifts from household to AI owners (parameter φ). Fully specified.
3. **Extinction risk**: Probability ξ of total loss conditional on singularity. Modeled following Jones (2024).
4. **Market incompleteness**: Household cannot trade restricted AI equity. Modeled as the source of the valuation premium.
5. **Veto / blocking AI development** (Extension 1): Household can block AI at a cost. Modeled with positive and negative singularity outcomes.
6. **Government transfers with deadweight costs** (Extension 2): Tax-and-transfer with quadratic waste. Fully specified with effective displacement parameter φ_eff.

### Discussed but NOT Explicitly Modeled
7. **Entry of new cohorts / creative destruction** (GKP mechanism): AI owners are analogized to future entrants, but the paper does not model entry dynamics.
8. **Labor market mechanisms**: Displacement is via consumption shares, not an explicit labor market model.
9. **Financial market frictions**: Illiquidity, restricted ownership, and non-existence of future capital are mentioned as motivations but not modeled as separate frictions.
10. **Continuous-time dynamics, heterogeneous beliefs, production-side details**: Listed in the conclusion as abstractions.

## Caution Assessment

The paper is consistently cautious about every unmodeled channel:

- **Entry dynamics (GKP)**: Two explicit disclaimers. Line 77: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 174: "though we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."
- **Overall scope**: The conclusion (line 270) explicitly lists what is abstracted away: "It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis."
- **Purpose framing**: Line 271: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Hedging language throughout**: The paper uses "in part" (abstract), "Part of this premium" (line 49), "may partly reflect" (lines 55, 220), and "suggests" (line 261) when connecting model results to real-world phenomena.
- **Policy nuance**: Line 261: "The policy implication is nuanced." Transfers are described as "may be worth designing" rather than as a definitive recommendation.
- **AI regulation connection**: Framed as "may partly reflect investors' inability to share in the upside" — appropriately speculative.
- **Approximation transparency**: The closed-form P/D derivation explicitly acknowledges its stationarity approximation (line 149) and states when it is exact vs. approximate.

No instance was found where the paper makes strong claims about a channel it does not explicitly model.
