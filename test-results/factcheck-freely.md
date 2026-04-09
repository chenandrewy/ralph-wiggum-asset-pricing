# tests/factcheck-freely.py
Started: 2026-04-09 19:33:01 EDT
Runtime: 7m 41s
[ralph-garage/agent-logs/20260409T193301.994893-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T193301.994893-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: FAIL
REASON: The paper misattributes the authors of "Left Behind: Creative Destruction, Inequality, and the Stock Market" (JPE 2020), listing Kogan, Papanikolaou, and Stoffman instead of the correct authors Kogan, Papanikolaou, Schmidt, and Song.

## Critical Issues

### 1. Incorrect citation: Kogan et al. (2020)
The bibliography entry `KoganPapanikolaouStoffman2020` in `paper/references.bib` (line 134-142) lists the authors of "Left Behind: Creative Destruction, Inequality, and the Stock Market" (JPE 2020, 128(3), 855-906) as Kogan, Papanikolaou, and **Stoffman**. The actual authors are Kogan, Papanikolaou, **Schmidt**, and **Song**. Noah Stoffman is not an author of this paper. The cite key and author field in `paper.tex` line 71 propagate this error into the rendered text. This is a regression: the prior commit (rloop-03) had the correct authors, but the working copy reverted to the wrong ones.

## Minor Issues

### 2. "Non-AI stocks' dividends shrink" is imprecise (paper.tex line 152)
The text states non-AI stocks' dividends "shrink" upon singularity, with the parenthetical $\Gamma^N < 1+\eta$. With baseline parameters, $\Gamma^N = (1-\Delta\theta)(1+\eta) = 0.8 \times 1.5 = 1.2 > 1$. Non-AI dividends grow in level (by 20%) but shrink as a share of the economy. The parenthetical is correct, but the word "shrink" without qualification is misleading.

### 3. Price appreciation vs. P/D ratio comparison (paper.tex line 201)
The text compares NASDAQ price appreciation relative to the S&P 500 (from Figure 1) with the model's P/D ratio differences. Cumulative price appreciation and P/D ratio spreads are distinct objects. The hedging language ("broadly consistent") is reasonable but a referee could flag this conflation.

## Verified as Correct

- **Euler equation derivation** (Appendix A): All algebra checks out; correctly produces $v = A/(1-A)$.
- **$\Gamma^{AI}$ and $\Gamma^N$ definitions**: Correctly represent dividend growth conditional on singularity.
- **$\Gamma^{AI} > 1+\eta$ and $\Gamma^N < 1+\eta$**: Correct given $\Delta\theta > 0$.
- **Comparative statics (Proposition 2)**: All three claims (i)-(iii) are correct.
- **Corollary 1 (Valuation spread)**: Correct.
- **Veto proposition (Proposition 3)**: Formula and proof logic are sound; extinction normalization is correctly characterized as conservative.
- **Transfer ratio**: Verified algebraically; $(1+\eta)$ cancels, confirming independence from $\eta$.
- **Numerical claims**: $\phi^{-\gamma} = 160{,}000$ with $\phi=0.05$, $\gamma=4$ is correct ($20^4$). $\phi(1+\eta) = 0.75$ (baseline) and $0.5$ (large singularity) are correct. P/D magnitudes in the text match the formulas.
- **Private AI capital dividends**: Internally consistent given the constraint $\alpha_t \in (0, 1-\theta_t]$.
- **Literature characterizations**: GKP (2012) and Jones (2024) are accurately described.
- **NASDAQ as "AI- and technology-heavy"**: Reasonable characterization.
