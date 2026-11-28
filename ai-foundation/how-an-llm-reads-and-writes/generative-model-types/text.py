# Text, the way a large language model writes it: one model call for each new token.
# A toy in plain Python: nothing to install, no network, no key. The "model" is a stand-in that already
# knows its answer, so you see the shape of the work, not the learning. The tokens are split by hand.
import time

ANSWER = ["Diffusion", " starts", " from", " random", " noise", "."]  # what the stand-in will write

def model(tokens_so_far):  # the stand-in: it reads the tokens so far and returns the next one
    return ANSWER[len(tokens_so_far)]

tokens = []
while len(tokens) < len(ANSWER):  # a real model stops when it writes its end token
    tokens.append(model(tokens))  # one model call adds one token to the end
    time.sleep(0.5)  # a short pause, so each call prints on its own
    print(f"call {len(tokens)}: {''.join(tokens)}")

print(f"{len(tokens)} model calls for {len(tokens)} tokens: a longer answer needs more calls")
