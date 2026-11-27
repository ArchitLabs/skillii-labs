# What a teacher model hands its student in distillation: soft targets. Plain Python: no install, no network, no key.
import math
import time

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# a teacher model's scores (logits) for one picture of a car: made-up numbers for the demo
logits = {"car": 9.0, "truck": 4.0, "carrot": -2.0}

def softmax(scores, T):  # T is the temperature: a higher T gives softer probabilities
    weights = {k: math.exp(v / T) for k, v in scores.items()}
    total = sum(weights.values())
    return {k: w / total for k, w in weights.items()}

def row(name, probs):
    return f"{name:<14}" + "".join(f"{k:>8} {100 * p:6.2f}%" for k, p in probs.items())

show("picture: a car")
show(row("hard label", {"car": 1.0, "truck": 0.0, "carrot": 0.0}))
show(row("teacher, T=1", softmax(logits, 1)))
show(row("teacher, T=4", softmax(logits, 4)))
show("the student is trained to match the T=4 row")
