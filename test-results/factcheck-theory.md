# tests/factcheck-theory.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 8m 33s
[ralph-garage/agent-logs/20260409T220435.845325-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T220435.845325-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects are traceable to the assumptions.

## Requirement 1: Notational Consistency

**Status: PASS**

21 symbol families were cataloged across all sections including appendix/proofs:
$t$, $C$, $c$, $\alpha$, $\phi$, $g$, $p$, $\xi$, $\eta$, $\theta$, $\Delta\theta$, $D$, $P$, $v$, $\Gamma$, $A$, $\beta$, $\gamma$, $U$, $\tau$, $\delta$

**Zero genuine symbol collisions found.** Every mathematical symbol denotes a single formal object throughout the paper. Superscript conventions ($H$, $AI$, $N$, $j$) are applied uniformly across all families.

Minor notes (none are errors):
- $u$ (period utility) appears informally in the proof of Proposition 3(i) without explicit definition, though unambiguous from context.
- $\alpha$ (household consumption share) and $\theta$ (AI dividend share) both partition $C_t$; the paper explicitly addresses this distinction in the transfers section.
- Time subscripts are dropped in comparative-static sections — standard practice.
- $\phi$ is reused symmetrically in Extension 1 ($\alpha/\phi$ for positive singularity) — internally consistent.

## Requirement 2: Assumption Consistency

**Status: PASS**

21 assumptions were cataloged spanning time structure (A1), agents (A2-A3), consumption processes (A4-A5), singularity mechanics (A6-A8), asset definitions (A9-A10), market structure (A11), preferences (A12), approximations (A13-A14), calibration (A15), and extensions (A16-A21).

Cross-referencing all assumptions against each other revealed no direct or implicit contradictions:
- Consumption growth under singularity correctly compounds normal growth $(1+g)$ with jump $(1+\eta)$.
- Dividend shares sum to one: $D^{AI} + D^N = C_t$.
- $\alpha$ and $\theta$ are independent parameters by construction.
- $\phi \in (0,1)$ is compatible with positive singularity $\alpha/\phi$ (capped by $\min(1, \cdot)$).
- Extinction utility $U_{\text{ext}} = 0$ is consistent with $\gamma > 1$ CRRA (where $u(c) < 0$).
- Parameter restrictions are non-conflicting.
- Existence condition $A^j < 1$ is satisfied numerically for baseline calibration and correctly violated for large-singularity calibration (as claimed).
- Euler equation expansion in Appendix A verified step by step.
- $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is correctly $\theta$-independent.
- $\phi \to \phi_{\text{eff}}$ substitution is valid (transfers affect SDF but not dividend growth factors).
- Extensions are clearly separated from the baseline and introduce no contradictions.

Minor issues (not contradictions):
1. **Deadweight cost parameter range**: General formulation permits $\delta\tau > 1$ when $\delta > 1$, making net transfers negative. Calibration ($\delta = 0.5$) avoids this, but no general restriction $\delta\tau < 1$ is stated. (Low severity)
2. **Transfer effect on aggregate dividends**: Deadweight loss destroys resources but is implicitly assumed not to affect the dividend process $D_t = \theta_t C_t$. Standard simplification, not explicitly stated. (Low severity)
3. **Extension 1 missing probability parameterization**: Probabilities of positive vs. negative non-extinction singularity are not parameterized; Proposition 3 is stated qualitatively. (Low severity)
4. **Extension 2 incomplete parameter restatement**: Figure caption does not restate $\theta$ and $\Delta\theta$, leaving readers to infer baseline values apply. (Negligible)

## Requirement 3: Traceability

**Status: PASS**

All mathematical objects in propositions, remarks, equations, and proofs were traced to the stated assumptions:

| Expression | Traced to |
|---|---|
| Eq. (1): $C_{t+1} = (1+g)C_t$ | A4 directly |
| Eq. (2): $\alpha_{t+1} = \phi\alpha_t$ | A7 directly |
| Eq. (3): CRRA utility | A12 directly |
| Euler equation (Appendix A) | Standard result from A2 + A12 |
| $\Gamma^{AI}$, $\Gamma^N$ | Algebraic from A9, A10, A7 |
| Proposition 1 (P/D ratios) | Euler equation + A4-A10 + A13 |
| Remark 1 ($A^j < 1$) | Mathematical consequence of Prop. 1 |
| Proposition 2 (comparative statics) | Derivatives of Prop. 1 formulas |
| Proposition 3 (veto) | A16-A18 + social efficiency as stated assumption |
| Eq. (7): $c^H_{\text{post}}$ | Algebraic from A5, A7, A19 |
| Eq. (8): $\phi_{\text{eff}}$ | Algebraic factoring of Eq. (7) |
| Eq. (9): transfer ratio | Ratio of Eq. (7) to no-transfer case |

No mathematical expression was found that cannot be logically derived from the stated assumptions.

Note: The Euler equation is invoked as a standard result from consumption-based asset pricing (following from the household being the marginal investor with CRRA preferences), not re-derived from first principles. This is standard practice in the target literature and does not constitute a traceability gap.
