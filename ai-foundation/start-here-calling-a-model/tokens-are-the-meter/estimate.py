# What will it cost to run? Price one real request, then multiply it out to a month.
# The token counts come from the API. The team's numbers below are yours to change.
from pathlib import Path

import anthropic
from prices import cost

ENGINEERS, REQUESTS_PER_DAY, WORKDAYS = 50, 40, 22

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
guide = (Path(__file__).parent / "team-style-guide.md").read_text()
system = [{"type": "text", "text": guide, "cache_control": {"type": "ephemeral"}}]
ask = [{"role": "user", "content": "Review this line in one sentence: x=1;y = 2"}]
spent = 0

for attempt in (1, 2):  # the first request writes the cache, the second reads it
    u = client.messages.create(model="claude-opus-5-5", max_tokens=1000,
                               system=system, messages=ask).usage
    spent += cost(u.input_tokens, u.output_tokens,
                  u.cache_creation_input_tokens, u.cache_read_input_tokens)

no_cache = cost(u.input_tokens + u.cache_read_input_tokens, u.output_tokens)
cached = cost(u.input_tokens, u.output_tokens, 0, u.cache_read_input_tokens)
month = ENGINEERS * REQUESTS_PER_DAY * WORKDAYS
print(f"one request: {u.output_tokens} output tokens, {u.cache_read_input_tokens} read from cache")
print(f"requests a month: {month:,}")
print(f"without caching: about ${no_cache * month:,.0f} a month")
print(f"with caching:    about ${cached * month:,.0f} a month")
print(f"cost: ${spent:.6f}")
