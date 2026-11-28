# Why guessing wins the test: 100 four-option questions the model has no idea about, graded two ways.
questions = 100
right = questions // 4  # a blind guess on four options is right 1 time in 4
wrong = questions - right

for penalty in (0, 1):  # points lost for each wrong answer
    guess = right - wrong * penalty
    idk = 0  # "I don't know" earns nothing and loses nothing
    print(f"wrong costs {penalty}:  guessing scores {guess:>3}   I don't know scores {idk}")
