# The loop, run by hand: ask for one token, add it to the text, ask again.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
text = "The quick brown fox jumps"
spent = 0.0

for step in range(1, 6):
    reply = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1,  # one new token, then stop
        messages=[
            {"role": "user", "content": "Finish this sentence in plain words."},
            {"role": "assistant", "content": text.rstrip()},  # the text so far
        ],
    )
    spent += cost(reply.usage.input_tokens, reply.usage.output_tokens)
    token = "".join(b.text for b in reply.content if b.type == "text")
    if not token.strip():  # no visible token: say why, and stop
        print(f"step {step}: no visible token (stop_reason: {reply.stop_reason})")
        break
    text += token
    print(f"step {step}: {token!r:<10} {' '.join(text.split())}")

print(f"cost: ${spent:.6f}")
