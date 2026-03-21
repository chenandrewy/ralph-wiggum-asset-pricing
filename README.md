# ralph-wiggum-asset-pricing

This project writes an academic asset pricing theory paper using Geoffrey Huntley's Ralph Wiggum (a.k.a. ralph) loop applied to a standard research project structure.

The ralph loop has agents continuously improve the repo based on the spec and tests.

## Repository wiring

- `AGENTS.md` is a symlink to `CLAUDE.md` (`AGENTS.md -> CLAUDE.md`).
- Keep agent instructions in `CLAUDE.md`; `AGENTS.md` reflects the same content via the symlink.

## Repo Structure

### Research Project

These are the paper and its supporting materials.

- `paper/` — canonical LaTeX source for the reviewable paper (`paper.tex`, references, and only exhibits used by that paper)
- `code/` — R scripts and analysis code (if needed)
- `data/` — datasets (if needed)
- `spec/lit/` — literature for reference
- `dev/` — scratch work, journals, experiments

### Specification

These files are the source of truth for the repo's intent.
- `spec/paper-spec.md` — the paper specification
- `spec/asset-pricing-background.md` — asset pricing conventions
- `spec/CFR-R1-report.md` — the CFR referee report to address
- `spec/ralph-spec.md` — the Ralph loop specification
- `spec/test-spec.md` — the test framework specification

### Tests

Test and referee definitions that evaluate the paper.

- `tests/` — test scripts (no prefix) and referee scripts (`referee-` prefix)
- `test-results/` — test and referee outputs from the latest completed run

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
- `bash ralph/init.sh` initializes `paper/` from templates.

## Ralph Loop

The Ralph workflow is specified in `spec/ralph-spec.md`.

To run: `bash ralph/ralph-loop.sh`

## `.devcontainer/` folder

Files are brought over from https://github.com/anthropics/claude-code.
