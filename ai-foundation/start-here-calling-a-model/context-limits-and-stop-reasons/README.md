# LLM Errors: "Prompt Too Long" vs a Cut-Off Answer

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The lab from the SKILLii lesson video *LLM Errors: "Prompt Too Long" vs a Cut-Off Answer*.

`limits.py` uses the Anthropic Python SDK to show the two ways a request can fail at a model's limits, and how each
one comes back.

- **A prompt that does not fit.** It builds a request from a long log, counts its tokens with the token counting endpoint,
  and sends it. The input is larger than the model's context window, so the API rejects the request with an
  error, and no answer comes back.
- **An answer that is cut off.** It sends a shorter log that fits, first with a small `max_tokens`, then with a
  larger one. Both replies come back. The first stops with `stop_reason` `max_tokens`, part way through; the second
  stops with `end_turn`. The script checks the stop reason before treating a reply as finished. A reply longer
  than 90 characters is printed as its first 80 characters, then `...` and its full length, so the whole run fits
  on one screen; the `...` is the script's, not the model's.

It uses Claude Haiku 4.5, whose context window is 200K tokens (see the
[models overview](https://platform.claude.com/docs/en/models/overview)), so the oversized log stays small enough to
send quickly. The script reads the window size from the Models API and prints it.

Prices in `prices.py` are Claude Haiku 4.5's, as of 26 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them. The
rejected request returns no token usage, so the printed cost is that of the two replies.

| Script | What it shows | Cost to run |
|---|---|---|
| `limits.py` | A request rejected as too long, a reply cut off by `max_tokens`, and the same reply finished | under one cent on a typical run (two short paid replies; the recorded run below prints its cost) |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python limits.py
```

Your counts may differ a little from run to run, and the replies will.

## Recorded run

<!-- skillii-kit:run limits -->
Recorded run of `python limits.py` (26 Nov 2026):

```text
input: 420,016 tokens, window: 200,000
error: 400 invalid_request_error
message: prompt is too long: 420032 tokens > 200000 maximum
input: 4,216 tokens, window: 200,000
max_tokens 15: stop_reason max_tokens
reply: # Log Summary The `/orders` endpoint is receiving repeated GET requests that
finished: no, cut off
max_tokens 300: stop_reason end_turn
reply: # Log Summary The `/orders` endpoint is receiving repeated GET requests that con... (295 chars)
finished: yes
cost: $0.008822
```

One run cost $0.008822 at the prices in the code.
<!-- /skillii-kit:run limits -->
