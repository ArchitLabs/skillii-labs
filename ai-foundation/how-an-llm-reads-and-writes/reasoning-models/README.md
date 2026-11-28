# Reasoning Models Explained: Why They Think First

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *Reasoning Models Explained: Why They Think First*. A reasoning model can work
through a problem before it answers. This lab asks one model the same multi-step question twice, a five-digit by
five-digit multiplication, first with thinking off and then with thinking on, and puts the two replies side by side.

| Script | What it shows | Cost to run |
|---|---|---|
| `think.py` | Uses the Anthropic Python SDK to ask Claude Haiku 5.5 "What is 73,846 times 59,217?" with `thinking={"type": "disabled"}` and then with `thinking={"type": "adaptive", "display": "summarized"}`. For each reply it prints the answer, whether it matches the product Python works out, the start of the thinking summary that came before the answer, the output tokens and the seconds the request took, then what the two requests cost | well under one cent on a typical run (the recorded run below prints its cost) |

The script only sends two API requests: it creates nothing and saves nothing, so there is nothing to tidy up.

What you see of the thinking is a summary the API returns (`display: "summarized"`), not the model's full reasoning.
With thinking on, the model decides for itself how much to think, so your token counts, timings and summary will
differ from the recorded run. Output tokens include the thinking tokens.

Prices in `prices.py` are Claude Haiku 5.5's (for prompts up to 100,000 tokens), as of 28 November 2026.
[Check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python think.py
```

## Recorded run

<!-- skillii-kit:run think -->
Recorded run of `python think.py` (28 Nov 2026):

```text
question: What is 73,846 times 59,217? Reply with only the number.
right answer (worked out by Python): 4,372,938,582
thinking off| answer: 4,373,855,782
thinking off| correct: no
thinking off| thought first: (nothing)
thinking off| output tokens: 9 | seconds: 1.9
thinking on | answer: 4,372,938,582
thinking on | correct: yes
thinking on | thought first: I'm splitting the multiplication into 73,846 × 59,
thinking on | output tokens: 267 | seconds: 4.1
cost: $0.000144
```

One run cost $0.000144 at the prices in the code.
<!-- /skillii-kit:run think -->
