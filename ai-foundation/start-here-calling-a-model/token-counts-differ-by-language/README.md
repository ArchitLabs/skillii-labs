# Why Indian Languages Use More AI Tokens

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The lab from the SKILLii lesson video *Why Indian Languages Use More AI Tokens*

`languages.py` takes one sentence, "Please send me the bill for this month by email.", written in English, Hindi, Tamil
and Odia, and prints for each language what you can count yourself (characters and UTF-8 bytes) beside what two
models' own tokenizers count. The token counts come from Anthropic's token counting endpoint, for Claude Sonnet 4.5,
on the earlier tokenizer, and Claude Opus 5.5, on the newer one.

Each count is for the whole request, one user message holding the sentence, so it includes the same few tokens that
wrap every message. The count is an estimate the API gives before anything is sent. One sentence is a small sample:
the research papers the video cites measure many sentences.

| Script | What it shows | Cost to run |
|---|---|---|
| `languages.py` | Characters, bytes and the tokens two models count for the same sentence in four languages | free (token counting is free to use) |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python languages.py
```

Token counting is free, but it has its own requests-per-minute limit; the script makes eight requests.
See [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting).

## Recorded run

<!-- skillii-kit:run languages -->
Recorded run of `python languages.py` (26 Nov 2026):

```text
language  chars bytes  sonnet 4.5  opus 5.5
english      48    48          18        21
hindi        41   107          35        36
tamil        64   178          61        62
odia         41   111          67        68
```

This lab makes no paid request.
<!-- /skillii-kit:run languages -->
