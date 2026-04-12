# tests/theory-unmodeled-channels.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 1m 21s
[ralph-garage/agent-logs/20260411T211526.521680-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.521680-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently flags unmodeled channels and avoids overclaiming about mechanisms it does not formally capture.

## Channels Identified

### Explicitly Modeled
1. **Hedging channel / displacement risk**: Core mechanism. The household's consumption share drops upon singularity (parameter phi), and AI stocks provide a partial hedge. Fully formalized in Propositions 1-2.
2. **Market incompleteness**: The household cannot trade restricted AI equity. Central to the model; the valuation premium collapses under complete markets.
3. **Extinction risk**: Modeled as probability xi of total loss upon singularity, following Jones (2024). Proposition 2 formally shows it attenuates the hedging channel.
4. **Veto / blocking AI development**: Extension 1 formally models a veto option with cost kappa. Proposition 3 derives conditions under which the household blocks socially efficient development.
5. **Government transfers with deadweight costs**: Extension 2 formally models a tax-and-transfer scheme with waste parameter delta. Closed-form expressions for effective displacement and P/D ratios under transfers.

### Discussed but Not Explicitly Modeled
6. **Entry dynamics / new cohorts of firms (GKP mechanism)**: The paper draws an analogy between AI owners and GKP's future innovators. Cautious treatment confirmed at multiple points.
7. **Creative destruction by new entrants**: Distinguished from the paper's discrete singularity mechanism.
8. **Wealth heterogeneity and AI attitudes**: Discussed as a comparative-statics implication, not a formal result.
9. **Continuous-time dynamics, heterogeneous beliefs, production-side details**: Acknowledged as abstractions in the conclusion.
10. **Labor income as a separate channel**: Bundled into the consumption share alpha rather than modeled separately.
11. **Intergenerational transfers / bequests**: Referenced from GKP's robustness discussion; the paper takes this to its own setting rather than claiming to model the same mechanism.

## Assessment of Caution

The paper is consistently cautious about every unmodeled channel identified:

- **Entry dynamics**: Explicitly flagged twice. Line 79: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 173 (Discussion): "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."

- **GKP relationship**: The paper carefully distinguishes its mechanism from GKP's continuous displacement, noting "The key difference is the nature of the displacement event" and attributing the core insights about displacement risk and incomplete markets to GKP.

- **Empirical content**: The quantitative comparison to data is hedged explicitly: "This comparison is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure."

- **Wealth heterogeneity**: Framed as a "complementary channel" and an implication of comparative statics, not a formal result from the model.

- **Scope limitations**: The conclusion states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

- **Labor income**: Transparently bundled into the displacement parameter: "the non-tradeable component (primarily labor income) is what phi captures."

No instance was found where the paper claims formal results about a channel it does not model, or where it discusses an unmodeled channel without appropriate caveats.
