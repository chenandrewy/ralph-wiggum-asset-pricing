# tests/factcheck-theory.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 7m 35s
[ralph-garage/agent-logs/20260412T095842.938480-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260412T095842.938480-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

26 symbol families were identified and checked for internal consistency, cross-family collisions, and semantic stability. Every symbol family denotes a single formal object throughout the paper. Variants within families follow transparent conventions (time indexing, asset-type superscripts, state-descriptor subscripts, or explicitly defined transformations). No symbol collisions or genuine ambiguities were found.

Key families: $\alpha$ (household share), $\phi$/$\phi_\text{eff}$ (displacement), $\theta$ (AI dividend share), $\gamma$ (risk aversion), $\beta$ (discount), $\eta$ (productivity jump), $\xi$ (extinction), $\delta$ (deadweight), $\kappa$ (veto cost), $\tau$ (tax rate), $C$/$c^H$ (consumption), $P$/$D$ (prices/dividends), $\Gamma$ (dividend growth factors), $U$/$u$/$V$ (utility hierarchy), $A$/$B$/$S$/$f$/$v$ (proof auxiliaries).

Three minor stylistic observations (implicit $N$ = "Non-AI" convention, asymmetric $v^{AI}$ without $v^N$ in the appendix, shift from time-subscript to state-descriptor subscript on $c^H$) do not rise to genuine ambiguity.

Detailed report: `ralph-garage/scratch/factcheck-notation.md`.

## Requirement 2: Assumption Consistency — PASS

50+ assumptions were cataloged across 7 categories (parameter restrictions, structural, behavioral, probability, market structure, extension-specific, calibration). All are mutually consistent:

1. **Parameter restrictions**: 15 explicit restrictions on distinct objects, no contradictions.
2. **Probability structure**: Probabilities sum to 1 at every branching node (baseline 3-branch tree and Extension 1 4-branch tree). All non-negative.
3. **Dynamics**: $\alpha_t$ and $\theta_t$ remain in $(0,1)$ under all singularity paths including repeated events.
4. **Extensions vs. baseline**: Extension 1 nests the baseline (set $q=0$). Extension 2 modifies post-singularity allocation without altering aggregate dynamics.
5. **Complete markets**: The claim $\phi_\text{eff} = 1$ under complete markets is consistent; veto part (ii) follows correctly from $\eta > 0$.
6. **Veto proof**: The limit argument ($\gamma \to \infty$) is valid under $\phi(1+\eta) < 1$, which the calibration satisfies ($0.75 < 1$).
7. **Transfer accounting**: Full consumption accounting verified algebraically — household + AI owners + deadweight loss = aggregate output. Numerical claims verified (e.g., $3.5\times$ consumption multiple at $\delta = 0.9$, $\tau = 0.30$).
8. **Existence condition**: $A^j < 1$ verified for baseline calibration; $A^{AI} > 1$ verified for large singularity without transfers — both as claimed.

One minor observation (not an inconsistency): the deadweight specification implicitly requires $\delta\tau < 1$, which is guaranteed for all numerical examples but not formally restricted when $\delta > 1$.

Detailed report: `ralph-garage/scratch/factcheck-assumptions.md`.

## Requirement 3: Traceability — PASS

All mathematical objects in the paper trace back to declared assumptions and parameters:

| Expression | Objects Used | Source |
|-----------|-------------|--------|
| P/D ratios (eqs 4–5) | $\beta, g, \gamma, p, \xi, \eta, \phi, \Gamma^{AI}, \Gamma^N$ | Assumptions A1–A10, B2–B7 |
| $\Gamma^{AI}, \Gamma^N$ (Prop 1) | $\theta, \Delta\theta, \eta$ | Assumptions A5–A7, B7, B10 |
| $A^j$ (Remark 1, eq 6) | Same as P/D numerator | Same as P/D |
| $B, S, f(A)$ (Prop 2 proof) | $\beta, g, \gamma, \eta, \phi, A$ | Local proof definitions from assumptions |
| $\Delta u(\gamma)$ (eq 9) | $q, \alpha^+, \alpha, \phi, \eta$ | Assumptions A8, A11, A12, F1 |
| $V_\text{veto}, V_\text{develop}, V_\text{develop}^{CM}$ (Prop 3) | $\beta, p, \xi, q, \alpha, \phi, \eta, \kappa, \gamma, g$ | Assumptions A1–A5, A8–A13, F1, F3, F4 |
| $c^H_{post}$ (eq 6) | $\phi, \alpha, \eta, C_t, g, \tau, \delta$ | Assumptions A2, A5, A8, A14, A15, B3, F5, F6 |
| $\phi_\text{eff}$ (eq 7) | $\phi, \tau, \delta, \alpha$ | Assumptions A2, A8, A14, A15 |
| Transfer ratio (eq 8) | $\tau, \delta, \phi, \alpha$ | Same as $\phi_\text{eff}$ |
| Euler equation (eq 10) | $\beta, \gamma, c_t^H, P_t^j, D_t^j$ | Assumptions C1, C2, E1, E3 |

No orphan mathematical objects were found. Every derived quantity is built from primitives declared in the model setup or extensions.
