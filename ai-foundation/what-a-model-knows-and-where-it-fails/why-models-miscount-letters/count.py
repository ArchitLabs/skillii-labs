# Ask a model to count the letters in four words, then check each answer with code.
import json
from collections import Counter

import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
words = ["strawberry", "mississippi", "bookkeeper", "abracadabra"]
prompt = 'Count how many times each letter appears in the word "{}". Reply with JSON only, like {{"a": 1}}.'
replies, right = [], 0


def ask(word):
    reply = client.messages.create(model="claude-haiku-4-5", max_tokens=200,
                                   messages=[{"role": "user", "content": prompt.format(word)}])
    replies.append(reply)
    text = next((b.text for b in reply.content if b.type == "text"), "")
    try:
        return json.loads(text[text.find("{"):text.rfind("}") + 1])
    except ValueError:
        return {}


print(f"{'word':<13}{'repeats model/code':<22}every letter")
for word in words:
    model, code = ask(word), Counter(word)
    repeats = "  ".join(f"{c} {model.get(c, '?')}/{n}" for c, n in code.items() if n > 1)
    ok = {c: n for c, n in model.items() if n} == dict(code)
    right += ok
    print(f"{word:<13}{repeats:<22}{'right' if ok else 'wrong'}")

print(f"words with every letter right: {right} of {len(words)}")
spent = sum(cost(r.usage.input_tokens, r.usage.output_tokens) for r in replies)
print(f"cost: ${spent:.6f}")
