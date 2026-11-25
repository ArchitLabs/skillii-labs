# How LLM Pricing Works: Input vs Output Tokens

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The labs from the SKILLii lesson video *How LLM Pricing Works: Input vs Output Tokens*. Each one talks to Claude
Opus 5.5 with the Anthropic Python SDK, reads the token counts the response reports in `usage`, and prices them.

Prices in `prices.py` are Claude Opus 5.5's, as of 26 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `ask.py` | One request: count the question before sending it, send it, and price the input side and the output side apart | about $0.004 |
| `chat.py` | Three turns of one chat: the input grows every turn, because the whole history is sent again | about $0.01 |
| `cache.py` | The same long instructions (`team-style-guide.md`) sent twice with prompt caching: the first request writes the cache, the second reads it | about $0.02 |
| `estimate.py` | What will it cost to run? Price one real request with and without caching, then multiply it out to a month for a team (edit the numbers at the top) | about $0.03 |
| `count.py` | Count a question's tokens before sending it (not in the video) | free |

Each paid script prints what its own run cost on its last line.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python ask.py
python chat.py
python cache.py
python estimate.py
```

Your numbers will differ a little from run to run: the model's output length, and its thinking, vary. Thinking
tokens are billed as output, so `output_tokens` counts them even though the reply does not show them. The caching
estimate assumes requests come often enough to keep the cache warm: a 5-minute cache entry is refreshed by each hit.

## Recorded run

<!-- skillii-kit:run ask -->
Recorded run of `python ask.py` (26 Nov 2026):

```text
counted before sending: 24
input_tokens:    24 x $4.00 per million = $0.000096
output_tokens:  178 x $20.00 per million = $0.003560
cost: $0.003656
blocks in the reply: thinking, text
answer: Output tokens cost more because they must be generated one at a time, each requiring its own
        memory-bandwidth-bound pass through the model, whereas input tokens are processed
        together in a single, highly parallel pass that uses the GPU far more efficiently.
```

One run cost $0.003656 at the prices in the code.
<!-- /skillii-kit:run ask -->

<!-- skillii-kit:run chat -->
Recorded run of `python chat.py` (26 Nov 2026):

```text
turn 1: input_tokens   18, output_tokens  119, $0.002452
turn 2: input_tokens  154, output_tokens  128, $0.003176
turn 3: input_tokens  303, output_tokens  107, $0.003352
cost: $0.008980
```

One run cost $0.00898 at the prices in the code.
<!-- /skillii-kit:run chat -->

<!-- skillii-kit:run cache -->
Recorded run of `python cache.py` (26 Nov 2026):

```text
request 1: cache write 3092, cache read    0, input 18, $0.018852
request 2: cache write    0, cache read 3092, input 18, $0.001730
cost: $0.020582
```

One run cost $0.020582 at the prices in the code.
<!-- /skillii-kit:run cache -->

<!-- skillii-kit:run estimate -->
Recorded run of `python estimate.py` (26 Nov 2026):

```text
one request: 179 output tokens, 3077 read from cache
requests a month: 44,000
without caching: about $703 a month
with caching:    about $189 a month
cost: $0.009043
```

One run cost $0.009043 at the prices in the code.
<!-- /skillii-kit:run estimate -->
