# tests/theory-intro-payoff.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 1m 6s
[ralph-garage/agent-logs/20260409T205235.720054-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260409T205235.720054-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature that produces a distinct economic result is discussed in the introduction.

## Detailed Findings

### Modeling features mapped to introduction coverage

| # | Modeling Feature | Economic Result | Intro Paragraph | Coverage |
|---|---|---|---|---|
| 1 | Market incompleteness (private AI capital untradeable) | AI stocks command a hedging premium over non-AI stocks | ¶2 ("markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium") | Explicit |
| 2 | Singularity (probability p, displacement φ, productivity η) | Closed-form P/D ratios; AI P/D up to ~6x non-AI | ¶3 ("P/D ratios for AI stocks can reach roughly six times those of non-AI stocks") | Explicit |
| 3 | Extinction risk (probability ξ, per Jones 2024) | Attenuates the AI valuation premium | ¶3 ("Extinction risk attenuates this gap") | Explicit |
| 4 | Positive singularity + household veto (Extension 1) | Incomplete markets distort real decisions; household blocks socially efficient AI | ¶4 ("a risk-averse household that cannot hedge displacement may rationally choose to block it") | Explicit |
| 5 | Government transfers with deadweight costs (Extension 2) | Singularity-driven growth overwhelms deadweight costs, making redistribution effective | ¶5 ("singularity with explosive output growth...even grossly inefficient redistribution delivers large consumption gains") | Explicit |
| 6 | AI authorship of the paper itself | Concrete illustration of the displacement mechanism | ¶6 ("All analysis, code, and prose were produced by AI agents") | Explicit |
| 7 | Existence condition (Remark 1) | Extreme displacement makes prices infinite; motivates transfers | ¶5 (implicit via "creating a rationale for government transfers") | Implicit |
| 8 | Comparative statics on p and ξ (Proposition 2) | Spread increases in p, decreases in ξ | ¶3 (singularity probabilities map to valuation ratios; extinction attenuates) | Explicit |
| 9 | Comparative static on φ (Proposition 2(i)) | Spread increases in displacement severity | ¶3 (mechanism description: displacement raises marginal utility, benefiting AI stocks) | Implicit via mechanism |

### Assessment

All six modeling features that produce distinct economic results (hedging premium, extinction attenuation, veto distortion, transfer effectiveness, AI-authorship illustration, and the comparative statics) are discussed in the introduction. The displacement-severity comparative static (Proposition 2(i)) is the least explicitly stated, but it follows directly from the hedging-channel mechanism described in ¶3, where the introduction explains that the household's consumption falls upon singularity while AI stocks pay off, making them valuable. The existence condition (Remark 1) is a technical result whose economic implication (motivating transfers) is covered by the transfer discussion.

No modeling feature leads to an economic result that is absent from the introduction.
