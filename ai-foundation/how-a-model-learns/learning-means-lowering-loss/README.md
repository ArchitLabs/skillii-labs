# Loss Function Explained: How a Model Learns

Course: AI Foundation · Section: How a model learns

The lab from the SKILLii lesson video *Loss Function Explained: How a Model Learns*. A loss is one number for how
wrong a model's guesses are on its data, and training is the work of making that number smaller. As the
[Stanford CS231n notes](https://cs231n.github.io/linear-classify/) put it: "We are going to measure our unhappiness
with outcomes such as this one with a loss function".

| Script | What it shows | Cost to run |
|---|---|---|
| `loss.py` | A one-knob model, `minutes = w * km`, on three made-up deliveries. It prints the loss (the mean of the squared misses) of three guesses for `w`, where the lowest loss is the best fit; then it trains `w` from 0, step by step, printing the loss after each step, and stops when the loss falls by less than 0.01 in a step: the loss has levelled off, and the run has converged | free |

The script uses only Python itself: nothing to install, no network, no key. It creates nothing and leaves nothing to
tidy up. The deliveries are made up, and their times do not sit exactly on one line, so the loss levels off above zero.
It pauses half a second before each training step, so you can watch the loss fall one line at a time.

## Run it

```bash
python loss.py
```

The data never changes, so the numbers are the same on every run.

## Recorded run

<!-- skillii-kit:run loss -->
Recorded run of `python loss.py` (26 Nov 2026):

```text
guess w = 2.0: loss 104.67
guess w = 3.0: loss 29.67
guess w = 3.5: loss 10.92
start: w = 0, loss 404.67
step 1: loss 104.67
step 2: loss 29.67
step 3: loss 10.92
step 4: loss 6.23
step 5: loss 5.06
step 6: loss 4.76
step 7: loss 4.69
step 8: loss 4.67
step 9: loss 4.67
converged at step 9: learned w = 3.99 minutes per km
```

This lab makes no paid request.
<!-- /skillii-kit:run loss -->
