# Thinking tokens: billed as output, counted inside max_tokens, steered by effort.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-opus-5-5"  # thinks adaptively: effort sets how much
QUESTION = "How many numbers from 1 to 99999 have digits that add up to 25? Reply with only the number."
RIGHT = sum(1 for n in range(1, 100000) if sum(map(int, str(n))) == 25)
print("question:", QUESTION)
print(f"right answer (worked out by Python): {RIGHT}")


def ask(effort, max_tokens):
    reply = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,  # one cap for thinking plus text
        output_config={"effort": effort},
        messages=[{"role": "user", "content": QUESTION}],
    )
    usage = reply.usage
    details = usage.output_tokens_details  # how much of the output was thinking
    thinking = details.thinking_tokens if details else 0
    answer = " ".join("".join(b.text for b in reply.content if b.type == "text").split())
    spent = cost(usage.input_tokens, usage.output_tokens)  # thinking is inside output_tokens
    print(f"effort {effort}, max_tokens {max_tokens}: stop_reason {reply.stop_reason}")
    print(f"input {usage.input_tokens}, output {usage.output_tokens:,} (thinking {thinking:,}),"
          f" answer: {answer[:20] or '(none)'}, cost ${spent:.6f}")
    return spent


total = ask("low", 16000)    # 1. less thinking
total += ask("high", 16000)  # 2. more thinking, the same question
total += ask("high", 50)     # 3. a cap far too small for the thinking
print(f"total cost: ${total:.6f}")
