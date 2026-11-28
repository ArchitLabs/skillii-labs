# Why Temperature 0 Still Gives Different Answers

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *Why Temperature 0 Still Gives Different Answers*. At temperature 0 a model
always picks the word with the highest score, so you might expect the same answer every time. But a computer adds
decimal numbers with a tiny rounding step, and adding the same numbers in a different order can give a slightly
different sum. When two words are nearly tied, that tiny difference decides which one comes out on top. On a real
server, how the work is split depends on how many requests are being processed together, so the order can change from
one call to the next.

| Script | What it shows | Cost to run |
|---|---|---|
| `order.py` | Adds 0.1, 0.2 and 0.3 in two orders and prints both sums, then gives two words the same three made-up score parts (a tie on paper) and shows that the way the adding is split decides which word a temperature-0 pick takes | free: plain Python, no network, no key |

The script calls nothing and saves nothing, so there is nothing to tidy up. The two words and their scores are made
up for the demo; a real model scores every token in its vocabulary. Python's built-in `sum()` is not used
on purpose: since Python 3.12 it adds floats with extra care, which would hide the effect, so the script adds one
number at a time, as a simple loop does.

## Run it

```
python order.py
```

## Recorded run

<!-- skillii-kit:run order -->
Recorded run of `python order.py` (28 Nov 2026):

```text
(0.1 + 0.2) + 0.3 = 0.6000000000000001
0.1 + (0.2 + 0.3) = 0.6
in one go:   Paris 0.6000000000000001  Lyon 0.6  -> picks Paris
split up:    Paris 0.6  Lyon 0.6000000000000001  -> picks Lyon
```

This lab makes no paid request.
<!-- /skillii-kit:run order -->
