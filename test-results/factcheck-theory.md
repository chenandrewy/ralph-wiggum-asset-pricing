# tests/factcheck-theory.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 8m 56s
[ralph-garage/agent-logs/20260409T203927.593701-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T203927.593701-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions with correct derivations.

## Requirement 1: Notational Consistency — PASS

22 symbol families were cataloged. No semantic collisions (same symbol used for different formal objects) were found. Four minor issues were identified, none creating genuine ambiguity:

1. **Undefined `u` (line 213):** The period utility function is referenced as `u` in the proof of Proposition 3 but never formally assigned that symbol. The paper defines utility only inside the lifetime utility formula (line 116). Any asset pricing reader would resolve this unambiguously, but it is technically an omission.
2. **`\alpha` time subscript dropped (Section 4.2):** `\alpha_t` is used consistently in Section 2, but bare `\alpha` appears without comment in Section 4.2 (lines 227+). The context (single-period transfer analysis) makes the meaning clear.
3. **`\theta` time subscript dropped (line 134):** `\theta_t` is used in asset definitions (lines 106-107), but bare `\theta` appears in the $\Gamma$ definitions. The stationary-equilibrium context resolves this.
4. **Prime notation `(\alpha', \theta')` at line 291:** Introduced without definition in the appendix proof, constituting a third convention alongside time-subscripted and bare forms. Meaning is clear from context.

## Requirement 2: Assumption Consistency — PASS

30 mathematical assumptions were identified across Setup, Propositions, Calibration, and Extensions. All are mutually consistent:

- **Parameter restrictions:** All independent interval restrictions on distinct parameters; no conflicts. Calibration values satisfy all restrictions.
- **Probability tree:** $(1-p) + p\xi + p(1-\xi) = 1$. Well-defined.
- **Budget constraints:** Consumption shares sum to $C_t$; total dividends equal aggregate consumption; post-transfer resource accounting balances exactly (household + AI owners + deadweight loss = total output).
- **Extensions vs. baseline:** Extension 1 augments the singularity structure compatibly. Extension 2 reduces to baseline at $\tau = 0$.
- **Existence condition:** Correctly stated; satisfied for the baseline calibration grid. The large-singularity violation ($\eta = 9$, $\phi = 0.05$, $\tau = 0$) is correctly identified in the paper.
- **Share dynamics:** $\alpha_t \in (0,1)$ and $\theta_t \in (0,1)$ are preserved under repeated singularities.
- **Numerical claims verified:** $\phi(1+\eta) = 0.75$ (baseline), $\phi(1+\eta) = 0.5$ (large singularity), $\phi^{-\gamma} = 160{,}000$ — all correct.

**Minor observation:** At the large-singularity parameters ($\eta = 9$, $\phi = 0.05$, $\tau = 0$), both AI and non-AI P/D ratios are undefined ($A^{AI} \approx 2.37$, $A^{N} \approx 1.45$), but the paper (line 244) discusses only the AI stock P/D being undefined. This is an incomplete description, not a mathematical inconsistency.

## Requirement 3: Traceability — PASS

All mathematical objects in the paper trace back to the assumptions:

| Object | Traced to |
|--------|-----------|
| $\Gamma^{AI}, \Gamma^{N}$ | Defined from $\theta, \Delta\theta, \eta$ (Assumptions 9, 10, 7) |
| $A^j$ | Defined from $\beta, g, \gamma, p, \xi, \eta, \phi, \Gamma^j$ (Assumptions 2, 5-8, 13, 16) |
| P/D ratios (Prop. 1) | Derived from Euler equation via CRRA preferences + marginal investor (Assumptions 12, 13); derivation verified step-by-step |
| Comparative statics (Prop. 2) | Follow from P/D formulas by differentiation |
| Veto result (Prop. 3) | Follows from concavity of CRRA utility + incomplete markets (Assumptions 12, 13, 19-23) |
| $c^H_{post}$ (eq. 7) | Derived from $\phi, \alpha, \eta, g, C_t, \tau, \delta$ (Assumptions 2, 3, 7, 8, 24, 25) |
| Transfer ratio (eq. 8) | Derived from eq. 7; verified algebraically; correctly independent of $\eta$ |
| $\phi_\text{eff}$ | Derived from transfer consumption formula (Assumption 27) |
| $v^{AI}$ | Notation for P/D ratio in appendix proof |

No expression in the paper fails to derive from the stated assumptions. The one approximation (post-singularity P/D ratio treated as equal to pre-singularity P/D ratio, line 291) is explicitly acknowledged.
