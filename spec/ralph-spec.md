# Ralph Loop Specification

## Purpose

Define the Ralph loop contract for improving the paper and recording current test evidence on a dedicated Ralph branch.

## Structure

- The main control flow lives in `ralph/ralph-loop.sh`.
- The bash loop should stay minimal and explicit.
- Config loading and validation is handled by `ralph/load-config.py`.
- Python scripts handle the individual work steps:
  - `ralph/load-config.py`
  - `ralph/author-plan.py`
  - `ralph/author-improve.py`
  - `ralph/run-tests.py`
  - `ralph/run-reviews.py`
  - `ralph/commit-iteration.py`

## Inputs And Configuration

- Core project state lives in `paper/`.
- Loop intent lives in `spec/`, with `spec/paper-spec.md` used by the current author prompts.
- Test definitions live in `tests/`.
- All prompts live inline in their respective scripts (e.g. `ralph/author-plan.py`, `ralph/author-improve.py`, `ralph/commit-iteration.py`).
- Runtime configuration lives in `config-ralph.yaml`.
- `config-ralph.yaml` is re-read at the start of each iteration so that the human can adjust settings (e.g. `max-iter`) mid-run without restarting.
- Referee definitions live in `tests/` with `referee-` prefix.
- `config-ralph.yaml` may optionally enable referee reviews with `reviews`.
- `config-ralph.yaml` may optionally enable continual-improvement mode with `continual-improvement`; this requires `reviews: true`.
- `config-ralph.yaml` may optionally enable a baseline pre-loop test run with `test-before-loop`.
- `config-ralph.yaml` may optionally specify a `run-name` that labels the current run for traceability in commit subjects and logs.

## Test Artifact Preparation

- Test artifact preparation consists of:
  - compiling `paper/paper.tex` into `paper/paper.pdf`
  - rendering `paper/paper.pdf` into `ralph-garage/page-images/page-*.png`
  - building `ralph-garage/page-images/exhibit-manifest.json`
- LaTeX compilation of `paper/paper.tex` is a deterministic build gate that runs before page-image generation and before the test phase.
- If the LaTeX build gate fails for an iteration, Ralph records that iteration as failed, skips page-image generation, skips the test phase, skips the review phase, and continues to the next iteration instead of terminating the whole loop.

## Branch Model

- `main` is the integration branch, and `ralph/run` is Ralph's working branch.
- `ralph/run` is a reusable working branch label, not a one-time unique run identifier.
- Manual config, spec, or tooling changes may be committed directly on `main` between Ralph stretches.
- Ralph work should be merged back into `main` with a non-fast-forward merge so each Ralph stretch remains visible in git history.
- When Ralph is started from `main`, it treats that startup as a fresh Ralph stretch and wipes old files from `ralph-garage/agent-logs/` before any pre-loop test or review phase begins.
- When Ralph is started from `ralph/run`, it treats that startup as a continuation and does not wipe the full agent log directory at startup.

## Manual Intervention Model

- The human may stop Ralph at any time.
- The human may manually edit `spec/`, `tests/`, `ralph/`, or other repo files between or during Ralph runs.
- Ralph does not require a clean working tree before starting or resuming.

## Iteration Workspace

- Ralph writes canonical run artifacts under `ralph-garage/`.
- The active plan file is `ralph-garage/improvement-plan.md`.
- Shared page images for the current compiled paper live in `ralph-garage/page-images/`.
- The exhibit-page manifest for the current compiled paper lives at `ralph-garage/page-images/exhibit-manifest.json`.
- Test and referee outputs live in `test-results/`.
- Ralph writes non-canonical debug logs under `ralph-garage/agent-logs/`.

## Iteration Lifecycle

If `test-before-loop` is enabled, Ralph first runs the LaTeX build gate. If that baseline build succeeds, Ralph prepares the remaining test artifacts and then runs `ralph/run-tests.py` once before iteration 1 to establish the current baseline. If `reviews` is also enabled, Ralph runs the selected reviews once after the baseline test run completes. If the baseline LaTeX build fails, Ralph skips the baseline test and review phase and proceeds to iteration 1.

For each iteration from `1` through `max-iter`:

1. Run `ralph/author-plan.py`.
2. Require the planning phase to create `ralph-garage/improvement-plan.md`.
3. Run `ralph/author-improve.py`.
4. Run the LaTeX build gate for `paper/paper.tex`.
5. If the LaTeX build gate fails, record the iteration as failed, skip page-image generation, skip tests and referees, create the iteration commit, and continue according to the normal exit rules.
6. If the LaTeX build gate succeeds, prepare the remaining test artifacts.
7. Run `ralph/run-tests.py`.
8. If reviews are enabled, run `ralph/run-reviews.py` after the test phase completes.
9. Create one git commit for the iteration with `ralph/commit-iteration.py`.
10. If continual-improvement is disabled, exit successfully as soon as the test phase returns success.
11. If continual-improvement is enabled, continue to the next iteration regardless of test results.

## Commit Model

- Ralph creates one commit per iteration.
- The commit step uses `--allow-empty`.
- Commits created by the Ralph loop must start with `rloop` (e.g., `rloop [run-name]: ...`).
- Ralph commit subjects should headline the substantive paper change.
- Ralph commit bodies should describe the failing tests the iteration attempted to fix.

- The commit step stages only:
  - `paper/`
  - `ralph-garage/improvement-plan.md`
  - `test-results/`
- Shared page images under `ralph-garage/page-images/` are transient inputs to tests and are not committed.
- Specs, tests, prompts, Ralph tooling, and `ralph-garage/agent-logs/` are not included in Ralph iteration commits.

## Exit Conditions

- When continual-improvement is disabled (default): exit `0` immediately after the first iteration whose selected tests all pass.
- When continual-improvement is enabled: exit `0` after completing `max-iter` iterations.
- Exit `1` if an author step fails, planning does not produce `ralph-garage/improvement-plan.md`, the commit step fails, or (when continual-improvement is disabled) the iteration limit is reached without a passing test run.
