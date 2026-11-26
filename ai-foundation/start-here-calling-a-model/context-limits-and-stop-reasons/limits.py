# Two ways a request fails at the limit: a prompt too long, and an answer cut off.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-haiku-4-5"
window = client.models.retrieve(MODEL).max_input_tokens
LINE = "INFO GET /orders 200 OK in 12 ms\n"


def log_request(lines):
    prompt = LINE * lines + "Summarise this log in two sentences."
    messages = [{"role": "user", "content": prompt}]
    size = client.messages.count_tokens(model=MODEL, messages=messages).input_tokens
    print(f"input: {size:,} tokens, window: {window:,}")
    return messages


# 1. The whole log: more tokens than the window holds.
try:
    client.messages.create(model=MODEL, max_tokens=300, messages=log_request(30_000))
except anthropic.BadRequestError as e:
    print(f"error: {e.status_code} {e.type}")
    print(f"message: {e.api_message}")

# 2. 300 lines fit. Too small a max_tokens cuts the answer off.
messages = log_request(300)
spent = 0.0
for limit in (15, 300):
    reply = client.messages.create(model=MODEL, max_tokens=limit, messages=messages)
    text = " ".join("".join(b.text for b in reply.content if b.type == "text").split())
    print(f"max_tokens {limit}: stop_reason {reply.stop_reason}")
    print("reply:", text if len(text) <= 90 else f"{text[:80]}... ({len(text)} chars)")
    print("finished:", "yes" if reply.stop_reason == "end_turn" else "no, cut off")
    spent += cost(reply.usage.input_tokens, reply.usage.output_tokens)

# The rejected request returned no usage to price, so the cost is the two replies'.
print(f"cost: ${spent:.6f}")
