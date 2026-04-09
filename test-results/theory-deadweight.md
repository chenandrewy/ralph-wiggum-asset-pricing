# tests/theory-deadweight.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 1m 42s
[ralph-garage/agent-logs/20260409T190308.202000-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T190308.202000-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to an economic claim, quantitative result, or narrative mechanism; no deadweight formalism was found.

## Audit methodology

Every formal object was catalogued and checked against four criteria: (1) is it introduced and then abandoned? (2) could its takeaway be stated in plain English without weakening economic claims? (3) is any variable/parameter unused in results, calibration, or interpretation? (4) is any formalism pompous, ceremonial, or a detour from the main argument?

## Parameters (16 total)

| Parameter | Where introduced | Where used | Verdict |
|-----------|-----------------|------------|---------|
| $C_t$ | Setup (Sec 2.1) | All derivations, calibration | Essential |
| $g$ | eq:agg-consumption-growth | P/D formulas, calibration ($g=0.02$) | Essential |
| $\alpha_t$ | Setup | Defines household consumption; displacement mechanism via $\phi$ | Essential |
| $\theta_t$ | Assets paragraph | Defines dividends; enters $\Gamma^{AI}$, $\Gamma^N$; calibrated ($\theta=0.15$) | Essential |
| $p$ | Singularity paragraph | P/D formulas, comparative statics (Prop 2(ii)), calibration grid | Essential |
| $\xi$ | Singularity paragraph | P/D formulas, comparative statics (Prop 2(iii)), calibration grid | Essential |
| $\eta$ | Singularity paragraph | P/D formulas, calibration ($\eta=0.5$, $\eta=9$), transfer analysis | Essential |
| $\phi$ | eq:displacement | P/D formulas, comparative statics (Prop 2(i)), calibration ($\phi=0.5$, $\phi=0.05$) | Essential |
| $\Delta\theta$ | Assets paragraph | $\Gamma^{AI}$, $\Gamma^N$; Corollary 1; calibrated ($\Delta\theta=0.2$) | Essential |
| $\gamma$ | Preferences | P/D formulas, Prop 2(ii), Prop 3(i); calibrated ($\gamma=4$) | Essential |
| $\beta$ | Preferences | P/D formulas; calibrated ($\beta=0.96$) | Essential |
| $\lambda$ | Extension 1 | Prop 3; governs positive vs negative singularity | Essential |
| $\phi^+$ | Extension 1 | Prop 3; positive singularity share gain | Essential |
| $\kappa$ | Extension 1 | Veto cost in Prop 3 | Essential |
| $\tau$ | Extension 2 | Transfer consumption (eq 7), transfer ratio (eq 8), figure | Essential |
| $\delta_0$ | Extension 2 | Deadweight cost in eqs 7-8, figure | Essential |

No parameter is introduced and then abandoned. All 16 appear in at least one result, calibration exercise, or figure.

## Equations (11 total, including appendix)

1. **eq:agg-consumption-growth** ($C_{t+1}=(1+g)C_t$): Foundation of the consumption process. Used in all derivations.
2. **eq:displacement** ($\alpha_{t+1}=\phi\alpha_t$): Core mechanism. Enters P/D formulas through $\phi^{-\gamma}$.
3. **eq:utility** (CRRA): Defines preferences. Generates the SDF used in all pricing.
4. **eq:pd-ai**: Core quantitative result. Used in Table 1, Figure 2, Propositions 1-2.
5. **eq:pd-nonai**: Companion to eq 4. Used in Table 1, Corollary 1, Proposition 2.
6. **eq:veto-gain** ($\Delta U^H$): States the veto condition precisely. Used in Proposition 3.
7. **eq:transfer-consumption**: Defines the transfer mechanism. Basis for eq 8 and Figure 2.
8. **eq:transfer-ratio**: Delivers the key insight that the consumption ratio is independent of $\eta$. Discussed in text and illustrated in Figure 2.
9-11. **Appendix eqs** (Euler equation, expansion, solution): Required by the spec ("all propositions are explicitly proved, with long proofs in the appendix"). These constitute the proof of Proposition 1.

No equation is ornamental. Each either states a result, defines a mechanism, or proves a claim.

## Propositions and corollary

- **Proposition 1** (P/D ratios): Core result driving the entire quantitative analysis.
- **Corollary 1** (valuation spread): Direct implication but highlights the paper's central prediction. Short (3 lines) and provides a clean reference point for the discussion.
- **Proposition 2** (comparative statics): All three parts are verified quantitatively in Section 3 and referenced in the discussion of Table 1.
- **Proposition 3** (veto): Delivers the extension's main result about how incompleteness distorts AI development.

## Items examined for potential deadweight

1. **Corollary 1**: Could be folded into prose after Proposition 1. However, it isolates the paper's central empirical prediction in a citable result, which is standard in finance theory papers. At 3 lines including the proof, the overhead is negligible.

2. **eq:veto-gain in Proposition 3**: The proof of Proposition 3 is qualitative ("for $\gamma$ sufficiently large, the downside dominates"). One could ask whether the explicit formula adds value beyond the verbal argument. However, the formula makes the veto condition precise and verifiable, and it clarifies the role of extinction normalization ($u_\text{ext}=0$). This is standard practice for stating a formal result.

3. **Private AI capital dividends** ($(1-\alpha_t)C_t - D_t^{AI}$): Stated once in the setup as a definitional aside. Not used in any equation or proof. However, it serves a necessary narrative function: it explains what AI owners receive and why the household cannot trade this residual. One line of text, not a formal object.

4. **Domain restriction $\alpha_t \in (0, 1-\theta_t]$**: Stated once, never binding in any result. But this is a standard modeling boundary condition ensuring the household cannot consume more than is available after AI dividends. Not formalism — just a well-posedness condition.

## Conclusion

The paper is lean. Every parameter appears in at least one result or calibration. Every equation either states a core result, defines a mechanism, or proves a proposition. No formal object is introduced and then abandoned. No qualitative takeaway could be stated in plain English in a way that would eliminate an equation without weakening the paper's claims. The formalism is purposeful and proportionate to the economic content.
