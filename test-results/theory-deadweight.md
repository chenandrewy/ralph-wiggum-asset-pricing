# tests/theory-deadweight.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 1m 56s
[ralph-garage/agent-logs/20260411T100209.039200-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260411T100209.039200-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to an economic claim, quantitative result, or narrative argument; no deadweight formalism was found.

## Audit methodology

Every formal object (equation, proposition, remark, parameter, and variable) was cataloged and traced through the paper to verify that it (a) appears in at least one result, calibration, or interpretation, (b) cannot be replaced by plain English without weakening the economic claims, and (c) does not constitute a ceremonial or pompous detour.

## Formal objects cataloged

### Parameters and variables (all used)

| Symbol | Introduced | Used in |
|--------|-----------|---------|
| $C_t$, $g$ | Setup (Eq 1) | P/D formulas, quantitative analysis, transfers |
| $\alpha_t$, $c_t^H$ | Setup | SDF, veto analysis, transfer base |
| $p$, $\xi$ | Singularity | P/D formulas, comparative statics, calibration grid |
| $\eta$ | Singularity | P/D formulas, displacement condition $\phi(1+\eta)<1$, transfer levels |
| $\phi$ | Displacement (Eq 2) | P/D formulas, comparative statics, veto, transfers ($\phi_\text{eff}$) |
| $\theta_t$, $\Delta\theta$ | Assets | $\Gamma^{AI}$, $\Gamma^{N}$, hedging channel |
| $\gamma$, $\beta$ | Preferences (Eq 3) | P/D formulas, veto threshold, calibration |
| $\Gamma^{AI}$, $\Gamma^{N}$ | Prop 1 | Comparative statics, hedging channel interpretation |
| $A^j$ | Remark 1 (Eq 6) | Existence condition, comparative statics proof (iii), Extension 2 |
| $q$ | Extension 1 | Veto proof (Eq 7), numerical example |
| $\kappa$ | Extension 1 | Veto cost, Proposition 3 |
| $\tau$, $\delta$ | Extension 2 | Transfer consumption (Eq 8), $\phi_\text{eff}$ (Eq 9), Figure 2 |
| $\phi_\text{eff}$ | Eq 9 | Connects transfers to baseline P/D formula |

No parameter or variable is introduced and then abandoned.

### Equations

1. **Eq 1** (consumption growth): Sets notation; feeds into the Euler equation and every pricing formula. One line, no bloat.
2. **Eq 2** (displacement): Core mechanism of the model. Referenced throughout.
3. **Eq 3** (CRRA utility): Standard preference specification. Used through the Euler equation and explicitly in the veto analysis.
4. **Eqs 4--5** (P/D ratios, Proposition 1): The paper's main quantitative result. Calibrated in Table 1.
5. **Eq 6** (existence condition, Remark 1): Not decorative---it is used in the Discussion (Section 2.3), in the comparative statics proof (iii), and is the key feature exploited in Extension 2 (infinite hedging demand at $\tau = 0$ under the large singularity).
6. **Eq 7** ($\Delta u(\gamma)$, veto proof): Required for the limiting argument in Proposition 3(i). The proof would be incomplete without it.
7. **Eq 8** (transfer consumption): Sets up the transfer mechanism. Every subsequent result in Extension 2 flows from it.
8. **Eq 9** ($\phi_\text{eff}$): Bridges transfers to the baseline pricing formula, enabling reuse of Proposition 1. Efficient.
9. **Eq 10** (transfer ratio): Makes transparent that the ratio is independent of $\eta$---the key insight that singularity-scale growth overwhelms deadweight costs. Stating this in words alone would obscure the mechanism.
10. **Appendix Eqs 11--14**: Proof of Proposition 1, required by paper spec.

### Propositions and remarks

- **Proposition 1** (P/D ratios): The central result. Calibrated quantitatively.
- **Remark 1** (existence condition): Does real work---motivates Extension 2 and the infinite-hedging-demand discontinuity.
- **Proposition 2** (comparative statics): Organizes the key qualitative predictions. Each part is interpreted against Table 1. The convexity argument in part (iii) adds genuine insight about extinction risk.
- **Proposition 3** (veto): Central to Extension 1. Both parts do economic work: (i) shows incomplete markets distort real decisions, (ii) shows complete markets eliminate the distortion.

### Subparts within objects

- **$\Gamma^{AI}$ vs $\Gamma^{N}$**: The comparison is the economic heart of Proposition 1 (hedging channel). Not extraneous notation.
- **$\alpha^+ = \min(1, \alpha/\phi)$** in the positive singularity: Technical but necessary to ensure the share stays in $(0,1)$. Used in Eq 7.
- **$(1-\alpha_t)C_t$** (AI owners' consumption): Introduced in the setup and used as the transfer base in Extension 2 (Eq 8). Would be a loose end if Extension 2 didn't exist, but it does.
- **$V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$**: Referenced in Proposition 3 without explicit display formulas. The proof works through $\Delta u(\gamma)$ and limits, which is more transparent than displaying the full Bellman. This is the right level of formalism.

## Specific checks

**Introduced-then-abandoned formalism?** No. Every symbol traces to at least one result, calibration value, or interpretive passage.

**Could any formal object's takeaway be stated in plain English without weakening claims?** The closest candidate is Eq 10 (transfer ratio), but its independence from $\eta$ is the key analytical insight of Extension 2, and displaying it makes the mechanism transparent. Stating "the ratio doesn't depend on $\eta$" in words alone would be less convincing and would deprive the reader of the ability to verify the claim at a glance.

**Unused variables or parameters?** None found. Every parameter appears in a formula, calibration, or proposition.

**Pompous or ceremonial formalism?** No. The paper avoids unnecessary generality (e.g., no measure-theoretic probability, no abstract state spaces, no general equilibrium existence theorems). The singularity is modeled as a simple Bernoulli event. CRRA is stated in one line. The appendix proof is mechanical and compact.

**Auxiliary formal detours?** No. Each extension branches directly off the baseline model and introduces only the new parameters it needs ($q, \kappa$ for Extension 1; $\tau, \delta$ for Extension 2). There are no formal lemmas, no intermediate results that exist only to support other results.
