# AI Wins Olympiad Gold, Still Misreads Clocks

Course: AI Foundation · Section: What a model knows, and where it fails

The lab from the SKILLii lesson video *AI Wins Olympiad Gold, Still Misreads Clocks*. Google DeepMind
[reports](https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)
gold-medal level at the International Mathematical Olympiad, while on [ClockBench](https://clockbench.ai/) many models
still misread analog clocks. This lab tries the same contrast on a small scale, on your own key: one model, one hard
task and one easy-looking one, every answer checked by code.

| Script | What it shows | Cost to run |
|---|---|---|
| `ask.py` | **Hard task or easy task?** With the Anthropic Python SDK, it asks Claude Sonnet 5.5 for the last three digits of 7 to the power 2026, a contest-style puzzle, and Python's `pow` works out the true answer. Then it shows the same model three analog clocks that `clock.py` draws, and asks the time on each. The code drew the clocks, so it knows each time. For every task it prints the model's answer, the true answer and whether they match; then how many clocks the model read right, and what the four requests cost | a few cents |
| `clock.py` | Draws a plain clock face (a rim, a tick for every minute, a heavier mark at 12, a short hour hand and a long minute hand) as a PNG image in memory, with nothing but Python's standard library | free |

A clock counts as read right only when the hour and the minute both match exactly. The math answer counts as right
only when it matches Python's.

Whatever the model answers is what the run prints: a model that reads every clock right, or misses the puzzle, is a
true result too. Run it a few times and compare. The code's answers are the same every time.

Prices in `prices.py` are Claude Sonnet 5.5's, as of 28 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

The script creates nothing and leaves nothing to tidy up: the clock images live only in memory.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python ask.py
```

The model's replies may differ from run to run.

## Recorded run

<!-- skillii-kit:run ask -->
Recorded run of `python ask.py` (28 Nov 2026):

```text
task                    model   true    result
math: 7^2026 mod 1000   649     649     right
clock 1                 4:47    4:47    right
clock 2                 8:23    8:23    right
clock 3                 11:38   11:38   right
clocks read right: 3 of 3
cost: $0.016256
```

One run cost $0.016256 at the prices in the code.
<!-- /skillii-kit:run ask -->
