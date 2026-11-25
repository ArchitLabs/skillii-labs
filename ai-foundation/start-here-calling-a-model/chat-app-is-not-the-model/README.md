# AI Chat App vs the Model Behind It

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The lab from the SKILLii lesson video *AI Chat App vs the Model Behind It*.

`ask.py` asks Claude Opus 5.5 the same question twice with the Anthropic Python SDK: "What is today's date?". The
first request is the bare model, with no system prompt. The second adds one line of system prompt, "The current date
is ...", the kind of line a chat app puts in front of every conversation. It prints both replies, the input tokens of
each request (the system prompt is input too) and what the two requests cost together.

Prices in `prices.py` are Claude Opus 5.5's, as of 25 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `ask.py` | One question sent bare and with a date line in the system prompt: both replies, the input tokens of each, the cost | well under one cent |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python ask.py
```

Anthropic publishes the system prompts its Claude apps use, and states that they do not apply to the Claude API
([System prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/overview)). A request to the API
carries only what your code puts in it, so anything the app supplies, such as today's date, your code has to supply.

Your replies will differ a little from run to run, and the date line uses your computer's date.

## Recorded run

<!-- skillii-kit:run ask -->
Recorded run of `python ask.py` (25 Nov 2026):

```text
no system prompt: I don't have access to real-time information, so I can't know today's date; please check your device's clock or calendar.
with the date line: Today is Wednesday, 25 November 2026.
input_tokens: 24 and 43
cost: $0.001708
```

One run cost $0.001708 at the prices in the code.
<!-- /skillii-kit:run ask -->
