# History of AI Assistants: From Chat Models to Agents

Course: AI Foundation · Section: What AI is, how it began, how it is built

The lab from the SKILLii lesson video *History of AI Assistants: From Chat Models to Agents*. InstructGPT
([Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155),
section 3.5) trained its reward model on labelers' rankings: a labeler ranks between K = 4 and K = 9 answers to one
prompt, and every pair in that ranking becomes one comparison, "this answer is preferred to that one". The script
turns one ranking of four answers into its six comparisons, then counts the comparisons one ranking gives for every K
from 4 to 9.

| Script | What it shows | Cost to run |
|---|---|---|
| `rankings.py` | **One ranking, many comparisons**: the pairs a ranking of four answers gives, and the count for K = 4 to 9 | free |

The script uses only Python itself: no library, no network, no key. It creates nothing and leaves nothing to tidy up.

## Run it

```bash
python rankings.py
```

The counting is the same on every run, so the output is too.

## Recorded run

<!-- skillii-kit:run rankings -->
Recorded run of `python rankings.py` (25 Nov 2026):

```text
ranking: A > B > C > D
  A is preferred to B
  A is preferred to C
  A is preferred to D
  B is preferred to C
  B is preferred to D
  C is preferred to D
K = 4: 6 comparisons
K = 5: 10 comparisons
K = 6: 15 comparisons
K = 7: 21 comparisons
K = 8: 28 comparisons
K = 9: 36 comparisons
```

This lab makes no paid request.
<!-- /skillii-kit:run rankings -->
