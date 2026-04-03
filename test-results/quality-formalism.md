# tests/quality-formalism.py
Started: 2026-04-02 21:49:42 EDT
Runtime: 1m 45s
[ralph-garage/agent-logs/20260402T214942.812167-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T214942.812167-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: PASS
REASON: The paper maintains lean, economical formalism where each formal object does distinct economic work, and scope remains tightly controlled.

## 8a — Theory style

**PASS**

### Dead-weight formalism: None found

Every formal object (Assumptions 1--3, Propositions 1--4, Remarks 1--2) serves a distinct role:

- **Assumptions 1--3** are standard model primitives that define the economic environment and ensure well-defined equilibrium. No assumption is introduced and then ignored.
- **Proposition 1** delivers the closed-form PD ratios that anchor all subsequent results. Both AI and non-AI formulas are needed (non-AI feeds Proposition 2).
- **Proposition 2** (cross-section) is a direct subtraction but states the paper's key cross-sectional claim. It earns its place as a named result.
- **Proposition 3** (comparative static) directly addresses the paper's central question: does singularity probability raise AI valuations? The sufficient condition is interpretable and economically meaningful.
- **Proposition 4** (complete vs. incomplete markets) isolates the hedging premium, the paper's core contribution. Both the complete-market PD and the premium formula do distinct work.
- **Remark 1** (extreme singularity) connects to Jones (2024) on utility curvature and extreme growth, a spec-permitted extension. Compact and necessary.
- **Remark 2** (Coase/frictions) addresses the spec-required contribution relative to GKP on transfers and displacement. Necessary.

### Compressible formalism: No strong candidates

Closest candidate is equation (21), the friction cost formula $F/Y + \tau(\omega - \tilde\omega)$. The insight ("fixed costs vanish when output is enormous") is nearly verbal, but the formula is a single line that makes the Coase-theorem argument precise and directly supports Remark 2. This is within the spec-permitted extension on transfers/GKP contribution. Not compressible enough to fail.

The budget constraint (eq. 7) and market-clearing derivation of equilibrium consumption (eq. 8) are standard model-building primitives needed to make the equilibrium self-contained. The Euler equation (eq. 9) is the workhorse pricing equation. All are necessary.

### Orphan notation: None found

Every named variable, parameter, or function is used in at least one result, calibration, or interpretation:

- $D_t^P$ (private AI dividends): defined to close the output-share accounting; implicitly referenced in complete-markets discussion.
- $n_t^A$, $n_t^N$ (holdings): used in budget constraint and consumed into market-clearing consumption.
- $F$, $\tau$, $T$ (friction parameters): local to Section 4.2 and serve Remark 2.
- All pricing objects ($R$, $\Phi^A$, $\Phi^N$, $V_1$, $\Delta$) are used in multiple propositions.

### Prose detours: None found

The Jones (2024) discussion in Section 4.1 (connecting utility curvature to the hedging premium limit) is brief interpretive prose tied to a spec-permitted extension, not a new mechanism or scope expansion. Section 4.2's Coase-theorem discussion is the spec-required GKP contribution on transfers. No new heterogeneity, bargaining variants, mortality channels, or dynamic laws of motion are introduced.

### Ceremonial formalism: None found

The paper avoids inflated theorem environments. Remarks are used for limit results rather than full propositions. Proofs are short and inline except Proposition 3's, which is appropriately in the appendix.

## 8b — Empirical scope

**PASS**

Empirical content is limited to a single CRSP-based figure (Figure 1) in the introduction showing AI vs. non-AI price-dividend ratios. No regression tables, event studies, or additional empirical analysis. This matches the spec's ideal of "a single figure in the introduction."

## 8c — Testable predictions

**PASS**

The paper's predictions are direct implications of the model: (i) AI stocks trade at higher PD ratios than non-AI stocks, (ii) the spread increases with perceived singularity risk, (iii) the premium vanishes under complete markets. These are a handful of core implications, not a laundry list. The conclusion does not generate auxiliary predictions beyond the model's main arguments.

## 8d — Quantitative material

**PASS**

Quantitative content is limited to a single numerical illustration (Table 1) with rough parameterizations ($\beta = 0.96$, $\gamma = 3$, etc.) to gauge magnitudes. The text explicitly frames this as illustrative: "To gauge magnitudes, consider the following parameterization." There is no systematic calibration, estimation, moment-matching, or sensitivity analysis.
