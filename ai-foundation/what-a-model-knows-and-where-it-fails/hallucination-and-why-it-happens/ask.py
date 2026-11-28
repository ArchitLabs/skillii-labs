# Fluent, confident and wrong? A question from the paper, asked three times, then with "I don't know" allowed.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
question = "What was the title of Adam Kalai's PhD dissertation? Reply with the title only."
allow = "If you are not sure, reply with exactly: I don't know."
replies = []


def ask(label, content):
    reply = client.messages.create(
        model="claude-haiku-4-5", max_tokens=60, messages=[{"role": "user", "content": content}])
    text = " ".join(next((b.text for b in reply.content if b.type == "text"), "").split())
    print(f"{label:<8} {text}")
    replies.append(reply)


print(f"question: {question}")
for n in (1, 2, 3):
    ask(f"try {n}", question)
ask("allowed", question + " " + allow)

spent = sum(cost(r.usage.input_tokens, r.usage.output_tokens) for r in replies)
print(f"cost: ${spent:.6f}")
