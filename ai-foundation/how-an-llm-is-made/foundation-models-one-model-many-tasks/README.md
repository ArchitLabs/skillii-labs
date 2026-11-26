# What Is a Foundation Model? One Model, Many Tasks

Course: AI Foundation · Section: How an LLM is made

The lab from the SKILLii lesson video *What Is a Foundation Model? One Model, Many Tasks*. A foundation model is
trained once on broad data with no labels, and is then adapted to many different tasks. As
[On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) puts it, these are models
"trained on broad data at scale and are adaptable to a wide range of downstream tasks". This lab builds a tiny base
in that spirit and reuses it for two tasks.

| Script | What it shows | Cost to run |
|---|---|---|
| `base.py` | A base built once from eight sentences with no labels: each word is known by the words it shares a sentence with. Two tasks are then built on that same base, each from only two labelled words: "animal or food?" and "happy or sad?". A new word takes the label of the example it shares the most words with. The same two labels with no base can answer nothing, and a word the base never read gets no answer in any task built on it | free |

The script uses only Python itself: nothing to install, no network, no key. It creates nothing and leaves nothing to
tidy up. It is a toy that keeps one idea of a real foundation model, not how one is built: a real model is a deep
network trained on a vast amount of text, and is adapted by prompting it or by further training. The idea is the
same: the expensive part is done once, on text nobody labelled, and every task reuses it, gaps and all. It pauses half
a second before each line, so you can read the output one line at a time.

## Run it

```bash
python base.py
```

Nothing is random, so the output is the same every time.

## Recorded run

<!-- skillii-kit:run base -->
Recorded run of `python base.py` (26 Nov 2026):

```text
pre-trained once: 8 sentences, no labels, 20 words
cat: pet quiet   dog: loyal pet   rice: cook dinner
task    examples              answers
kind    dog=animal rice=food  cat=animal mango=food tiger=?
mood    smile=happy cry=sad   laugh=happy tears=sad grief=?
no base dog=animal rice=food  cat=? mango=? tiger=?
```

This lab makes no paid request.
<!-- /skillii-kit:run base -->
