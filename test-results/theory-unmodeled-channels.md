# tests/theory-unmodeled-channels.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 1m 25s
[ralph-garage/agent-logs/20260412T154740.748513-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.748513-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently hedges claims about channels it does not explicitly model, using careful qualifiers and explicit disclaimers throughout.

## Channels Inventory

### Explicitly Modeled
1. **Hedging channel** — AI stocks pay off when household consumption falls, inflating P/D ratios via the SDF. Fully derived in Proposition 1.
2. **Displacement risk** — Parameter $\phi$ governs how singularity reallocates consumption from household to AI owners. Core mechanism.
3. **Market incompleteness** — Household cannot trade restricted AI equity; gap between $\alpha$ (consumption share) and $\theta$ (dividend share). Drives entire valuation premium.
4. **Extinction risk** — Probability $\xi$ of extinction upon singularity. Modeled per Jones (2024); attenuation effect proved in Proposition 2.
5. **Veto / blocking AI development** — Household can block AI at deadweight cost $\kappa$. Extension 1, Proposition 3.
6. **Positive singularity** — Probability $q$ of household share increasing. Extension 1.
7. **Government transfers with deadweight costs** — Tax $\tau$ on AI owners with waste fraction $\delta\tau$. Extension 2, equation (8).

### Discussed but NOT Explicitly Modeled
1. **Entry dynamics / creative destruction by new cohorts (GKP 2012)** — The paper draws an analogy between AI owners and GKP's future innovators.
2. **Continuous-time dynamics** — Mentioned in conclusion as abstracted away.
3. **Heterogeneous beliefs** — Mentioned in conclusion as abstracted away.
4. **Production-side details** — Mentioned in conclusion as abstracted away.
5. **Voluntary bequests / intergenerational transfers** — Referenced as GKP's observation; distinguished from government transfers.
6. **Earnings growth vs. valuation multiples** — Acknowledged in the empirical discussion as not disentangled.

## Caution Assessment (Channel by Channel)

### 1. Entry dynamics (GKP analogy) — CAUTIOUS
The spec flags this as critical ("we do not explicitly model this entry dynamic and should not allow the reader to think that we do"). The paper handles it carefully in two places:
- Section 2.1: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism."
- Section 2.3: "though we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."

### 2. GKP contribution framing — CAUTIOUS
The paper is modest: "The main insights about displacement risk and incomplete markets originate in their work; we connect these ideas to the AI singularity and examine how explosive growth interacts with government transfers." The contribution is characterized as extending, not originating.

### 3. Empirical mapping — CAUTIOUS
Section 3 explicitly flags the imperfect mapping: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure." Results are described as "broadly suggestive," not conclusive.

### 4. Jones (2024) preference channels — CAUTIOUS
The paper describes its own displacement channel as "complementary" to Jones's existential-risk channels, not as a replacement or encompassing framework.

### 5. Veto and AI regulation — CAUTIOUS
Uses hedged language: "calls to slow or halt AI development may partly reflect investors' inability to hedge the downside" (emphasis on "may partly").

### 6. Closed-form approximation — CAUTIOUS
Explicitly flagged: "This approximation becomes exact when $\Delta\theta \to 0$ and becomes less accurate as $\Delta\theta$ grows." Numerically exact values are provided alongside.

### 7. Conclusion scope — CAUTIOUS
"Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

## Overall Assessment
The paper is consistently cautious about every unmodeled channel it discusses. It uses appropriate qualifiers ("may," "partly," "complementary," "broadly suggestive"), provides explicit disclaimers where analogies could mislead (especially the GKP entry dynamics), and frames its own contribution modestly. No instance was found where the paper overstates what its model can deliver or implies that an unmodeled channel is captured by the formalism.
