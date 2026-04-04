Title: Paper Settlement Study
Date: 2026-04-03
Time: 19:44 EDT

Brief note on when each `backup-ralph/*` branch appears to begin substantive paper work.

Method:
- For each branch, compute the merge-base with `main`.
- List the first four commits reachable from the branch but not from `main`.
- This keeps branch-initializer commits visible, since some branches begin with a blank-condition or setup commit.

`backup-ralph/run-0325`
- `76395086` `rloop [ref-cfr+factcheck]: Add title, full model, proposition, calibration table, and extension section; address displacement/incomplete-markets framing per CFR-R1`
- `a35228f8` `rloop [ref-cfr+factcheck]: Add AI valuation figure, sensitivity table, Proposition 2, and calibration detail`
- `f662bd34` `rloop [ref-cfr+factcheck]: Add AI capital owner justification paragraph, fix Proposition 2 proof, and add testable implications`
- `6fa11572` `rloop [ref-cfr+factcheck]: Add implied singularity beliefs, policy counterfactual, and welfare cost paragraphs`

`backup-ralph/run-0328`
- `c62f31b3` `set config for run`
- `480e281e` `rloop [test-manual-cleanup]: Add incomplete-markets hedging model with singularity shock and existential risk extension`
- `6a6b74ea` `rloop [test-manual-cleanup]: staged-diff summary commit with notation, `kappa`, theorem, and calibration-table changes`
- `ee2de53b` `rloop [test-manual-cleanup]: Fix sign error in Prop 1(iii), revert singularity state notation, and formalize abundance-resolution section`

`backup-ralph/run-0331`
- `fd13b3e7` `rloop start: record initial condition before author steps`
- `9045bc0b` `rloop [lots-of-tests-now]: Full paper draft with model, propositions, proofs, and Jones extension`
- `3ffc0239` `rloop [lots-of-tests-now]: Fix CRRA bound condition, integration variable, and Coase theorem exposition`
- `89a1d97b` `rloop [lots-of-tests-now]: Add Proposition 3 sufficient-condition tightening, Coase theorem proof, and grounding paragraphs; scaffold data-driven Figure 1 code`

`backup-ralph/run-0401`
- `403bf853` `rloop start: record initial condition before author steps`
- `fc07d4eb` `rloop [limit-paper-scope]: expand the paper from a placeholder skeleton to a full draft with titled sections, propositions, proofs, and extended bibliography`
- `8a9a4d73` `rloop [limit-paper-scope]: add first exhibit (AI vs market P/E figure) and strengthen bounded-utility argument in extension`
- `cb9a12f6` `rloop [limit-paper-scope]: sharpen partial-hedge framing, elevate heterogeneous risk-attitudes to a formal remark, and cite KorinekSuh2024`

Takeaway:
- `run-0325` starts directly with substantive paper commits.
- `run-0328` starts with a non-paper setup commit, then substantive drafting begins immediately after.
- `run-0331` and `run-0401` start with a recorded blank initial condition, then move into full-draft work on the next commit.

Follow-up conclusion: low-cost spec test
- Proposed strategy: run about five parallel trials, each with only `AuthorPlan` and `AuthorImprove`, with no extra fact-check, referee, or cleanup steps.
- Evaluation target: use those outputs to assess whether the paper spec is steering the draft in the right big-picture direction.
- Ignore for this experiment: proof bugs, fact-check misses, notation glitches, citation problems, calibration mistakes, LaTeX issues, and similar local defects.

Why this strategy makes sense
- The evidence from the early branch histories is that the paper's directional choices settle very quickly.
- In all four `backup-ralph/*` branches, the first substantive `paper.tex` commit already contains the core thesis: public AI stocks hedge a negative AI singularity because the representative household cannot access private AI capital.
- The next few commits usually do not replace that thesis. Instead they refine it by tightening proofs, changing notation, clarifying comparative statics, or elaborating the extension.
- This means the first plan-plus-improve cycle is likely to reveal the branch's conceptual direction even if the draft is still technically rough.

Evidence by branch
- `run-0325`: the first substantive commit already has the full introduction takeaway, the two-agent incomplete-markets setup, and the extension with existential risk and transfer/abundance logic. The next few commits add figure motivation, sensitivity analysis, implied-belief interpretation, policy discussion, and welfare exposition, but do not change the main idea.
- `run-0328`: after the setup commit, the first substantive commit already states the same hedge-through-incomplete-markets thesis. The next commits mostly clean up notation, proposition conditions, calibration details, and extension formalization. Again, the main direction is present immediately.
- `run-0331`: after the blank-condition commit, the first substantive draft already contains the core thesis and a full paper structure. The main branch-level difference is modeling style: it starts in continuous time with Poisson singularity shocks. The subsequent commits mostly repair or sharpen this framework rather than changing the paper's economic message.
- `run-0401`: after the blank-condition commit, the first substantive draft again contains the same base thesis. The meaningful early movement is in the extension: it starts with a looser claim that sufficiently large output can overcome frictions, then quickly tightens that into a bounded-utility condition under which endogenous completion may or may not occur. This is an extension-detail shift, not a base-thesis shift.

Implication for the spec test
- A five-way parallel run with only `AuthorPlan` and `AuthorImprove` should be enough to catch the failures we care about at this stage:
- whether the introduction lands on the intended thesis;
- whether the modeling style is simple and aligned with the spec, rather than drifting into an overbuilt or off-spec framework;
- whether the extension remains an extension instead of taking over the paper;
- whether the contribution relative to GKP stays modest and correctly framed.
- This setup is not appropriate for judging correctness or polish, but it is appropriate for testing whether the spec induces the right high-level paper.
