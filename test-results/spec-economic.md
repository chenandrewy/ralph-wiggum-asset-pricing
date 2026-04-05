# tests/spec-economic.py
Started: 2026-04-04 23:45:08 EDT
Runtime: 1m 46s
[ralph-garage/agent-logs/20260404T234508.986612-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260404T234508.986612-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the background spec consistently with their definitions throughout every section.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**
- Introduction (line 55): "An AI singularity---a sudden, dramatic improvement in AI capability---would vastly increase total economic output." — Matches spec.
- Section 2.2 (line 108): "Total output jumps by factor $G > 1$: the economy becomes vastly more productive." — The singularity always has $G > 1$, consistent with "vastly increases productivity and output."
- Abstract (line 30): "devastating AI singularity" — Used in conjunction with "negative," not redefining the base term.

No inconsistencies found. The paper always pairs the singularity with an output increase ($G > 1$), matching the spec.

### 2. Negative AI Singularity

**Spec definition:** "An AI singularity that is devastating for the typical investor."

**Paper usages:**
- Section 2.2 (line 126): "When $\Lambda < 1$---a *negative* AI singularity---the household's consumption falls despite a massive increase in total output."
- Section 3.3, Panel B discussion (line 231): "$\Lambda = 0.8$, the singularity reduces the household's consumption to 80\% of its pre-singularity level."

The household is the representative (typical) investor. Consumption falling despite output booming is devastating. The formal condition $\Lambda < 1$ faithfully captures the spec's qualitative definition. Consistent throughout.

### 3. Budget Constraints

**Spec definition:** Budget constraints must be satisfied; violations are fundamental flaws.

**Paper usage:** The household's consumption equals publicly traded output pre-singularity and $(1-\phi)G Y_\tau (1+g)^{t-\tau}$ post-singularity (line 117–118). AI capital owners capture fraction $\phi$; the household receives the remainder. Total claims sum to total output. No budget constraint violations detected in the model, the transfer extension (line 247, where transfer proceeds plus remaining private capital plus household share equal total output), or elsewhere.

No inconsistencies found.

### 4. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets means "some assets cannot be bought by the representative investor" (e.g., equity in privately-held AI firms). Does NOT necessarily refer to Arrow-Debreu securities. Complete markets discussions should focus on which important assets are unavailable.

**Paper usages:**
- Section 2.3 (line 137): "The household cannot trade the private AI capital held by AI owners. This is the key friction." — Exactly the spec's framing: specific assets that the representative investor cannot buy.
- Section 3.2 (line 197): "Under complete markets, the household can trade claims on the private AI capital." — Framed as ability to trade a specific asset, not as Arrow-Debreu completeness.
- Section 4.1 (line 250): "With full transfers ($\theta = 1$) and no deadweight cost ($\delta = 0$): $\Lambda = G$, reproducing the complete-markets benchmark." — Complete markets defined by the household accessing full output through trading AI capital.
- Section 4.2 (line 270–271): "Under complete markets, the household shares in the full output gains from the singularity." — Same framing.
- Introduction (line 59): "Under incomplete markets, the premium is strictly larger than under complete markets, because the household's marginal utility in the singularity state is amplified by the displacement it cannot insure away." — Incomplete markets defined by inability to insure, not by Arrow-Debreu.

No references to Arrow-Debreu securities anywhere in the paper. Consistent throughout.

### 5. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Introduction (line 55): "Publicly traded AI stocks partially hedge this displacement because their dividends grow relative to other stocks when the singularity arrives." — "partially" is consistent with "need not be perfect." "Dividends grow" is consistent with "payoff tends to increase."
- Abstract (line 31): "they hedge against a devastating AI singularity" — Consistent.
- Section 3 (line 170–171): Hedge factors $H^A = (\alpha_S/\alpha)\Lambda^{1-\gamma}$ capture dividend growth ($\alpha_S/\alpha > 1$) times SDF weighting. Under the paper's parameterizations ($\alpha_S = 0.50$, $\alpha = 0.15$, $\Lambda = 0.8$), AI stock dividends jump by factor $(\alpha_S/\alpha)\Lambda = 3.33 \times 0.8 = 2.67 > 1$. AI stock payoffs do increase when the singularity materializes.
- Section 3.3 (line 231): "AI stocks function as insurance: their value rises precisely because the disaster they hedge against becomes more likely." — Consistent with payoff increasing when risk materializes.
- The paper uses "hedging premium" to mean a P/D ratio premium (higher valuation), not a positive expected return premium. The spec does not constrain how "premium" is used, only how "hedge" is used.

No inconsistencies found. The paper never claims the hedge is perfect, and never claims AI stocks earn a negative risk premium overall.

### 6. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium means prices are determined by equilibrium conditions (does NOT mean consumption is endogenous). Partial equilibrium means prices are exogenous.

**Paper usage:**
- Definition 1 (line 141–147): "An equilibrium consists of asset prices $(P_t^A, P_t^N)$ such that the household's Euler equations hold... and markets clear." — Prices are determined endogenously by equilibrium conditions (Euler equations + market clearing). This is general equilibrium by the spec's definition.
- Consumption is determined by the output structure and the share parameter $\phi$, not by household optimization over a budget constraint. Per the spec, this is fine: general equilibrium does not require endogenous consumption.
- The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly, avoiding any potential confusion.

No inconsistencies found.

## Cross-Section Consistency Check

Each term maintains the same economic meaning across all sections:

| Concept | Abstract | Intro | Model | Results | Extensions | Conclusion | Appendix |
|---------|----------|-------|-------|---------|------------|------------|----------|
| AI singularity (G > 1) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Negative singularity (Λ < 1) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Incomplete markets (can't trade AI capital) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Hedging (payoff increases when risk materializes) | ✓ | ✓ | — | ✓ | ✓ | ✓ | — |

No cross-section drift detected.
