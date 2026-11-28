# The same multi-step question, asked twice: once with thinking off, once with thinking on.
import time
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-haiku-5-5"
A, B = 73_846, 59_217
QUESTION = f"What is {A:,} times {B:,}? Reply with only the number."


def ask(thinking):
    start = time.perf_counter()
    reply = client.messages.create(
        model=MODEL, max_tokens=8000, thinking=thinking,
        messages=[{"role": "user", "content": QUESTION}],
    )
    seconds = time.perf_counter() - start
    answer = "".join(b.text for b in reply.content if b.type == "text").strip()
    summary = "".join(b.thinking for b in reply.content if b.type == "thinking")
    return answer, summary, reply.usage, seconds


print("question:", QUESTION)
print(f"right answer (worked out by Python): {A * B:,}")
total = 0.0
for label, thinking in (("off", {"type": "disabled"}),
                        ("on", {"type": "adaptive", "display": "summarized"})):
    answer, summary, usage, seconds = ask(thinking)
    total += cost(MODEL, usage.input_tokens, usage.output_tokens)
    digits = "".join(c for c in answer if c.isdigit())
    tag = f"thinking {label:<3}|"
    print(tag, "answer:", answer)
    print(tag, "correct:", "yes" if digits == str(A * B) else "no")
    print(tag, "thought first:", " ".join(summary.split())[:50] or "(nothing)")
    print(tag, f"output tokens: {usage.output_tokens} | seconds: {seconds:.1f}")

print(f"cost: ${total:.6f}")
