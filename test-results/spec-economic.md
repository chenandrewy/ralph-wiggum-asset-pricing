# tests/spec-economic.py
Started: 2026-04-02 22:13:44 EDT
Runtime: 2m 13s
[ralph-garage/agent-logs/20260402T221344.373115-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T221344.373115-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: FAIL
REASON: The paper broadens the spec's definitions of "AI singularity" and "negative AI singularity" so that the model encompasses cases the spec excludes.

---

## Concept 1: AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**

- **Abstract:** "a sudden AI-driven productivity surge that displaces existing workers and firms" — consistent with "sudden" and productivity increase; "surge" implies large magnitude.
- **Introduction:** "A sudden AI breakthrough---a singularity---could dramatically increase productivity" — "dramatically" aligns with "vastly."
- **Model (Section 2.1):** "A singularity is an absorbing event that arrives with independent probability $p$ each period." Output shifts from growth rate $g$ to $\tilde{g} > g$, i.e., "a strictly higher rate, reflecting the productivity increase that accompanies the singularity." The paper then states: "The model allows for any magnitude of productivity increase; the extension explores the limit $\tilde{g} \to \infty$, corresponding to a singularity that vastly increases output."
- **Extension (Section 4):** The limit $\tilde{g} \to \infty$ is described as "corresponding to a singularity that vastly increases output."

**Finding:** The spec defines "AI singularity" with the qualifier "vastly increases productivity." The model only requires $\tilde{g} > g$, which includes arbitrarily small improvements (e.g., growth rising from 2% to 2.1%). The paper explicitly acknowledges this generality ("allows for any magnitude") and reserves "vastly increases output" for the $\tilde{g} \to \infty$ limit. This means the paper's baseline model labels events as "singularities" that the spec would not classify as singularities. The introduction uses "dramatically," which is closer to the spec, but the formal model drops this qualifier.

**Verdict on this concept: INCONSISTENT.** The model's use of "singularity" is broader than the spec's definition. The paper uses "singularity" throughout (Assumptions 1–3, Propositions 1–3, numerical illustration) for the event defined by $\tilde{g} > g$, not restricted to "vastly increases."

---

## Concept 2: Negative AI Singularity

**Spec definition:** "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- **Abstract:** "a negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms" — "displaces" suggests severity but doesn't explicitly say "devastating."
- **Model, Assumption 1 (Negative singularity):** "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$." Equivalently, $\Delta < 1$.
- **Results (Section 3):** "the household is displaced at the singularity ($\Delta < 1$)" — no magnitude qualifier.
- **Numerical illustration:** $\Delta = 0.75$ (household share drops from 60% to 45%) — this could reasonably be called "devastating."

**Finding:** The spec requires that a negative AI singularity be "devastating for the typical investor." Assumption 1 only requires $\Delta < 1$, which includes near-zero displacement (e.g., $\Delta = 0.999$, a 0.1% decline in the household's share). The paper never restricts its use of "negative singularity" to cases where the displacement is devastating. The numerical illustration chooses parameters that are plausibly devastating, but the theoretical results and propositions apply to all $\Delta < 1$, including mild cases.

**Verdict on this concept: INCONSISTENT.** The formal definition of "negative singularity" in the paper (Assumption 1) is weaker than the spec's requirement of "devastating."

---

## Concept 3: Budget Constraints

**Spec definition:** "A core element of asset pricing theory... is that budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- **Section 2.3:** The household's budget constraint is stated in equation (6): $c_t + P_t^A n_{t+1}^A + P_t^N n_{t+1}^N = (D_t^A + P_t^A) n_t^A + (D_t^N + P_t^N) n_t^N$.
- Market clearing ($n_t^A = n_t^N = 1$) plus the budget constraint determines $c_t = D_t^A + D_t^N = \omega Y_t$.
- Output shares sum to 1: $\theta + \nu + (1 - \theta - \nu) = 1$ and $\tilde{\theta} + \tilde{\nu} + (1 - \tilde{\theta} - \tilde{\nu}) = 1$.

**Finding:** Budget constraints are explicitly stated and satisfied. Output shares sum to one in both regimes. Consumption is pinned down by market clearing and the budget constraint. No violations detected.

**Verdict on this concept: CONSISTENT.**

---

## Concept 4: Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. For example, if the representative investor cannot buy equity in privately-held AI firms, then markets are incomplete. Incomplete markets does not necessarily refer to Arrow-Debreu securities." "Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- **Introduction:** "Private AI ventures and yet-to-be-created firms would capture much of the new value, but the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets..."
- **Section 2.1:** "AI owners hold private AI capital and do not participate in public stock markets."
- **Section 2.3:** "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital."
- **Proposition 3:** "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output: $c_t = Y_t$."
- **Conclusion:** "any mechanism that allows the representative household to share in AI upside reduces the hedging premium"

**Finding:** The paper consistently frames incomplete markets as the household's inability to invest in private AI capital. Complete markets are defined by the household gaining access to this asset. No reference to Arrow-Debreu securities. Discussions focus squarely on the specific unavailable asset (private AI capital). This matches the spec's framing precisely, including the spec's example ("if the representative investor cannot buy equity in privately-held AI firms").

**Verdict on this concept: CONSISTENT.**

---

## Concept 5: Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- **Abstract:** "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity" and "uniquely valuable as partial insurance against displacement."
- **Introduction:** "publicly traded AI stocks offer the best available hedge: they are the investor's only tradeable claim on the AI upside."
- **Introduction:** "hedging premium: in singularity states, the household's marginal utility is high... while AI stocks pay relatively more. This positive covariance between the stochastic discount factor and AI dividends lowers the required return and raises the valuation."
- **Results (Section 3):** "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices. AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge."
- **Proposition 3:** The "hedging premium" $V_0^A - V_0^{A,\text{CM}} > 0$ is isolated formally.

**Finding:** The paper uses "hedge" to mean that AI stocks' payoffs increase when the singularity risk materializes ($\tilde{\theta}/\theta > 1$). This matches the spec's definition. The paper explicitly notes the hedge is partial ("partial insurance," "best available hedge"), consistent with the spec's "need not be perfect." The paper does not claim AI stocks earn a negative risk premium—they command a higher price-dividend ratio, which is a different statement. Usage is consistent across all sections.

**Verdict on this concept: CONSISTENT.**

---

## Concept 6: General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:** The paper does not use the terms "general equilibrium" or "partial equilibrium" anywhere.

**Finding:** Since neither term appears in the paper, there is no opportunity for inconsistency with the spec. The paper's model does determine prices through equilibrium conditions (the Euler equation and market clearing), which is general equilibrium in the spec's sense, though the paper does not label it as such.

**Verdict on this concept: NOT APPLICABLE (terms not used).**

---

## Cross-Section Consistency Check

- **"Singularity"**: Used in the abstract, introduction, model, results, extension, and conclusion. The meaning is consistent within the paper (absorbing event with $\tilde{g} > g$ and share shifts), but this paper-internal definition is broader than the spec as noted above.
- **"Displacement"/"displaced"**: Used consistently throughout to mean the household's consumption share falling ($\Delta < 1$).
- **"Hedging premium"**: Introduced in the introduction, formalized in Section 3 (Proposition 3), and discussed in the extension and conclusion. Meaning is stable: the valuation gap between incomplete- and complete-market AI stock prices.
- **"Incomplete markets"**: Used in the introduction, model, and results sections. Always refers to the household's inability to invest in private AI capital.

No cross-section drift detected in the paper's internal usage. The inconsistencies are between the paper and the spec, not between sections of the paper.

---

## Summary of Findings

| Concept | Verdict |
|---|---|
| AI Singularity | **INCONSISTENT** — model allows non-vast productivity increases |
| Negative AI Singularity | **INCONSISTENT** — model allows non-devastating displacement |
| Budget Constraints | Consistent |
| Complete vs. Incomplete Markets | Consistent |
| Hedging | Consistent |
| General vs. Partial Equilibrium | Not applicable |
