# What fills a context window? Count each part of one request, then send it.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-opus-5-5"
window = client.models.retrieve(MODEL).max_input_tokens
print(f"window: {MODEL}, max_input_tokens {window:,}")

system = "You support engineers on a cloud platform. Answer in one short sentence."
tools = [{"name": "get_quota", "description": "Look up the monthly token quota of a team.",
          "input_schema": {"type": "object", "properties": {"team": {"type": "string"}}}}]
history = [{"role": "user", "content": "Our team is called Atlas."},
           {"role": "assistant", "content": "Hello, team Atlas. How can I help?"}]
question = {"role": "user", "content": "What is a context window? One sentence."}


def count(label, **parts):
    tokens = client.messages.count_tokens(model=MODEL, **parts).input_tokens
    print(f"{label:<18}{tokens:>6}")


count("message only", messages=[question])
count("+ system prompt", system=system, messages=[question])
count("+ tool definition", system=system, tools=tools, messages=[question])
count("+ earlier turns", system=system, tools=tools, messages=history + [question])

reply = client.messages.create(model=MODEL, max_tokens=1000, system=system, tools=tools,
                               messages=history + [question])
usage = reply.usage
print(f"sent: input_tokens {usage.input_tokens}, output_tokens {usage.output_tokens}")
print(f"used: {usage.input_tokens + usage.output_tokens:,} of {window:,}")
print(f"cost: ${cost(usage.input_tokens, usage.output_tokens):.6f}")
