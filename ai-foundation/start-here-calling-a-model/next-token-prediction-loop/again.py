# One request, sent three times: each run picks its own next tokens.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
spent = 0.0

for run in range(1, 4):
    reply = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=12,
        messages=[
            {"role": "user", "content": "Continue this story."},
            {"role": "assistant", "content": "The robot opened the door and saw"},
        ],
    )
    text = "".join(b.text for b in reply.content if b.type == "text")
    story = " ".join(("The robot opened the door and saw" + text).split())
    print(f"run {run}: {story}")
    spent += cost(reply.usage.input_tokens, reply.usage.output_tokens)

print(f"cost: ${spent:.6f}")
