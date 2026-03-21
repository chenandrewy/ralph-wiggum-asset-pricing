# Test Result Specification

## Purpose

Define required output behavior for all tests under `tests/`.

## Terminology

- `test result`: markdown report at `test-results/<test-id>.md`.
- `agent log`: raw runtime log under `ralph-garage/agent-logs/`.
- `agent-backed test`: a test that calls an LLM via `ralph/agent_wrapper.py`.
- `pure Python test`: a test using only local Python logic.
- `page images`: PNG renders of `paper/paper.pdf` at `ralph-garage/page-images/page-*.png`.
- `exhibit manifest`: JSON file at `ralph-garage/page-images/exhibit-manifest.json` that maps rendered page images to the expected figures and tables visible on each page.

## Evaluation Scope (Files Under Test)

Primary source trees evaluated by tests:
- `paper/` (including `paper/paper.tex`, `paper/paper.pdf`, and `paper/references.bib`)
- `spec/` (at minimum `spec/paper-spec.md` for compliance tests)

## Artifact Preparation

- Before executing tests, the Ralph loop MUST first run a deterministic LaTeX build gate for `paper/paper.tex`.
- If the LaTeX build gate fails, `ralph/run-tests.py` MUST NOT run for that iteration.
- If the LaTeX build gate succeeds, the Ralph loop MUST prepare the remaining test artifacts.
- Remaining test artifact preparation consists of:
  - rendering `paper/paper.pdf` into `ralph-garage/page-images/page-*.png`
  - building `ralph-garage/page-images/exhibit-manifest.json`

## Test Result Contract

- Each invocation of `ralph/run-tests.py` owns `test-results/`.
- Each test MUST produce `test-results/<test-id>.md`.
- The runner MUST prepend a human-readable metadata header before the test body:
  - line 1: `# <repo-relative test script path>`
  - next: `Started: <timestamp in America/New_York>`
  - next: `Runtime: <human-readable wall-clock duration>`
  - optional next: markdown link to the agent log under `ralph-garage/agent-logs/`
- After one blank line, the report body MUST begin with:
  - line 1 of body: `# <test-id>`
  - next: `VERDICT: PASS` or `VERDICT: FAIL`
  - next: `REASON: <one short sentence>`
- Tests MUST return exit code `0` for PASS, `1` for FAIL.
- `test-results/summary.json` remains the canonical machine-readable test summary.

## Agent Wrapper Contract

- Agent-backed tests MUST call `ralph/agent_wrapper.py` with `--step-label <test-id>` and `--failure-log-mode off`.
