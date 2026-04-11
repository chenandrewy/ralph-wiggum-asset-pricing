# Improvement Plan
AUTHOR PLAN — 2026-04-10 22:03:35 EDT

## Assessment

No overhaul needed. The model is mathematically correct, the code produces correct exhibits, and the paper addresses the referee report. After 14 rloop iterations, the paper is structurally sound. Improvements target model clarity, quantitative depth in Extension 1, and tighter alignment with the referee's suggestions.

## Issues

1. **Model clarity on α vs θ (Section 2.1).** The model defines two share variables—α_t (household consumption share) and θ_t (AI dividend share)—but never explains their relationship. Since D^AI + D^N = C_t, a reader may wonder where AI owners' private claims come from if public stocks already account for all aggregate consumption. The answer is that AI owners also hold public stocks; the household is the *marginal* investor, not the sole investor. This needs a brief clarification to make the incomplete-markets story airtight.

2. **Extension 1 (Veto) lacks quantitative teeth.** Proposition 3 is purely qualitative ("for γ sufficiently large"). Extension 2 has a compelling two-panel figure; Extension 1 has nothing quantitative. A brief numerical example showing the household vetoes at baseline parameters would strengthen this section significantly.

3. **Referee suggestion on Jones (2024) heterogeneity.** The referee specifically asked the paper to engage with Jones (2024)'s observation that rich and poor households hold heterogeneous views about AI risk. The paper uses Jones only for extinction risk. A brief remark connecting the model's displacement mechanism to Jones's rich-vs-poor framing would directly address this referee comment and differentiate the paper from GKP.

4. **Introduction flow.** After 14 iterations of reworking, verify the introduction reads cleanly from start to finish: each paragraph should set up the next, and the GKP contribution framing should remain appropriately modest per spec.

## Plan

### Step 1: Clarify α vs θ in model setup (paper)

In Section 2.1, after the "Assets" paragraph, add 2–3 sentences:
- Public stock dividends (D^AI + D^N = C_t) are distributed among all investors, not solely the household.
- The household's consumption α_t C_t reflects the net outcome of its portfolio returns (from public stocks it holds) and any labor-like income.
- AI owners hold restricted equity *and* some public stocks; the household is the marginal investor setting prices via its Euler equation, not necessarily the sole holder.

This makes explicit why α_t < 1 is consistent with the dividend structure and why market incompleteness (the household cannot trade restricted AI equity) matters for pricing.

### Step 2: Add quantitative veto example (paper + code)

In Section 4.1, after Proposition 3's proof, add a brief numerical illustration:
- Use baseline parameters plus a positive-singularity probability (e.g., 70% positive, 30% negative conditional on non-extinction).
- Compute the household's expected utility with and without AI development, including a veto cost.
- Show that the household vetoes even when development is socially efficient and the veto cost is substantial.
- Show that under complete markets (household consumption share doesn't drop), the household does not veto.

Add the computation to `code/generate-exhibits.R` (can be printed to console or included as a brief in-text number, no new exhibit needed).

### Step 3: Add Jones (2024) heterogeneity remark (paper)

In the discussion after Proposition 3 (Section 4.1), add 2–3 sentences connecting the veto result to Jones (2024)'s observation:
- Jones notes that wealthier households are more concerned about AI existential risk, while poorer households are more willing to accept risk for higher consumption.
- The model offers a complementary channel: under incomplete markets, households with more to lose from displacement (higher α) have stronger veto incentives—connecting wealth heterogeneity to attitudes about AI development through the financial channel, not just existential risk.

### Step 4: Review introduction flow (paper)

Read the introduction cold and verify:
- Each paragraph transitions naturally to the next.
- The GKP contribution framing is modest ("builds on," "inherits their central economic logic").
- The AI-authorship device appears in both abstract and introduction (currently in footnote—verify this is the right placement per spec).
- The lit review is under half a page and centered on top-journal papers.

### Step 5: Verify spec compliance

- Abstract ≤ 100 words: currently ~92 words ✓
- ≤ 20 pages: currently ~14 pages ✓
- ≤ 6 exhibits: currently 3 ✓
- All display equations numbered ✓
- All propositions proved ✓
- Code runs from scratch in < 180s ✓

No spec violations found. Focus on Steps 1–3 for substantive improvement.
