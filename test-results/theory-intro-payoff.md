# tests/theory-intro-payoff.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 53s
[ralph-garage/agent-logs/20260409T210608.980963-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260409T210608.980963-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature in the paper leads to an economic result that is discussed in the introduction.

## Detailed Findings

Each modeling feature was traced to its payoff in the introduction:

| Modeling Feature | Introduction Payoff |
|---|---|
| Market incompleteness (household cannot trade private AI capital) | "markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium" |
| Discrete singularity with displacement parameter $\phi$ | "modeling a discrete AI singularity with severe displacement" |
| Productivity boost $\eta$ | Implicit in singularity mechanism; explicit in transfers discussion ("singularity-driven growth") |
| Extinction risk $\xi$ | "Extinction risk attenuates this gap: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest" |
| AI vs non-AI stock structure ($\theta$, $\Delta\theta$) | "AI stocks grow as a share of the economy with each singularity, making them a partial hedge" |
| CRRA preferences with $\gamma > 1$ | "risk-averse household that cannot hedge displacement may rationally choose to block it" |
| Closed-form P/D ratios (Proposition 1) | "The model delivers closed-form price-dividend ratios" |
| Comparative statics (Proposition 2) | "P/D ratios for AI stocks can reach roughly six times those of non-AI stocks" |
| Veto mechanism under incomplete markets (Proposition 3) | "market incompleteness distorts the development of AI itself...rationally choose to block it---the uninsurable downside looms larger than the expected upside" |
| Positive singularity (Extension 1) | "When the positive singularity is more likely than the negative one, AI development is socially efficient" |
| Government transfers with deadweight cost $\delta\tau$ (Extension 2) | "government transfers that becomes compelling when singularity-driven growth overwhelms deadweight costs" |
| Existence condition / infinite hedge value (Remark 1) | Indirectly through the transfers and incompleteness discussion; explicitly in the model section |

No orphan modeling features were found. Every parameter and mechanism introduced in the model contributes to a result that the introduction previews for the reader.
