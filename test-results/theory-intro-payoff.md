# tests/theory-intro-payoff.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 55s
[ralph-garage/agent-logs/20260409T203927.600653-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260409T203927.600653-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature in the paper connects to an economic result that is discussed in the introduction.

## Detailed Mapping: Modeling Features → Introduction Results

| # | Modeling Feature | Intro Discussion | Intro Location |
|---|-----------------|-----------------|----------------|
| 1 | Market incompleteness (private AI capital untradeable) | "much of this capital is private...this market incompleteness forces investors into publicly traded AI stocks" | Para 2 |
| 2 | Stochastic singularity (probability p) | "a stochastic singularity that shifts consumption toward AI owners"; P/D ratios across "plausible singularity probabilities" | Para 4 (GKP paragraph) |
| 3 | Displacement (household share drops by phi) | "severe displacement"; "AI stocks pay off precisely when the household's consumption falls" | Para 4 |
| 4 | Productivity boost (eta) | "aggregate consumption rises" in singularity; P/D ratios "roughly six times" | Para 4 |
| 5 | Extinction risk (xi, Jones 2024) | "Extinction risk attenuates this gap: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest" | Para 4 |
| 6 | AI vs non-AI stocks with dividend share expansion (Delta-theta) | "AI stocks grow as a share of the economy with each singularity, making them a partial hedge" | Para 4 |
| 7 | CRRA preferences (gamma > 1) | Drives both the hedging motive (high marginal utility in displacement) and the veto result (risk aversion makes downside loom larger); both discussed | Paras 4-5 |
| 8 | Positive singularity + veto mechanism (Extension 1) | "When the positive singularity is more likely than the negative one, AI development is socially efficient. Yet a risk-averse household that cannot hedge displacement may rationally choose to block it" | Para 5 |
| 9 | Government transfers with deadweight costs (Extension 2) | "the sheer abundance of resources can overcome the frictions that normally make government transfers ineffective...even highly inefficient redistribution delivers large consumption gains" | Para 6 |

## Notes

- The existence condition (Remark 1, where P/D ratios can diverge under extreme displacement) is not explicitly mentioned in the introduction. However, this is a technical boundary condition rather than a distinct modeling feature, and its economic implication -- motivating the role of transfers -- is discussed. The introduction's transfer paragraph covers the economic content without referencing the technical pricing breakdown.
- All three propositions (P/D ratios, comparative statics, veto) have clear introductory counterparts.
- The quantitative calibration result (P/D ratios ~6x) is previewed in the introduction.
