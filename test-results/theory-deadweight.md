# tests/theory-deadweight.py
Started: 2026-04-14 10:33:09 EDT
Runtime: 1m 47s
[ralph-garage/agent-logs/20260414T103309.987276-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260414T103309.987276-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to an economic claim, calibration, or cross-reference; no deadweight formalism was found.

## Audit Details

### Catalog of Formal Objects

| Object | Purpose | Used In |
|--------|---------|---------|
| Eq (1): $C_{t+1}=(1+g)C_t$ | Aggregate growth | Foundation for all P/D derivations |
| Eq (2): $\alpha_{t+1}=\phi\alpha_t$ | Displacement | Central mechanism; drives SDF wedge |
| Eq (3): $\theta$ update | AI share expansion | Drives $\Gamma^{AI}\neq\Gamma^N$ |
| Eq (4): CRRA utility | Preferences | SDF derivation, veto proof |
| Prop 1 / Eqs (5)-(6): P/D ratios | Main pricing result | Table 1, Extensions, Appendix |
| Remark 1 / Eq (7): Existence condition | Finite-price boundary | Extension 2 (infinite P/D at $\tau=0$) |
| Prop 2: Extinction attenuation | Comparative static | Table 1 patterns, Discussion |
| Prop 3 / Eq (8): Veto | Real distortion from incompleteness | Extension 1 core result |
| Eq (9): Transfer consumption | Post-transfer household consumption | Extension 2 setup |
| Eq (10): $\phi_\text{eff}$ | Effective displacement under transfers | Connects transfers back to Prop 1 |
| Eq (11): Transfer ratio | $\eta$-independence of consumption multiple | Key economic insight of Extension 2 |
| Appendix Eqs (12)-(14) | Euler equation derivation | Proof of Prop 1 |

### Parameters

Every parameter is used in at least one result, calibration, or economic interpretation:

- **$g, \beta$**: Growth and discounting — enter all P/D expressions and calibration.
- **$\gamma$**: Risk aversion — enters SDF, drives veto threshold in Prop 3, calibrated.
- **$p$**: Singularity probability — P/D grid variable in Table 1.
- **$\xi$**: Extinction probability — P/D grid variable, Prop 2 comparative static.
- **$\eta$**: Productivity jump — enters $\Gamma$ factors, calibrated, central to Extension 2.
- **$\phi$**: Displacement severity — enters SDF via $\phi^{-\gamma}$, calibrated, veto condition.
- **$\theta, \Delta\theta$**: AI dividend share and jump — define $\Gamma^{AI}$ vs $\Gamma^N$, calibrated.
- **$q$**: Positive singularity probability — Extension 1, enters veto proof.
- **$\kappa$**: Veto cost — Extension 1, quantitative example.
- **$\tau$**: Tax rate — Extension 2, Figure 3 x-axis.
- **$\delta$**: Deadweight cost parameter — Extension 2, calibrated and stress-tested.

### Checks Against Audit Criteria

**Introduced and abandoned?** No. Every formal object is referenced after introduction — either in a later result, a calibration, a figure, or a cross-section discussion. The existence condition (Remark 1) has the longest gap between introduction and use (Section 2 to Section 4.2), but it is explicitly invoked in the Extension 2 discussion and figure caption.

**Could the takeaway be stated in plain English?** Propositions 1-3 all have prose interpretations immediately following them, but the formal statements add precision that the prose alone would lack. For example, Prop 2's claim that the spread is "decreasing in $\xi$" is tighter than "extinction risk reduces the premium." The P/D closed forms enable the quantitative analysis in Table 1. The veto threshold $\bar{\gamma}$ in Prop 3 makes precise an otherwise vague claim about risk aversion. Removing any of these would weaken the paper's economic claims.

**Unused variables?** No. All parameters appear in results or calibrations that matter for the paper's conclusions.

**Pompous or ceremonial formalism?** No. The paper avoids theorem-environment inflation (only three propositions and one remark across the entire paper). Proofs are compact — Prop 2's proof is three lines inline, Prop 3's proof is one paragraph, and only Prop 1's proof is relegated to the appendix. No lemmas, corollaries, or definitions are introduced.

**Auxiliary formal detours?** No. The paper proceeds linearly: setup → pricing → quantitative analysis → extensions. Each section builds on the previous one. There are no side results or tangential formalizations.
