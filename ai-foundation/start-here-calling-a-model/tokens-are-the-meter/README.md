# How LLM Pricing Works: Input vs Output Tokens

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The labs from the SKILLii lesson video *How LLM Pricing Works: Input vs Output Tokens*.
Prices in `prices.py` are Claude Opus 5.5's, as of November 2026 — [check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `count.py` | Count a question's tokens before sending it | free |
| `ask.py` | One real request: count, send, read `usage`, price both sides, and show the reply's blocks (thinking, then text) | about $0.004 |
| `chat.py` | Three turns of one chat: the input grows every turn, because the whole history is sent again | about $0.01 |
| `cache.py` | The same long instructions (`team-style-guide.md`) sent twice with prompt caching: the first writes the cache, the second reads it | about $0.02 |
| `estimate.py` | Answer "what will it cost to run?": price one real request with and without caching, then multiply it out to a month for your team (edit the numbers at the top) | about $0.03 |

Set `SKILLII_MODEL` to use another model your account has.

## What the video recorded (17–18 November 2026, claude-opus-5-5)

```
$ python3 count.py
counted before sending: 24

$ python3 ask.py
counted before sending: 24
input_tokens: 24
output_tokens: 173
cost: $0.003556
blocks in the reply: thinking, text
answer: Output tokens cost more because they must be generated one at a time, each requiring its own
        full pass through the model, whereas input tokens can all be processed together in a
        single parallel pass that uses the hardware far more efficiently.

$ python3 chat.py
turn 1: input_tokens 18, output_tokens 104
turn 2: input_tokens 139, output_tokens 126
turn 3: input_tokens 286, output_tokens 58

$ python3 cache.py
request 1: cache write 3077, cache read 0, input 18
  cost: $0.016657
request 2: cache write 0, cache read 3077, input 18
  cost: $0.001887

$ python3 estimate.py
one request: 168 output tokens, 3077 read from cache
requests a month: 44,000
without caching: about $694 a month
with caching:    about $179 a month
```

Your numbers will differ a little run to run: the model's output length (and its thinking) varies. The caching
estimate assumes requests come often enough to keep the cache warm — a cache entry lasts five minutes.

Why so many output tokens for a one-sentence answer? The model thinks before it answers, and thinking tokens are
billed as output — the `usage` count includes them even though you don't see them in the reply.
