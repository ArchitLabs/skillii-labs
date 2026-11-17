# Claude Opus 5.5 prices, in US dollars per million tokens, as of November 2026.
# Source: https://platform.claude.com/docs/en/about-claude/pricing
# Prices change. Check the page before you rely on these numbers.
INPUT = 4.00
OUTPUT = 20.00
CACHE_WRITE = 5.00   # writing to the 5-minute cache
CACHE_READ = 0.20    # a cache hit: 5% of the input price


def cost(input_tokens=0, output_tokens=0, cache_write=0, cache_read=0):
    """What a request cost, in dollars, from the token counts it reports."""
    dollars = (input_tokens * INPUT + output_tokens * OUTPUT
               + cache_write * CACHE_WRITE + cache_read * CACHE_READ)
    return dollars / 1_000_000
