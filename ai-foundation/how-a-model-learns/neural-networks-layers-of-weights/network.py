# A neural network: layers of nodes, joined by weights, plus one bias for each node.
# Plain Python: nothing to install, no network, no key. The output is the same on every run.
import time

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# the network: 2 inputs -> a hidden layer of 3 nodes -> 1 output node
weights = [
    [[0.5, 1.0], [1.0, -1.0], [-1.0, 1.0]],  # hidden layer: 3 nodes, one weight per input
    [[1.0, 2.0, 1.0]],  # output layer: 1 node, one weight per hidden node
]
biases = [[0.0, 0.5, 0.0], [-0.5]]  # one bias for each node

def layer(inputs, ws, bs, hidden):  # each node: its weighted sum of the inputs, plus its bias
    sums = [sum(w * x for w, x in zip(node, inputs)) + b for node, b in zip(ws, bs)]
    return [max(0.0, s) for s in sums] if hidden else sums  # a hidden node passes on only a positive sum

def forward(x):  # the input flows through the layers, one after the other
    h = layer(x, weights[0], biases[0], hidden=True)
    return h, layer(h, weights[1], biases[1], hidden=False)[0]

x = [2.0, 1.0]
h, out = forward(x)
show(f"input: {x}")
show(f"hidden layer: {h}")
show(f"output: {out}")

# turn one knob: training sets every weight; here one is set by hand
weights[1][0][0] = 2.0
show(f"first output weight 1.0 -> 2.0, output: {forward(x)[1]}")

# the parameters: every weight plus every bias
n_weights = sum(len(node) for ws in weights for node in ws)
n_biases = sum(len(bs) for bs in biases)
show(f"parameters: {n_weights} weights + {n_biases} biases = {n_weights + n_biases}")

def count(sizes):  # each layer: (inputs x nodes) weights, plus one bias per node
    return sum(a * b + b for a, b in zip(sizes, sizes[1:]))

# bigger networks, counted the same way (a 28 x 28 image is 784 inputs)
for sizes in [[3, 4, 2], [784, 256, 10], [4096, 4096, 4096]]:
    show(f"layers {' -> '.join(map(str, sizes))}: {count(sizes):,} parameters")
