# tests/theory-unmodeled-channels.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 1m 14s
[ralph-garage/agent-logs/20260411T214322.786842-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260411T214322.786842-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, using clear disclaimers, hedging language, and explicit acknowledgments of limitations.

## Channels and their modeling status

### Explicitly modeled
1. **Hedging/displacement risk premium** -- Core mechanism via SDF and P/D ratios (Proposition 1).
2. **Market incompleteness** -- Household cannot trade restricted AI equity; modeled via distinct consumption share (alpha) vs dividend share (theta).
3. **Extinction risk attenuation** -- Modeled via extinction probability xi (Proposition 2).
4. **Singularity productivity jump** -- Modeled via eta parameter.
5. **Veto/blocking of AI development** -- Extension 1, Proposition 3.
6. **Positive vs negative singularity** -- Extension 1, probability q.
7. **Government transfers with deadweight costs** -- Extension 2, tax rate tau with waste parameter delta.

### Discussed but NOT explicitly modeled
1. **Entry dynamics / new cohorts of firms (GKP-style)** -- AI owners serve as an analogy for future capital owners.
2. **Continuous-time dynamics** -- Abstracted from; discrete-time model used.
3. **Heterogeneous beliefs** -- Not modeled; representative household framework.
4. **Production-side details** -- Abstracted from entirely.
5. **Broader trading of AI equity** -- Discussed as the ideal but infeasible solution; not modeled.
6. **Wealth heterogeneity** -- Discussed via comparative statics on alpha, but the model has a single representative household.

## Assessment of caution

The paper handles every unmodeled channel with appropriate care:

- **Entry dynamics**: Explicitly flagged twice. Line 79: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 172: "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."

- **Model scope**: The conclusion states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

- **Empirical claims**: The quantitative section uses cautious language: "The magnitudes are broadly suggestive" and "This comparison is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure."

- **Policy implications**: The paper hedges: "The policy implication is nuanced. In normal times, government transfers are a blunt and wasteful tool for addressing displacement risk."

- **Real-world connections**: Uses "may partly reflect" when connecting the veto result to real-world AI regulation debates, rather than claiming the model fully explains such phenomena.

- **Approximations**: The closed-form P/D ratio relies on an approximation (post-singularity P/D treated as equal to pre-singularity), which is explicitly acknowledged and supplemented with numerically exact solutions in the table.

- **GKP contribution**: The paper is modest in characterizing its contribution relative to GKP, noting that "the main insights about displacement risk and incomplete markets are already in GKP" (per the spec) and describing its extensions as taking GKP's observations "to the specific setting of an AI singularity."

No instances were found where the paper claims to model something it does not, or where it draws strong conclusions from unmodeled channels without appropriate qualification.
