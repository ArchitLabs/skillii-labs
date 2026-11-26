# Pre-training at toy size: text that nobody labelled, where the answer to learn is always the word that comes next.
# Plain Python: nothing to install, no network, no key. The output is the same on every run.
import time
from collections import Counter

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# the text: three dated pages, and nobody has labelled any of it
pages = {
    "2023": "the capital of india is new delhi .",
    "2024": "the latest app version is 2 .",
    "2025": "the latest app version is 3 .",
}
cutoff = "2024"  # pre-training stops here: later pages are never read

# pre-training: in every three words in a row, the first two are the input and the third is the answer to learn
seen, examples, read = {}, 0, 0
for date, page in pages.items():
    if date > cutoff:
        continue
    words = page.split()
    read += len(words)
    for a, b, after in zip(words, words[1:], words[2:]):
        seen.setdefault((a, b), Counter())[after] += 1
        examples += 1

# writing: from the last two words, add the word seen most often after them, until a full stop
def complete(prompt):
    words = prompt.split()
    while words[-1] != "." and (words[-2], words[-1]) in seen:
        nexts = seen[(words[-2], words[-1])]
        words.append(max(nexts, key=nexts.get))
    return " ".join(words[len(prompt.split()):]) or "?"  # nothing added: these words were never read together

show(f"pre-trained on pages up to {cutoff}: {read} words, {examples} practice examples, no labels")
show("   ".join(f"{a} {b} -> {max(n, key=n.get)}" for (a, b), n in list(seen.items())[:3]))
for prompt in ["the capital of india is", "the capital of kenya is", "the latest app version is"]:
    show(f"{prompt} -> {complete(prompt)}")
for date in [d for d in pages if d > cutoff]:
    show(f"never read, the {date} page: {pages[date]}")
