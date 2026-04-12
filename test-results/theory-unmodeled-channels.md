# tests/theory-unmodeled-channels.py
Started: 2026-04-11 21:27:07 EDT
Runtime: 1m 16s
[ralph-garage/agent-logs/20260411T212707.758664-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260411T212707.758664-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently uses cautious language when discussing channels it does not explicitly model, and explicitly flags its abstractions.

## Channels identified

### Explicitly modeled channels
1. **Hedging channel via AI stocks**: Core mechanism. Household uses AI stocks to hedge displacement under incomplete markets. Formalized in Proposition 1 with closed-form P/D ratios.
2. **Displacement from singularity**: Household consumption share drops by factor phi upon singularity. Parameterized and quantified.
3. **Market incompleteness**: Household cannot trade restricted AI equity (founder stakes, pre-IPO shares). Drives the valuation wedge.
4. **Extinction risk**: Singularity triggers extinction with probability xi. Modeled explicitly following Jones (2024). Proposition 2 shows it attenuates the premium.
5. **Veto / blocking AI development** (Extension 1): Household can block development at cost kappa. Proposition 3 proves veto occurs under incomplete markets for sufficiently risk-averse households.
6. **Government transfers** (Extension 2): Tax-and-transfer mechanism with quadratic deadweight costs. Modeled with effective displacement parameter phi_eff.
7. **Complete markets benchmark**: Used as counterfactual in Proposition 3 to show veto disappears.

### Discussed but not explicitly modeled channels
1. **Entry of new cohorts / creative destruction (GKP dynamics)**: The paper draws an analogy to GKP (2012) where displacement comes from new entrants. **Cautious handling**: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (line 76). Repeated in Section 2.3: "we do not model the entry dynamics that are central to their framework" (line 169).
2. **Continuous-time dynamics**: Noted as abstracted away in the conclusion (line 283).
3. **Heterogeneous beliefs**: Noted as abstracted away in the conclusion (line 283).
4. **Production-side details**: Noted as abstracted away in the conclusion (line 283).
5. **Wealth heterogeneity and attitudes toward AI**: Discussed in connection with Jones (2024). Uses cautious framing: "Our model offers a complementary channel" (line 231).
6. **Broader trading of AI capital (ideal market solution)**: Discussed qualitatively as the ideal fix but acknowledged as infeasible due to non-existent future capital. Not modeled; only the transfer alternative is formalized.
7. **Repeated singularities compounding displacement**: Mentioned as a reinforcing effect in the veto discussion: "Allowing repeated singularities would reinforce the veto motive" (line 227). Acknowledged as unmodeled in the main veto analysis (one-shot treatment).

## Assessment of caution

The paper is consistently cautious about unmodeled channels:

- **GKP entry dynamics**: Flagged twice with explicit disclaimers (lines 76 and 169), matching the spec's requirement that the reader not be led to think entry is modeled.
- **Policy implications**: Uses hedging language throughout. "This suggests that contingent transfer policies... may be worth designing in advance" (line 274). "Calls to slow or halt AI development may partly reflect investors' inability to hedge" (line 53).
- **Empirical fit**: The quantitative comparison to NASDAQ valuations is explicitly qualified: "This comparison is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure" (line 189).
- **Scope**: The conclusion explicitly enumerates what the model abstracts from and states: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel" (line 283).
- **Approximations**: The closed-form P/D approximation is flagged as becoming less accurate as Delta-theta grows (line 151), and numerically exact values are provided alongside.

No instance was found where the paper claims results about a channel it does not model without appropriate qualification.
