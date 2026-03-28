# dev/qf/qf-pattern.py
Started: 2026-03-28 14:44:57 EDT
Runtime: 1m 43s
[ralph-garage/agent-logs/20260328T144457.286145-0400_qf-pattern_claude_opus.log](../../ralph-garage/agent-logs/20260328T144457.286145-0400_qf-pattern_claude_opus.log)

# qf-pattern
VERDICT: FAIL
REASON: Corollary 2 is compressible formalism whose content follows immediately from already-established comparative statics.

## Borderline formal objects identified

1. **Corollary 2 (Two-type marginal investors)**: The clearest case. Its entire content is: "Since the hedging premium increases as phi falls (already established in Corollary 1 and Proposition 1), an investor with lower phi faces a higher premium." The proof re-derives d(Delta)/d(phi) < 0, which already appears in Corollary 1's proof, and chains it with d(Lambda)/d(Delta) > 0, which is Proposition 3(i). The formal corollary, proof, and displayed inequality (equation 15) span ~15 lines for a result that is a one-sentence consequence of existing monotonicity. The fact that it works with Lambda_ext rather than Lambda is trivial because the extinction-adjusted kernel inherits the same monotonicity in Delta.

   One could argue Corollary 2 provides a useful anchor for the subsequent marginal-investor discussion. But the discussion itself (how VSL varies with wealth, how the phi and q channels interact) does not rely on the formal statement---it could reference the comparative static directly. The corollary adds a label, not content.

2. **Equation (7)** (d/a > phi*s/(1-s)): A first-order sufficient condition for the singularity being negative. Borderline compressible---could be stated as "when most AI capital is private, even moderate displacement suffices." However, it is a single line and provides a useful reference point for calibration. Not sufficient on its own to fail.

3. **Equation (12)** (extinction Euler contribution = 0): States the measure-theoretic fact that 0 times X equals 0 a.s. The surrounding prose already explains this in plain English. The equation formalizes what the text just said. Marginally redundant but very compact.

## Objects that earn their keep

- **Propositions 1-3**: Each introduces a distinct economic result. No redundancy.
- **Corollary 1**: The cross-sectional prediction is the paper's main empirical contribution and requires the small-firm assumption to be stated precisely.
- **Corollary 3**: Non-monotonicity from endogenous friction resolution is non-obvious and requires the formal argument.
- **Remarks 1-2**: Prose-level discussion in remark environments, which is standard.
- **Standard primitives and derivations**: Equations (1)-(4), (6), (8)-(10), (13)-(14), (16)-(17) are all necessary scaffolding or core derivations.

## Aggregate assessment

Corollary 2 is compressible. It repackages the phi comparative static (already formally established) for two investor labels without adding new economic content. The proof duplicates steps from Corollary 1. Replacing the formal corollary with a sentence---"By the same logic as Corollary 1, the hedging premium is larger when retail investors, who face lower phi, are marginal"---would lose nothing and free space. This violates Requirement 2 (no compressible formalism).

Equations (7) and (12) are borderline but individually too compact to condemn. They do not change the verdict but reinforce the direction: the paper occasionally formalizes claims that the surrounding prose already conveys.
