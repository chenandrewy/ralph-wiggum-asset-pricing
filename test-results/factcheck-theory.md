# tests/factcheck-theory.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 7m 27s
[ralph-garage/agent-logs/20260409T215056.134463-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T215056.134463-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

A comprehensive audit of all mathematical symbols found no collisions, ambiguities, or inconsistencies. Key findings:

- **9 Greek-letter parameters** ($\alpha, \theta, \phi, \gamma, \beta, \eta, \xi, \delta, \tau$), each assigned to exactly one economic concept with no reuse.
- **Consumption convention** is clean: uppercase $C_t$ for aggregate, lowercase $c_t^H$ for household, with transfer variants ($c^H_{post}$, $c^H_{no\text{-}transfer}$) clearly scoped to Section 4.2.
- **Superscript convention** ($AI$, $N$, $H$, $j$) is stable throughout for asset type and agent identity.
- **Time subscripts** are used consistently ($t, t+1$) and dropped only in stationary-state analysis (Propositions 1–2, Section 4.2), which is standard.
- **Derived quantities** ($\Gamma^j$, $A^j$, $v^{AI}$, $\phi_\text{eff}$) are all explicitly defined at their point of introduction.
- **Proofs match propositions**: Appendix A uses the same objects as Proposition 1; the Proposition 2 proof correctly uses $A^j$ from Remark 1; the Proposition 3 proof is consistent with the model setup.
- The appendix claim that $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is $\theta$-independent was verified algebraically against the Proposition 1 definition — confirmed correct.
- **Minor observation**: The Proposition 3 proof uses informal $u$ for the period utility function without a formal definition, but this causes no confusion in context.

Full notation audit: `ralph-garage/scratch/factcheck-notation.md`

## Requirement 2: Assumption Consistency — PASS

All mathematical assumptions were catalogued (structural, parameter restrictions, distributional, equilibrium, normalizations, existence conditions, extension-specific) and checked pairwise. No contradictions found. Key verifications:

- **All calibration values** ($\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$, $\alpha=0.70$, $\delta=0.5$) satisfy their stated parameter domains.
- **Existence condition** ($A^j < 1$): Verified numerically for all baseline grid points ($A^{AI}$ ranges from 0.91 to 0.99). The intentional violation under large-singularity parameters ($\eta=9$, $\phi=0.05$) is explicitly discussed in the paper.
- **Extinction + utility**: CRRA with $\gamma > 1$ gives negative utility for all $c > 0$, so $U_\text{ext} = 0$ means extinction is "preferred." The paper correctly notes this makes the veto result conservative. The extinction state contributes zero to pricing equations, so the utility divergence at $c = 0$ never enters the math.
- **Transfer budget balance**: Verified algebraically — household consumption + AI owners' consumption + deadweight loss = total resources.
- **$\phi_\text{eff}$ derivation**: Correct algebraic division of Eq (5) by $\alpha(1+\eta)(1+g)C_t$.
- **Positive singularity** ($\alpha_{t+1} = \min(1, \alpha_t/\phi)$): Naturally inverts the negative singularity, preserves $\alpha \in (0,1]$, consistent with all parameter restrictions.
- **"Socially efficient"**: Well-defined as a utilitarian welfare criterion, stated as an assumption about parameters.
- **All proofs' assumptions match their propositions.**

Full assumptions audit: `ralph-garage/scratch/factcheck-assumptions.md`

## Requirement 3: Traceability — PASS

All mathematical objects in the paper trace back to assumed primitives:

| Object | Traced to |
|--------|-----------|
| $c_t^H = \alpha_t C_t$ | $\alpha_t$, $C_t$ |
| $D_t^{AI} = \theta_t C_t$ | $\theta_t$, $C_t$ |
| $D_t^N = (1-\theta_t) C_t$ | $\theta_t$, $C_t$ |
| $U_0^H$ (Eq 3) | $\beta$, $\gamma$, $c_t^H$ |
| $\Gamma^{AI}$, $\Gamma^N$ | $\theta$, $\Delta\theta$, $\eta$ |
| $A^j$ (Remark 1) | $\beta$, $g$, $\gamma$, $p$, $\xi$, $\eta$, $\phi$, $\Gamma^j$ |
| $P^{AI}/D^{AI}$, $P^N/D^N$ (Prop 1) | Euler equation from all primitives |
| $v^{AI}$ (Appendix A) | Shorthand for $P^{AI}/D^{AI}$ |
| $\phi_\text{eff}$ (Eq 6) | $\phi$, $\tau$, $\delta$, $\alpha$ |
| $c^H_{post}$ (Eq 5) | $\phi$, $\alpha$, $\eta$, $C_t$, $g$, $\tau$, $\delta$ |
| Transfer ratio (Eq 7) | $\tau$, $\delta$, $\phi$, $\alpha$ |

No expressions were found that cannot be logically derived from the assumptions.
