# tests/factcheck-exhibits.py
Started: 2026-04-02 22:28:07 EDT
Runtime: 1m 47s
[ralph-garage/agent-logs/20260402T222807.265066-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T222807.265066-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: Table 1 values are correctly generated from the paper's closed-form formulas with matching parameters and rounding.

## Table 1: Numerical Illustration: Price-Dividend Ratios

**Description.** Table 1 reports price-dividend ratios ($V_0^A$, $V_0^N$, $V_0^{A,\text{CM}}$), their spread, and the hedging premium (%) for five values of the singularity probability $p \in \{0, 0.005, 0.01, 0.02, 0.05\}$. Parameters are listed in the table notes.

### Suspicious features

1. **Steep rise in $V_0^A$**: The AI price-dividend ratio more than doubles from 11.9 (p=0) to 26.5 (p=0.05), a large effect from a small probability shift.
2. **Large hedging premium at p=0.05**: The hedging premium reaches 73.4%, which is a sizable departure from complete-markets pricing.
3. **Stale comment**: The LaTeX source contains `% Exhibit 2` next to `\label{tab:numerical}`, but the table renders as Table 1. This is a code comment only and does not affect the rendered output.

### Code check

**Feature 1 — Steep rise in $V_0^A$.** Traced to `code/numerical-illustration.R`, lines 26 and 51. The singularity-state pricing kernel $\Phi^A = \beta \Delta^{-\gamma}(1+\tilde{g})^{1-\gamma}(\tilde{\theta}/\theta)$ evaluates to approximately 6.19 with the stated parameters ($\Delta = 0.75$, $\gamma = 3$, $\tilde{\theta}/\theta = 3$). The term $\Phi^A(1 + V_\text{post}) \approx 6.19 \times 7.74 \approx 47.9$ is large relative to $R/(1-R) \approx 11.9$, so even small $p$ sharply raises the numerator of the price-dividend formula. Manual verification at p=0.01: $V_0^A = (0.99 \times 0.9227 + 0.01 \times 47.92)/(1 - 0.99 \times 0.9227) = 1.393/0.0865 \approx 16.10$. Matches the displayed 16.1. **Correctly generated; not an artifact.**

**Feature 2 — Large hedging premium.** The hedging premium isolates the $\Delta^{-\gamma} - 1$ channel (code line 36, paper eq. hedging-premium). With $\Delta^{-3} \approx 2.37$, the incomplete-markets $\Phi^A$ is 2.37× the complete-markets $\Phi^{A,\text{CM}}$. At p=0.05 this accumulates to 73.4%. Manual check at p=0.01: $(16.10 - 12.90)/12.90 \times 100 \approx 24.8\%$. Matches. **Correctly generated; economically consistent with displacement severity.**

**Feature 3 — Stale comment.** The `% Exhibit 2` comment appears in the LaTeX source but has no effect on the rendered table, which correctly displays as "Table 1." **Not a rendered feature; no impact.**

### Verification summary

| p | $V_0^A$ (code) | $V_0^A$ (manual) | $V_0^N$ (code) | $V_0^N$ (manual) | Match |
|---|---|---|---|---|---|
| 0.000 | 11.9 | 11.9 | 11.9 | 11.9 | Yes |
| 0.010 | 16.1 | 16.1 | 11.6 | 11.6 | Yes |
| 0.050 | 26.5 | 26.5 | 10.6 | 10.6 | Yes |

All code formulas (R, V1, Φ_A, Φ_N, Φ_A_CM, V0 expressions) match the paper's stated equations exactly. Parameters in code match the table notes. Rounding to one decimal is consistent throughout.

**Exhibit verdict: PASS** — All values are correctly generated from the paper's closed-form expressions; no artifacts, errors, or unsupported features found.
