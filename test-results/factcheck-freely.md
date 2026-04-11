# tests/factcheck-freely.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 8m 51s
[ralph-garage/agent-logs/20260411T101504.810663-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T101504.810663-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: FAIL
REASON: The paper contains one factually incorrect claim (P/D spread "vanishes" under complete markets) and one logical inconsistency (Proposition 3(ii) stated unconditionally but proved only for small veto costs).

## Issue 1: P/D spread does not vanish when displacement is hedged

**Location:** Section 2.3, line 178.

**Claim:** "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$: displacement is fully hedged, the SDF no longer overweights singularity states, and the P/D spread between AI and non-AI stocks vanishes."

**Problem:** Setting $\phi_\text{eff} = 1$ eliminates the displacement channel in the SDF ($\phi^{-\gamma} = 1$, so singularity states are no longer overweighted). However, the P/D spread does not vanish because the dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ remain different. Specifically, $\Gamma^{AI}$ depends on $\theta + \Delta\theta(1-\theta)$, while $\Gamma^{N} = (1-\Delta\theta)(1+\eta)$. Since $\Delta\theta > 0$, AI stocks still have superior dividend growth in singularity states regardless of $\phi$. At baseline parameters with $\phi = 1$, the P/D ratio is approximately 1.02 (versus 1.40 at $\phi = 0.5$) --- dramatically reduced but not zero.

**Severity:** Moderate. The economic intuition is correct (displacement is the dominant driver), but the mathematical claim is false within the paper's own model. The displacement-driven premium nearly vanishes; the total spread does not.

**Fix:** Replace "vanishes" with language reflecting that the displacement-driven spread is eliminated while a small residual spread from differential dividend growth remains, or qualify that the claim holds approximately when $\Delta\theta$ is small.

## Issue 2: Proposition 3(ii) overstated relative to its proof

**Location:** Section 4.1, line 220.

**Statement:** "Under complete markets: the household never vetoes socially efficient AI development ($V_\text{develop}^{CM} > V_\text{veto}$)."

**Proof (line 233):** "The household strictly prefers development for any $\gamma > 1$ and any $\kappa$ small enough, and in particular for the same $\kappa$ used in part (i)."

**Problem:** The proposition states an unconditional result ("never vetoes") but the proof establishes it only for $\kappa$ below a threshold. For arbitrarily large veto costs $\kappa$, the result need not hold --- the positive utility gain $u(\alpha(1+\eta)) - u(\alpha)$ from development can be offset by a sufficiently large $\kappa$. The proposition statement and proof are not aligned.

**Severity:** Minor. The result holds for all economically plausible $\kappa$ values, and the proof is transparent about the qualification. But a formal proposition should match its proof.

**Fix:** Add "for $\kappa$ sufficiently small" to the proposition statement, or note that the result holds for the same $\kappa$ as in part (i).
