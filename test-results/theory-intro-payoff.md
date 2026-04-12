# tests/theory-intro-payoff.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 1m 8s
[ralph-garage/agent-logs/20260412T093252.130993-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.130993-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature leads to an economic result discussed in the introduction.

## Detailed Findings

### Mapping of modeling features to introduction payoffs

| # | Modeling Feature | Economic Result | Intro Coverage |
|---|---|---|---|
| 1 | Discrete AI singularity with displacement parameter φ | AI stocks command a hedging premium because they pay off when household consumption falls | Para 2–3: "investors use AI stocks to partially insure against displacement from AI" |
| 2 | Market incompleteness (restricted equity unavailable for trading) | Valuation spread between AI and non-AI stocks; identified as "the key driver" | Para 2–3: "Because investors cannot trade the restricted equity, they turn to publicly traded AI stocks as the only available partial hedge" |
| 3 | Extinction risk ξ (Jones 2024) | Attenuates the valuation premium; Proposition 2 | Para 3: "extinction risk attenuates the premium, because the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest" |
| 4 | Two public assets: AI stocks (θ share) and non-AI stocks | Closed-form P/D ratios; AI P/D roughly doubles non-AI at p=1% | Para 3: "closed-form price-dividend ratios…P/D ratios for AI stocks roughly double relative to non-AI stocks" |
| 5 | Positive singularity (probability q), veto mechanism with cost κ | Risk-averse household may rationally block socially efficient AI development; Proposition 3 | Para 5: "a risk-averse household that cannot hedge displacement may rationally choose to block it—the uninsurable downside looms larger than the expected upside" |
| 6 | Government transfers (tax rate τ) with deadweight costs (δτ) | Singularity-driven growth overwhelms deadweight costs, making even inefficient transfers effective | Para 6–7: "singularity can produce output growth so large that even grossly inefficient transfers become effective, because the resource base overwhelms the deadweight costs" |
| 7 | CRRA preferences with γ > 1 | High marginal utility in displacement states drives hedging demand and veto incentive | Para 3 (implied via displacement mechanics) and para 5: "risk-averse household" |
| 8 | Existence condition (Remark 1: infinite hedging demand when displacement is extreme) | Motivates government transfers as necessary to restore finite prices | Para 7 (implicitly): "the same explosive growth that drives the incomplete-markets problem also provides the means to overcome it" |

### Summary paragraph from introduction confirming full coverage

The introduction explicitly enumerates all three main results in its penultimate paragraph: "the paper offers three linked results: a hedging-based explanation for AI valuation premia, a rationale for resistance to AI development rooted in market incompleteness, and a mechanism through which singularity-driven growth enables effective redistribution despite frictions."

No modeling feature is orphaned (present in the model without a payoff in the introduction), and no introduction claim lacks a corresponding model feature.
