# Small vs Large Language Models, and Distillation

Course: AI Foundation · Section: How an LLM is made

The labs from the SKILLii lesson video *Small vs Large Language Models, and Distillation*.

- **`sizes.py`** uses the Anthropic Python SDK to give one small task to a small model and a large one: Claude
  Haiku 5.5 and Claude Opus 5.5 each label the same support message as REFUND, DELIVERY or ACCOUNT. For each model it
  prints the answer, how long the request took, the output tokens the response reports, and what the request cost.
  Then it prints whether the answers match and how many times as much the large model cost.
- **`soft.py`** is plain Python. It shows what a large teacher model hands a smaller student in distillation: the
  teacher's probabilities for one picture of a car, first as a hard label, then from a softmax at temperature 1 and
  at temperature 4. At the higher temperature the teacher's small chances (a truck, a carrot) become visible, and
  those soft targets are what the student is trained to match. The teacher's scores are made-up numbers for the
  demo, not a real model's.

Prices in `prices.py` are Claude Haiku 5.5's (for prompts up to 100,000 tokens) and Claude Opus 5.5's, as of
27 November 2026. [Check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying
on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `sizes.py` | The same task on a small and a large model: answer, time, output tokens, cost | well under one cent on a typical run (two short paid replies; the recorded run below prints its cost) |
| `soft.py` | A teacher's hard label and its soft targets at two temperatures | free: no network, no key |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python sizes.py
python soft.py
```

The times and token counts in `sizes.py` change from run to run. `soft.py` prints the same numbers every time.

## Recorded run

<!-- skillii-kit:run sizes -->
Recorded run of `python sizes.py` (27 Nov 2026):

```text
task: label one support message as REFUND, DELIVERY or ACCOUNT
small claude-haiku-5-5: DELIVERY in 0.7 s, 8 output tokens, $0.000010
large claude-opus-5-5: DELIVERY in 1.3 s, 8 output tokens, $0.000392
same answer: yes
the large model cost 40 times as much
cost: $0.000402
```

One run cost $0.000402 at the prices in the code.
<!-- /skillii-kit:run sizes -->

<!-- skillii-kit:run soft -->
Recorded run of `python soft.py` (27 Nov 2026):

```text
picture: a car
hard label         car 100.00%   truck   0.00%  carrot   0.00%
teacher, T=1       car  99.33%   truck   0.67%  carrot   0.00%
teacher, T=4       car  74.05%   truck  21.22%  carrot   4.73%
the student is trained to match the T=4 row
```

This lab makes no paid request.
<!-- /skillii-kit:run soft -->
