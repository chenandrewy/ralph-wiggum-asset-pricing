# tests/factcheck-theory.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 10m 18s
[ralph-garage/agent-logs/20260409T190308.208787-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T190308.208787-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: FAIL

REASON: The P/D formula (Proposition 1) requires an unstated existence condition that the paper's own Extension 2 calibration violates, producing undefined price-dividend ratios.

---

## Requirement 1: Notational Consistency — PASS

No symbol collisions found. All 22 symbol families were catalogued; no symbol is reused for a different formal object anywhere in the paper.

**Minor issues (not failures):**
- $\alpha_t$ and $\theta_t$ silently lose their time subscripts in Section 4 and the $\Gamma$ definitions (standard but unstated convention).
- $\Delta\theta$ is a parameter, not the actual change $\theta_{t+1} - \theta_t$, while $\Delta U^H$ uses $\Delta$ as a genuine difference. Semantic inconsistency in the $\Delta$ prefix, but $\Delta\theta$ is explicitly defined.
- $c^H_{no\text{-}transfer}$ used in Eq (7) without standalone definition.
- $u_\text{ext}$ appears in prose without formal definition.
- $\delta_0$ has an unexplained subscript (no $\delta_1$ exists).

**Conclusion:** These are minor stylistic imperfections. No ambiguity that would cause a reader to confuse one formal object with another.

---

## Requirement 2: Assumption Consistency — PASS

44 assumptions catalogued across 6 categories. No contradictions found between any pair of stated assumptions.

- All parameter domains are mutually compatible.
- All probability trees sum to 1.
- Accounting identities hold ($\alpha_t C_t + (1-\alpha_t)C_t = C_t$; $\theta_t C_t + (1-\theta_t)C_t = C_t$).
- Extinction utility normalization ($u_\text{ext} = 0$) is internally consistent.
- Extensions nest the baseline (set $\lambda = 0$ or $\tau = 0$).
- Comparative statics (Proposition 2) are consistent with the model structure.
- Transfer ratio (Eq 7) correctly derived from Eq (6) and is $\eta$-independent as claimed.
- $\theta_t$ dynamics preserve $\theta_t \in (0,1)$.

**Unstated restrictions (not contradictions, but omissions):**
1. $\phi \leq 1 - \Delta\theta$ is needed for the domain $\alpha_t \leq 1-\theta_t$ to be preserved after singularities when $\alpha_t$ is at its upper bound. All calibrations satisfy it. Severity: low.
2. Extension 1 does not specify $\theta$ dynamics in a positive singularity and does not bound $\phi^+$. Severity: low (Extension 1 is qualitative).
3. No constraint ensures $\delta_0 \tau < 1$, needed for net transfers to be positive. Severity: low.

**Conclusion:** The stated assumptions are mutually consistent. The omissions are parameter-domain gaps, not contradictions.

---

## Requirement 3: Traceability — FAIL

### Objects traced successfully

All primitive parameters are defined in the assumptions: $\beta, g, \gamma, p, \xi, \eta, \phi, \Delta\theta, \theta, \alpha, \lambda, \phi^+, \kappa, \tau, \delta_0$.

The following derived objects are fully traceable to the assumptions:
- $\Gamma^{AI} = \frac{\theta + \Delta\theta(1-\theta)}{\theta}(1+\eta)$ — from $\theta, \Delta\theta, \eta$.
- $\Gamma^{N} = \frac{1-\theta-\Delta\theta(1-\theta)}{1-\theta}(1+\eta)$ — from $\theta, \Delta\theta, \eta$.
- $\Delta U^H$ (Eq 5) — from $p, \xi, \lambda, \phi^+, \phi, \alpha, \eta, g, C_t, u(\cdot)$.
- $c^H_{post}$ (Eq 6) — from $\phi, \alpha, \eta, C_t, g, \tau, \delta_0$.
- Transfer ratio (Eq 7) — derived from Eq 6.

### Critical failure: P/D formula existence condition

The P/D formula (Proposition 1, Eqs 4–4b) has the form $A/(1-A)$ where:

$$A = \beta(1+g)^{1-\gamma}\left[(1-p) + p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^j\right]$$

This formula produces a valid (positive, finite) price-dividend ratio only when $A < 1$. **This condition is never stated as an assumption.**

**The paper's own Extension 2 calibration violates it.** Using $\eta = 9$, $\phi = 0.05$, $p = 0.005$, $\xi = 0.05$, $\theta = 0.15$, $\Delta\theta = 0.2$, $\beta = 0.96$, $g = 0.02$, $\gamma = 4$:

| Asset | $\Gamma^j$ | $A$ | $A < 1$? |
|-------|-----------|-----|----------|
| AI stocks | 21.33 | **2.37** | No |
| Non-AI stocks | 8.00 | **1.45** | No |

At $\tau = 0$ (no transfers), the P/D formula produces **negative** (meaningless) values for both asset classes under the large-singularity parameters. The formula diverges because the SDF-weighted expected dividend growth exceeds 1: the household's marginal utility in the singularity state ($\phi^{-\gamma} = 0.05^{-4} = 160{,}000$) is so extreme that the geometric pricing sum does not converge.

This matters because Extension 2's Figure 2 plots P/D ratios against $\tau$, and at $\tau = 0$ the formula should reduce to the baseline Proposition 1 formula — which is undefined at these parameters.

The baseline calibration ($\eta = 0.5$, $\phi = 0.5$) satisfies the condition: $A_{AI} = 0.94$, $A_N = 0.92$.

### Summary of untraceable expressions

| Expression | Issue |
|-----------|-------|
| $P^{AI}/D^{AI}$ (Eq 4) at $\eta=9, \phi=0.05$ | Requires unstated $A < 1$; violated by Extension 2 calibration |
| $P^{N}/D^{N}$ (Eq 4b) at $\eta=9, \phi=0.05$ | Same |

---

## Detailed Reports

- Notational consistency: `ralph-garage/scratch/factcheck-notation.md`
- Assumptions consistency: `ralph-garage/scratch/factcheck-assumptions.md`
