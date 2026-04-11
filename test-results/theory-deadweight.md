# tests/theory-deadweight.py
Started: 2026-04-10 22:15:41 EDT
Runtime: 1m 45s
[ralph-garage/agent-logs/20260410T221541.754886-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260410T221541.754886-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to an economic claim, calibration, or result; no deadweight formalism was found.

## Audit Details

### Parameters
All 14 parameters are used in at least one result, calibration, or interpretation:

| Parameter | Introduced | Used in |
|-----------|-----------|---------|
| $g$ (growth rate) | Eq (1) | P/D formulas (4–5), calibration (Table 1) |
| $\alpha_t$ (household share) | Setup | Displacement (2), utility (3), transfers (7–9), veto (Prop 3) |
| $\phi$ (displacement) | Eq (2) | P/D formulas, comp statics (Prop 2), transfers ($\phi_\text{eff}$), veto, calibration |
| $\eta$ (productivity jump) | Singularity setup | P/D formulas, $\Gamma$ factors, transfer ratio (9), calibration |
| $\xi$ (extinction prob) | Singularity setup | P/D formulas, comp statics (iii), calibration, veto discussion |
| $p$ (singularity prob) | Singularity setup | P/D formulas, comp statics (ii), calibration, veto numerical example |
| $\theta_t$ (AI dividend share) | Assets setup | $\Gamma^{AI}$, $\Gamma^{N}$, backward recursion, calibration |
| $\Delta\theta$ (share jump) | Assets setup | $\Gamma$ factors, approximation discussion, calibration |
| $\beta$ (discount factor) | Eq (3) | P/D formulas, calibration |
| $\gamma$ (risk aversion) | Eq (3) | P/D formulas, comp statics, veto condition, calibration |
| $\tau$ (tax rate) | Eq (7) | Transfer consumption, $\phi_\text{eff}$, transfer ratio, Figure 2 |
| $\delta$ (deadweight cost) | Eq (7) | Transfer consumption, $\phi_\text{eff}$, transfer ratio, Figure 2 |

No parameter is introduced without being used in a result or calibration.

### Equations
All display equations do economic or derivational work:

1. **Eq (1)** ($C_{t+1} = (1+g)C_t$): Establishes the growth process; enters the SDF and P/D formulas.
2. **Eq (2)** ($\alpha_{t+1} = \phi\alpha_t$): Defines displacement, the central mechanism.
3. **Eq (3)** (CRRA utility): Needed for the Euler equation and all pricing results.
4. **Eqs (4–5)** (P/D ratios): Main results of the paper, used in quantitative section.
5. **Eq (6)** (existence condition $A^j < 1$): Referenced in Prop 2 proof (iii) and Extension 2 (infinite P/D at extreme displacement).
6. **Eq (7)** (transfer consumption): Basis for Extension 2 analysis and Figure 2.
7. **Eq (8)** ($\phi_\text{eff}$): Connects transfers back to Prop 1, enabling reuse of the P/D formula.
8. **Eq (9)** (transfer ratio): Establishes the key economic point that the ratio is $\eta$-independent while levels grow with $\eta$.

### Propositions and Remark

- **Proposition 1** (P/D ratios): Core pricing result. Used in quantitative section (Table 1), Extension 2 (via $\phi_\text{eff}$), and guides all economic interpretation.
- **Proposition 2** (Comparative statics): Organizes the interpretation of Table 1. Part (iii) uses a non-obvious convexity argument about $A^j/(1-A^j)$ that would be hard to convey in prose alone.
- **Proposition 3** (Veto): Main result of Extension 1. Both parts do distinct economic work: (i) shows incomplete markets distort real decisions, (ii) shows complete markets eliminate the distortion.
- **Remark 1** (Existence condition): Referenced in Prop 2 proof (iii) and in Extension 2's discussion of infinite P/D ratios under extreme displacement. It also motivates the transfer mechanism (Section 4.2).

### Derived Quantities

- $\Gamma^{AI}$, $\Gamma^{N}$: Dividend growth factors that carry the economic content of Prop 1 (the comparison $\Gamma^{AI} > \Gamma^{N}$ drives the hedging channel). Used in P/D formulas and comparative statics.
- $A^j$: Compact notation for the existence condition. Used in Prop 2 proof (iii) and Remark 1.
- $\phi_\text{eff}$: Effective displacement under transfers. Connects Extension 2 back to the baseline P/D formula.

### Checks for Specific Problems

1. **Formalism introduced then abandoned?** No. Every formal object appears in at least one downstream result or calibration.
2. **Qualitative takeaway statable in plain English without loss?** No. The P/D formulas (Prop 1) deliver closed-form expressions used in calibration. The comparative statics (Prop 2) include a non-obvious convexity result in (iii). The veto proposition (Prop 3) requires the formal distinction between incomplete and complete markets to state precisely.
3. **Unused variables or parameters?** No. All 14 parameters are used.
4. **Pompous or ceremonial formalism?** No. The paper uses three propositions, one remark, and nine display equations for a model with two assets, two agent types, three states, and two extensions. This is lean for an asset pricing theory paper.
5. **Auxiliary formal detours?** No. The extensions branch directly off the baseline (as the spec requires) and each addresses a specific economic question.
