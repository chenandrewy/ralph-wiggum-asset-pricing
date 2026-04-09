# ralph-wiggum-asset-pricing

This project writes an academic asset pricing theory paper using Geoffrey Huntley's Ralph Wiggum (a.k.a. ralph) loop applied to a standard research project structure.

The ralph loop has agents continuously improve the repo based on the spec, tests, and referees.

## Repository wiring

- `AGENTS.md` is a symlink to `CLAUDE.md` (`AGENTS.md -> CLAUDE.md`).
- Keep agent instructions in `CLAUDE.md`; `AGENTS.md` reflects the same content via the symlink.

## Repo Structure

### Research Project

These are the paper and its supporting materials.

- `paper/` — canonical LaTeX source for the referee-ready paper (`paper.tex`, references, and only exhibits used by that paper)
- `code/` — R scripts and analysis code (if needed)
- `data/` — datasets (if needed)
- `spec/lit/` — literature for reference
- `dev/` — scratch work, journals, experiments

### Specification

`spec/` contains the source-of-truth specifications for the project, including the paper requirements, economic background, referee reports, Ralph loop behavior, and test framework.

### Tests

Test and referee definitions that evaluate the paper.

- `tests/` — PASS/FAIL test scripts (no prefix) and open-ended referee scripts (`referee-` prefix)
- `test-results/` — latest test and referee outputs

### Ralph (Permanent)

Infrastructure that drives the improvement loop.

- `ralph/` — loop script, agent wrapper, prompts, init script

### Ralph Garage (Transient)

Working artifacts generated during a Ralph run.

- `ralph-garage/improvement-plan.md` — the current iteration's plan
- `ralph-garage/page-images/` — uncommitted page renders of the current compiled paper, shared across tests
- `ralph-garage/history/` — iteration history (PDFs, plan/test compilations)
- `ralph-garage/loop.log` — console output from the ralph loop

### Dev Logs

Non-canonical debugging output.

- `ralph-garage/agent-logs/` — logs from agent invocations

## Build Helpers

- `bash ralph/build-paper.sh` builds the canonical paper.
- `bash check-ralph-direction.sh` generates candidate startup baselines under `ralph-garage/check-direction/`.

## Ralph Loop

The Ralph workflow is specified in `spec/ralph-spec.md`.

Fresh start from `main`:

1. Set `startup-source` in `config-ralph.yaml` to either `ralph/research-template` or a selected `ralph-garage/check-direction/run-*` candidate.
2. Commit `config-ralph.yaml`.
3. Run `bash go-ralph-go.sh` or `bash ralph/ralph-loop.sh`.

On a fresh start from `main`, Ralph clears live `paper/` and `code/`, installs them from `startup-source`, and then creates the startup commit on `ralph/run`.

Resume an existing stretch:

- Run Ralph from `ralph/run`. Resumes do not re-install from `startup-source`.

## `.devcontainer/` folder

Files are brought over from https://github.com/anthropics/claude-code.
