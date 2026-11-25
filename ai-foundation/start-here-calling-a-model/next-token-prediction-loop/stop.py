# Why a reply ends: the model ends its turn, or it reaches max_tokens.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
spent = 0.0

for question, limit in [
    ("Finish this sentence in a few words: The cat sat on the", 50),
    ("Explain in one paragraph why the sky is blue.", 10),
]:
    reply = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=limit,
        messages=[{"role": "user", "content": question}],
    )
    text = "".join(b.text for b in reply.content if b.type == "text")
    print("reply:", " ".join(text.split()))
    print("stop_reason:", reply.stop_reason)
    print("output_tokens:", reply.usage.output_tokens)
    spent += cost(reply.usage.input_tokens, reply.usage.output_tokens)

print(f"cost: ${spent:.6f}")
