# tests/theory-unmodeled-channels.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 1m 8s
[ralph-garage/agent-logs/20260412T093252.137507-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.137507-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently flags unmodeled channels with explicit disclaimers and uses cautious language ("may," "partly," "suggests") when discussing mechanisms it does not formally capture.

## Economic Channels and Modeling Status

### Explicitly Modeled
1. **Hedging channel / displacement risk**: Core mechanism. Household uses AI stocks to hedge against singularity displacement. Formalized in Proposition 1 with closed-form P/D ratios.
2. **Market incompleteness**: Household cannot trade restricted AI equity. Built into model structure; discussed as the key driver.
3. **Extinction risk**: Singularity triggers extinction with probability xi (following Jones 2024). Proposition 2 quantifies attenuation of valuation premium.
4. **Veto / blocking AI development**: Extension 1. Proposition 3 shows risk-averse household may block socially efficient AI development under incomplete markets.
5. **Government transfers with deadweight costs**: Extension 2. Tax-and-transfer mechanism with quadratic deadweight costs; closed-form effective displacement parameter.

### Discussed but Not Modeled
6. **Entry of new cohorts / creative destruction (GKP-style)**: The paper draws an analogy to GKP's framework but explicitly states: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1) and "we do not model the entry dynamics that are central to their framework" (Section 2.3).
7. **Continuous displacement**: The discussion section explicitly contrasts: "GKP model continuous displacement from expanding technological variety, while we model a sudden, severe shift" (Section 2.3).
8. **Wealth heterogeneity and AI attitudes**: The paper connects to Jones (2024)'s observation about wealth and risk attitudes but frames it as "a complementary channel" rather than a modeled result (Section 4.1).
9. **Intergenerational transfers / bequests**: Attributed to GKP as their observation; paper says "We take this observation to the specific setting of an AI singularity" (Section 4.2).
10. **Continuous-time dynamics, heterogeneous beliefs, production-side details**: Conclusion explicitly lists these as abstractions: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features" (Section 5).

### Empirical mapping caveats
11. **NASDAQ-to-model mapping**: The paper flags: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure" (Section 3).

## Assessment of Caution

The paper is consistently cautious across every unmodeled channel:

- **Explicit disclaimers** appear wherever the paper discusses mechanisms it does not formally capture (entry dynamics, continuous displacement, production-side details).
- **Hedging language** is used throughout: "in part" (abstract), "may partly reflect" (Sections 1, 4.1), "suggests that...may be worth" (Section 4.2), "broadly suggestive" (Section 3).
- **Attribution to prior work** is careful: insights about displacement risk and incomplete markets are credited to GKP; the contribution is framed as "purposefully modest."
- **The conclusion** is a model of caution, explicitly listing abstractions and stating: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Approximations are flagged**: The closed-form P/D approximation is noted as becoming less accurate as Delta-theta grows, and Table 1 reports numerically exact values.

No instance was found where the paper makes strong claims about a channel it does not formally model.
