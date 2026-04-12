# tests/factcheck-narrative.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 3m 6s
[ralph-garage/agent-logs/20260411T214322.774994-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T214322.774994-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative

VERDICT: PASS
REASON: Every section delivers on its stated contract, cross-references resolve correctly, and no verbal claim exceeds the evidence the paper provides.

---

## Section-by-Section Analysis

### Abstract

- **Contract**: AI stocks have high valuations partly from hedging against displacement under incomplete markets; incompleteness distorts valuations and AI development; government transfers become compelling when singularity growth overwhelms deadweight costs; the paper itself was produced by AI agents.
- **Deliverables**: The body delivers all four claims: Sections 2--3 establish the hedging/valuation mechanism, Section 4.1 establishes the development-distortion (veto) result, Section 4.2 establishes the government-transfer mechanism, and a footnote in Section 1 plus the abstract's closing sentence cover the self-referential AI-production claim.
- **Status**: FULFILLED.

### Section 1: Introduction

- **Contract**: Motivate high AI valuations empirically (Figure 1), introduce the hedging mechanism, state the three linked results (valuation premia, veto distortion, government transfers), and provide a roadmap.
- **Deliverables**: Figure 1 illustrates elevated P/D ratios and NASDAQ vs. S&P 500 divergence. The hedging mechanism is explained verbally and tied to the model. The three results are previewed with forward references to Propositions 1--3 and Sections 2--5. A lit review closes the introduction.
- **Status**: FULFILLED. Every claim made in the introduction is delivered by the referenced body section. Specific numerical claim ("at a singularity probability of one percent, P/D ratios for AI stocks roughly double") is confirmed by Table 1 (p=1%, xi=0%: ratio = 2.0). The roadmap matches the actual section structure.

### Section 1 (Lit Review)

- **Contract**: Situate the paper relative to existing literature, with emphasis on GKP (2012) and Jones (2024).
- **Deliverables**: GKP and Jones are discussed with specific connections to the paper's mechanism. Additional citations cover creative destruction, macro AI growth, rare disasters, and technological revolutions.
- **Status**: FULFILLED.

### Section 2.1: Setup

- **Contract**: Define the model primitives (agents, consumption, singularity, assets, preferences).
- **Deliverables**: Defines the representative household and AI owners, aggregate consumption growth, singularity mechanics (displacement and extinction), two public assets (AI and non-AI stocks) with dividend dynamics, restricted equity as the source of market incompleteness, and CRRA preferences. Clarifies that AI owners are analogous to GKP's future innovators but that entry dynamics are not modeled.
- **Status**: FULFILLED.

### Section 2.2: Equilibrium Prices

- **Contract**: Derive equilibrium price-dividend ratios.
- **Deliverables**: Proposition 1 provides closed-form P/D ratios for both assets. Remark 1 states the existence condition. Proposition 2 establishes that extinction attenuates the valuation spread. Proofs are provided (Proposition 2 in-text, Proposition 1 in the appendix). The text explains the economic content of the formulas (the hedging channel via comparison of Gamma^AI and Gamma^N) and notes the approximation used in the closed form.
- **Status**: FULFILLED. The section title promises "Equilibrium prices" and delivers closed-form expressions, an existence condition, and comparative statics. The approximation is disclosed and the numerically exact values are deferred to Table 1.

### Section 2.3: Discussion

- **Contract**: Discuss the model's mechanism and its relationship to prior work.
- **Deliverables**: Compares the model to GKP (2012), explains the role of market incompleteness (complete markets would collapse the premium), discusses the existence-condition discontinuity unique to discrete singularities, and motivates the extensions.
- **Status**: FULFILLED.

### Section 3: Quantitative Analysis

- **Contract**: Provide quantitative analysis of the model's predictions.
- **Deliverables**: Table 1 reports P/D ratios across a grid of singularity probabilities and extinction risks. Parameterization is stated. Three patterns are identified and discussed: (1) AI P/D > non-AI P/D across the grid, (2) the premium rises with p, (3) extinction compresses the premium. Magnitudes are compared to observed data (Figure 1).
- **Status**: FULFILLED. Numerical claims in the text match Table 1 exactly: p=0.5%/xi=0% gives AI P/D of 15.5 vs. non-AI of 11.1 (ratio 1.4); p=1%/xi=0% gives ratio of 2.0. The comparison to empirical data is appropriately hedged ("This comparison is imperfect").

### Section 4: Extensions (framing)

- **Contract**: "Examines two further consequences" of market incompleteness: distortion of AI development and government policy.
- **Deliverables**: Two subsections deliver exactly these two topics.
- **Status**: FULFILLED.

### Section 4.1: Veto and Efficient Development

- **Contract**: Show that market incompleteness distorts the development of AI.
- **Deliverables**: Augments the baseline with a positive singularity. Defines social efficiency (Kaldor-Hicks). Introduces a veto mechanism with deadweight cost. Proposition 3 proves that (i) under incomplete markets, sufficiently risk-averse households veto even socially efficient AI development, and (ii) under complete markets they do not. A numerical example is provided. Discussion connects to extinction risk and wealth heterogeneity.
- **Status**: FULFILLED. Both "veto" and "efficient development" are delivered. The proposition proves what it claims. The numerical example is consistent with the stated parameters.

### Section 4.2: Government Transfers

- **Contract**: Show that government transfers can address the incomplete-markets problem, especially under singularity-driven growth.
- **Deliverables**: Models transfers with deadweight costs. Derives effective displacement parameter phi_eff. Shows that the transfer ratio is independent of eta, so explosive growth makes even inefficient transfers effective. Provides a specific numerical illustration (delta=0.9, tau=0.30 yields 3.5x consumption multiple). Figure 2 illustrates P/D compression and consumption gains across two parameterizations. Discusses the existence-condition violation at low tau under extreme displacement. Policy implications are stated.
- **Status**: FULFILLED. The numerical claim (3.5x at delta=0.9, tau=0.30) is verified by direct computation from equation (7). The section delivers both the pricing effect (P/D compression) and the real effect (veto elimination) mentioned in the opening paragraph.

### Section 5: Conclusion

- **Contract**: Summarize the paper's contributions.
- **Deliverables**: Restates the three linked results (hedging-based valuation premia, veto distortion, government transfers). Acknowledges the model's deliberate simplicity.
- **Status**: FULFILLED.

### Appendix A: Proof of Proposition 1

- **Contract**: Prove Proposition 1 (P/D ratios).
- **Deliverables**: Derives the Euler equation, expands it across the three states, solves for the P/D ratio, and notes the approximation and the numerical method for exact values.
- **Status**: FULFILLED.

---

## Cross-Reference Audit

| Reference | Location | Target | Resolves? |
|---|---|---|---|
| Figure 1 | Intro para 1, Sec 3 | fig-ai-valuations (Exhibit 1) | Yes |
| Table 1 | Sec 3 | tab-pd-ratios (Exhibit 2) | Yes |
| Figure 2 | Sec 4.2 | fig-extension-panels (Exhibit 3) | Yes |
| Proposition 1 | Intro, Sec 2.2, Sec 4.2, App A | prop:pd-ratios in Sec 2.2 | Yes |
| Proposition 2 | Intro, Sec 3 | prop:comp-statics in Sec 2.2 | Yes |
| Proposition 3 | Intro, Sec 4.1 | prop:veto in Sec 4.1 | Yes |
| Remark 1 | Sec 2.3, Sec 4.2, Fig 2 caption | rem:existence in Sec 2.2 | Yes |
| Section 2 | Intro roadmap | sec:model | Yes |
| Section 3 | Intro roadmap | sec:quant | Yes |
| Section 4 | Intro roadmap | sec:extensions | Yes |
| Section 5 | Intro roadmap | sec:conclusion | Yes |
| Section 4.2 | Remark 1 | sec:ext2 | Yes |
| Appendix A | Prop 1 proof, Sec 2.2, Table 1 note | app:proof-pd | Yes |
| Equation refs (1)--(10) | Various | Corresponding equations | Yes |

All cross-references resolve to content that exists and matches what the referring text claims.

---

## Claim-Strength Audit

1. **"P/D ratios for AI stocks roughly double relative to non-AI stocks"** (Intro). Table 1 confirms ratio = 2.0 at p=1%, xi=0%. Claim matches evidence.

2. **"Proposition 2 quantifies this attenuation"** (Intro). Proposition 2 provides a comparative static with a full proof. The word "quantifies" is slightly strong for a qualitative monotonicity result, but the table provides numerical support, and the proof gives the exact mechanism. Borderline but acceptable.

3. **"AI development is socially efficient in the Kaldor-Hicks sense"** (Sec 4.1). Defined and justified: aggregate consumption rises by (1+eta), so total surplus is positive. Claim matches the definition provided.

4. **"even grossly inefficient redistribution transforms a 50% consumption loss into a 250% gain"** (Sec 4.2). Verified by direct computation from equation (7): at delta=0.9, tau=0.30, eta=9, phi=0.05, the consumption multiple is ~3.5x vs. 0.5x without transfers. Claim matches evidence.

5. **"the valuation spread widens with displacement severity... and with singularity probability"** (Sec 2.2). These follow directly from inspection of the P/D formulas and are confirmed by Table 1. Claim matches evidence.

6. **"This comparison is imperfect"** (Sec 3, re: empirical match). Appropriately hedged. The caveats (NASDAQ broader than AI stocks, earnings growth vs. multiples, S&P 500 AI exposure) are specific and honest.

7. **"Calls to slow or halt AI development may partly reflect investors' inability to hedge"** (Sec 4.1). Qualified with "may partly reflect," which is appropriately modest for a model-based inference. No overclaim.

No claims were found to exceed the evidence provided.

---

## Summary

The paper's verbal narrative is internally consistent and well-calibrated. Every section delivers what its title and opening framing promise. All cross-references resolve correctly. Numerical claims in the text match the exhibits. Verbal claims are either directly supported by the paper's formal results or appropriately hedged. The Abstract and Introduction claims are fully supported by the body sections.
