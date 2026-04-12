# tests/theory-unmodeled-channels.py
Started: 2026-04-12 09:46:31 EDT
Runtime: 1m 27s
[ralph-garage/agent-logs/20260412T094631.067190-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260412T094631.067190-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, flagging limitations, approximations, and scope boundaries throughout.

## Channels explicitly modeled

1. **Hedging motive / displacement risk premium** -- Core model with displacement parameter $\phi$, singularity probability $p$, and closed-form P/D ratios (Proposition 1).
2. **Market incompleteness** -- Household cannot trade restricted AI equity; captured by separation of $\alpha$ (consumption share) and $\theta$ (dividend share).
3. **Extinction risk** -- Parameter $\xi$ in the singularity structure; attenuation effect proved in Proposition 2.
4. **Veto / blocking AI development** -- Extension 1, Proposition 3, with veto cost $\kappa$.
5. **Positive singularity** -- Extension 1, probability $q$, with $q > 1/2$.
6. **Government transfers** -- Extension 2, tax rate $\tau$ with deadweight costs $\delta\tau$.

## Channels discussed but not explicitly modeled

1. **Entry of new cohorts / creative destruction (GKP dynamics)** -- The paper draws an analogy between AI owners and GKP's future innovators but is explicit: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1). Reiterated in Discussion: "we do not model the entry dynamics that are central to their framework" (Section 2.3).

2. **Continuous displacement** -- The paper contrasts its discrete singularity with GKP's continuous displacement and notes the qualitative difference (existence condition for finite prices has "no analog in GKP's continuous-displacement framework").

3. **Heterogeneous beliefs** -- Listed as an abstraction in the conclusion; not overclaimed.

4. **Production-side details** -- Listed as an abstraction in the conclusion; not overclaimed.

5. **Continuous-time dynamics** -- Listed as an abstraction in the conclusion; not overclaimed.

6. **Intergenerational transfers / bequests** -- Referenced from GKP as a robustness argument; the paper models government transfers as a specific case rather than claiming to capture the full bequest channel.

7. **Wealth heterogeneity and attitudes toward AI risk** -- Jones (2024) is cited for the observation that attitudes depend on consumption levels. The paper positions its own insight as "a complementary channel through financial markets rather than existential risk" -- careful not to claim it models Jones's channel.

8. **Repeated singularities in the veto extension** -- Noted as reinforcing ("Allowing repeated singularities would reinforce the veto motive") but not claimed as modeled.

## Assessment of caution

The paper handles unmodeled channels with consistent care:

- **GKP entry dynamics**: Flagged twice with explicit disclaimers (Sections 2.1 and 2.3). This is the most important unmodeled channel and receives the strongest caveats.
- **Empirical mapping**: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect" and "The magnitudes are broadly suggestive."
- **Approximations**: The closed-form P/D ratio approximation is flagged as "exact when $\Delta\theta \to 0$ and becomes less accurate as $\Delta\theta$ grows." The $\phi_\text{eff}$ approximation at initial $\alpha_0$ is noted.
- **Scope**: The conclusion states plainly: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features." And: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Policy**: "The policy implication is nuanced" -- avoids overclaiming on transfers.
- **GKP credit**: The contribution is "purposefully modest" per the spec, and the paper delivers: "The main insights about displacement risk and incomplete markets originate in their work."

No instance was found where the paper discusses an unmodeled channel as if it were captured by the model.
