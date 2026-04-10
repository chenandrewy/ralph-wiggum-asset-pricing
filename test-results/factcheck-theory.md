# tests/factcheck-theory.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 6m 58s
[ralph-garage/agent-logs/20260409T205235.751397-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T205235.751397-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

Every mathematical symbol in the paper was catalogued into 22 symbol families. No symbol is reused for a different formal object anywhere in the paper. Five minor infelicities were identified, none rising to the level of genuine ambiguity:

1. **$c^H$ subscripts**: The subscript convention shifts from time index ($c_t^H$) to semantic label ($c^H_{post}$, $c^H_{no\text{-}transfer}$) in Extension 2 without explicit announcement.
2. **$\alpha$ subscripts**: Time subscript dropped in Extension 2 without explicit note; $\alpha'$ appears once in the appendix without definition.
3. **$\Delta\theta$ naming**: Uses the $\Delta$ prefix (conventionally "change in $\theta$") for a parameter that is not the actual change $\theta_{t+1} - \theta_t = \Delta\theta(1-\theta_t)$.
4. **$u$ (lowercase)**: Period utility function referenced in Proposition 3 proof ("$u$ is concave") but never formally defined as a symbol.
5. **$\theta$ subscripts**: Time subscript dropped in Proposition 1 and Section 3, standard in stationary analysis but inconsistent with $\theta_t$ in the setup.

No symbol collisions, no conflicting definitions across sections, no reuse of symbols for different economic concepts.

## Requirement 2: Assumption Consistency — PASS

17 distinct mathematical assumptions were identified across the setup (A1–A11), existence condition (A12), extensions (A13–A15), and calibrations (A16–A17). Detailed consistency checks found:

- **Parameter domains**: All compatible. No parameter restriction contradicts another.
- **Probability structure**: Event probabilities sum to 1 in every branch of the event tree.
- **Functional forms**: Consumption growth, dividend growth, and SDF expressions are mutually consistent. The full Euler equation derivation was verified algebraically from the SDF through to the closed-form P/D formula (Proposition 1).
- **Extension 2 algebra**: Transfer consumption (Eq. 9), effective displacement $\phi_\text{eff}$, and transfer ratio (Eq. 10) are all algebraically consistent with the baseline.
- **Existence condition**: Correctly satisfied by baseline calibration ($A^{AI} = 0.987 < 1$ at $p = 1\%$, $\xi = 0$) and correctly violated by large-singularity parameters ($A^{AI} = 2.37$), as the paper states.
- **Numerical claims verified**: P/D of ~18 vs ~11 at $p = 0.5\%$ (actual: 17.5 vs 11.1); ratio of ~6 at $p = 1\%$ (actual: 5.7); $\phi^{-\gamma} = 160{,}000$; consumption changes of 25% and 50%.
- **Extension 1 vs. baseline**: No contradiction. The positive singularity $\alpha_{t+1} = \min(1, \alpha_t/\phi)$ correctly caps at 1. The negative singularity matches the baseline.
- **Extinction utility**: $U_\text{ext} = 0 > u(c)$ for $\gamma > 1$ is correctly described as conservative for the veto result.

Three low-severity observations (not inconsistencies):
1. The stationarity approximation (post-singularity P/D $\approx$ pre-singularity P/D) is acknowledged but error magnitude is unanalyzed.
2. Household consumption share $\alpha_t$ is exogenous rather than micro-founded through budget constraints — a standard modeling simplification.
3. Extension 1 omits explicit probabilities for positive vs. negative singularity (qualitative by design).

## Requirement 3: Traceability — PASS

All mathematical objects in the paper trace back to the 17 assumptions:

| Derived Object | Traces to |
|---|---|
| $\Gamma^{AI}, \Gamma^{N}$ (dividend growth factors) | A5 ($\eta$), A7 ($\theta, \Delta\theta$) |
| $A^j$ (existence condition) | A2 ($g$), A4 ($p$), A5 ($\eta, \phi$), A6 ($\xi$), A10 ($\beta, \gamma$), A7/A8 (via $\Gamma^j$) |
| $v^{AI}, v^{N}$ (P/D ratios) | Euler equation from A10 preferences + all model primitives |
| SDF $\beta(c_{t+1}^H/c_t^H)^{-\gamma}$ | A10 ($\beta, \gamma$), A3 ($c_t^H$) |
| $\phi_\text{eff}$ (effective displacement) | A5 ($\phi$), A15 ($\tau, \delta$), A3 ($\alpha$) |
| $c^H_{post}, c^H_{no\text{-}transfer}$ | A3, A5, A15 |
| Comparative statics (Proposition 2) | Differentiation of P/D formulas |
| Veto result (Proposition 3) | A10 (CRRA with $\gamma > 1$), A9 (incomplete markets), A13–A14 |

No expression in the paper was found that cannot be logically derived from the stated assumptions.
