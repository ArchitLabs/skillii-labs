# A model is a function whose numbers were learned from data.
# Same code, two data sets, two different models. Plain Python: no library, no network, no key.

def f(x, w, b):  # the model's shape: y = w * x + b, where w and b are its parameters
    return w * x + b

def fit(xs, ys):  # learn w and b from examples: the line that best fits the points (least squares)
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    w = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return w, my - w * mx

# data A: the same temperatures, read in Celsius and in Fahrenheit
celsius = [0, 10, 25, 37, 100]
fahrenheit = [32, 50, 77, 98.6, 212]

# data B: a made-up shop, kilograms of rice and the bill in rupees
kg = [1, 2, 5, 10]
bill = [80, 140, 320, 620]

temp_w, temp_b = fit(celsius, fahrenheit)
rice_w, rice_b = fit(kg, bill)
print(f"temperature model learned: w = {temp_w:.2f}, b = {temp_b:.2f}")
print(f"rice model learned: w = {rice_w:.2f}, b = {rice_b:.2f}")

# call each model like any function, on an input it never saw
print(f"temperature model: f(20) = {f(20, temp_w, temp_b):.2f}")
print(f"rice model: f(20) = {f(20, rice_w, rice_b):.2f}")
