# Ralph Loop Specification

## Purpose

Define the Ralph loop contract for improving the paper and recording current test evidence on a dedicated Ralph branch.

This contract also defines an optional manual direction-selection stage that may run before a Ralph stretch begins.

## Structure

- The human-facing entry points are lightweight shell scripts at the repo root.
- `go-ralph-go.sh` runs the main Ralph loop by calling `ralph/ralph-loop.sh`.
- A separate direction-selection entry point may run before `go-ralph-go.sh` and does not itself start the Ralph loop.
- The main control flow lives in `ralph/ralph-loop.sh`.
- The bash loop should stay minimal and explicit.
- Config loading and validation is handled by `ralph/load-config.py`.
- Python scripts handle the individual work steps:
  - `ralph/load-config.py`
  - `ralph/author-plan.py`
  - `ralph/author-improve.py`
  - `ralph/author-fix-build.py`
  - `ralph/run-tests.py`
  - `ralph/run-referees.py`
  - `ralph/commit-iteration.py`
- Direction-selection tooling may also use:
  - `ralph/check-direction.py`

## Author Working Directories

The author steps (`author-plan.py`, `author-improve.py`) may modify files in these directories:

- `paper/` — LaTeX source
- `code/` — R scripts and analysis
- `data/` — datasets (not committed; working directory only)

## Inputs And Configuration

- Core project state lives in the author working directories.
- Loop intent lives in `spec/`, with `spec/paper-spec.md` used by the current author prompts.
- When the spec or tests name a literature file as authoritative context, that named file is the Ralph loop's canonical source for that paper; for GKP, the canonical source is `spec/lit/GKP-2012.md`.
- Test definitions live in `tests/`.
- All prompts live inline in their respective scripts (e.g. `ralph/author-plan.py`, `ralph/author-improve.py`, `ralph/commit-iteration.py`).
- Agent invocation settings such as agent choice, model choice, and effort level belong in the calling script, alongside constants such as `AGENT` and `MODEL`.
- `ralph/agent_wrapper.py` may translate those script-level settings into provider-specific CLI arguments, but per-step agent behavior should not be introduced through new repo-wide config keys or environment variables unless the behavior is truly loop-wide.
- Runtime configuration lives in `config-ralph.yaml`.
- `config-ralph.yaml` is re-read at the start of each iteration so that the human can adjust settings (e.g. `max-iter`) mid-run without restarting.
- `max-iter` is the maximum total number of Ralph iteration commits for the current `ralph/run` stretch, counted since the most recent Ralph startup commit on the branch.
- Human edits to `config-ralph.yaml` are allowed at any time during a Ralph run.
- Referee definitions live in `tests/` with `referee-` prefix.
- `config-ralph.yaml` may optionally enable referees with `referees`.
- `config-ralph.yaml` may optionally enable continual-improvement mode with `continual-improvement`; this requires `referees: true`.
- `config-ralph.yaml` may optionally enable a baseline pre-loop test run with `test-before-loop`.
- `config-ralph.yaml` may optionally specify a `run-note` for internal traceability in loop logs and config history.
- `config-ralph.yaml` may optionally enable a Claude quota preflight with `quota-preflight` and may set its stop threshold with `claude-5h-utilization-limit`.
- `config-ralph.yaml` also defines the startup-only setting `startup-source`, which is read when Ralph is started from `main` to begin a fresh stretch.

## Initialization

- Initialization is only relevant when Ralph is started from `main` to begin a fresh Ralph stretch.
- A fresh Ralph stretch from `main` begins with an explicit initialization choice before `go-ralph-go.sh` is run.
- Initialization is controlled by `config-ralph.yaml`.
- `config-ralph.yaml` selects the startup baseline through a `startup-source` setting.
- `startup-source` must be a repo-relative path.
- There are exactly two approved `startup-source` values for a fresh Ralph stretch from `main`:
  - `ralph/research-template`
  - a candidate directory under `ralph-garage/check-direction/run-*`
- On `main`, live `paper/` and `code/` must not already be present before a fresh Ralph stretch begins.
- Fresh starts from `main` must not rely on live `paper/` and `code/` as authoritative author state; Ralph initializes those directories from `startup-source`.
- On a fresh Ralph stretch from `main`, Ralph auto-installs live `paper/` and `code/` from the configured `startup-source` before creating the startup commit.
- Live `paper/` and `code/` are the author working directories that hold the installed startup baseline.
- Live `paper/` and `code/` are not an independent third startup source for a fresh Ralph stretch from `main`.
- Ralph must not create the startup commit for a fresh Ralph stretch from `main` unless `startup-source` is explicit, valid, and unambiguous.

### Template Initialization

- Template initialization uses `startup-source: ralph/research-template`.
- `ralph/research-template/` contains both `paper/` and `code/` as the canonical blank-slate startup baseline.
- `ralph/wipe.sh` is a separate cleanup utility and is not part of the authoritative initialization contract.

### Candidate Generation Via Check-Direction

- Ralph may optionally begin with a manual check-direction stage before `go-ralph-go.sh` is run.
- The purpose of this stage is to sample several plausible initial drafts from the current spec before the main loop starts improving one chosen draft.
- This stage is not itself the initialization choice.
- This stage is outside the Ralph iteration lifecycle and outside the Ralph commit count.
- The human-facing entry point for this stage is `bash check-ralph-direction.sh`.
- The check-direction stage may run several isolated preliminary author runs in parallel from the current git state.
- Each preliminary run executes:
  1. `ralph/author-plan.py`
  2. `ralph/author-improve.py`
- Each preliminary run writes its candidate outputs under `ralph-garage/check-direction/`.
- The canonical unit of selection is the full author working state produced by a preliminary run:
  - `paper/`
  - `code/`
- After preliminary runs finish, the human chooses one candidate.
- The chosen candidate is selected by setting `startup-source` in `config-ralph.yaml` to the candidate's repo-relative directory, such as `ralph-garage/check-direction/run-01`.
- The check-direction stage does not create `rloop-*` commits.
- Preliminary outputs under `ralph-garage/check-direction/` are transient artifacts, not canonical source files.

## Test Artifact Preparation

- Test artifact preparation consists of:
  - compiling `paper/paper.tex` into `paper/paper.pdf`
  - rendering `paper/paper.pdf` into `ralph-garage/page-images/page-*.png`
  - building `ralph-garage/page-images/exhibit-manifest.json`
- LaTeX compilation of `paper/paper.tex` is a deterministic build gate that runs before page-image generation and before the test phase.
- If the LaTeX build gate fails for an iteration, Ralph runs a focused build-fix step (`ralph/author-fix-build.py`) and retries the build once. If the retry also fails, Ralph records that iteration as failed, skips page-image generation, skips the test phase, skips the referee phase, and continues to the next iteration instead of terminating the whole loop.

## Branch Model

- `main` is the integration branch, and `ralph/run` is Ralph's working branch.
- `ralph/run` is a reusable working branch label, not a one-time unique run identifier.
- Manual config, spec, or tooling changes may be committed directly on `main` between Ralph stretches.
- Ralph work should be merged back into `main` with a non-fast-forward merge so each Ralph stretch remains visible in git history.
- Initialization runs before Ralph branch setup for a new stretch from `main` and does not itself require switching to `ralph/run`.
- When Ralph is started from `main`, it treats that startup as a fresh Ralph stretch and wipes old files from `ralph-garage/agent-logs/` before any pre-loop test or referee phase begins.
- When Ralph is started from `ralph/run`, it treats that startup as a continuation and does not wipe the full agent log directory at startup.
- On a fresh Ralph stretch from `main`, setup validation must validate `startup-source` before the startup commit is created.
- On a fresh Ralph stretch from `main`, Ralph reads `startup-source` from `config-ralph.yaml`, installs `paper/` and `code/` from that source, and only then creates the startup commit on `ralph/run`.
- On a fresh Ralph stretch from `main`, Ralph must not silently treat the current live working tree as an independent startup baseline outside the approved initialization paths.
- On a fresh Ralph stretch from `main`, Ralph must stop before the startup commit if `startup-source` is missing, invalid, or inconsistent with the required source structure.

## Manual Intervention Model

- The human may stop Ralph at any time.
- The human may edit `config-ralph.yaml` at any time, including during an active step; Ralph should not treat that as an author-step failure.
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

If `test-before-loop` is enabled, Ralph first runs the LaTeX build gate. If that baseline build succeeds, Ralph prepares the remaining test artifacts and then runs `ralph/run-tests.py` once before iteration 1 to establish the current baseline. If `referees` is also enabled, Ralph runs the selected referees once after the baseline test run completes. If the baseline LaTeX build fails, Ralph skips the baseline test and referee phase and proceeds to iteration 1.

If `quota-preflight` is enabled, Ralph runs a lightweight active Claude quota probe immediately before each batch test phase. If the probe observes five-hour utilization at or above `claude-5h-utilization-limit`, Ralph stops the loop cleanly before launching the test batch.

Let the current Ralph stretch begin at the most recent startup commit on `ralph/run`. For each iteration from the next unfinished iteration through `max-iter` for that stretch:

1. Run `ralph/author-plan.py`.
2. Require the planning phase to create `ralph-garage/improvement-plan.md`.
3. Run `ralph/author-improve.py`.
4. Run the LaTeX build gate for `paper/paper.tex`.
5. If the LaTeX build gate fails, run `ralph/author-fix-build.py` to attempt a focused build recovery, then re-run the LaTeX build gate.
6. If the build gate still fails after the fix attempt, record the iteration as failed, skip page-image generation, skip tests and referees, create the iteration commit, and continue according to the normal exit rules.
7. If the LaTeX build gate succeeds (on the first try or after the fix attempt), prepare the remaining test artifacts.
8. If enabled, run the Claude quota preflight for the test phase.
9. Run `ralph/run-tests.py`.
10. If referees are enabled, run `ralph/run-referees.py` after the test phase completes.
11. Create one git commit for the iteration with `ralph/commit-iteration.py`.
12. If continual-improvement is disabled, exit successfully as soon as the test phase returns success.
13. If continual-improvement is enabled, continue to the next iteration regardless of test results.

## Commit Model

- Ralph creates one commit per iteration.
- Ralph may also create one startup commit per fresh Ralph stretch before iteration 1 to record the initial condition on `ralph/run`.
- The commit step uses `--allow-empty`.
- Commits created by the Ralph loop must start with `rloop-` plus the zero-padded iteration number (e.g., `rloop-01: ...`).
- Ralph commit subjects should headline the substantive paper change.
- Ralph commit bodies should describe the failing tests the iteration attempted to fix.

- The commit step stages all author working directories except `data/`, plus `ralph-garage/improvement-plan.md` and `test-results/`.
- `data/` is a working directory but is not committed (too large for git).
- Shared page images under `ralph-garage/page-images/` are transient inputs to tests and are not committed.
- The startup commit stages only `paper/` and `code/`.
- Specs, tests, prompts, Ralph tooling, and `ralph-garage/agent-logs/` are not included in Ralph iteration commits.

## Wipe

- Wiping gives Ralph a blank slate: empty author working directories, empty `test-results/`, and no `ralph-garage/`.
- `ralph/wipe.sh` performs a wipe.
- Wiping is a manual cleanup operation and does not itself determine the startup baseline for a fresh Ralph stretch from `main`.

## Exit Conditions

- When continual-improvement is disabled (default): exit `0` immediately after the first iteration whose selected tests all pass.
- When continual-improvement is enabled: exit `0` after the current Ralph stretch reaches `max-iter` total iterations.
- Exit `0` early if the active Claude quota preflight stops the loop before a batch test phase due to low observed headroom.
- Exit `1` if an author step fails, planning does not produce `ralph-garage/improvement-plan.md`, the commit step fails, or (when continual-improvement is disabled) the iteration limit is reached without a passing test run.
