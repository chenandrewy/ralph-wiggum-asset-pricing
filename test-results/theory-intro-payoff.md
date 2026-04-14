# tests/theory-intro-payoff.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 1m 10s
[ralph-garage/agent-logs/20260414T102326.825454-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260414T102326.825454-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature in the paper leads to an economic result that is discussed in the introduction.

## Detailed Findings

### Mapping of modeling features to introduction payoffs

| Modeling Feature | Intro Payoff |
|---|---|
| Incomplete markets (household cannot trade restricted AI equity) | "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium." (P2) |
| Discrete AI singularity (probability p, displacement phi, productivity eta) | "investors use AI stocks to hedge against an AI singularity that displaces their consumption" (P2); "at a singularity probability of one percent, P/D ratios for AI stocks roughly double relative to non-AI stocks" (P3) |
| Extinction risk (xi) | "Extinction risk partially offsets this premium: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest, narrowing the valuation spread" (P3) |
| AI dividend share dynamics (theta, Delta-theta) | Implicit in the hedging mechanism: AI stocks grow as a share of the economy with each singularity, making them a partial hedge (P3) |
| Positive singularity (q) and veto mechanism (kappa) | "When the positive singularity is more likely than the negative one, AI development is socially efficient, yet a risk-averse household that cannot hedge displacement may rationally choose to block it" (P4) |
| Government transfers (tau) with deadweight costs (delta) | "Government transfers can substitute for missing markets, but standard fiscal tools are limited by deadweight costs that scale with the size of transfers, making them ineffective in ordinary settings" (P5); "if a singularity produces the kind of explosive output growth...even grossly inefficient transfers become effective, because the resource base overwhelms the deadweight costs" (P6) |
| CRRA preferences (gamma, beta) | Standard preference specification; risk aversion gamma drives all results and is referenced via "risk-averse household" in P4 |

### Notes

- All three propositions (P/D ratios, extinction attenuation, veto under incomplete markets) are previewed in the introduction.
- The existence condition (Remark 1, where P/D ratios can become infinite under severe displacement) is not explicitly mentioned in the introduction, but this is a technical boundary result rather than a standalone modeling feature. It connects to the transfers discussion, which IS in the introduction.
- The wealth-heterogeneity channel (households with larger consumption shares have stronger veto incentives, discussed in Extension 1's final paragraph) is a secondary implication that goes beyond the intro's scope, but the core veto result it elaborates is fully previewed.
