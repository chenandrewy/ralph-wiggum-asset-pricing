# tests/factcheck-anaphora.py
Started: 2026-04-02 18:17:45 EDT
Runtime: 1m 5s
[ralph-garage/agent-logs/20260402T181745.335260-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260402T181745.335260-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: FAIL
REASON: One anaphora resolution error found where prose attributes a mechanism to a cross-referenced assumption that does not contain it.

## Findings

### Model (lines 65–146)

**Line 108** — Assumption~\ref{as:neg-sing} over-glossed with mechanism not in the assumption.

> "Assumption~\ref{as:neg-sing} states that $\Delta < 1$: the singularity displaces the household by shifting output toward private AI capital."

Assumption 1 (`as:neg-sing`, line 97) says only: "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$." The causal gloss "by shifting output toward private AI capital" is not contained in the referenced assumption. The assumption constrains the sum of household shares but says nothing about where the lost share goes. The directional mechanism (output flowing to private AI capital) belongs to the broader model setup, not to Assumption 1 alone.

### Introduction (lines 41–64)
No issues found. No \ref or \eqref cross-references in this section.

### Results (lines 147–230)
No issues found. All demonstratives near cross-references resolve correctly.

### Extension (lines 231–277)
No issues found. No \ref or \eqref cross-references within this section.

### Conclusion (lines 278–293)
No issues found. No cross-references in this section.

### Proofs (lines 294–310)
No issues found. Demonstratives resolve correctly to their targets.
