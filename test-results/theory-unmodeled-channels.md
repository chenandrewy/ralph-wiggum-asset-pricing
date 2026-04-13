# tests/theory-unmodeled-channels.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 1m 12s
[ralph-garage/agent-logs/20260412T202602.585684-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260412T202602.585684-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently and explicitly flags every unmodeled channel, uses cautious language when discussing them, and makes no claims that exceed the model's scope.

## Channels and Assessment

### Explicitly Modeled Channels
1. **Hedging / displacement risk via AI stocks** — core mechanism, fully modeled with closed-form P/D ratios
2. **Market incompleteness (restricted AI equity)** — modeled as household's inability to trade private AI capital
3. **Extinction risk** — modeled via parameter ξ; Proposition 2 derives its attenuating effect
4. **Veto / blocking AI development** — modeled in Extension 1 with positive and negative singularities
5. **Government transfers with deadweight costs** — modeled in Extension 2 with effective displacement parameter φ_eff

### Discussed but Not Modeled — Assessed for Caution

6. **Entry dynamics / new cohorts of firms (GKP)** — NOT modeled. The paper is very cautious: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1). Reiterated in Section 2.3: "though we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."

7. **Creative destruction by new entrants (GKP continuous displacement)** — NOT modeled. Explicitly contrasted: "GKP model continuous displacement from expanding technological variety, while we model a sudden, severe shift" (Section 2.3). The paper notes "This discontinuity... cannot arise under GKP's gradual displacement."

8. **Continuous-time dynamics** — NOT modeled. Flagged in conclusion: "It abstracts from continuous-time dynamics."

9. **Heterogeneous beliefs** — NOT modeled. Flagged in conclusion alongside other abstractions.

10. **Production-side details** — NOT modeled. Flagged in conclusion: "abstracts from... production-side details, and many other features that would enrich the analysis."

11. **Bequests and intergenerational gifts (GKP mechanism)** — Discussed as GKP's mechanism in Extension 2 context ("In an economy populated by a representative, altruistically-linked dynasty, bequests and gifts between generations would ensure equal consumption"), but not claimed as part of the paper's model. Appropriately framed as GKP's observation.

12. **Jones (2024) preference channels (risk aversion + consumption levels)** — Discussed at end of Extension 1. The paper frames its own contribution as "a complementary channel through financial markets rather than existential risk," explicitly distinguishing what it models from what Jones models.

13. **Empirical mapping (NASDAQ vs. model AI/non-AI)** — The quantitative section is explicitly cautious: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure."

14. **P/D ratio approximation** — The paper flags the closed-form approximation: "This approximation becomes exact as Δθ → 0 and becomes less accurate as Δθ grows" and reports numerically exact values separately.

### Overall Assessment

The paper is consistently cautious about unmodeled channels:
- Every unmodeled channel is explicitly flagged with clear language
- The GKP entry dynamics are flagged twice with "Importantly, we do not explicitly model..."
- The conclusion uses deliberately modest framing: "Our model is deliberately simple" and "The goal is not to provide a definitive account... but to highlight a specific channel"
- The contribution relative to GKP is "purposefully modest" per the spec, and the paper delivers on this
- No claims exceed the model's formal scope
