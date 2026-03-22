#!/usr/bin/env bash
# How to run: bash ralph/ralph-loop.sh
# Inputs: config-ralph.yaml, paper/, spec/*, tests/*, ralph/*.py
# Outputs: in-place updates under paper/, paper/paper.pdf, ralph-garage/history/*,
#          ralph-garage/improvement-plan.md, ralph-garage/page-images/*,
#          ralph-garage/page-images/exhibit-manifest.json, test-results/*,
#          ralph-garage/loop.log, ralph-garage/agent-logs/*, and git commits on ralph/run
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

log() {
    printf '[%s] %s\n' "$(TZ='America/New_York' date '+%Y-%m-%d %H:%M')" "$*"
}

is_truthy() { case "${1,,}" in true|on|yes|1) return 0;; *) return 1;; esac; }

clear_dir() {
    mkdir -p "$1"
    find "$1" -mindepth 1 ! -name '.gitkeep' -exec rm -rf {} +
}

# Build paper, run build gate test, and generate page images.
# Returns 1 if the LaTeX build gate fails (caller decides how to handle).
# Exits the script if page image generation fails (unrecoverable).
build_paper_artifacts() {
    log "--- build paper ---"
    bash ralph/build-paper.sh || return 1
    python3 tests/build-latex.py || return 1
    log "--- generate page images ---"
    python3 ralph/generate-page-images.py || { log "ERROR: page image generation failed"; exit 1; }
}

# --- load config and validate ---
_CONFIG="$(python3 ralph/load-config.py)"
eval "$_CONFIG"

log "--- setup check ---"
python3 ralph/check-setup.py || { log "ERROR: setup check failed"; exit 1; }

mkdir -p ralph-garage ralph-garage/history ralph-garage/page-images test-results ralph-garage/agent-logs
exec > >(tee ralph-garage/loop.log) 2>&1
export RALPH_GARAGE_DIR=ralph-garage

# --- branch setup ---
CURRENT_BRANCH="$(git branch --show-current)"
if [ "$CURRENT_BRANCH" = "ralph/run" ]; then
    :
else
    log "--- wipe agent logs for fresh Ralph stretch from $CURRENT_BRANCH ---"
    clear_dir ralph-garage/agent-logs
    if git show-ref --verify --quiet refs/heads/ralph/run; then
        log "--- switch to existing ralph/run and fast-forward from $CURRENT_BRANCH ---"
        if ! git merge-base --is-ancestor ralph/run "$CURRENT_BRANCH"; then
            log "ERROR: branch 'ralph/run' has commits not merged into '$CURRENT_BRANCH'"
            log "Hint: switch to 'ralph/run' to resume that work, or merge it into '$CURRENT_BRANCH' first."
            exit 1
        fi
        git switch ralph/run && git merge --ff-only "$CURRENT_BRANCH" || {
            log "ERROR: could not fast-forward 'ralph/run' to '$CURRENT_BRANCH'"; exit 1
        }
    else
        log "--- fresh branch setup from $CURRENT_BRANCH to ralph/run ---"
        git switch -c ralph/run || {
            log "ERROR: could not create branch 'ralph/run' from '$CURRENT_BRANCH'"; exit 1
        }
    fi
fi

if [ -n "$RUN_NAME" ]; then
    log "=== ralph loop started: $RUN_NAME (branch ralph/run, max $MAX_ITER iterations, agent-log-mode $AGENT_LOG_MODE) ==="
    export RALPH_RUN_NAME="$RUN_NAME"
else
    log "=== ralph loop started (branch ralph/run, max $MAX_ITER iterations, agent-log-mode $AGENT_LOG_MODE) ==="
fi

# --- pre-loop baseline ---
if is_truthy "$TEST_BEFORE_LOOP"; then
    log "--- pre-loop test & referee phase ---"
    clear_dir test-results
    if ! build_paper_artifacts; then
        log "=== pre-loop LaTeX build failed; skipping baseline test & referee phase ==="
    else
        python3 ralph/run-tests.py && test_rc=0 || test_rc=$?
        if [ "$test_rc" -eq 0 ]; then
            log "=== pre-loop tests passed ==="
        else
            log "=== pre-loop tests failed ==="
        fi
        if is_truthy "$REFEREES_ENABLED"; then
            log "--- pre-loop referee phase ---"
            python3 ralph/run-referees.py
            log "=== pre-loop referees complete ==="
        fi
    fi
fi

# --- main loop ---
iteration=1
while true; do
    _CONFIG="$(python3 ralph/load-config.py)"
    eval "$_CONFIG"
    if [ "$iteration" -gt "$MAX_ITER" ]; then break; fi
    log "=== iteration $iteration / $MAX_ITER ==="
    rm -f ralph-garage/improvement-plan.md ralph-garage/agent-logs/agent-failure.log
    mkdir -p ralph-garage/agent-logs

    # 1. Plan and author improvements
    log "--- author plan ---"
    python3 ralph/author-plan.py || { log "ERROR: author plan step failed"; exit 1; }

    log "--- author improve ---"
    python3 ralph/author-improve.py || { log "ERROR: author improve step failed"; exit 1; }

    # 2. Build paper and generate test artifacts (build gate)
    clear_dir test-results
    if ! build_paper_artifacts; then
        log "=== iteration $iteration LaTeX build failed; skipping tests and referees ==="
        log "--- commit iteration $iteration ---"
        python3 ralph/commit-iteration.py
        continue
    fi

    cp paper/paper.pdf "ralph-garage/history/$(printf '%03d-paper.pdf' "$iteration")" 2>/dev/null || true

    # 3. Run tests and referees
    log "--- test phase ---"
    python3 ralph/run-tests.py && test_rc=0 || test_rc=$?

    if is_truthy "$REFEREES_ENABLED"; then
        log "--- referee phase ---"
        python3 ralph/run-referees.py
        log "=== referees complete ==="
    fi

    # 4. Commit and compile history
    log "--- commit iteration $iteration ---"
    python3 ralph/commit-iteration.py
    python3 ralph/compile-improvement-plan-history.py || true
    python3 ralph/compile-test-result-history.py || true

    # 5. Exit or continue
    if [ "$test_rc" -eq 0 ]; then
        if is_truthy "$CONTINUAL_IMPROVEMENT"; then
            log "=== all tests passed at iteration $iteration (continual-improvement: continuing) ==="
        else
            log "=== all tests passed at iteration $iteration ==="
            exit 0
        fi
    fi
    iteration=$((iteration + 1))
done

if is_truthy "$CONTINUAL_IMPROVEMENT"; then
    log "=== continual-improvement: completed $MAX_ITER iterations ==="
    exit 0
fi

log "=== iteration limit reached ($MAX_ITER) ==="
exit 1
