# How a Chat Model Is Made: Fine-Tuning and RLHF

Course: AI Foundation · Section: How an LLM is made

The lab from the SKILLii lesson video *How a Chat Model Is Made: Fine-Tuning and RLHF*. A pre-trained model carries on
text; it does not yet answer. The InstructGPT paper ([arXiv 2203.02155](https://arxiv.org/abs/2203.02155)) describes
the stages that teach it to: fine-tune on a dataset of "labeler demonstrations of the desired model behavior", then
collect "a dataset of rankings of model outputs" and train further "using reinforcement learning from human feedback".
Anthropic's [glossary](https://platform.claude.com/docs/en/about-claude/glossary) describes the same two stages. This
lab runs all three steps at toy size.

| Script | What it shows | Cost to run |
|---|---|---|
| `posttrain.py` | A tiny model that holds a score for each of four replies to one question, where each extra point doubles a reply's chance. After pre-training it most likely carries on with another question. Step 1, fine-tuning: seven answers written by people each raise their reply's score, so the model now mostly answers. Step 2, the reward model: people rank three replies, best first, and the reward model learns which words the better reply of each pair had, so it can score any reply, even one nobody ranked. Step 3, reinforcement learning: each reply's score moves by its reward, and the reply people ranked best becomes the likeliest | free |

The script uses only Python itself: nothing to install, no network, no key. It creates nothing and leaves nothing to
tidy up. It is a toy that keeps the idea of each step, not how a real model is trained: a real model writes its
replies token by token instead of choosing from a list, learns from thousands of written answers and rankings across
many prompts, and its reward model is itself a language model. In real reinforcement learning the model writes
replies, the reward model scores them, and an algorithm such as PPO updates the model, with a penalty that keeps it
close to the fine-tuned model it started from; here one step applies each reply's reward directly. It pauses half a
second before each line, so you can read the output one line at a time.

## Run it

```bash
python posttrain.py
```

Nothing is random, so the output is the same every time. Try swapping the first two replies in the ranking, or adding
a reply such as "great question, boil water." to the scores, and predict the reward and the chances before you run it.

## Recorded run

<!-- skillii-kit:run posttrain -->
Recorded run of `python posttrain.py` (27 Nov 2026):

```text
asked: how do i make tea?
fine-tuning data: 7 answers written by people
human ranking: boil water, add the tea. > boil water. > great question!
reply                      pre-trained  fine-tuned  reward  after RL
how do i make coffee?              67%         24%      +0        2%
boil water.                         8%         47%      +2       19%
boil water, add the tea.            8%         24%      +5       78%
great question!                    17%          6%      -2        0%
```

This lab makes no paid request.
<!-- /skillii-kit:run posttrain -->
