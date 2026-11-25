# How LLMs Write: Next-Token Prediction Explained

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The labs from the SKILLii lesson video *How LLMs Write: Next-Token Prediction Explained*.

A language model writes one token at a time: it predicts the next token from all the text so far, adds it, and
repeats until it ends its turn or reaches a limit. Inside one API request the model runs that loop for you. These
three short scripts, each using the Anthropic Python SDK and Claude Haiku 4.5, let you watch it from the outside.

| Script | What it shows | Cost to run |
|---|---|---|
| `loop.py` | The loop run by hand: five requests, each asking for one token (`max_tokens=1`) and continuing the text so far, starting from "The quick brown fox jumps". Each step prints the new token and the text it grew. If a reply holds no visible token, the script prints its `stop_reason` and stops. | well under one cent |
| `stop.py` | Why a reply ends: one reply ends on its own (`stop_reason: end_turn`); the other is cut off by `max_tokens=10` (`stop_reason: max_tokens`). | well under one cent |
| `again.py` | The same request sent three times. Each run picks its own next tokens, so the three endings can differ. | well under one cent |

Each script prints its own cost, from the token counts the API reports and the prices in `prices.py`: Claude Haiku
4.5's, as of 26 November 2026 — [check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
before relying on them.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python loop.py
python stop.py
python again.py
```

Why Claude Haiku 4.5: `loop.py` hands the model "the text so far" as the start of its own reply (a *prefill*, the
last `assistant` message) and asks it to continue. Claude Haiku 4.5 accepts a prefill when thinking is off, which is
its default; newer models such as Claude Haiku 5.5 reject a prefill. Claude Haiku 4.5 is an active model on the
Claude API as of 26 November 2026.

What to expect: your tokens and endings may differ from the recorded run, because each request samples its next
tokens. In `loop.py`, each step is a whole new request that carries the text so far; the API does not keep it
between requests.

## Recorded run

<!-- skillii-kit:run loop -->
Recorded run of `python loop.py` (26 Nov 2026):

```text
step 1: ' over'    The quick brown fox jumps over
step 2: ' the'     The quick brown fox jumps over the
step 3: ' lazy'    The quick brown fox jumps over the lazy
step 4: ' dog'     The quick brown fox jumps over the lazy dog
step 5: ' because' The quick brown fox jumps over the lazy dog because
cost: $0.000140
```

One run cost $0.00014 at the prices in the code.
<!-- /skillii-kit:run loop -->

<!-- skillii-kit:run stop -->
Recorded run of `python stop.py` (26 Nov 2026):

```text
reply: The cat sat on the **windowsill**.
stop_reason: end_turn
output_tokens: 13
reply: # Why the Sky is Blue The sky appears
stop_reason: max_tokens
output_tokens: 10
cost: $0.000154
```

One run cost $0.000154 at the prices in the code.
<!-- /skillii-kit:run stop -->

<!-- skillii-kit:run again -->
Recorded run of `python again.py` (26 Nov 2026):

```text
run 1: The robot opened the door and saw ...nothing but darkness. Its optical sensors whirred
run 2: The robot opened the door and saw the girl standing there, drenched from head to toe
run 3: The robot opened the door and saw nothing but fog. The fog was thick and cold,
cost: $0.000234
```

One run cost $0.000234 at the prices in the code.
<!-- /skillii-kit:run again -->
