# AI vs Machine Learning vs Deep Learning vs Generative AI

Course: AI Foundation · Section: What AI is, how it began, how it is built

The labs from the SKILLii lesson video *AI vs Machine Learning vs Deep Learning vs Generative AI*. One customer
message, "This doesn't fit. Can I send it back?", is handled two ways:

| Script | What it shows | Cost to run |
|---|---|---|
| `draft.py` | **Generative AI**: one call to a model makes new content, a draft reply to the customer | a fraction of a cent |
| `act.py` | **Agentic AI**: a model chooses each next step toward a goal (look up the order, open the return, email the customer) and the code carries each step out | a few cents |

`act.py` calls the tools in `shop.py`, a stand-in for a shop's own order, returns and email software. The stand-in
changes nothing real: it only returns made-up results, so the lab creates nothing and leaves nothing to tidy up.

Both scripts use the [Anthropic Python SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) and
print what their requests cost, from the token counts in each response and the prices in `prices.py`: Claude Opus
5.5's, as of 20 November 2026. [Check the pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
before relying on them.

## Run it

```bash
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key; never write it into a file
python draft.py
python act.py
```

The model's words, and the steps `act.py` takes, will differ a little from run to run.

## Recorded run

<!-- skillii-kit:run draft -->
Recorded run of `python draft.py` (20 Nov 2026):

```text
customer: This doesn't fit. Can I send it back?
draft reply: Hi there,  Sorry to hear it doesn't fit! Yes, you can send it back. Returns are **free
             within 30 days** of receiving your order.  If you'd like a different size
             instead, just let us know and we'll be happy to help.  Thanks, [Your Name]
input_tokens: 53, output_tokens: 199
cost: $0.004192
```

One run cost $0.004192 at the prices in the code.
<!-- /skillii-kit:run draft -->

<!-- skillii-kit:run act -->
Recorded run of `python act.py` (22 Nov 2026):

```text
step 1: get_order {"order_id": "4417"}
        -> {"order_id": "4417", "item": "linen shirt, size M", "delivered_days_ago": 6}
step 2: create_return {"order_id": "4417", "reason": "Doesn't fit"}
        -> {"return_id": "R-4417", "label": "ready to print"}
step 3: email_customer {"order_id": "4417", "text": "Hi! We've opened a free return for [...]
        -> {"sent": true}
step 4: done
        Yes, you can send it back. Your linen shirt (size M) arrived 6 days ago, so it's
        well within our 30-day free return window.  - **Return ID:** R-4417 - **Return
        label:** Ready to print. I've emailed you the details.  Pack the shirt, put the
        label on, and drop it off with the carrier. If you'd like a different size
        instead, tell me and I can help with that.
cost: $0.021560
```

One run cost $0.02156 at the prices in the code.
<!-- /skillii-kit:run act -->
