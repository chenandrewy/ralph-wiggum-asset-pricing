# tests/factcheck-anaphora.py
Started: 2026-04-02 18:07:23 EDT
Runtime: 3m 55s
[ralph-garage/agent-logs/20260402T180723.879330-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260402T180723.879330-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: No demonstrative near a cross-reference misresolves against its target.

## Findings by section

- **Introduction (lines 41--64):** No cross-references (`\ref` or `\eqref`) appear, so no demonstrative can misresolve.
- **Model (lines 65--145):** One case examined (`Assumption~\ref{as:neg-sing} states that $\Delta < 1$`); "that" is a conjunction, not a demonstrative. No issues.
- **Results (lines 146--229):** Several demonstratives near cross-references examined: "that of non-AI stocks" (near `\eqref{eq:pd-ai}`), "these high-marginal-utility states" (near `\eqref{eq:PhiA}--\eqref{eq:PhiN}`), "this holds" (near `\eqref{eq:comp-static}`). All resolve correctly to their intended targets.
- **Extension (lines 230--276):** No `\ref` or `\eqref` cross-references in this section. No issues.
- **Conclusion (lines 277--292):** No `\ref` or `\eqref` cross-references in this section. No issues.
- **Proofs (lines 293--309):** One case examined: "This is positive" (near `\eqref{eq:numerator}` and `\eqref{eq:comp-static}`). "This" correctly refers to the numerator expression in the preceding equation. No issues.
