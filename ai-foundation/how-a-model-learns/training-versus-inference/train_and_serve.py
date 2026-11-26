# Training vs inference: train a model once, then use it many times.
# Plain Python: no library, no network, no key. The times vary by machine; the counts do not.
import time

def predict(km, w, b):  # the model: fare = w * km + b
    return w * km + b

# training data: 10 past taxi trips in a made-up city (km, and the fare in rupees)
km = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fare = [42, 54, 66, 78, 90, 102, 114, 126, 138, 150]

# TRAINING: start from w = 0 and b = 0, and nudge them, trip by trip, pass after pass
start = time.perf_counter()
w, b, updates = 0.0, 0.0, 0
for _ in range(5000):
    for x, y in zip(km, fare):
        miss = predict(x, w, b) - y
        w, b = w - 0.005 * miss * x, b - 0.005 * miss
        updates += 1
train_ms = (time.perf_counter() - start) * 1000
print(f"training: 5000 passes over {len(km)} trips = {updates:,} updates in {train_ms:.1f} ms, done once")
print(f"learned: w = {w:.2f}, b = {b:.2f}")

# INFERENCE: the numbers are now fixed; every new trip is one quick call
new_trips = [(i % 250) / 10 for i in range(1_000_000)]
start = time.perf_counter()
fares = [predict(x, w, b) for x in new_trips]
infer_ms = (time.perf_counter() - start) * 1000
print(f"inference: {len(fares):,} new trips, one call each, {infer_ms * 1000 / len(fares):.2f} microseconds per call")
print(f"all {len(fares):,} calls together: {infer_ms:.1f} ms")
print(f"a 7.5 km trip: fare = {predict(7.5, w, b):.2f}")
print(f"after {len(fares):,} calls the numbers are still: w = {w:.2f}, b = {b:.2f}")
