# What Is a Token in AI? Words, Pieces and Bytes

Course: AI Foundation · Section: Calling a model: tokens, window and cost

The lab from the SKILLii lesson video *What Is a Token in AI? Words, Pieces and Bytes*

`count.py` takes five short texts (one letter, one long word, an English sentence, the same sentence in Hindi and
one emoji) and prints, for each, what you can count yourself (words, characters, UTF-8 bytes) beside what the model's
own tokenizer counts. The token counts come from Anthropic's token counting endpoint, for two models: Claude Sonnet
4.5, on the earlier tokenizer, and Claude Opus 5.5, on the newer one.

Each count is for the whole request, one user message holding the text, so it includes the few tokens that wrap a
message. The `letter` row shows how many a one-letter message already counts. The count is an estimate the API gives
before anything is sent.

| Script | What it shows | Cost to run |
|---|---|---|
| `count.py` | Words, characters and bytes beside the tokens two models count for the same five texts | free (token counting is free to use) |

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python count.py
```

Token counting is free, but it has its own requests-per-minute limit; the script makes ten requests.
See [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting).

## Recorded run

<!-- skillii-kit:run count -->
Recorded run of `python count.py` (25 Nov 2026):

```text
text     words chars bytes  sonnet 4.5  opus 5.5
letter       1     1     1           8         9
word         1    12    12          11        13
english      9    50    50          18        23
hindi        8    40   106          41        42
emoji        1     1     4          11        11
```

This lab makes no paid request.
<!-- /skillii-kit:run count -->
