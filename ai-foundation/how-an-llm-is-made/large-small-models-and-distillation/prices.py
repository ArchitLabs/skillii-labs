# Prices in US dollars per million tokens (input, output), as of 27 November 2026.
# Source: https://platform.claude.com/docs/en/about-claude/pricing
# Claude Haiku 5.5's price is the one for prompts up to 100,000 tokens. Prices change: check the page first.
PRICES = {"claude-haiku-5-5": (0.10, 0.50), "claude-opus-5-5": (4.00, 20.00)}


def cost(model, input_tokens, output_tokens):
    """What a request cost, in dollars, from the token counts it reports."""
    price_in, price_out = PRICES[model]
    return (input_tokens * price_in + output_tokens * price_out) / 1_000_000
