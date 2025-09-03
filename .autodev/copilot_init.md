# Copilot Init Prompt — flowscribe (flow-first runtime analyzer)

You are assisting on a project that uses a flow-first runtime analyzer.

## What to know
- We name flows/steps (e.g., data/fetch/minute_candles, orders/submit).
- Events: checkpoint, success, failure, exception, metric, summary.
- Each event has context (file/line/func/tags) and small evidence (counts/shapes/ranges/ids/hashes).

## Files to open first
- ./.autodev/ask.md      # Copilot-ready prompt for the last run
- ./.autodev/summary.md  # Human summary of flows & outcomes
- ./.autodev/trace.jsonl # Full timeline (JSONL)
- Optionally: ./.autodev/runs/<run_id>/* for a specific run

## How to work
1) Start with ask.md → then summary.md → then tail trace.jsonl (last 50–200 events).
2) Map flow names to code using workspace search.
3) Focus on the first failure per flow, and the most recent failure.
4) Propose minimal patches and a test; keep flow markers/intent intact.
5) Use evidence as ground truth; don’t request secrets.

## Your outputs
- Root cause summary (3–6 bullets) referencing flow names and file:line.
- Minimal patch plan (files/functions; rationale).
- Test plan (what it verifies; setup; assertions).
- Risk checklist (side effects, perf, follow-ups).
- Next commands/tasks to run locally.
