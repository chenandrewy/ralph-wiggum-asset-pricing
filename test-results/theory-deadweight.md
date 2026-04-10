# tests/theory-deadweight.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 1m 47s
[ralph-garage/agent-logs/20260409T220435.838087-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T220435.838087-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper does meaningful economic or narrative work; no dead-weight formalism found.

## Audit methodology

Every formal object—equations, propositions, remarks, parameters, and defined variables—was checked against three criteria: (1) is it used in a result, calibration, or interpretation that matters for the paper's conclusions? (2) could its qualitative takeaway be stated in plain English without loss? (3) is it ceremonial or pompous?

## Formal objects reviewed

### Parameters ($\beta, g, \gamma, p, \xi, \eta, \phi, \theta, \Delta\theta, \alpha, \tau, \delta$)
All twelve parameters appear in either the P/D formulas (Proposition 1), the comparative statics (Proposition 2), the calibration table, or the extension figures. None is introduced and abandoned.

### Equation (1): Aggregate consumption growth $C_{t+1} = (1+g)C_t$
Defines $g$, which enters every P/D formula and the calibration. Minimal—one line.

### Equation (2): Displacement $\alpha_{t+1} = \phi \alpha_t$
Core mechanism. Used in Propositions 1–3, the table, and both extensions.

### Equation (3): CRRA utility
Defines the SDF that drives all pricing results. Could in principle be omitted ("CRRA with $\gamma$ and $\beta$"), but a two-line display for the utility function is standard practice and keeps the paper self-contained. Not ceremonial.

### Dividend definitions ($D_t^{AI} = \theta_t C_t$, $D_t^N = (1-\theta_t) C_t$, and $\Delta\theta$ dynamics)
Define the two assets whose valuation spread is the paper's central object of study. Essential.

### Proposition 1 (P/D ratios) and $\Gamma^{AI}$, $\Gamma^{N}$
Core result. The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are the key objects that explain *why* AI stocks trade at a premium. Both are used in Proposition 2 and the quantitative section. No dead weight.

### Remark 1 (Existence condition, $A^j < 1$)
Not decorative. It is invoked in Extension 2 to explain the infinite-P/D discontinuity at $\tau = 0$ under the large singularity—one of the paper's most striking results. Also reused in the proof of Proposition 2(iii).

### Proposition 2 (Comparative statics)
All three subparts do work:
- **(i)** Spread increasing in displacement severity: directly interpreted in the quantitative section.
- **(ii)** Spread increasing in $p$: confirmed in the table and discussed in Section 3.
- **(iii)** Spread decreasing in $\xi$: the extinction-attenuation result, discussed in the introduction, quantitative section, and veto extension.

No subpart is introduced and then abandoned.

### Proposition 3 (Veto)
Both subparts do work:
- **(i)** Veto under incomplete markets: the core Extension 1 result, connecting asset pricing to AI regulation debates.
- **(ii)** No veto under complete markets: provides the contrast that gives (i) its economic punch. Without (ii), the reader cannot see that market incompleteness—not risk aversion alone—drives the distortion.

### Equations (7)–(9): Transfer mechanism
- Equation (7) defines post-transfer consumption—used in the figure and to derive $\phi_\text{eff}$.
- Equation (8) defines $\phi_\text{eff}$, which bridges transfers back to Proposition 1's P/D formula. This is economical, not ceremonial—it avoids re-deriving the pricing formula.
- Equation (9) shows the transfer ratio is independent of $\eta$, a meaningful economic point (the ratio is constant but levels grow without bound). Used in the surrounding prose and the figure interpretation.

### Appendix proof (Proposition 1)
The Euler equation derivation is appropriately placed in the appendix. It serves double duty: it proves the closed form *and* explains the backward-recursion method used for the numerically exact values in the table.

## Potential concerns considered and dismissed

1. **Could equation (1) be omitted?** No—$g$ enters every pricing formula and the calibration.
2. **Is the existence condition (Remark 1) a detour?** No—it is load-bearing for Extension 2's infinite-P/D result.
3. **Are non-AI stocks ($D_t^N$) formal baggage?** No—the paper's entire quantitative message is the *spread* between AI and non-AI P/D ratios.
4. **Is the CRRA utility display ceremonial?** Borderline, but it is two lines and standard practice. Omitting it would save one display equation at the cost of making the paper less self-contained.
5. **Is $\phi_\text{eff}$ an unnecessary intermediate variable?** No—it economically bridges equations (7) and Proposition 1, avoiding a re-derivation.

## Summary

The paper contains 9 numbered equations, 3 propositions, 1 remark, and 12 parameters. Every one connects to either a quantitative result (table or figure), a comparative static, or the economic argument of an extension. No formal object is introduced and abandoned, no subpart is dead weight, and no formalism is pompous or ceremonial. The formalism-to-insight ratio is appropriate for a compact theory paper.
