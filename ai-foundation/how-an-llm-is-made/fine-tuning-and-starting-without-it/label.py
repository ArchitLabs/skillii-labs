# The same support message, labelled twice: prompt only, then with rules and examples in the prompt.
import re
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-haiku-4-5"
MESSAGE = "My parcel was due on Monday and still has not come. I need it for a wedding on Saturday."
HOUSE = re.compile(r"^\[(REFUND|DELIVERY|ACCOUNT)\] (low|medium|high) :: .+$")

# The house format, taught in the prompt: three rules and three worked examples.
RULES = """Label each support message in one line: [LABEL] priority :: summary.
LABEL is REFUND, DELIVERY or ACCOUNT. priority is low, medium or high.
The summary has at most eight words.

I was charged twice for the same jacket.
[REFUND] medium :: charged twice for one jacket

I cannot log in since I changed my phone number.
[ACCOUNT] medium :: login fails after phone change

Where is my order? It has been three weeks.
[DELIVERY] medium :: order three weeks late
"""


def label(prompt):
    reply = client.messages.create(
        model=MODEL, max_tokens=60, messages=[{"role": "user", "content": prompt}]
    )
    text = " ".join("".join(b.text for b in reply.content if b.type == "text").split())
    return text, reply.usage


print("message:", MESSAGE)
spent, sizes = 0.0, []
for name, prompt in (
    ("prompt only", f"Label this support message.\n\n{MESSAGE}"),
    ("rules + 3 examples", f"{RULES}\n{MESSAGE}"),
):
    text, usage = label(prompt)
    print(f"{name}: {usage.input_tokens} input tokens")
    print("reply:", text if len(text) <= 70 else f"{text[:60]}... ({len(text)} chars)")
    print("house format:", "yes" if HOUSE.match(text) else "no")
    sizes.append(usage.input_tokens)
    spent += cost(usage.input_tokens, usage.output_tokens)

# The examples are sent, and billed as input, on every request. Tuning is one way to remove them.
print(f"examples add {sizes[1] - sizes[0]} input tokens to every request")
print(f"cost: ${spent:.6f}")
