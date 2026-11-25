# How many tokens is a text? Ask the model's own tokenizer: token counting is free.
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
OLD, NEW = "claude-sonnet-4-5-20250929", "claude-opus-5-5"

texts = {
    "letter": "a",
    "word": "unbelievable",
    "english": "Tokens are the smallest units of a language model.",
    "hindi": "टोकन भाषा मॉडल की सबसे छोटी इकाइयाँ हैं।",
    "emoji": "🙂",
}


def tokens(model, text):
    message = [{"role": "user", "content": text}]
    return client.messages.count_tokens(model=model, messages=message).input_tokens


print(f"{'text':<8}{'words':>6}{'chars':>6}{'bytes':>6}{'sonnet 4.5':>12}{'opus 5.5':>10}")
for name, text in texts.items():
    words, chars, size = len(text.split()), len(text), len(text.encode("utf-8"))
    print(f"{name:<8}{words:>6}{chars:>6}{size:>6}{tokens(OLD, text):>12}{tokens(NEW, text):>10}")
