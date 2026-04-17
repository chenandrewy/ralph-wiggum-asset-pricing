# Ralph Loop Limitations

Date: 2026-04-16
Time: 20:17 EDT

This note documents several cases where the Ralph loop appeared to overreact to localized test failures or implementation issues, producing visible paper artifacts that were disproportionate to the underlying problem.

## 1. Strange abstract line

The abstract line "The displacement the paper models is closer than it appears" was introduced in `59c098cf95448127fef5e8c61c1f1da19f224eb7` on 2026-04-12 09:55:59 EDT (`rloop-28`).

This was almost certainly a reaction to `element-rhetoric-meta`. In `rloop-27` (`853b90510442a839783b1bcf8b6fd122131586ad`), the remaining failures explicitly included `element-rhetoric-meta (abstract placement still flagged)`. The previous abstract sentence had been much more explicit:

`This paper demonstrates the displacement it models: AI agents produced all analysis and writing from a human-authored specification.`

The saved test report after `rloop-28` passed and praised the replacement sentence as a subtler "cryptic closing hook."

The loop behavior here looks like test overfitting. A rhetorical test disliked the explicit sentence, and the loop replaced it with a line that is vague, stylized, and somewhat disconnected from the rest of the abstract.

## 2. Strange Figure 1 choices

The history shows that Ralph-run at one point actively pursued a CRSP-based opening figure. Earlier commits and code show a WRDS/CRSP pipeline for the opening figure, including:

- `89a1d97b3c7c4a790823b9880a1c07b3c3f638be` on 2026-03-30 (`rloop [lots-of-tests-now]`): scaffolded data-driven Figure 1 code.
- `884f1ec11743c30a18980da7f1559b043242bbd4` on 2026-03-30: added split-adjusted CRSP dividend P/D ratio.
- `d5c5bb25cbe05c43322e1339fa51a2a003d390bd` on 2026-04-02: still reported `factcheck-code (CRSP dividend/shares split-adjustment consistency)`.

My reading is that the later Figure 1 choices were an overreaction to share-adjustment problems. The loop seems to have encountered reproducibility and split-adjustment trouble in the CRSP-based opening figure, then moved toward less direct and less conceptually clean substitutes rather than resolving the narrower empirical-data issue cleanly.

This is a limitation worth documenting because the loop did not just struggle with code correctness. It also struggled to maintain a stable empirical design once technical data issues appeared.

## 3. Strange remark

Remark 1, "Existence condition," was introduced in `42ce3a298a6c9e9ec144949346034b8af9055646` on 2026-04-09 19:42:23 EDT (`rloop-04`).

The immediate preceding commit, `3b369029a115df6ac8cadb918510cd21f06bc96b` (`rloop-03`), listed this remaining failure:

- `factcheck-theory: Proposition 1 P/D formula requires an existence condition (denominator > 0) that the paper's own large-singularity calibration may violate; condition not yet stated in the proposition.`

The improvement plan at `AUTHOR PLAN — 2026-04-09 19:15:07 EDT` described the issue as:

- "Critical Issue: Extension 2 Calibration Breaks P/D Formula"

It noted that the P/D formula had the form $A/(1-A)$ and required $A < 1$, but the paper never stated this, while the large-singularity calibration in Extension 2 violated it (`A = 2.37` for AI stocks). The code returned `NA`, the figure omitted undefined regions, and the paper did not explain why P/D was undefined at $\tau = 0$.

The response appears excessive. The underlying issue was real, but it was local: a technical restriction became binding for one calibration. That does not obviously require a numbered main-text remark. A more proportionate repair would have been:

- change the calibration,
- explain the restriction locally in the figure discussion or caption,
- or move the condition into a proof, appendix remark, or footnote.

Instead, the loop elevated the issue into a conspicuous main-text remark. This looks like another case where the loop optimized for explicit test satisfaction rather than rhetorical proportionality in the paper.

This later seems to have been embellished into a supposed differentiator from GKP. The paper eventually says that the discrete singularity has an existence-condition issue with "no analog" in GKP's continuous-displacement framework, and treats the finite-to-infinite pricing discontinuity as part of what distinguishes the paper.

That differentiation is silly. The relevant point is just that one particular closed-form expression under one severe calibration can fail to deliver finite prices. That is a technical feature of the chosen setup and parameterization, not a meaningful contribution-level distinction from GKP. Elevating it into a conceptual differentiator is another example of the loop turning a local repair into inflated paper rhetoric.

## 4. Faulty referee-response insertion

Later in the paper, the text says:

`This connects wealth heterogeneity to attitudes about AI development through the displacement channel, not just through differential valuations of life.`

The phrase appears without prior discussion in the paper of the value of life or "differential valuations of life." The phrase was first introduced in `fefd0b77994c70449afef61f8328b886f6a2d466` on 2026-04-10 22:24:42 EDT (`rloop-15`).

The motivation does not appear to have come from a failing test. Instead, the `AUTHOR PLAN — 2026-04-10 22:03:35 EDT` states:

- `Referee suggestion on Jones (2024) heterogeneity.`
- "The referee specifically asked the paper to engage with Jones (2024)'s observation that rich and poor households hold heterogeneous views about AI risk."

The plan then proposes adding a Jones (2024) heterogeneity remark to the veto discussion, connecting displacement exposure to wealth heterogeneity and presenting this as a way to respond to the referee and differentiate the paper from GKP.

This looks like a faulty author-agent response to reading `spec/CFR-R1-report.md`. Instead of integrating the referee point carefully and with the proper setup, the loop inserted a dangling phrase borrowed from the Jones framing. The result is under-motivated and rhetorically sloppy: it gestures toward a "value of life" discussion that the paper has not actually developed. This is another example of the loop satisfying a perceived referee demand locally, without checking whether the resulting sentence is properly introduced or supported in the paper's own argument.
