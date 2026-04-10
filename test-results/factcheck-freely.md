# tests/factcheck-freely.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 7m 8s
[ralph-garage/agent-logs/20260409T202148.442575-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T202148.442575-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: PASS
REASON: No factually incorrect statements or logical inconsistencies found; all core math, code, and citations are correct.

## Review Details

An Opus-level subagent conducted a thorough review of the paper's mathematical derivations, quantitative claims, code consistency, and citation accuracy. Below is a summary of findings.

### Confirmed Correct

1. **Euler equation derivation (Appendix A)**: The three-state expansion, algebra, and $v^j = A^j/(1-A^j)$ solution are mathematically correct.
2. **Equation (6) for transfer consumption**: Correctly decomposes displaced consumption and net transfers with deadweight costs.
3. **Equation (7), ratio independent of $\eta$**: Confirmed exact — $(1+\eta)$ cancels in the ratio.
4. **Corollary 1 (valuation spread)**: $\Gamma^{AI} > \Gamma^N$ when $\Delta\theta > 0$; monotonicity of $v^j$ in $\Gamma^j$ verified.
5. **Proposition 2 (comparative statics)**: All three parts correct.
6. **Quantitative claims**: "P/D ratios 1.5 to 6 times higher" verified ($p=0.5\%$: ratio 1.58; $p=1\%$: ratio 5.76). "Nearly 6 to 1" and "roughly 18 vs. 11" are accurate.
7. **R code consistency**: `compute_pd`, `compute_pd_with_transfer`, and `consumption_growth` all correctly implement the paper's formulas.
8. **$\phi^{-\gamma} = 160{,}000$ claim**: Correct ($0.05^{-4} = 160{,}000$).
9. **Citation accuracy**: GKP 2012, Jones 2024, Kogan-Papanikolaou 2014, Knesl 2023, Nordhaus 2021, Pastor-Veronesi 2009 all accurately characterized.

### Minor Issues Noted (Not Rising to Errors or Inconsistencies)

1. **Post-singularity stationarity approximation** (acknowledged in paper): Creates upward bias in P/D ratios since post-singularity $\Gamma^{AI}$ is lower. Standard modeling simplification.
2. **Transfer base scope**: Ambiguity in whether tax applies to public AI stock dividends or only private capital surplus. Internally consistent under the reduced-form interpretation of $\alpha$.
3. **Extinction utility normalization**: Paper uses standard CRRA rather than Jones's shifted specification. The "conservative" claim is correct under their specification.
4. **Extinction term in Euler equation**: The $0 \times \infty$ form is resolved by standard rare-disasters convention (Barro 2006).
5. **Figure axis label**: Panel (b) omits $(1+g)$ factor; negligible impact and consistent between code and text.
6. **Complete markets proof (Prop 3(ii))**: Informal argument implicitly assumes household captures some surplus; standard in theory papers.
7. **$\alpha_t \leq 1-\theta_t$ constraint**: Stated but not used; automatically satisfied after singularities.
