# tests/theory-deadweight.py
Started: 2026-04-11 16:10:24 EDT
Runtime: 2m 41s
[ralph-garage/agent-logs/20260411T161024.937358-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260411T161024.937358-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, subpart, parameter, and equation in the paper contributes to an economic claim, quantitative result, or structural argument; no formalism is abandoned, ceremonial, or replaceable by plain English without weakening the paper.

## Audit of Formal Objects

### Propositions

**Proposition 1 (P/D ratios).** Core result. Produces closed-form expressions used in Table 1, the quantitative analysis, and Extension 2 (via $\phi_\text{eff}$ substitution). Indispensable.

**Proposition 2 (Extinction attenuation).** States that the valuation spread shrinks with extinction probability $\xi$. The qualitative direction is intuitive (higher $\xi$ reduces weight on non-extinction states), but the formal proof reveals a non-trivial mechanism: it requires the convexity of $A/(1-A)$ and the condition $A^j > 1/2$, which is a substantive parameter restriction that the reader cannot infer from prose alone. The result is one of the paper's "three linked results" (line 59), is verified in the quantitative table, and connects the hedging channel to the extinction literature. Retains its place.

**Proposition 3 (Veto under incomplete markets).** Core Extension 1 result.
- Part (i): Non-trivial—shows that sufficiently high risk aversion causes the household to veto even socially efficient development. Carries the extension.
- Part (ii): Trivially true (complete markets give the household $\alpha(1+\eta)C_t(1+g) > \alpha C_t(1+g)$). However, the two-line proof is the contrast that makes Part (i) meaningful—without it, the reader might attribute the veto to inherent features of the singularity rather than to market incompleteness. The subpart does narrative work despite its simplicity.

### Remark

**Remark 1 (Existence condition).** Defines $A^j < 1$ as the condition for finite P/D ratios. Referenced in Extension 2's transfer analysis and the figure caption (Exhibit 3), where it explains the infinite-P/D discontinuity. It foreshadows and motivates the entire government-transfers extension. Not ceremonial.

### Equations (numbered 1–12)

| Eq. | Content | Where used |
|-----|---------|------------|
| (1) | Aggregate consumption growth | Euler equation derivation (Appendix) |
| (2) | Displacement rule $\alpha_{t+1} = \phi\alpha_t$ | All propositions, calibration |
| (3) | CRRA utility | Pricing, veto analysis |
| (4)–(5) | P/D ratios for AI and non-AI stocks | Table 1, Extension 2 |
| (6) | Existence condition $A^j < 1$ | Extension 2, figure caption |
| (7) | Veto one-period utility gain $\Delta u(\gamma)$ | Proposition 3 proof |
| (8) | Transfer consumption $c^H_{post}$ | Extension 2, figure |
| (9) | Effective displacement $\phi_\text{eff}$ | Connects transfers to Proposition 1 |
| (10) | Transfer ratio $c^H_{post}/c^H_{no\text{-}transfer}$ | Shows $\eta$-independence of the ratio, setting up the levels argument |
| (11)–(12) | Euler equation expansion | Appendix proof of Proposition 1 |

Equation (10) is the most dispensable—the paper itself notes "the economic content is in the levels." But it is a single line that crystallizes the mechanism (the ratio is fixed, so as $\eta$ grows, levels grow without bound), and removing it would force the reader to derive the insight themselves.

### Parameters and Variables

Every parameter ($g, \beta, \gamma, p, \xi, \eta, \phi, \theta, \Delta\theta, \alpha, q, \kappa, \tau, \delta$) appears in at least one result, calibration, or figure. No parameter is introduced and abandoned.

- $q$ and $\kappa$: scoped to Extension 1, both appear in Proposition 3 and the numerical example.
- $\tau$ and $\delta$: scoped to Extension 2, both appear in the transfer formulas and Figure 3.
- $\Gamma^{AI}$ and $\Gamma^{N}$: defined in Proposition 1 and discussed economically in the paragraph that follows (line 155), explaining the hedging channel via differential dividend growth.

### AI owners' consumption $(1-\alpha_t)C_t$

Mentioned once in the setup (line 86) and not analyzed further. This is a model accounting identity (where does the rest of consumption go?), not a formal object. It takes half a sentence and is needed for the model to be well-defined.

### Kaldor-Hicks efficiency definition

Stated in prose in Extension 1 (line 204). Holds trivially when $\eta > 0$, and the paper says so explicitly. This is a definition, not a formal result, and it correctly avoids dressing up a trivial condition as a proposition.

## Summary

The paper has 3 propositions, 1 remark, and 12 numbered equations across ~20 pages. For a theory paper in asset pricing, this is lean. Each formal object satisfies at least one of: (a) delivers a non-obvious economic result, (b) provides closed-form expressions used in quantitative analysis, or (c) connects model components across sections (e.g., $\phi_\text{eff}$ linking transfers back to Proposition 1). No formalism is introduced and abandoned, no parameter goes unused, and no result could be replaced by prose without losing either quantitative content or structural rigor.
