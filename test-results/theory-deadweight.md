# tests/theory-deadweight.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 2m 11s
[ralph-garage/agent-logs/20260412T093252.129321-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.129321-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and proposition contributes to an economic claim, calibration, or narrative thread; no deadweight formalism found.

## Audit Details

### Parameters audited (all used)

| Parameter | Introduced | Used in |
|-----------|-----------|---------|
| $C_t$, $g$ | Setup (eq 1) | P/D formulas, transfers (eq 7), veto numerics |
| $\alpha_t$ | Setup | SDF, veto, transfers, throughout |
| $p$ | Singularity | P/D formulas, calibration table, veto numerics |
| $\xi$ | Singularity | Prop 2, calibration table, veto discussion |
| $\eta$ | Singularity | P/D formulas, transfers, calibration |
| $\phi$ | Displacement (eq 2) | P/D formulas, veto, transfers, Remark 1 |
| $\theta_t$, $\Delta\theta$ | Assets | $\Gamma^{AI}$, $\Gamma^N$ in P/D formulas, calibration |
| $\gamma$, $\beta$ | Preferences (eq 3) | P/D formulas, veto threshold, calibration |
| $\Gamma^{AI}$, $\Gamma^N$ | Prop 1 | Core hedging-channel comparison, Prop 2 proof |
| $A^j$ | Remark 1 (eq 6) | Prop 2 proof, Extension 2 (infinite P/D at low $\tau$) |
| $q$ | Extension 1 | Veto proposition, numerical example |
| $\kappa$ | Extension 1 | Veto proposition, numerical example |
| $\alpha^+$ | Extension 1 | Veto proof (eq 8) |
| $\tau$ | Extension 2 | Transfer consumption (eq 7), $\phi_\text{eff}$ (eq 8), figure |
| $\delta$ | Extension 2 | Deadweight costs in transfers, figure |
| $\phi_\text{eff}$ | Extension 2 (eq 8) | Bridges transfers back to Prop 1 P/D formula |

### Propositions audited (all contribute)

1. **Proposition 1 (P/D ratios)**: Core result. Delivers closed-form valuations used in calibration table, discussion of hedging channel, and Extension 2 (via $\phi_\text{eff}$ substitution).
2. **Proposition 2 (Extinction attenuation)**: Interprets calibration table patterns. The proof is inline but all steps are necessary — the ratio result (not just the level result) requires the convexity and semi-elasticity argument.
3. **Proposition 3 (Veto)**: Core extension result. Both parts (incomplete vs. complete markets) do distinct work. Numerical example grounds the result at reasonable parameter values.

### Remark 1 (Existence condition)

Not ceremonial. Directly invoked in Extension 2 to explain the infinite P/D ratio phenomenon in Figure 3 (large-singularity case at low tax rates). Also motivates why transfers matter — they restore the existence condition.

### Other formal objects audited

- **Euler equation and appendix proof**: Required by the paper's convention of explicit proofs. Standard derivation, no excess.
- **AI owners**: Described but deliberately not given formal preferences or optimization — the paper explicitly states they are not marginal investors. This is the right level of formalism; modeling them further would be unnecessary.
- **Complete-markets counterfactual** ($\phi_\text{eff} \to 1$): Invoked in discussion and Prop 3(ii) without a separate formal equilibrium. Efficient treatment.
- **Transfer ratio (eq 9)**: Does economic work — shows the ratio is independent of $\eta$, which is the key insight enabling the "growth overwhelms deadweight costs" argument.
- **$B$, $S$ in Prop 2 proof**: Intermediate proof variables, not promoted to named model objects. Appropriate.

### Checks for specific failure modes

- **Introduced and abandoned?** No. Every named object reappears in a result, calibration, or interpretation.
- **Qualitative takeaway statable without formalism?** The P/D formulas, existence condition, and $\phi_\text{eff}$ bridge all provide quantitative content beyond what prose could deliver. The veto threshold $\bar{\gamma}$ is existence-type, not computable in plain English.
- **Pompous or ceremonial?** No. The paper uses standard asset-pricing notation. No unnecessary generality (e.g., no general SDF beyond CRRA, no multi-good extensions, no continuous-time embedding).
- **Auxiliary formal detours?** No. Each extension branches from the baseline with minimal new notation and directly addresses a stated economic question.
