# The machine learning lifecycle in one small script.
# Will a food delivery arrive late? The app promises 40 minutes.


def orders(first, count, minutes_per_km):
    """Make delivered orders: (distance in km, was it late?)."""
    rows = []
    for i in range(first, first + count):
        km = i % 20 + 1
        rush = 5 if i % 3 == 0 else 0  # every third order hits traffic
        minutes = km * minutes_per_km + rush
        rows.append((km, minutes > 40))
    return rows


def train(rows):
    """Pick the distance to predict late from: fewest mistakes wins."""
    def mistakes(t):
        return sum((km >= t) != late for km, late in rows)
    return min(range(1, 22), key=mistakes)


def accuracy(threshold, rows):
    right = sum((km >= threshold) == late for km, late in rows)
    return 100 * right / len(rows)


# 1. Data: 100 delivered orders, on the old roads (3 minutes a km).
history = orders(0, 100, minutes_per_km=3)
# 2. Split: 60 to train on, 40 held out that training never sees.
train_rows, test_rows = history[:60], history[60:]
print(f"data: {len(train_rows)} orders to train, {len(test_rows)} held out")

# 3. Train, then 4. test on the held-out orders.
threshold = train(train_rows)
print(f"trained: late from {threshold} km")
print(f"held-out test: {accuracy(threshold, test_rows):.1f}%")


# 5. Deploy: the app calls this for every new order.
def predict(km):
    return "late" if km >= threshold else "on time"


print(f"a 12 km order: {predict(12)}")

# 6. Monitor: each week, compare predictions with what really happened.
week1 = orders(100, 20, minutes_per_km=3)
week2 = orders(120, 20, minutes_per_km=4)  # roadworks: 4 minutes a km
for name, week in [("week 1", week1), ("week 2", week2)]:
    score = accuracy(threshold, week)
    print(f"{name}: {score:.1f}%" + ("  ALERT: below 90%" if score < 90 else ""))

# 7. Retrain on weeks 2 to 4 (since the roadworks), then deploy again.
old_threshold = threshold
threshold = train(orders(120, 60, minutes_per_km=4))
print(f"retrained: late from {threshold} km")
week5 = orders(180, 20, minutes_per_km=4)
print(f"week 5, old model: {accuracy(old_threshold, week5):.1f}%")
print(f"week 5, new model: {accuracy(threshold, week5):.1f}%")
print(f"a 12 km order: {predict(12)}")
