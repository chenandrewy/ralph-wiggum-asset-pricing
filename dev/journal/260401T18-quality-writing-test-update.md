# Potential tightening of quality-writing test Requirement 5

Date: 2026-04-01 6:00 PM ET

## Context

Added Requirement 5 to `tests/quality-writing.py` to enforce the spec IV.5 umbrella clause ("compelling and conversational, yet rigorous") as a pass/fail gate across the full paper body, not just the abstract and introduction.

## Potential update

Requirement 5 is more subjective than the other requirements. It says what should fail but does not force the evaluator to cite concrete passages from the body the way Requirement 3 does for plain-English violations. This makes enforcement less crisp.

If Requirement 5 proves too lenient in practice (i.e., it passes papers that should fail because the evaluator hand-waves), tighten it by adding a guideline that requires the evaluator to quote specific passages — similar to the guideline for Requirement 3 at `tests/quality-writing.py:85`.

## Decision

Wait to see how the test performs before tightening. No action unless we see a concrete failure mode.
