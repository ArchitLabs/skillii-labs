# Machine Learning vs Traditional Programming

Course: AI Foundation · Section: What AI is, how it began, how it is built

The labs from the SKILLii lesson video *Machine Learning vs Traditional Programming*. The same idea is solved two
ways, with the examples from Google's codelab
[Say hello to the "Hello, World" of machine learning](https://developers.google.com/codelabs/tensorflow-1-helloworld):

| Script | What it shows | Cost to run |
|---|---|---|
| `rules.py` | **Traditional programming**: a person writes the rules (walking, running, biking by speed). Data goes in, answers come out, and no rule can answer "golf" | free |
| `learn.py` | **Machine learning**: data and answers go in, and training works out the rule. Each round predicts, measures the error and adjusts two values a little, as in [Google's gradient descent steps](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent) | free |

Both scripts use only Python itself: no library, no network, no key. They create nothing and leave nothing to tidy
up.

## Run it

```bash
python rules.py
python learn.py
```

`learn.py` starts from the same values every time, so its numbers are the same on every run.

## Recorded run

<!-- skillii-kit:run rules -->
Recorded run of `python rules.py` (24 Nov 2026):

```text
speed 3: walking
speed 8: running
speed 15: biking
speed 3, playing golf: walking
```

This lab makes no paid request.
<!-- /skillii-kit:run rules -->

<!-- skillii-kit:run learn -->
Recorded run of `python learn.py` (24 Nov 2026):

```text
round 1: error 56.5000
round 10: error 6.5255
round 100: error 0.0001
round 500: error 0.0000
learned values: w = 3.0001, b = 0.9998
prediction for x = 10: 31.0004
```

This lab makes no paid request.
<!-- /skillii-kit:run learn -->
