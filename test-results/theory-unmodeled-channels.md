# tests/theory-unmodeled-channels.py
Started: 2026-04-11 15:16:00 EDT
Runtime: 1m 24s
[ralph-garage/agent-logs/20260411T151600.904975-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260411T151600.904975-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently flags channels it does not explicitly model, uses cautious language when drawing implications from them, and hedges empirical comparisons appropriately.

## Channels and Assessment

### Explicitly Modeled Channels
1. **Hedging displacement via AI stocks under incomplete markets** — Core mechanism. Fully modeled with closed-form P/D ratios (Proposition 1).
2. **Extinction risk** — Modeled as probability xi; interaction with hedging premium derived in Proposition 2.
3. **Market incompleteness (inability to trade restricted AI equity)** — Modeled via separation of household consumption share (alpha) from AI dividend share (theta).
4. **Veto / blocking AI development** — Explicitly modeled in Extension 1 with formal proposition (Proposition 3).
5. **Positive singularity** — Modeled in Extension 1 with probability q.
6. **Government transfers with deadweight costs** — Explicitly modeled in Extension 2 with effective displacement parameter phi_eff.

### Discussed but Not Explicitly Modeled Channels
7. **Entry of new cohorts / future innovators (GKP dynamic)** — The paper draws an analogy between its static AI owners and GKP's entering cohorts. Cautious? **Yes.** The paper explicitly states: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1). Reiterated in Section 2.3: "we do not model the entry dynamics that are central to their framework."
8. **Creative destruction from continuous technological variety expansion** — Discussed as GKP's mechanism. Cautious? **Yes.** The paper distinguishes its discrete singularity from GKP's continuous displacement and does not claim to capture this channel.
9. **Continuous-time dynamics** — Not modeled. Cautious? **Yes.** The conclusion explicitly lists this as an abstraction.
10. **Heterogeneous beliefs** — Not modeled. Cautious? **Yes.** Explicitly listed in the conclusion as omitted.
11. **Production-side details** — Not modeled. Cautious? **Yes.** Explicitly listed in the conclusion.
12. **Wealth heterogeneity and attitudes toward AI risk** — Discussed in Section 4.1, connecting to Jones (2024). The paper has only one representative household but draws comparative-statics implications about how households with different consumption shares would behave. Cautious? **Yes.** Framed as "Our model offers a complementary channel" and "This connects wealth heterogeneity to attitudes about AI development through the displacement channel"—presented as a connection, not a formal result.
13. **Intergenerational bequests (GKP)** — Referenced from GKP's discussion. Cautious? **Yes.** The paper says "Building on their discussion, we study transfers in the specific setting of an AI singularity" and models a simpler government tax/transfer instead, without claiming to capture the bequest channel.

### Empirical Hedging
14. **NASDAQ vs. S&P 500 comparison** — The paper acknowledges the comparison is "imperfect": "the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure." Uses language like "broadly suggestive" and "consistent with."

### Overall Assessment
The paper is consistently cautious about every channel it does not explicitly model:
- Entry dynamics from GKP are flagged twice as not modeled.
- The conclusion explicitly enumerates abstractions (continuous-time, heterogeneous beliefs, production details).
- Empirical comparisons are hedged with appropriate caveats.
- Policy implications use cautious language ("may partly reflect," "suggests that").
- The contribution relative to GKP is framed modestly throughout.
- No instance found where the paper claims to capture a channel it does not formally model.
