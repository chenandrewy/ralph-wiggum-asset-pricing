# tests/theory-unmodeled-channels.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 55s
[ralph-garage/agent-logs/20260409T182005.673061-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.673061-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, clearly flagging limitations and using hedging language.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging/displacement risk** — Baseline model: household's consumption share drops upon singularity, AI stocks pay off in those states. Fully formalized (Proposition 1).
2. **Market incompleteness** — Private AI capital cannot be traded by the household. Defined in the asset structure (Section 2.1).
3. **Extinction risk** — Singularity triggers extinction with probability ξ. Modeled following Jones (2024).
4. **Positive singularity and veto** — Extension 1: household can block socially efficient AI development due to unhedgeable downside risk (Proposition 3).
5. **Government transfers with deadweight costs** — Extension 2: tax-and-transfer with waste parameter δ₀τ, analyzed quantitatively.

### Discussed but Not Explicitly Modeled
6. **Entry of new cohorts / creative destruction (GKP 2012)** — AI owners are analogized to future entrants, but the entry dynamics are not modeled.
7. **Cash flow optimism** — Mentioned as a complementary explanation for high AI valuations.
8. **Continuous-time dynamics, heterogeneous beliefs, production-side details** — Listed as abstractions in the conclusion.

## Cautiousness Assessment

| Unmodeled Channel | How Discussed | Cautious? |
|---|---|---|
| Entry dynamics (GKP) | "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group" (Section 2.1). Repeated in Discussion: "we do not model the entry dynamics that are central to their framework" (Section 2.3). | Yes — flagged twice, with clear language distinguishing the paper's mechanism from GKP's. |
| Cash flow optimism | "One answer is straightforward optimism about future cash flows. But a complementary explanation..." (Introduction). | Yes — framed as complementary, not as the sole or dominant explanation. |
| Continuous-time, heterogeneous beliefs, production details | "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features" (Conclusion). | Yes — openly acknowledged as simplifications. |
| Scope of results | "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel" (Conclusion). | Yes — modest framing of the paper's contribution. |
| Policy implications | "The policy implication is nuanced" (Section 4.2). Transfers described as contingent and worth "designing in advance," not as a definitive recommendation. | Yes — appropriately hedged. |
| Connection to real AI regulation | "calls to slow or halt AI development may partly reflect the inability of most investors to share in the upside" (Section 4.1). | Yes — "may partly" is cautious. |
| Quantitative fit | "The magnitudes are broadly consistent with observed valuation spreads" (Section 3). | Yes — "broadly consistent," not claiming a precise match. |
| GKP contribution | "Our contribution is to connect their framework to the specific features of AI" (Introduction). The paper inherits GKP's "central economic logic." | Yes — purposefully modest, as required by the spec. |

## Summary

The paper identifies its core unmodeled channel — GKP-style entry dynamics — and flags it explicitly and repeatedly. Other omissions (cash flow optimism, continuous-time dynamics, heterogeneous beliefs, production details) are acknowledged in appropriate places. Claims about real-world implications consistently use hedging language ("may," "partly," "broadly consistent," "nuanced"). No instance was found where the paper claims a result from a channel it does not formally capture.
