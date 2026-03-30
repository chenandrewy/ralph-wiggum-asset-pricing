Title: Ralph Loop Rate-Limit Stall
Date: 2026-03-30
Time: 10:07:26 EDT

Iteration 12 of the Ralph loop stalled during test phase around 6:41am EDT. The newest agent logs show several test agents hit a rate limit with the message "You've hit your limit · resets 10am (America/New_York)", but the wrapper then scheduled retries for 2026-04-03 19:01 EDT. Looking further up in the same logs, the stream includes multiple structured rate-limit events with different horizons.

Excerpt from `ralph-garage/agent-logs/20260330T064100.358091-0400_quality-formalism_claude_opus.log`:

```text
[STDOUT]       },
[STDOUT]       "inference_geo": null,
[STDOUT]       "iterations": null,
[STDOUT]       "speed": null
[STDOUT]     },
[STDOUT]     "content": [
[STDOUT]       {
[STDOUT]         "type": "text",
[STDOUT]         "text": "You've hit your limit · resets 10am (America/New_York)"
[STDOUT]       }
[STDOUT]     ],
[STDOUT]     "context_management": null
[STDOUT]   },
[STDOUT]   "parent_tool_use_id": null,
[STDOUT]   "session_id": "299e6501-aee4-4d9b-8823-74d4bc29e633",
[STDOUT]   "uuid": "c697c1af-5c2e-4000-8cbf-5be6aa03ba1d",
[STDOUT]   "error": "rate_limit"
[STDOUT] }
[STDOUT] You've hit your limit · resets 10am (America/New_York)
[WAIT] [agent-wrapper] rate limit for step 'quality-formalism'; waiting until 2026-04-03T19:00:00-04:00 (retry scheduled for 2026-04-03T19:01:00-04:00, sleep 389594.6s)
```

Relevant code from `ralph/agent_wrapper.py`:

```python
def extract_rate_limit_reset_at(stream_json_text):
    if not stream_json_text.strip():
        return None
    for line in stream_json_text.splitlines():
        raw = line.strip()
        if not raw:
            continue
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if payload.get("type") != "rate_limit_event":
            continue
        info = payload.get("rate_limit_info")
        if not isinstance(info, dict):
            continue
        reset_at = info.get("resetsAt")
        if isinstance(reset_at, (int, float)):
            return float(reset_at)
    return None


def maybe_wait_for_rate_limit(stdout_text, stderr_text, stream_json_text, live_log_path, step_label):
    reset_at = get_rate_limit_reset_at(stdout_text, stderr_text, stream_json_text)
    if reset_at is None:
        return False, ""

    now_ts = time.time()
    sleep_seconds = max(0.0, reset_at - now_ts) + RATE_LIMIT_SLEEP_BUFFER_SECONDS
    reset_ny = datetime.fromtimestamp(reset_at, tz=NEW_YORK_TZ)
    wake_ny = datetime.fromtimestamp(now_ts + sleep_seconds, tz=NEW_YORK_TZ)
    message = (
        f"[agent-wrapper] rate limit for step '{safe_label(step_label or 'run')}'; "
        f"waiting until {reset_ny.isoformat(timespec='seconds')} "
        f"(retry scheduled for {wake_ny.isoformat(timespec='seconds')}, "
        f"sleep {sleep_seconds:.1f}s)\n"
    )
    append_live_log(live_log_path, "WAIT", message)
    time.sleep(sleep_seconds)
    return True, message
```

Structured rate-limit entries from the same logs:

From `ralph-garage/agent-logs/20260330T064100.358091-0400_quality-formalism_claude_opus.log`:

```text
[STDOUT] {
[STDOUT]   "type": "rate_limit_event",
[STDOUT]   "rate_limit_info": {
[STDOUT]     "status": "allowed_warning",
[STDOUT]     "resetsAt": 1775257200,
[STDOUT]     "rateLimitType": "seven_day",
[STDOUT]     "utilization": 0.76,
[STDOUT]     "isUsingOverage": false,
[STDOUT]     "surpassedThreshold": 0.75
[STDOUT]   }
[STDOUT] }
```

Later in the same log:

```text
[STDOUT] {
[STDOUT]   "type": "rate_limit_event",
[STDOUT]   "rate_limit_info": {
[STDOUT]     "status": "rejected",
[STDOUT]     "resetsAt": 1774879200,
[STDOUT]     "rateLimitType": "five_hour",
[STDOUT]     "overageStatus": "rejected",
[STDOUT]     "overageDisabledReason": "org_level_disabled",
[STDOUT]     "isUsingOverage": false
[STDOUT]   }
[STDOUT] }
```

From `ralph-garage/agent-logs/20260330T064100.356798-0400_factcheck-theory_claude_opus.log`:

```text
[STDOUT] {
[STDOUT]   "type": "rate_limit_event",
[STDOUT]   "rate_limit_info": {
[STDOUT]     "status": "allowed_warning",
[STDOUT]     "resetsAt": 1774879200,
[STDOUT]     "rateLimitType": "five_hour",
[STDOUT]     "utilization": 0.99,
[STDOUT]     "isUsingOverage": false,
[STDOUT]     "surpassedThreshold": 0.9
[STDOUT]   }
[STDOUT] }
```

And the final rejection in that log:

```text
[STDOUT] {
[STDOUT]   "type": "rate_limit_event",
[STDOUT]   "rate_limit_info": {
[STDOUT]     "status": "rejected",
[STDOUT]     "resetsAt": 1774879200,
[STDOUT]     "rateLimitType": "five_hour",
[STDOUT]     "overageStatus": "rejected",
[STDOUT]     "overageDisabledReason": "org_level_disabled",
[STDOUT]     "isUsingOverage": false
[STDOUT]   }
[STDOUT] }
```

The more plausible bug is that `extract_rate_limit_reset_at()` returns the first `rate_limit_event` it encounters in the captured stream, without checking `status` or `rateLimitType`. In these logs, an early seven-day warning appears before a later five-hour rejection, so the wrapper can sleep on the wrong horizon.
