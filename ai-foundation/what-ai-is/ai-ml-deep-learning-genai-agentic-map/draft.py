# Generative AI: one call to a model that makes new content, a reply to a customer.
import textwrap

import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-opus-5-5"
message = "This doesn't fit. Can I send it back?"

reply = client.messages.create(
    model=MODEL,
    max_tokens=1000,
    system="You draft short, friendly replies for a clothing shop. Returns are free within 30 days.",
    messages=[{"role": "user", "content": message}],
)

draft = next(b.text for b in reply.content if b.type == "text")
print("customer:", message)
print("draft reply:", textwrap.fill(draft, 88, subsequent_indent="             "))

usage = reply.usage
print(f"input_tokens: {usage.input_tokens}, output_tokens: {usage.output_tokens}")
print(f"cost: ${cost(usage.input_tokens, usage.output_tokens):.6f}")
