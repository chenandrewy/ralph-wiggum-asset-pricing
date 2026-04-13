# tests/theory-deadweight.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 2m 17s
[ralph-garage/agent-logs/20260412T200023.655364-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.655364-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper serves at least one result, calibration, or economic interpretation; no formalism is introduced and abandoned, ceremonial, or replaceable by plain English without weakening the paper's claims.

## Detailed Audit

### Parameters and Variables
All parameters and variables are used in at least one proposition, calibration (Table 1), or figure:

- **Baseline model**: $g, \beta, \gamma, p, \xi, \eta, \phi, \theta, \Delta\theta, \alpha_t$ — all appear in the P/D formulas (Prop 1) and the quantitative table.
- **Extension 1**: $q$ (positive singularity probability), $\kappa$ (veto cost), $\alpha^+$ (post-positive share) — all used in Prop 3 and its proof.
- **Extension 2**: $\tau$ (tax rate), $\delta$ (deadweight cost severity), $\phi_\text{eff}$ (effective displacement) — all used in the transfer equations and figure.
- **No orphan variables**: every symbol introduced is referenced in a result or calibration.

### Equations
1. **Eq (1)** — Aggregate consumption growth $C_{t+1} = (1+g)C_t$: feeds into the SDF and all pricing expressions.
2. **Eq (2)** — Displacement $\alpha_{t+1} = \phi\alpha_t$: central to the model's mechanism.
3. **Eq (3)** — CRRA utility: required to derive the household SDF that prices both assets.
4. **Eqs (4)–(5)** — P/D ratio formulas (Prop 1): the paper's main quantitative result, used in the table, discussed throughout, and reused in Extension 2 via $\phi_\text{eff}$.
5. **Eq (6)** — Existence condition $A^j < 1$ (Remark 1): does triple duty — used in Prop 2 proof (decomposes $A^j$), Extension 2 (explains infinite prices at low $\tau$), and the figure caption.
6. **Eq (7)** — Veto utility gain $\Delta u(\gamma)$: used in Prop 3 proof to show the negative-singularity term dominates as $\gamma \to \infty$.
7. **Eq (8)** — Post-transfer household consumption: foundation of Extension 2, feeds into $\phi_\text{eff}$ and the figure.
8. **Eq (9)** — Effective displacement $\phi_\text{eff}$: connects transfers back to the baseline pricing formula (Prop 1), avoiding the need to re-derive prices.
9. **Eq (10)** — Transfer ratio: carries the key economic insight that the proportional benefit of transfers is independent of the productivity jump $\eta$, while the level benefit grows without bound. This cannot be stated qualitatively without losing the precision of the claim.
10. **Appendix Eqs (11)–(13)** — Euler equation expansion and solution: required for the proof of Prop 1 (the spec mandates explicit proofs).

### Propositions and Formal Results
- **Proposition 1** (P/D ratios): The paper's main result. The closed-form formulas drive the quantitative table, and the $\Gamma^{AI}$ vs $\Gamma^{N}$ comparison is the economic heart of the hedging channel.
- **Remark 1** (Existence condition): Not merely a technical aside — it motivates the infinite-price phenomenon in Extension 2 and is explicitly used in the figure discussion.
- **Proposition 2** (Extinction attenuation): Establishes that extinction risk narrows the valuation spread, connecting the model to Jones (2024). The inline proof is somewhat involved (semi-elasticity of $A/(1-A)$) but provides the mechanism, not just the sign. The proof does economic work: it shows that the result holds for the *ratio* of P/D ratios, which is stronger than the level result and non-obvious.
- **Proposition 3** (Veto): The two-part structure (incomplete vs. complete markets) is essential — without part (ii), the veto could reflect high risk aversion alone rather than market incompleteness specifically.

### Checks Against Specific Criteria

**Formalism introduced and abandoned?** No. Every equation and proposition is referenced later in the text, either in a proof, calibration, or economic discussion.

**Qualitative takeaway replaceable by plain English?** No object can be removed without weakening the paper:
- The P/D formulas are needed for the table's quantitative magnitudes.
- The existence condition is needed to explain the infinite-price phenomenon in Extension 2.
- The transfer ratio's $\eta$-independence is a precise quantitative claim.
- Prop 3 requires formal statement to distinguish risk aversion from market incompleteness.

**Variables introduced and unused?** None found. All parameters appear in at least one result or calibration.

**Pompous or ceremonial formalism?** None found. The paper uses standard notation (CRRA, Euler equation, SDF) and does not over-formalize simple ideas. The "Kaldor-Hicks" efficiency definition is one sentence and sets up the tension with the veto — not ceremonial.

**Auxiliary formal detours?** None found. The paper moves linearly from setup to pricing to extensions, with no side results that fail to connect back to the main argument.
