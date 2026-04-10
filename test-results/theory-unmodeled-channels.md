# tests/theory-unmodeled-channels.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 54s
[ralph-garage/agent-logs/20260409T203927.631428-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T203927.631428-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, using clear qualifiers and disclaimers throughout.

## Channels Identified

### Explicitly Modeled Channels
1. **Hedging motive / displacement risk** — Core model: singularity shifts consumption shares, AI stocks serve as partial hedge. Fully modeled with closed-form P/D ratios.
2. **Market incompleteness** — Household cannot trade private AI capital. Modeled as the source of the hedging premium.
3. **Extinction risk** — Modeled with probability $\xi$ following Jones (2024). Interacts with displacement in a countervailing way.
4. **Positive singularity and veto** — Extension 1 models the household's option to block socially efficient AI development.
5. **Government transfers with deadweight costs** — Extension 2 models tax-and-transfer with quadratic waste, showing singularity growth can overwhelm frictions.

### Discussed but Not Modeled Channels
6. **Entry of new cohorts / creative destruction (GKP 2012)** — The paper draws an analogy between AI owners and future innovators but explicitly disclaims modeling entry dynamics.
7. **Continuous-time dynamics** — Acknowledged as an abstraction in the conclusion.
8. **Heterogeneous beliefs** — Acknowledged as an abstraction in the conclusion.
9. **Production-side details** — Acknowledged as an abstraction in the conclusion.
10. **Financial market solutions (broader trading, insurance instruments)** — Discussed as a gap in the conversation but not modeled; framed as informative for policymakers.
11. **Technology policy and labor market responses** — Mentioned as the dominant focus of existing AI-risk discussions, not modeled.
12. **Contingent transfer policies** — Suggested as worth designing but not dynamically modeled.

## Assessment of Caution

The paper is consistently cautious about unmodeled channels. Key examples:

- **Entry dynamics (GKP analogy):** "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." (Section 2.1) and "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants" (Section 2.3).
- **AI regulation connection:** Uses hedged language: "calls to slow or halt AI development *may partly reflect* the inability of most investors to share in the upside" (emphasis added).
- **Scope disclaimers in the conclusion:** "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Transfer policy implication:** "contingent transfer policies...may be worth designing in advance" — appropriately tentative.
- **Tractability assumption:** The proof explicitly notes "For tractability, we focus on the pre-singularity valuation, treating the post-singularity P/D ratio as approximately $v^{AI}$."
- **Financial market solutions:** "Market frictions limit what financial markets can do, but understanding *where* those limits bind is itself informative" — acknowledges limits without overclaiming.

No instance was found where the paper discusses an unmodeled channel as if it were captured by the model. The paper consistently distinguishes between what the model delivers and what remains outside its scope.
