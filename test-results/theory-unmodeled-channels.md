# tests/theory-unmodeled-channels.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 1m 6s
[ralph-garage/agent-logs/20260409T202148.445958-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.445958-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently uses cautious language when discussing channels it does not explicitly model.

## Channels Identified

### Explicitly Modeled Channels
1. **Hedging motive / displacement risk under incomplete markets** — Core model: singularity displaces household consumption share (parameter phi), private AI capital cannot be traded, AI stocks serve as partial hedge.
2. **Extinction risk** — Modeled as probability xi within the singularity event, following Jones (2024).
3. **Market incompleteness** — Household cannot trade private AI capital; this is the source of the valuation premium.
4. **Veto / blocking AI development (Extension 1)** — Household can block socially efficient AI development due to uninsurable downside risk.
5. **Positive singularity (Extension 1)** — Household share increases with probability lambda.
6. **Government transfers with deadweight costs (Extension 2)** — Tax on AI surplus, transferred to household with quadratic deadweight costs.

### Discussed but Not Modeled Channels
1. **Entry dynamics / creative destruction (GKP 2012)** — The paper discusses GKP's overlapping-generations structure with new cohorts of firms entering the economy.
2. **Technology policy and labor market solutions** — Mentioned as the dominant focus of existing AI risk discussions.
3. **Broader trading of AI-linked securities / insurance instruments** — Mentioned as potential financial market solutions.
4. **Continuous-time dynamics, heterogeneous beliefs, production-side details** — Acknowledged as features that would enrich the analysis.
5. **Labor income dynamics** — The introduction references "labor income" displacement, but the model works through consumption shares, not explicit labor markets.

## Assessment of Caution

### Entry dynamics (GKP analogy)
The paper is explicitly cautious. Line 78: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 181: "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants." This directly satisfies the spec requirement (spec item I.4.d) that the paper not allow readers to think entry dynamics are modeled.

### Technology policy and labor markets
Line 52: "Discussions of AI risk focus overwhelmingly on technology policy and labor markets; financial market solutions... remain largely absent from the conversation." This is framed as factual context about the policy landscape, not as a modeling claim. No overclaiming.

### Financial market solutions
Line 52-53: "Market frictions limit what financial markets can do, but understanding where those limits bind is itself informative for policymakers weighing complementary interventions." Cautious framing — "informative," not definitive.

### AI regulation connection
Line 234: "calls to slow or halt AI development may partly reflect the inability of most investors to share in the upside of AI progress." Uses hedging language ("may partly reflect"), appropriate given the model captures a veto mechanism but not actual regulatory dynamics.

### Policy implications of transfers
Line 269: "The policy implication is nuanced. In normal times, government transfers are a blunt and wasteful tool..." and "This suggests that contingent transfer policies... may be worth designing in advance." Uses "suggests" and "may be worth" — appropriately cautious.

### Model limitations in conclusion
Line 278: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

### GKP contribution framing
The paper is modest throughout: "We build on their framework" (line 54), "parallels GKP" (line 179), "inherits their central economic logic" (line 65). This is consistent with the spec's requirement for cautious, modest characterization of the contribution relative to GKP.

### Post-singularity approximation
The proof (line 307) transparently flags a simplification: "For tractability, we focus on the pre-singularity valuation, treating the post-singularity P/D ratio as approximately v^{AI}."

## Minor Observation
The introduction (line 50) references "labor income and consumption" displacement, while the model works only through consumption shares with no explicit labor income. This is a standard reduced-form approach and the paper does not overclaim — it generally uses "consumption" or "displacement" when describing the model's mechanics, reserving "labor income" for the economic motivation. No overclaiming detected.
