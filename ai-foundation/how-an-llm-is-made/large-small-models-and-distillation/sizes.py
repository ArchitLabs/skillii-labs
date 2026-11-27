# One task, two model sizes: a small model and a large model label the same support message.
import time
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
SMALL, LARGE = "claude-haiku-5-5", "claude-opus-5-5"
TASK = """Label this support message REFUND, DELIVERY or ACCOUNT. Reply with the label only.

My parcel was due on Monday and still has not come."""


def ask(model):
    start = time.perf_counter()
    reply = client.messages.create(
        model=model, max_tokens=2000, messages=[{"role": "user", "content": TASK}]
    )
    seconds = time.perf_counter() - start
    text = " ".join("".join(b.text for b in reply.content if b.type == "text").split())
    return text, seconds, reply.usage


print("task: label one support message as REFUND, DELIVERY or ACCOUNT")
answers, costs = [], []
for size, model in (("small", SMALL), ("large", LARGE)):
    text, seconds, usage = ask(model)
    answers.append(text)
    costs.append(cost(model, usage.input_tokens, usage.output_tokens))
    print(f"{size} {model}: {text} in {seconds:.1f} s, {usage.output_tokens} output tokens, ${costs[-1]:.6f}")

print("same answer:", "yes" if answers[0] == answers[1] else "no")
print(f"the large model cost {costs[1] / costs[0]:.0f} times as much")
print(f"cost: ${sum(costs):.6f}")
