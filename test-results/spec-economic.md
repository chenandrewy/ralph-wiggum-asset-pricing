# tests/spec-economic.py
Started: 2026-04-02 22:39:49 EDT
Runtime: 1m 29s
[ralph-garage/agent-logs/20260402T223949.798022-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T223949.798022-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**
- Abstract (line 30): "a sudden AI-driven productivity surge that displaces existing workers and firms"
- Section 2.1 (line 74): "A singularity is an absorbing event that arrives with independent probability $p$ each period."
- Section 2.1 (line 78-82): "output grows at a strictly higher rate, reflecting the productivity increase that accompanies the singularity" and "singularities that vastly increase productivity and substantially displace existing firms"
- Section 4 (line 238-241): considers the limit $\tilde{g} \to \infty$, consistent with "vastly increases productivity"

**Assessment:** Consistent. The paper captures "sudden" (discrete arrival with probability $p$), "improvement in AI" (AI-driven), and "vastly increases productivity and output" (higher growth rate $\tilde{g} > g$, with focus on large disruptions).

### 2. Negative AI Singularity

**Spec definition:** "An AI singularity that is devastating for the typical investor."

**Paper usages:**
- Abstract (line 30): "a negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms"
- Assumption 1 (line 101-103): "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$."
- Section 2.2 (line 109-113): displacement ratio $\Delta < 1$, "the household's share of output falls at the singularity"
- Introduction (line 52): "displacing traditional businesses and reducing the investor's share of total output"

**Assessment:** Consistent. The representative household is the "typical investor," and displacement ($\Delta < 1$) makes the singularity devastating for that investor. The paper consistently frames the negative singularity as harmful to the household/investor throughout all sections.

### 3. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**
- Section 2.3 (line 122-126): Explicit budget constraint in equation (6): $c_t + P_t^A n_{t+1}^A + P_t^N n_{t+1}^N = (D_t^A + P_t^A) n_t^A + (D_t^N + P_t^N) n_t^N$
- Section 2.2 (line 88-92): Output shares sum to one: $\theta + \nu + (1 - \theta - \nu) = 1$
- Section 2.3 (line 128-132): Market clearing ($n_t^A = n_t^N = 1$) pins down equilibrium consumption as $c_t = D_t^A + D_t^N = \omega Y_t$

**Assessment:** Consistent. Budget constraints are explicitly stated and satisfied. Output shares sum to one both pre- and post-singularity. Market clearing is imposed.

### 4. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = "some assets cannot be bought by the representative investor." Complete markets = focus on "important assets that are unavailable to the representative investor." Neither necessarily refers to Arrow-Debreu securities.

**Paper usages:**
- Introduction (line 52): "Private AI ventures and yet-to-be-created firms would capture much of the new value, but the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets..."
- Section 2.1 (line 84): "AI owners hold private AI capital and do not participate in public stock markets."
- Section 2.3 (line 122): "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital."
- Proposition 3 (line 200-201): "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output: $c_t = Y_t$."
- Section 4.2 (line 250): "Transfers---bequests, government programs, private insurance---can offset displacement. With no transfers, the displacement ratio is $\Delta$... With full transfers, $\Delta = 1$ and the hedging premium vanishes, as in the complete-markets case."

**Assessment:** Consistent. Incomplete markets is always framed as the household's inability to invest in private AI capital---a specific, important asset class. Complete markets is framed as gaining access to that asset class. No mention of Arrow-Debreu securities anywhere. The discussion in Section 4.2 extends complete markets to transfers, which is consistent with the spec's focus on available assets rather than Arrow-Debreu formalism.

### 5. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Abstract (line 30): "public AI stocks uniquely valuable as partial insurance against displacement"
- Introduction (line 52): "publicly traded AI stocks offer the best available hedge"
- Introduction (line 56): "The mechanism is a hedging premium: in singularity states, the household's marginal utility is high (due to displacement) while AI stocks pay relatively more."
- Section 3 (line 184): "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices. AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge."
- Proposition 3 (line 206-209): The hedging premium is defined as the valuation difference $V_{\mathrm{pre}}^A - V_{\mathrm{pre}}^{A,\mathrm{CM}} > 0$.

**Assessment:** Consistent. The paper's hedging concept exactly matches the spec: AI stock payoffs increase when singularity risk materializes ($\tilde{\theta}/\theta > 1$). The paper explicitly notes the hedge is partial ("partial insurance," "best available hedge"), consistent with "need not be perfect." The hedging premium is about higher valuations (lower required returns), not about negative risk premiums overall---the asset still earns a positive return.

### 6. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:** The paper does not explicitly use the terms "general equilibrium" or "partial equilibrium."

**Assessment:** No inconsistency. The model is implicitly general equilibrium in the spec's sense: prices are determined by the Euler equation and market clearing (equations 6-8), not taken as exogenous. Consumption is pinned down by market clearing rather than being a separate choice variable, which is consistent with the spec's note that GE "does not mean that consumption is endogenous." The paper avoids these terms entirely, so there is no risk of misuse.

## Cross-Section Consistency Check

All key terms maintain consistent meaning across sections:

| Term | Intro | Model | Results | Extension | Conclusion |
|------|-------|-------|---------|-----------|------------|
| Singularity | Sudden AI breakthrough | Absorbing event, prob $p$ | Same formal object | Same + limit analysis | Same |
| Negative singularity | Displaces investors | $\Delta < 1$ | Same | Same | Same |
| Incomplete markets | Can't buy private AI | Household excluded from $D^P$ | Same | Same | Same |
| Hedging | AI stocks as hedge | Payoff covariance | $\Phi^A$ mechanism | Attenuation analysis | Same |
| Displacement | Share of output falls | $\tilde{\omega} < \omega$ | Same | Same, with transfers | Same |

No cross-section drift detected.
