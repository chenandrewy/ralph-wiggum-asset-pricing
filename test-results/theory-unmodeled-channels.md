# tests/theory-unmodeled-channels.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 1m 20s
[ralph-garage/agent-logs/20260411T101504.817333-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260411T101504.817333-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently hedges claims about channels it does not explicitly model, using appropriate caveats and disclaimers throughout.

## Channels and modeling status

| Channel | Modeled? | Cautious? |
|---------|----------|-----------|
| Hedging displacement via AI stocks | Yes (core mechanism) | N/A |
| Market incompleteness (restricted equity) | Yes (core assumption) | N/A |
| Extinction risk | Yes (parameter xi) | N/A |
| Displacement of household consumption | Yes (parameter phi) | N/A |
| Veto / blocking AI development | Yes (Extension 1) | N/A |
| Government transfers with deadweight costs | Yes (Extension 2) | N/A |
| Positive singularity | Yes (Extension 1) | N/A |
| Entry of new cohorts / creative destruction (GKP) | No | Yes |
| Continuous-time dynamics | No | Yes |
| Heterogeneous beliefs | No | Yes |
| Production-side details | No | Yes |
| Wealth heterogeneity across households | No (comparative statics only) | Yes |
| Earnings growth vs. valuation multiples (empirical) | No (empirical comparison only) | Yes |

## Assessment of cautiousness for unmodeled channels

**Entry dynamics (GKP).** The paper explicitly flags this twice: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (line 77) and "we do not model the entry dynamics that are central to their framework" (line 178). This is clear and appropriately cautious.

**Continuous-time dynamics, heterogeneous beliefs, production-side details.** The conclusion states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis" (line 292). The paper explicitly acknowledges these omissions and frames the model's goal as highlighting a specific channel rather than providing a comprehensive account.

**Wealth heterogeneity.** The paper discusses how "households with larger consumption shares---more exposed to displacement---have stronger veto incentives" (line 240) as a comparative static interpretation of the single-agent model. It uses the phrase "Our model offers a complementary channel" rather than claiming to model heterogeneity directly. This is a standard and appropriate use of comparative statics.

**Empirical comparison.** The paper states: "This comparison is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure" (line 198). It frames magnitudes as "broadly suggestive" rather than calibrated.

**Closed-form approximation.** The paper acknowledges the stationarity approximation in Proposition 1, notes it "becomes less accurate as Delta-theta grows," and provides numerically exact values in the table as a check (line 153).

**Policy implications.** The paper hedges: "In normal times, government transfers are a blunt and wasteful tool" and frames the singularity case as a conditional possibility, not a recommendation (line 283).

Throughout, the paper uses appropriately cautious language for unmodeled channels: "may partly reflect," "complementary channel," "comparison is imperfect," "broadly suggestive," "deliberately simple." No unmodeled channel is presented as though it were captured by the formal framework.
