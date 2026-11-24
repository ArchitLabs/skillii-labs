# Classify (binary classification): predict a category, rain or no rain, from days whose answers are known.
# Made-up days: (humidity %, what happened). The right answers come with the data.

days = [(35, "no rain"), (42, "no rain"), (50, "no rain"), (58, "no rain"), (63, "rain"),
        (66, "no rain"), (71, "rain"), (75, "rain"), (82, "rain"), (90, "rain")]


def classify(humidity, k=5):
    # the model: the five most similar known days vote, and the vote is a likelihood
    nearest = sorted(days, key=lambda day: abs(day[0] - humidity))[:k]
    likelihood = sum(1 for _, label in nearest if label == "rain") / k
    return likelihood, "rain" if likelihood >= 0.5 else "no rain"


for humidity in (45, 68, 85):
    likelihood, label = classify(humidity)
    print(f"humidity {humidity}%: {label} (likelihood of rain {likelihood:.1f})")
