#!/usr/bin/env python3
"""
Lightweight agent wrapper that dispatches to Claude or Codex.

Wrapper-level effort control is provider-agnostic:
- `--effort ...` maps to Claude CLI `--effort ...`
- `--effort ...` maps to Codex CLI `-c model_reasoning_effort="..."`

Omitting `--effort` preserves each provider's default behavior. Supported
effort levels differ by provider/model, so unsupported combinations should
fail clearly at the wrapper or provider boundary.
"""
import subprocess
import sys
import os
import shlex
import shutil
import tempfile
import threading
from datetime import datetime
from zoneinfo import ZoneInfo

LOG_SECTION_MAX_BYTES = 500000
DEFAULT_GARAGE_DIR = "ralph-garage"
DEFAULT_AGENT_LOG_DIR = "ralph-garage/agent-logs"
CLAUDE_STREAM_JQ_FILTER = ".result // ."
VALID_LOG_MODES = ("off", "verbose", "all", "1", "true", "yes")
VALID_FAILURE_LOG_MODES = ("on", "off", "auto")
VALID_CLAUDE_EFFORTS = ("low", "medium", "high", "max")
VALID_CODEX_EFFORTS = ("none", "low", "medium", "high", "xhigh")
NEW_YORK_TZ = ZoneInfo("America/New_York")


def write_log(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def normalize_log_mode(value):
    return (value or 'off').strip().lower()


def agent_logs_enabled(log_mode):
    return normalize_log_mode(log_mode) in VALID_LOG_MODES[1:]


def split_agent_args(args):
    agent = "claude"
    step_label = None
    log_mode = "off"
    failure_log_mode = "on"
    effort = None
    forwarded = []
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--agent":
            if i + 1 >= len(args):
                print("ERROR: --agent requires a value", file=sys.stderr)
                sys.exit(1)
            agent = args[i + 1].strip().lower()
            i += 2
            continue
        if arg == "--step-label":
            if i + 1 >= len(args):
                print("ERROR: --step-label requires a value", file=sys.stderr)
                sys.exit(1)
            step_label = args[i + 1]
            i += 2
            continue
        if arg == "--log-mode":
            if i + 1 >= len(args):
                print("ERROR: --log-mode requires a value", file=sys.stderr)
                sys.exit(1)
            log_mode = normalize_log_mode(args[i + 1])
            if log_mode not in VALID_LOG_MODES:
                allowed = ", ".join(VALID_LOG_MODES)
                print(f"ERROR: unsupported --log-mode '{log_mode}' (expected one of: {allowed})", file=sys.stderr)
                sys.exit(1)
            i += 2
            continue
        if arg == "--failure-log-mode":
            if i + 1 >= len(args):
                print("ERROR: --failure-log-mode requires a value", file=sys.stderr)
                sys.exit(1)
            failure_log_mode = args[i + 1].strip().lower()
            if failure_log_mode not in VALID_FAILURE_LOG_MODES:
                allowed = ", ".join(VALID_FAILURE_LOG_MODES)
                print(
                    f"ERROR: unsupported --failure-log-mode '{failure_log_mode}' (expected one of: {allowed})",
                    file=sys.stderr,
                )
                sys.exit(1)
            i += 2
            continue
        if arg == "--effort":
            if i + 1 >= len(args):
                print("ERROR: --effort requires a value", file=sys.stderr)
                sys.exit(1)
            effort = args[i + 1].strip().lower()
            i += 2
            continue
        forwarded.append(arg)
        i += 1
    if agent not in ("claude", "codex"):
        print(f"ERROR: unsupported agent '{agent}' (expected 'claude' or 'codex')", file=sys.stderr)
        sys.exit(1)

    if effort is not None:
        if agent == "claude" and effort not in VALID_CLAUDE_EFFORTS:
            allowed = ", ".join(VALID_CLAUDE_EFFORTS)
            print(
                f"ERROR: unsupported --effort '{effort}' for claude (expected one of: {allowed})",
                file=sys.stderr,
            )
            sys.exit(1)
        if agent == "codex" and effort not in VALID_CODEX_EFFORTS:
            allowed = ", ".join(VALID_CODEX_EFFORTS)
            print(
                f"ERROR: unsupported --effort '{effort}' for codex (expected one of: {allowed})",
                file=sys.stderr,
            )
            sys.exit(1)

    return agent, step_label, log_mode, failure_log_mode, effort, forwarded


def build_bash_command(agent, forwarded_args, log_mode, effort=None, stream_capture_path=None):
    args_str = ' '.join(shlex.quote(arg) for arg in forwarded_args)
    if agent == "codex":
        effort_flag = ""
        if effort is not None:
            config_override = f'model_reasoning_effort="{effort}"'
            effort_flag = f" -c {shlex.quote(config_override)}"
        return f"codex exec --sandbox danger-full-access{effort_flag} {args_str}"

    output_format = 'stream-json' if agent_logs_enabled(log_mode) else 'text'
    effort_flag = f" --effort {shlex.quote(effort)}" if effort is not None else ""

    base_cmd = (
        f"claude -p --output-format {shlex.quote(output_format)}"
        f"{effort_flag} --dangerously-skip-permissions {args_str}"
    )

    if output_format != 'stream-json':
        return base_cmd

    # Stream mode is more informative when verbose event logs are enabled.
    stream_cmd = (
        f"claude -p --verbose --output-format stream-json"
        f"{effort_flag} --dangerously-skip-permissions {args_str}"
    )
    if stream_capture_path:
        tee_cmd = f"{stream_cmd} | tee {shlex.quote(stream_capture_path)}"
        if shutil.which('jq'):
            return f"set -o pipefail; {tee_cmd} | jq -r {shlex.quote(CLAUDE_STREAM_JQ_FILTER)}"
        return f"set -o pipefail; {tee_cmd}"
    if shutil.which('jq'):
        return f"set -o pipefail; {stream_cmd} | jq -r {shlex.quote(CLAUDE_STREAM_JQ_FILTER)}"
    return stream_cmd


def should_echo_output(step_label, rc):
    label = (step_label or '').strip().lower()
    if label.startswith('author-'):
        return rc != 0
    return True


def safe_label(text):
    cleaned = ''.join(ch if (ch.isalnum() or ch in '._-') else '_' for ch in text)
    cleaned = cleaned.strip('_')
    return cleaned or "run"


def truncate_log_section(text):
    if LOG_SECTION_MAX_BYTES == 0:
        return text
    data = text.encode('utf-8', errors='replace')
    if len(data) <= LOG_SECTION_MAX_BYTES:
        return text
    kept = data[-LOG_SECTION_MAX_BYTES:].decode('utf-8', errors='replace')
    return f"(truncated; keeping last {LOG_SECTION_MAX_BYTES} bytes)\n{kept}"


def now_ny():
    return datetime.now(NEW_YORK_TZ)


def build_verbose_log_path(agent, model, step_label, ts=None):
    step_label = safe_label(step_label or 'run')
    model_label = safe_label(model)
    if ts is None:
        ts = now_ny().strftime('%Y%m%dT%H%M%S.%f%z')
    return os.path.join(DEFAULT_AGENT_LOG_DIR, f"{ts}_{step_label}_{agent}_{model_label}.log")


def write_verbose_log(agent, model, step_label, log_mode, rc, stdout_text, stderr_text, stream_json_text="", log_path=None):
    if not agent_logs_enabled(log_mode):
        return

    step_label = safe_label(step_label or 'run')
    if log_path is None:
        log_path = build_verbose_log_path(agent, model, step_label)
    payload = (
        f"timestamp_ny: {now_ny().isoformat(timespec='seconds')}\n"
        f"agent: {agent}\n"
        f"step_label: {step_label}\n"
        f"model: {model}\n"
        f"exit_code: {rc}\n"
        f"{'-' * 72}\n"
        f"[STREAM_JSON]\n"
        f"{truncate_log_section(stream_json_text or '')}\n"
        f"{'-' * 72}\n"
        f"[STDOUT]\n"
        f"{truncate_log_section(stdout_text or '')}\n"
        f"{'-' * 72}\n"
        f"[STDERR]\n"
        f"{truncate_log_section(stderr_text or '')}\n"
    )
    write_log(log_path, payload)


def run_command_with_live_capture(bash_command, env, live_log_path=None):
    process = subprocess.Popen(
        ['bash', '-c', bash_command],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
        bufsize=1,
    )

    stdout_chunks = []
    stderr_chunks = []
    lock = threading.Lock()
    live_file = None
    if live_log_path:
        os.makedirs(os.path.dirname(live_log_path), exist_ok=True)
        live_file = open(live_log_path, 'a', encoding='utf-8')

    def _pump(stream, target, label):
        if stream is None:
            return
        for line in iter(stream.readline, ''):
            target.append(line)
            if live_file is not None:
                with lock:
                    live_file.write(f"[{label}] {line}")
                    live_file.flush()
        stream.close()

    stdout_thread = threading.Thread(target=_pump, args=(process.stdout, stdout_chunks, "STDOUT"))
    stderr_thread = threading.Thread(target=_pump, args=(process.stderr, stderr_chunks, "STDERR"))
    stdout_thread.start()
    stderr_thread.start()
    stdout_thread.join()
    stderr_thread.join()
    try:
        rc = process.wait(timeout=60)
    except subprocess.TimeoutExpired:
        process.kill()
        rc = process.wait()

    if live_file is not None:
        live_file.close()

    return rc, ''.join(stdout_chunks), ''.join(stderr_chunks)


def should_write_failure_log(step_label, failure_log_mode):
    mode = (failure_log_mode or "on").strip().lower()
    if mode == "on":
        return True
    if mode == "off":
        return False
    label = (step_label or "").strip().lower()
    return label.startswith("author-")


def handle_failure(agent, model, step_label, failure_log_mode, rc, stdout_text, stderr_text):
    if not should_write_failure_log(step_label, failure_log_mode):
        sys.exit(1)

    error_text = (stderr_text or '') + (stdout_text or '')
    ts = now_ny().isoformat(timespec='seconds')
    snippet_lines = error_text.strip().splitlines()[-20:]
    snippet = '\n'.join(snippet_lines) if snippet_lines else '(no output captured)'
    failure_record = (
        f"[{ts}] agent={agent} model={model} exit_code={rc}\n"
        f"{snippet}\n"
        f"{'-' * 72}\n"
    )
    write_log(os.path.join(DEFAULT_AGENT_LOG_DIR, "agent-failure.log"), failure_record)
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: agent_wrapper.py [agent arguments...]", file=sys.stderr)
        sys.exit(1)

    agent, step_label, log_mode, failure_log_mode, effort, forwarded_args = split_agent_args(sys.argv[1:])

    env = os.environ.copy()
    stream_capture_path = None
    if agent == "claude" and agent_logs_enabled(log_mode):
        fd, stream_capture_path = tempfile.mkstemp(prefix='ralph-stream-json-', suffix='.log')
        os.close(fd)

    args = forwarded_args
    model = "unknown"
    for i, arg in enumerate(args):
        if arg == '--model' and i + 1 < len(args):
            model = args[i + 1]
            break

    # Build the command for the selected agent.
    bash_command = build_bash_command(agent, forwarded_args, log_mode, effort, stream_capture_path)

    live_log_path = None
    if agent_logs_enabled(log_mode):
        live_log_path = build_verbose_log_path(agent, model, step_label)
        write_log(
            live_log_path,
            (
                f"timestamp_ny: {now_ny().isoformat(timespec='seconds')}\n"
                f"agent: {agent}\n"
                f"step_label: {safe_label(step_label or 'run')}\n"
                f"model: {model}\n"
                f"status: running\n"
                f"{'-' * 72}\n"
                f"[LIVE]\n"
            ),
        )

    rc, stdout_text, stderr_text = run_command_with_live_capture(bash_command, env, live_log_path=live_log_path)
    stream_json_text = ""
    if stream_capture_path and os.path.exists(stream_capture_path):
        try:
            with open(stream_capture_path, 'r', encoding='utf-8', errors='replace') as f:
                stream_json_text = f.read()
        finally:
            try:
                os.remove(stream_capture_path)
            except OSError:
                pass

    if should_echo_output(step_label, rc):
        # Preserve agent output for callers (tests parse VERDICT lines from stdout).
        if stdout_text:
            print(stdout_text, end="")
        if stderr_text:
            print(stderr_text, file=sys.stderr, end="")

    write_verbose_log(
        agent,
        model,
        step_label,
        log_mode,
        rc,
        stdout_text,
        stderr_text,
        stream_json_text,
        log_path=live_log_path,
    )

    if rc != 0:
        handle_failure(agent, model, step_label, failure_log_mode, rc, stdout_text, stderr_text)

    sys.exit(0)


if __name__ == '__main__':
    main()
