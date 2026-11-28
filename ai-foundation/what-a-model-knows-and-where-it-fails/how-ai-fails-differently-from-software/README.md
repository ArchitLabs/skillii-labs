# How AI Fails Differently From Normal Software

Course: AI Foundation · Section: What a model knows, and where it fails

The lab from the SKILLii lesson video *How AI Fails Differently From Normal Software*. It follows NIST's
[AI RMF Appendix B: How AI Risks Differ from Traditional Software Risks](https://airc.nist.gov/airmf-resources/airmf/appendices/app-b-how-ai-risks-differ-from-traditional-software-risks/):
an AI system depends on its data, and its data can drift away from the world it is used in.

| Script | What it shows | Cost to run |
|---|---|---|
| `fails.py` | Two programs work out the area of a square. One is a rule a person wrote (side times side). The other is a straight line learned from five examples, sides 1 to 5: a toy stand-in for a model, not a real AI model. Inside the examples the learned rule is close; at side 20 it is far off, and nothing raises an error. A bad input to the written rule stops it with an error you can read. Then the inputs move from sides 1 to 5 to sides 16 to 20, with no change to the code, and the average error grows | free: plain Python, no network, no key |

The script calls nothing and saves nothing, so there is nothing to tidy up. Every number it prints is exact and the
same on every machine.

## Run it

```
python fails.py
```

## Recorded run

<!-- skillii-kit:run fails -->
Recorded run of `python fails.py` (29 Nov 2026):

```text
learned from sides 1 to 5: area = 6.0 * side - 7.0
side  written  learned
   3        9     11.0
   5       25     23.0
  20      400    113.0
written, side "20": TypeError: can't multiply sequence by non-int of type 'str'
average error, sides 1 to 5: 1.6
average error, sides 16 to 20: 225.0
```

This lab makes no paid request.
<!-- /skillii-kit:run fails -->
