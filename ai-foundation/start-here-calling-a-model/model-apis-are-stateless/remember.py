# Does the model remember you? Separate requests, then one conversation that sends the history back.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
replies = []


def ask(label, messages):
    reply = client.messages.create(model="claude-opus-5-5", max_tokens=300, messages=messages)
    replies.append(reply)
    text = " ".join(next((b.text for b in reply.content if b.type == "text"), "").split())
    print(f"{label:<10} input_tokens {reply.usage.input_tokens:>4}  {text}")
    return {"role": "assistant", "content": text}


hello = {"role": "user", "content": "My name is Priya and I am learning model APIs. Reply in one sentence."}
name = {"role": "user", "content": "What is my name? Answer in one short sentence."}
topic = {"role": "user", "content": "What am I learning? Answer in one short sentence."}

print("Separate requests: each one sends only its own message")
answer = ask("request 1", [hello])
ask("request 2", [name])

print("One conversation: each turn sends the whole history again")
history = [hello, answer, name]  # turn 1 is request 1, sent back with its reply
history.append(ask("turn 2", history))
history.append(topic)
ask("turn 3", history)

spent = sum(cost(r.usage.input_tokens, r.usage.output_tokens) for r in replies)
print(f"cost: ${spent:.6f}")
