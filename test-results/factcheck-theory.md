# tests/factcheck-theory.py
Started: 2026-04-12 14:18:19 EDT
Runtime: 9m 26s
[ralph-garage/agent-logs/20260412T141819.070814-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260412T141819.070814-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to stated assumptions.

## Requirement 1: Notational Consistency — PASS

28 symbol families were identified across the full paper. Every family maintains a stable invariant meaning throughout. No symbol is reused for a different formal object, semantic role, or model without explicit redefinition.

Key checks:
- $\alpha_t$ (household consumption share) vs. $\theta_t$ (AI dividend share) are explicitly distinguished (line 108) and never conflated.
- $\phi$ vs. $\phi_\text{eff}$: the effective displacement parameter is explicitly defined and the substitution into Proposition 1 is clearly stated.
- Uppercase $C$ (aggregate consumption) vs. lowercase $c$ (household consumption): standard convention, explicitly defined.
- $U$ (lifetime utility) vs. $u$ (per-period utility): standard convention.
- $V$ (value functions in Extension 1) vs. $v$ (P/D ratio in Appendix A): distinguished by case and context, both explicitly defined where introduced.
- $\delta$ is used for deadweight cost severity rather than the discount factor convention ($\beta$ is the discount factor). Internally consistent.
- $\Delta\theta$ (share jump) vs. $\Delta u$ (utility change): both use $\Delta$ prefix for different objects, but no reader confusion is possible.

Two minor stylistic notes (not errors): (1) $\delta$ may briefly confuse readers expecting it as a discount factor; (2) $V/v$ use the same letter family for different objects, separated by case and section.

Full audit: `/ralph-garage/scratch/factcheck-notation.md`

## Requirement 2: Mutual Consistency of Assumptions — PASS

36 assumptions were cataloged across all sections (setup, propositions, extensions, appendix, calibration). All are mutually consistent.

Key consistency checks performed:
1. **Parameter domains**: All 14 parameters have calibration values strictly within stated domains.
2. **Displacement condition** $\phi(1+\eta) < 1$: Holds for all three parameterizations (baseline 0.75, large singularity 0.5, veto example 0.75).
3. **Existence condition** $A^j < 1$: Verified numerically for baseline ($A^{AI} \approx 0.944$, $A^N \approx 0.916$). Correctly violated for large singularity without transfers ($A^{AI} \approx 2.37$), consistent with the paper's claim that P/D is undefined at $\tau = 0$.
4. **Budget constraint**: $D^{AI} + D^N = C_t$ holds by construction ($\theta_t C_t + (1-\theta_t)C_t = C_t$).
5. **Dividend growth factors**: $\Gamma^{AI} > 1+\eta > \Gamma^N$ verified algebraically. $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is $\theta$-independent, confirming the Appendix claim.
6. **Extension 1 vs. baseline**: The $\min(1, \alpha/\phi)$ cap prevents $\alpha > 1$. At $\alpha = 0.70$, $\phi = 0.5$: $\alpha^+ = 1$ (household gets everything), a boundary case handled by the $\min$ function.
7. **Extension 2 transfers**: $\phi_\text{eff}$ derivation verified algebraically. The $3.5\times$ consumption multiple claim ($\delta = 0.9$, $\tau = 0.30$) verified numerically ($\approx 3.52$). Net transfer per dollar taxed $= 0.219$ verified.
8. **Proposition 2 proof**: $A^j > 1/2$ condition satisfied across parameterizations. Semi-elasticity $1/[A(1-A)]$ is increasing for $A > 1/2$, and since $A^{AI} > A^N$ with larger absolute reductions in $A^{AI}$, the ratio decreases in $\xi$.
9. **Normalizations**: $U_\text{ext} = 0$ is conservative since CRRA utility is negative for $\gamma > 1$.

Full audit: `/ralph-garage/scratch/factcheck-assumptions.md`

## Requirement 3: Traceability of Mathematical Objects — PASS

All derived mathematical objects trace back to stated assumptions (primitives: $\beta, g, \gamma, \phi, \eta, p, \xi, \theta, \Delta\theta, \alpha, q, \kappa, \tau, \delta, C_t$).

Derived objects and their traceability:

| Object | Traces to |
|--------|-----------|
| $\Gamma^{AI}, \Gamma^N$ | $\theta, \Delta\theta, \eta$ (dividend definitions + singularity dynamics) |
| $A^j$ | $\beta, g, \gamma, p, \xi, \eta, \phi, \Gamma^j$ (Remark 1 definition) |
| $P^{AI}/D^{AI}, P^N/D^N$ | Euler equation + all baseline primitives |
| $v^{AI}$ | Notation for $P^{AI}/D^{AI}$ |
| $B, S, f(A)$ | Proof auxiliaries from $\beta, g, \gamma, \phi, \eta$ |
| $V_\text{veto}, V_\text{develop}, V_\text{develop}^{CM}$ | Lifetime utility under different regimes |
| $\bar{\gamma}$ | Threshold from veto condition ($\Delta u(\gamma) \to -\infty$) |
| $\Delta u(\gamma)$ | $q, \alpha, \phi, \eta, \gamma$ (eq:veto-delta-u) |
| $\alpha^+$ | $\min(1, \alpha/\phi)$ |
| $c^H_{post}, c^H_\text{no-transfer}$ | $\phi, \alpha, \eta, g, C_t, \tau, \delta$ (transfer mechanism) |
| $\phi_\text{eff}$ | $\phi, \tau, \delta, \alpha$ (eq:phi-eff) |

Key derivation checks:
- **Proposition 1**: Euler equation expansion (lines 308-311) is algebraically correct. The $(1+g)^{-\gamma} \cdot (1+g)$ factors combine to $(1+g)^{1-\gamma}$, and $[\phi(1+\eta)]^{-\gamma}$ correctly decomposes into $\phi^{-\gamma}(1+\eta)^{-\gamma}$.
- **Proposition 2**: The semi-elasticity argument is valid. Both $\Gamma^{AI}/[A^{AI}(1-A^{AI})]$ and $\Gamma^N/[A^N(1-A^N)]$ are the relevant quantities; since both numerator and denominator favor AI stocks, the ratio decreases in $\xi$.
- **Proposition 3(i)**: As $\gamma \to \infty$, $[\phi(1+\eta)]^{1-\gamma} \to \infty$ dominates the negative singularity term, making $\Delta u(\gamma) \to -\infty$.
- **Proposition 3(ii)**: Under complete markets, $u(\alpha(1+\eta)) > u(\alpha)$ for all $\gamma > 1$ since $\eta > 0$.
- **Transfer ratio (eq:transfer-ratio)**: $(1+\eta)(1+g)C_t$ cancels in numerator and denominator, confirming $\eta$-independence.

No expression was found that cannot be logically derived from the stated assumptions.
