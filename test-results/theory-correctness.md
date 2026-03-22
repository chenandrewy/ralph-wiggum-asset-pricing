# tests/theory-correctness.py
Started: 2026-03-22 09:54:57 EDT
Runtime: 6m 15s
[ralph-garage/agent-logs/20260322T135457.719502Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T135457.719502Z_theory-correctness_claude_opus.log)

# theory-correctness

VERDICT: PASS

REASON: All mathematical derivations are correct, assumptions are consistent, notation is uniform, and verbal claims are supported by the formal theory.

## Condition 1: Notational Consistency

All mathematical objects were catalogued and grouped by economic concept (consumption, dividends, preferences, shock parameters, derived quantities, extension parameters). Notation is consistent throughout the paper. Each symbol is defined once and used with the same meaning in all subsequent appearances. The extension parameters ($\delta$, $\delta_H$, $\delta_O$, $\pi$, $Y_O$, $k$) are introduced cleanly and do not conflict with baseline notation.

## Condition 2: Consistent Assumptions

All assumptions were listed and cross-checked. Key consistency checks:
- $a < 1$ is implied by $\beta \in (0,1)$, $g > 0$, $\gamma > 1$, so the explicit assumption is redundant but not contradictory.
- Constancy of $s$ pre-singularity follows from the common growth rate $g$ in eq (4).
- The consumption jump factor $J(s) = 1 - \phi + (\theta+\phi)s$ is correctly derived from the dividend processes and the budget constraint.
- No pair of assumptions is mutually contradictory.

## Condition 3: Logical Results

Every derived expression was traced back to assumptions and verified:

- **Post-singularity P/D** ($\bar{v} = a/(1-a)$): Follows from the Euler equation with deterministic growth. Verified.
- **Proposition 1** (eqs 6–7): Euler equation expanded into no-singularity and singularity branches, solved for $v^A$. Algebraically verified.
- **Proposition 2** (eq 8): Subtraction of eq (7) from eq (6) yields the premium. All three comparative statics (i)–(iii) verified via calculus.
- **Decomposition** (eq 10): Correct factorization of $J^{-\gamma}$ from the premium expression.
- **Corollary 1**: Follows from Prop 2(ii) and the monotonicity of $\tilde{s}(\alpha)$ in $\alpha$.
- **Proposition 3** (eq 12): Extinction state contributes zero to pricing (dividends are zero); survival probability $(1-\delta)$ scales the singularity contribution. Verified.
- **Proposition 4** (eq 13): Four sub-states (no singularity, extinction, survive+friction, survive+resolve) correctly aggregated. Verified that the friction-resolves state contributes $\pi$ (not $\pi J^{-\gamma}$) because $J=1$ when the household rebalances.
- **Proposition 5**: Hedging component $\propto (\theta+\phi)(1-\pi)(J^{-\gamma}-1)$ correctly derived. Hump shape follows from competing monotonicity of $(1-\pi)$ (decreasing in $\theta$) and $(\theta+\phi)(J^{-\gamma}-1)$ (increasing then decreasing in $\theta$). Verified.
- **All numerical values** in Tables 1–3 were independently recomputed and match the paper to within rounding precision.

## Condition 4: Interpretations

All key verbal economic claims were checked against the formal results:

1. AI valuation premium exists and is positive — supported by Prop 2, eq (8).
2. Premium increasing in singularity probability — Prop 2(i).
3. Premium decreasing in AI share — Prop 2(ii).
4. Incomplete markets amplify the premium via the hedging channel — decomposition eq (10) shows amplifier $J^{-\gamma} > 1$.
5. Hedging demand roughly doubles the cash-flow premium — $J^{-\gamma} \approx 1.81$ at baseline calibration.
6. Self-limiting mechanism — larger AI share reduces premium, comparative statics in Prop 2(ii).
7. Broadening market access reduces the premium — Corollary 1.
8. AI stocks cannot hedge extinction — Prop 3.
9. Disagreement about extinction can unwind the friction — Prop 4.
10. Hedging component is hump-shaped — Prop 5(ii).
11. Cash-flow premium persists even as hedging vanishes — Prop 5(i).

**Minor note:** In the proof of Proposition 5(ii), the parenthetical "where the singularity becomes more harmful" as $\theta$ increases is imprecise — increasing $\theta$ actually raises $J$ and makes the singularity less harmful to the household. The hedging component increases for small $\theta$ because the dividend-differential factor $(\theta+\phi)$ grows faster than the hedging amplifier $J^{-\gamma}$ declines. The mathematical claim (hump shape) is correctly derived and the overall economic logic is sound; only the parenthetical explanation of the mechanism is misleading.
