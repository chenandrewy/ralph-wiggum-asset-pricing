# tests/factcheck-theory.py
Started: 2026-04-11 21:27:07 EDT
Runtime: 9m 13s
[ralph-garage/agent-logs/20260411T212707.761027-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260411T212707.761027-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS

REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions, with minor formal gaps that do not create ambiguity or error.

---

## Requirement 1: Notational Consistency — PASS

29 symbol families identified. No true symbol collisions found. Two minor flags:

1. **$U_\text{ext}$ vs. $V$ convention**: The paper uses $V$ for value functions ($V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$) but writes extinction utility as $U_\text{ext}$. This mixes the $U$/$V$ naming convention. The meaning is unambiguous, but the convention is inconsistent.

2. **Value functions never formally defined**: $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ appear in Proposition 3 inequality comparisons but no Bellman equation is written down for them. The reader must infer their construction from context.

No symbol is reused for a different formal object. The two $\Gamma^N$ representations (Proposition 1 vs. Appendix A) were verified to be algebraically identical.

---

## Requirement 2: Mutual Consistency of Assumptions — PASS

All assumptions catalogued across the setup (12 structural, 10 parameter restrictions, 2 existence conditions, 1 normalization, 6 Extension 1 assumptions, 5 Extension 2 assumptions, 13 calibration values). All are mutually consistent. Three minor flags:

1. **$\phi(1+\eta) < 1$ unstated in Proposition 3**: The proof requires this condition explicitly, but the proposition does not list it among its conditions. The baseline calibration satisfies it ($0.5 \times 1.5 = 0.75 < 1$), and the condition is stated transparently within the proof, but a formal proposition should list all conditions.

2. **State space boundary**: $\alpha \in (0,1)$ should technically be $(0,1]$ for Extension 1, since the positive singularity with $\alpha = 0.7$, $\phi = 0.5$ gives $\min(1, 1.4) = 1$.

3. **Implicit constraint $\delta\tau < 1$** in Extension 2 for positive net transfers is not stated. Automatically satisfied under the calibration ($\delta = 0.5$, $\tau < 1$).

All calibration values satisfy all stated restrictions. All quantitative claims verified numerically (P/D ratios, ratio claims, $\phi^{-\gamma}$ values, existence condition violations, transfer formula $\eta$-independence).

---

## Requirement 3: Traceability — PASS

All mathematical objects trace back to the model primitives:

- **Fully traceable**: $\Gamma^{AI}$, $\Gamma^N$, $A^j$, P/D ratios (Eqs 1–2), $v^{AI}$, $B$, $S$, $f(A)$, $\Delta u(\gamma)$, $\alpha^+$, $c^H_{post}$, $\phi_\text{eff}$, transfer ratio, $\bar{\gamma}$.

- **Flag — value functions not formally defined**: $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ are implicitly determined by the model primitives (CRRA preferences, discount factor, singularity dynamics) but never given explicit Bellman-equation definitions. The paper mentions "the infinite-horizon Bellman equation" in prose but does not write it. This is a formal completeness gap rather than a traceability failure — all inputs to these value functions are specified.

No expression was found that cannot be logically derived from the assumptions.

---

## Summary of All Flags

| # | Flag | Severity | Requirement |
|---|------|----------|-------------|
| 1 | $U_\text{ext}$ vs. $V$ naming inconsistency | Minor | Req 1 |
| 2 | $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ never formally defined | Minor | Req 1, 3 |
| 3 | $\phi(1+\eta) < 1$ unstated in Proposition 3 | Minor | Req 2 |
| 4 | $\alpha \in (0,1)$ should be $(0,1]$ for Extension 1 | Negligible | Req 2 |
| 5 | Implicit $\delta\tau < 1$ constraint in Extension 2 | Negligible | Req 2 |
