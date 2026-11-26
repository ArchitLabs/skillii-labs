# What Is Deep Learning? Many Layers, Learned Features

Course: AI Foundation · Section: How a model learns

The lab from the SKILLii lesson video *What Is Deep Learning? Many Layers, Learned Features*. Deep learning stacks
layers, and each layer builds its features on the values of the layer below. Nobody writes those features by hand:
every layer's weights are fitted together, by lowering one loss. As
[Dive into Deep Learning](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html) puts it, "no linear model can solve
the four-point XOR problem"; this lab shows a stack of two layers solving it.

| Script | What it shows | Cost to run |
|---|---|---|
| `layers.py` | XOR (the answer is 1 when exactly one of two inputs is 1), fitted twice. First by one node reading the inputs directly: it tries every setting of its weights and bias and keeps the one with the lowest loss, and still gets one answer wrong. Then by two layers, two hidden nodes and one output node, all fitted together the same way: they get all four right. It then prints what each hidden node learned to fire on, and the output the last node builds from them | free |

The script uses only Python itself: nothing to install, no network, no key. It creates nothing and leaves nothing to
tidy up. To keep every number exact, each weight may only be -1, 0 or 1 and each bias -1.5, -0.5 or 0.5, and the
"training" tries every setting and keeps the one with the lowest loss (how many of the four answers are wrong). Real
networks have millions of weights, so they are trained by gradient descent instead, which lowers the loss step by
step; the idea is the same: all the layers are fitted together to lower one loss. It pauses half a second before each
line, so you can read the output one line at a time.

## Run it

```bash
python layers.py
```

Nothing is random, so the output is the same every time.

## Recorded run

<!-- skillii-kit:run layers -->
Recorded run of `python layers.py` (26 Nov 2026):

```text
wanted:     [0, 1, 1, 0]
one layer:  [0, 1, 0, 0]  3 of 4 right (best of 27)
two layers: [0, 1, 1, 0]  4 of 4 right (best of 19,683)
input   hidden  output
(0, 0)  (1, 0)  0
(0, 1)  (0, 0)  1
(1, 0)  (0, 0)  1
(1, 1)  (0, 1)  0
```

This lab makes no paid request.
<!-- /skillii-kit:run layers -->
