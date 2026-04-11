# tests/factcheck-theory.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 6m 18s
[ralph-garage/agent-logs/20260410T225642.494332-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260410T225642.494332-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to stated assumptions.

## Requirement 1: Notational Consistency — PASS

24 symbol families identified. No collisions found. Every symbol has a unique, stable meaning throughout the paper. Key checks:

- **$\alpha$ vs $\theta$**: Distinct objects (consumption share vs. dividend share). The paper explicitly distinguishes them (line 108).
- **$\phi$ vs $\phi_\text{eff}$**: Clearly distinguished via subscript. $\phi_\text{eff}$ is a derived quantity with an explicit definition (eq. 8).
- **$\delta$ vs $\Delta\theta$**: Different symbols, no collision.
- **$v^{AI}$ vs $P^{AI}/D^{AI}$**: $v^{AI}$ introduced in the proof as shorthand; consistent usage.
- **Superscript conventions**: $AI$, $N$, $H$, $j$ are each used for a single role throughout.
- **Time subscript dropping**: $\alpha$, $\theta$ drop time subscripts in stationary-equilibrium and extension analyses. Standard practice, semantically clear.

Minor observations (not failures):
- Lowercase $u$ used once informally in prose (Proposition 3 proof) for period utility. Not formally defined but unambiguous in context.

## Requirement 2: Assumption Consistency — PASS

28 assumptions cataloged across timing/structure, consumption, singularity, assets, preferences, equilibrium, and both extensions. No parameter range conflicts, no logical contradictions, no timing conflicts.

Key consistency checks:
- **$\gamma > 1$ (E1)** is consistent with the extinction utility normalization $U_\text{ext} = 0$ (G5), since CRRA utility is negative for $c > 0$ when $\gamma > 1$.
- **$\phi \in (0,1)$ (C3)** is preserved under both positive ($\min(1, \alpha/\phi)$) and negative ($\phi\alpha$) singularity transitions.
- **Market incompleteness (D4)** vs. Extension 1's complete-markets counterfactual (Prop 3(ii)): explicitly a comparison, not a contradiction.
- **Baseline negative-only singularity (C3)** vs. Extension 1's positive singularity (G1): explicitly an augmentation.
- **Total dividends $= C_t$ (D3)** is consistent with household consumption $= \alpha_t C_t$ (B2): the paper explains that dividends are distributed among all investors, not solely the household.
- **Calibration values** all satisfy stated parameter constraints.

Three negligible implicit constraints ($\delta\tau < 1$, $p \in (0,1)$, $\xi \in [0,1)$) are never explicitly stated but are standard and satisfied by all calibrations.

## Requirement 3: Traceability — PASS

All mathematical objects trace back to the stated assumptions:

| Derived Object | Source Assumptions |
|---|---|
| $\Gamma^{AI}, \Gamma^N$ (dividend growth factors) | $\theta_t$ (D1), $\Delta\theta$ (D1), $\eta$ (C3) |
| $A^j$ (existence condition) | $\beta$ (E1), $g$ (B1), $\gamma$ (E1), $p$ (C1), $\xi$ (C3/C4), $\eta$ (C3), $\phi$ (C3), $\Gamma^j$ |
| $P^{AI}/D^{AI}$, $P^N/D^N$ (P/D ratios) | Euler equation from E1 + singularity structure (C1-C5) + asset definitions (D1-D2) |
| $v^{AI}$ (proof shorthand) | $= P^{AI}/D^{AI}$, same derivation |
| Comparative statics (Prop 2) | Derivatives of P/D formulas w.r.t. $\phi$, $p$, $\xi$ |
| Veto result (Prop 3) | Extension 1 assumptions (G1-G5) + baseline preferences (E1) |
| $c^H_{post}$ (eq. 6) | $\phi$ (C3), $\alpha$ (B2), $\eta$ (C3), $g$ (B1), $C_t$ (B1), $\tau$ (H1), $\delta$ (H2) |
| $\phi_\text{eff}$ (eq. 8) | $\phi$ (C3), $\tau$ (H1), $\delta$ (H2), $\alpha$ (B2) |
| Transfer ratio (eq. 9) | Ratio of eq. 6 to baseline, using same primitives |

### Proof algebra verification

The Euler equation expansion (eq. 10) correctly handles all three branches:
- No singularity: SDF $= \beta(1+g)^{-\gamma}$, dividend growth $= (1+g)$, product $= \beta(1+g)^{1-\gamma}$. Correct.
- Non-extinction singularity: SDF $= \beta[\phi(1+g)(1+\eta)]^{-\gamma}$, dividend growth $= \Gamma^{AI}(1+g)$, product $= \beta(1+g)^{1-\gamma}\phi^{-\gamma}(1+\eta)^{-\gamma}\Gamma^{AI}$. Correct.
- Extinction: payoff is zero. Correct.

Solving $v = A/(1-A)$ from the Euler equation is algebraically verified. The $\phi_\text{eff}$ factorization (eq. 8 from eq. 6) is verified. The transfer ratio (eq. 9) is verified. $\Gamma^N = (1-\Delta\theta)(1+\eta)$ simplification in the proof is verified.

No expression was found that cannot be logically derived from the stated assumptions.
