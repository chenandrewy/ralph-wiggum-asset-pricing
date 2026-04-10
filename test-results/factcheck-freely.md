# tests/factcheck-freely.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 7m 50s
[ralph-garage/agent-logs/20260409T210608.981679-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T210608.981679-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: FAIL
REASON: The bibliography omits Amit Seru as a co-author of Kogan, Papanikolaou, Seru, and Stoffman (2020, JPE), a factual error in a citation.

## Detailed Findings

### Factual Error: Missing Author on Citation

The bib entry `KoganPapanikolaouStoffman2020` in `paper/references.bib` lists only Kogan, Papanikolaou, and Stoffman as authors of "Left Behind: Creative Destruction, Inequality, and the Stock Market" (JPE 2020). The actual paper has four authors: Kogan, Papanikolaou, **Seru**, and Stoffman. This is a factual error — omitting a co-author misattributes the work. The paper text (`paper.tex`, line 68) also cites it without Seru via `\citet{KoganPapanikolaouStoffman2020}`.

### Items Verified as Correct

1. **Mathematical derivations (Proposition 1, Appendix A):** The Euler equation derivation is algebraically sound. The three-state enumeration (no singularity, non-extinction singularity, extinction) correctly produces the P/D formulas in equations (4)–(5).

2. **Comparative statics (Proposition 2):** All three claims — (i) increasing in displacement severity, (ii) increasing in $p$ for large $\gamma$, (iii) decreasing in $\xi$ for the parameterizations considered — are logically consistent with the formulas. The proof of (iii) uses a convexity argument qualified to specific parameterizations, which is appropriate.

3. **Quantitative claims:** At $p = 1\%$, $\xi = 0$ with stated parameters, the AI-to-non-AI P/D ratio reaches roughly 6x. The "roughly six times" claim is accurate.

4. **Hedging argument:** Internally consistent. AI stocks have $\Gamma^{AI} > \Gamma^{N}$, so they pay more in singularity states where household marginal utility ($\phi^{-\gamma}$) is high. This correctly implements the hedging channel.

5. **Extension 1 (Veto, Proposition 3):** Logic is sound. Under incomplete markets with high $\gamma$, the concavity of CRRA utility makes the downside of negative singularity dominate the upside of positive singularity, producing the veto even when development is socially efficient. The extinction utility normalization ($U_{ext} = 0$) is correctly described as conservative.

6. **Extension 2 (Transfers):** 
   - Equation (7) transfer ratio: correctly independent of $\eta$ (it cancels in numerator and denominator).
   - $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$ for baseline: correct.
   - $\phi(1+\eta) = 0.05 \times 10 = 0.5$ for large singularity: correct.
   - $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$: correct.

7. **"Consumption falls by 25%":** Correct. The ratio of singularity to counterfactual consumption is $\phi(1+\eta) = 0.75$; the growth factor $(1+g)$ appears in both and cancels.

8. **Literature characterizations:**
   - GKP 2012: Accurately described as showing displacement risk from innovation under incomplete markets creates a systematic risk factor, with growth stocks providing a partial hedge.
   - Jones 2024: The claim about bounded utility making agents conservative about extinction is accurate.

9. **"Zero traditional research labor":** The abstract claim is qualified by "traditional" and the footnote clarifies the human authored the specification and test scripts. This is a rhetorical choice rather than a factual error, though it is aggressive.

### Minor Notes (Not Rising to Factual Error)

- The stationarity approximation (post-singularity P/D ≈ pre-singularity P/D) introduces non-trivial error when $\Delta\theta = 0.2$, since $\theta$ jumps from 0.15 to 0.32 after one singularity, changing $\Gamma^{AI}$ by ~33%. The paper acknowledges this is an approximation.
- The characterization of GKP's discussion of transfers is slightly generous — GKP mention transfers as a robustness observation rather than a policy recommendation — but is not factually incorrect.
