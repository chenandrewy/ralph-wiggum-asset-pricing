#!/usr/bin/env python3
"""
Lightweight agent wrapper that dispatches to Claude or Codex.
"""
import subprocess
import sys
import os
import shlex
import shutil
import tempfile
import threading
from datetime import datetime, timezone

LOG_SECTION_MAX_BYTES = 500000
DEFAULT_GARAGE_DIR = "ralph-garage"
DEFAULT_AGENT_LOG_DIR = "ralph-garage/agent-logs"
VALID_LOG_MODES = ("off", "verbose", "all", "1", "true", "yes")
VALID_FAILURE_LOG_MODES = ("on", "off", "auto")


def write_log(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def resolve_agent_log_dir():
    configured = os.environ.get("RALPH_AGENT_LOG_DIR", "").strip()
    return configured or DEFAULT_AGENT_LOG_DIR


def normalize_log_mode(value):
    return (value or 'off').strip().lower()


def agent_logs_enabled(log_mode):
    return normalize_log_mode(log_mode) in VALID_LOG_MODES[1:]


def split_agent_args(args):
    agent = "claude"
    step_label = None
    log_mode = "off"
    failure_log_mode = "on"
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
        forwarded.append(arg)
        i += 1
    if agent not in ("claude", "codex"):
        print(f"ERROR: unsupported agent '{agent}' (expected 'claude' or 'codex')", file=sys.stderr)
        sys.exit(1)
    return agent, step_label, log_mode, failure_log_mode, forwarded


def build_bash_command(agent, forwarded_args, log_mode, env_values=None):
    if env_values is None:
        env_values = os.environ
    args_str = ' '.join(shlex.quote(arg) for arg in forwarded_args)
    if agent == "codex":
        return f"codex exec --sandbox danger-full-access {args_str}"

    output_format = env_values.get('CLAUDE_SAFE_OUTPUT_FORMAT', 'text').strip() or 'text'
    if agent_logs_enabled(log_mode):
        output_format = 'stream-json'
    use_jq_raw = env_values.get('CLAUDE_SAFE_USE_JQ')
    use_jq = True if use_jq_raw is None else use_jq_raw.strip().lower() in ('1', 'true', 'yes', 'on')
    jq_filter = env_values.get('CLAUDE_SAFE_JQ_FILTER', '.result // .')
    stream_capture_path = env_values.get('CLAUDE_STREAM_JSON_CAPTURE', '').strip()

    base_cmd = (
        f"claude -p --output-format {shlex.quote(output_format)}"
        f" --dangerously-skip-permissions {args_str}"
    )

    if output_format != 'stream-json':
        return base_cmd

    # Stream mode is more informative when verbose event logs are enabled.
    stream_cmd = (
        f"claude -p --verbose --output-format stream-json"
        f" --dangerously-skip-permissions {args_str}"
    )
    if stream_capture_path:
        tee_cmd = f"{stream_cmd} | tee {shlex.quote(stream_capture_path)}"
        if use_jq and shutil.which('jq'):
            return f"set -o pipefail; {tee_cmd} | jq -r {shlex.quote(jq_filter)}"
        return f"set -o pipefail; {tee_cmd}"
    if use_jq and shutil.which('jq'):
        return f"set -o pipefail; {stream_cmd} | jq -r {shlex.quote(jq_filter)}"
    return stream_cmd


def should_echo_output(step_label, rc):
    mode = os.environ.get('AGENT_STDIO_ECHO', 'auto').strip().lower()
    if mode in ('1', 'true', 'yes', 'on'):
        return True
    if mode in ('0', 'false', 'no', 'off'):
        return rc != 0
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


def build_verbose_log_path(agent, model, step_label, ts=None):
    step_label = safe_label(step_label or 'run')
    model_label = safe_label(model)
    if ts is None:
        ts = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    agent_log_dir = resolve_agent_log_dir()
    return os.path.join(agent_log_dir, f"{ts}_{step_label}_{agent}_{model_label}.log")


def write_verbose_log(agent, model, step_label, log_mode, rc, stdout_text, stderr_text, stream_json_text="", log_path=None):
    if not agent_logs_enabled(log_mode):
        return

    step_label = safe_label(step_label or 'run')
    if log_path is None:
        log_path = build_verbose_log_path(agent, model, step_label)
    payload = (
        f"timestamp_utc: {datetime.now(timezone.utc).isoformat(timespec='seconds')}\n"
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
    ts = datetime.now(timezone.utc).isoformat(timespec='seconds')
    snippet_lines = error_text.strip().splitlines()[-20:]
    snippet = '\n'.join(snippet_lines) if snippet_lines else '(no output captured)'
    failure_record = (
        f"[{ts}] agent={agent} model={model} exit_code={rc}\n"
        f"{snippet}\n"
        f"{'-' * 72}\n"
    )
    agent_log_dir = resolve_agent_log_dir()
    write_log(os.path.join(agent_log_dir, "agent-failure.log"), failure_record)
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: agent_wrapper.py [agent arguments...]", file=sys.stderr)
        sys.exit(1)

    agent, step_label, log_mode, failure_log_mode, forwarded_args = split_agent_args(sys.argv[1:])

    env = os.environ.copy()
    if agent == "claude":
        # Avoid nested Claude Code session guard failures when tests invoke Claude
        # from within another Claude-hosted runtime.  Clear all CLAUDE* env vars
        # that may trigger nested session detection.
        for key in list(env):
            if key.startswith("CLAUDE") or key == "CLAUDECODE":
                env.pop(key, None)
    stream_capture_path = None
    if agent == "claude" and agent_logs_enabled(log_mode):
        # When agent logs are enabled, force stream-json and capture the raw stream.
        env['CLAUDE_SAFE_OUTPUT_FORMAT'] = 'stream-json'
        fd, stream_capture_path = tempfile.mkstemp(prefix='ralph-stream-json-', suffix='.log')
        os.close(fd)
        env['CLAUDE_STREAM_JSON_CAPTURE'] = stream_capture_path

    args = forwarded_args
    model = "unknown"
    for i, arg in enumerate(args):
        if arg == '--model' and i + 1 < len(args):
            model = args[i + 1]
            break

    # Build the command for the selected agent.
    bash_command = build_bash_command(agent, forwarded_args, log_mode, env)

    live_log_path = None
    if agent_logs_enabled(log_mode):
        live_log_path = build_verbose_log_path(agent, model, step_label)
        write_log(
            live_log_path,
            (
                f"timestamp_utc: {datetime.now(timezone.utc).isoformat(timespec='seconds')}\n"
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
