# tests/factcheck-narrative.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 2m 6s
[ralph-garage/agent-logs/20260402T184535.063782-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T184535.063782-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative

VERDICT: PASS
REASON: Every section delivers what its title and framing promise, cross-references are accurate, and no verbal claim exceeds the evidence provided.

---

## Section-by-Section Analysis

### Abstract

- **Contract**: Summarize the paper's main results: hedging premium, role of incomplete markets, effect of singularity probability, complete-markets benchmark, and abundance/transfers result.
- **Deliverables**: Six claims: (1) AI stocks command a valuation premium as a hedge, (2) representative household cannot invest in private AI capital, (3) P/D ratio increases with singularity probability when displacement is severe, (4) complete markets eliminates the premium, (5) abundant output + modest transfers can eliminate displacement risk.
- **Status**: FULFILLED. Each claim maps to a specific result in the body: (1) Proposition 2, (2) Section 2.1/2.3, (3) Proposition 3, (4) Proposition 4, (5) Remark 2. The abstract's qualifier "when displacement is sufficiently severe" correctly reflects Proposition 3's condition.

### Preface (TBC) (unnumbered)

- **Contract**: Left blank per spec requirement.
- **Deliverables**: Empty section.
- **Status**: FULFILLED. The spec requires this section to be blank.

### Section 1: Introduction

- **Contract**: Motivate the paper, present empirical evidence, outline the model and main results, situate in the literature.
- **Deliverables**: (a) Empirical motivation with Figure 1 (AI vs. non-AI P/D ratios from CRSP), (b) intuitive explanation of the hedging channel, (c) model overview (two assets, representative household, AI owners, singularity as absorbing event), (d) summary of four main results (closed-form P/D, increasing in p, complete-markets benchmark, extension), (e) self-referential paragraph on AI authorship, (f) literature review paragraph.
- **Status**: FULFILLED. Every claim made in the introduction is delivered by a corresponding section in the body. The intro says "We derive the price-dividend ratio of AI stocks in closed form" (Proposition 1 delivers), "the ratio increases with the probability of a singularity" with qualifier "Under natural parameter restrictions" (Proposition 3 delivers with condition), "Under complete markets, the household could invest in private AI capital, eliminating displacement risk and the hedging premium" (Proposition 4 delivers), and the extension claims are delivered by Section 4.

### Section 2.1: Environment

- **Contract**: Define the economic environment: time, output, agents, singularity.
- **Deliverables**: Discrete time, aggregate output with normal growth rate g, singularity as absorbing event with probability p producing higher growth rate g-tilde, two agent types (representative household, AI owners), interpretation of AI owners following GKP.
- **Status**: FULFILLED. All elements of the economic environment are specified.

### Section 2.2: Assets and Dividends

- **Contract**: Define the asset structure and dividend processes.
- **Deliverables**: Three dividend streams (public AI, non-AI, private AI) as shares of output, pre- and post-singularity shares, two named assumptions (Assumption 1: negative singularity; Assumption 2: AI share growth), definition of displacement ratio Delta.
- **Status**: FULFILLED. The section defines exactly what the title promises.

### Section 2.3: The Household's Problem

- **Contract**: Specify the household's optimization problem.
- **Deliverables**: CRRA preferences, budget constraint with two traded assets, market clearing (n=1 for both), equilibrium consumption, Euler equation.
- **Status**: FULFILLED. The household's problem is fully specified, including the key restriction that the household cannot invest in private AI capital.

### Section 2.4: Equilibrium

- **Contract**: Characterize the equilibrium.
- **Deliverables**: Statement that P/D ratios are constant in each regime (with explanation: i.i.d. growth rates), Assumption 3 (existence conditions ensuring finite P/D ratios), note that these are automatic for gamma > 1.
- **Status**: FULFILLED. The section establishes that equilibrium P/D ratios exist and are constant, setting up the derivation in Section 3. This is a standard theory-paper structure where model setup (Section 2) precedes results (Section 3).

### Section 3: Results

- **Contract**: Present the paper's main theoretical results.
- **Deliverables**: Four propositions with proofs, a numerical illustration, and interpretive discussion.
- **Status**: FULFILLED. See sub-analysis below.

**Proposition 1 (P/D ratios)**: Delivers closed-form expressions for AI and non-AI P/D ratios. Proof is inline and complete.

**Proposition 2 (AI stocks trade at a premium)**: Delivers the cross-sectional spread V_0^A - V_0^N > 0 with inline proof.

**Post-Proposition 2 paragraph**: States that the spread increases with p and (1-Delta). These are informal comparative statics supported by inspection of equation (12). No formal proof is given, but the claims are presented as observations from the formula, which is standard practice.

**Proposition 3 (Singularity probability raises AI valuations)**: Delivers the comparative static dV_0^A/dp > 0 with an explicit necessary-and-sufficient condition. Proof is deferred to Appendix A, which contains it.

**Proposition 4 (Incomplete vs. complete markets)**: Derives complete-markets P/D ratio, isolates hedging premium, proves it is positive. Inline proof.

**Numerical illustration**: Reports specific parameter values and resulting P/D ratios. Claims: V_0^A ~ 16.1 at p=0.01 (Table: 16.1), V_0^N ~ 11.6 (Table: 11.6), ratio ~1.4 (16.1/11.6 = 1.39), no-singularity baseline ~11.9 (Table: 11.9/11.9), complete-markets V_0^{A,CM} ~ 12.9 (Table: 12.9), hedging premium "about 25%" (Table: 24.8%). All verified against Table 1.

### Section 4: Extension: Singularity, Extinction, and Frictions

- **Contract**: Extend the baseline model in two directions: extinction risk and overcoming frictions.
- **Deliverables**: Two subsections addressing each direction.
- **Status**: FULFILLED.

### Section 4.1: Extinction Risk

- **Contract**: Incorporate the possibility that the singularity destroys the economy.
- **Deliverables**: Modified P/D ratio formula with extinction probability q (equation 17), discussion of how extinction attenuates the hedging premium, connection to Jones (2024) on utility curvature, Remark 1 on the limit as g-tilde goes to infinity.
- **Status**: FULFILLED. The section delivers a formal modification of the pricing formula and interprets it economically.

### Section 4.2: Overcoming Frictions

- **Contract**: Analyze when the frictions that sustain displacement risk can be overcome (the "Coase theorem in the singularity").
- **Deliverables**: Discussion of GKP's friction assumption, transfer cost model (F + tau*T), equation (18) showing fixed costs vanish as Y grows, Remark 2 formalizing the result.
- **Status**: FULFILLED. The section promises a formal analysis of how transfer mechanisms scale with output, and delivers it via a cost model with fixed and proportional components. This goes beyond merely citing a number---it provides a structured argument with a displayed equation.

### Section 5: Conclusion

- **Contract**: Summarize the paper's contributions.
- **Deliverables**: Restates main results (hedging premium, cross-sectional prediction, complete-markets benchmark), summarizes the extension's two channels (Remark 1 and Remark 2), notes that financial market solutions to AI disaster risk are under-discussed, suggests policy implications (expanding tradeable AI assets).
- **Status**: FULFILLED. Every claim in the conclusion is supported by results in the body. The cross-references to Remark 1 and Remark 2 are accurate.

### Appendix A: Proofs

- **Contract**: Provide deferred proofs.
- **Deliverables**: Proof of Proposition 3.
- **Status**: FULFILLED. The only deferred proof (Proposition 3) is provided.

---

## Cross-Reference Audit

| Reference | Location | Target | Status |
|-----------|----------|--------|--------|
| Figure 1 (ai-valuations) | Section 1 | exhibits/ai-valuations.pdf | EXISTS |
| Table 1 (numerical) | Section 3 | exhibits/numerical-illustration.tex | EXISTS |
| Assumption 1 | Propositions 1-4 | Section 2.2 | EXISTS |
| Assumption 2 | Propositions 1-4 | Section 2.2 | EXISTS |
| Assumption 3 | Propositions 1-4 | Section 2.4 | EXISTS |
| Appendix A | Proposition 3 proof | Appendix A | EXISTS, contains proof |
| Remark 1 | Conclusion | Section 4.1 | EXISTS |
| Remark 2 | Conclusion | Section 4.2 | EXISTS |
| Equation references | Throughout | Throughout | ALL VALID |

No broken cross-references found.

---

## Claim-Strength Audit

1. **"We show that publicly traded AI stocks command a valuation premium"** (Abstract, Conclusion): Supported by Proposition 2 and Proposition 4. APPROPRIATE.

2. **"The price-dividend ratio of AI stocks increases with the probability of a singularity when displacement is sufficiently severe"** (Abstract): Accurately reflects the conditional result in Proposition 3. APPROPRIATE.

3. **"The valuation spread...increases with the singularity probability p and with the severity of displacement"** (post-Proposition 2): Informal comparative static stated without formal proof. The claim follows from inspection of equation (12), which is displayed. APPROPRIATE for the context, though slightly stronger than what is formally proved.

4. **"Automatically satisfied for gamma > 1, the empirically relevant case"** (Assumption 3): Mathematical claim about the existence conditions. APPROPRIATE---standard observation for CRRA models.

5. **"A 1% annual singularity probability generates a hedging premium of about 25%"** (numerical illustration): Table shows 24.8% at p=0.01. APPROPRIATE.

6. **"Our contribution relative to GKP is purposefully modest"** (Introduction): Consistent with the paper's framing throughout. The paper explicitly states that the main insights originate in GKP. APPROPRIATE.

7. **"GKP...do not conduct a formal analysis of how these mechanisms scale with output. We take up this question."** (Section 4.2): The paper does provide a formal cost-scaling argument. Whether GKP truly omit this is a factual claim about an external paper, which this test cannot verify, but the claim is specific and falsifiable. NOTED but not flagged.

---

## Narrative Consistency

The paper tells a coherent, linear story: empirical motivation (Section 1) -> model setup (Section 2) -> closed-form results with numerical illustration (Section 3) -> extensions connecting to broader literature (Section 4) -> conclusion (Section 5). Later sections consistently build on earlier ones without relying on unfulfilled promises. The abstract and introduction accurately preview what the body delivers.
