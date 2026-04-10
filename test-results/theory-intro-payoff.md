# tests/theory-intro-payoff.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 1m 5s
[ralph-garage/agent-logs/20260409T202148.441146-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.441146-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature leads to an economic result that is discussed in the introduction.

## Detailed Findings

### Modeling features and their introduction payoffs

1. **Discrete singularity (prob $p$, productivity boost $\eta$)** — Intro: "stochastic singularity that shifts consumption toward AI owners holding private capital." Quantitative result: "P/D ratios for AI stocks can reach roughly six times those of non-AI stocks across plausible singularity probabilities."

2. **Displacement ($\phi$)** — Intro: "displaces their labor income and consumption." This is the core mechanism driving the hedging channel.

3. **Market incompleteness (private AI capital)** — Intro: "much of this capital is private, held by founders and early-stage investors in firms that may not yet exist. This market incompleteness forces investors into publicly traded AI stocks as an imperfect substitute." Also drives the veto result: "calls to slow or halt AI development may partly reflect investors' inability to share in its upside."

4. **Two asset types with dividend dynamics ($\theta$, $\Delta\theta$)** — Intro: "AI stocks grow as a share of the economy with each singularity, making them a partial hedge." Delivers the valuation spread result.

5. **CRRA preferences ($\gamma > 1$)** — Intro (implicit): "risk-averse household that cannot hedge displacement may rationally choose to block it." Risk aversion is the force that makes the downside loom larger than the expected upside.

6. **Extinction risk ($\xi$)** — Intro: "Extinction risk attenuates this gap: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest, reducing the probability weight on the non-extinction states where the hedging channel operates."

7. **Positive singularity ($\lambda$) and veto mechanism** — Intro: "When the positive singularity is more likely than the negative one, AI development is socially efficient. Yet a risk-averse household that cannot hedge displacement may rationally choose to block it."

8. **Government transfers with deadweight costs ($\tau$, $\delta$)** — Intro: "even highly inefficient redistribution delivers large consumption gains---the resource base is so enormous that waste becomes tolerable."

### Note on the existence condition

Remark 1 (P/D ratio divergence under extreme displacement) is discussed in Section 4.2 but not explicitly in the introduction. This is a mathematical property of the pricing formula rather than a separate modeling feature — it arises from displacement severity ($\phi$) and risk aversion ($\gamma$), both of which are discussed in the introduction. It does not constitute a missing payoff.
