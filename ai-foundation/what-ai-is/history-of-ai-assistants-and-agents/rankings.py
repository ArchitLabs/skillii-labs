# How one ranking becomes many training pairs for a reward model.
# InstructGPT ("Training language models to follow instructions with
# human feedback", section 3.5): labelers rank K = 4 to 9 answers to
# one prompt, and every pair in the ranking becomes one comparison.
from itertools import combinations

# A labeler ranked four answers to one prompt, best first.
ranking = ["A", "B", "C", "D"]

print("ranking: " + " > ".join(ranking))
for better, worse in combinations(ranking, 2):
    print(f"  {better} is preferred to {worse}")

# How many comparisons one ranking gives, from K = 4 to K = 9.
for k in range(4, 10):
    pairs = len(list(combinations(range(k), 2)))
    print(f"K = {k}: {pairs} comparisons")
