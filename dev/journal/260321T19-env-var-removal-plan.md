# Env Var Inventory and Removal Plan
**Date:** 2026-03-21, 7:00 PM ET

## Purpose

This note focuses on each environment variable currently used in the repo runtime and wrapper flow.

For each env var, the note answers three questions:

1. What is the env var?
2. What does it do now?
3. How should it be removed?

The recommended design is:

- Keep durable settings in `config-ralph.yaml`.
- Pass transient execution state through explicit CLI flags.
- Inline agent/model selection inside each Python script when that choice is part of the script's design.
- Hardcode fixed wrapper behavior when it is not a meaningful configuration axis.
- Avoid env vars for internal repo control flow.

## Runtime env vars

### `RALPH_AGENT`

**What it does**

- Set by `ralph/ralph-loop.sh`.
- Read by `tests/_test_helpers.py`, `tests/_referee_helpers.py`, and `ralph/commit-iteration.py`.
- Chooses the agent provider for tests, reviews, and commit-message generation.

**How to remove**

- Inline `AGENT = "..."` in each Python entrypoint that uses an agent.
- Let each test, referee, author, or commit script define its own provider choice locally.
- Remove `load_agent_model()` environment reads from the test/referee helpers.
- Remove any assumption that `ralph/run-tests.py` or `ralph/run-reviews.py` centrally decides the agent for child scripts.
- Remove `export RALPH_AGENT=...` from `ralph/ralph-loop.sh`.

**Design note**

- This repo should treat agent selection as part of each script's design, not as external orchestration state.
- That makes the choice visible at the point of use and allows different scripts to intentionally use different agents.

### `RALPH_MODEL`

**What it does**

- Set by `ralph/ralph-loop.sh`.
- Read by `tests/_test_helpers.py` and `tests/_referee_helpers.py`.
- Chooses the model for tests and reviews.

**How to remove**

- Inline `MODEL = "..."` in each Python entrypoint that needs a model choice.
- Keep the model definition next to the script's prompt and evaluation logic.
- Remove the environment fallback from shared helpers.
- Remove `export RALPH_MODEL=...` from `ralph/ralph-loop.sh`.

**Design note**

- Model choice belongs with the script because different tests, referees, or author steps may need different model behavior.
- Centralizing it outside the script hides an important design choice.

### `RALPH_AGENT_LOG_DIR`

**What it does**

- Set by `ralph/ralph-loop.sh`.
- Read by `ralph/agent_wrapper.py`.
- Tells the wrapper where to write verbose agent logs and `agent-failure.log`.

**How to remove**

- Hardcode the log directory in `ralph/agent_wrapper.py` as `ralph-garage/agent-logs`.
- Remove `resolve_agent_log_dir()` environment lookup.
- Let the wrapper always write logs to that path.
- Remove `export RALPH_AGENT_LOG_DIR=...` from `ralph/ralph-loop.sh`.

**Design note**

- The log directory is fixed repo behavior, not a useful runtime knob.
- Hardcoding it is clearer than plumbing it through the environment or CLI.

### `RALPH_RUN_NAME`

**What it does**

- Set by `ralph/ralph-loop.sh`.
- Read by `ralph/commit-iteration.py`.
- Used only to add `[run-name]` into the iteration commit prefix.

**How to remove**

- Have `ralph/commit-iteration.py` read `run-name` directly from `config-ralph.yaml`.
- Remove the environment lookup from `commit_prefix()`.
- Remove `export RALPH_RUN_NAME=...` from `ralph/ralph-loop.sh`.

**Design note**

- `run-name` is durable loop configuration, so it belongs in `config-ralph.yaml`.
- It does not need to be passed through the environment or CLI.

### `RALPH_TEST_STARTED_AT_UTC`

**What it does**

- Set by `ralph/run-tests.py`.
- Read by `tests/_test_helpers.py`.
- Passes a parent timestamp into each test subprocess so the test report header and summary share the same start time.

**How to remove**

- Remove the env var entirely.
- Have each test script record its own local start time when it begins.
- Let `tests/_test_helpers.py` build report timing from the test script's own execution.
- Let `ralph/run-tests.py` keep its separate timing for the run summary.

**Design note**

- There is no strong reason to pass timing state from the parent runner into each child test.
- Small differences between runner timing and test-local timing are acceptable and simpler.

### `RALPH_LATEX_BUILD_GATE`

**What it does**

- Set inline in `ralph/ralph-loop.sh`.
- Read by `tests/build-latex.py`.
- Tells the build-latex script whether it is running in gate mode and should also write `test-results/summary.json`.

**How to remove**

- Remove the env var entirely.
- Make `tests/build-latex.py` a normal self-contained test script that always just evaluates the LaTeX artifacts and writes its normal report.
- Move gate-only summary behavior out of `tests/build-latex.py` and into the caller, or into a small dedicated helper if needed.
- Remove all gate-mode branching from `tests/build-latex.py`.

**Design note**

- Gate mode is a caller responsibility, not a hidden mode that the test script should infer from ambient state.
- Splitting those responsibilities is clearer than replacing the env var with a CLI flag.

### `RALPH_LATEX_BUILD_EXIT_CODE`

**What it does**

- Set inline in `ralph/ralph-loop.sh`.
- Read by `tests/build-latex.py`.
- Passes the shell LaTeX build return code into the Python gate script.

**How to remove**

- Remove the env var entirely.
- Make `tests/build-latex.py` evaluate pass/fail only from the artifacts it inspects:
  - `paper/.latex-build.log`
  - `paper/paper.pdf`
  - freshness relative to `paper/paper.tex`
  - fatal errors found in the log
- Remove any dependency on the shell build return code.

**Design note**

- The build-latex test should be artifact-based and self-contained.
- It should not need hidden state from the caller in order to know whether the build succeeded.

## Wrapper/debug env vars

### `AGENT_STDIO_ECHO`

**What it does**

- Read by `ralph/agent_wrapper.py`.
- Controls whether wrapper stdout/stderr is echoed to the caller.

**How to remove**

- Hardcode the current default behavior directly in `ralph/agent_wrapper.py`.
- Remove the environment lookup entirely.
- Do not replace it with a CLI flag unless a real need appears.

### `CLAUDE_SAFE_OUTPUT_FORMAT`

**What it does**

- Read by `ralph/agent_wrapper.py`.
- Alters Claude output mode.
- Also set internally by the wrapper when verbose logging is enabled.

**How to remove**

- Hardcode wrapper behavior:
  - use text output in normal mode
  - use stream-json output when verbose agent logging is enabled
- Let the wrapper decide output mode directly from its local logic.
- Remove the environment lookup entirely.

### `CLAUDE_SAFE_USE_JQ`

**What it does**

- Read by `ralph/agent_wrapper.py`.
- Controls whether stream-json output is piped through `jq`.

**How to remove**

- Pick deterministic behavior in code.
- Recommended rule: if `jq` exists, use it; otherwise skip it.
- Remove the environment lookup entirely.

### `CLAUDE_SAFE_JQ_FILTER`

**What it does**

- Read by `ralph/agent_wrapper.py`.
- Customizes the `jq` filter applied to Claude stream-json output.

**How to remove**

- Hardcode the filter in the wrapper.
- Remove the environment lookup entirely.

### `CLAUDE_STREAM_JSON_CAPTURE`

**What it does**

- Read by `ralph/agent_wrapper.py`.
- Holds the temp-file path used to capture raw Claude stream-json output.
- Set internally by the wrapper before invoking Claude.

**How to remove**

- Keep the capture path as a normal local variable.
- Pass it directly into helper functions such as `build_bash_command()` instead of routing through the environment.
- Do not expose it as a CLI flag.

## Non-runtime env vars to keep

### `CLAUDE*` and `CLAUDECODE`

**What it does**

- These are not repo control vars.
- `ralph/agent_wrapper.py` clears them from the child environment before invoking Claude to avoid nested-session issues.

**How to remove**

- Do not remove as part of this cleanup.
- Keep the cleanup behavior unless the wrapper architecture changes materially.

### `CLAUDE_OUTPUT`

**What it does**

- Used only in `.devcontainer/aliases.sh`.
- Controls a developer convenience shell function.

**How to remove**

- No change needed for the repo runtime.
- Leave it alone unless the shell aliases are being redesigned.

### `CLAUDE_CODE_VERSION`, `CODEX_CLI_VERSION`, `CLAUDE_CONFIG_DIR`, `CODEX_HOME`, `PATH`

**What it does**

- Defined in `.devcontainer/`.
- Used for container/toolchain setup.

**How to remove**

- Do not treat these as Ralph runtime env vars.
- Leave them in place.

## Recommended order of work

1. Remove `RALPH_AGENT` and `RALPH_MODEL` by inlining those choices in each Python script.
2. Remove `RALPH_AGENT_LOG_DIR` and `RALPH_RUN_NAME`.
   - Hardcode the log dir in the wrapper.
   - Read `run-name` directly from `config-ralph.yaml` in `commit-iteration.py`.
3. Remove `RALPH_TEST_STARTED_AT_UTC`, `RALPH_LATEX_BUILD_GATE`, and `RALPH_LATEX_BUILD_EXIT_CODE`.
   - Let each test time itself locally.
   - Make `build-latex.py` self-contained.
   - Move any gate-only summary behavior to the caller or a dedicated helper.
4. Simplify `ralph/agent_wrapper.py` by removing `AGENT_STDIO_ECHO`, `CLAUDE_SAFE_OUTPUT_FORMAT`, `CLAUDE_SAFE_USE_JQ`, `CLAUDE_SAFE_JQ_FILTER`, and `CLAUDE_STREAM_JSON_CAPTURE`.
   - Hardcode the wrapper behaviors that are currently hidden behind these env vars.

## Recommendation

Do not replace these env vars with more config files.

Use:

- `config-ralph.yaml` for durable loop configuration
- in-script constants for script-specific agent/model choices
- explicit CLI flags only when transient script-to-script wiring is truly needed
- hardcoded local constants and logic for fixed wrapper behavior such as log dir and output shaping
- env vars only for real external environment concerns
