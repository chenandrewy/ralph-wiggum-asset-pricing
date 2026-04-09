# tests/theory-deadweight.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 2m 15s
[ralph-garage/agent-logs/20260409T182005.678130-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.678130-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: FAIL
REASON: The appendix is a ceremonial shell containing no real proof details, and one function notation is introduced then immediately abandoned.

## Detailed Findings

### 1. Appendix A is ceremonial formalism (primary finding)

The paper includes a formal appendix titled "Proof Details" (lines 305-307) that contains no actual proof details. Its full content is:

> The proofs of Propositions 1-2 are given in the main text. Proposition 3 relies on the comparison of expected utility under the household's SDF versus the social planner's SDF, which integrates over both agents' consumption. The complete-markets result follows because, under complete markets, the household's SDF coincides with the social SDF, and the social surplus is positive by assumption.

This is an auxiliary formal detour. The first sentence simply tells the reader what they already know (the proofs are in the main text). The second and third sentences restate Proposition 3(ii)'s proof in SDF language, but the main-text proof (lines 254-255) already makes the same argument in plain English. The SDF reframing adds no economic content, no mathematical rigor, and no insight beyond the main text. This is a formal appendix that exists to look like a theory paper should have an appendix — exactly the kind of "pompous or ceremonial formalism" the spec warns against (II.8.a).

**Recommendation**: Remove the appendix entirely, or (if the authors want to keep it) add genuine proof details that go beyond the main text — e.g., the explicit algebra showing the social SDF prices the surplus correctly.

### 2. $\delta(\tau)$ function notation is introduced and abandoned (secondary finding)

Line 263 introduces a general function notation: "Deadweight costs consume a fraction $\delta(\tau) = \delta_0 \tau$ of the transferred amount." The function wrapper $\delta(\tau)$ is never referenced again. In Eq. (10) and Eq. (11), the paper writes out the explicit form $\delta_0 \tau$ directly. The general function notation suggests a level of generality (arbitrary deadweight cost schedules) that the paper never exploits. The sentence could simply read: "Deadweight costs consume a fraction $\delta_0 \tau$ of the transferred amount, where $\delta_0 > 0$ governs the severity of waste."

This is minor but it is formalism that does no work — a function name that is defined and immediately discarded.

### 3. Borderline: Corollary 1

Corollary 1 (lines 167-173) states that $P^{AI}/D^{AI} > P^N/D^N$ whenever $\Delta\theta > 0$ and $\phi < 1$. This is a trivially obvious consequence of Proposition 1: the P/D ratio formula is increasing in $\Gamma^j$, and $\Gamma^{AI} > \Gamma^{N}$ when $\Delta\theta > 0$. The one-sentence proof confirms this. The prose paragraph immediately following (lines 165-166) already explains the identical economic content in plain English.

Elevating this to a formal corollary is arguably ceremonial — it could be a sentence in the discussion. That said, corollaries for key predictions are standard in theory papers, and this is the paper's central empirical prediction, so the formal treatment is defensible. Flagged as borderline rather than a clear violation.

### Items audited and passed

The following formal objects were audited and found to carry their weight:

- **Eq. (1)** ($C_{t+1} = (1+g)C_t$): Serves as a building block used explicitly in the Proposition 1 proof.
- **Eq. (2)** (displacement $\alpha_{t+1} = \phi \alpha_t$): Central mechanism, used in all results and calibration.
- **Eq. (3)** (CRRA utility): Needed for the Euler equation and the veto proposition.
- **Proposition 1 and Eqs. (4)-(5)** (P/D ratios): Central results, used in calibration and comparative statics.
- **Eqs. (6)-(8)** (Euler equation derivation): The in-text proof of Proposition 1. Standard and necessary — the spec requires explicit proofs.
- **Proposition 2** (comparative statics): All three parts are used in the quantitative discussion (Section 3) and the extension analysis.
- **Proposition 3 and Eq. (9)** (veto): Extension 1's core result. The formal utility-gain expression is needed to state what "veto" means precisely.
- **Eq. (10)** (transfer consumption): Extension 2's core equation, used in the figure and the limit result.
- **Eq. (11)** (transfer limit): Delivers the key insight that singularity growth overwhelms deadweight costs. Qualitative takeaway would be weaker without the clean limit.
- **All parameters** ($\beta, g, \gamma, \phi, \eta, p, \xi, \theta, \Delta\theta, \lambda, \phi^+, \kappa, \tau, \delta_0$): Each is used in at least one result, calibration, or figure that matters for the paper's conclusions.
- **$\Gamma^{AI}$, $\Gamma^{N}$** (dividend growth factors): Used in both propositions and the quantitative table.

### Minor LaTeX note

The preamble defines `\newtheorem{lemma}{Lemma}` (line 22) but no lemma appears in the paper. This is invisible to readers but is a code-level artifact of formalism that was planned but dropped.
