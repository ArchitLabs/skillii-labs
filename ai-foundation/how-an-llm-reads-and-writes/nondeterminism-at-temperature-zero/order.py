# Same numbers, different order, different sum: enough to change the word temperature 0 picks.
# Plain Python: no install, no network, no key.
import time


def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)


def add_up(numbers):  # add left to right, one number at a time
    total = 0.0
    for n in numbers:
        total = total + n
    return total


def add_split(numbers):  # split the work: add the rest first, then the first number
    return numbers[0] + add_up(numbers[1:])


show(f"(0.1 + 0.2) + 0.3 = {add_up([0.1, 0.2, 0.3])}")
show(f"0.1 + (0.2 + 0.3) = {add_split([0.1, 0.2, 0.3])}")

# made-up scores for two next words: the same three parts, so on paper both are exactly 0.6, a tie
parts = {"Paris": [0.1, 0.2, 0.3], "Lyon": [0.2, 0.3, 0.1]}

for label, add in (("in one go:", add_up), ("split up:", add_split)):
    scores = {word: add(numbers) for word, numbers in parts.items()}
    top = max(scores, key=scores.get)  # temperature 0: always take the highest score
    show(f"{label:<12} Paris {scores['Paris']}  Lyon {scores['Lyon']}  -> picks {top}")
