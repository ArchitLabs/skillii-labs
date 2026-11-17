# SKILLii labs

The code behind SKILLii's lesson videos: every lab you see run on screen, so you can run it yourself.

| Lesson | What you'll see |
|---|---|
| [01-llm-pricing](01-llm-pricing/) | Count a prompt's tokens, send one real request and price it, watch a chat's input grow every turn, and see prompt caching cut the cost of repeated input. |

## Run a lab

You need Python 3.10+ and an Anthropic API key.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # your own key; never commit it
cd 01-llm-pricing && python3 ask.py
```

Each lesson's README says what every script costs to run (fractions of a US cent to a few cents) and shows the output
we recorded for the video. Your numbers will differ a little: models change and answers vary. That's the point of
counting real tokens.

## Keeping keys out of git

- Keys are read from the environment only. `.env` is ignored; `.env.example` shows the names.
- `git config core.hooksPath .githooks` turns on a pre-commit check that refuses key-shaped text.
- The same check runs on every push.

## Licence

MIT, see [LICENSE](LICENSE).
