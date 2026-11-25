# The same long instructions, sent twice with prompt caching on.
# The first request writes the cache; the second one reads it.
import time
from pathlib import Path

import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
guide = (Path(__file__).parent / "team-style-guide.md").read_text()
guide = f"Loaded at {time.time()}\n" + guide  # a new first line: every run starts with an empty cache
system = [{"type": "text", "text": guide,
           "cache_control": {"type": "ephemeral"}}]
spent = 0

for attempt in (1, 2):
    reply = client.messages.create(
        model="claude-opus-5-5", max_tokens=300, system=system,
        messages=[{"role": "user", "content": "Name rule 1. Ten words."}])
    u = reply.usage
    dollars = cost(u.input_tokens, u.output_tokens,
                   u.cache_creation_input_tokens, u.cache_read_input_tokens)
    spent += dollars
    print(f"request {attempt}: cache write {u.cache_creation_input_tokens:>4}, "
          f"cache read {u.cache_read_input_tokens:>4}, input {u.input_tokens}, ${dollars:.6f}")

print(f"cost: ${spent:.6f}")
