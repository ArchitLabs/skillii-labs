# Claude Sonnet 5.5 prices, in US dollars per million tokens, as of 28 November 2026.
# Source: https://platform.claude.com/docs/en/about-claude/pricing
# Prices change. Check the page before you rely on these numbers.
INPUT = 2.00
OUTPUT = 10.00


def cost(input_tokens, output_tokens):
    """What a request cost, in dollars, from the token counts it reports."""
    return (input_tokens * INPUT + output_tokens * OUTPUT) / 1_000_000
