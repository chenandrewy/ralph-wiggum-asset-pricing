# Improvement Plan

## Current State

- **Tests**: All pass (spec-compliance, theory-correctness).
- **Referee (referee-top3)**: Two substantive comments, both actionable.
- **CFR-R1**: Largely addressed — GKP differentiation and Jones 2024 extension are in the paper.

## Key Issues

### 1. Constant-λ tension with Figure 1 (referee-top3 #1)

The model assumes constant λ. With differential growth, s_t rises and the premium *erodes* — the opposite of what Figure 1 shows (widening gap post-2023). The model cannot explain its own motivating time-series fact. This is the most important issue.

**Options**: (a) Add time-varying λ (two-state Markov chain), or (b) reframe as a cross-sectional story and acknowledge the limitation.

**Decision**: Option (b). Adding a Markov chain for λ_t is a significant model extension that risks bloating the paper beyond 20 pages. The cleaner fix is to reframe the contribution as cross-sectional (why AI stocks are expensive *relative to* non-AI stocks at any point in time) and explicitly address the time-series limitation. The paper already hints at this ("part of the explanation") but needs to be more disciplined about it.

### 2. Testable implications lack empirical content (referee-top3 #2)

Section 3.4 identifies a sharp prediction but defers all empirical work. The referee wants at least suggestive evidence — even a small event-study table (5-10 events) showing AI abnormal returns around singularity-risk events conditional on earnings controls.

**Decision**: Add a small event-study exhibit. Use AI capability/safety announcements (e.g., GPT-4 release, major AI safety incidents, executive orders) and show abnormal returns for AI stocks relative to earnings-revision controls. This is feasible with existing data and strengthens the paper without requiring a full empirical section.

### 3. Minor: Proposition 6 proof imprecision (theory-correctness note)

The proof sketch claims |(\theta+\phi)(J^{-\gamma}-1)| ~ θ^{1-\gamma}, but for large θ, J^{-\gamma}-1 → -1, so the expression grows as ~θ. The conclusion Δ^hedge → 0 still holds because (1-π) → 0 dominates. Fix the proof sketch.

## Plan

### Step 1: Reframe as cross-sectional story

- **Intro**: Adjust the framing. Figure 1 motivates the *level* of the AI premium (AI stocks trade at 2-2.7x market P/D). Stop implying the model explains the *widening* post-2023. Add a sentence acknowledging that the time-series dynamics (the post-2023 acceleration) require time-varying beliefs about singularity risk, which is beyond the scope of this paper.
- **Section 3.4 (Testable Implications)**: Frame the erosion prediction (rising s_t shrinks premium) as a long-run cross-sectional prediction. Note that the constant-λ model is silent on short-run time-series variation driven by belief shocks. Mention that extending to time-varying λ_t is a natural direction for future work.

### Step 2: Add event-study evidence

- Create an R script to compute abnormal returns for AI stocks around 5-10 singularity-risk events (AI capability announcements, safety incidents, regulation). Use a simple market model or Fama-French 3-factor residuals. Show a small table or figure with cumulative abnormal returns (CARs) and confidence intervals.
- Add a brief empirical subsection (or expand Section 3.4) presenting this evidence as suggestive, not definitive. The prediction: events that shift perceived singularity risk without revising near-term earnings should move AI valuations.
- Keep it compact — one exhibit maximum.

### Step 3: Fix Proposition 6 proof sketch

- Correct the intermediate bound: note that the dominant convergence comes from (1-π) → 0 (super-linear decay), not from the J^{-γ} factor.
