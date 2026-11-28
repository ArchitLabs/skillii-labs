# One model, two kinds of task: a contest-style math puzzle and three analog clocks. Code checks every answer.
import base64
import re

import anthropic
from clock import draw_clock
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
replies = []


def ask(content):
    reply = client.messages.create(model="claude-sonnet-5-5", max_tokens=8000,
                                   messages=[{"role": "user", "content": content}])
    replies.append(reply)
    return next((b.text for b in reply.content if b.type == "text"), "")


def row(task, said, true, ok):
    print(f"{task:<24}{said:<8}{true:<8}{'right' if ok else 'wrong'}")


print(f"{'task':<24}{'model':<8}{'true':<8}result")

# The hard task: a math puzzle. Python works out the true answer exactly.
puzzle = "What are the last three digits of 7 to the power 2026? End with a line: Answer: <number>"
said = re.findall(r"Answer:\s*\**\s*(\d+)", ask(puzzle))
true = pow(7, 2026, 1000)
row("math: 7^2026 mod 1000", said[-1] if said else "?", str(true), bool(said) and int(said[-1]) == true)

# The easy task: read three analog clocks. The code drew them, so it knows each time.
prompt = "What time does this analog clock show? Reply with the time only, like 3:25."
clocks_right = 0
for k, (h, m) in enumerate([(4, 47), (8, 23), (11, 38)], 1):
    png = base64.standard_b64encode(draw_clock(h, m)).decode()
    reply = ask([{"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": png}},
                 {"type": "text", "text": prompt}])
    said = re.search(r"(\d{1,2}):(\d{2})", reply)
    ok = bool(said) and int(said[1]) % 12 == h % 12 and int(said[2]) == m
    clocks_right += ok
    row(f"clock {k}", said[0] if said else "?", f"{h}:{m:02d}", ok)

print(f"clocks read right: {clocks_right} of 3")
spent = sum(cost(r.usage.input_tokens, r.usage.output_tokens) for r in replies)
print(f"cost: ${spent:.6f}")
