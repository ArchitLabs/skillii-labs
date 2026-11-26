# One base, built once from text with no labels, then reused for two tasks with two labelled words each.
# Plain Python: nothing to install, no network, no key. The output is the same on every run.
import time

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# broad text with no labels: nobody says which word is an animal, a food or a feeling
text = [
    "the dog is a loyal pet", "the cat is a quiet pet",
    "we cook rice for dinner", "we eat sweet mango for dinner",
    "we smile when friends visit", "we laugh with friends",
    "we cry when we feel alone", "tears fall when we feel alone",
]
skip = {"the", "is", "a", "we", "for", "when", "with"}  # small words that say little

# pre-training, done once: each word is known by the words it shares a sentence with
base = {}
for sentence in text:
    words = [w for w in sentence.split() if w not in skip]
    for w in words:
        base.setdefault(w, set()).update(v for v in words if v != w)

# adapting to a task: a new word takes the label of the example it shares the most words with
def label(word, examples, known):
    shared = {lab: len(known.get(word, set()) & known.get(ex, set())) for ex, lab in examples.items()}
    best = max(shared, key=shared.get)
    return best if shared[best] > 0 else "?"  # shares nothing with any example: no answer

# two tasks, two labelled words each, both built on the same base
kind = {"dog": "animal", "rice": "food"}
mood = {"smile": "happy", "cry": "sad"}

def row(name, examples, words, known):
    shown = " ".join(f"{w}={lab}" for w, lab in examples.items())
    answers = " ".join(f"{w}={label(w, examples, known)}" for w in words)
    show(f"{name:<8}{shown:<22}{answers}")

show(f"pre-trained once: {len(text)} sentences, no labels, {len(base)} words")
show("   ".join(f"{w}: {' '.join(sorted(base[w]))}" for w in ["cat", "dog", "rice"]))
show(f"{'task':<8}{'examples':<22}answers")
row("kind", kind, ["cat", "mango", "tiger"], base)
row("mood", mood, ["laugh", "tears", "grief"], base)
# the same two labels with no pre-training: the task has only its own two examples to go on
row("no base", kind, ["cat", "mango", "tiger"], {})
