# tests/theory-unmodeled-channels.py
Started: 2026-04-12 14:18:19 EDT
Runtime: 1m 13s
[ralph-garage/agent-logs/20260412T141819.035802-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260412T141819.035802-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, flagging each limitation clearly.

## Economic Channels and Modeling Status

### Explicitly Modeled Channels
1. **Hedging motive / displacement risk**: Core mechanism. Household uses AI stocks to hedge against singularity displacement. Fully formalized in Propositions 1-2.
2. **Market incompleteness**: Household cannot trade restricted AI equity. Source of valuation premium. Explicitly modeled via the separation of α (consumption share) and θ (dividend share).
3. **Extinction risk**: Modeled as probability ξ conditional on singularity, following Jones (2024). Proposition 2 derives attenuation effect.
4. **Veto / AI development distortion**: Extension 1. Proposition 3 shows risk-averse household may block socially efficient development under incomplete markets.
5. **Government transfers with deadweight costs**: Extension 2. Tax rate τ with quadratic deadweight δτ. Quantitative analysis shows explosive growth can overwhelm waste.

### Discussed but Not Explicitly Modeled Channels
6. **Entry dynamics / new cohorts (GKP's creative destruction)**: The paper discusses GKP's mechanism where displacement comes from new firms entering the economy, and AI owners play an analogous role. **Cautious?** Yes. Two explicit disclaimers:
   - "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." (Section 2.1)
   - "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants." (Section 2.3)

7. **Continuous-time dynamics**: Mentioned in the conclusion as an abstraction. **Cautious?** Yes. Conclusion states: "It abstracts from continuous-time dynamics..."

8. **Heterogeneous beliefs**: Listed in the conclusion as omitted. **Cautious?** Yes.

9. **Production-side details**: Listed in the conclusion as omitted. **Cautious?** Yes.

10. **Wealth heterogeneity and attitudes toward AI risk**: Discussed in the context of Jones (2024)'s observation about risk attitudes varying with consumption levels. The paper positions its own channel as "complementary" rather than a substitute. **Cautious?** Yes. It does not overclaim.

11. **Repeated singularities in the veto extension**: The veto analysis treats the singularity as one-shot for tractability. **Cautious?** Yes. The paper notes: "Allowing repeated singularities would reinforce the veto motive by compounding displacement risk."

### Approximations and Empirical Mapping (Also Cautious)
- **Closed-form approximation**: "The closed-form expressions... rely on an approximation: the post-singularity P/D ratio is treated as equal to the pre-singularity ratio. This is exact when Δθ → 0 and becomes less accurate as Δθ grows." Numerically exact values are also reported.
- **Transfer approximation**: "For simplicity, we compute φ_eff at the initial share α_0... This approximation does not affect the qualitative conclusions."
- **Empirical mapping**: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure."
- **Scope**: Conclusion explicitly states "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

## Assessment

The paper is consistently cautious about unmodeled channels. Each channel that is discussed but not formally captured comes with an explicit disclaimer. The most important instance is the treatment of GKP's entry dynamics, which receives two separate disclaimers in different sections. The conclusion forthrightly lists the model's abstractions. Empirical claims are hedged with acknowledgments of imperfect mapping. The overall contribution is characterized modestly. No instance was found where the paper discusses an unmodeled channel as though it were captured by the formal framework.
