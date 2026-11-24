# Traditional programming: a person writes the rules. Data goes in, answers come out.
# The rules are the ones in Google's "Hello, World" of machine learning codelab.


def activity(speed):
    if speed < 4:
        return "walking"
    elif speed < 12:
        return "running"
    else:
        return "biking"


for speed in [3, 8, 15]:
    print(f"speed {speed}: {activity(speed)}")

# A golfer walks between shots. No speed rule can answer "golf".
print(f"speed 3, playing golf: {activity(3)}")
