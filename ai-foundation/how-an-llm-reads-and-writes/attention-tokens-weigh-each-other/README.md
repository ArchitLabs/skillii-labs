# Attention in LLMs Explained, Without the Math

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *Attention in LLMs Explained, Without the Math*. Attention lets each word in a
sentence weigh the other words when the model works out what it means. The classic test is the word "it" in a
sentence pair from Google Research's 2017 Transformer post: "The animal didn't cross the street because it was too
tired" and the same sentence ending in "wide". Most people read "it" as the animal in the first and the street in the
second, and the only clue is one word that comes after "it".

| Script | What it shows | Cost to run |
|---|---|---|
| `it.py` | Uses the Anthropic Python SDK to ask Claude Haiku 5.5 what "it" refers to in each sentence of the pair, prints both answers, whether changing one word changed the answer, and what the two requests cost | well under one cent on a typical run (two short paid replies; the recorded run below prints its cost) |

The script only sends two API requests: it creates nothing and saves nothing, so there is nothing to tidy up. It
shows what attention makes possible, the answer changing with a word later in the sentence; it does not print the
model's attention weights, which the API does not expose.

Prices in `prices.py` are Claude Haiku 5.5's (for prompts up to 100,000 tokens), as of 27 November 2026.
[Check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python it.py
```

## Recorded run

<!-- skillii-kit:run it -->
Recorded run of `python it.py` (27 Nov 2026):

```text
sentence: The animal didn't cross the street because it was too tired.
"it" refers to: animal
sentence: The animal didn't cross the street because it was too wide.
"it" refers to: street
one word changed, and so did the answer: yes
cost: $0.000028
```

One run cost $2.8e-05 at the prices in the code.
<!-- /skillii-kit:run it -->
