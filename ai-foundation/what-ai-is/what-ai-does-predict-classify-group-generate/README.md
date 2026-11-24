# What Can AI Do? Predict, Classify, Group, Generate

Course: AI Foundation · Section: What AI is, how it began, how it is built

The labs from the SKILLii lesson video *What Can AI Do? Predict, Classify, Group, Generate*. Each script is one
kind of output a model can give:

| Script | What it shows | Cost to run |
|---|---|---|
| `predict.py` | **Predict a number** (regression): days with known ice-cream sales go in, a straight line is fitted, and it predicts a new day's sales | free |
| `classify.py` | **Pick a category** (binary classification): days labelled rain or no rain go in; for a new day the five most similar days vote, giving a likelihood and a category | free |
| `group.py` | **Find groups** (clustering, with k-means): customers with no labels go in, and the script groups the similar ones. It does not name the groups | free |
| `generate.py` | **Generate new content** (generative AI): the same request goes to a model twice, and each reply is new text | a fraction of a cent |

The data in the first three scripts is made up, small enough to read on one screen. Those three use only Python
itself: no library, no network, no key.

`generate.py` uses the [Anthropic Python SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) and
prints what its two requests cost, from the token counts in each response and the prices in `prices.py`: Claude
Opus 5.5's, as of 24 November 2026. [Check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
before relying on them.

No script creates anything or leaves anything to tidy up.

## Run it

```bash
python predict.py
python classify.py
python group.py

pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key; never write it into a file
python generate.py
```

The first three print the same thing on every run. The model's words in `generate.py` will differ from run to run.

## Recorded run

<!-- skillii-kit:run predict -->
Recorded run of `python predict.py` (24 Nov 2026):

```text
learned: about 5.74 more ice creams for each degree
prediction for 26 C: 138 ice creams
```

This lab makes no paid request.
<!-- /skillii-kit:run predict -->

<!-- skillii-kit:run classify -->
Recorded run of `python classify.py` (24 Nov 2026):

```text
humidity 45%: no rain (likelihood of rain 0.2)
humidity 68%: rain (likelihood of rain 0.6)
humidity 85%: rain (likelihood of rain 0.8)
```

This lab makes no paid request.
<!-- /skillii-kit:run classify -->

<!-- skillii-kit:run group -->
Recorded run of `python group.py` (24 Nov 2026):

```text
group 1: customers 1, 4, 7 (about 2 visits, $83 a visit)
group 2: customers 5, 8, 9 (about 12 visits, $14 a visit)
group 3: customers 2, 3, 6 (about 6 visits, $41 a visit)
the groups have no names: what each one means is yours to decide
```

This lab makes no paid request.
<!-- /skillii-kit:run group -->

<!-- skillii-kit:run generate -->
Recorded run of `python generate.py` (24 Nov 2026):

```text
run 1: Know before you go.
run 2: Know before you go.
cost: $0.000584
```

One run cost $0.000584 at the prices in the code.
<!-- /skillii-kit:run generate -->
