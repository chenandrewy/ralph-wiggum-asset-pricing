# tests/factcheck-theory.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 10m 52s
[ralph-garage/agent-logs/20260409T182005.675863-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.675863-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, assumptions are mutually compatible, and all mathematical objects trace to the assumptions, though several presentation gaps and one vacuous limit are noted.

## Requirement 1: Notational Consistency — PASS

25 symbol families were identified across all sections and the appendix. **No collisions found.** Every symbol maintains a single, consistent semantic role throughout the paper.

Minor issues:
- The stochastic discount factor (SDF) is referenced in prose (Sec 2.2, Appendix A) but never assigned a symbol. The implicit form $\beta(c_{t+1}^H/c_t^H)^{-\gamma}$ is clear from the Euler equation.
- $\alpha', \theta'$ appear informally in the proof of Prop 1 (line 156) as shorthand for post-singularity values but are never defined. Context makes them clear.
- "Social surplus" and "social SDF" are referenced in Prop 3 proof and Appendix A without formal definition.

These are prose-level references, not notation inconsistencies.

## Requirement 2: Consistent Assumptions — PASS

38 assumptions were catalogued across all sections. No outright contradictions were found between any pair of assumptions.

### Flags

**F1 (LOW):** The constraint $\alpha_t \in (0, 1-\theta_t]$ (A7) is not formally verified after repeated singularities change both $\alpha_t$ and $\theta_t$. It holds by inspection: $\alpha_t = \phi^n\alpha_0 \to 0$ geometrically, while $1-\theta_t > 0$ always.

**F2 (MEDIUM):** In Extension 1, a positive singularity sets $\alpha_{t+1} = \phi^+\alpha_t > \alpha_t$ while $\theta_t$ also increases via $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$. Both increasing simultaneously could push $\alpha_t + \theta_t > 1$, violating A7 and making private AI capital dividends negative. No constraint on $\phi^+$ prevents this. Practical impact is limited since Extension 1 does not derive pricing formulas.

**F3 (LOW):** Net transfer non-negativity ($1 - \delta_0\tau > 0$) is not stated as a constraint in Extension 2.

**F4 (MEDIUM):** The P/D ratio formula requires a convergence condition (denominator positive) that is never stated. Using calibration values ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$):
- At $p=1\%$, $\xi=0$: effective discount factor $\approx 0.987$, yielding P/D $\approx 76$. Barely converges.
- At $p=2\%$, $\xi=0$: effective discount factor $\approx 1.07 > 1$. **Formula diverges.** The paper's table avoids this region but does not discuss the boundary.

**F6 (LOW):** Extension 1 does not specify whether $\theta_t$ dynamics apply to positive singularities.

**F7 (LOW):** Post-singularity stationarity (treating the new P/D ratio as approximately $v^{AI}$) is acknowledged as an approximation. Since $\Gamma^{AI}$ depends on $\theta$, which changes after a singularity, the approximation is not exact.

## Requirement 3: Traceability — PASS

All mathematical objects (derived quantities $\Gamma^{AI}$, $\Gamma^N$, $v^{AI}$, $P^{AI}/D^{AI}$, $P^N/D^N$, $\Delta U^H$, $c^H_{post}$, $c^H_{no\text{-}transfer}$) trace back to the stated assumptions. Derivations were verified:

- **Prop 1 (P/D ratios):** Euler equation expansion verified step by step. The algebra from the three-state expectation to the closed-form $v^{AI} = A/(1-A)$ is correct.
- **Corollary 1 (spread):** $\Gamma^{AI} > \Gamma^N$ when $\Delta\theta > 0$ verified algebraically.
- **Prop 2 (comparative statics):** Arguments are correct given the formula structure.
- **Prop 3 (veto):** Part (i) is qualitatively correct — for large $\gamma$, the concavity of CRRA makes the downside dominate. Part (ii) relies on the assumed social efficiency (A33) and the undefined "social surplus," but the logical chain is valid given the assumption.

### Vacuous limit in eq (11)

The ratio $c^H_{post}/c^H_{no\text{-}transfer}$ presented with $\lim_{\eta \to \infty}$ does not actually depend on $\eta$. Both numerator and denominator contain the factor $(1+\eta)(1+g)C_t$, which cancels:

$$\frac{c^H_{post}}{c^H_{no\text{-}transfer}} = \frac{\phi\alpha + \tau(1-\delta_0\tau)(1-\phi\alpha)}{\phi\alpha} = 1 + \frac{\tau(1-\delta_0\tau)(1-\phi\alpha)}{\phi\alpha}$$

This is an exact identity for any $\eta > 0$. The limit is vacuous — the expression does not converge to this value, it equals it always. The paper claims the ratio "converges to a finite constant," which is misleading. The formula itself is correct, and the paper's separate claim that the *level* of consumption grows without bound as $\eta \to \infty$ is also correct. But the limit notation adds no information and misrepresents the result as a convergence statement.

## Summary of Issues

| # | Issue | Severity | Req |
|---|-------|----------|-----|
| 1 | Vacuous $\lim_{\eta\to\infty}$ in eq (11) — ratio is $\eta$-independent | MEDIUM | R3 |
| 2 | P/D convergence condition unstated; binds tightly at calibration grid edge (F4) | MEDIUM | R2 |
| 3 | Positive singularity could violate $\alpha_t + \theta_t \leq 1$ (F2) | MEDIUM | R2 |
| 4 | "Social surplus" referenced without formal definition | LOW | R1/R3 |
| 5 | SDF referenced without symbol assignment | LOW | R1 |
| 6 | Various minor gaps (F1, F3, F6, F7) | LOW | R2 |
