# tests/factcheck-theory.py
Started: 2026-04-02 22:28:07 EDT
Runtime: 6m 1s
[ralph-garage/agent-logs/20260402T222807.259950-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T222807.259950-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency

**PASS.** 25 symbol families were catalogued. All conventions (tilde = post-singularity, superscripts A/N/P = asset type, subscripts pre/post/CM = regime) are introduced explicitly and applied uniformly. No true collisions or ambiguities found.

Minor observations (none rising to failure):
- LaTeX source uses `\text{CM}` in one place and `\mathrm{CM}` elsewhere; renders identically.
- $R$ denotes a discount-factor composite rather than a gross return (conventional finance meaning), but is explicitly defined.
- The letter $P$ serves as both the price base symbol and the "private" superscript, but $P_t^P$ never appears.

## Requirement 2: Assumption Consistency

**PASS.** 18 assumptions identified (3 formal, 4 parameter domain restrictions, 9 implicit structural, 2 proposition-level conditions). All are mutually consistent.

Key checks:
- A1 ($\tilde{\omega} < \omega$) and A2 ($\tilde{\theta} > \theta$, $\tilde{\nu} < \nu$) are logically independent and jointly satisfiable: the non-AI loss must exceed the AI gain, with the difference captured by private capital.
- A3 (existence conditions) is redundant given $\gamma > 1$, $\beta \in (0,1)$, and $g > 0$; the paper correctly notes this.
- A14 (incomplete markets) and A18 (complete markets) are not imposed simultaneously; A18 is a counterfactual.
- The numerical example ($\beta=0.96, \gamma=3, g=0.02, \tilde{g}=0.05, \theta=0.05, \tilde{\theta}=0.15, \nu=0.55, \tilde{\nu}=0.30$) satisfies all restrictions simultaneously, serving as a constructive witness.

## Requirement 3: Traceability of Mathematical Objects

**PASS.** Every mathematical expression in the paper traces back to the model primitives ($p, \beta, \gamma, g, \tilde{g}, \theta, \tilde{\theta}, \nu, \tilde{\nu}$) and the Euler equation.

### Derived objects and their provenance

| Object | Defined from |
|--------|-------------|
| $\omega, \tilde{\omega}, \Delta$ | Output share parameters $\theta, \tilde{\theta}, \nu, \tilde{\nu}$ |
| $R$ | $\beta, g, \gamma$ |
| $\Phi^A$ | $\beta, \Delta, \gamma, \tilde{g}, \tilde{\theta}, \theta$ |
| $\Phi^N$ | $\beta, \Delta, \gamma, \tilde{g}, \tilde{\nu}, \nu$ |
| $V_{\mathrm{post}}$ | $\beta, \tilde{g}, \gamma$ via Euler equation |
| $V_{\mathrm{pre}}^A, V_{\mathrm{pre}}^N$ | $p, R, \Phi^{A/N}, V_{\mathrm{post}}$ via Euler equation |
| $\Phi^{A,\mathrm{CM}}, V_{\mathrm{pre}}^{A,\mathrm{CM}}$ | Complete-markets counterfactual (removes $\Delta^{-\gamma}$) |
| $V_{\mathrm{pre}}^{A,q}$ | Adds extinction parameter $q$; multiplies singularity term by $(1-q)$ |
| $F, \tau, T$ | Self-contained extension parameters (Sec 4.2) |
| $\mathcal{N}(p), \mathcal{D}(p)$ | Proof-local auxiliaries for Prop. 2 |

### Derivation verification

- **Proposition 1:** Euler equation expanded over two states (no-singularity with prob $1-p$, singularity with prob $p$). Consumption growth and dividend growth in each state follow from the assumptions. Solving the fixed-point equation for $V_{\mathrm{pre}}^A$ yields the closed-form expression. Verified correct.
- **Proposition 2:** Quotient rule applied to $V_{\mathrm{pre}}^A = \mathcal{N}(p)/\mathcal{D}(p)$. The numerator of the derivative simplifies to $\Phi^A(1+V_{\mathrm{post}})(1-R) - R$, giving the stated if-and-only-if condition. The identity $R/(1-R) = V_{\mathrm{pre}}^A\big|_{p=0}$ is the standard Gordon growth formula. Verified correct.
- **Proposition 3:** Under complete markets, household consumption equals total output, so singularity-state consumption growth is $(1+\tilde{g})$ rather than $\Delta(1+\tilde{g})$. This removes $\Delta^{-\gamma}$ from $\Phi^A$. The hedging premium follows by subtraction. Verified correct.
- **Eq. (18) (extinction):** Extinction state contributes zero to asset values (by stated convention). Singularity contribution is multiplied by $(1-q)$. Verified correct.

No expression in the paper fails to derive from the stated assumptions and model structure.
