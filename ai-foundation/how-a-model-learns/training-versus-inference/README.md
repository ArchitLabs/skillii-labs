# Training vs Inference in AI: What's the Difference?

Course: AI Foundation · Section: How a model learns

The lab from the SKILLii lesson video *Training vs Inference in AI: What's the Difference?*. Training sets a model's
numbers from data, once. Inference uses the finished model on new inputs, many times over, and leaves its numbers
as they are. As [Dive into Deep Learning](https://d2l.ai/chapter_introduction/index.html) puts it: "Once training
finishes and the weights are frozen, running the model forward on new inputs is called inference".

| Script | What it shows | Cost to run |
|---|---|---|
| `train_and_serve.py` | A one-line model, `fare = w * km + b`, trained once on ten made-up taxi trips (5,000 passes, 50,000 small updates), then called on a million new trips, one call each. It prints how long training took, how long one call takes, how long all the calls took together, and that the model's numbers did not change while it served | free |

The script uses only Python itself: no library, no network, no key. It creates nothing and leaves nothing to tidy
up. The taxi fares are made up (30 rupees plus 12 per km).

## Run it

```bash
python train_and_serve.py
```

The counts and the learned numbers are the same on every run; the times depend on your machine.

## Recorded run

<!-- skillii-kit:run serve -->
Recorded run of `python train_and_serve.py` (26 Nov 2026):

```text
training: 5000 passes over 10 trips = 50,000 updates in 21.3 ms, done once
learned: w = 12.00, b = 30.00
inference: 1,000,000 new trips, one call each, 0.09 microseconds per call
all 1,000,000 calls together: 89.8 ms
a 7.5 km trip: fare = 120.00
after 1,000,000 calls the numbers are still: w = 12.00, b = 30.00
```

This lab makes no paid request.
<!-- /skillii-kit:run serve -->
