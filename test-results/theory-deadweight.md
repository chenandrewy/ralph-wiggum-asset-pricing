# tests/theory-deadweight.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260412T202602.579578-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260412T202602.579578-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object contributes meaningfully to the paper's economic claims, quantitative analysis, or narrative arc; no dead-weight formalism was found.

## Audit methodology

Every formal object—equations, propositions, remarks, parameters, and notation—was checked against four criteria: (1) whether it is introduced and then abandoned, (2) whether its takeaway could be stated in plain English without weakening the paper's claims, (3) whether any variable or parameter goes unused in results, calibration, or interpretation, and (4) whether any formalism is pompous, ceremonial, or constitutes an auxiliary detour.

## Detailed findings

### Parameters and variables

All 13 parameters ($\beta, g, \gamma, \phi, \eta, \theta, \Delta\theta, p, \xi, q, \kappa, \tau, \delta$) are used in at least one proposition, proof, calibration table, or figure. None is introduced and abandoned. Specifically:

- **Baseline model** ($\beta, g, \gamma, \phi, \eta, \theta, \Delta\theta, p, \xi$): All appear in the P/D expressions (Proposition 1), the quantitative table, and/or Proposition 2. Each drives a distinct economic channel (discounting, growth, risk aversion, displacement severity, productivity jump, AI share dynamics, singularity probability, extinction risk).
- **Extension 1** ($q, \kappa$): Both are used in Proposition 3 and the numerical veto example. $q$ governs the positive-singularity probability; $\kappa$ is the veto cost. Neither is abandoned after introduction.
- **Extension 2** ($\tau, \delta$): Both appear in the transfer consumption equation, $\phi_\text{eff}$, the transfer ratio, and Figure 3. Neither is abandoned.

The auxiliary notation ($\Gamma^{AI}, \Gamma^{N}, A^j, \phi_\text{eff}, \alpha^+$) is similarly load-bearing: $\Gamma^{AI}$ and $\Gamma^{N}$ encode the hedging channel and are referenced throughout; $A^j$ (Remark 1) is used in the Proposition 2 proof and motivates Extension 2's discussion of infinite prices; $\phi_\text{eff}$ links transfers back to the P/D formula; $\alpha^+$ appears in the veto proof.

### Equations

| Eq. | Content | Where used |
|-----|---------|------------|
| (1) | Aggregate consumption growth | Euler equation derivation, all pricing results |
| (2) | Displacement $\alpha_{t+1} = \phi\alpha_t$ | Core mechanism; Propositions 1–3, calibration |
| (3) | AI share expansion | Drives $\Gamma^{AI} \neq \Gamma^{N}$; Proposition 1, Table 1 |
| (4) | CRRA utility | Euler equation, veto analysis |
| (5)–(6) | P/D ratio closed forms | Quantitative table, comparative statics, Extension 2 |
| (7) | Existence condition $A^j < 1$ | Proposition 2 proof, Extension 2 (infinite prices) |
| (8)–(9) | Euler equation expansion | Appendix proof of Proposition 1 |
| (10) | $\Delta u(\gamma)$ | Proof of Proposition 3 |
| (11) | Transfer consumption | Core of Extension 2, derives $\phi_\text{eff}$ |
| (12) | $\phi_\text{eff}$ | Links transfers to P/D formula; Figure 3 |
| (13) | Transfer ratio | Key insight: benefit independent of $\eta$; robustness discussion |

No equation is introduced without being used in a subsequent result, calibration, or figure.

### Propositions and Remark

- **Proposition 1** (P/D ratios): The core pricing result. Closed-form expressions are needed for the quantitative table and the $\Gamma^{AI}$ vs. $\Gamma^{N}$ comparison that drives the entire hedging argument. Cannot be replaced with plain English.
- **Remark 1** (Existence condition): Introduces $A^j < 1$, which is used in the Proposition 2 proof and is the economic linchpin of Extension 2 (the transition from infinite to finite prices under transfers). It does real narrative and analytical work.
- **Proposition 2** (Extinction attenuation): Delivers a non-obvious comparative static (extinction narrows the spread, including the *ratio*). The inline proof is one paragraph and uses the semi-elasticity argument. While the economic intuition is clear from prose, the formal statement and proof are needed because the ratio result is not obvious and the paper's quantitative table relies on it. The proof is compact enough to remain inline.
- **Proposition 3** (Veto): Both parts (incomplete vs. complete markets) do distinct economic work. Part (i) establishes that the household vetoes despite social efficiency; part (ii) shows complete markets eliminate the veto. The inline proof is necessary for the argument.

### Check for ceremonial or pompous formalism

- The "Kaldor-Hicks" efficiency definition (Section 4.1) is a standard economics label, immediately explained in plain English, and brief. It is not ceremonial—it clarifies what "socially efficient" means in this context and sets up the veto argument.
- The paper does not introduce lemmas, corollaries, or definitions beyond the three propositions and one remark. This is lean for a theory paper.
- The appendix contains only the proof of Proposition 1 (the Euler equation derivation), which is the standard location for such proofs.

### Check for auxiliary detours

No section or subsection departs from the main argument. The model setup feeds directly into the pricing results; the extensions address incompleteness consequences (veto, transfers) that are previewed in the introduction. The quantitative section illustrates the propositions without becoming a calibration exercise. The discussion subsection contextualizes the model relative to GKP (2012) and the existence condition, both of which are referenced later.

## Conclusion

The paper's formalism is well-targeted: every parameter, equation, and proposition contributes to either the economic claims, the quantitative illustrations, or the narrative arc. No formal object is introduced and abandoned, no qualitative statement could replace a formal result without weakening the paper, and no formalism is ceremonial or constitutes an auxiliary detour.
