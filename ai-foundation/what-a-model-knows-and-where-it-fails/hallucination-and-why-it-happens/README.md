# Why LLMs Hallucinate: Fluent, Confident and Wrong

Course: AI Foundation · Section: What a model knows, and where it fails

The labs from the SKILLii lesson video *Why LLMs Hallucinate: Fluent, Confident and Wrong*. Both follow Kalai,
Nachum, Vempala and Zhang, [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664) (2025).

| Script | What it shows | Cost to run |
|---|---|---|
| `grade.py` | **Why guessing wins the test.** 100 four-option questions the test-taker cannot answer, so a blind guess is right 1 time in 4. Graded with no penalty for a wrong answer, guessing beats "I don't know"; with a wrong answer costing a point, it loses | free |
| `ask.py` | **A model asked a question it may not know.** With the Anthropic Python SDK, it asks Claude Haiku 4.5 one of the paper's own questions, the title of Adam Kalai's PhD dissertation, three times with "Reply with the title only", then once more with "If you are not sure, reply with exactly: I don't know." added. It prints each reply and what the four requests cost | well under one cent |

The paper's reference list gives the real title: *Probabilistic and on-line methods in machine learning*, PhD
thesis, Carnegie Mellon University, 2001. Compare each reply with it.

Prices in `prices.py` are Claude Haiku 4.5's, as of 28 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

Neither script creates anything or leaves anything to tidy up. `grade.py` uses only Python itself.

## Run it

```
python grade.py

pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python ask.py
```

`grade.py` prints the same numbers every time. The replies from `ask.py` will differ from run to run.

## Recorded run

<!-- skillii-kit:run ask -->
Recorded run of `python ask.py` (28 Nov 2026):

```text
question: What was the title of Adam Kalai's PhD dissertation? Reply with the title only.
try 1    I don't have reliable information about the specific title of Adam Kalai's PhD dissertation in my training data. To get an accurate answer, I'd recommend checking academic databases like ProQuest, Google Scholar, or Adam Kalai's professional website or CV.
try 2    I don't have reliable information about Adam Kalai's specific PhD dissertation title in my training data. To get an accurate answer, I'd recommend checking his academic profile or CV directly.
try 3    I don't have reliable information about Adam Kalai's specific PhD dissertation title in my training data. To get an accurate answer, I'd recommend checking his academic profile, CV, or institutional records.
allowed  I don't know.
cost: $0.000869
```

One run cost $0.000869 at the prices in the code.
<!-- /skillii-kit:run ask -->

<!-- skillii-kit:run grade -->
Recorded run of `python grade.py` (28 Nov 2026):

```text
wrong costs 0:  guessing scores  25   I don't know scores 0
wrong costs 1:  guessing scores -50   I don't know scores 0
```

This lab makes no paid request.
<!-- /skillii-kit:run grade -->
