# tests/theory-intro-payoff.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 57s
[ralph-garage/agent-logs/20260412T154740.740403-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.740403-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature maps to an economic result that is explicitly discussed in the introduction.

## Detailed Findings

### Modeling Features and Introduction Payoffs

| Modeling Feature | Economic Result | Introduction Reference |
|---|---|---|
| Incomplete markets (restricted AI equity) | AI stocks command a hedging premium | "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium." |
| Discrete singularity with displacement (φ) | Hedging motive drives valuations | "investors use AI stocks to hedge against an AI singularity that displaces their consumption" |
| Productivity boost (η) | Quantitative P/D ratios | "P/D ratios for AI stocks roughly double relative to non-AI stocks" at p = 1% |
| Two asset types with dividend dynamics (θ, Δθ) | AI stocks are a partial hedge | "AI stocks grow as a share of the economy with each singularity, making them a partial hedge" |
| CRRA preferences (γ > 1) | Risk-averse household faces uninsurable downside | "a risk-averse household that cannot hedge displacement may rationally choose to block it" |
| Extinction risk (ξ) | Extinction attenuates the premium (Prop 2) | "Extinction risk...partially offsets this premium...narrowing the valuation spread (Proposition 2)" |
| Positive singularity (q) | Veto distortion despite efficient development (Prop 3) | "When the positive singularity is more likely than the negative one, AI development is socially efficient, yet a risk-averse household...may rationally choose to block it" |
| Veto mechanism (κ) | Rational blocking of AI development | "Calls to slow or halt AI development may partly reflect investors' inability to hedge the downside" |
| Government transfers (τ, δ) | Transfers overcome deadweight costs under singularity | "Government transfers can substitute for missing markets...even grossly inefficient transfers become effective, because the resource base overwhelms the deadweight costs" |

### Summary

The introduction systematically previews every economic result that the model delivers:
1. **Hedging premium** — from incomplete markets, displacement, and AI dividend dynamics
2. **Extinction attenuation** — from the extinction channel (ξ)
3. **Veto distortion** — from positive singularity (q), veto cost (κ), and risk aversion (γ)
4. **Transfer effectiveness** — from government transfers (τ) overcoming deadweight costs (δ) when growth (η) is large

No modeling feature is introduced without a corresponding payoff in the introduction. The common thread—market incompleteness—is explicitly stated in the final paragraph of the introduction.
