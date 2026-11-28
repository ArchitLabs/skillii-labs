# Thinking Tokens: The Hidden Cost of Reasoning Models

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *Thinking Tokens: The Hidden Cost of Reasoning Models*.

`effort.py` uses the Anthropic Python SDK to show what a model's thinking costs, and how `max_tokens` and the effort
setting change it. It asks Claude Opus 5.5 one counting question three times:

- **Low effort**, with room to spare (`max_tokens` 16000).
- **High effort**, the same question and the same room.
- **High effort with a small cap** (`max_tokens` 50), far too small for the thinking.

For each reply it prints the `stop_reason`, the input and output tokens, how many of the output tokens were thinking
(`usage.output_tokens_details.thinking_tokens`), the answer the model wrote, and what the request cost. Thinking
tokens are billed as output tokens, so the cost is worked out from `output_tokens`, thinking included. Python works
out the right answer itself, so you can check each reply.

Prices in `prices.py` are Claude Opus 5.5's, as of 28 November 2026:
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them. How
`max_tokens` and effort bound thinking is described in Anthropic's
[Steering thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost) guide.

| Script | What it shows | Cost to run |
|---|---|---|
| `effort.py` | The same question at low and high effort, and with a cap too small for the thinking | a few cents on a typical run (three paid replies; the recorded run below prints its cost) |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python effort.py
```

The model decides how much to think on each request, so your token counts and cost will differ from run to run.

## Recorded run

<!-- skillii-kit:run effort -->
Recorded run of `python effort.py` (28 Nov 2026):

```text
question: How many numbers from 1 to 99999 have digits that add up to 25? Reply with only the number.
right answer (worked out by Python): 5631
effort low, max_tokens 16000: stop_reason end_turn
input 40, output 144 (thinking 140), answer: 5631, cost $0.003040
effort high, max_tokens 16000: stop_reason end_turn
input 40, output 209 (thinking 205), answer: 5631, cost $0.004340
effort high, max_tokens 50: stop_reason max_tokens
input 40, output 50 (thinking 50), answer: (none), cost $0.001160
total cost: $0.008540
```

One run cost $0.00854 at the prices in the code.
<!-- /skillii-kit:run effort -->
