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

has_tracked_files() {
    git ls-files --error-unmatch -- "$1" >/dev/null 2>&1
}

require_clean_committed_config() {
    if ! has_tracked_files "config-ralph.yaml"; then
        log "ERROR: config-ralph.yaml must be tracked in git before starting Ralph from main"
        exit 1
    fi
    if ! git diff --quiet -- config-ralph.yaml; then
        log "ERROR: config-ralph.yaml has unstaged changes; commit it before starting Ralph from main"
        exit 1
    fi
    if ! git diff --cached --quiet -- config-ralph.yaml; then
        log "ERROR: config-ralph.yaml has staged but uncommitted changes; commit it before starting Ralph from main"
        exit 1
    fi
}

count_completed_iterations() {
    local start_commit
    start_commit="$(git log --first-parent --grep='^rloop start: record initial condition before author steps$' --format=%H -n 1 HEAD 2>/dev/null || true)"
    if [ -z "$start_commit" ]; then
        echo 0
        return
    fi
    git log --first-parent --format=%s "${start_commit}..HEAD" | awk '
        BEGIN { count = 0 }
        /^rloop-[0-9]+:/ { count++ }
        END { print count }
    '
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

run_test_quota_preflight() {
    local phase_label="$1"
    local preflight_rc
    if ! is_truthy "$QUOTA_PREFLIGHT"; then
        return 0
    fi
    python3 ralph/check-claude-budget.py \
        --phase "$phase_label" \
        --utilization-limit "$CLAUDE_5H_UTILIZATION_LIMIT" && preflight_rc=0 || preflight_rc=$?
    if [ "$preflight_rc" -eq 0 ]; then
        return 0
    fi
    if [ "$preflight_rc" -eq 2 ]; then
        log "=== stopping Ralph loop before $phase_label due to low Claude quota headroom ==="
        exit 0
    fi
    log "ERROR: Claude quota preflight failed before $phase_label"
    exit 1
}

# --- load config and validate ---
_CONFIG="$(python3 ralph/load-config.py)"
eval "$_CONFIG"

# --- branch setup ---
CURRENT_BRANCH="$(git branch --show-current)"
APPEND_LOOP_LOG=0
if [ "$CURRENT_BRANCH" = "ralph/run" ]; then
    APPEND_LOOP_LOG=1
else
    if [ "$CURRENT_BRANCH" != "main" ]; then
        log "ERROR: Ralph must be started from 'main' for a fresh stretch or from 'ralph/run' to continue"
        exit 1
    fi
    require_clean_committed_config
    log "--- setup check (fresh main start) ---"
    python3 ralph/check-setup.py --fresh-main-start || { log "ERROR: setup check failed"; exit 1; }
    startup_paths=()
    if git show-ref --verify --quiet refs/heads/ralph/run; then
        APPEND_LOOP_LOG=1
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
    mkdir -p ralph-garage ralph-garage/history ralph-garage/page-images test-results ralph-garage/agent-logs
    log "--- wipe agent logs for fresh Ralph stretch from $CURRENT_BRANCH ---"
    clear_dir ralph-garage/agent-logs
    log "--- install startup baseline from $STARTUP_SOURCE ---"
    python3 ralph/install-startup-source.py "$STARTUP_SOURCE" || {
        log "ERROR: could not install startup baseline from $STARTUP_SOURCE"; exit 1
    }
fi

log "--- setup check ---"
python3 ralph/check-setup.py || { log "ERROR: setup check failed"; exit 1; }

if [ "$CURRENT_BRANCH" != "ralph/run" ]; then
    log "--- commit startup state before author steps ---"
    for path in paper code; do
        if [ -e "$path" ] || has_tracked_files "$path"; then
            startup_paths+=("$path")
        fi
    done
    if [ "${#startup_paths[@]}" -gt 0 ]; then
        git add -A -- "${startup_paths[@]}"
    fi
    git -c user.name="Ralph Loop" -c user.email="noreply@gmail.com" commit --allow-empty \
        -m "rloop start: record initial condition before author steps"
fi

mkdir -p ralph-garage ralph-garage/history ralph-garage/page-images test-results ralph-garage/agent-logs
if [ "$APPEND_LOOP_LOG" -eq 1 ]; then
    exec > >(tee -a ralph-garage/loop.log) 2>&1
else
    exec > >(tee ralph-garage/loop.log) 2>&1
fi

if [ -n "$RUN_NOTE" ]; then
    log "=== ralph loop started: $RUN_NOTE (branch ralph/run, max $MAX_ITER iterations, agent-log-mode $AGENT_LOG_MODE) ==="
else
    log "=== ralph loop started (branch ralph/run, max $MAX_ITER iterations, agent-log-mode $AGENT_LOG_MODE) ==="
fi
completed_iterations="$(count_completed_iterations)"
log "=== completed Ralph iterations on this branch stretch: $completed_iterations / $MAX_ITER ==="

# --- pre-loop baseline ---
if is_truthy "$TEST_BEFORE_LOOP"; then
    log "--- pre-loop test & referee phase ---"
    clear_dir test-results
    if ! build_paper_artifacts; then
        log "=== pre-loop LaTeX build failed; skipping baseline test & referee phase ==="
    else
        run_test_quota_preflight "pre-loop tests"
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
iteration=$((completed_iterations + 1))
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
        log "--- build failed; attempting fix ---"
        python3 ralph/author-fix-build.py || { log "ERROR: author fix-build step failed"; exit 1; }
        if ! build_paper_artifacts; then
            log "=== iteration $iteration LaTeX build failed after fix attempt; skipping tests and referees ==="
            log "--- commit iteration $iteration ---"
            python3 ralph/commit-iteration.py "$iteration"
            iteration=$((iteration + 1))
            continue
        fi
        log "--- build fix succeeded ---"
    fi

    cp paper/paper.pdf "ralph-garage/history/$(printf '%03d-paper.pdf' "$iteration")" 2>/dev/null || true

    # 3. Run tests and referees
    log "--- test phase ---"
    run_test_quota_preflight "test phase"
    python3 ralph/run-tests.py && test_rc=0 || test_rc=$?

    if is_truthy "$REFEREES_ENABLED"; then
        log "--- referee phase ---"
        python3 ralph/run-referees.py
        log "=== referees complete ==="
    fi

    # 4. Commit and compile history
    log "--- commit iteration $iteration ---"
    python3 ralph/commit-iteration.py "$iteration"
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
