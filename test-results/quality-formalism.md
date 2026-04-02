# tests/quality-formalism.py
Started: 2026-04-02 18:07:23 EDT
Runtime: 2m 29s
[ralph-garage/agent-logs/20260402T180723.871801-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T180723.871801-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: PASS
REASON: The paper maintains lean, purposeful formalism throughout; each formal object does economic work or serves a spec-required analysis, and the scope stays compact.

## 8a — Theory style

**PASS.**

**Propositions and core formalism.** The four propositions form a tight chain: Proposition 1 derives PD ratios in closed form; Proposition 2 uses the difference to establish the cross-sectional prediction; Proposition 3 delivers the key comparative static on singularity probability; Proposition 4 isolates the hedging premium by comparing incomplete and complete markets. Every intermediate object ($R$, $\Phi^A$, $\Phi^N$, $V_1$, $\Delta$) appears in at least one result or its interpretation. No proposition contains subparts that are stated but unused.

**Model primitives (Section 2).** The environment, dividend structure, assumptions, household problem, and equilibrium conditions are the minimum needed to derive the results. Two minor notation items deserve mention:

- $D_t^P$ (private AI capital dividends): introduced in eqs. (3)–(4) to show output shares sum to 1, but never appears in any pricing result. This is borderline orphan notation, but it is part of the standard accounting identity that defines the economy and takes only one line. Acceptable as self-contained model definition.
- $n_t^A$, $n_t^N$ (share holdings): introduced in the budget constraint (eq. 7) and immediately set to 1 by market clearing. Standard model presentation — the budget constraint is one equation and motivates why equilibrium consumption equals public dividends.

**Extension formalism (Section 4).** The extinction-risk formula (eq. 17) is a one-line modification of Proposition 1 that directly supports Remark 1. The transfer parameter $\lambda$ in eq. (18) and the friction cost formula (eq. 19) with parameters $F$ and $\tau$ are the most scrutinizable items. However, the spec explicitly requires "a formal analysis" of how transfers affect displacement (spec 6a) and asks the paper to "quantify the size of frictions that can be overcome, given infinite output" (spec 5c). These two equations are the minimal formal treatment of those requirements. $F$ and $\tau$ are local notation used in a single equation to make the $Y \to \infty$ argument precise; they are not ceremonial.

**Remarks vs. Propositions.** The paper uses Remark environments (not Propositions) for the informal observations about extreme singularities (Remark 1) and the Coase theorem (Remark 2). This is appropriate — these are qualitative observations that do not require proof, and using Remarks avoids ceremonial over-formalization.

**Prose detours.** No section introduces a new mechanism, heterogeneity, bargaining variant, or dynamic channel that lacks formal payoff. The meta-commentary about AI writing the paper (Introduction, paragraph 5) is spec-required (spec 5d). The related literature is a single paragraph. The conclusion is four short paragraphs with no new formalism.

**Orphan notation.** No named variable, parameter, or function is introduced and then entirely abandoned. $D_t^P$ is the closest candidate but serves the accounting identity.

## 8b — Empirical scope

**PASS.** The paper contains no empirical content whatsoever — no figures, no tables, no data analysis. The introduction references AI stock valuation trends in prose ("Between 2023 and 2025, the largest AI-related companies collectively gained trillions of dollars in market value") but presents no data. This is well within the "very limited" requirement. (The spec suggests a single CRSP figure would be ideal, but its absence is a completeness issue, not a scope violation.)

## 8c — Testable predictions

**PASS.** The paper generates exactly one cross-sectional prediction (AI stocks should trade at higher PD ratios than non-AI stocks, with the spread increasing in singularity risk) plus the comparative statics from Propositions 3–4. These are direct implications of the model, not a laundry list of auxiliary predictions. The conclusion explicitly notes the model is "deliberately stylized and not designed to match specific valuation levels."

## 8d — Quantitative material

**PASS.** The paper includes a single numerical illustration paragraph (after Proposition 4) with one parameterization yielding specific PD ratios. It is clearly framed as illustrative ("To gauge magnitudes, consider the following parameterization"). There is no calibration exercise, no estimation, no moment-matching, and no sensitivity analysis. This is exactly the kind of rough quantitative parameterization the spec permits.
