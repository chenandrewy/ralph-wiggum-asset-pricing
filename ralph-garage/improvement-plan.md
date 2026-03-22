# Improvement Plan

## Status

- **Tests**: All pass (spec-compliance, theory-correctness).
- **Referee (referee-top3)**: Two comments, both actionable.

## Key Issues

1. **Paper is 22 pages; limit is 20.** The spec-compliance test reported 13 pages (likely counting content pages wrong), but the referee confirmed 22 from the PDF. This is a binding constraint.

2. **Business-cycle augmentation (Section 3.4) is informal.** Every other result has a proposition and proof. The expected-returns decomposition (eq 17) is stated as prose with back-of-envelope numbers. A top-journal referee will demand formalization.

These two issues are linked: formalizing the business-cycle result costs ~0.5 pages, so ~2.5 pages must be cut elsewhere.

## Plan

### 1. Formalize the business-cycle result as a Proposition

Add a brief Proposition (after the current expected-returns prose in Section 3.4) establishing:
- With i.i.d. normal-period shocks, the P/D expressions in Propositions 1–2 are unchanged to first order in σ².
- The expected-return decomposition (eq 17) is exact conditional on no singularity.
- Include a short proof sketch (Euler equation with the augmented SDF).

This replaces the current informal paragraph; net cost is ~0.5 pages after removing redundant prose.

### 2. Cut ~2.5 pages through targeted compression

**(a) Shorten the Proposition 1 proof (~0.5 pages saved).** The proof is a standard Euler-equation manipulation. Reduce to 3–4 lines: state the Euler equation, note the two-state expansion, and say "solving for v^A yields (7)." The derivation is mechanical and the theory-correctness test has verified it.

**(b) Condense the η-robustness discussion in Section 2.3 (~0.3 pages saved).** Currently ~10 lines of text plus three numerical examples. Reduce to 2 sentences noting the robustness check and pointing to Table 3 for details. The numbers can go in a table note or be dropped.

**(c) Shorten "Level Effects on Non-AI Stocks" paragraph (~0.3 pages saved).** Currently a full paragraph with a lit comparison. Reduce to 2 sentences: state that non-AI valuations also rise (with the equation reference) and note the contrast with standard disaster models.

**(d) Tighten the GKP comparison in the introduction (~0.3 pages saved).** The three-way comparison with GKP runs long. Compress to the two most distinctive differences (private vs. unborn owners; reducible friction with policy lever α). Drop or fold in the footnote-14 point more concisely.

**(e) Compress calibration parameter grounding (~0.3 pages saved).** The paragraph justifying each calibration parameter (λ, θ, ϕ, ϕ_L) with citations is thorough but verbose. Tighten each to one sentence.

**(f) Tighten Proposition 5 proof (~0.3 pages saved).** The two-part proof is detailed. The key steps are the super-linear growth condition and J crossing 1. Compress each part to 2–3 lines.

**(g) Reduce references page (~0.5 pages saved).** Use a more compact bibliography style (e.g., smaller font or abbreviated journal names) to reduce the ~2-page bibliography to ~1.5 pages.

### 3. Verify page count

After edits, compile and confirm ≤ 20 pages. If still over, further trim the introduction (currently ~2 pages; target 1.5).
