# One layer or two stacked layers: which can learn XOR? Nobody tells the hidden nodes what to look for.
# Plain Python: nothing to install, no network, no key. The output is the same on every run.
import time
from itertools import product

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# XOR: the answer is 1 when exactly one of the two inputs is 1
data = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)]

def node(xs, s):  # s = (weight 1, weight 2, bias); the node fires (1) when its sum is above 0
    return 1 if s[0] * xs[0] + s[1] * xs[1] + s[2] > 0 else 0

def wrong(predict):  # the loss: how many of the 4 answers are wrong
    return sum(predict(x) != y for x, y in data)

# every setting one node can take: each weight -1, 0 or 1, and a bias of -1.5, -0.5 or 0.5
settings = list(product([-1, 0, 1], [-1, 0, 1], [-1.5, -0.5, 0.5]))

# one layer: a single node reads the inputs; keep its setting with the lowest loss
one = min(settings, key=lambda s: wrong(lambda x: node(x, s)))

# two layers: two hidden nodes read the inputs, and the output node reads only the hidden nodes
def stack(x, h1, h2, out):
    return node((node(x, h1), node(x, h2)), out)

# fit all three nodes together: try every combination, keep the one with the lowest loss
h1, h2, out = min(product(settings, repeat=3), key=lambda s: wrong(lambda x: stack(x, *s)))

def report(name, predict, tried):
    answers = [predict(x) for x, _ in data]
    show(f"{name} {answers}  {4 - wrong(predict)} of 4 right (best of {tried:,})")

show(f"wanted:     {[y for _, y in data]}")
report("one layer: ", lambda x: node(x, one), len(settings))
report("two layers:", lambda x: stack(x, h1, h2, out), len(settings) ** 3)

# the features the hidden layer found for itself, and the answer the output node builds on them
show("input   hidden  output")
for x, _ in data:
    show(f"{x}  {(node(x, h1), node(x, h2))}  {stack(x, h1, h2, out)}")
