# The same question, sent to the model twice: once bare, once with a date line like a chat app's system prompt.
import datetime
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
question = [{"role": "user", "content": "What is today's date? Answer in one short sentence."}]

bare = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    messages=question,
)

today = datetime.date.today().strftime("%A, %d %B %Y")
app = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    system=f"The current date is {today}.",
    messages=question,
)


def text(reply):
    return " ".join(next((b.text for b in reply.content if b.type == "text"), "").split())


print("no system prompt:", text(bare))
print("with the date line:", text(app))
print(f"input_tokens: {bare.usage.input_tokens} and {app.usage.input_tokens}")
spent = sum(cost(r.usage.input_tokens, r.usage.output_tokens) for r in (bare, app))
print(f"cost: ${spent:.6f}")
