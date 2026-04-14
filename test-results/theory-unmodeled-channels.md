# tests/theory-unmodeled-channels.py
Started: 2026-04-14 10:33:09 EDT
Runtime: 1m 3s
[ralph-garage/agent-logs/20260414T103309.985407-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260414T103309.985407-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, using hedging language and explicit disclaimers throughout.

## Channels and Modeling Status

### Explicitly Modeled Channels
1. **Hedging channel (AI stocks hedge displacement risk)** — Core mechanism, fully modeled via the SDF and P/D ratio expressions (Proposition 1).
2. **Displacement from AI singularity** — Modeled via the parameter phi governing consumption share loss.
3. **Market incompleteness** — Modeled as the household's inability to trade restricted AI equity.
4. **Extinction risk** — Modeled via probability xi, following Jones (2024). Proposition 2 derives its attenuating effect.
5. **Veto of AI development** — Modeled in Extension 1 with positive/negative singularity and a veto cost kappa.
6. **Government transfers with deadweight costs** — Modeled in Extension 2 with tax rate tau and deadweight parameter delta.

### Discussed but Not Explicitly Modeled Channels
1. **Entry dynamics / creative destruction by new cohorts (GKP 2012)** — AI owners play an "analogous role" to GKP's future entrants but entry is not modeled.
2. **Continuous displacement (GKP style)** — The paper contrasts its discrete singularity with GKP's continuous displacement.
3. **Heterogeneous beliefs** — Mentioned in the conclusion as an abstraction.
4. **Production-side details** — Mentioned in the conclusion as an abstraction.
5. **Continuous-time dynamics** — Mentioned in the conclusion as an abstraction.
6. **Jones (2024) preference channels** — Jones's two channels (risk aversion toward existential gambles; valuation of current living standards) are referenced, and the paper offers a "complementary channel" rather than claiming to model them.

## Assessment of Caution

The paper handles unmodeled channels with consistent care:

- **GKP entry dynamics**: Explicitly flagged twice. Line 74: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 174: "though we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."

- **Conclusion disclaimer**: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

- **Empirical mapping**: Uses hedging language when connecting to data: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect" and "The magnitudes are broadly suggestive."

- **Policy implications**: "This suggests that contingent transfer policies ... may be worth designing in advance" — uses "suggests" and "may."

- **Veto interpretation**: "calls to slow or halt AI development may partly reflect unhedgeable downside risk" — uses "may partly."

- **Jones (2024) channels**: Described as "complementary" rather than subsumed.

- **Approximations**: Transparent about the closed-form approximation (post-singularity P/D treated as equal to pre-singularity) and the transfer computation (phi_eff at initial alpha_0).

No instance was found where the paper overclaims or discusses an unmodeled channel without appropriate hedging language.
