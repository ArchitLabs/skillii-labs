# Agentic AI: a model chooses each next step toward a goal, and this code carries it out.
import json
import textwrap

import anthropic
from prices import cost
from shop import TOOLS, run_tool

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-opus-5-5"
goal = "Order 4417 doesn't fit. Can I send it back?"
messages = [{"role": "user", "content": goal}]
spent = 0.0

for step in range(1, 7):
    reply = client.messages.create(
        model=MODEL, max_tokens=1500, tools=TOOLS, messages=messages,
        system="You handle returns for a clothing shop. Use the tools to finish the request.",
        tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    )
    spent += cost(reply.usage.input_tokens, reply.usage.output_tokens)
    if reply.stop_reason != "tool_use":
        break
    call = next(b for b in reply.content if b.type == "tool_use")
    result = run_tool(call.name, call.input)
    print(f"step {step}: {call.name} {textwrap.shorten(json.dumps(call.input), 70)}")
    print(f"        -> {result}")
    messages += [
        {"role": "assistant", "content": reply.content},
        {"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": call.id, "content": result}]},
    ]

final = next((b.text for b in reply.content if b.type == "text"), "")
print(f"step {step}: done")
print(textwrap.fill(final, 88, initial_indent="        ", subsequent_indent="        "))
print(f"cost: ${spent:.6f}")
