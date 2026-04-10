# tests/theory-deadweight.py
Started: 2026-04-09 20:07:38 EDT
Runtime: 2m 20s
[ralph-garage/agent-logs/20260409T200738.675415-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T200738.675415-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation performs economic or narrative work; no deadweight formalism found.

## Audit Method

Checked every formal object (3 propositions, 1 corollary, 1 remark, 8 numbered equations), every parameter, and every prose mechanism for: (a) introduced-then-abandoned formalism, (b) results statable in plain English without loss, (c) unused variables/parameters, (d) pompous or ceremonial formalism, and (e) auxiliary formal detours.

## Detailed Findings

### Parameters — All Used

| Parameter | Introduced | Used in |
|-----------|-----------|---------|
| $g$ | Eq (1) | P/D formulas, calibration |
| $\alpha_t$ | Setup | Displacement eq (2), Extension 2 eqs (7)–(8), calibration |
| $\phi$ | Eq (2) | P/D formulas, comparative statics, calibration, Extension 2 |
| $p, \xi$ | Setup | P/D formulas, comparative statics, calibration |
| $\eta$ | Setup | P/D formulas, calibration, Extension 2 |
| $\theta, \Delta\theta$ | Setup | $\Gamma^{AI}, \Gamma^{N}$, P/D formulas, calibration |
| $\gamma, \beta$ | Eq (3) | P/D formulas, comparative statics, calibration |
| $\lambda$ | Extension 1 | Proposition 3 (qualitative, as appropriate for the claim) |
| $\tau, \delta$ | Extension 2 | Eqs (7)–(8), figure, policy discussion |
| $\phi_{\text{eff}}$ | Extension 2 | Connects transfers back to Proposition 1 |

Note: $\alpha_t$ cancels out of the baseline P/D formulas (since the SDF depends on consumption *growth*), but this is a natural consequence of the model, not deadweight. It re-enters substantively in Extension 2 where the *level* of household consumption matters for transfers.

### Formal Environments — All Earn Their Keep

- **Proposition 1 (P/D ratios):** Central result. Closed-form pricing formulas used in calibration, comparative statics, and Extension 2.
- **Remark 1 (existence condition):** Defines when P/D ratios are well-defined. Directly motivates Extension 2's discussion of infinite P/D under severe displacement and the role of transfers in restoring finite prices.
- **Corollary 1 (valuation spread):** States the paper's main economic claim: AI stocks trade at higher P/D than non-AI stocks. While the result follows quickly from Proposition 1, formalizing the paper's central qualitative prediction as a numbered result is standard practice in asset pricing theory and serves a clear signposting function. Not ceremonial.
- **Proposition 2 (comparative statics):** All three parts do work. Part (i) connects to calibration (displacement severity). Part (ii) has a non-trivial qualification ("$\gamma$ sufficiently large"). Part (iii) is the extinction-attenuation result, highlighted as a contribution distinct from standard displacement models.
- **Proposition 3 (veto):** Extension 1's main result. The qualitative proof style matches the qualitative claim. Both parts (incomplete vs. complete markets) are needed to make the argument.

### Equations — All Perform Work

- **Eq (1):** Consumption growth. Standard one-line setup equation. Establishes notation for the P/D derivation.
- **Eq (2):** Displacement. Key mechanism equation.
- **Eq (3):** CRRA utility. Defines preferences and the SDF.
- **Eqs (4)–(5):** P/D ratio formulas. Central results.
- **Eq (6):** Existence condition. Used substantively in Extension 2 (infinite P/D discussion).
- **Eq (7):** Post-transfer consumption. Extension 2 mechanism.
- **Eq (8):** Transfer ratio. Reveals a non-obvious property ($\eta$-independence of the ratio) that supports the argument about singularity-driven growth overwhelming deadweight costs.

### Prose Mechanisms — No Detours

- The discussion section (2.3) contextualizes relative to GKP and Jones without introducing new formalism.
- The quantitative section (3) interprets the calibration without introducing new formal objects.
- Extension discussions stay within the formal apparatus already established.

### Minor Observations (Not Failures)

- The upper bound $\alpha_t \in (0, 1-\theta_t]$ is an inline consistency constraint that is never referenced again. This is a standard modeling annotation, not deadweight formalism.
- Private AI capital dividends $(1-\alpha_t)C_t - D_t^{AI}$ appear inline to explain the source of market incompleteness; the expression is never used in any derivation. This is explanatory prose rather than formalism.

Neither rises to the level of "abandoned" or "ceremonial" formalism.
