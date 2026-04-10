# tests/factcheck-theory.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 7m 32s
[ralph-garage/agent-logs/20260409T202148.475370-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.475370-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS

REASON: All notation is consistent with no symbol collisions, all assumptions are mutually consistent, and all mathematical objects trace to the assumptions; moderate prose-formula mismatch in transfer base description and minor implicit conditions are noted but do not constitute mathematical errors.

## Requirement 1: Notational Consistency — PASS

The paper uses approximately 20 distinct base symbols, each with a single economic meaning throughout. No symbol is reused for a different formal object, and no two different symbols denote the same object without explicit equivalence.

**Findings:**

1. **MODERATE — Transfer base prose/formula mismatch (lines 240 vs. 243).** The prose describes the tax as levied on "AI owners' surplus," but eq. (6) taxes $(1 - \phi\alpha)$ of post-singularity output — all non-household consumption, including public AI stock dividends. In the model setup (line 111), AI owners specifically hold private capital with dividends $(1-\alpha_t - \theta_t)C_t$, a proper subset. The formula is broader than the prose description.

2. **MINOR — Implicit stationarity convention.** The stochastic processes $\alpha_t$ and $\theta_t$ silently become fixed parameters $\alpha$ and $\theta$ (dropping time subscripts) when moving from the general setup to equilibrium pricing and extensions. Standard practice but never stated.

3. **NEGLIGIBLE — Dual P/D notation.** The P/D ratio is $P^{AI}/D^{AI}$ in propositions and $v^{AI}$ in the proof. Explicitly equated at line 293. No real confusion.

## Requirement 2: Assumption Consistency — PASS

All mathematical assumptions are mutually consistent. Detailed checks performed:

- **Parameter restrictions**: No contradictions among interval restrictions on distinct parameters.
- **Probability structure**: Well-defined and sums to 1 in all branches (baseline and extensions).
- **Budget constraints**: Satisfied. Post-transfer budget accounts for household consumption, AI owner consumption, and deadweight loss as resource destruction.
- **Domain restrictions**: $\alpha_t \in (0, 1-\theta_t]$ preserved across singularities under implicit condition $\phi \leq 1 - \Delta\theta$ (satisfied by all calibrations).
- **Baseline/extension compatibility**: Extension 1 reduces to baseline at $\lambda = 0$; Extension 2 reduces to baseline at $\tau = 0$.
- **Euler equation algebra**: Verified correct (Appendix A).
- **Existence condition**: Numerically verified for large-singularity calibration ($A^{AI} = 2.37 > 1$, consistent with paper's claim).
- **Consumption ratio independence of $\eta$**: Verified algebraically.
- **$\phi_\text{eff}$ formula**: Consistent with eq. (6).

**Findings:**

1. **MODERATE — Transfer base mismatch (same as notation finding).** Eq. (6) taxes $(1 - \phi\alpha)$ of post-singularity output (all non-household consumption), but the prose says "AI owners' surplus." The equations are self-consistent; the verbal description is narrower than the formula. Fix: change prose to "non-household consumption."

2. **MINOR — Implicit domain-preservation condition.** The constraint $\alpha_t \in (0, 1-\theta_t]$ is preserved across repeated singularities only if $\phi \leq 1 - \Delta\theta$. Satisfied by all calibrations (baseline: $0.5 \leq 0.8$; large singularity: $0.05 \leq 0.8$) but never stated.

3. **MINOR — Implicit feasibility condition $\delta\tau < 1$.** Required for positive net transfers. Satisfied by calibration ($\delta = 0.5$, $\tau < 1$) but not formally assumed.

4. **MINOR — Positive singularity lacks functional form.** Extension 1 assumes $\alpha_{t+1} > \alpha_t$ (line 213) without specifying a formula, unlike the negative case ($\alpha_{t+1} = \phi\alpha_t$). Sufficient for the qualitative Proposition 3 but prevents quantitative analysis.

5. **NEGLIGIBLE — Stationarity approximation acknowledged.** The proof (line 307) treats the post-singularity P/D ratio as approximately equal to the pre-singularity ratio. The paper acknowledges this is an approximation.

## Requirement 3: Traceability — PASS

All mathematical objects in the paper's results trace back to explicitly stated assumptions:

| Object | Source |
|--------|--------|
| $\beta, \gamma$ | Preference assumptions (C1, line 114) |
| $g$ | Consumption growth (A2, line 81) |
| $p$ | Singularity probability (A5, line 90) |
| $\xi$ | Extinction probability (A6, line 93) |
| $\eta$ | Productivity boost (A7, line 93) |
| $\phi$ | Displacement parameter (A8, line 95) |
| $\alpha_t$ | Household share (A3, line 87) |
| $\theta_t, \Delta\theta$ | AI dividend share (B1, line 107) |
| $\Gamma^{AI}, \Gamma^N$ | Derived from $\theta, \Delta\theta, \eta$ (line 135) |
| $A^j$ | Derived from $\beta, g, \gamma, p, \xi, \eta, \phi, \Gamma^j$ (line 145) |
| $v^{AI}$ | Defined as $P^{AI}/D^{AI}$ (line 293) |
| $\lambda$ | Extension 1 assumption (E1, line 212) |
| $\tau, \delta$ | Extension 2 assumptions (F1-F2, line 240) |
| $\phi_\text{eff}$ | Derived from $\phi, \tau, \delta, \alpha$ (line 248) |
| $U_\text{ext}$ | Normalization assumption (C2, line 219) |

No expression in the paper's propositions, corollaries, remarks, or extension formulas references an object that is not traceable to an explicitly stated assumption.
