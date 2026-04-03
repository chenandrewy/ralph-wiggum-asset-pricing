# tests/factcheck-theory.py
Started: 2026-04-02 22:54:31 EDT
Runtime: 1h 13m 39s
[ralph-garage/agent-logs/20260402T225431.399602-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T225431.399602-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually compatible, and all mathematical expressions trace back to model primitives.

## Requirement 1: Notational Consistency — PASS

Full audit in `ralph-garage/scratch/factcheck-notation.md`.

**21 symbol families** identified. **Zero true collisions** — no symbol family is reused for a semantically different formal object anywhere in the paper.

**8 minor flags**, all standard informalities:

| # | Symbol | Issue | Severity |
|---|--------|-------|----------|
| 1 | $Y$ (bare) | Used without time subscript in friction-cost limit argument (Eq. 9), while the paper otherwise defines $Y_t$ | Minor |
| 2 | $\Delta$ | Conventionally "change in"; here a ratio $\tilde{\omega}/\omega$ — explicitly defined | Minor |
| 3 | $P$ | Base symbol for prices ($P_t^A$) and superscript for "Private" ($D_t^P$) — different syntactic roles | Minor |
| 4 | $R$ | Named "pricing kernel" but letter conventionally used for gross returns; no return variable in paper | Minor |
| 5 | $V_{\text{next}}^A$ | Uses `\text{}` while other regime subscripts use `\mathrm{}` | Cosmetic |
| 6 | $V_{\mathrm{post}}$ | Lacks asset superscript; justified (common to all assets) but could use a clarifying phrase | Expository |
| 7 | $T$ vs $t$ | Transfer amount vs. time index — same letter, different case | Minor |
| 8 | $q$ dual role | Standalone extinction probability and superscript label in $V_{\mathrm{pre}}^{A,q}$ | Negligible |

All conventions (tilde for post-singularity, asset superscripts, regime subscripts, time indexing) are stable and internally consistent.

## Requirement 2: Assumption Consistency — PASS

Full audit in `ralph-garage/scratch/factcheck-assumptions.md`.

**3 formal assumptions** (Negative singularity, AI share growth, Existence) and **11 informal/implicit assumptions** identified.

**All assumptions are mutually consistent.** The numerical illustration ($\beta=0.96$, $\gamma=3$, $g=0.02$, $\tilde{g}=0.05$, $\theta=0.05$, $\tilde{\theta}=0.15$, $\nu=0.55$, $\tilde{\nu}=0.30$) constructively confirms simultaneous satisfiability.

Key consistency checks performed:
- A1 and A2 are logically independent but compatible (A1 requires non-AI loss to exceed AI gain; A2 does not imply this).
- A3 existence conditions are automatically satisfied under $\gamma > 1$ with positive growth rates.
- The denominator $1-(1-p)R > 0$ is guaranteed by A3.
- $\Phi^A, \Phi^N > 0$ under all stated assumptions.

**Gaps (no contradictions, but unstated domain restrictions):**

| # | Gap | Severity |
|---|-----|----------|
| 1 | Positivity of $\theta, \nu, \tilde{\theta}, \tilde{\nu} > 0$ and bounds $\theta+\nu \leq 1$, $\tilde{\theta}+\tilde{\nu} \leq 1$ never formally stated. $\theta = 0$ breaks $\tilde{\theta}/\theta$ in Prop 1. | Moderate |
| 2 | $g > 0$ never formally stated, despite the claim that A3 is automatic for positive growth | Low |

These are omissions of standard domain restrictions, not contradictions between assumptions.

## Requirement 3: Traceability — PASS

All mathematical objects trace back to model primitives ($\beta, \gamma, g, \tilde{g}, p, \theta, \nu, \tilde{\theta}, \tilde{\nu}, q, F, \tau$) and the model structure (CRRA utility, budget constraint, market clearing, Euler equation).

**Derived objects verified:**

- $\omega \equiv \theta + \nu$, $\tilde{\omega} \equiv \tilde{\theta}+\tilde{\nu}$, $\Delta \equiv \tilde{\omega}/\omega$ — direct definitions from primitives.
- $R \equiv \beta(1+g)^{1-\gamma}$ — from SDF in normal state.
- $\Phi^A, \Phi^N$ — from SDF $\times$ dividend growth in singularity state; $\Delta^{-\gamma}$ arises from consumption displacement.
- $V_{\mathrm{post}}$ — from Euler equation in absorbing post-singularity regime. Common to both assets because share fractions cancel (P/D depends on growth rate, not level).
- $V_{\mathrm{pre}}^A, V_{\mathrm{pre}}^N$ — from Euler equation with two-state regime switching. Algebra verified.
- Proposition 2 comparative static — quotient rule applied to $\mathcal{N}(p)/\mathcal{D}(p)$; expansion in Eqs. (14)–(16) verified.
- $\Phi^{A,\mathrm{CM}}, V_{\mathrm{pre}}^{A,\mathrm{CM}}$ — same derivation with $c_t = Y_t$, so $\Delta^{-\gamma} \to 1$.
- Hedging premium (Eq. 12) — subtraction of complete- from incomplete-market valuations; positivity from $\Delta^{-\gamma} - 1 > 0$.
- $V_{\mathrm{pre}}^{A,q}$ — singularity contribution scaled by $(1-q)$ using stated extinction convention.
- Friction cost expression (Eq. 9) — direct algebra from transfer cost structure.

**No expression in the paper fails to trace back to stated assumptions and model primitives.**
