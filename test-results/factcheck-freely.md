# tests/factcheck-freely.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 3m 42s
[ralph-garage/agent-logs/20260409T190308.199207-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T190308.199207-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: PASS
REASON: No factually incorrect statements or logical inconsistencies found in the paper.

## Detailed Review

### Mathematical Correctness
- **Proposition 1 (P/D Ratios):** The Euler equation derivation in Appendix A is algebraically correct. The three states are properly enumerated, SDF terms are correct, and the fixed-point solution $v = K/(1-K)$ follows. The expressions for $\Gamma^{AI}$ and $\Gamma^{N}$ correctly capture dividend growth conditional on a non-extinction singularity.
- **Proposition 2 (Comparative Statics):** All three parts are correctly stated and proved. (i) Decreasing $\phi$ raises $\phi^{-\gamma}$, amplifying the singularity term more for the asset with higher $\Gamma^j$. (ii) The qualification "for $\gamma$ sufficiently large" is appropriate. (iii) Higher $\xi$ proportionally reduces the singularity term weight.
- **Proposition 3 (Veto):** Equation (6) correctly computes the one-period utility gain. The extinction normalization ($u_{ext}=0$) is properly noted as conservative for $\gamma > 1$. Both parts (i) and (ii) are logically sound.
- **Transfer ratio (Equation 9):** Correctly derived from Equation (8). The independence from $\eta$ is verified algebraically.

### Internal Consistency — Numerical Examples
- $\phi(1+\eta) = 0.75$ with $\phi=0.5$, $\eta=0.5$: $0.5 \times 1.5 = 0.75$. **Correct.**
- $\phi(1+\eta) = 0.5$ with $\phi=0.05$, $\eta=9$: $0.05 \times 10 = 0.5$. **Correct.**
- AI P/D ~18 and non-AI P/D ~11 at $p=0.5\%$, $\xi=0$: Hand calculation yields AI P/D ~17.4 and non-AI P/D ~11.0, ratio ~1.58. Paper says "roughly 18" and "near 11" with "a ratio of about 1.6." **Consistent** within stated approximation.

### Economic Logic
- **Hedging mechanism:** Sound. AI stocks pay off in singularity states where household marginal utility is high due to displacement.
- **Market incompleteness:** Correctly motivated. If the household could trade private AI capital, the valuation spread would collapse.
- **Veto proposition:** Logically correct. Risk-averse household facing unhedgeable downside may block socially efficient development.
- **Transfer mechanism:** Sound. The transfer ratio being independent of $\eta$ while levels grow with $\eta$ is correctly derived and economically meaningful.

### Citation Accuracy
- **GKP (2012):** Accurately represented as showing displacement risk is a systematic factor, growth stocks hedge it, and market incompleteness arises from future innovators being untradeable. The paper's deliberately modest characterization of its contribution relative to GKP is appropriate.
- **Jones (2024):** Accurately represented regarding bounded utility, extinction risk, and the connection between powerful AI and existential risk.
- Other citations (Kogan-Papanikolaou, Barro, Wachter, Pastor-Veronesi, Korinek-Suh) are used appropriately and consistently with the cited works.

### Factual Claims
- AI-exposed firms trading at P/E ratios "two to five times the market average" is plausible (e.g., NVIDIA P/E of 50-70+ vs. S&P 500 P/E of ~20-22).
- Figure 1 is appropriately labeled "Illustrative."

### Code-Paper Consistency
- The R code's `compute_pd` function implements the exact formula from Propositions 1. Parameters match those stated in the paper.
- The extension code correctly implements the transfer consumption formula (Equation 8) and modifies the P/D formula accordingly.

### Minor Notes (Not Errors)
- The stationarity approximation (treating post-singularity P/D as approximately equal to pre-singularity P/D) is acknowledged in the proof and is standard in this class of models.
- The description of Jones (2024) on "bounded utility functions" is technically correct ($\gamma > 1$ implies bounded utility) though Jones's result is more nuanced about the specific $\gamma$ threshold. This is an acceptable simplification, not an error.
