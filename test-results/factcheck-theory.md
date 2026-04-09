# tests/factcheck-theory.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 6m 45s
[ralph-garage/agent-logs/20260409T184838.241906-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T184838.241906-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to stated assumptions.

## Requirement 1: Notational Consistency — PASS

The paper uses 26 symbol families. No collisions, reuse for different formal objects, or substantive ambiguities were found.

**Minor observations (non-failing):**
- Time subscripts on $\alpha$ and $\theta$ are dropped in Sections 3–4 (standard practice in stationary/one-period contexts).
- $\delta_0$ uses an unmotivated subscript "0" (unambiguous but mildly unconventional).
- $v^N$ for non-AI P/D ratio is implicitly rather than explicitly defined.

Full notation audit: `ralph-garage/scratch/factcheck-notation.md`

## Requirement 2: Mutual Consistency of Assumptions — PASS

22 structural assumptions, 9 parameter restrictions, 10 Extension 1 assumptions, 4 Extension 2 assumptions, and 4 implicit proof assumptions were cataloged. No contradictions found.

**Budget constraints** balance exactly, including under government transfers (verified algebraically).

**Extensions** branch cleanly off the baseline with no conflicts (Extension 1 augments the singularity with positive/negative types; Extension 2 adds transfers).

**Missing regularity conditions (non-contradictions):**
1. Convergence condition for P/D formula ($A < 1$ in denominator) is not stated. Fails for $p \gtrsim 2\%$ with $\xi = 0$ under the calibration.
2. The condition $\phi + \Delta\theta \leq 1$ (needed to preserve $\alpha_t \leq 1 - \theta_t$ after singularity) is implicit. Holds for the calibration ($0.5 + 0.2 = 0.7 \leq 1$).
3. No upper bound on $\phi^+$ ensures $\alpha_t \leq 1 - \theta_t$ after a positive singularity in Extension 1.
4. The deadweight cost feasibility condition $\delta_0 \tau < 1$ is economically necessary but not stated.
5. The stationarity approximation (post-singularity P/D ≈ pre-singularity P/D) is explicitly acknowledged as approximate.
6. The $0 \times \infty$ product in the extinction-state Euler equation is handled by convention (standard in the rare disasters literature) but not discussed.

These are standard omissions in theoretical asset pricing, not logical contradictions between assumptions.

Full assumption audit: `ralph-garage/scratch/factcheck-assumptions.md`

## Requirement 3: Traceability of Mathematical Objects — PASS

All mathematical objects in the paper trace back to the stated assumptions:

| Derived Object | Source Assumptions |
|---|---|
| $\Gamma^{AI}, \Gamma^{N}$ (dividend growth factors) | Dividend definitions (S13, S14, S16), $\Delta\theta$ (P7), $\eta$ (P5) |
| P/D ratios (Eqs. 4–5) | Euler equation (S20), CRRA preferences (S19), consumption process (S5, S6, S8–S12), stationarity (S21–S22) |
| Corollary 1 (valuation spread) | P/D formula structure + $\Delta\theta > 0$ (P7) |
| Proposition 2 (comparative statics) | P/D formula + parameter restrictions (P6, P8) |
| $\Delta U^H$ (Eq. 9, veto gain) | $p$ (S8), $\xi$ (S9), $\lambda$ (E3), $\phi^+$ (E1), $\phi$ (P6), $\alpha$ (S6), $\eta$ (P5), $g$ (P1), $u(\cdot)$ (S19, E9) |
| $c^H_{post}$ (Eq. 12, transfer consumption) | $\phi$ (P6), $\alpha$ (S6), $\eta$ (P5), $g$ (P1), $\tau$ (T1), $\delta_0$ (T3) |
| Transfer ratio (Eq. 13) | Algebraic consequence of Eq. 12 |

No expression was found that cannot be logically derived from the assumptions.
