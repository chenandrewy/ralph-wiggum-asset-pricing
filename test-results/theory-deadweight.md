# tests/theory-deadweight.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 1m 43s
[ralph-garage/agent-logs/20260411T214322.784493-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260411T214322.784493-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to a result, calibration, or economic interpretation; no deadweight formalism was found.

## Audit methodology

Inventoried every formal object (parameters, variables, equations, propositions, remarks) and checked whether each (a) appears in at least one result, calibration, or interpretation that matters for the paper's conclusions, (b) could be replaced by plain English without weakening the economic claims, and (c) avoids ceremonial or pompous detours.

## Inventory of formal objects and their uses

### Core parameters (all appear in Propositions 1-2, Table 1, and/or extensions)
| Object | Introduced | Used in |
|--------|-----------|---------|
| $C_t$, $g$ (eq 1) | Setup | P/D formulas via $(1+g)^{1-\gamma}$; calibration |
| $\alpha_t$, $\phi$ (eq 2) | Setup | SDF, P/D formulas via $\phi^{-\gamma}$; veto analysis; transfer analysis |
| $p$, $\xi$, $\eta$ | Setup | P/D formulas; Prop 2 (extinction attenuation); Table 1 grid axes; Extension 2 |
| $\theta_t$, $\Delta\theta$ | Assets | $\Gamma^{AI}$, $\Gamma^{N}$ definitions; Table 1 |
| $\gamma$, $\beta$ (eq 3) | Preferences | P/D formulas; veto threshold $\bar{\gamma}$ (Prop 3); calibration |

### Propositions and remarks
| Object | Role | Deadweight? |
|--------|------|-------------|
| Prop 1 (P/D ratios) | Core pricing result; drives Table 1 and all quantitative analysis | No |
| Remark 1 (existence condition) | Foreshadows Extension 2; directly used in Figure 3 narrative (infinite P/D at $\tau=0$) | No |
| Prop 2 (extinction attenuation) | Second main result; verified in Table 1 | No |
| Prop 3 (veto) | Extension 1 main result; illustrated with numerical example | No |

### Derived quantities
| Object | Role | Deadweight? |
|--------|------|-------------|
| $\Gamma^{AI}$, $\Gamma^{N}$ | Core of the hedging mechanism comparison; appear in Prop 1-2 and proof of Prop 2 | No |
| $A^j$ (eq 6) | Compact form for existence condition; used in Prop 2 proof and Extension 2 | No |

### Extension 1 parameters
| Object | Role | Deadweight? |
|--------|------|-------------|
| $q$ (positive singularity prob) | Appears in Prop 3 proof (eq 7) and numerical example ($q=0.70$) | No |
| $\kappa$ (veto cost) | Appears in Prop 3 statement and numerical example ($\kappa=1\%$) | No |
| $\alpha^+$ | Appears in eq 7 and proof | No |
| $\Delta u(\gamma)$ (eq 7) | Core of Prop 3 proof; shows how risk aversion drives veto | No |

### Extension 2 parameters
| Object | Role | Deadweight? |
|--------|------|-------------|
| $\tau$ (tax rate) | x-axis of Figure 3; appears in eqs 8-10 | No |
| $\delta$ (deadweight cost) | Appears in eqs 8-10; calibrated at 0.5 and 0.9 | No |
| $\phi_\text{eff}$ (eq 9) | Links transfers to baseline pricing (Prop 1 with $\phi \to \phi_\text{eff}$) | No |
| Transfer ratio (eq 10) | Key insight: ratio is $\eta$-independent, so levels grow with singularity size | No |
| $c^H_{post}$ (eq 8) | Defines household post-transfer consumption; basis for Figure 3 panel (b) | No |

### Appendix
The Euler equation derivation (eqs 11-13) is the proof of Proposition 1, required by the spec (all propositions explicitly proved, long proofs in appendix).

## Checks for specific failure modes

**Introduced-then-abandoned formalism:** None found. Every parameter introduced in the Setup appears in at least one of Propositions 1-3, the calibration table, or the extension figures.

**Qualitative takeaway replaceable by plain English:** The display equations are concise (most are one line) and all carry quantitative content used in calibrations or proofs. Equation (1) ($C_{t+1} = (1+g)C_t$) and equation (2) ($\alpha_{t+1} = \phi\alpha_t$) are simple enough to state in prose, but they establish notation referenced in later equations, so removing them would require more verbose prose elsewhere. This is standard and not deadweight.

**Unused variables/parameters:** None. Every symbol introduced appears in a result, proof, or calibration.

**Pompous or ceremonial formalism:** The paper uses only three propositions and one remark. There are no lemmas, corollaries, definitions, or assumptions environments. The model has a small parameter set (9 core parameters, 3 extension-specific parameters per extension). The formalism is lean relative to standard theory papers in top finance journals.

**Auxiliary formal detours:** None. The paper moves linearly: setup -> pricing -> quantitative analysis -> extensions -> conclusion. There are no side results or tangential formal excursions.
