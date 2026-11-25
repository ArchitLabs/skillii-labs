# What Happens When You Message an AI Model?

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The lab from the SKILLii lesson video *What Happens When You Message an AI Model?*

`ask.py` sends one real request to Claude Opus 5.5 with the Anthropic Python SDK. The request holds three things:
the instructions (`system`), the earlier messages of the conversation, and the new message. It prints what came
back: the reply's text, the kinds of block in the reply, the tokens that went in and came out (`usage`), and what
the request cost.

Prices in `prices.py` are Claude Opus 5.5's, as of 25 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `ask.py` | One request (instructions, earlier messages, new message) and its response: the text, the blocks, `input_tokens`, `output_tokens` and the cost | well under one cent |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python ask.py
```

The new message, "How long will that take?", only makes sense because the earlier messages travel with it: the
API keeps nothing between requests, so the application sends the whole conversation every time.

Your numbers will differ a little from run to run: the reply's length varies, and Claude Opus 5.5 may think before
it answers. Thinking tokens are billed as output tokens, so `output_tokens` can be larger than the visible reply.

## Recorded run

<!-- skillii-kit:run ask -->
Recorded run of `python ask.py` (25 Nov 2026):

```text
reply: About 15 minutes if your rice is already cooked, or around 40 minutes if you need to cook it first.
blocks in the reply: thinking, text
input_tokens: 64
output_tokens: 87
cost: $0.001996
```

One run cost $0.001996 at the prices in the code.
<!-- /skillii-kit:run ask -->
