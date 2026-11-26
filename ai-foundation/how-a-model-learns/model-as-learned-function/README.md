# What Is an AI Model? A Function Learned From Data

Course: AI Foundation · Section: How a model learns

The lab from the SKILLii lesson video *What Is an AI Model? A Function Learned From Data*. A model is a function
whose numbers (its parameters) were learned from data, as
[Dive into Deep Learning](https://d2l.ai/chapter_introduction/index.html) puts it: "Once the parameters are fixed, we
call the program a model".

| Script | What it shows | Cost to run |
|---|---|---|
| `model.py` | One function, `f(x) = w * x + b`, written once. Fitted to two data sets (temperatures in Celsius and Fahrenheit; a made-up shop's rice bills), it learns two sets of parameters and so becomes two different models. Each is then called like any function on an input it never saw | free |

The script uses only Python itself: no library, no network, no key. It creates nothing and leaves nothing to tidy
up. The temperature pairs are exact conversions; the rice shop is made up.

## Run it

```bash
python model.py
```

The data never changes, so the numbers are the same on every run.

## Recorded run

<!-- skillii-kit:run model -->
Recorded run of `python model.py` (26 Nov 2026):

```text
temperature model learned: w = 1.80, b = 32.00
rice model learned: w = 60.00, b = 20.00
temperature model: f(20) = 68.00
rice model: f(20) = 1220.00
```

This lab makes no paid request.
<!-- /skillii-kit:run model -->
