# tests/theory-intro-payoff.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 1m 5s
[ralph-garage/agent-logs/20260411T214322.801347-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260411T214322.801347-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature introduced in the model and extensions maps to an economic result that is previewed in the introduction.

## Detailed Findings

### Mapping of modeling features to introduction payoffs

| Modeling Feature | Where Introduced | Introduction Payoff |
|---|---|---|
| Discrete AI singularity with displacement (φ) | Section 2.1 (eq. 2) | Para 2: "investors use AI stocks to partially insure against displacement from AI" |
| Market incompleteness (restricted AI equity) | Section 2.1, Assets paragraph | Para 2: "investors cannot trade the restricted equity"; Para 4: "market incompleteness is the key driver" |
| Two assets: AI stocks (θ, Δθ) vs non-AI stocks | Section 2.1, Assets paragraph | Para 3: "P/D ratios for AI stocks roughly double relative to non-AI stocks" |
| Extinction risk (ξ) from Jones (2024) | Section 2.1, Singularity paragraph | Para 3: "extinction risk attenuates the premium" and "Proposition 2 quantifies this attenuation" |
| CRRA preferences (γ > 1, β) | Section 2.1, Preferences paragraph | Implicitly supports hedging channel and veto result; risk aversion drives both |
| Closed-form P/D ratios (Proposition 1) | Section 2.2 | Para 3: "The model delivers closed-form price-dividend ratios" with quantitative magnitudes |
| Positive singularity (probability q) and veto cost (κ) | Section 4.1 | Para 5: "risk-averse household...may rationally choose to block it—the uninsurable downside looms larger than the expected upside (Proposition 3)" |
| Government transfers (τ) with deadweight costs (δ) | Section 4.2 | Para 6–7: "Government transfers can substitute for missing markets, but standard fiscal tools are limited by deadweight costs"; "singularity can produce output growth so large that even grossly inefficient transfers become effective" |
| Existence condition (Remark 1) | Section 2.2 | Not explicitly named in the intro, but the economic consequence (infinite hedging demand motivating transfers) is covered in para 7: "the resource base overwhelms the deadweight costs." The extensions discussion ties it to the transfer mechanism. |

### Assessment

The introduction previews three linked results (para 8): "(1) a hedging-based explanation for AI valuation premia, (2) a rationale for resistance to AI development rooted in market incompleteness, and (3) a mechanism through which singularity-driven growth enables effective redistribution despite frictions." Every modeling ingredient in Sections 2–4 serves at least one of these three results, and each result is clearly flagged in the introduction before the reader encounters the formal model.

The only borderline item is the existence condition (Remark 1), which is a technical result rather than a standalone modeling feature. Its economic consequence—that displacement can be so severe that no finite price clears the market—is not explicitly named in the introduction, but it is implicitly covered by the discussion of how transfers overcome the incomplete-markets problem. Since this is a remark supporting the transfer result rather than an independent economic finding, it does not constitute a failure.
