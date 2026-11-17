# Count a question's tokens before sending it. The count is free.
import os

import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = os.environ.get("SKILLII_MODEL", "claude-opus-5-5")
question = "In one sentence: why do output tokens cost more?"

count = client.messages.count_tokens(
    model=MODEL,
    messages=[{"role": "user", "content": question}],
)
print(f"counted before sending: {count.input_tokens}")
