# tests/theory-deadweight.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 2m 17s
[ralph-garage/agent-logs/20260412T095842.938758-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260412T095842.938758-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation does meaningful economic or narrative work; no deadweight formalism found.

## Audit method

Cataloged every parameter, equation, proposition, remark, and formal mechanism in the paper. For each, checked: (1) is it used in at least one result, calibration, or interpretation? (2) could it be replaced with plain English without loss? (3) is it ceremonial or pompous?

## Parameters and variables

All 20+ parameters and variables introduced in the paper are used in at least one proposition, calibration, or quantitative illustration:

- **Core model** ($C_t$, $g$, $\alpha_t$, $p$, $\xi$, $\eta$, $\phi$, $\theta_t$, $\Delta\theta$, $\gamma$, $\beta$): All appear directly in the P/D formulas (Proposition 1) and the calibration (Table 1). None is introduced and abandoned.
- **Derived quantities** ($\Gamma^{AI}$, $\Gamma^{N}$, $A^j$): $\Gamma$ factors are the key economic comparison driving the hedging channel. $A^j$ (existence condition) is used in Remark 1 and then load-bearing in Extension 2 (infinite P/D at $\tau=0$ under large singularity).
- **Extension 1** ($q$, $\kappa$, $\alpha^+$, $V_\text{veto}$, $V_\text{develop}$): All used in Proposition 3 and its numerical illustration. $q > 1/2$ makes the veto result economically striking.
- **Extension 2** ($\tau$, $\delta$, $\phi_\text{eff}$): All used in the transfer mechanism and Figure 3. $\phi_\text{eff}$ cleanly connects transfers back to Proposition 1's P/D formula.

No parameter is introduced without appearing in a result, calibration, or interpretation that matters for the paper's conclusions.

## Equations

All 10 numbered equations do work:

1. **Eq (1)** ($C_{t+1} = (1+g)C_t$): Minimal statement of growth; feeds into Euler equation derivation.
2. **Eq (2)** ($\alpha_{t+1} = \phi\alpha_t$): Displacement is the central mechanism.
3. **Eq (3)** (CRRA utility): Needed for closed-form P/D; $\gamma$ appears explicitly in formulas.
4. **Eqs (4)-(5)** (P/D ratios): Core result.
5. **Eq (6)** (existence condition): Referenced in Extension 2 and Figure 3 discussion.
6. **Eq (7)** ($\Delta u(\gamma)$): Used in Proposition 3 proof.
7. **Eq (8)** (transfer consumption): Foundation of Extension 2.
8. **Eq (9)** ($\phi_\text{eff}$): Bridges transfers to P/D formula.
9. **Eq (10)** (transfer ratio): Key insight that ratio is $\eta$-independent, setting up the levels argument.

## Propositions and remark

- **Proposition 1** (P/D ratios): Core result. No deadweight.
- **Remark 1** (existence condition): Not ceremonial---directly motivates Extension 2's transfer mechanism and is referenced in the Figure 3 caption.
- **Proposition 2** (extinction attenuation): The inline proof is detailed (semi-elasticity argument, convexity of $f(A) = A/(1-A)$), but this detail is necessary because the *ratio* result is non-trivial. The economic content (extinction attenuates, not amplifies, the premium) is discussed in Table 1 and is a distinct contribution.
- **Proposition 3** (veto): Both parts do economic work. Part (i) shows incomplete markets distort real decisions; part (ii) shows complete markets eliminate the distortion. The numerical example sharpens the point.

## Formal mechanisms checked for ceremonialism

- **Kaldor-Hicks label**: Efficient shorthand for the compensation principle; one sentence, not formalized further.
- **Complete-markets counterfactual** ($\phi_\text{eff} \to 1$): Stated in prose, not over-formalized. Drives the key economic point that market incompleteness is central.
- **AI owners as static group**: Explicitly noted as not modeling entry dynamics (avoiding scope creep). Honest and lean.

## Conclusion

The paper's formalism is compact and functional. Every formal object contributes to an economic claim, a calibration, or a quantitative illustration. No parameters are introduced and abandoned. No propositions are ceremonial. No auxiliary detours were found.
