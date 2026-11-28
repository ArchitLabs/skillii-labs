# How LLM Tool Calling Works: The Model Only Asks

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *How LLM Tool Calling Works: The Model Only Asks*.

`clock.py` uses the Anthropic Python SDK to show that a model never runs a tool itself. It offers Claude Opus 5.5 one
tool, `get_time`, and asks what time it is in Mumbai. A model has no clock, so:

1. **The model asks.** Its first reply stops with `stop_reason` `tool_use`, and holds a `tool_use` block: the tool's
   name and a JSON input, written by the model as data. The script prints that block (its name and input).
2. **Your code runs the tool.** `get_time` is ordinary Python on your computer: it reads the clock for the time zone
   the model named.
3. **The result goes back.** A second request sends the result in a `tool_result` block, and the model writes its
   answer from it.

Each reply prints its `stop_reason` and its input and output tokens, and the script prints what the two requests
cost. Prices in `prices.py` are Claude Opus 5.5's, as of 28 November 2026:
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them. The round
trip is described in Anthropic's [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works).

| Script | What it shows | Cost to run |
|---|---|---|
| `clock.py` | A tool call written by the model, run by your code, and answered from its result | under a cent on a typical run (two paid requests; the recorded run below prints its cost) |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python clock.py
```

The time, the token counts and the cost will differ on your run.

## Recorded run

<!-- skillii-kit:run clock -->
Recorded run of `python clock.py` (28 Nov 2026):

```text
question: What time is it in Mumbai right now? Answer in one short sentence.
reply: stop_reason tool_use, input 419, output 55
the model wrote: {"type": "tool_use", "name": "get_time", "input": {"timezone": "Asia/Kolkata"}}
my code ran get_time: Saturday 28 November 2026, 10:29
reply: stop_reason end_turn, input 497, output 30
the model answered: It's 10:29 on Saturday, 28 November 2026 in Mumbai.
total cost: $0.005364
```

One run cost $0.005364 at the prices in the code.
<!-- /skillii-kit:run clock -->
