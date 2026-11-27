# Meaning as numbers: each word is a list of 200 numbers, and closeness between two lists measures similarity.
# Plain Python: nothing to install, no key, no sign-in, nothing saved. The vectors are "Word2Vec 10K", the demo data
# of TensorFlow's Embedding Projector, read from the Projector's own server (projector.tensorflow.org).
import math, struct, time, urllib.request

DATA = "https://projector.tensorflow.org/oss_data/word2vec_10000_200d_"
SIZE = 200  # numbers per word

def get(name):  # one file from the Projector's server
    with urllib.request.urlopen(DATA + name, timeout=60) as r:
        return r.read()

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# the words (one a line: the word, then how often it was seen) and their numbers (4 bytes each)
words = [line.split("\t")[0] for line in get("labels.tsv").decode().splitlines()[1:]]
raw = get("tensors.bytes")
numbers = struct.unpack(f"<{len(raw) // 4}f", raw)
vector = {w: numbers[i * SIZE:(i + 1) * SIZE] for i, w in enumerate(words)}
show(f"{len(vector):,} words, {SIZE} numbers each")

# meaning as numbers: the first 5 of each word's 200
for w in ["cat", "dog", "car"]:
    show(f"{w}: " + "  ".join(f"{x:.3f}" for x in vector[w][:5]) + f"  ... ({SIZE} numbers)")

# closeness: cosine similarity, from 1 (the two lists point the same way) down to -1 (opposite)
def similarity(a, b):
    dot = sum(x * y for x, y in zip(vector[a], vector[b]))
    return dot / math.sqrt(sum(x * x for x in vector[a]) * sum(y * y for y in vector[b]))

for a, b in [("cat", "dog"), ("cat", "car"), ("car", "truck")]:
    show(f"similarity {a}, {b}: {similarity(a, b):.2f}")

# search: the 5 words whose numbers sit closest to one word's
query = "coffee"
others = [w for w in vector if w not in (query, "UNK")]  # UNK is a placeholder, not a word
nearest = sorted(others, key=lambda w: similarity(query, w), reverse=True)[:5]
show(f"nearest to {query}: " + ", ".join(nearest))
