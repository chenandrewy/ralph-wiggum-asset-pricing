# tests/theory-unmodeled-channels.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 1m 7s
[ralph-garage/agent-logs/20260409T220435.846099-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T220435.846099-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently uses cautious, hedged language when discussing economic channels it does not explicitly model.

## Channels Identified

### Explicitly Modeled
1. **Hedging channel**: Core mechanism; AI stocks hedge displacement risk via SDF pricing (Proposition 1).
2. **Market incompleteness**: Household cannot trade restricted AI equity; source of valuation premium.
3. **Displacement / consumption reallocation**: Parameter φ governs household share loss upon singularity.
4. **Extinction risk**: Probability ξ attenuates hedging premium (Proposition 2(iii)).
5. **Veto of AI development** (Extension 1): Household blocks socially efficient AI under incomplete markets.
6. **Government transfers with deadweight costs** (Extension 2): Tax τ on AI owners with waste parameter δ.

### Discussed but NOT Explicitly Modeled
7. **Entry dynamics / creative destruction (GKP 2012)**: AI owners are described as analogous to future entrants, but the paper does not model entry.
8. **Financial market hedging instruments**: Mentioned as limited by frictions (illiquidity, restricted ownership, non-existence of future capital), but no formal instrument pricing.
9. **Continuous-time dynamics, heterogeneous beliefs, production-side details**: Listed in conclusion as abstractions.
10. **Labor market effects**: Mentioned as context ("discussions of AI risk focus overwhelmingly on technology policy and labor markets") but not modeled.
11. **AI regulation debates**: Connected to the veto mechanism but not modeled as a policy game.

## Assessment of Cautiousness

The paper is consistently cautious about channels it does not capture:

- **Entry dynamics**: Disclaimed explicitly twice. Line 75: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group." Line 172: "we do not model the entry dynamics that are central to their framework."
- **Hedging claim**: Hedged with "Part of this premium, we argue" (line 49) and "in part" in the abstract.
- **AI regulation link**: Qualified with "may partly reflect" (lines 55, 218), not presented as a definitive explanation.
- **Financial frictions**: Described with "could in principle" (line 51), presented as motivation for the incompleteness assumption rather than a modeled result.
- **Quantitative fit**: Described as "broadly consistent with" (line 190), not as a calibration match.
- **Conclusion**: Explicitly acknowledges the model "abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details" and states the goal is "not to provide a definitive account of AI stock valuations but to highlight a specific channel" (lines 268-269).
- **Policy implications**: Described as "nuanced" (line 259) and transfers "may be worth designing" (line 260), not as firm recommendations.
- **GKP contribution**: Characterized modestly throughout; the paper credits GKP with the central economic logic and frames its own contribution as applying GKP's insights to the AI singularity setting.

No instance was found where the paper overstates conclusions from an unmodeled channel or allows the reader to infer that an unmodeled mechanism has been formally established.
