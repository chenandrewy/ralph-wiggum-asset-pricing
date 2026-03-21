#!/usr/bin/env bash
# How to run: bash ralph/ralph-loop.sh
# Inputs: config-ralph.yaml, paper/, spec/*, tests/*, ralph/*.py
# Outputs: in-place updates under paper/, paper/paper.pdf, ralph-garage/history/*, ralph-garage/improvement-plan.md, ralph-garage/page-images/*, ralph-garage/page-images/exhibit-manifest.json, test-results/*, ralph-garage/loop.log, ralph-garage/agent-logs/*, and git commits on ralph/run
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

CONFIG_FILE="$REPO_ROOT/config-ralph.yaml"
READ_CONFIG="$REPO_ROOT/ralph/read-config.py"
PRUNE_AGENT_LOGS="$REPO_ROOT/ralph/prune-agent-logs.py"
TEST_RUNNER="$REPO_ROOT/ralph/run-tests.py"
REVIEW_RUNNER="$REPO_ROOT/ralph/run-reviews.py"
SETUP_CHECK="$REPO_ROOT/ralph/check-setup.py"
COMMIT_SCRIPT="$REPO_ROOT/ralph/commit-iteration.py"
AUTHOR_PLAN="$REPO_ROOT/ralph/author-plan.py"
AUTHOR_IMPROVE="$REPO_ROOT/ralph/author-improve.py"
BUILD_PAPER="$REPO_ROOT/ralph/build-paper.sh"
PAGE_IMAGES_SCRIPT="$REPO_ROOT/ralph/generate-page-images.py"
LATEX_BUILD_TEST="$REPO_ROOT/tests/build-latex.py"

GARAGE_DIR="$REPO_ROOT/ralph-garage"
HISTORY_DIR="$GARAGE_DIR/history"
PAGE_IMAGES_DIR="$GARAGE_DIR/page-images"
TEST_RESULTS_DIR="$REPO_ROOT/test-results"
PLAN_FILE="$GARAGE_DIR/improvement-plan.md"
AGENT_LOGS_DIR="$GARAGE_DIR/agent-logs"
RUN_BRANCH_NAME="ralph/run"

log() {
    printf '[%s] %s\n' "$(TZ='America/New_York' date '+%Y-%m-%d %H:%M')" "$*"
}

clear_transient_results_dir() {
    local target_dir="$1"
    mkdir -p "$target_dir"
    find "$target_dir" -mindepth 1 ! -name '.gitkeep' -exec rm -rf {} +
}

wipe_agent_logs() {
    clear_transient_results_dir "$AGENT_LOGS_DIR"
}

prune_agent_logs() {
    python3 "$PRUNE_AGENT_LOGS" \
        --log-dir "$AGENT_LOGS_DIR" \
        --retention-days "$AGENT_LOG_RETENTION_DAYS"
}

run_latex_build_gate() {
    local build_rc=0

    log "--- build paper ---"
    if bash "$BUILD_PAPER"; then
        build_rc=0
    else
        build_rc=$?
    fi

    if RALPH_LATEX_BUILD_GATE=1 \
        RALPH_LATEX_BUILD_EXIT_CODE="$build_rc" \
        python3 "$LATEX_BUILD_TEST"; then
        return 0
    fi

    return 1
}

reviews_enabled() {
    case "${REVIEWS_ENABLED,,}" in
        true|on|yes|1)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

commit_iteration() {
    python3 "$COMMIT_SCRIPT" \
        --repo-root "$REPO_ROOT" \
        --test-results-dir "$TEST_RESULTS_DIR" \
        --agent-log-mode "$AGENT_LOG_MODE"
}

MAX_ITER="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "max-iter")"
AGENT="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "agent")"
MODEL="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "model")"
export RALPH_AGENT="$AGENT"
export RALPH_MODEL="$MODEL"
AGENT_LOG_MODE="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "agent-log-mode" "off")"
AGENT_LOG_RETENTION_DAYS="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "agent-log-retention-days" "14")"
TEST_BEFORE_LOOP="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "test-before-loop" "off")"
REVIEWS_ENABLED="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "reviews" "false")"
CONTINUAL_IMPROVEMENT="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "continual-improvement" "false")"
RUN_NAME="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "run-name" "")"

if ! [[ "$MAX_ITER" =~ ^[1-9][0-9]*$ ]]; then
    log "ERROR: max-iter must be a positive integer (got: $MAX_ITER)"
    exit 1
fi
if [ "$AGENT" != "claude" ] && [ "$AGENT" != "codex" ]; then
    log "ERROR: agent must be 'claude' or 'codex' (got: $AGENT)"
    exit 1
fi
if [ -z "$MODEL" ]; then
    log "ERROR: model must be non-empty"
    exit 1
fi
case "${AGENT_LOG_MODE,,}" in
    off|verbose|all|1|true|yes)
        ;;
    *)
        log "ERROR: agent-log-mode must be one of: off, verbose, all, 1, true, yes (got: $AGENT_LOG_MODE)"
        exit 1
        ;;
esac
AGENT_LOG_MODE="${AGENT_LOG_MODE,,}"

if ! [[ "$AGENT_LOG_RETENTION_DAYS" =~ ^[0-9]+$ ]]; then
    log "ERROR: agent-log-retention-days must be a non-negative integer (got: $AGENT_LOG_RETENTION_DAYS)"
    exit 1
fi

case "${TEST_BEFORE_LOOP,,}" in
    off|on|1|true|yes)
        ;;
    *)
        log "ERROR: test-before-loop must be one of: off, on, 1, true, yes (got: $TEST_BEFORE_LOOP)"
        exit 1
        ;;
esac
TEST_BEFORE_LOOP="${TEST_BEFORE_LOOP,,}"

log "--- setup check ---"
if ! python3 "$SETUP_CHECK"; then
    log "ERROR: setup check failed"
    exit 1
fi

mkdir -p "$GARAGE_DIR" "$HISTORY_DIR" "$PAGE_IMAGES_DIR" "$TEST_RESULTS_DIR" "$AGENT_LOGS_DIR"
LOOP_LOG="$GARAGE_DIR/loop.log"
exec > >(tee "$LOOP_LOG") 2>&1
export RALPH_GARAGE_DIR="$GARAGE_DIR"
export RALPH_AGENT_LOG_DIR="$AGENT_LOGS_DIR"
CURRENT_BRANCH="$(git branch --show-current)"
if [ "$CURRENT_BRANCH" = "$RUN_BRANCH_NAME" ]; then
    RUN_BRANCH="$CURRENT_BRANCH"
    prune_agent_logs
else
    log "--- wipe agent logs for fresh Ralph stretch from $CURRENT_BRANCH ---"
    wipe_agent_logs
    prune_agent_logs
    if git show-ref --verify --quiet "refs/heads/$RUN_BRANCH_NAME"; then
        log "--- switch to existing $RUN_BRANCH_NAME and fast-forward from $CURRENT_BRANCH ---"
        if ! git merge-base --is-ancestor "$RUN_BRANCH_NAME" "$CURRENT_BRANCH"; then
            log "ERROR: branch '$RUN_BRANCH_NAME' has commits not merged into '$CURRENT_BRANCH'"
            log "Hint: switch to '$RUN_BRANCH_NAME' to resume that work, or merge it into '$CURRENT_BRANCH' first."
            exit 1
        fi
        if git switch "$RUN_BRANCH_NAME" && git merge --ff-only "$CURRENT_BRANCH"; then
            RUN_BRANCH="$RUN_BRANCH_NAME"
        else
            log "ERROR: could not fast-forward '$RUN_BRANCH_NAME' to '$CURRENT_BRANCH'"
            exit 1
        fi
    else
        log "--- fresh branch setup from $CURRENT_BRANCH to $RUN_BRANCH_NAME ---"
        if git switch -c "$RUN_BRANCH_NAME"; then
            RUN_BRANCH="$RUN_BRANCH_NAME"
        else
            log "ERROR: could not create branch '$RUN_BRANCH_NAME' from '$CURRENT_BRANCH'"
            exit 1
        fi
    fi
fi

if [ -n "$RUN_NAME" ]; then
    log "=== ralph loop started: $RUN_NAME (branch $RUN_BRANCH, max $MAX_ITER iterations, agent $AGENT, model $MODEL, agent-log-mode $AGENT_LOG_MODE) ==="
    export RALPH_RUN_NAME="$RUN_NAME"
else
    log "=== ralph loop started (branch $RUN_BRANCH, max $MAX_ITER iterations, agent $AGENT, model $MODEL, agent-log-mode $AGENT_LOG_MODE) ==="
fi

if [ "$TEST_BEFORE_LOOP" != "off" ]; then
    log "--- pre-loop test & review phase ---"
    prune_agent_logs
    clear_transient_results_dir "$TEST_RESULTS_DIR"
    if ! run_latex_build_gate; then
        log "=== pre-loop LaTeX build failed; skipping baseline test & review phase ==="
    else
        log "--- generate page images ---"
        if ! python3 "$PAGE_IMAGES_SCRIPT"; then
            log "ERROR: page image generation failed"
            exit 1
        fi

        python3 "$TEST_RUNNER" --agent-log-mode "$AGENT_LOG_MODE" && test_rc=0 || test_rc=$?
        if [ "$test_rc" -eq 0 ]; then
            log "=== pre-loop tests passed ==="
        else
            log "=== pre-loop tests failed ==="
        fi

        if reviews_enabled; then
            log "--- pre-loop review phase ---"
            python3 "$REVIEW_RUNNER" --agent-log-mode "$AGENT_LOG_MODE"
            log "=== pre-loop reviews complete ==="
        fi
    fi
fi

iteration=1
while true; do
    MAX_ITER="$(python3 "$READ_CONFIG" "$CONFIG_FILE" "max-iter")"
    if [ "$iteration" -gt "$MAX_ITER" ]; then
        break
    fi
    log "=== iteration $iteration / $MAX_ITER ==="
    rm -f "$PLAN_FILE" "$AGENT_LOGS_DIR/agent-failure.log"
    mkdir -p "$AGENT_LOGS_DIR"
    prune_agent_logs

    log "--- author plan ---"
    python3 "$AUTHOR_PLAN" \
        --repo-root "$REPO_ROOT" \
        --agent "$AGENT" \
        --model "$MODEL" \
        --agent-log-mode "$AGENT_LOG_MODE" \
        --iteration "$iteration" || {
        rc=$?
        log "ERROR: author plan step failed (exit $rc)"
        exit 1
    }

    log "--- author improve ---"
    python3 "$AUTHOR_IMPROVE" \
        --repo-root "$REPO_ROOT" \
        --agent "$AGENT" \
        --model "$MODEL" \
        --agent-log-mode "$AGENT_LOG_MODE" \
        --iteration "$iteration" || {
        rc=$?
        log "ERROR: author improve step failed (exit $rc)"
        exit 1
    }

    clear_transient_results_dir "$TEST_RESULTS_DIR"
    if ! run_latex_build_gate; then
        log "=== iteration $iteration LaTeX build failed; skipping tests and reviews ==="
        log "--- commit iteration $iteration ---"
        commit_iteration
        continue
    fi

    cp "$REPO_ROOT/paper/paper.pdf" "$HISTORY_DIR/$(printf '%03d-paper.pdf' "$iteration")" 2>/dev/null || true

    log "--- generate page images ---"
    if ! python3 "$PAGE_IMAGES_SCRIPT"; then
        log "ERROR: page image generation failed"
        exit 1
    fi

    log "--- test phase ---"
    python3 "$TEST_RUNNER" --agent-log-mode "$AGENT_LOG_MODE" && test_rc=0 || test_rc=$?

    if reviews_enabled; then
        log "--- review phase ---"
        python3 "$REVIEW_RUNNER" --agent-log-mode "$AGENT_LOG_MODE"
        log "=== reviews complete ==="
    fi

    log "--- commit iteration $iteration ---"
    commit_iteration
    python3 "$REPO_ROOT/ralph/compile-improvement-plan-history.py" --repo-root "$REPO_ROOT" || true
    python3 "$REPO_ROOT/ralph/compile-test-result-history.py" --repo-root "$REPO_ROOT" || true

    if [ "$test_rc" -eq 0 ]; then
        if [ "${CONTINUAL_IMPROVEMENT,,}" = "true" ] || [ "${CONTINUAL_IMPROVEMENT,,}" = "on" ] || [ "${CONTINUAL_IMPROVEMENT,,}" = "yes" ] || [ "${CONTINUAL_IMPROVEMENT,,}" = "1" ]; then
            log "=== all tests passed at iteration $iteration (continual-improvement: continuing) ==="
        else
            log "=== all tests passed at iteration $iteration ==="
            exit 0
        fi
    fi
    iteration=$((iteration + 1))
done

if [ "${CONTINUAL_IMPROVEMENT,,}" = "true" ] || [ "${CONTINUAL_IMPROVEMENT,,}" = "on" ] || [ "${CONTINUAL_IMPROVEMENT,,}" = "yes" ] || [ "${CONTINUAL_IMPROVEMENT,,}" = "1" ]; then
    log "=== continual-improvement: completed $MAX_ITER iterations ==="
    exit 0
fi

log "=== iteration limit reached ($MAX_ITER) ==="
exit 1
