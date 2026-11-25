# Do AI Models Remember Your Chat? (They Don't)

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The lab from the SKILLii lesson video *Do AI Models Remember Your Chat? (They Don't)*.

`remember.py` talks to Claude Opus 5.5 with the Anthropic Python SDK in two ways.

- **Separate requests.** Request 1 tells the model a name. Request 2, a new request, asks for that name. Request 2
  carries only its own message, so the model has nothing to answer from.
- **One conversation.** The same question again, but this time the code sends request 1's message and the model's
  reply back with it. Turn 3 adds one more question on top of the whole history.

For each request it prints the input tokens the response reports, so you can see the input grow as the history is
sent again, and at the end what all four requests cost together.

Prices in `prices.py` are Claude Opus 5.5's, as of 26 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `remember.py` | Two separate requests, then the same question with the history sent back: each reply, the input tokens of each request, the cost | well under one cent |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python remember.py
```

Your replies will differ a little from run to run.

## Recorded run

<!-- skillii-kit:run remember -->
Recorded run of `python remember.py` (26 Nov 2026):

```text
Separate requests: each one sends only its own message
request 1  input_tokens   33  Nice to meet you, Priya, and good luck learning model APIs!
request 2  input_tokens   23  I don't know your name since you haven't shared it with me.
One conversation: each turn sends the whole history again
turn 2     input_tokens   75  Your name is Priya.
turn 3     input_tokens  103  You're learning model APIs.
cost: $0.002836
```

One run cost $0.002836 at the prices in the code.
<!-- /skillii-kit:run remember -->
