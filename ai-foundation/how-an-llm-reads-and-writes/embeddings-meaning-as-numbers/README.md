# Embeddings Explained: Meaning as Numbers

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *Embeddings Explained: Meaning as Numbers*. An embedding turns a piece of text
into a list of numbers, a vector, and the distance between two vectors measures how similar the two texts are. This
lab looks at real word vectors: "Word2Vec 10K", the demo data of TensorFlow's
[Embedding Projector](https://projector.tensorflow.org/), where each of 10,000 words is a list of 200 numbers.

| Script | What it shows | Cost to run |
|---|---|---|
| `words.py` | Downloads the words and their vectors from the Projector's own server, prints the first 5 of the 200 numbers for three words, measures the cosine similarity of three pairs of words (1 means the two lists point the same way, -1 opposite), then searches all 10,000 words for the 5 whose vectors sit closest to one word | free |

The script uses only Python itself: nothing to install, no key, no sign-in. It reads two files from
projector.tensorflow.org (the word list and the 8 MB of numbers) and saves nothing, so there is nothing to tidy up. It
pauses half a second before each line, so you can read the output one line at a time.

These are word vectors. Embedding models used for search today do the same for a whole sentence or document: one
list of numbers per text, compared the same way.

## Run it

```bash
python words.py
```

## Recorded run

<!-- skillii-kit:run words -->
Recorded run of `python words.py` (27 Nov 2026):

```text
10,000 words, 200 numbers each
cat: 0.270  0.289  -0.254  0.296  -0.175  ... (200 numbers)
dog: 0.224  0.198  -0.125  0.029  -0.010  ... (200 numbers)
car: 0.018  0.170  -0.004  0.307  0.240  ... (200 numbers)
similarity cat, dog: 0.65
similarity cat, car: 0.50
similarity car, truck: 0.65
nearest to coffee: tea, sugar, cotton, vegetables, cocoa
```

This lab makes no paid request.
<!-- /skillii-kit:run words -->
