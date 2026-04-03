# tests/quality-formalism.py
Started: 2026-04-02 22:39:49 EDT
Runtime: 1m 45s
[ralph-garage/agent-logs/20260402T223949.798406-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T223949.798406-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: PASS
REASON: The paper maintains lean formalism throughout; every formal object does economic work, notation is used after introduction, and scope stays compact.

## 8a — Theory style

**PASS.** Audited every displayed equation, proposition, assumption, remark, and proof for dead-weight, compressible, or orphan content.

**Propositions and proofs.** All three propositions carry distinct economic weight: Proposition 1 delivers the closed-form P/D ratios (the paper's core object), Proposition 2 gives the comparative static on singularity probability (the paper's headline claim), and Proposition 3 isolates the hedging premium by contrasting incomplete and complete markets (the central result per the abstract). No proposition contains subparts that merely restate qualitative points already obvious from the text. The inline proof of Proposition 1 is economically informative because it traces the origin of the displacement term Delta^{-gamma} through the Euler equation. The proof of Proposition 3 is two sentences. The appendix proof of Proposition 2 is standard quotient-rule calculus, appropriately deferred.

**Assumptions.** Assumptions 1-2 encode the paper's economic premises (negative singularity, AI share growth). Assumption 3 is a standard transversality/existence condition. All three are referenced by every proposition. No assumption is orphaned or ceremonial.

**Notation audit.** Every named variable introduced in the model section (theta, nu, omega, Delta, R, Phi^A, Phi^N, V_post, V_pre^A, V_pre^N) appears in at least one proposition or its economic interpretation. The closest candidate for orphan notation is D_t^P (private AI capital dividends, eq 3-4), which never reappears in any formula — but it serves the standard purpose of closing the output-accounting identity and is not ceremonially named or developed further. The extension introduces F, tau, T for the friction-cost formula (eq 17); these are local notation used in the immediately following remark and not inflated into a separate result.

**Borderline item: equation (17), friction-cost formula.** This is trivial algebra (F/Y vanishes as Y grows). A skeptic could argue the qualitative point ("fixed costs become negligible relative to output") needs no display equation. However, the spec explicitly calls for "a formal analysis" of how transfers scale with output (spec I.6.a), and the equation is one line. Keeping it is defensible under the spec; inflating it into a proposition would not be.

**Prose detours.** The extension section discusses the Coase theorem, Jones (2024) on utility curvature, and the extinction-state product convention. All three are tightly scoped to the spec-permitted extensions (extinction risk, infinite output, GKP transfer mechanism). No new agent heterogeneity, bargaining variants, mortality channels, or auxiliary mechanisms are introduced. The conclusion explicitly disclaims omitted features (heterogeneous households, production frictions, endogenous innovation) rather than sketching them as future work.

**No compressible formal objects.** Each displayed equation either (a) defines a model primitive needed for self-containment, (b) states a result used in a proposition or its interpretation, or (c) supports a spec-required extension. No subpart could be replaced by plain English without either making a claim imprecise or violating the spec's call for formal analysis.

## 8b — Empirical scope

**PASS.** Empirical content is limited to a single introductory figure (Figure 1) showing AI vs. non-AI price-dividend ratios from CRSP data. No regressions, no additional empirical exhibits, no data tables beyond the theoretical numerical illustration.

## 8c — Testable predictions

**PASS.** The paper generates only the direct implications of the main model: AI stocks trade at a premium over non-AI stocks, the premium increases with singularity probability and displacement severity, and the premium vanishes under complete markets. The conclusion explicitly states: "It does not generate a broad menu of testable predictions." No auxiliary cross-sectional predictions, no factor-model implications, no laundry list of corollaries.

## 8d — Quantitative material

**PASS.** One numerical illustration (Table 1) with a single parameterization varying p across a few values. Described as illustrative ("To gauge magnitudes"). No calibration to data moments, no estimation, no sensitivity analysis across parameter grids. The parameters are round numbers chosen for transparency, not fitted.
