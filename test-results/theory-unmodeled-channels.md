# tests/theory-unmodeled-channels.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 1m 12s
[ralph-garage/agent-logs/20260412T095842.937252-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260412T095842.937252-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, with clear disclaimers for each.

## Channels and Modeling Status

### Explicitly Modeled Channels
1. **Hedging motive / displacement risk premium** — Core mechanism. Household uses AI stocks to hedge displacement; formalized in Proposition 1.
2. **Market incompleteness** — Household cannot trade restricted AI equity; central to all results.
3. **Extinction risk attenuation** — Parameter ξ; formalized in Proposition 2.
4. **Veto / blocking AI development** — Extension 1; formalized in Proposition 3.
5. **Government transfers with deadweight costs** — Extension 2; formalized with effective displacement parameter φ_eff.

### Discussed but Not Modeled Channels
6. **Entry dynamics / new cohorts of firms (GKP)** — Explicitly disclaimed: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (line 75). Reiterated in discussion: "we do not model the entry dynamics that are central to their framework" (line 169).
7. **Continuous displacement / creative destruction (GKP)** — Distinguished from the paper's discrete mechanism: "GKP model continuous displacement from expanding technological variety, while we model a sudden, severe shift" (line 167).
8. **Heterogeneous beliefs** — Acknowledged as abstracted away in the conclusion (line 283).
9. **Continuous-time dynamics** — Acknowledged as abstracted away in the conclusion (line 283).
10. **Production-side details** — Acknowledged as abstracted away in the conclusion (line 283).
11. **Labor market mechanisms** — Labor income displacement is captured in reduced form through φ; the paper notes "the non-tradeable component (primarily labor income) is what φ captures" (line 112), making clear this is a reduced-form treatment.
12. **Wealth heterogeneity and AI attitudes (Jones 2024)** — Discussed as a complementary channel: "Our model offers a complementary channel through financial markets rather than existential risk" (line 231). Does not claim to capture Jones's mechanism.
13. **Intergenerational transfers / bequests (GKP)** — Carefully attributed: "GKP note, in the context of a robustness argument, that intergenerational transfers..." (line 236). The paper positions its own contribution as taking this observation to a specific setting.

### Empirical Mapping
14. **NASDAQ as proxy for AI stocks** — Explicitly hedged: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure" (line 189).

## Assessment

The paper demonstrates consistent caution across all unmodeled channels:

- **Entry dynamics**: The spec requires that the paper "should not allow the reader to think that we do" model entry dynamics. The paper follows this with two separate, explicit disclaimers (lines 75 and 169).
- **Scope acknowledgment**: The conclusion states the model is "deliberately simple" and lists specific abstractions (line 283).
- **Attribution**: Contributions relative to GKP are "purposefully modest" — the paper credits GKP for the main insights and frames its own work as connecting those ideas to the AI singularity setting.
- **Empirical content**: The quantitative comparison to data is described as "broadly suggestive" (line 189) rather than definitive, with specific caveats about the imperfect mapping.
- **Complementary channels**: When discussing related mechanisms from other papers (Jones 2024 on wealth heterogeneity), the paper frames its own contribution as "complementary" rather than subsuming those channels.

No instance was found where the paper claims results from or makes strong assertions about a channel it does not formally model.
