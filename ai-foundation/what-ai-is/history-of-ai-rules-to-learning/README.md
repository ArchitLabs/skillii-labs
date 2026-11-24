# History of AI: From Hand-Written Rules to Learning

Course: AI Foundation · Section: What AI is, how it began, how it is built

The lab from the SKILLii lesson video *History of AI: From Hand-Written Rules to Learning*. It is a tiny expert
system, built the way the 1980s systems are described in Microsoft's lesson
[History of machine learning](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/2-history-of-ML/README.md):
a rules engine (if-then rules a person wrote by hand) and an inference engine that applies them to deduce new facts.

| Script | What it shows | Cost to run |
|---|---|---|
| `expert.py` | **An expert system**: inside its narrow domain, one rule's conclusion lets the next rule fire, until it reaches an answer; given facts outside that domain, no rule fits and it deduces nothing | free |

The script uses only Python itself: no library, no network, no key. It creates nothing and leaves nothing to tidy up.

## Run it

```bash
python expert.py
```

The rules are applied in the same order every time, so the output is the same on every run.

## Recorded run

<!-- skillii-kit:run expert -->
Recorded run of `python expert.py` (24 Nov 2026):

```text
case 1: has fur, eats meat, has stripes
  rule: has fur -> mammal
  rule: eats meat + mammal -> carnivore
  rule: carnivore + has stripes -> tiger
  new facts: 3
case 2: has scales, lives in water
  new facts: 0
```

This lab makes no paid request.
<!-- /skillii-kit:run expert -->
