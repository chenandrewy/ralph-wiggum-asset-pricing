# tests/quality-formalism.py
Started: 2026-04-02 22:54:31 EDT
Runtime: 1m 57s
[ralph-garage/agent-logs/20260402T225431.391133-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T225431.391133-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: PASS
REASON: The paper's formalism is lean and well-targeted; each formal object does identifiable economic work, and scope remains compact.

## 8a — Theory style

### Dead-weight formalism: PASS

No dead-weight formal objects found. Every proposition, assumption, and remark connects to the paper's economic claims. The three propositions (price-dividend ratios, comparative static on singularity probability, incomplete vs. complete markets) form a tight logical chain. The two remarks address spec-required extensions (extreme singularity limit, Coase theorem in the singularity). The three assumptions define essential model primitives.

### Compressible formalism: PASS (borderline items noted)

**Borderline candidates examined:**

1. **Equation (12), extinction-risk P/D ratio.** The economic point is simply "multiply the singularity term by the survival probability $(1-q)$." This could be stated in English. However, the spec explicitly requires formal incorporation of extinction risk (spec I.5.a: "formally incorporates ideas from Jones-2024"), and the equation is a single compact line. Justified.

2. **Equation (11), friction cost formula.** The point is "fixed costs become negligible as output grows." Again statable in English, but the spec requires formal analysis of how transfers scale with output (spec I.6.a-c). The equation is minimal and serves the Coase-theorem argument. Justified.

3. **Non-AI P/D ratio $V_{\mathrm{pre}}^N$ in Proposition 1.** One could argue the cross-sectional comparison $V_{\mathrm{pre}}^A > V_{\mathrm{pre}}^N$ follows immediately from $\tilde{\theta}/\theta > 1 > \tilde{\nu}/\nu$ and the shared denominator, so the full formula for $V_{\mathrm{pre}}^N$ is dispensable. However, displaying both formulas makes the comparison transparent and the proposition is more useful as a reference. The cost is one additional equation with identical structure; the benefit is completeness of the main pricing result. Acceptable.

No compressible formal object rises to the level of a failure. The paper consistently uses its formalism to advance economic claims.

### Orphan notation: PASS (one minor flag)

**$D_t^P$ (private AI capital dividends):** Named in equations (3)-(4) and never referenced again in any result, calibration, or interpretation. The paper could replace these with prose ("the remainder $1-\theta-\nu$ of output accrues to private AI capital") without losing anything. However, this falls under the standard-primitives exception (guideline 3): displaying the full output decomposition is conventional model accounting that keeps the environment self-contained. One named variable in a display equation is not a meaningful violation.

No other orphan notation found. All other named variables ($R$, $\Phi^A$, $\Phi^N$, $V_{\mathrm{post}}$, $\Delta$, $\omega$, $\tilde{\omega}$, etc.) appear in results, interpretations, or calibration.

### Pompous/ceremonial formalism and scope detours: PASS

The paper avoids gratuitous formalism. There are no unnecessary lemmas, no "without loss of generality" invocations, no displayed sufficient conditions that go unused, and no named examples or cases beyond what the argument requires. Proofs are either inline (short) or in the appendix (Proposition 2). The extension (Section 4) stays within spec-permitted territory: extinction risk and overcoming frictions. No additional heterogeneity, bargaining variants, mortality channels, or auxiliary mechanisms are introduced.

The prose is disciplined. The conclusion explicitly acknowledges what the model omits ("heterogeneous households, production-side frictions, and endogenous innovation") without developing these as future-work channels. The self-referential paragraph about AI authorship is spec-required (spec IV.5.d) and kept to one paragraph.

## 8b — Empirical scope: PASS

Empirical content consists of a single introductory figure (Figure 1) showing AI vs. non-AI price-dividend ratios using CRSP data. No additional empirical analysis, regressions, event studies, or data tables appear anywhere in the paper. This matches the spec's ideal of "a single figure in the introduction" (spec II.8.b).

## 8c — Testable predictions: PASS

The paper generates only direct implications of the model: (i) AI stocks trade at a P/D premium over non-AI stocks; (ii) the premium increases with singularity probability and displacement severity; (iii) the premium vanishes under complete markets; (iv) the premium is largest for moderate singularities. The conclusion explicitly states: "It does not generate a broad menu of testable predictions." No auxiliary predictions, cross-sectional sorts, or empirical hypotheses beyond the model's core logic.

## 8d — Quantitative material: PASS

Quantitative content consists of one numerical illustration (Table 1) with a single parameter vector ($\beta=0.96$, $\gamma=3$, $g=0.02$, $\tilde{g}=0.05$, etc.) reported for several values of $p$. The conclusion explicitly states the paper "does not attempt to match specific valuation levels." There is no calibration to data moments, no estimation, no sensitivity analysis, and no model-vs-data comparison. The parameterization is purely illustrative.
