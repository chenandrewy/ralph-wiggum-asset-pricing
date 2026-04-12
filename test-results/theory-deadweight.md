# tests/theory-deadweight.py
Started: 2026-04-11 21:27:07 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260411T212707.757734-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260411T212707.757734-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to quantitative results, economic intuition, or narrative progression; no deadweight formalism was found.

## Audit methodology

Every formal object was checked against four criteria: (1) introduced and then abandoned or doing no economic/narrative work, (2) qualitative takeaway statable in plain English without weakening claims, (3) variables/parameters introduced but unused in any result, calibration, or interpretation, (4) pompous or ceremonial formalism or auxiliary detours.

## Catalog of formal objects

### Parameters and variables
| Symbol | Where introduced | Where used | Verdict |
|--------|-----------------|------------|---------|
| $C_t$ (aggregate consumption) | Sec 2.1 | Throughout model, calibration, extensions | Active |
| $g$ (growth rate) | Sec 2.1 | P/D formulas, calibration table, extensions | Active |
| $\alpha_t$ (household share) | Sec 2.1 | Displacement, veto (Prop 3), transfers (Ext 2) | Active |
| $p$ (singularity prob) | Sec 2.1 | P/D formulas, calibration grid, veto, figure | Active |
| $\xi$ (extinction prob) | Sec 2.1 | P/D formulas, Prop 2, calibration grid | Active |
| $\eta$ (productivity jump) | Sec 2.1 | P/D formulas, calibration, transfer analysis | Active |
| $\phi$ (displacement) | Sec 2.1 | Central to all results | Active |
| $\theta_t, \Delta\theta$ (dividend shares) | Sec 2.1 | $\Gamma$ factors, P/D formulas, calibration | Active |
| $\gamma$ (risk aversion) | Sec 2.1 | P/D formulas, veto threshold, calibration | Active |
| $\beta$ (discount factor) | Sec 2.1 | P/D formulas, calibration | Active |
| $\Gamma^{AI}, \Gamma^{N}$ (dividend growth factors) | Prop 1 | P/D comparison, Prop 2 proof, discussion | Active |
| $q$ (positive singularity prob) | Sec 4.1 | Prop 3 proof, numerical example | Active |
| $\kappa$ (veto cost) | Sec 4.1 | Prop 3, numerical example | Active |
| $\tau$ (tax rate) | Sec 4.2 | Transfer equation, $\phi_\text{eff}$, figure | Active |
| $\delta$ (deadweight cost) | Sec 4.2 | Transfer equation, figure | Active |
| $\phi_\text{eff}$ (effective displacement) | Sec 4.2 | Bridges transfers to P/D formula, figure | Active |

No variable or parameter is introduced and then abandoned. Every symbol appears in at least one result, calibration, or figure.

### Displayed equations (numbered)
1. **Eq (1)**: Aggregate consumption growth — used in Euler equation derivation (Appendix), establishes baseline dynamics.
2. **Eq (2)**: Displacement equation — central mechanism, used in all results.
3. **Eq (3)**: CRRA utility — standard, grounds Euler equation and risk aversion.
4. **Eqs (4)–(5)**: P/D ratios — the paper's main quantitative result, used in Table 1 and Figure 3.
5. **Eq (6)**: Existence condition — used in Remark 1, referenced in Extension 2 (infinite-price phenomenon in Figure 3).
6. **Eq (7)**: One-period utility gain $\Delta u(\gamma)$ — used in Prop 3(i) proof.
7. **Eq (8)**: Post-transfer consumption — core of Extension 2, used to derive $\phi_\text{eff}$.
8. **Eq (9)**: Effective displacement $\phi_\text{eff}$ — connects transfers to P/D formula, used in Figure 3.
9. **Eq (10)**: Transfer ratio — shows $\eta$-independence, supports the "singularity overwhelms deadweight costs" argument.
10. **Eqs (11)–(13)**: Appendix derivation — required proof of Prop 1.

No equation is ceremonial or disconnected from downstream results.

### Propositions and remarks
- **Proposition 1** (P/D ratios): Delivers the closed-form expressions used in Table 1. Essential.
- **Remark 1** (existence condition): Introduced in Sec 2 and pays off in Extension 2, where the infinite-price phenomenon motivates transfers. Not a dead end.
- **Proposition 2** (extinction attenuation): Comparative statics result verified in the calibration table. The inline proof is compact and the convexity argument ($f(A) = A/(1-A)$, $f'' > 0$) is needed to go from "larger absolute reduction in $A^{AI}$" to "larger proportional reduction in P/D ratio" — this step is non-trivial and cannot be replaced by plain English without weakening the claim.
- **Proposition 3** (veto): Advances the paper's argument about real distortions from incomplete markets. Both parts (incomplete vs. complete markets) are needed for the contrast. The numerical example makes the result concrete.

### Structural check: Could any formal object be replaced by plain English?

- The P/D formulas (Prop 1) cannot — they deliver quantitative magnitudes used in the calibration table.
- The $\Gamma^{AI}$ vs. $\Gamma^{N}$ comparison cannot — the formal expressions are needed to see *why* AI stocks command a premium (differential dividend growth interacting with the SDF).
- The existence condition cannot — it is used quantitatively in Figure 3 (the infinite-price region).
- The veto threshold cannot — the limit argument as $\gamma \to \infty$ is the proof mechanism.
- The transfer ratio (Eq 10) is the closest candidate, since its main point ("the ratio is $\eta$-independent") could be stated verbally. But the equation is one line and immediately supports the economic interpretation in the next sentence. The formalism is minimal and clarifying, not ceremonial.

### Check for auxiliary detours

The paper has no formal sections or derivations that fail to connect to one of its three main results (hedging premium, veto distortion, transfer effectiveness). Each extension branches from the baseline and contributes a distinct economic point. No formal "aside" or tangential model variant is introduced.

## Conclusion

The paper's formalism is lean and functional. Every parameter, equation, proposition, and remark contributes to either (a) a quantitative result shown in a table or figure, (b) an economic mechanism discussed in prose, or (c) a later section of the paper. No formal object is introduced and abandoned, no result can be replaced by plain English without losing economic content, and no auxiliary detour or ceremonial formalism was found.
