# tests/theory-deadweight.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260412T154740.738942-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.738942-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation contributes to economic claims, quantitative analysis, or necessary proofs; no abandoned, ceremonial, or deadweight formalism found.

## Audit methodology

Checked every parameter, variable, equation, proposition, remark, and proof in `paper/paper.tex` against four criteria: (1) introduced then abandoned, (2) replaceable by plain English without weakening claims, (3) unused in any result/calibration/interpretation, (4) pompous or ceremonial.

## Parameters and variables

All parameters appear in results, calibrations, or both:

| Parameter | Introduced | Used in |
|-----------|-----------|---------|
| $g, \beta, \gamma$ | Setup (§2.1) | P/D formulas, calibration table, veto proof, transfer analysis |
| $p, \xi$ | Singularity (§2.1) | P/D formulas, Prop 2, calibration, veto numerics |
| $\eta, \phi$ | Singularity (§2.1) | P/D formulas, calibration, displacement severity, transfer equation |
| $\alpha_t$ | Consumption (§2.1) | Veto analysis, transfer equation, $\phi_\text{eff}$ |
| $\theta_t, \Delta\theta$ | Assets (§2.1) | $\Gamma^{AI}$, $\Gamma^N$ factors, calibration, approximation discussion |
| $\Gamma^{AI}, \Gamma^N$ | Prop 1 (§2.2) | Key economic comparison (hedging channel), Prop 2 proof |
| $q$ | Extension 1 (§4.1) | Veto proposition, numerical example |
| $\kappa$ | Extension 1 (§4.1) | Veto proposition (both parts), numerical example |
| $\tau, \delta$ | Extension 2 (§4.2) | Transfer consumption, $\phi_\text{eff}$, transfer ratio, figure |
| $\phi_\text{eff}$ | Extension 2 (§4.2) | Bridges transfers to baseline P/D formula |
| $A^j$ | Remark 1 (§2.2) | Existence condition, Prop 2 proof, Extension 2 discussion |

No parameter is introduced and then abandoned. No variable is unused in downstream results.

## Equations

| Equation | Role | Deadweight? |
|----------|------|-------------|
| (1) Agg consumption growth | Defines $g$ notation | Borderline—could be prose—but standard in asset pricing and sets up notation used in proofs. No. |
| (2) Displacement | Defines core mechanism ($\phi$) | Essential. No. |
| (3) Utility | Establishes CRRA preferences | Required for SDF derivation. No. |
| (4)–(5) P/D ratios | Core results | Essential—drive Table 1, Prop 2, extension analysis. No. |
| (6) Existence condition | Defines $A^j < 1$ | Referenced in Extension 2 (infinite prices at $\tau=0$), figure caption. Does real work. No. |
| (7) Veto $\Delta u$ | Used in Prop 3 proof | Necessary for the proof. No. |
| (8) Transfer consumption | Defines transfer mechanism | Essential for Extension 2. No. |
| (9) $\phi_\text{eff}$ | Connects transfers to P/D | Key bridging result. No. |
| (10) Transfer ratio | Shows $\eta$-independence | Delivers economic insight (transfers always help regardless of $\eta$). No. |
| (11)–(13) Euler expansion (Appendix) | Proof of Prop 1 | Required by spec (explicit proofs). No. |

## Propositions and proofs

- **Proposition 1 (P/D ratios)**: Core result. Proof in appendix as required.
- **Remark 1 (existence condition)**: Not ceremonial—it motivates Extension 2's infinite-price result and is referenced in the figure caption and discussion.
- **Proposition 2 (extinction attenuation)**: Delivers a non-obvious comparative static. The inline proof is somewhat technical (convexity/semi-elasticity argument) but provides genuine insight into *why* the ratio decreases, not just that it does. The proof is self-contained and not excessively long.
- **Proposition 3 (veto)**: Both parts do economic work. Part (i) shows incompleteness distorts real decisions. Part (ii) provides the key contrast: complete markets eliminate the veto. Neither part is ceremonial.

## Potential borderline items examined

1. **Equation (1)**: $C_{t+1} = (1+g)C_t$ is a display equation for constant growth, which could be stated in prose. However, it's brief, standard in asset pricing, and the spec requires numbered display equations. Not deadweight.

2. **Kaldor-Hicks efficiency paragraph** (§4.1): Names a well-known economic concept for a trivially true observation ($\eta > 0$ implies surplus is positive). But the naming does narrative work: it establishes that the problem is distributional, not allocative, which is the entire point of the extensions.

3. **AI owners' consumption share $(1-\alpha_t)C_t$**: Introduced once in setup, later appears implicitly in the transfer equation as $(1-\phi\alpha)$. Not abandoned.

4. **The $\min(1, \alpha/\phi)$ detail** in the positive singularity: A small technical bound, but necessary to prevent $\alpha > 1$. Not ceremonial—it's a one-token fix for a real issue.

## Conclusion

The paper is lean. Each formal object contributes to either (a) the core pricing results and their calibration, (b) the extension arguments about veto and transfers, or (c) necessary proofs. No formalism is introduced and abandoned. No auxiliary formal detour is present. The formal apparatus is proportionate to the economic claims.
