# tests/spec-economic.py
Started: 2026-04-09 19:33:01 EDT
Runtime: 2m 0s
[ralph-garage/agent-logs/20260409T193301.995512-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T193301.995512-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concepts Evaluated

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- Abstract: "an AI singularity that displaces their consumption"
- Introduction (line 50): "the risk that an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption"
- Model (line 92): "Each period, with probability $p$, an AI singularity occurs." Non-extinction branch: "Aggregate consumption jumps by a factor $1 + \eta$" — consistent with "vastly increases productivity and output."
- Extension 1 (line 217): "With probability $1 - \lambda$, the singularity is *negative* (as in the baseline): $\alpha_{t+1} = \phi \alpha_t$ with $\phi < 1$." In all calibrations, $\phi(1+\eta) < 1$, so the household's consumption falls — devastating for the typical investor, consistent with the spec's "negative AI singularity."
- Extension 1 (line 215): "With probability $\lambda$, the singularity is *positive*: the household's share *increases*." This is explicitly not devastating — correctly not labeled "negative."

**Assessment:** Consistent. The singularity is always defined as a sudden productivity improvement. The negative singularity is always devastating for the household. The extinction branch is modeled as a consequence triggered by the singularity event (the AI becoming powerful), not as a redefinition of singularity itself.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Consumption: household gets $\alpha_t C_t$, AI owners get $(1 - \alpha_t) C_t$. Sum = $C_t$. Satisfied.
- Dividends: AI stocks pay $\theta_t C_t$, non-AI stocks pay $(1 - \theta_t) C_t$, private AI capital pays the residual $(1 - \alpha_t) C_t - \theta_t C_t$. These allocate the full consumption. Satisfied.
- Transfers (Extension 2, line 253): Tax is on AI owners' surplus, deadweight costs reduce the transfer, and the household's post-transfer consumption plus AI owners' post-tax consumption plus deadweight loss sum correctly. Satisfied.

**Assessment:** Consistent. No budget constraint violations found.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract (line 33): "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium."
- Introduction (line 50): "If markets were complete, investors could insure against this risk directly by trading claims on AI capital. But much of this capital is private."
- Model (line 113): "The household *cannot* trade this private capital. This is the source of market incompleteness."
- Discussion (line 183): "If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk."
- Extension 1 (line 241): "Under complete markets, the household can trade claims on private AI capital before the singularity."
- Conclusion (line 284): "This mechanism requires market incompleteness---the inability to trade private AI capital."

**Assessment:** Consistent. Every reference to market incompleteness focuses on the household's inability to buy specific important assets (private AI capital). No references to Arrow-Debreu securities. Complete markets is framed as the household being able to trade the currently unavailable private AI capital.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract (line 33): "investors use AI stocks to hedge against an AI singularity that displaces their consumption"
- Introduction (line 50): "AI stocks serve as a *hedge* against a risk"
- After Proposition 1 (line 152): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — AI dividends grow upon singularity ($\Gamma^{AI} > 1+\eta$), so payoff increases when risk materializes. Explicitly called "partial hedge."
- Extension 2 (line 268): "the hedge value of AI stocks becomes infinite" — extreme case where the hedging payoff is so valuable the price diverges.
- Conclusion (line 284): "hedging motive"

**Assessment:** Consistent. AI stocks' dividends increase when the singularity (the risk) materializes, satisfying "payoff tends to increase when risk materializes." The paper consistently calls it a "partial hedge," consistent with "need not be perfect." The paper does not claim AI stocks earn a negative risk premium, consistent with the spec.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does **not** mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- Literature review (line 67): "Our paper builds most directly on GKP2012, who develop a general-equilibrium model in which innovation displaces existing agents." GKP2012 does determine prices via equilibrium conditions — correct usage.
- The paper's own model determines prices endogenously through the household's Euler equation (Proposition 1), which is an equilibrium condition. The paper does not explicitly label its own model as GE, but the structure is consistent: prices are endogenous, determined by equilibrium.
- The paper does not conflate general equilibrium with endogenous consumption. Consumption shares are set by the singularity mechanism, and the paper does not claim this makes the model GE.

**Assessment:** Consistent. The one explicit reference to "general-equilibrium" (GKP2012) is correct per the spec's definition. The paper's own model is implicitly GE (prices from Euler equation) and never mischaracterizes this. No conflation of GE with endogenous consumption.

## Cross-Section Consistency

All five concepts maintain the same economic meaning across the abstract, introduction, model, extensions, discussion, quantitative analysis, conclusion, and appendix. No drift in terminology was detected.
