# tests/theory-intro-payoff.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 1m 9s
[ralph-garage/agent-logs/20260411T101504.818081-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260411T101504.818081-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature in the paper leads to an economic result that is discussed in the introduction.

## Detailed Mapping

Each modeling feature was checked for a corresponding economic result discussed in the introduction.

| # | Modeling Feature | Intro Payoff | Location in Intro |
|---|---|---|---|
| 1 | Market incompleteness (restricted AI equity, cannot trade private capital) | Hedging motive and valuation premium | Para 2-3: "markets are incomplete—investors cannot trade the restricted equity of AI owners" |
| 2 | Displacement parameter φ (household share drops upon singularity) | Displacement of consumption | Para 2: "singularity that displaces the typical investor's labor income and consumption" |
| 3 | Singularity probability p | Quantitative valuation spread | Para 3: "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks across plausible singularity probabilities" |
| 4 | Productivity jump η (aggregate consumption rises by 1+η) | Aggregate output growth in singularity | Para 3: implied in closed-form results; Para 6: "singularity with explosive output growth" |
| 5 | Extinction probability ξ | Attenuation of valuation gap | Para 3: "Extinction risk attenuates this gap: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest" |
| 6 | Two asset types (AI stocks with share θ, Non-AI stocks) | Valuation spread between AI and non-AI stocks | Para 3: "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks" |
| 7 | CRRA preferences with γ > 1 | Drives hedging demand and veto threshold | Implicit in hedging motive (Para 3) and explicit in veto discussion (Para 4): "risk-averse household" |
| 8 | Positive singularity probability q (Extension 1) | Social efficiency of AI development | Para 4: "When the positive singularity is more likely than the negative one, AI development is socially efficient" |
| 9 | Veto mechanism with cost κ (Extension 1) | Distortion of efficient AI development | Para 4: "risk-averse household that cannot hedge displacement may rationally choose to block it—the uninsurable downside looms larger than the expected upside" |
| 10 | Government transfers with deadweight cost δ (Extension 2) | Policy resolution under explosive growth | Para 5: "Government transfers offer an alternative, though they ordinarily incur deadweight costs... even grossly inefficient redistribution delivers large consumption gains" |

## Summary

All ten distinct modeling features produce economic results that the introduction previews. The intro follows a logical progression: (1) hedging motive from market incompleteness → (2) quantitative valuation predictions → (3) extinction attenuation → (4) real distortion via veto → (5) policy resolution via transfers. No modeling feature is introduced without a corresponding payoff in the introduction, and no introductory claim lacks a modeling foundation in the paper.
