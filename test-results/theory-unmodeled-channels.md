# tests/theory-unmodeled-channels.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 1m 2s
[ralph-garage/agent-logs/20260409T210608.982855-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T210608.982855-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, using explicit disclaimers, hedged language ("in part," "partly," "nuanced"), and transparent acknowledgment of abstractions.

## Channels and Assessment

### Explicitly Modeled Channels
1. **Hedging channel via AI stocks** (Proposition 1, core mechanism). Correctly presented as the paper's main contribution.
2. **Displacement under incomplete markets** (household share parameter phi, private AI capital untradeable). Formally specified.
3. **Extinction risk** (probability xi, following Jones 2024). Integrated into pricing formulas.
4. **Veto / blocking AI development** (Extension 1, Proposition 3). Formally modeled with complete- vs. incomplete-markets comparison.
5. **Government transfers with deadweight costs** (Extension 2). Formally modeled with tax rate tau and waste parameter delta.
6. **Positive singularity** (Extension 1). Household share can increase; used to establish social efficiency.

### Discussed but Not Explicitly Modeled Channels
7. **Entry of new cohorts / creative destruction (GKP 2012)** — The paper draws an analogy to GKP's overlapping-generations framework where new firm cohorts enter. **Cautiousness: Excellent.** Explicitly disclaimed twice: "we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1) and "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants" (Section 2.3).

8. **Financial market hedging instruments** — The introduction mentions that "Financial markets could in principle provide hedging instruments, but frictions---illiquidity, private ownership, the non-existence of future capital---limit their effectiveness." **Cautiousness: Good.** The paper does not claim to model these instruments; it simply notes the frictions as motivation for why markets are incomplete in the model.

9. **Continuous-time dynamics, heterogeneous beliefs, production-side details** — **Cautiousness: Excellent.** The conclusion explicitly acknowledges: "It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis" and frames the goal as highlighting "a specific channel" rather than a definitive account.

10. **Labor market mechanisms** — The introduction mentions "labor income and consumption" displacement, but the model uses consumption shares as a reduced form rather than modeling a labor market. **Cautiousness: Good.** The model's setup transparently defines displacement through the share parameter phi without claiming to capture labor market dynamics. The paper does not overclaim labor market implications.

11. **AI regulation debates** — The paper connects its veto result to real-world regulation debates. **Cautiousness: Good.** Uses hedged language: "calls to slow or halt AI development *may partly* reflect investors' inability to share in its upside."

12. **Broader contribution relative to GKP** — **Cautiousness: Excellent.** The paper explicitly states it "inherits their central economic logic" and that its contribution is "purposefully modest" in spirit, building on rather than superseding GKP's insights.

## Summary

Every unmodeled channel is treated with appropriate caution:
- Entry dynamics (GKP): double-disclaimed with precise language about what is and isn't modeled.
- Financial market solutions: noted qualitatively without overclaiming formal modeling.
- Omitted model features: explicitly listed in the conclusion as deliberate abstractions.
- Labor market details: handled through a transparent reduced-form consumption-share approach.
- Policy implications: consistently hedged with "may," "partly," "nuanced," and "worth considering."
- The hedging channel itself is framed as explaining "part of" the AI valuation premium, not all of it.
