# One question, one model, three ways: the question alone, with an instruction, with a document.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-haiku-5-5"
QUESTION = "How many days do I have to return a Ravelli desk lamp?"
INSTRUCTION = "Answer in one sentence of at most 15 words. If you do not know, say so."
# A made-up shop's policy, so no model learned it in training.
# A RAG system would retrieve it; here it is pasted in by hand.
DOCUMENT = "Ravelli returns policy: desk lamps can be returned within 45 days of delivery."

PROMPTS = {
    "question only": QUESTION,
    "+ instruction": f"{INSTRUCTION}\n\n{QUESTION}",
    "+ document": f"<document>{DOCUMENT}</document>\n\n{INSTRUCTION}\n\n{QUESTION}",
}


def ask(prompt):
    reply = client.messages.create(
        model=MODEL, max_tokens=2000, messages=[{"role": "user", "content": prompt}]
    )
    text = " ".join("".join(b.text for b in reply.content if b.type == "text").split())
    return text, reply.usage


print(f"question: {QUESTION}")
total = 0.0
for n, (way, prompt) in enumerate(PROMPTS.items(), 1):
    text, usage = ask(prompt)
    usd = cost(MODEL, usage.input_tokens, usage.output_tokens)
    total += usd
    tokens = f"{usage.input_tokens} input tokens, {usage.output_tokens} output tokens"
    print(f"{n} {way}: {tokens}, ${usd:.6f}")
    print("  " + (text if len(text) <= 66 else text[:63] + "..."))
print(f"cost: ${total:.6f}")
