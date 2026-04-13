# tests/theory-intro-payoff.py
Started: 2026-04-12 20:12:03 EDT
Runtime: 1m 34s
[ralph-garage/agent-logs/20260412T201203.499754-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260412T201203.499754-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature leads to at least one economic result discussed in the introduction, though the existence condition (Remark 1) is a near-miss.

## Detailed Findings

### Feature-to-Intro Mapping

| Modeling Feature | Economic Result | Discussed in Introduction? |
|---|---|---|
| Market incompleteness (restricted equity) | AI valuation premium via hedging channel | Yes — "investors use AI stocks to partially insure against displacement" |
| Displacement parameter φ | Household consumption falls, hedging demand | Yes — "singularity that displaces the typical investor's labor income and consumption" |
| Singularity probability p | P/D ratios scale with p | Yes — "at a singularity probability of one percent, P/D ratios for AI stocks roughly double" |
| Extinction risk ξ (Jones 2024) | Attenuates valuation premium (Prop 2) | Yes — "Extinction risk partially offsets this premium" |
| CRRA preferences (γ > 1) | Risk aversion drives hedging demand | Yes — implicit in hedging motive discussion |
| Productivity boost η | Aggregate consumption jump | Yes — implicit in singularity definition |
| Two public assets (θ, Δθ) | AI vs non-AI valuation spread | Yes — "pushing valuations above those of non-AI stocks" |
| Positive singularity probability q | Veto distortion (Prop 3) | Yes — "When the positive singularity is more likely than the negative one" |
| Veto cost κ | Household blocks socially efficient development | Yes — "risk-averse household...may rationally choose to block it" |
| Transfer parameters (τ, δ) | Transfers overcome deadweight costs in singularity | Yes — "government transfers that becomes compelling when singularity-driven growth overwhelms deadweight costs" |

### Near-Miss: Existence Condition (Remark 1)

The existence condition — where displacement is so severe that the SDF-weighted expected dividend growth exceeds the discount rate and no finite P/D ratio can clear the market — is discussed at length in:
- Section 2.2 (Remark 1)
- Section 2.3 (Discussion: "sufficiently severe displacement can violate the existence condition for finite prices")
- Section 4.2 (Extension 2: transfers restore finite prices from infinite hedging demand)

This result is NOT explicitly mentioned in the introduction. The intro covers the transfers channel but does not mention the infinite-price discontinuity that motivates it. However, this is a mathematical property of the P/D formula rather than a separate modeling feature, and the economic content it delivers (extreme displacement → transfers as solution) IS covered in the intro. Every actual model ingredient (parameter or assumption) does produce at least one economic result that appears in the introduction.
