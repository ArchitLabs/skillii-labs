# What Is a Context Window? One Token Budget

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The lab from the SKILLii lesson video *What Is a Context Window? One Token Budget*.

`budget.py` uses the Anthropic Python SDK to show what fills one model's context window.

- **The window.** It asks the Models API for Claude Opus 5.5's `max_input_tokens`, the size of its window.
- **What fills it.** It builds one request part by part (the user's question, then a system prompt, then a tool
  definition, then two earlier turns) and counts the tokens after each part with the free token counting endpoint.
- **The output counts too.** It sends the full request once and prints the input and output tokens the response
  reports, how many of the window the request used, and what it cost.

Prices in `prices.py` are Claude Opus 5.5's, as of 26 November 2026 —
[check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.
Claude Opus 5.5 thinks adaptively, and its thinking tokens count as output.

| Script | What it shows | Cost to run |
|---|---|---|
| `budget.py` | The window size, the tokens each part of a request adds, and the input and output of one real request against the window | well under one cent on a typical run (one paid request, at most about $0.03) |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python budget.py
```

Your counts may differ a little from run to run, and the output tokens will.

## Recorded run

<!-- skillii-kit:run budget -->
Recorded run of `python budget.py` (26 Nov 2026):

```text
window: claude-opus-5-5, max_input_tokens 1,000,000
message only          19
+ system prompt       43
+ tool definition    397
+ earlier turns      426
sent: input_tokens 426, output_tokens 58
used: 484 of 1,000,000
cost: $0.002864
```

One run cost $0.002864 at the prices in the code.
<!-- /skillii-kit:run budget -->
