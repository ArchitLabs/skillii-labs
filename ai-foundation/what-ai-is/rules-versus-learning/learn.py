# Machine learning: data and answers go in, and training works out the rule.
# The data and answers are the ones in Google's "Hello, World" of machine learning codelab.

xs = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]  # data
ys = [-2.0, 1.0, 4.0, 7.0, 10.0, 13.0]  # answers (the labels)

w, b = 0.0, 0.0  # the model: two values, not a rule anyone wrote
step = 0.01  # how far each round moves the values

for n in range(1, 501):
    # predict, then measure the error: the mean of the squared misses
    guesses = [w * x + b for x in xs]
    misses = [g - y for g, y in zip(guesses, ys)]
    error = sum(m * m for m in misses) / len(xs)
    # adjust both values a small amount in the direction that reduces the error
    w -= step * 2 * sum(m * x for m, x in zip(misses, xs)) / len(xs)
    b -= step * 2 * sum(misses) / len(xs)
    if n in (1, 10, 100, 500):
        print(f"round {n}: error {error:.4f}")

print(f"learned values: w = {w:.4f}, b = {b:.4f}")
print(f"prediction for x = 10: {w * 10 + b:.4f}")
