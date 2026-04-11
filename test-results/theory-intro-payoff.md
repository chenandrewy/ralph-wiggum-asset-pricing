# tests/theory-intro-payoff.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 1m 19s
[ralph-garage/agent-logs/20260411T103039.126291-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.126291-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature in the paper leads to an economic result that is discussed in the introduction.

## Detailed Mapping

| Modeling Feature | Introduction Coverage |
|---|---|
| Discrete singularity with probability $p$ | "singularity that displaces their consumption"; quantitative results "across plausible singularity probabilities" |
| Displacement parameter $\phi$ | "shifts consumption toward AI owners"; "severe displacement" |
| Productivity jump $\eta$ | "dramatic improvement in AI productivity" |
| Market incompleteness (restricted equity) | "markets are incomplete---investors cannot trade private AI capital"; "inability to share in its upside" |
| Extinction risk $\xi$ | "Extinction risk attenuates this gap" |
| Two public assets (AI vs non-AI) with $\Delta\theta$ | "AI stocks grow as a share of the economy with each singularity, making them a partial hedge" |
| CRRA preferences ($\gamma$, $\beta$) | "risk-averse household" |
| Closed-form P/D ratios (Prop 1) | "closed-form price-dividend ratios"; "P/D ratios for AI stocks can reach roughly twice those of non-AI stocks" |
| Comparative statics (Prop 2) | All three covered: displacement severity (implicit), singularity probability ("across plausible singularity probabilities"), extinction ("attenuates") |
| Veto mechanism with cost $\kappa$ and positive singularity $q$ (Prop 3) | "risk-averse household...may rationally choose to block it"; "calls to slow or halt AI development may partly reflect investors' inability to share in its upside" |
| Government transfers $\tau$ with deadweight cost $\delta$ | "Government transfers offer an alternative"; "singularity-driven growth overwhelms deadweight costs" |
| Complete markets benchmark | "If markets were complete...the displacement-driven premium would largely vanish"; "Complete markets would eliminate this distortion" |

## Summary

The introduction systematically previews every economic result that the model produces. The three main results---the hedging-driven valuation premium (Propositions 1-2), the veto distortion under incomplete markets (Proposition 3), and the effectiveness of government transfers under explosive growth (Extension 2)---are all clearly foreshadowed. Supporting mechanisms (extinction attenuation, complete-markets benchmark, comparative statics) are also covered. No modeling feature is introduced without its payoff being signaled in the introduction.
