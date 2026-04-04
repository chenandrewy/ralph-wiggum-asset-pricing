# Test Result Specification

Defines the output contract for PASS/FAIL tests in `tests/`. Referee scripts (`tests/referee-*.py`) are outside this contract.

## Inputs

PASS/FAIL tests may inspect repo files needed for evaluation, including `paper/`, `code/`, `data/`, and `spec/`.

When the paper spec defines a canonical analysis pipeline, PASS/FAIL tests should evaluate that canonical pipeline as the default local workflow. If the paper spec requires the canonical pipeline to run from scratch, tests should treat from-scratch execution as the default expectation.

PASS/FAIL tests assume Ralph has already prepared:
- `paper/paper.pdf`
- `ralph-garage/page-images/page-*.png`
- `ralph-garage/page-images/exhibit-manifest.json`

## Report Contract

Each PASS/FAIL test writes exactly one markdown report at:

`test-results/<test-id>.md`

where `<test-id>` is the test script stem.

Each report must contain:
- a runner-prepended header:
  - `# <repo-relative test script path>`
  - `Started: <timestamp in America/New_York>`
  - `Runtime: <human-readable duration>`
  - optional link to an agent log
- a body beginning with:
  - `# <test-id>`
  - `VERDICT: PASS` or `VERDICT: FAIL`
  - `REASON: <one short sentence>`

Tests return:
- `0` for `PASS`
- `1` for `FAIL`

`test-results/summary.json` is the canonical machine-readable summary.

## Agent-Backed Tests

Agent-backed tests must call `ralph/agent_wrapper.py` with:
- `--step-label <test-id>`
- `--failure-log-mode off`

Agent-backed test prompts may use any structure.

Agent-backed tests should apply a strict pass/fail standard.

Agent-backed tests should use sub-agents to divide independent evaluation work whenever the test covers multiple distinct requirement groups, paper sections, claims, or exhibits. Pure Python tests and narrowly scoped agent-backed tests need not use sub-agents.
