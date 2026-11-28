# One fact hidden in a long list, moved from the start to the end. Can the model still find it?
import random
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
rng = random.Random(46)  # a fixed seed: the same list on every run
others = rng.sample([n for n in range(1000, 10000) if n != 7319], 1000)
lines = [f"Locker {n} holds code {rng.randint(1000, 9999)}." for n in others]
fact = "Locker 7319 holds code 4862."
question = "What code does locker 7319 hold? Reply with the code only."
replies, found = [], 0


def ask(where, at):
    global found
    text_in = "\n".join(lines[:at] + [fact] + lines[at:]) + "\n\n" + question
    reply = client.messages.create(model="claude-haiku-4-5", max_tokens=20,
                                   messages=[{"role": "user", "content": text_in}])
    text = " ".join(next((b.text for b in reply.content if b.type == "text"), "").split())
    hit = "4862" in text
    print(f"{where:<7} line {at + 1:>4} of {len(lines) + 1}  {'found' if hit else 'missed':<6}  {text}")
    replies.append(reply)
    found += hit


print(f"input: {len(lines) + 1} lines, the question after them")
print(f"question: {question}")
for where, share in [("start", 0), ("25%", 0.25), ("middle", 0.5), ("75%", 0.75), ("end", 1)]:
    ask(where, round(len(lines) * share))

print(f"input tokens, all 5 requests: {sum(r.usage.input_tokens for r in replies)}")
print(f"found: {found} of 5")
spent = sum(cost(r.usage.input_tokens, r.usage.output_tokens) for r in replies)
print(f"cost: ${spent:.6f}")
