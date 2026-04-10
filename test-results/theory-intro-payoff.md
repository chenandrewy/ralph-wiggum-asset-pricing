# tests/theory-intro-payoff.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 49s
[ralph-garage/agent-logs/20260409T220435.843929-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260409T220435.843929-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature maps to an economic result discussed in the introduction.

## Detailed Findings

### Modeling features and their introduction payoffs

| # | Modeling Feature | Intro Payoff | Location in Intro |
|---|-----------------|-------------|-------------------|
| 1 | Market incompleteness (restricted AI equity, AI owners) | "markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium" | Para 2-3 |
| 2 | Singularity probability $p$ | "stochastic singularity"; quantitative results across "plausible singularity probabilities" | Para 3-4 |
| 3 | Displacement $\phi$ | "displaces their consumption"; "shifts consumption toward AI owners holding private capital" | Para 2-3 |
| 4 | Productivity jump $\eta$ | Implicit in singularity definition; explicit in transfers discussion ("singularity-driven growth") | Para 2, 5 |
| 5 | Extinction risk $\xi$ | "Extinction risk attenuates this gap: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest" | Para 4 |
| 6 | Two asset classes (AI vs non-AI stocks, $\theta_t$, $\Delta\theta$) | "AI stocks grow as a share of the economy with each singularity, making them a partial hedge" | Para 3 |
| 7 | CRRA preferences with $\gamma > 1$ | "risk-averse household that cannot hedge displacement" | Para 4 |
| 8 | Positive singularity + veto (Extension 1) | "When the positive singularity is more likely than the negative one, AI development is socially efficient. Yet a risk-averse household...may rationally choose to block it" | Para 4 |
| 9 | Government transfers with deadweight costs $\delta$ (Extension 2) | "government transfers that becomes compelling when singularity-driven growth overwhelms deadweight costs" | Abstract, Para 5 |
| 10 | Existence condition (Remark 1) | Implicit in the transfers discussion: "the abundance of resources in a singularity can overcome the market frictions" | Para 5 |
| 11 | Closed-form P/D ratios (Proposition 1) | "The model delivers closed-form price-dividend ratios" and "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks" | Para 4 |
| 12 | Comparative statics (Proposition 2) | Displacement severity, singularity probability, and extinction effects all previewed | Para 4 |

### Assessment

The introduction systematically previews every modeling ingredient and its economic consequence. The mapping is tight: no modeling feature is introduced without a corresponding result being flagged in the introduction, and no introduction claim lacks a formal counterpart in the model. The hedging channel, extinction attenuation, veto distortion, and transfers result are all clearly connected from intro to formal model.
