# tests/quality-formalism.py
Started: 2026-04-02 22:28:07 EDT
Runtime: 1m 30s
[ralph-garage/agent-logs/20260402T222807.260045-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T222807.260045-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: PASS
REASON: The paper maintains disciplined economy of formalism with no dead-weight objects, no compressible subparts, and tightly scoped empirical and quantitative content.

## 8a — Theory style

**PASS.**

**Dead-weight formalism:** None found. Every formal object—equations, assumptions, propositions, remarks—is invoked in a later result, interpretation, or numerical illustration. No theorem environments are introduced and abandoned.

**Compressible formalism:** No clear failures. The candidates I scrutinized:

- *Friction cost equation (eq 18):* The algebra (F/Y + τ(ω − ω̃)) is trivially simple, and the insight—fixed costs vanish as Y → ∞—could be stated in English. However, the spec explicitly requests "formal analysis" of how transfers scale with output (spec 6a), so this formalism is spec-mandated rather than ceremonial.
- *Assumption 3 (Existence):* Standard transversality condition, actually used to ensure the denominator in the P/D formulas is positive. Convention in asset pricing theory papers.
- *Budget constraint (eq 7):* Standard primitive needed for model self-containedness. Leads directly to the market-clearing consumption result.
- *Non-AI P/D ratio (V^N_pre) and Φ^N:* Used in Proposition 1, in the interpretation paragraph (valuation spread), and in the numerical illustration. Not orphaned.

**Orphan notation:** None found. Every named variable, parameter, and function introduced in the paper is used in at least one result, calibration entry, or economic interpretation:
- D^P_t (private AI dividends): completes the output accounting identity and establishes AI owners' role.
- n^A_t, n^N_t (share holdings): used in budget constraint and market clearing.
- R, Φ^A, Φ^N, V_post: all appear in Propositions 1–3 and/or the numerical illustration.
- Δ (displacement ratio): used in Propositions 1–3, Remark 1, and interpretation throughout.
- q (extinction probability): used in eq (17) and Remark 1.
- F, τ (friction costs): used in eq (18) and Remark 2.

**Pompous/ceremonial formalism:** The paper avoids unnecessary ceremony. Propositions are few (3) and each does distinct economic work. Remarks are used for limit results rather than inflated proposition environments. Proofs are either inline (short) or in the appendix (longer).

**Prose detours:** No scope-violating prose detours. The extension (Section 4) covers extinction risk and the Coase-theorem friction analysis—both within the spec-permitted extension scope (spec items 5a–c, 6a–c). No additional heterogeneity, mortality channels, bargaining variants, or auxiliary mechanisms are introduced.

## 8b — Empirical scope

**PASS.** The only empirical content is a single CRSP figure (Figure 1, currently commented out) in the introduction illustrating AI vs. non-AI price-dividend ratios. No additional empirical analysis, regressions, or data exercises appear anywhere in the paper.

## 8c — Testable predictions

**PASS.** The paper generates only direct implications of the three propositions: (i) AI stocks trade at a premium over non-AI stocks, (ii) the premium increases with singularity probability, (iii) the premium vanishes under complete markets. The conclusion explicitly states: "It does not generate a broad menu of testable predictions." No laundry list of auxiliary predictions is present.

## 8d — Quantitative material

**PASS.** The paper includes one numerical illustration (Section 3, Table 1) with a single parameterization to gauge magnitudes. The conclusion explicitly disclaims matching specific valuation levels. No calibration exercise, estimation, or systematic parameter exploration is attempted.
