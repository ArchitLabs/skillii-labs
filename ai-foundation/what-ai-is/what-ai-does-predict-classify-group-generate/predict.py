# Predict a number (regression): learn from days whose answers are known, then predict a new day.
# Made-up days: (temperature in C, ice creams sold). The right answers come with the data.

temps = [18, 21, 24, 27, 30, 33]  # data
sold = [92, 110, 127, 141, 163, 178]  # answers (the labels)

# the model: a straight line, sold = w * temperature + b, fitted to the days above
mean_t, mean_s = sum(temps) / len(temps), sum(sold) / len(sold)
w = sum((t - mean_t) * (s - mean_s) for t, s in zip(temps, sold)) / sum((t - mean_t) ** 2 for t in temps)
b = mean_s - w * mean_t

print(f"learned: about {w:.2f} more ice creams for each degree")
print(f"prediction for 26 C: {w * 26 + b:.0f} ice creams")
