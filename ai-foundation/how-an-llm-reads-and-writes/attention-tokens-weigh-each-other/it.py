# One word changes, and so does "it": a model reads the whole sentence to work out what "it" means.
import anthropic
from prices import cost

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-haiku-5-5"
SENTENCE = "The animal didn't cross the street because it was too {}."
QUESTION = 'In this sentence, what does "it" refer to? Reply with one word.'


def ask(sentence):
    reply = client.messages.create(
        model=MODEL, max_tokens=2000,
        messages=[{"role": "user", "content": f"{QUESTION}\n\n{sentence}"}],
    )
    text = "".join(b.text for b in reply.content if b.type == "text")
    word = text.split()[-1].strip('.*"').lower()  # the last word, without punctuation
    return word, cost(MODEL, reply.usage.input_tokens, reply.usage.output_tokens)


answers, total = [], 0.0
for last_word in ("tired", "wide"):
    sentence = SENTENCE.format(last_word)
    word, spent = ask(sentence)
    answers.append(word)
    total += spent
    print("sentence:", sentence)
    print('"it" refers to:', word)

print("one word changed, and so did the answer:", "yes" if answers[0] != answers[1] else "no")
print(f"cost: ${total:.6f}")
