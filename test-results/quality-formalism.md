# tests/quality-formalism.py
Started: 2026-04-02 18:17:45 EDT
Runtime: 1m 56s
[ralph-garage/agent-logs/20260402T181745.329306-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T181745.329306-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: PASS
REASON: The paper maintains disciplined formalism throughout; every formal object serves the economic argument or is mandated by the spec, and scope remains compact.

## 8a — Theory style

**PASS.** Each formal object was audited against the burden-of-proof test.

### Formal objects audit

**Propositions 1–4:** All essential. Proposition 1 delivers the closed-form P/D ratios (the paper's core deliverable). Proposition 2 establishes the cross-sectional prediction (AI > non-AI valuations). Proposition 3 provides the key comparative static (dV/dp > 0 under conditions). Proposition 4 isolates the hedging premium by comparing incomplete and complete markets—this is described as the "central result." No proposition contains dead-weight subparts; each formula is used in the paper's interpretation or numerical illustration.

**Auxiliary notation (R, Phi^A, Phi^N, V_1):** All four appear in multiple propositions and in the economic interpretation. Not orphan.

**Assumptions 1–3:** Assumption 1 (negative singularity) and Assumption 2 (AI share growth) define the economic setting and are invoked by every proposition. Assumption 3 (finite prices) is a standard existence condition. All essential.

**Displacement ratio Delta (eq 5):** Appears in every proposition's formula or interpretation. Essential.

**D_t^P (private AI capital dividends, eqs 3–4):** Named but never enters a pricing formula. However, it is needed to close the model: the reader must know where the rest of output goes, and the existence of inaccessible private AI capital is the source of the incomplete-markets friction. Passes the burden-of-proof test (cutting it would leave the displacement story incomplete).

**Budget constraint (eq 7) and holdings n_t^A, n_t^N:** Standard model primitive. The holdings are immediately pinned down by market clearing, yielding equilibrium consumption (eq 8). The budget constraint is necessary to make the household's problem self-contained.

**Remark 1 (extreme singularity limit):** Takes g-tilde to infinity and shows the hedging premium vanishes. This connects to Jones (2024) and is a spec-permitted extension (spec 5b). Not a detour.

**Delta(lambda) (eq 15):** Linear parameterization of partial risk-sharing. Borderline compressible—the qualitative point (transfers reduce displacement) could be stated in English. However, the spec explicitly requests "formal analysis" of how transfers affect displacement (spec 6a), so this is spec-mandated.

**Friction cost formula (eq 16):** F + tau*T divided by Y. The F/Y → 0 insight is nearly obvious, but the spec says "quantify the size of frictions that can be overcome" (spec 5c). Spec-mandated.

**Remark 2 (Coase in the singularity):** Summarizes the friction-cost argument. Spec-permitted extension (spec 5c, 6a–c).

### Orphan notation check

No orphan notation found. Every named variable, parameter, or function is used in at least one result, calibration, or interpretation. D_t^P is the closest to orphan status but serves essential model-accounting and narrative purposes.

### Prose detour check

No prose detours found. The introduction's related literature is within spec length constraints. The self-referential paragraph (AI writing the paper) is spec-mandated (spec IV.5.d). The conclusion's policy paragraph (expanding tradeable AI assets) executes spec item 3c. Section 4.2's Coase-theorem discussion executes spec items 5c and 6a–c. No new mechanisms, heterogeneity, or bargaining variants are introduced beyond what the spec permits.

## 8b — Empirical scope

**PASS.** The paper contains zero empirical content—no figures, no data, no regressions. The spec says empirical content should be "very limited, ideally a single introductory figure." Zero is even more limited than one figure. This requirement concerns excess empirical content, not insufficiency.

## 8c — Testable predictions

**PASS.** The paper states one cross-sectional prediction (AI stocks trade at higher P/D ratios than non-AI stocks, with the spread increasing in singularity risk) and notes it is "consistent with elevated valuations" while emphasizing the model is "deliberately stylized." No laundry list of auxiliary predictions.

## 8d — Quantitative material

**PASS.** One numerical illustration paragraph (end of Section 3) with a single parameterization to gauge magnitudes. Clearly illustrative—introduced with "To gauge magnitudes, consider the following parameterization." No calibration, estimation, or systematic quantitative exercise.
