# Notes on Responding to the Referee's Heterogeneity Suggestion

April 1, 2026

## What the Referee Says

From CFR-R1-report.md, Comment 2:

> *Jones (2024)* discusses the heterogeneous views of rich and poor households on the existential risk from AI Singularity, highlighting that rich people are more concerned about AI Singularity, while poor people are more willing to gamble with their lives to attain much higher living standards. This feature relies on the assumption that existential risk strikes rich and poor equally once AI reaches Singularity. Incorporating such a feature could enrich the current paper's setting and predictions, where the displacement risk from AI Singularity disproportionately benefits AI asset holders while harming the rest of the population.

## What We Actually Take from Jones

Three things (see `dev/journal/260401T19-my-notes-on-Jones.md` and `dev/journal/260401T19-Jones-2024-AERI-notes.md`):

1. **Existential risk.** The singularity may destroy rather than create. This extends the model in a useful direction (our extinction risk extension).
2. **Infinite consumption.** With $\gamma > 1$, utility is bounded, so even infinite output delivers finite welfare. This gives us the transfer/dissolution result.
3. **VSL calibration (dropped).** Jones uses VSL to pin down $\bar{u}$ and calibrate attitudes toward extinction. We explored this but it doesn't work for asset pricing: VSL disciplines the *level* of utility, but the SDF depends on *marginal* utility, so $\bar{u}$ never enters the pricing equations. See `dev/journal/260331T21-dropping-vsl-calibration.md`.

## Difficulty of Introducing Jones-Style Heterogeneity in an Interesting Way

### The Jones mechanism does not naturally translate

In Jones, heterogeneity is interesting because rich and poor agents *jointly decide* whether to pursue AI development. They disagree: poor people are willing to gamble (they gain more in utility terms from higher consumption), rich people are not (bounded utility means they have less to gain and more to lose from extinction). The tension between these views is the paper's main contribution. (See `dev/journal/260401T19-Jones-2024-AERI-notes.md`, "Heterogeneity" subsection: "Poor people have lower $v(c)$ and would be more willing to accept existential risk for higher growth.")

In our paper, the singularity arrives exogenously with probability $p$ — there is no collective decision about AI investment intensity. The rich-vs-poor disagreement about whether to pursue AI, which is the core of Jones's heterogeneity result, would need an endogenous decision over $p$ or AI investment to operate through. Introducing such a decision is possible in principle, but it would be a substantial departure from the asset pricing focus of the paper. As noted in `dev/journal/260401T19-my-notes-on-Jones.md`: "Of course, this is very different than my paper where in the singularity the representative household suffers while the AI owners gain dramatically."

### Standard asset pricing channels for heterogeneity are largely independent of displacement

We considered several well-known asset pricing channels through which agent heterogeneity affects prices. In each case, the channel would operate alongside the displacement mechanism rather than interacting with it in a way that produces new insights:

- **Heterogeneous risk aversion** (Dumas 1989, Chan & Kogan 2002). Agents with different $\gamma$ trade with each other, and the wealth distribution shifts over time, generating time-varying risk premia. This is a powerful mechanism but it would require replacing the representative household with a full cross-sectional portfolio choice problem. The displacement channel (household can't access private AI capital) would still operate in the same way.

- **Heterogeneous beliefs about $p$** (Scheinkman & Xiong 2003, Harrison & Kreps 1978). If some investors think the singularity is likely and others don't, you get speculative trading and potentially overpricing of AI stocks. This is an interesting direction in its own right, but it is about disagreement and short-sale constraints rather than displacement or hedging.

- **Heterogeneous displacement exposure** (i.e., some households are more exposed to AI displacement than others). The model already captures the key version of this: AI owners vs. the representative household. Further decomposing the household side (into rich and poor sub-agents) would not change the hedging premium mechanism, which is driven by the gap between the household and private AI capital. (GKP's own model introduces cross-sectional heterogeneity via growth vs. value firms, not via household heterogeneity — see `dev/journal/260401T19-GKP-2012-notes.md`, "Value vs. Growth Stock Returns.")

In each case, adding heterogeneity would produce additive effects (displacement risk *plus* heterogeneous-agent dynamics) rather than a genuinely new interaction. We have not found a formulation where heterogeneity and displacement risk reinforce each other in a way that yields qualitatively new predictions.

### The referee's specific suggestion

The referee writes that our displacement risk "disproportionately benefits AI asset holders while harming the rest of the population" and suggests connecting this to Jones's rich-vs-poor heterogeneity. The asymmetry between AI owners and the household is already central to the model. The natural question is whether further decomposing the household side (into rich and poor sub-agents) generates new asset pricing predictions. We have thought about this carefully and have not identified a way to do so that would sharpen the paper's contribution rather than expand its scope.

## Summary for Response

We engage seriously with Jones (2024) — existential risk and infinite consumption are incorporated, and the heterogeneous attitudes toward extinction are acknowledged. The specific mechanism the referee highlights (rich-vs-poor disagreement about whether to pursue AI) would require an endogenous decision about AI investment intensity, which is a different question from the asset pricing one we address. We considered several standard asset pricing channels for heterogeneity (risk aversion, beliefs, exposure) and found that they would operate alongside the displacement channel rather than interacting with it. We remain open to the possibility that a productive formulation exists, but have not yet found one.
