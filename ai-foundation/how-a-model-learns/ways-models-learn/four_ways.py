# Four ways a model learns. The same small data, four kinds of signal to learn from:
# labels, no labels, a reward, and the data itself. Plain Python: no network, no key, the same output every run.
import time
from collections import Counter

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# data: six parcels by weight in kg, and the depot's dispatch log as text
weights = [1, 2, 3, 10, 11, 12]
log = "parcel to pune parcel to delhi parcel to pune"

# 1. supervised: every example comes with its right answer, a label
labels = ["small", "small", "small", "large", "large", "large"]
small = [w for w, label in zip(weights, labels) if label == "small"]
large = [w for w, label in zip(weights, labels) if label == "large"]
cut = (sum(small) / len(small) + sum(large) / len(large)) / 2  # half way between the two averages
show(f"supervised: 6 labelled parcels, learned the cut at {cut} kg")
for w in [4, 9]:  # two new parcels, never seen
    show(f"  new parcel {w} kg -> {'small' if w < cut else 'large'}")

# 2. unsupervised: no labels; find two groups by distance alone (2-means clustering)
a, b = min(weights), max(weights)  # two starting centres
for _ in range(3):
    group_a = [w for w in weights if abs(w - a) <= abs(w - b)]
    group_b = [w for w in weights if abs(w - a) > abs(w - b)]
    a, b = sum(group_a) / len(group_a), sum(group_b) / len(group_b)
show(f"unsupervised: no labels, found 2 groups: {group_a} and {group_b}")

# 3. reinforcement: no labels; act, get a reward, and keep what scored best
def reward(weight, vehicle):  # the world scores each action; the learner never reads this rule
    if vehicle == "bike":
        return 2 if weight <= 5 else -5  # a bike is cheap, but cannot carry a heavy parcel
    return 1  # a van always delivers, but costs more

show("reinforcement: no labels, one reward per try")
bike = []
for w in weights:  # trial and error: try both, keep the higher reward
    scores = {v: reward(w, v) for v in ["bike", "van"]}
    show(f"  parcel {w} kg: bike {scores['bike']:+d}, van {scores['van']:+d}")
    if scores["bike"] > scores["van"]:
        bike.append(w)
show(f"  learned: bike for {bike}, van for the rest")

# 4. self-supervised: no labels added; each word's label is simply the next word
words = log.split()
pairs = list(zip(words, words[1:]))  # (word, next word), made from the data itself
show(f"self-supervised: {len(pairs)} pairs made from the log, first {pairs[0][0]} -> {pairs[0][1]}")
nexts = {}
for word, after in pairs:
    nexts.setdefault(word, Counter())[after] += 1
for word in ["parcel", "to"]:
    guess, n = nexts[word].most_common(1)[0]
    show(f"  after {word}: {guess} ({n} of {sum(nexts[word].values())} times)")
