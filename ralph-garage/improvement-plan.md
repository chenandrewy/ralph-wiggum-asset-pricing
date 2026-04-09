# Improvement Plan
AUTHOR PLAN — 2026-04-09 17:48:46 EDT

## Current State

**Tests: 9 pass / 16 fail.** No overhaul needed — the model structure is sound — but the paper has critical formula display errors, a broken narrative about "catastrophic" displacement, and several content gaps.

---

## Priority 1: Fix Mathematical Errors (paper + code)

### 1a. P/D formula display errors (eqs 4, 5, 8)

The displayed formulas use $(1+\eta)^{1-\gamma}$ but the correct expression (matching the proof and the code) is $(1+\eta)^{-\gamma}$ when multiplied by $\Gamma^j$. The paper has an extra factor of $(1+\eta)$. Additionally, eq (4) has numerator $A/(1-AB)$ but the proof derives $AB/(1-AB)$ (i.e., $K/(1-K)$). Fix the displayed formulas to match the code.

**Affected tests:** factcheck-code, factcheck-bysection, factcheck-freely, factcheck-exhibits

### 1b. Fix "catastrophic" narrative and parameterization

With $\phi = 0.7$ and $\eta = 0.5$, household consumption *grows* by 5% in a singularity ($\phi(1+\eta) = 1.05$). The paper falsely claims consumption "drops sharply." Two options:
- **Option A (preferred):** Lower $\phi$ to 0.5, so $\phi(1+\eta) = 0.75$ — a genuine 25% consumption drop. Regenerate table and figures.
- **Option B:** Reframe narrative to emphasize *share* loss rather than absolute consumption decline.

Option A is preferred because it makes the "catastrophic" framing truthful, strengthens the hedging motivation, and makes Figure 2 panel (b) visually compelling (consumption below 1 at $\tau=0$).

**Affected tests:** factcheck-code, factcheck-bysection, element-transfers-fig, factcheck-exhibits

### 1c. Fix limit equation (10)

The ratio $c^H_{post}/c^H_{no\text{-}transfer}$ is actually a finite constant independent of $\eta$. The paper incorrectly writes $\to \infty$. Fix to show that the *level* of post-transfer consumption grows without bound, not the ratio. Or redefine the ratio relative to pre-singularity consumption.

**Affected tests:** factcheck-bysection, factcheck-freely

### 1d. Fix Proposition 2(iii)

The claim that the P/D *ratio* may increase in $\xi$ is contradicted by the table (monotonic decrease at every $p$). Either prove it for different parameters, or correct the proposition to state the ratio decreases.

**Affected tests:** factcheck-bysection, factcheck-freely

### 1e. Remove dangling $R_f$ from Proposition 1

Defined but never used. Delete the sentence.

**Affected tests:** theory-deadweight, factcheck-theory

### 1f. Fix $\alpha_t$ domain

Change $\alpha_t \in (0,1]$ to $\alpha_t \in (0, 1 - \theta_t]$ to prevent negative private AI capital dividends.

**Affected tests:** factcheck-theory

---

## Priority 2: Fix Content Gaps

### 2a. Add entry-dynamics disclaimer

The spec (I.4.d) requires an explicit statement that we do NOT model entry dynamics. Add a sentence in Section 2.1 (near the AI owners paragraph) and in Section 2.3: "Importantly, we do not explicitly model the entry of new cohorts; AI owners are a static group."

**Affected tests:** theory-unmodeled-channels

### 2b. Fix Figure 1 — fabricated data

Either:
- **(Preferred)** Label the figure clearly as "illustrative" in caption and text. Change paper text from "plots the price-to-earnings ratios" to "illustrates the pattern of price-to-earnings ratios" with a note that values are approximate.
- Or download real CRSP/market data (but spec says do not download additional data, and scope should stay limited).

Also address P/E vs P/D conflation: add a brief note that P/E ratios proxy for P/D ratios here.

**Affected tests:** element-opening-fig, factcheck-code, factcheck-exhibits

### 2c. Add missing lit citations

Add to the lit review:
- **Kogan and Papanikolaou (2014, JF)** — technology shocks, displacement risk, and cross-section of returns
- **Kogan, Papanikolaou, and Stoffman (2020, JPE)** — creative destruction, stock returns, inequality

These are the most critical gaps. Consider also Papanikolaou (2011, JFE) if space permits.

**Affected tests:** element-lit-review

### 2d. Fix GKP citation issues

- Remove defensive meta-commentary: "We are intentionally modest about our incremental contribution relative to their framework." Show modesty through substance, not proclamation.
- Fix misattribution in Section 4.2: GKP mention broader trading as a technical remark, not a normative policy prescription. Soften the framing.

**Affected tests:** element-gkp-cites

### 2e. Trim abstract to 100 words

Currently ~103 words. Cut 3-4 words.

**Affected tests:** spec-paper

---

## Priority 3: Presentation Fixes

### 3a. Tone down AI-authorship paragraph in intro

The standalone disclosure paragraph is too prominent and self-congratulatory. Fold the disclosure into 1-2 sentences within another paragraph rather than giving it its own block. Remove "If AI can produce passable academic research..." — it alienates the reader.

**Affected tests:** element-rhetoric-meta, writing-intro

### 3b. Fix Figure 2 legend rendering

Unicode $\eta$ renders as ".." in PDF. Use R expression syntax or plotmath instead of Unicode characters in legend labels.

**Affected tests:** visual-figures-image-only

### 3c. Improve intro flow

- Give more prominence to arguments (c) and (d) from the spec: financial market solutions are under-discussed; singularity overcomes frictions.
- Smooth transition between GKP comparison paragraph and the extensions discussion.
- Ensure extinction risk claim matches Proposition 2(iii) after it's corrected.

**Affected tests:** writing-intro, factcheck-narrative

---

## Execution Order

1. **Code first:** Update `generate-exhibits.R` — change $\phi$ to 0.5 (or chosen value), fix legend rendering. Regenerate all exhibits.
2. **Formulas:** Fix eqs (4), (5), (8), (10) in `paper.tex`. Fix Proposition 2(iii). Remove $R_f$. Fix $\alpha_t$ domain.
3. **Narrative:** Rewrite "catastrophic" claims in Section 4.2, fix limit discussion, update table commentary to match new numbers.
4. **Content:** Add entry-dynamics disclaimer, fix Figure 1 labeling, add missing citations, fix GKP framing.
5. **Writing:** Trim abstract, tone down AI-authorship paragraph, improve intro flow.
6. **Verify:** Recompile paper, rerun tests.
