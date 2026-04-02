# tests/factcheck-theory.py
Started: 2026-04-02 18:17:45 EDT
Runtime: 5m 52s
[ralph-garage/agent-logs/20260402T181745.335748-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T181745.335748-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS

REASON: All notation is consistent, all assumptions are mutually compatible, and all mathematical expressions trace back to stated assumptions and model primitives.

## Requirement 1: Notational Consistency — PASS

Every mathematical object was cataloged into 23 symbol families. Key findings:

- **Tilde convention** (post-singularity values: $\tilde{g}, \tilde{\theta}, \tilde{\nu}, \tilde{\omega}$) is applied uniformly.
- **Subscript convention** (0 = pre-singularity regime, 1 = post-singularity regime) is stable.
- **Superscript convention** ($A$ = AI stocks, $N$ = non-AI stocks, $P$ = private capital; $\text{CM}$ = complete markets, $q$ = extinction variant) is consistent.
- **No symbol collisions** between the main model (Sections 2–3) and the extension (Section 4).
- **Minor observations** (not failures):
  - The transition from $\Delta$ to $\Delta_0 / \Delta(\lambda)$ in Section 4.2 is adequate but could state explicitly that the main model corresponds to $\lambda = 0$.
  - The letter $A$ serves as both a superscript label (AI stocks) and a proof-local function name $A(p)$ in the Appendix; these are syntactically distinct and cause no confusion.

## Requirement 2: Assumption Consistency — PASS

Three formal assumptions and ten implicit assumptions were identified. All are mutually consistent:

- **Assumptions 1 and 2** are compatible: they require $\tilde{\theta} - \theta < \nu - \tilde{\nu}$ (the non-AI share decrease exceeds the AI share increase), which is feasible.
- **Assumption 3** (existence) is automatically satisfied for $\gamma > 1$ with positive growth rates and $\beta < 1$, as the paper correctly claims.
- **Output share constraints** are consistent in both regimes ($\theta + \nu < 1$, $\tilde{\theta} + \tilde{\nu} < 1$).
- **Extension parameters** ($q \in [0,1)$, $\lambda \in [0,1]$, $F > 0$, $\tau \geq 0$) reduce to the main model at boundary values and introduce no contradictions.
- **Numerical illustration** ($\beta = 0.96, \gamma = 3, g = 0.02, \tilde{g} = 0.05, \theta = 0.05, \tilde{\theta} = 0.15, \nu = 0.55, \tilde{\nu} = 0.30, p = 0.01$) satisfies all assumptions. All reported values match the formulas: $V_0^A = 16.10$ (paper: ~16.1), $V_0^N = 11.57$ (~11.6), $V_0^{A,\text{CM}} = 12.90$ (~12.9), hedging premium = 24.8% (~25%).

## Requirement 3: Traceability of Mathematical Objects — PASS

All mathematical expressions in the paper trace back to the stated assumptions, model primitives, or clearly introduced extension parameters:

| Expression(s) | Source |
|---|---|
| Eqs. 1–2 (output growth) | Environment primitives ($g, \tilde{g}$) |
| Eqs. 3–4 (dividends) | Output shares ($\theta, \nu, \tilde{\theta}, \tilde{\nu}$) + output $Y_t$ |
| Eq. 5 ($\Delta$) | Defined from $\omega = \theta + \nu$, $\tilde{\omega} = \tilde{\theta} + \tilde{\nu}$; sign from Assumption 1 |
| Eq. 6 (Euler equation) | Standard first-order condition from CRRA utility |
| Eq. 7 (equilibrium consumption) | Market clearing ($n_t^A = n_t^N = 1$) + dividend definitions |
| Eqs. 7–11 (Proposition 1: P/D ratios) | Euler equation + dividends + growth + consumption + Assumption 3 |
| Eq. 11 (Proposition 2: cross-section) | Subtraction of P/D formulas; sign from Assumption 2 |
| Eq. 13 (Proposition 3: comparative static) | Quotient rule on Eq. 7; algebra verified line-by-line |
| Eqs. 12, 14 (Proposition 4: complete markets) | Modified consumption ($c_t = Y_t$) removes $\Delta^{-\gamma}$ |
| Eq. 14 (extinction risk) | Scales singularity contribution by $(1-q)$; new parameter $q$ |
| Eq. 15 ($\Delta(\lambda)$) | Extension parameter $\lambda$; reduces to $\Delta_0$ at $\lambda = 0$ |
| Eq. 16 (friction cost) | Extension modeling parameters ($F, \tau, T$); limit argument |
| Remark 1 (extreme singularity) | Limit of $\Phi^A, V_1$ as $\tilde{g} \to \infty$ with $\gamma > 1$ |
| Remark 2 (Coase theorem) | Consequence of Eq. 16 in the limit $Y \to \infty$ |

No expression was found that cannot be logically derived from the assumptions and model setup.

## Appendix Proof Verification

The proof of Proposition 3 in the Appendix was verified algebraically:

1. $A'(p) = -R + \Phi^A(1+V_1)$ and $B'(p) = R$ — correct derivatives.
2. Numerator expansion: $[-R + \Phi^A(1+V_1)][1-(1-p)R] - [(1-p)R + p\Phi^A(1+V_1)]R$ simplifies to $\Phi^A(1+V_1)(1-R) - R$ — verified.
3. The condition $\Phi^A(1+V_1) > R/(1-R) = V_0^A|_{p=0}$ follows correctly.
