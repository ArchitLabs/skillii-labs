# One real request: count it, send it, and price both sides.
import os
import textwrap

import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = os.environ.get("SKILLII_MODEL", "claude-opus-5-5")
messages = [{"role": "user",
             "content": "In one sentence: why do output tokens cost more?"}]

counted = client.messages.count_tokens(model=MODEL, messages=messages)
print(f"counted before sending: {counted.input_tokens}")

reply = client.messages.create(model=MODEL, max_tokens=400, messages=messages)
usage = reply.usage
print(f"input_tokens: {usage.input_tokens}")
print(f"output_tokens: {usage.output_tokens}")
print(f"cost: ${cost(usage.input_tokens, usage.output_tokens):.6f}")
print("blocks in the reply:", ", ".join(b.type for b in reply.content))
answer = next(b.text for b in reply.content if b.type == "text")
print("answer:", textwrap.fill(answer, 96, subsequent_indent="        "))
