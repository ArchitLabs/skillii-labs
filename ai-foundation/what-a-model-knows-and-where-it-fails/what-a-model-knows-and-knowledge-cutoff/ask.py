# What does the model know? One question, asked alone, then with a dated fact placed in the request.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
question = "When will Claude Opus 4.5 be retired on the Claude API? Answer in one short sentence."
fact = "On November 23, 2026, Anthropic set Claude Opus 4.5's retirement date: January 22, 2027."


def ask(label, content):
    reply = client.messages.create(
        model="claude-opus-5-5", max_tokens=300, messages=[{"role": "user", "content": content}])
    text = " ".join(next((b.text for b in reply.content if b.type == "text"), "").split())
    print(f"{label:<13} input_tokens {reply.usage.input_tokens:>3}  {text}")
    return reply


print(f"question: {question}")
alone = ask("no context", question)
dated = ask("with the fact", fact + "\n\n" + question)

spent = sum(cost(r.usage.input_tokens, r.usage.output_tokens) for r in (alone, dated))
print(f"cost: ${spent:.6f}")
