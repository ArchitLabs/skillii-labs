# What Does an LLM Know? Knowledge Cutoff Explained

Course: AI Foundation · Section: What a model knows, and where it fails

The lab from the SKILLii lesson video *What Does an LLM Know? Knowledge Cutoff Explained*.

`ask.py` asks Claude Opus 5.5 one question with the Anthropic Python SDK, twice.

- **No context.** It asks when Claude Opus 4.5 will be retired on the Claude API. Anthropic's models overview gives
  Claude Opus 5.5 a reliable knowledge cutoff of June 2026, and Anthropic's model deprecations page says the
  retirement date (January 22, 2027) was announced on November 23, 2026, so the answer is not in what it learned.
- **With the fact.** The same question, with one dated line from that deprecations notice placed in the request
  before it.
  The model is the same; only the request changed.

For each request it prints the reply and the input tokens the response reports, so you can see what the added line
cost, and at the end what both requests cost together.

Prices in `prices.py` are Claude Opus 5.5's, as of 28 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `ask.py` | One question asked with no context, then with a dated fact in the request: both replies, the input tokens of each, the cost | well under one cent |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python ask.py
```

Your replies will differ a little from run to run.

## Recorded run

<!-- skillii-kit:run ask -->
Recorded run of `python ask.py` (28 Nov 2026):

```text
question: When will Claude Opus 4.5 be retired on the Claude API? Answer in one short sentence.
no context    input_tokens  41  I don't know of an announced retirement date for Claude Opus 4.5, so check Anthropic's official model deprecations page (docs.anthropic.com) for the latest schedule.
with the fact input_tokens  81  According to the announcement you cite, Claude Opus 4.5 will be retired on the Claude API on January 22, 2027, though I can't independently verify this.
cost: $0.004888
```

One run cost $0.004888 at the prices in the code.
<!-- /skillii-kit:run ask -->
