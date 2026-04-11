# tests/factcheck-freely.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 6m 29s
[ralph-garage/agent-logs/20260411T103039.143177-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T103039.143177-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: FAIL
REASON: Figure 1 caption labels price indices as "valuations," which is factually inaccurate, and the proof of Proposition 2(iii) contains imprecise logical reasoning.

## Issues Found

### 1. Figure 1 caption mislabels price indices as "valuations" (Factual Error)

**Location**: Section 1, Figure 1 caption.

The caption reads "Valuations of AI-Exposed Stocks vs. the Broader Market," but the figure shows normalized *price levels* (Jan 2015 = 100), not valuation multiples (P/D or P/E). A stock can have a higher normalized price without having a higher valuation ratio if its earnings grew proportionally. The paper partially acknowledges this in Section 3 ("return differences partly reflect earnings growth rather than valuation multiples"), but the caption itself is factually misleading.

### 2. Proof of Proposition 2(iii) uses imprecise reasoning (Logical Imprecision)

**Location**: Proof of Proposition 2, part (iii).

The proof states that "an increase in $\xi$ reduces $A^{AI}$ and $A^{N}$ by the same multiplicative factor on their singularity terms." This is ambiguous and not quite right: increasing $\xi$ reduces the singularity term $p(1-\xi)S\Gamma^j$ proportionally in both, but this is not the same as reducing $A^j$ by the same factor, since $A^j$ also contains the $(1-p)$ term which is unaffected. The final conclusion (spread narrows) is correct via the convexity argument, but the verbal exposition in the proof is sloppy.

### 3. Transfer extension uses undisclosed approximation (Moderate Concern)

**Location**: Section 4.2, equations (11)-(12), and code implementation.

The effective displacement parameter $\phi_{\text{eff}}$ depends on the household's consumption share $\alpha$, which changes after each singularity ($\alpha_{k+1} = \phi \alpha_k$). The backward recursion uses $\phi_{\text{eff}}$ computed at $\alpha_0 = 0.70$ for every step, but after the first singularity the share drops to $\phi \alpha_0 = 0.35$, changing the transfer formula. This is an undisclosed approximation affecting the quantitative accuracy of Figure 2, though not the qualitative conclusions.

## Items Verified as Correct

- Proposition 1 derivation and closed-form P/D expressions
- Proposition 2 comparative statics (conclusions correct, despite proof imprecision)
- Proposition 3 (veto result) and its limit argument
- Numerical claims: P/D ratios (~15.5 and ~11 at p=0.5%, ratio ~1.4; ratio ~2 at p=1%)
- The $\phi^{-\gamma} = 160{,}000$ claim ($0.05^{-4} = 160{,}000$)
- All citations present in references.bib
- Remark 1 existence condition
- Code correctly implements the backward recursion for the baseline model
