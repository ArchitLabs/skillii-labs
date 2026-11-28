# Why LLMs Can't Count the R's in Strawberry

Course: AI Foundation · Section: What a model knows, and where it fails

The lab from the SKILLii lesson video *Why LLMs Can't Count the R's in Strawberry*. It follows the test in Fu and
colleagues, [Why Do Large Language Models (LLMs) Struggle to Count Letters?](https://arxiv.org/abs/2412.18626) (2024):
ask a model to count every letter in a word as JSON, then compare its answer with the true counts.

| Script | What it shows | Cost to run |
|---|---|---|
| `count.py` | **Model or code?** With the Anthropic Python SDK, it asks Claude Haiku 4.5 to count every letter in four words with repeated letters: strawberry, mississippi, bookkeeper and abracadabra. Python's `collections.Counter` counts the same letters exactly. For each word the script prints the model's count and the code's count for every letter that appears more than once, and whether the model got every letter right; then how many words it got fully right, and what the four requests cost | well under one cent |

Whatever the model answers is what the run prints: a model that counts all four words right is a true result too.
Run it a few times and compare. The code's count is the same every time.

Prices in `prices.py` are Claude Haiku 4.5's, as of 28 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

The script creates nothing and leaves nothing to tidy up.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python count.py
```

The model's replies may differ from run to run.

## Recorded run

<!-- skillii-kit:run count -->
Recorded run of `python count.py` (28 Nov 2026):

```text
word         repeats model/code    every letter
strawberry   r 3/3                 right
mississippi  i 4/4  s 4/4  p 2/2   right
bookkeeper   o 4/2  k 2/2  e 3/3   wrong
abracadabra  a 5/5  b 2/2  r 2/2   right
words with every letter right: 3 of 4
cost: $0.000985
```

One run cost $0.000985 at the prices in the code.
<!-- /skillii-kit:run count -->
