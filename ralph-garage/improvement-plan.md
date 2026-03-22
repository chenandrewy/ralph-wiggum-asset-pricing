# Improvement Plan

## Current State

All tests pass. The referee report (referee-top3) identifies two issues:

1. **The event-study table is weak and should be dropped.** Table 4 uses only six hand-picked events with no statistical tests, no controls, and no formal identification. The Biden Executive Order goes the wrong way. The referee says it undermines credibility and wastes an exhibit slot.

2. **The $\alpha$ parameter needs concrete empirical grounding.** The paper claims broadening market access is a policy lever but never quantifies what $\alpha$ is today, how it has changed, or what specific policies move it. The GKP distinction remains purely theoretical without this.

The CFR-R1 referee report is already addressed (Jones extension, GKP distinction, incomplete markets). No overhaul needed—the model section is clean and all theory tests pass.

## Plan

### 1. Drop the event-study table and discussion

- Remove Table 4 (`\input{table-event-study.tex}`) and the "Suggestive Event-Study Evidence" subsubsection entirely.
- This frees one exhibit slot (back to 5/6) and ~0.5 pages.
- The testable implications in Section 3.4 (two identifying predictions) stand on their own without informal evidence.
- Keep the "Testable Implications" subsection header and the two prediction paragraphs; just remove the event-study material after them.

### 2. Add a concrete discussion of $\alpha$ in practice

Use the freed space to add a short subsubsection (or extend existing prose) in Section 3.3 (Sensitivity and Partial Market Access) that:

- **Quantifies current $\alpha$**: Public AI market cap is ~$5T; total AI-sector value including private firms (OpenAI, Anthropic, xAI, etc.) is ~$7-8T. So $\alpha \approx 0.60$--$0.70$ today, meaning the household already has substantial but incomplete access.
- **Notes the trend**: $\alpha$ has been rising as AI startups IPO or are acquired by public firms (e.g., Google/DeepMind). The trend is plausibly upward.
- **Connects to specific policies**: Expanding accredited-investor rules, creating AI-sector index funds with private-capital exposure, and regulatory reform around secondary-market trading of pre-IPO shares. These are the concrete levers that move $\alpha$.
- **Strengthens the GKP distinction**: GKP's friction is intergenerational and structurally irreducible; ours is observable ($\alpha$ ≈ public/total AI market cap) and policy-responsive. This is now backed by data, not just theory.

### 3. Tighten the testable implications section

With the event study removed, sharpen the two remaining predictions:
- Prediction 1 (singularity-risk shocks move AI valuations conditional on earnings): note this is testable with future high-frequency event data as the regulatory landscape evolves.
- Prediction 2 (hedging premium erodes as $s_t$ rises): note this is a long-run cross-sectional prediction testable with time-series data on AI market share.

Keep this concise—no more than the current length minus the removed event-study text.

### 4. Update conclusion

- Remove the sentence referencing Table 4 / event-study evidence.
- Add a brief mention of the observable $\alpha$ trajectory and policy implications in the concluding paragraph about financial inclusion.
