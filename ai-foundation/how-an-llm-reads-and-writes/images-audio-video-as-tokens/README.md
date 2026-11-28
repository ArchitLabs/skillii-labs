# How AI Reads Images and Audio: They Become Tokens

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *How AI Reads Images and Audio: They Become Tokens*.

`images.py` uses the Anthropic Python SDK to show that a picture is counted in tokens, just like text. It makes one
plain white PNG picture in memory at four sizes (200x200, 1000x1000, 1920x1080 and 3840x2160 pixels) and asks
Claude Opus 5.5's token counting endpoint how many input tokens a short question takes on its own, and with each
picture attached. For each size it prints:

- **28px patches**: the picture's size in 28-pixel squares, worked out by Python (`ceil(width / 28) * ceil(height / 28)`).
- **with image**: the token count of the question with the picture attached.
- **image tokens**: the difference, which is what the picture alone adds.

Compare the two columns. Claude shrinks a picture that is over the model's limits before it counts it, so the
largest picture's count is capped. How Claude resizes and pads pictures is described in Anthropic's
[Coordinates and bounding boxes](https://platform.claude.com/docs/en/build-with-claude/vision-coordinates) guide.

| Script | What it shows | Cost to run |
|---|---|---|
| `images.py` | The token count of one picture at four sizes | free: it only calls the token counting endpoint, and sends nothing to the model |

No picture file is read or written: the pictures are made in memory and sent as base64.

## Run it

```
pip install anthropic
export ANTHROPIC_API_KEY=...   # your own key
python images.py
```

## Recorded run

<!-- skillii-kit:run images -->
Recorded run of `python images.py` (28 Nov 2026):

```text
text only: 15 tokens
size        28px patches  with image  image tokens
200x200               64          82            67
1000x1000           1296        1314          1299
1920x1080           2691        2709          2694
3840x2160          10764        4802          4787
```

This lab makes no paid request.
<!-- /skillii-kit:run images -->
