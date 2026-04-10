# tests/theory-unmodeled-channels.py
Started: 2026-04-09 20:07:38 EDT
Runtime: 57s
[ralph-garage/agent-logs/20260409T200738.673979-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T200738.673979-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently hedges claims about unmodeled channels, explicitly disclaims what it does not capture, and avoids overclaiming.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging / displacement risk under incomplete markets** -- Core model: household cannot trade private AI capital, AI stocks serve as partial hedge (Section 2).
2. **Extinction risk** -- Probability $\xi$ of extinction conditional on singularity (Section 2.1).
3. **Market incompleteness** -- Household cannot trade private AI capital; source of valuation spread (Section 2).
4. **Positive singularity** -- Extension 1 allows positive singularity with probability $\lambda$ (Section 4.1).
5. **Veto / blocking AI development** -- Extension 1 models household veto under incomplete vs. complete markets (Section 4.1).
6. **Government transfers with deadweight costs** -- Extension 2 models tax-and-transfer with quadratic deadweight costs (Section 4.2).

### Not Explicitly Modeled -- Assessment of Caution

1. **Entry dynamics / creative destruction by new cohorts (GKP 2012)**
   - Discussed extensively in Sections 2.1 and 2.3.
   - Caution: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." (Section 2.1) and "we do not model the entry dynamics that are central to their framework" (Section 2.3). **Appropriately cautious.**

2. **Continuous displacement from expanding technological variety (GKP)**
   - Discussion section contrasts: "GKP model continuous displacement from expanding technological variety, while we model a sudden, severe shift." **Appropriately cautious.**

3. **Post-singularity P/D dynamics**
   - Appendix A notes: "For tractability, we focus on the pre-singularity valuation, treating the post-singularity P/D ratio as approximately $v^{AI}$." **Transparent about approximation.**

4. **Continuous-time dynamics, heterogeneous beliefs, production-side details**
   - Conclusion explicitly lists these as abstractions: "It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis." **Appropriately cautious.**

5. **Labor income as a separate channel**
   - Introduction mentions "displaces their labor income and consumption," but the model works only through consumption shares ($\alpha_t$), not a separate labor-income channel. This is a minor looseness, but the model's consumption-share mechanism implicitly captures the idea, and the paper does not make claims about labor market dynamics. **Acceptable.**

6. **Financial market solutions beyond public stocks**
   - Introduction: "financial market solutions to AI disaster risk...remain under-explored in the AI risk discourse, even though market frictions limit their reach." This is framed as an observation about the discourse, not a claim the model addresses. **Appropriately cautious.**

7. **AI regulation and policy**
   - End of Extension 1: "This connects to debates about AI regulation: calls to slow or halt AI development may partly reflect the inability of most investors to share in the upside." Uses "may partly reflect" -- hedged appropriately. **Appropriately cautious.**

8. **Scope of contribution relative to GKP**
   - Discussion: "The key difference is the nature of the displacement event" and attributes central economic logic to GKP. Contribution is characterized modestly. **Appropriately cautious.**

## Summary

The paper is systematically cautious about every channel it does not explicitly model. It uses explicit disclaimers for entry dynamics (the most important unmodeled channel), lists abstractions in the conclusion, hedges real-world policy connections with "may partly reflect," and frames its contribution modestly relative to GKP. No channel is discussed as if it were modeled when it is not.
