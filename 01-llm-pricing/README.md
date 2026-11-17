# 01 — How LLM pricing works: input vs output tokens

The labs from the SKILLii lesson video *How LLM Pricing Works: Input vs Output Tokens*.
Prices in `prices.py` are Claude Opus 5.5's, as of November 2026 — [check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `count.py` | Count a question's tokens before sending it | free |
| `ask.py` | One real request: count, send, read `usage`, price both sides | about $0.003 |
| `chat.py` | Three turns of one chat: the input grows every turn, because the whole history is sent again | about $0.01 |
| `cache.py` | The same long instructions (`team-style-guide.md`) sent twice with prompt caching: the first writes the cache, the second reads it | about $0.02 |

Set `SKILLII_MODEL` to use another model your account has.

## What we recorded (17 November 2026, claude-opus-5-5)

```
$ python3 count.py
counted before sending: 24

$ python3 ask.py
counted before sending: 24
input_tokens: 24
output_tokens: 147
cost: $0.003036

$ python3 chat.py
turn 1: input_tokens 18, output_tokens 108
turn 2: input_tokens 143, output_tokens 84
turn 3: input_tokens 248, output_tokens 74

$ python3 cache.py
request 1: cache write 3077, cache read 0, input 18
  cost: $0.016657
request 2: cache write 0, cache read 3077, input 18
  cost: $0.001887
```

Why so many output tokens for a one-sentence answer? The model thinks before it answers, and thinking tokens are
billed as output — the `usage` count includes them even though you don't see them in the reply.
