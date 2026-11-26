# What Does "8B" Mean in an AI Model's Name?

Course: AI Foundation · Section: How a model learns

The lab from the SKILLii lesson video *What Does "8B" Mean in an AI Model's Name?*. A model you can download is two
kinds of file: a configuration file that describes its architecture, and a weights file that holds its parameters,
the numbers learned in training. As the
[Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter2/3) puts it, "the model weights are the
parameters of the model". The "8B" in a name counts those numbers. This lab counts them for
[Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B), an open-weights model (Apache 2.0) that anyone can download without
signing in.

| Script | What it shows | Cost to run |
|---|---|---|
| `count.py` | Reads Qwen3-8B's `config.json` (the architecture: layers, hidden size, vocabulary) and works out how many numbers each part holds, a weight matrix of r rows and k columns holding r x k. It adds them up and compares the total with the "8B" in the name. Then it reads the weights' own index, which says how many bytes the numbers fill, and shows that is 2 bytes a number (bfloat16); then the size of the weight files on disk, and the memory needed just to hold the numbers at 2 bytes and at 1 byte each | free |

The script uses only Python itself: nothing to install, no key, no sign-in. It reads three small JSON files from
huggingface.co (the config, the weights index and the repository's file list), never the 16 GB of weights, and saves
nothing, so there is nothing to tidy up. It reads one fixed version of the repository, so the output is the same on
every run. It pauses half a second before each line, so you can read the output one line at a time.

The memory figures are for the numbers alone. Running a model also needs memory for its working values, which grows
with the length of the text.

## Run it

```bash
python count.py
```

## Recorded run

<!-- skillii-kit:run count -->
Recorded run of `python count.py` (26 Nov 2026):

```text
model: Qwen/Qwen3-8B
config.json: 36 layers, hidden size 4,096, vocabulary 151,936
one layer:           192,946,432 numbers
36 layers:         6,946,071,552 numbers
outside layers:    1,244,663,808 numbers
total:             8,190,735,360 numbers = 8.2B
weights: 16,381,470,720 bytes = 2 bytes a number (bfloat16)
on disk: 5 files, 16.4 GB
to load: 16.4 GB at 2 bytes a number, 8.2 GB at 1 byte
```

This lab makes no paid request.
<!-- /skillii-kit:run count -->
