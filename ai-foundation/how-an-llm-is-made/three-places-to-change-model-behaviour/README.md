# 3 Ways to Change What an LLM Does

Course: AI Foundation · Section: How an LLM is made

The lab from the SKILLii lesson video *3 Ways to Change What an LLM Does*.

- **`three_ways.py`** uses the Anthropic Python SDK to ask Claude Haiku 5.5 one question three ways, without
  touching the model's weights:
  1. the question alone;
  2. the question with an instruction in the prompt (answer in one sentence of at most 15 words, or say you do not
     know);
  3. the same instruction and question, with a short document placed in the context ahead of them.

  The question is about a made-up shop's returns policy, so no model learned the answer in training. In a real
  retrieval-augmented generation (RAG) system a retriever would find the document; here it is pasted in by hand.
  For each request the script prints the input and output tokens the response reports, what the request cost, and
  the first 66 characters of the answer. Output tokens include any thinking the model did.

Prices in `prices.py` are Claude Haiku 5.5's (for prompts up to 100,000 tokens), as of 27 November 2026.
[Check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `three_ways.py` | The same question as a bare question, with an instruction, and with a document in the context: tokens, cost, answer | well under one cent (three short paid replies; the recorded run below prints its cost) |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python three_ways.py
```

The answers and token counts change from run to run.

## Recorded run

<!-- skillii-kit:run ways -->
Recorded run of `python three_ways.py` (27 Nov 2026):

```text
question: How many days do I have to return a Ravelli desk lamp?
1 question only: 28 input tokens, 345 output tokens, $0.000175
  I don't have Ravelli's return policy, and it depends on where y...
2 + instruction: 54 input tokens, 66 output tokens, $0.000038
  I don't know Ravelli's return window; please check their websit...
3 + document: 90 input tokens, 26 output tokens, $0.000022
  You have 45 days from delivery to return a Ravelli desk lamp.
cost: $0.000236
```

One run cost $0.000236 at the prices in the code.
<!-- /skillii-kit:run ways -->
