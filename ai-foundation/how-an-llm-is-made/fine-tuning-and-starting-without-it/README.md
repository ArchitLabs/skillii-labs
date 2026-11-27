# Fine-Tuning an LLM: Why Most Teams Start Without It

Course: AI Foundation · Section: How an LLM is made

The lab from the SKILLii lesson video *Fine-Tuning an LLM: Why Most Teams Start Without It*.

`label.py` uses the Anthropic Python SDK to try the cheap route first: teach a model a house format in the prompt,
with no fine-tuning at all.

- **Prompt only.** It asks Claude Haiku 4.5 to label one support message, with no rules and no examples. The reply
  comes back in the model's own words, and the script's check says it is not in the house format,
  `[LABEL] priority :: summary`.
- **Rules and three examples in the prompt.** It sends the same message after three rules and three worked
  examples (few-shot prompting). The reply comes back in the house format, and the check says so.
- **What the examples cost.** It prints how many more input tokens the second prompt used. Those examples are sent,
  and billed as input tokens, on every request. Removing them from the prompt is one of the things fine-tuning is
  for.

A reply longer than 70 characters is printed as its first 60 characters, then `...` and its full length, so the
whole run fits on one screen; the `...` is the script's, not the model's.

Prices in `prices.py` are Claude Haiku 4.5's, as of 27 November 2026.
[Check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) before relying on them.

| Script | What it shows | Cost to run |
|---|---|---|
| `label.py` | One message labelled without and with examples in the prompt, the format check, and the examples' extra input tokens | under one cent on a typical run (two short paid replies; the recorded run below prints its cost) |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python label.py
```

Your token counts should match closely from run to run; the replies' wording will differ.

## Recorded run

<!-- skillii-kit:run label -->
Recorded run of `python label.py` (27 Nov 2026):

```text
message: My parcel was due on Monday and still has not come. I need it for a wedding on Saturday.
prompt only: 35 input tokens
reply: # Support Message Label **Category:** Delivery Issue / Late ... (242 chars)
house format: no
rules + 3 examples: 147 input tokens
reply: [DELIVERY] high :: parcel late, needed for saturday wedding
house format: yes
examples add 112 input tokens to every request
cost: $0.000567
```

One run cost $0.000567 at the prices in the code.
<!-- /skillii-kit:run label -->
