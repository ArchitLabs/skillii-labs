# One sentence in four languages: how many tokens does each cost?
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
OLD, NEW = "claude-sonnet-4-5-20250929", "claude-opus-5-5"

sentence = {
    "english": "Please send me the bill for this month by email.",
    "hindi": "कृपया इस महीने का बिल मुझे ईमेल से भेजें।",
    "tamil": "தயவுசெய்து இந்த மாதத்தின் பில்லை எனக்கு மின்னஞ்சலில் அனுப்பவும்.",
    "odia": "ଦୟାକରି ଏହି ମାସର ବିଲ୍ ମୋତେ ଇମେଲରେ ପଠାନ୍ତୁ।",
}


def tokens(model, text):
    message = [{"role": "user", "content": text}]
    return client.messages.count_tokens(model=model, messages=message).input_tokens


print(f"{'language':<9}{'chars':>6}{'bytes':>6}{'sonnet 4.5':>12}{'opus 5.5':>10}")
for language, text in sentence.items():
    chars, size = len(text), len(text.encode("utf-8"))
    print(f"{language:<9}{chars:>6}{size:>6}{tokens(OLD, text):>12}{tokens(NEW, text):>10}")
