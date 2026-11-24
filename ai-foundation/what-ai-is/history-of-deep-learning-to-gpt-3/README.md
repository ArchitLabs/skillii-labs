# History of Deep Learning: From ImageNet to GPT-3

Course: AI Foundation · Section: What AI is, how it began, how it is built

The lab from the SKILLii lesson video *History of Deep Learning: From ImageNet to GPT-3*. It counts the parameters of
three GPT-3 models from nothing but the shapes their paper lists, the number of layers and the width of each
([Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), Table 2.1), with the rule from
[Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), section 2.1: each layer holds about
12 x width x width weights, leaving out the embeddings. For the largest model the count lands close to the
175 billion the paper lists; for the smallest, the embeddings it leaves out make up much of the difference.

| Script | What it shows | Cost to run |
|---|---|---|
| `params.py` | **Where 175 billion comes from**: layers times width squared, counted for GPT-3 Small, 13B and 175B, beside the count the paper lists | free |

The script uses only Python itself: no library, no network, no key. It creates nothing and leaves nothing to tidy up.

## Run it

```bash
python params.py
```

The arithmetic is the same on every run, so the output is too.

## Recorded run

<!-- skillii-kit:run params -->
Recorded run of `python params.py` (24 Nov 2026):

```text
GPT-3 Small: 12 layers, width 768
  counted: 84,934,656  paper: 125M
GPT-3 13B: 40 layers, width 5140
  counted: 12,681,408,000  paper: 13.0B
GPT-3 175B: 96 layers, width 12288
  counted: 173,946,175,488  paper: 175.0B
```

This lab makes no paid request.
<!-- /skillii-kit:run params -->
