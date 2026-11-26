# Post-training at toy size: fine-tuning on answers people wrote, a reward model trained on a human ranking, and
# reinforcement learning against that reward model. Plain Python: nothing to install, no network, no key.
import time

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# the model: a score for each reply it could give; each extra point doubles that reply's chance
prompt = "how do i make tea?"
score = {"how do i make coffee?": 3, "boil water.": 0, "boil water, add the tea.": 0, "great question!": 1}

def chances():
    total = sum(2 ** s for s in score.values())
    return {reply: f"{100 * 2 ** s / total:.0f}%" for reply, s in score.items()}

pretrained = chances()  # after pre-training it carries on a page of questions

# step 1, fine-tuning: train further on answers people wrote; each one raises its reply's score
written = ["boil water."] * 4 + ["boil water, add the tea."] * 3
for answer in written:
    score[answer] += 1
finetuned = chances()

# step 2, the reward model: people ranked three replies, best first; it learns the words of the better reply
ranking = ["boil water, add the tea.", "boil water.", "great question!"]

def words(reply):  # the words of a reply, without punctuation
    return set(reply.replace(",", "").strip(".?!").split())

vote = {}
for better, worse in zip(ranking, ranking[1:]):
    for w in words(better) - words(worse):
        vote[w] = vote.get(w, 0) + 1
    for w in words(worse) - words(better):
        vote[w] = vote.get(w, 0) - 1
reward = {reply: sum(vote.get(w, 0) for w in words(reply)) for reply in score}

# step 3, reinforcement learning: each reply's score moves by the reward the reward model gives it
for reply in score:
    score[reply] += reward[reply]
after = chances()

show(f"asked: {prompt}")
show(f"fine-tuning data: {len(written)} answers written by people")
show("human ranking: " + " > ".join(ranking))
show(f"{'reply':<26}{'pre-trained':>12}{'fine-tuned':>12}{'reward':>8}{'after RL':>10}")
for reply in score:
    show(f"{reply:<26}{pretrained[reply]:>12}{finetuned[reply]:>12}{reward[reply]:>+8}{after[reply]:>10}")
