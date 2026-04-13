# tests/theory-unmodeled-channels.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 1m 15s
[ralph-garage/agent-logs/20260412T200023.655154-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.655154-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, flagging each abstraction and acknowledging its limitations.

## Channels Identified

### Explicitly Modeled Channels
1. **Hedging channel (core mechanism):** Household uses AI stocks to partially hedge displacement risk. Modeled via closed-form P/D ratios (Proposition 1).
2. **Displacement under incomplete markets:** Household cannot trade restricted AI equity; parameter phi governs displacement severity. Fully formalized.
3. **Extinction risk:** Following Jones (2024), singularity may trigger extinction with probability xi. Explicitly modeled and interacted with valuations (Proposition 2).
4. **Veto of AI development (Extension 1):** Household can block AI development at deadweight cost kappa. Modeled with positive/negative singularity probabilities.
5. **Government transfers (Extension 2):** Tax rate tau on AI owners with quadratic deadweight costs. Formalized via effective displacement parameter phi_eff.
6. **Positive singularity (Extension 1):** Probability q that the singularity benefits the household. Explicitly modeled.

### Discussed but Not Explicitly Modeled Channels
1. **Entry dynamics / creative destruction (GKP 2012):** AI owners are analogized to future innovators who have not yet entered the economy. The paper explicitly states: "we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1) and "we do not model the entry dynamics that are central to their framework" (Section 2.3).
2. **Continuous-time dynamics:** Abstracted away. Acknowledged in the conclusion.
3. **Heterogeneous beliefs:** Abstracted away. Acknowledged in the conclusion.
4. **Production-side details:** Abstracted away. Acknowledged in the conclusion.
5. **Bequests and intergenerational transfers (GKP mechanism):** Discussed qualitatively in Extension 2 as a channel GKP identifies, but not modeled. The paper focuses on government transfers instead.
6. **Wealth heterogeneity and attitudes toward AI:** Discussed qualitatively in connection to Jones (2024)'s preference channels, clearly framed as "a complementary channel" rather than a modeled result.

## Assessment of Cautiousness

The paper is consistently cautious across every unmodeled channel:

- **Entry dynamics:** The most important unmodeled channel is flagged twice with explicit disclaimers (Sections 2.1 and 2.3). The paper carefully distinguishes its static AI-owner structure from GKP's dynamic entry mechanism.
- **GKP contribution:** The paper is purposefully modest: "The main insights about displacement risk and incomplete markets originate in their work; we connect these ideas to the AI singularity" (lit review).
- **Empirical mapping:** The paper notes "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect" and lists specific reasons (Section 3).
- **Approximations:** The closed-form P/D ratio approximation is flagged ("exact when Delta-theta -> 0 and becomes less accurate as Delta-theta grows"), and numerically exact values are provided separately. The phi_eff approximation is similarly flagged.
- **Scope:** The conclusion explicitly states: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Jones (2024) interaction:** The paper carefully distinguishes its displacement channel from Jones's existential-risk preference channels, calling its contribution "complementary."
- **Extinction utility normalization:** The paper flags that its normalization of extinction utility to zero is "conservative" and discusses how alternative normalizations would change the veto result.

No instance was found where the paper claims results from, or draws strong conclusions about, a channel it does not formally model.
