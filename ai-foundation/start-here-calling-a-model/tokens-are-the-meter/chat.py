# Three turns of one conversation. The model keeps no memory between requests,
# so every turn sends the whole history again, as input.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
questions = ["What is a token? One sentence.",
             "And why does output cost more? One sentence.",
             "So what makes a long chat expensive? One sentence."]
history = []
spent = 0

for turn, question in enumerate(questions, start=1):
    history.append({"role": "user", "content": question})
    reply = client.messages.create(model="claude-opus-5-5", max_tokens=400,
                                   messages=history)
    history.append({"role": "assistant", "content": reply.content})
    u = reply.usage
    dollars = cost(u.input_tokens, u.output_tokens)
    spent += dollars
    print(f"turn {turn}: input_tokens {u.input_tokens:>4}, "
          f"output_tokens {u.output_tokens:>4}, ${dollars:.6f}")

print(f"cost: ${spent:.6f}")
