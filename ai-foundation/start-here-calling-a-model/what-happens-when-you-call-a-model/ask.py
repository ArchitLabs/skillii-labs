# One message to a model: the request your app sends, and the response that comes back.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY

reply = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    system="You help people cook at home. Answer in one short sentence.",
    messages=[
        {"role": "user", "content": "I have rice, eggs and spinach."},
        {"role": "assistant", "content": "You could make egg fried rice with spinach."},
        {"role": "user", "content": "How long will that take?"},
    ],
)

answer = next(b.text for b in reply.content if b.type == "text")
print("reply:", " ".join(answer.split()))
print("blocks in the reply:", ", ".join(b.type for b in reply.content))

usage = reply.usage
print(f"input_tokens: {usage.input_tokens}")
print(f"output_tokens: {usage.output_tokens}")
print(f"cost: ${cost(usage.input_tokens, usage.output_tokens):.6f}")
