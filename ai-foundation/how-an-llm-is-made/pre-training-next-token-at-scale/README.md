# LLM Pre-Training Explained: Predicting the Next Token

Course: AI Foundation · Section: How an LLM is made

The lab from the SKILLii lesson video *LLM Pre-Training Explained: Predicting the Next Token*. Pre-training is the
first stage of making a language model. As Anthropic's
[glossary](https://platform.claude.com/docs/en/about-claude/glossary) puts it, it is "the initial process of training
language models on a large unlabeled corpus of text", in which models "are pretrained to predict the next word, given
the previous context of text in the document". This lab pre-trains a tiny model in that spirit.

| Script | What it shows | Cost to run |
|---|---|---|
| `pretrain.py` | Three dated pages of text that nobody labelled, read up to a cutoff year. Every run of three words becomes one practice example: the first two words are the input, and the word that comes next is the answer to learn, so the text supplies its own answers. The model then writes by adding, again and again, the word it saw most often after the last two. It completes a fact it read, has nothing to add about one it never read, and gives the answer from the last page it read, while a page after its cutoff says otherwise | free |

The script uses only Python itself: nothing to install, no network, no key. It creates nothing and leaves nothing to
tidy up. It is a toy that keeps the idea of pre-training, not how a real model is built: a real model is a deep
network that looks at all the text before the next token, not just two words, learns its weights by lowering its loss
on these same next-token examples instead of counting them, and reads trillions of tokens, not fifteen words. The idea
is the same: the answers come from the text itself, and the model knows only what was in the text it read before its
cutoff. It pauses half a second before each line, so you can read the output one line at a time.

## Run it

```bash
python pretrain.py
```

Nothing is random, so the output is the same every time. Try adding a page about Kenya dated 2023, or moving the
cutoff to 2025, and predict the output before you run it.

## Recorded run

<!-- skillii-kit:run pretrain -->
Recorded run of `python pretrain.py` (27 Nov 2026):

```text
pre-trained on pages up to 2024: 15 words, 11 practice examples, no labels
the capital -> of   capital of -> india   of india -> is
the capital of india is -> new delhi .
the capital of kenya is -> ?
the latest app version is -> 2 .
never read, the 2025 page: the latest app version is 3 .
```

This lab makes no paid request.
<!-- /skillii-kit:run pretrain -->
