# Two programs meet inputs they were not built for: one written by a person, one learned from examples.
# Plain Python: no install, no network, no key.
import time


def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)


def area_written(side):  # normal software: a person wrote the rule, area = side times side
    return side * side


# AI, in miniature: the rule is learned from examples. A straight line is fitted to five
# squares (sides 1 to 5) by least squares, the simplest kind of training.
examples = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
mean_x = sum(x for x, _ in examples) / len(examples)
mean_y = sum(y for _, y in examples) / len(examples)
slope = (sum((x - mean_x) * (y - mean_y) for x, y in examples)
         / sum((x - mean_x) ** 2 for x, _ in examples))
intercept = mean_y - slope * mean_x


def area_learned(side):  # the learned rule: the line that fits the five examples best
    return slope * side + intercept


show(f"learned from sides 1 to 5: area = {slope} * side - {-intercept}")
show("side  written  learned")
for side in (3, 5, 20):  # no line here raises an error, right or wrong
    show(f"{side:>4}  {area_written(side):>7}  {area_learned(side):>7}")

try:  # normal software failing: a bad input stops it with an error you can read
    area_written("20")
except TypeError as err:
    show(f'written, side "20": TypeError: {err}')

# drift: the inputs move from sides 1 to 5 up to sides 16 to 20; the code does not change
for low, high in ((1, 5), (16, 20)):
    errors = [abs(area_learned(s) - area_written(s)) for s in range(low, high + 1)]
    show(f"average error, sides {low} to {high}: {sum(errors) / len(errors)}")
