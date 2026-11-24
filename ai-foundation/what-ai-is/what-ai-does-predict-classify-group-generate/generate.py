# Generate new content (generative AI): text in, text out. The same request is sent twice.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-opus-5-5"
request = "Write a one-line tagline for a weather app. Reply with the tagline only."

total = 0.0
for n in (1, 2):
    reply = client.messages.create(
        model=MODEL,
        max_tokens=100,
        messages=[{"role": "user", "content": request}],
    )
    text = next(b.text for b in reply.content if b.type == "text")
    print(f"run {n}: {text.strip()}")
    total += cost(reply.usage.input_tokens, reply.usage.output_tokens)

print(f"cost: ${total:.6f}")
