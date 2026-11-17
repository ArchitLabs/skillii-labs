# The same long instructions, sent twice with prompt caching on.
# The first request writes the cache; the second one reads it.
import os
from pathlib import Path

import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = os.environ.get("SKILLII_MODEL", "claude-opus-5-5")
guide = (Path(__file__).parent / "team-style-guide.md").read_text()
system = [{"type": "text", "text": guide,
           "cache_control": {"type": "ephemeral"}}]

for attempt in (1, 2):
    reply = client.messages.create(
        model=MODEL, max_tokens=60, system=system,
        messages=[{"role": "user", "content": "Name rule 1. Ten words."}])
    u = reply.usage
    print(f"request {attempt}: cache write {u.cache_creation_input_tokens}, "
          f"cache read {u.cache_read_input_tokens}, input {u.input_tokens}")
    dollars = cost(u.input_tokens, u.output_tokens,
                   u.cache_creation_input_tokens, u.cache_read_input_tokens)
    print(f"  cost: ${dollars:.6f}")
