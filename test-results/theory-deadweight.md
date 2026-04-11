# tests/theory-deadweight.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 2m 16s
[ralph-garage/agent-logs/20260411T101504.830354-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260411T101504.830354-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation earns its place through use in a result, calibration, or economic interpretation.

## Detailed Audit

### Formal Objects Inventory

| Object | Purpose | Used In |
|--------|---------|---------|
| Eq (1): $C_{t+1}=(1+g)C_t$ | Defines deterministic growth | Euler equation, all P/D formulas |
| Eq (2): $\alpha_{t+1}=\phi\alpha_t$ | Displacement mechanism | Core of hedging channel, SDF |
| Eq (3): CRRA utility | Preferences | SDF derivation, veto proof |
| Prop 1 + Eqs (4)-(5) | Closed-form P/D ratios | Table 1 calibration, Extension 2 |
| Remark 1 + Eq (6) | Existence condition $A^j<1$ | Extension 2 (infinite P/D at $\tau=0$), Prop 2(iii) proof |
| Prop 2 (i)-(iii) | Comparative statics | Interprets Table 1 patterns directly |
| Prop 3 + Eq (7) | Veto under incomplete markets | Extension 1 main result |
| Eq (8) | Post-transfer consumption | Extension 2 setup, feeds Eq (9) |
| Eq (9): $\phi_\text{eff}$ | Effective displacement | Connects transfers to Prop 1 formula |
| Eq (10) | Transfer ratio independent of $\eta$ | Key insight: explosive growth overwhelms deadweight costs |
| Appendix Eqs (11)-(14) | Full Euler equation proof | Proves Proposition 1 |

### Parameters Check

Every parameter introduced is used in at least one result, calibration value, or figure:

- $\beta, g, \gamma, \phi, \eta, \theta, \Delta\theta, p, \xi$: All appear in the P/D formulas (Prop 1) and the calibration table
- $\Gamma^{AI}, \Gamma^{N}$: Carry the key economic content (hedging channel comparison) and appear in comparative statics
- $q$: Probability of positive singularity — used in Prop 3 proof (Eq 7) and numerical example
- $\kappa$: Veto cost — used in Prop 3 statement and numerical example (1% of permanent consumption)
- $\tau, \delta$: Tax rate and deadweight cost — used in Eqs (8)-(10) and the two-panel figure
- $\alpha$: Household's consumption share — used in veto numerical example and transfer formula
- $\alpha^+ = \min(1, \alpha/\phi)$: Positive singularity share — used in Prop 3 proof

### Checks for Dead Weight

**Introduced and abandoned?** No. Every formal object introduced in the setup or extensions is referenced in at least one downstream result. The $\Gamma$ growth factors, the existence condition $A^j$, and $\phi_\text{eff}$ all reappear where needed.

**Could any formal object be replaced by plain English?** The comparative statics in Proposition 2 are directional claims that could in principle be stated informally, but the proof of part (iii) — using convexity of $A/(1-A)$ — reveals a non-obvious mechanism (why extinction compresses the *ratio*, not just the levels). The transfer ratio in Eq (10) delivers a non-trivial insight (independence from $\eta$) that requires the algebra. The P/D closed forms are the paper's main analytical contribution and cannot be replaced by prose.

**Unused variables?** None found. All parameters map to calibration values or figure axes.

**Pompous or ceremonial formalism?** The "Kaldor-Hicks" label for social efficiency is the closest candidate, but it serves a precise purpose: it clarifies that efficiency is defined by aggregate surplus, not Pareto improvement, which matters for the veto result. The condition is trivially satisfied ($\eta > 0$), but the label anchors the welfare comparison. No auxiliary lemmas, no detour propositions, no notation introduced for its own sake.

**Auxiliary formal detours?** None. The paper moves linearly: setup → pricing → calibration → extensions. Each extension branches from the baseline without building intermediate machinery.

### Overall Assessment

The formalism is lean and functional. The paper introduces exactly the machinery needed for its three propositions, one remark, and one quantitative figure, with no residual notation or abandoned threads.
