# tests/factcheck-theory.py
Started: 2026-04-04 23:45:08 EDT
Runtime: 6m 32s
[ralph-garage/agent-logs/20260404T234508.986317-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260404T234508.986317-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually compatible, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

26 symbol families were cataloged across the entire paper (body, extensions, and appendix). The notation is clean and internally consistent. Each symbol carries a single, stable meaning throughout the paper.

**Minor issues noted (none substantive):**

1. **$u(\cdot)$ never formally defined.** The per-period utility function $u(\cdot)$ is used in the Appendix veto proof (eqs A.5–A.7) but is never formally defined. The reader can infer $u(c) = c^{1-\gamma}/(1-\gamma)$ from eq (1), but this is left implicit.

2. **Letter $N$ overloaded.** As a superscript, $N$ denotes "non-AI" ($D^N$, $P^N$, $H^N$); as a subscript in the Appendix, $N$ denotes "pre-singularity" ($\pi_N^i$). These are different semantic roles. The collision is contained — the expression $\pi_N^N$ never appears — but it is latent. Fix: rename $\pi_N^i$ to $\pi_0^i$.

3. **$\pi$ notation in Appendix vs. $P/D$ in body.** The Appendix introduces $\pi_S$ and $\pi_N^i$ as proof-local P/D variables. The relationship $\pi_S = V_\infty$ is stated, but $\pi_N^i = P^i/D^i$ is only implicit.

None of these issues create actual ambiguity in any expression that appears in the paper.

## Requirement 2: Assumption Consistency — PASS

36 assumptions were identified across the baseline model, three extensions, and the appendix proofs. All are mutually consistent.

**Key consistency checks performed:**

- **Parameter restrictions compatible.** $\beta \in (0,1)$, $\gamma > 1$, $g > 0$ automatically imply $R = \beta(1+g)^{1-\gamma} < 1$. All share parameters ($\alpha, \alpha_S, \phi$) are on valid domains. $\Lambda = (1-\phi)G$ can be either above or below 1, and the paper correctly handles both cases.
- **Budget constraint satisfied.** Pre-singularity: $C_t = D_t^A + D_t^N = Y_t$. Post-singularity: $C_{\tau+k} = Y_{\tau+k}^{\text{pub}} = (1-\phi)GY_0(1+g)^{\tau+k}$. The accounting identity $Y_t^{\text{total}} = Y_t^{\text{pub}} + Y_t^{\text{private}}$ holds in all states.
- **Dividend jumps consistent with hedge factors.** AI dividend jump $D_{\tau+1}^A/D_\tau^A = (\alpha_S/\alpha)\Lambda(1+g)$ correctly yields $H^A = (\alpha_S/\alpha)\Lambda^{1-\gamma}$ through the Euler equation.
- **Extensions reduce to baseline.** Transfers ($\theta=0$), veto ($\kappa=0$), extinction ($q=0$) all recover baseline formulas.
- **Complete markets benchmark consistent.** $\Lambda^{CM} = G$ correctly removes the $(1-\phi)$ displacement factor.
- **Algebraic derivations verified.** $V_\infty - V_0 = pR/[(1-R)(1-(1-p)R)]$, spread formula, and amplification factor $(1-\phi)^{1-\gamma}$ all check out.

**Minor observations (not inconsistencies):**

- $\alpha_S < 1$ is implicit rather than stated.
- "Zero utility" in the extinction extension should more precisely say "zero continuation value."
- The veto cost accounting (where does $\kappa Y_t$ go?) is left unspecified, but the extension is qualitative.

## Requirement 3: Traceability — PASS

All mathematical objects trace back to the assumptions.

**Primitive objects (defined in assumptions):** $\beta$, $\gamma$, $C_t$, $Y_t$, $Y_0$, $g$, $\alpha$, $\alpha_S$, $p$, $\tau$, $G$, $\phi$, $\theta$, $\delta$, $\kappa$, $q$.

**Derived objects (all traceable):**

| Object | Derived from |
|--------|-------------|
| $\Lambda = (1-\phi)G$ | $\phi$, $G$ |
| $R = \beta(1+g)^{1-\gamma}$ | $\beta$, $g$, $\gamma$ |
| $V_0 = (1-p)R/[1-(1-p)R]$ | $p$, $R$ |
| $V_\infty = R/(1-R)$ | $R$ |
| $H^A = (\alpha_S/\alpha)\Lambda^{1-\gamma}$ | $\alpha_S$, $\alpha$, $\Lambda$, $\gamma$ |
| $H^N = ((1-\alpha_S)/(1-\alpha))\Lambda^{1-\gamma}$ | $\alpha_S$, $\alpha$, $\Lambda$, $\gamma$ |
| $P^i/D^i = (1-H^i)V_0 + H^iV_\infty$ | Euler equation + all primitives |
| Spread $= (H^A - H^N)(V_\infty - V_0)$ | Difference of P/D ratios |
| $\Lambda(\theta,\delta)$ | $\phi$, $G$, $\theta$, $\delta$ |
| $\Lambda^{CM} = G$ | $G$ |
| $\bar{\kappa}$ | Implicitly defined from $u$, $\Lambda$, $p$ |

**Verification of key derivation chain:** The pre-singularity Euler equation yields $\pi_N^i = (1-p)R(\pi_N^i + 1) + pRH^i(V_\infty + 1)$, which solves to $\pi_N^i = (1-H^i)V_0 + H^iV_\infty$. The extinction extension correctly scales $H^i$ by $(1-q)$, yielding $[1-(1-q)H^i]V_0 + (1-q)H^iV_\infty$. No expression in the paper fails to derive from the stated assumptions.
