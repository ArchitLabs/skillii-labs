# One real request: count it, send it, read its usage, and price each side.
import textwrap

import anthropic
from prices import INPUT, OUTPUT

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-opus-5-5"
messages = [{"role": "user",
             "content": "In one sentence: why do output tokens cost more?"}]

counted = client.messages.count_tokens(model=MODEL, messages=messages)
print(f"counted before sending: {counted.input_tokens}")

reply = client.messages.create(model=MODEL, max_tokens=1000, messages=messages)
usage = reply.usage
input_cost = usage.input_tokens * INPUT / 1_000_000
output_cost = usage.output_tokens * OUTPUT / 1_000_000
print(f"input_tokens:  {usage.input_tokens:>4} x ${INPUT:.2f} per million = ${input_cost:.6f}")
print(f"output_tokens: {usage.output_tokens:>4} x ${OUTPUT:.2f} per million = ${output_cost:.6f}")
print(f"cost: ${input_cost + output_cost:.6f}")
print("blocks in the reply:", ", ".join(b.type for b in reply.content))
answer = next((b.text for b in reply.content if b.type == "text"), "")
print("answer:", textwrap.fill(" ".join(answer.split()), 96, subsequent_indent="        "))
