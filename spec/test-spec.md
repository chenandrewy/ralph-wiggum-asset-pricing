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

Agent-backed test prompts should include:
- `Procedure`: a step by step process the agent should follow while evaluating the test
- `Requirements`: declarative statements that must be true for the test to pass
- `Output`: instructions for how to write the report body

These sections should use parallel structure:
- `Procedure` must be a numbered list so individual steps can be referenced unambiguously.
- `Requirements` must be a numbered list so individual pass/fail conditions can be referenced unambiguously.
- `Output` must explicitly instruct the agent to write the standard report body beginning with:
  - `# <test-id>`
  - `VERDICT: PASS` or `VERDICT: FAIL`
  - `REASON: <one short sentence>`
  - And then further details on the findings.

In the `Requirements` section:
- each item should be written as a declarative sentence or sentences
- each item should state a condition for passing
- items should not be phrased as questions
- For tests that evaluate an external specification, the prompt `Requirements` section should define what must be true for the evaluation to pass, such as exhaustiveness, evidence standards, and fail-on-any-violation behavior. It need not restate every requirement from the external specification.

Agent-backed tests should instruct the agent to apply a strict pass/fail standard. A numbered requirement should fail if the available evidence is missing, ambiguous, inconsistent, or only partially supports compliance.

For tests that evaluate analysis code or reproducibility, prompts should distinguish clearly between:
- the canonical analysis pipeline required by the paper spec
- any optional or non-canonical exploratory workflows
- and any caches, intermediate files, or downloaded inputs that the canonical pipeline creates or uses

Such tests should fail if the canonical pipeline is ambiguous, relies silently on inconsistent cached objects or manually prepared files, or does not satisfy the paper spec's required execution model.

Agent-backed tests should use sub-agents to divide independent evaluation work whenever the test covers multiple distinct requirement groups, paper sections, claims, or exhibits. Pure Python tests and narrowly scoped agent-backed tests need not use sub-agents.
