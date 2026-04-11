# tests/theory-intro-payoff.py
Started: 2026-04-11 15:15:59 EDT
Runtime: 1m 9s
[ralph-garage/agent-logs/20260411T151559.906315-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260411T151559.906315-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature introduced in the paper leads to an economic result that is discussed in the introduction.

## Detailed Findings

### Modeling Features and Their Introduction Payoffs

1. **Singularity event (p, eta, phi) and AI/non-AI stock structure (theta, Delta-theta)**
   - Model: Proposition 1 derives closed-form P/D ratios showing AI stocks command a premium via the hedging channel (Gamma^AI > Gamma^N).
   - Intro payoff: "The model delivers closed-form price-dividend ratios, and quantitative analysis shows that P/D ratios for AI stocks can reach roughly twice those of non-AI stocks across plausible singularity probabilities."

2. **Market incompleteness (restricted AI equity, private capital)**
   - Model: The household prices assets with its own SDF (not aggregate), and the displacement parameter phi drives the wedge. If phi_eff -> 1 (complete markets), the premium collapses.
   - Intro payoff: "If markets were complete---if the household could trade the restricted AI equity---the displacement-driven premium would largely vanish, confirming that market incompleteness is the key driver."

3. **Extinction risk (xi)**
   - Model: Proposition 2 shows the valuation spread is decreasing in xi, since higher extinction probability reduces weight on non-extinction states where the hedging channel operates.
   - Intro payoff: "Extinction risk works in the opposite direction: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest, reducing the weight on non-extinction states where the hedging channel operates."

4. **Positive singularity (q) and veto cost (kappa)**
   - Model: Proposition 3 shows that under incomplete markets, sufficiently risk-averse households veto socially efficient AI development; under complete markets, they never veto.
   - Intro payoff: "A risk-averse household that cannot hedge displacement may rationally choose to block it... Complete markets would eliminate this distortion entirely."

5. **Government transfers (tau, delta)**
   - Model: Extension 2 shows transfers reduce effective displacement (phi_eff), compress AI stock valuations, and can restore finite prices when the existence condition is violated. Explosive output growth overwhelms deadweight costs.
   - Intro payoff: "Government transfers offer an alternative, though they ordinarily incur deadweight costs that consume much of their value. In a singularity with explosive output growth, however, the resource base becomes so enormous that even grossly inefficient redistribution delivers large consumption gains."

6. **CRRA preferences (gamma, beta)**
   - Standard preference structure that enables all pricing results and the veto threshold (gamma-bar in Proposition 3). Not a novel modeling feature requiring its own intro discussion.

### Conclusion

All six modeling components map cleanly to economic results that the introduction previews. No modeling feature is introduced without a corresponding payoff in the introduction, and no introductory claim lacks a formal result in the body of the paper.
