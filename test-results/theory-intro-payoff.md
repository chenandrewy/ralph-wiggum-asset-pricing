# tests/theory-intro-payoff.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 1m 5s
[ralph-garage/agent-logs/20260411T211526.518593-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.518593-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature in the paper leads to an economic result that is explicitly discussed in the introduction.

## Detailed Findings

### Mapping of modeling features to introduction payoffs

1. **Displacement (φ) + market incompleteness** → Intro paras 2–3: hedging motive explanation for AI valuation premia; AI stocks as partial hedge; P/D ratios can reach ~2x non-AI stocks.

2. **Market incompleteness (restricted equity)** → Intro para 4: "Under complete markets the displacement-driven premium would largely vanish, because the household could trade the restricted AI equity directly; market incompleteness is the key driver."

3. **Extinction risk (ξ)** → Intro para 4: "extinction risk attenuates the hedging channel, because the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest." Proposition 2 quantifies this.

4. **Positive/negative singularity (q) + veto mechanism (κ)** → Intro para 5: "a risk-averse household that cannot hedge displacement may rationally choose to block it—the uninsurable downside looms larger than the expected upside. As Proposition 3 shows, calls to slow or halt AI development may partly reflect investors' inability to hedge the downside."

5. **Government transfers (τ) + deadweight costs (δ)** → Intro paras 7–8: "even grossly inefficient government transfers become effective, because the resource base grows so large that deadweight costs are overwhelmed." Links to Jones (2024) singularity growth.

6. **Productivity boost (η)** → Intro para 3 (quantitative magnitudes) and para 8 (explosive growth enables transfers despite deadweight costs).

7. **AI/non-AI dividend shares (θ, Δθ)** → Intro para 3: "AI stocks grow as a share of the economy with each singularity, making them a partial hedge."

### Conclusion

No modeling feature is introduced without a corresponding economic result in the introduction. The intro's final summary paragraph explicitly ties together all three linked results: (1) hedging-based valuation premia, (2) resistance to AI development from market incompleteness, and (3) singularity-driven growth enabling effective redistribution. Standard auxiliary parameters (β, g, γ, CRRA) serve as modeling tools and are referenced where relevant (e.g., "risk-averse household") without needing standalone discussion.
