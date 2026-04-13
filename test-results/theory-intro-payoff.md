# tests/theory-intro-payoff.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 1m 2s
[ralph-garage/agent-logs/20260412T200023.658806-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.658806-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature maps to an economic result previewed in the introduction.

## Detailed Findings

Each modeling ingredient in the paper connects to at least one result discussed in the introduction. No orphan features exist.

### Mapping of modeling features to introduction payoffs

| Modeling Feature | Where in Model | Introduction Payoff |
|---|---|---|
| Singularity probability $p$ | Section 2.1 (Singularity) | "at a singularity probability of one percent, P/D ratios for AI stocks roughly double relative to non-AI stocks" |
| Displacement parameter $\phi$ | Eq. (2), Section 2.1 | "investors use AI stocks to partially insure against displacement from AI" |
| Market incompleteness (restricted equity) | Section 2.1 (Assets) | "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium" |
| Extinction risk $\xi$ | Section 2.1 (Singularity) | "Extinction risk partially offsets this premium: the states in which AI is powerful enough to produce enormous growth are also those in which existential risk is highest, narrowing the valuation spread" |
| Two public assets (AI vs non-AI) with $\theta$, $\Delta\theta$ | Section 2.1 (Assets) | Mechanism for the hedging channel producing the valuation spread discussed in the introduction |
| CRRA preferences with $\gamma > 1$ | Eq. (3), Section 2.1 | Drives high marginal utility in displacement states; "risk-averse household that cannot hedge displacement may rationally choose to block it" |
| Productivity boost $\eta$ | Section 2.1 (Singularity) | "singularity-driven growth overwhelms deadweight costs" |
| Positive singularity probability $q$ | Section 4.1 (Extension 1) | "When the positive singularity is more likely than the negative one, AI development is socially efficient, yet a risk-averse household...may rationally choose to block it" |
| Veto mechanism with cost $\kappa$ | Section 4.1 (Extension 1) | "Calls to slow or halt AI development may partly reflect investors' inability to hedge the downside" |
| Government transfers $\tau$ with deadweight cost $\delta$ | Section 4.2 (Extension 2) | "Government transfers can substitute for missing markets, but standard fiscal tools are limited by deadweight costs...even grossly inefficient transfers become effective, because the resource base overwhelms the deadweight costs" |

### Summary

The introduction previews four main results:
1. **AI valuation premium** from hedging under incomplete markets (driven by $p$, $\phi$, restricted equity, $\theta/\Delta\theta$, CRRA $\gamma$)
2. **Extinction attenuation** of the premium (driven by $\xi$)
3. **Veto distortion** of AI development (driven by $q$, $\kappa$, $\gamma$, incomplete markets)
4. **Government transfers effectiveness** under singularity growth (driven by $\tau$, $\delta$, $\eta$)

Every modeling feature serves at least one of these results. No feature is introduced without an economic payoff that the introduction discusses.
