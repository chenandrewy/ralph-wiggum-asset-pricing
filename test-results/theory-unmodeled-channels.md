# tests/theory-unmodeled-channels.py
Started: 2026-04-11 16:10:24 EDT
Runtime: 1m 5s
[ralph-garage/agent-logs/20260411T161024.925042-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260411T161024.925042-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, flagging each abstraction and qualifying empirical comparisons.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging motive / displacement risk**: Core mechanism. Household uses AI stocks to hedge against singularity-driven displacement (Proposition 1).
2. **Market incompleteness**: Household cannot trade restricted AI equity; this drives the valuation premium.
3. **Extinction risk**: Modeled as probability $\xi$ within the singularity event (following Jones 2024). Proposition 2 quantifies attenuation.
4. **Veto / blocking AI development**: Extension 1 models household's option to block AI development at cost $\kappa$ (Proposition 3).
5. **Positive singularity**: Extension 1 introduces probability $q$ of a positive singularity outcome.
6. **Government transfers with deadweight costs**: Extension 2 models tax-and-transfer with waste parameter $\delta$.

### Discussed but Not Explicitly Modeled
7. **Entry dynamics / creative destruction (GKP 2012)**: GKP's overlapping-generations structure with new cohorts of firms entering the economy. The paper explicitly flags this: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1). Reiterated in Section 2.3: "we do not model the entry dynamics that are central to their framework."
8. **Continuous-time dynamics**: Acknowledged in conclusion as an abstraction.
9. **Heterogeneous beliefs**: Acknowledged in conclusion as an abstraction.
10. **Production-side details**: Acknowledged in conclusion as an abstraction.
11. **Wealth heterogeneity via existential risk (Jones 2024)**: The paper discusses Jones's channel where attitudes toward AI depend on consumption levels, and carefully distinguishes it from its own complementary channel through financial markets: "Our model offers a complementary channel through financial markets rather than existential risk" (Section 4.1).

## Cautiousness Assessment

The paper is consistently cautious about unmodeled channels in several ways:

1. **GKP entry dynamics**: Two explicit disclaimers (Sections 2.1 and 2.3) that the model does not capture the entry dynamics central to GKP. The analogy between AI owners and future capital owners is clearly labeled as "just an analogy."

2. **Empirical comparison**: The quantitative section explicitly qualifies the NASDAQ comparison: "This comparison is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure" (Section 3).

3. **Approximation transparency**: The closed-form P/D expression is flagged as an approximation that "becomes less accurate as $\Delta\theta$ grows," with numerically exact values reported separately (Section 2.2).

4. **Scope modesty**: The conclusion explicitly states: "It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

5. **GKP citation sensitivity**: The paper is careful to attribute the core incomplete-markets insight to GKP and frame its own contribution as taking GKP's ideas to a specific setting, not as originating the displacement-risk framework.

No instance was found where the paper discusses an unmodeled channel without appropriate qualification or caution.
