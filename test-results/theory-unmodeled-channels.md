# tests/theory-unmodeled-channels.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 1m 2s
[ralph-garage/agent-logs/20260414T102326.825454-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260414T102326.825454-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, flagging each one and using hedged language throughout.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging motive / displacement risk**: Core mechanism. Household uses AI stocks to hedge against singularity displacement ($\phi$ parameter).
2. **Market incompleteness**: Household cannot trade restricted AI equity. Central to all results.
3. **Extinction risk**: Modeled via probability $\xi$. Attenuates valuation premium (Proposition 2).
4. **AI development distortion (veto)**: Extension 1. Household can block socially efficient AI development under incomplete markets.
5. **Government transfers with deadweight costs**: Extension 2. Tax-and-transfer with waste parameter $\delta$.

### Discussed but Not Modeled
6. **Entry dynamics / creative destruction (GKP)**: AI owners are analogized to future entrants, but entry is not modeled.
7. **Continuous-time dynamics**: Mentioned in conclusion as abstracted away.
8. **Heterogeneous beliefs**: Mentioned in conclusion as abstracted away.
9. **Production-side details**: Mentioned in conclusion as abstracted away.

## Caution Assessment

The paper handles every unmodeled channel with appropriate caution:

- **GKP entry dynamics**: Explicitly disclaimed twice. Line 74: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 174 (Discussion): "though we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants."
- **Empirical mapping**: Line 194 acknowledges the NASDAQ-to-model mapping is "imperfect," noting the NASDAQ is broader than "AI stocks," return differences partly reflect earnings growth, and the S&P 500 itself has AI exposure.
- **Extinction normalization**: Line 233 flags that the zero-extinction-utility normalization is "conservative" and notes that a more severe penalty (as Jones argues) would amplify the veto incentive.
- **Closed-form approximation**: Lines 156 and 320 explicitly discuss when the P/D approximation is exact ($\Delta\theta \to 0$) vs. less accurate, and note that Table 1 reports numerically exact values.
- **Transfer approximation**: Line 259 notes $\phi_\text{eff}$ is computed at initial $\alpha_0$ and that this "does not affect the qualitative conclusions."
- **Scope disclaimer in conclusion**: Lines 289-290: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features... The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Hedged language throughout**: The paper uses "may partly reflect" (line 234) for the veto-regulation connection, "broadly suggestive" (line 194) for magnitudes, and "complementary channel" (line 236) when positioning relative to Jones (2024).
- **Modest GKP contribution**: Line 63: "The main insights about displacement risk and incomplete markets originate in their work."

No instance was found where the paper discusses an unmodeled channel without appropriate qualification.
