# Temperature and sampling: a model's scores become probabilities, then one next token is drawn.
# Plain Python: nothing to install, no key, no network, nothing saved. It prints the same every run.
import math, random, time

# Example scores (logits) for the next token after "The sky is". Made-up numbers, not a real model's:
# a real model gives a score to every token in its vocabulary; five are enough to see the idea.
SCORES = {"blue": 5.0, "clear": 4.0, "dark": 3.0, "grey": 2.0, "green": 0.0}

def softmax(scores, temp):  # divide each score by the temperature, then share out 100%
    weights = {tok: math.exp(s / temp) for tok, s in scores.items()}  # e to the power of each
    total = sum(weights.values())
    return {tok: w / total for tok, w in weights.items()}  # the probabilities add up to 1

def top_k(probs, k):  # keep only the k most likely tokens, then share out 100% among them
    kept = sorted(probs, key=probs.get, reverse=True)[:k]
    total = sum(probs[tok] for tok in kept)
    return {tok: probs[tok] / total for tok in kept}

def top_p(probs, p):  # keep the most likely tokens until their probabilities add up to p
    kept, total = [], 0.0
    for tok in sorted(probs, key=probs.get, reverse=True):
        kept.append(tok)
        total += probs[tok]
        if total >= p:
            break
    return {tok: probs[tok] / total for tok in kept}

def draw(probs, n=8):  # pick n tokens at random, each as likely as its probability
    rng = random.Random(7)  # a fixed seed: the same eight random numbers every time
    return rng.choices(list(probs), weights=list(probs.values()), k=n)

def show(label, text):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(f"{label:<11}{text}")

def row(probs):
    return "  ".join(f"{tok} {p * 100:.1f}%" for tok, p in probs.items())

show("scores", "  ".join(f"{tok} {s}" for tok, s in SCORES.items()))
for temp in (0.2, 1.0, 2.0):  # low, 1.0, and high
    show(f"temp {temp}", row(softmax(SCORES, temp)))

base = softmax(SCORES, 1.0)  # trim the list of candidates at temperature 1.0
show("top-k 2", row(top_k(base, 2)))
show("top-p 0.9", row(top_p(base, 0.9)))

for temp in (0.2, 1.0, 2.0):  # the same random numbers, drawn from three shapes
    show(f"draw {temp}", " ".join(draw(softmax(SCORES, temp))))
