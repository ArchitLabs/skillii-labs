# Loss: one number for how wrong a model is. Training is the work of making that number smaller.
# Plain Python: no library, no network, no key. The data is made up, and the output is the same on every run.

# data: three past deliveries (the distance in km, and the minutes each one took)
km = [1, 5, 7]
minutes = [5, 17, 30]

def loss(w):  # the model guesses minutes = w * km; its loss is the mean of the squared misses
    misses = [w * x - y for x, y in zip(km, minutes)]
    return sum(m * m for m in misses) / len(misses)

# three guesses for w on the same data: the lower the loss, the better the fit
for w in [2.0, 3.0, 3.5]:
    print(f"guess w = {w}: loss {loss(w):.2f}")

# training: start at w = 0, and step w downhill on the loss until the loss stops falling
w, rate = 0.0, 0.01  # rate: how far each step moves w
before = loss(w)
print(f"start: w = 0, loss {before:.2f}")
for n in range(1, 101):
    slope = 2 * sum((w * x - y) * x for x, y in zip(km, minutes)) / len(km)  # which way is downhill
    w -= rate * slope
    now = loss(w)
    print(f"step {n}: loss {now:.2f}")
    if before - now < 0.01:  # it fell by less than 0.01: the loss has levelled off
        print(f"converged at step {n}: learned w = {w:.2f} minutes per km")
        break
    before = now
