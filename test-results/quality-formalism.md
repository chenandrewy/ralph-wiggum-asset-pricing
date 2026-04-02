# tests/quality-formalism.py
Started: 2026-04-02 18:34:30 EDT
Runtime: 2m 15s
[ralph-garage/agent-logs/20260402T183430.357582-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T183430.357582-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: FAIL
REASON: Section 4.2 contains a compressible displayed equation — Δ(λ) in eq (15) — whose specific functional form is never used in any subsequent result, remark, or interpretation; the paper's Coasean argument depends only on the endpoints (Δ₀ and 1), not on the linear interpolation.

---

## 8a — Theory style

### 8a, Requirement 1 (no dead-weight formal objects): PASS

Every proposition, assumption, and remark performs distinct economic work:

- **Assumptions 1–3** define the model primitives and ensure existence. All are invoked in later results.
- **Proposition 1** (PD ratios) delivers the closed-form pricing formula used by every subsequent result.
- **Proposition 2** (cross-section) makes the AI-premium prediction explicit in one line—not merely restating Prop 1.
- **Proposition 3** (comparative static) provides the key condition for when singularity probability raises AI valuations.
- **Proposition 4** (complete vs. incomplete markets) isolates the hedging premium; the paper correctly calls this the central result.
- **Remark 1** (extreme singularity) connects to Jones (2024) on utility curvature. Compact and does distinct work.
- **Remark 2** (Coase in the singularity) delivers the paper's contribution relative to GKP on overcoming frictions.
- **Equation (14)** (extinction PD ratio) cleanly shows how extinction attenuates the premium.
- **Equation (16)** (friction cost) supports Remark 2 and is required by the spec's call for formal analysis of transfers.

No formal object is introduced and then abandoned entirely. No dead weight found.

### 8a, Requirement 2 (no compressible formal objects): FAIL

**Equation (15): Δ(λ) = 1 − (1 − Δ₀)(1 − λ).**

This displayed equation introduces a linear interpolation of the displacement ratio parameterized by transfer coverage λ. The paper's actual argument about overcoming frictions (eq 16, Remark 2) is about whether friction costs shrink relative to output as Y → ∞. That argument never references the functional form of Δ(λ). It needs only two qualitative facts: (i) Δ = Δ₀ when there are no transfers, and (ii) Δ = 1 when transfers fully offset displacement. The paper could replace eq (15) with a single sentence — "If transfers partially offset displacement, the effective displacement ratio lies between Δ₀ (no sharing) and 1 (full sharing); at Δ = 1, the hedging premium vanishes as in the complete-markets case" — without weakening any economic claim. The specific linear form is never used in a pricing formula, plugged into a result, or referenced in Remark 2.

This is the only compressible formal object I find. It is a minor issue, but the requirement is strict.

### 8a, Requirement 3 (no orphan notation): PASS

All named notation is used in at least one result or interpretation:

- R, Φ^A, Φ^N, V₁: all appear in Propositions 1–4.
- Δ: central to every result.
- ω, ω̃: used in the displacement ratio and numerical illustration.
- D^P_t (private AI capital dividends): defined in eqs (3)–(4) for the accounting identity that output shares sum to 1. This is standard model-completeness notation, not orphan.

The parameter λ introduced in eq (15) is arguably orphan — it appears only in its own defining equation and the immediately surrounding prose, never in any result or remark. However, since eq (15) is already flagged as compressible, I do not double-count this.

### 8a, Requirement 4 (no pompous/ceremonial formalism or auxiliary detours): PASS

The paper's tone is direct throughout. Proofs are short or deferred to the appendix. No section reads as ceremony. The extensions (extinction, Coase/transfers) are spec-permitted and kept compact. No prose detours introduce mechanisms, heterogeneity, or dynamic structures beyond what the model uses.

---

## 8b — Empirical scope: PASS

Empirical content is limited to a single figure (Figure 1) showing AI vs. non-AI price-dividend ratios from CRSP data. No regressions, event studies, or additional empirical exhibits. This meets the spec exactly.

---

## 8c — Testable predictions: PASS

The paper states one cross-sectional prediction (AI stocks trade at higher PD ratios, spread increasing in perceived singularity risk) and one comparative static (PD ratio increasing in p under a stated condition). Both follow directly from the model. There is no laundry list of auxiliary predictions.

---

## 8d — Quantitative material: PASS

The numerical illustration (one paragraph plus one table) uses a single parameterization to gauge magnitudes. It is explicitly framed as illustrative ("To gauge magnitudes, consider the following parameterization"). There is no calibration exercise, estimation, or moment-matching. This is well within the spec's allowance.
