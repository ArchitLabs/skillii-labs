# Three turns of one conversation. The model keeps no memory between requests,
# so every turn sends the whole history again, as input.
import os

import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = os.environ.get("SKILLII_MODEL", "claude-opus-5-5")
questions = ["What is a token? One sentence.",
             "And why does output cost more? One sentence.",
             "So what makes a long chat expensive? One sentence."]
history = []

for turn, question in enumerate(questions, start=1):
    history.append({"role": "user", "content": question})
    reply = client.messages.create(model=MODEL, max_tokens=200,
                                   messages=history)
    history.append({"role": "assistant", "content": reply.content})
    print(f"turn {turn}: input_tokens {reply.usage.input_tokens}, "
          f"output_tokens {reply.usage.output_tokens}")
