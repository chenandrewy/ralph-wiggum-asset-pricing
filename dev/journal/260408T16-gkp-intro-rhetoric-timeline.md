Title: GKP Intro Rhetoric Timeline
Date: 2026-04-08
Time: 16:09:47 EDT

This note records the commits that introduced or intensified the introduction's strange GKP-adjacent rhetoric about unborn/not-yet-existing capital.

Main finding:
- The seed appears in the first full-paper iteration.
- The stronger GKP-style "future counterparties do not yet exist" framing appears at iteration 6.
- The more awkward "cannot buy the capital that does not yet exist" wording appears at iteration 12.
- The current compressed version keeps that wording and adds the "deliberately a single-factor CCAPM" framing at iteration 26.

Commit timeline:

1. `d586301` (iteration 1)
- Headline: `rloop [ext-spec-refined-3]: Build full paper from placeholder text; 16 failing tests remain across theory, writing, and rhetoric`
- First full-paper version already contains the seed:
  - "firms and entrepreneurs who do not yet exist"
  - "startups that have not yet been founded"
  - "future AI entrepreneurs"
- At this point, the intro still describes incompleteness in relatively concrete terms rather than the later abstract "capital that does not yet exist" formulation.

2. `30cc343` (iteration 6)
- Headline: `rloop [ext-spec-refined-3]: Fix intro flow/rhetoric, transfers equation terminology, and figure distinguishability`
- First appearance of the stronger GKP-style counterparty rhetoric:
  - "the counterparties who would sell insurance against it---the future AI entrepreneurs and innovators---do not yet exist"
- This commit also rewrites the intro around GKP's intergenerational-risk-sharing friction more explicitly.
- This is the first commit where the intro starts to sound structurally closer to GKP than the paper's own reduced-form model warrants.

3. `09e7eac` (iteration 10)
- Headline: `rloop [ext-spec-refined-3]: Fix intro narrative momentum, Extensions preamble density, and transfers figure font sizes`
- Important checkpoint: the intro still does not yet contain the worst formulation.
- It has:
  - "The counterparties ... do not yet exist"
  - "startups not yet founded"
- But it does not yet say:
  - "the household cannot buy the capital that does not yet exist"

4. `5bff670` (iteration 12)
- Headline: `rloop [ext-spec-refined-3]: Fix abstract rhetoric, Extension 2 economic framing, and intro flow`
- First appearance of the most awkward abstract formulation:
  - "That scale difference exposes the incompleteness---the household cannot buy the capital that does not yet exist."
- This is the clearest commit where the rhetoric outruns the actual paper model.

5. `f395cab` (iteration 15)
- Headline: `rloop [ext-spec-refined-3]: Restructure Extension 2 so transfers target only private AI capital, removing the public-dividend tax equation and leading with the valuation-compression punchline`
- The problematic framing is fully stacked by this point:
  - future counterparties do not yet exist
  - startups not yet founded
  - capital that does not yet exist
- Also keeps the Extension 2 line:
  - "the relevant AI capital simply does not yet exist"

6. `aaab9a7` and `be467a1` (iterations 20 and 25)
- `aaab9a7` headline: `rloop [ext-spec-refined-3]: Fix $\tilde{\eta}_C$ notation, tighten Extensions section opening, remove SDF equations from Pricing paragraph, and increase transfers figure font sizes and canvas`
- `be467a1` headline: `rloop [ext-spec-refined-3]: Tighten prose in Results, Extensions, and Conclusion; darken transfers-figure break-even line`
- The same framing persists with only prose tightening.
- No fundamental correction occurs; the rhetoric is now part of the introduction's stable structure.

7. `0d6f8c3` (iteration 26)
- Headline: `rloop [ext-spec-refined-3]: Add veto-threshold table and restructure model, extensions, and intro sections`
- Keeps the "capital that does not yet exist" line.
- Compresses the surrounding paragraph.
- Adds:
  - "Our model is deliberately a single-factor CCAPM..."
- This commit does not introduce the unborn-capital rhetoric, but it reinforces the final form of the intro by combining that rhetoric with explicit referee-facing contribution framing.

8. `dae9b8e` (iteration 28)
- Headline: `rloop [ext-spec-refined-3]: Restructure Extensions intro and Extension 1 setup to lead with economic questions; condense "maintained conditions" blocks; move Lambda definition before equation; tighten prose throughout`
- Revises the single-factor CCAPM sentence into the current wording:
  - separates "GKP already established that displacement risk is a second priced factor"
  - then states "Our model is deliberately a single-factor CCAPM..."
- Does not fix the underlying unborn-capital mismatch.

9. `651484b` (iteration 30 / current)
- Headline: `rloop [ext-spec-refined-3]: Tighten assumption-block prose, reorder transfers setup, and narrow Panel A x-axis to τ ≤ 0.03`
- Current intro still contains:
  - "firms and entrepreneurs who do not yet exist"
  - "future AI entrepreneurs and innovators"
  - "the household cannot buy the capital that does not yet exist"
  - "the relevant AI capital simply does not yet exist"

Interpretation:
- If the question is "when did the strange problem begin?", the answer depends on severity:
  - earliest seed: `d586301`
  - first strong GKP-style counterparty rhetoric: `30cc343`
  - first clearly mismatched abstract "capital that does not yet exist" wording: `5bff670`
- Iteration 10 (`09e7eac`) is a sensible remembered checkpoint because the intro had drifted, but had not yet reached the worst "capital that does not yet exist" wording.
