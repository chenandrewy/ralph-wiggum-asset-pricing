# Theory Scope and Test Findings

Date: 2026-04-02
Time: 09:05:26 EDT

Summary:

The paper spec makes theory scope intentionally narrow. The key items are I.1, I.5.d, I.6.d, and especially IV.8 and IV.8.a-d in `spec/paper-spec.md`. The paper is supposed to be an academic asset pricing theory paper with tightly limited empirical content, intentionally limited to a compact theoretical contribution, with minimal formalism, very limited empirical material, no broad menu of new predictions, and only illustrative quantitative material.

Tests:

The main test that directly enforces this is `tests/quality-formalism.py`. A `main` commit immediately before this run, `20005fd`, explicitly says it expanded `quality-formalism` to enforce the full spec IV.8. The current config also selects `quality-formalism`. Other tests touch nearby issues indirectly, but they are not the primary scope test. In particular, `tests/spec-paper.py` explicitly keeps the Quality Requirements section out of scope, so it is not the relevant enforcement mechanism here.

Does the test work on the current draft?

Only partially. The current paper passes `quality-formalism`, but the pass is too lenient relative to the spec's compact-theory standard. The test is reasonably good at catching theorem bloat and excessive empirical or quantitative expansion. But it is weak on prose-level scope drift. The strongest borderline section is the two-factor pricing subsection, which adds extra formal machinery beyond the core comparative statics. The test currently rationalizes that section as doing distinct work rather than treating it as potentially compressible.

What is in scope versus out of scope:

The extinction-risk extension and the Coase / infinite-output transfer extension are in scope. They are required by `spec/paper-spec.md` section I.5 and reinforced by I.6.c. They should not be treated as scope creep. By contrast, the extra verbal add-ons around them, especially the wealth-heterogeneity and mortality-reduction discussion, look more like expansion pressure than minimal compliance with the spec.

Role of `referee-cfr-r1`:

The CFR R1 report pushes in the direction of adding richer singularity features and differentiating from GKP by doing more. The current referee output praises the draft for adding wealth heterogeneity and mortality reduction and suggests formalizing the heterogeneity discussion further rather than cutting it. This looks misaligned with IV.8's compact-theory mandate.

The two-factor pricing section also appears to be referee-driven. The original CFR R1 report criticized the earlier draft for collapsing to a one-factor CCAPM and contrasted that with GKP's two-factor structure. The current paper responds in the same language, and the current referee output explicitly praises the draft for preserving a two-factor pricing structure. The two-factor section is not explicitly required by the spec and is best understood as a response to the referee pressure about subsumption by GKP.

Bottom line:

If the goal is to improve the algorithm, the highest-value change is probably to remove or heavily constrain `tests/referee-cfr-r1.py` from the active loop. `quality-formalism` could still be improved, but `referee-cfr-r1` appears to be actively encouraging additions that make it harder to maintain the intended narrow theory scope.
