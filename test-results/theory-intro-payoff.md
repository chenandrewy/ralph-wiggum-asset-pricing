# tests/theory-intro-payoff.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 48s
[ralph-garage/agent-logs/20260409T215056.125059-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260409T215056.125059-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature introduced in the model maps to an economic result that is explicitly discussed in the introduction.

## Detailed Mapping

| # | Modeling Feature | Introduction Payoff |
|---|---|---|
| 1 | CRRA preferences with γ > 1 | "risk-averse household that cannot hedge displacement may rationally choose to block it" — risk aversion drives both the hedging channel and the veto result |
| 2 | Displacement parameter φ | Central thesis: "AI stocks serve as a hedge against a negative AI singularity—a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption" |
| 3 | Singularity probability p | "quantitative analysis shows that P/D ratios for AI stocks can reach roughly twice those of non-AI stocks across plausible singularity probabilities" |
| 4 | Productivity boost η | "singularity-driven growth overwhelms deadweight costs" — η drives the transfers result |
| 5 | Extinction risk ξ | "Extinction risk attenuates this gap: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest" |
| 6 | Two public assets (AI/non-AI) with dividend share θ and expansion Δθ | "AI stocks grow as a share of the economy with each singularity, making them a partial hedge" |
| 7 | Market incompleteness (restricted AI equity) | "Because markets are incomplete—investors cannot trade private AI capital—AI stocks command a premium" |
| 8 | Positive singularity + veto (Extension 1) | "calls to slow or halt AI development may partly reflect investors' inability to share in its upside" |
| 9 | Government transfers with deadweight costs δ (Extension 2) | "creating a rationale for government transfers that becomes compelling when singularity-driven growth overwhelms deadweight costs" |

## Notes
- Constant consumption growth rate g is a standard modeling device that provides the baseline; it does not require a separate economic result.
- The household consumption share α is a state variable that mediates displacement, not an independent modeling feature.
- No orphan modeling features were found: every substantive model ingredient produces an economic result that the introduction previews.
