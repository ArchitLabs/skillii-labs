# A tool call is text the model writes. Your code runs the tool and sends the result back.
import json
from datetime import datetime
from zoneinfo import ZoneInfo

import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-opus-5-5"
QUESTION = "What time is it in Mumbai right now? Answer in one short sentence."
ZONE = {"type": "string", "description": "An IANA time zone name, e.g. Europe/London"}
TOOLS = [{
    "name": "get_time",
    "description": "Get the current local date and time in a time zone.",
    "input_schema": {"type": "object", "properties": {"timezone": ZONE}, "required": ["timezone"]},
}]


def get_time(timezone):  # the tool: ordinary code, run on this computer
    return datetime.now(ZoneInfo(timezone)).strftime("%A %d %B %Y, %H:%M")


def ask(messages):
    reply = client.messages.create(
        model=MODEL, max_tokens=1024, tools=TOOLS, messages=messages,
        tool_choice={"type": "auto", "disable_parallel_tool_use": True},  # at most one call
    )
    used = reply.usage
    print(f"reply: stop_reason {reply.stop_reason}, input {used.input_tokens}, output {used.output_tokens}")
    return reply, cost(used.input_tokens, used.output_tokens)


print("question:", QUESTION)
messages = [{"role": "user", "content": QUESTION}]
reply, total = ask(messages)  # 1. the model replies with a request, not a time
call = next(block for block in reply.content if block.type == "tool_use")
print("the model wrote:", json.dumps({"type": call.type, "name": call.name, "input": call.input}))
result = get_time(**call.input)  # 2. your code runs the tool
print(f"my code ran {call.name}: {result}")
messages += [
    {"role": "assistant", "content": reply.content},
    {"role": "user", "content": [{"type": "tool_result", "tool_use_id": call.id, "content": result}]},
]
reply, spent = ask(messages)  # 3. the result goes back, and the model answers
answer = " ".join("".join(block.text for block in reply.content if block.type == "text").split())
print("the model answered:", answer[:100])
print(f"total cost: ${total + spent:.6f}")
