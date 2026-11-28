# LLM Temperature and Sampling Explained

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *LLM Temperature and Sampling Explained*. Before a model writes its next token,
it gives every token in its vocabulary a score. Softmax turns those scores into probabilities that add up to 100%, and
the temperature changes their shape first: a low temperature piles almost everything on the top token, a high one
spreads it out. Top-k and top-p trim the list of candidates, and then one token is drawn at random.

| Script | What it shows | Cost to run |
|---|---|---|
| `sample.py` | Takes five example scores for the next token after "The sky is", turns them into probabilities at temperatures 0.2, 1.0 and 2.0, trims the list with top-k 2 and top-p 0.9, and draws eight tokens at each temperature with the same fixed random numbers | free |

The scores are made-up example numbers, not a real model's: a real model scores every token in its vocabulary, and
five are enough to see the idea. The script uses only Python itself: nothing to install, no key, no sign-in, no
network. It saves nothing, so there is nothing to tidy up. Its random draws use a fixed seed, so every run prints the
same. It pauses half a second before each line, so you can read the output one line at a time.

## Run it

```bash
python sample.py
```

## Recorded run

<!-- skillii-kit:run sample -->
Recorded run of `python sample.py` (28 Nov 2026):

```text
scores     blue 5.0  clear 4.0  dark 3.0  grey 2.0  green 0.0
temp 0.2   blue 99.3%  clear 0.7%  dark 0.0%  grey 0.0%  green 0.0%
temp 1.0   blue 64.1%  clear 23.6%  dark 8.7%  grey 3.2%  green 0.4%
temp 2.0   blue 43.9%  clear 26.6%  dark 16.1%  grey 9.8%  green 3.6%
top-k 2    blue 73.1%  clear 26.9%
top-p 0.9  blue 66.5%  clear 24.5%  dark 9.0%
draw 0.2   blue blue blue blue blue blue blue blue
draw 1.0   blue blue clear blue blue blue blue blue
draw 2.0   blue blue clear blue clear blue blue clear
```

This lab makes no paid request.
<!-- /skillii-kit:run sample -->
