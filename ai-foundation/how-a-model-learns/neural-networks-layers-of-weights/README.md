# Neural Networks Explained: Layers and Weights

Course: AI Foundation · Section: How a model learns

The lab from the SKILLii lesson video *Neural Networks Explained: Layers and Weights*. A neural network is layers of
nodes. Each node takes a weighted sum of the layer before it and adds its own bias, and the weights and biases
together are the network's parameters. As the [Stanford CS231n notes](https://cs231n.github.io/neural-networks-1/)
put it, each neuron "performs a dot product with the input and its weights, adds the bias and applies the
non-linearity".

| Script | What it shows | Cost to run |
|---|---|---|
| `network.py` | A tiny network, 2 inputs, a hidden layer of 3 nodes and 1 output node, with its weights and biases written out by hand. It runs one input through the layers and prints each layer's values, changes one weight to show the output move, counts its parameters (every weight plus every bias), then counts the parameters of bigger networks the same way | free |

The script uses only Python itself: nothing to install, no network, no key. It creates nothing and leaves nothing to
tidy up. Its weights are set by hand; training is what would set them in a real network. It pauses half a second
before each line, so you can read the output one line at a time.

## Run it

```bash
python network.py
```

The weights never change between runs, so the numbers are the same every time.

## Recorded run

<!-- skillii-kit:run network -->
Recorded run of `python network.py` (26 Nov 2026):

```text
input: [2.0, 1.0]
hidden layer: [2.0, 1.5, 0.0]
output: 4.5
first output weight 1.0 -> 2.0, output: 6.5
parameters: 9 weights + 4 biases = 13
layers 3 -> 4 -> 2: 26 parameters
layers 784 -> 256 -> 10: 203,530 parameters
layers 4096 -> 4096 -> 4096: 33,562,624 parameters
```

This lab makes no paid request.
<!-- /skillii-kit:run network -->
