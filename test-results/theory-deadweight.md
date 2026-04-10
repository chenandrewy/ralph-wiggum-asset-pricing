# tests/theory-deadweight.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260409T202148.435035-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.435035-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: FAIL
REASON: Corollary 1 is ceremonial, and several formal subparts are introduced but do no work.

## Detailed Findings

### 1. Corollary 1 (Valuation spread) is ceremonial formalism

The prose paragraph immediately after Proposition 1 (line 150) already states the corollary's content in plain English: "AI stocks' payoffs are especially valuable, pushing their P/D ratio above that of non-AI stocks. This is the hedging channel." Corollary 1 then restates this as a formal theorem environment with a two-sentence proof. The proof says nothing beyond "P/D is increasing in $\Gamma^j$ and $\Gamma^{AI} > \Gamma^N$," which is already evident from the proposition's formulas. Packaging this as a corollary-with-proof is ceremonial: the qualitative takeaway is already delivered in the preceding paragraph and the formal statement adds no economic or mathematical content. Demoting it to a sentence of prose ("It follows immediately that AI stocks trade at a higher P/D ratio whenever $\Delta\theta > 0$") would tighten the paper without weakening any claim.

### 2. $\lambda$ is a parameter that appears in no equation or result

In Extension 1 (Section 4.1), $\lambda$ is introduced as the probability that the singularity is positive. Its only use is the qualitative assumption "$\lambda > 1/2$: the positive singularity is the most likely outcome." The parameter never appears in any numbered equation, any proposition's statement, any proof's algebra, any calibration, or any figure. Its role could be fully replaced by plain English: "We assume the positive singularity is more likely than the negative one." Introducing a named parameter for a single qualitative inequality that is never used formally is exactly the kind of deadweight the paper's own style guidelines warn against.

### 3. Private AI capital dividend formula is introduced and abandoned

Line 111 defines the private AI capital's dividends as $(1-\alpha_t)C_t - D_t^{AI}$. This expression never appears in any subsequent equation, proposition, proof, calibration, or figure. It is not used to derive any result. Its only purpose is to name the residual accruing to AI owners, but the conceptual point (the household cannot trade AI owners' surplus) is already made without this formula. Removing it would lose nothing.

### 4. Positive singularity displacement is formally invoked but never specified

Extension 1 states that in a positive singularity, "the household's share *increases* ($\alpha_{t+1} > \alpha_t$)," but never specifies the actual law of motion for $\alpha$ in the positive case (contrast with the negative case, which has the precise formula $\alpha_{t+1} = \phi\alpha_t$). Proposition 3's proof then argues qualitatively about the household's utility gain from the positive singularity without any formula. This is a formal mechanism that is introduced at just enough specificity to look like a model extension but not enough to produce any concrete result. Either the positive displacement should have a specified formula (even a simple one like $\alpha_{t+1} = \alpha_t / \phi$), or the discussion should be purely verbal rather than using formal notation.

### 5. The constraint $\alpha_t \in (0, 1-\theta_t]$ introduces a relationship that does no work

Line 87 bounds the household's share above by $1-\theta_t$. This implies that $\alpha_t + \theta_t \leq 1$, linking the household's consumption share to the AI dividend share. This constraint is never checked in any proof, never binds in any calibration (baseline: $0.70 + 0.15 = 0.85 < 1$; post-singularity: $0.35 + 0.32 = 0.67 < 1$), and is never referenced again. It is a piece of formalism that creates the appearance of rigor without doing any work. The simple bound $\alpha_t \in (0,1)$ would suffice, or the upper bound could be stated verbally as a side condition.

## Summary

The paper's core formalism (Propositions 1-3, the transfer equations, the existence condition) all earn their keep. But it carries several pieces of deadweight: a ceremonial corollary, a named parameter used only in one qualitative inequality, an abandoned formula, an underspecified formal mechanism, and a non-binding constraint. Individually these are minor; collectively they represent exactly the kind of "pompous or ceremonial formalism" and "auxiliary formal detours" that the paper's own quality standard (Spec IV.8.a) warns against.
