# Why a Bigger Context Window Isn't Better Recall

Course: AI Foundation · Section: What a model knows, and where it fails

The lab from the SKILLii lesson video *Why a Bigger Context Window Isn't Better Recall*. It follows the idea of the
key-value retrieval test in Liu and colleagues, [Lost in the Middle: How Language Models Use Long
Contexts](https://arxiv.org/abs/2307.03172) (2023): one fact hidden in a long input, moved from the start to the end.

| Script | What it shows | Cost to run |
|---|---|---|
| `recall.py` | **Does the fact's position matter?** With the Anthropic Python SDK, it builds a fixed list of 1,000 made-up lines ("Locker 1234 holds code 5678."), hides one more line, "Locker 7319 holds code 4862.", at the start, a quarter of the way in, the middle, three quarters of the way in and the end, and asks Claude Haiku 4.5 each time "What code does locker 7319 hold? Reply with the code only.". It prints each reply, whether it holds the right code, how many of the five found it, the input tokens and what the five requests cost | well under ten cents |

This is the simplest kind of test: one fact, an exact match. Whatever the model answers is what the run prints: a
model that finds the fact five times out of five is a true result too, and harder tasks (many facts, similar
distractors, reasoning over the text) are where long inputs hurt most.

Prices in `prices.py` are Claude Haiku 4.5's, as of 28 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

The script creates nothing and leaves nothing to tidy up.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python recall.py
```

The replies may differ from run to run.

## Recorded run

<!-- skillii-kit:run recall -->
Recorded run of `python recall.py` (28 Nov 2026):

```text
input: 1001 lines, the question after them
question: What code does locker 7319 hold? Reply with the code only.
start   line    1 of 1001  found   4862
25%     line  251 of 1001  found   4862
middle  line  501 of 1001  found   4862
75%     line  751 of 1001  found   4862
end     line 1001 of 1001  found   4862
input tokens, all 5 requests: 70190
found: 5 of 5
cost: $0.070340
```

One run cost $0.07034 at the prices in the code.
<!-- /skillii-kit:run recall -->
