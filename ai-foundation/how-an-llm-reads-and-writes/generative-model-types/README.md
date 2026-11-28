# Generative AI Model Types: Text, Image, Audio, Video

Course: AI Foundation · Section: How an LLM reads and writes

The labs from the SKILLii lesson video *Generative AI Model Types: Text, Image, Audio, Video*. Two families of
generative model do their work in two different shapes. A large language model writes one token at a time: as
the [Transformer paper](https://arxiv.org/abs/1706.03762) puts it, "At each step the model is auto-regressive",
"consuming the previously generated symbols as additional input when generating the next." A diffusion model starts from noise and refines the whole picture over many steps: as Hugging Face's
diffusion course puts it, "Generation begins with random noise, but this is gradually refined over a number of steps
until an output image emerges."

| Script | What it shows | Cost to run |
|---|---|---|
| `text.py` | Text, the LLM way: each model call adds one token to the end, so a six-token answer takes six calls, and a longer answer needs more calls | free |
| `image.py` | An image, the diffusion way: an 18-pixel picture starts as random noise, and each of five steps refines every pixel at once, until the picture (a hill) appears | free |

Both are toys. The "model" in each is a stand-in that already knows its answer, so you see the shape of the work
(how many model calls, and what each call touches), not the learning. A real diffusion model is trained to predict
the noise; a real language model is trained to predict the next token.

The scripts use only Python itself: nothing to install, no network, no key. They create nothing and leave nothing
to tidy up. Each pauses half a second between steps, so you can watch the output build one line at a time.

## Run it

```bash
python text.py
python image.py
```

The noise in `image.py` comes from a fixed seed, so both scripts print the same lines on every run.

## Recorded run

<!-- skillii-kit:run text -->
Recorded run of `python text.py` (28 Nov 2026):

```text
call 1: Diffusion
call 2: Diffusion starts
call 3: Diffusion starts from
call 4: Diffusion starts from random
call 5: Diffusion starts from random noise
call 6: Diffusion starts from random noise.
6 model calls for 6 tokens: a longer answer needs more calls
```

This lab makes no paid request.
<!-- /skillii-kit:run text -->

<!-- skillii-kit:run image -->
Recorded run of `python image.py` (28 Nov 2026):

```text
noise:  |▁▇▆▂▄▄▅▆▁ ▇▃▆ ▄▆▂█|
step 1: |▁▆▅▂▄▄▅▆▂▂▇▄▆▁▃▅▂▆|
step 2: |▁▄▄▂▄▄▆▇▄▃▇▄▆▂▃▄▁▅|
step 3: | ▃▄▃▄▄▆▇▅▅▇▅▅▂▃▄▁▃|
step 4: | ▂▃▃▄▅▆▇▇▆▇▅▅▃▃▃▁▂|
step 5: | ▁▂▃▄▅▆▇██▇▆▅▄▃▂▁ |
5 model calls, one per step, each over all 18 pixels
```

This lab makes no paid request.
<!-- /skillii-kit:run image -->
