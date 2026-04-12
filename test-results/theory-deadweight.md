# tests/theory-deadweight.py
Started: 2026-04-12 09:46:31 EDT
Runtime: 1m 54s
[ralph-garage/agent-logs/20260412T094631.065298-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260412T094631.065298-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to an economic claim, calibration, or narrative argument; no formalism is introduced and abandoned, ceremonial, or replaceable by plain English without losing precision.

## Audit Details

### Formal Inventory

**Parameters (all used):**
- $C_t$, $g$: aggregate consumption and growth — used in setup, P/D formulas, calibration, extensions.
- $\alpha_t$, $\phi$: household share and displacement — used in P/D formulas, calibration, veto proposition, transfers.
- $p$, $\xi$, $\eta$: singularity probability, extinction probability, productivity boost — used in P/D formulas, Prop 2, calibration table, extensions.
- $\theta_t$, $\Delta\theta$: AI dividend share and jump — used in P/D formulas, dividend growth factors, calibration.
- $\gamma$, $\beta$: risk aversion and discount factor — used in utility, P/D formulas, veto threshold, calibration.
- $q$: positive singularity probability (Extension 1) — used in Prop 3 and numerical example.
- $\kappa$: veto cost (Extension 1) — used in Prop 3.
- $\tau$, $\delta$: tax rate and deadweight cost (Extension 2) — used in transfer equations and figure.
- $\phi_\text{eff}$: effective displacement (Extension 2) — bridges transfers to the P/D formula from Prop 1.
- $\Gamma^{AI}$, $\Gamma^{N}$: dividend growth factors — used in P/D formulas, Prop 2, and discussion of hedging channel.
- $A^j$: SDF-weighted growth (Remark 1) — used in Prop 2 proof and Extension 2 existence discussion.

**Propositions:**
1. **Prop 1 (P/D ratios):** Core result. Delivers closed-form P/D ratios used in calibration (Table 1), discussion, and Extension 2 (via $\phi_\text{eff}$ substitution).
2. **Prop 2 (Extinction attenuation):** Comparative static on $\xi$. Substantive: shows extinction partially offsets the hedging premium. Used in calibration discussion and connects to Jones (2024).
3. **Prop 3 (Veto under incomplete markets):** Shows market incompleteness distorts real decisions, not just prices. Both parts (incomplete vs. complete markets) are essential for the paper's thesis. Numerical example sharpens the point.

**Remark 1 (Existence condition):** Identifies when P/D ratios are infinite. Not ceremonial — referenced substantively in Extension 2, where the large-singularity parameterization violates the condition and transfers restore it. The remark number makes it easy to cross-reference.

**Display equations (all contribute):**
- eq:agg-consumption-growth: basic setup, referenced implicitly throughout.
- eq:displacement: defines $\phi$, the paper's central displacement mechanism.
- eq:utility: standard CRRA specification, underpins Euler equation and veto analysis.
- eq:pd-ai, eq:pd-nonai: Prop 1 results, used in calibration and extensions.
- eq:existence: Remark 1, referenced in Extension 2.
- eq:veto-delta-u: Prop 3 proof, shows why risk aversion drives the veto.
- eq:transfer-consumption: Extension 2, defines the transfer mechanism.
- eq:phi-eff: bridges transfers to baseline P/D formula — not just algebra, but shows the economic connection.
- eq:transfer-ratio: shows consumption improvement is independent of $\eta$ — a non-obvious fact that supports the "abundance overwhelms deadweight costs" argument. Prose alone would lose this precision.
- eq:euler, eq:euler-expand, eq:pd-ai-solve: appendix proof steps for Prop 1.

### Checks Against Criteria

**1. Formalism introduced and then abandoned?**
No. Every parameter, proposition, and equation is referenced in at least one of: a later result, the calibration, the figure, or the discussion. No formal object is orphaned.

**2. Could any formal object's takeaway be stated in plain English without weakening the claims?**
No. The key results (P/D ratios, extinction attenuation, veto threshold, transfer effectiveness) involve specific quantitative relationships that cannot be stated in prose without losing the precision needed for calibration and cross-referencing. For example, eq:transfer-ratio's independence from $\eta$ is a specific mathematical fact that drives the paper's policy argument.

**3. Variables introduced and unused in any result, calibration, or interpretation?**
No. Every variable appears in at least one proposition, calibration value, or figure parameterization.

**4. Pompous or ceremonial formalism? Auxiliary formal detours?**
No. The paper is lean. There are no lemmas-for-the-sake-of-lemmas, no unnecessary generality, no detours into mathematical machinery that doesn't serve the economic argument. The Prop 2 proof is the most technical piece, but it proves a non-trivial claim (the P/D *ratio* decreases in $\xi$) that is used in the calibration discussion.
