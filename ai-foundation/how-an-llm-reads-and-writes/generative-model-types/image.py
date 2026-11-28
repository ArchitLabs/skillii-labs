# An image, the way a diffusion model makes it: start from noise, refine the whole picture each step.
# A toy in plain Python: nothing to install, no network, no key. The "model" is a stand-in that already
# knows the picture, so you see the shape of the work, not the learning.
# A real diffusion model is trained to predict the noise; this one is handed the answer.
import random
import time

SHADES = " ▁▂▃▄▅▆▇█"  # brightness 0 to 8, one character per pixel
PICTURE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # the 18-pixel picture: a hill
STEPS = 5

def show(label, pixels):  # print one row of pixels as shades
    print(f"{label:<8}|{''.join(SHADES[round(p)] for p in pixels)}|")

random.seed(1)  # the same noise on every run
pixels = [random.uniform(0, 8) for _ in PICTURE]  # the start: pure random noise, every pixel
show("noise:", pixels)
for step in range(1, STEPS + 1):
    noise = [p - t for p, t in zip(pixels, PICTURE)]  # one model call: the stand-in predicts the noise
    share = 1 / (STEPS - step + 1)  # remove a share of it: all of what is left by the last step
    pixels = [p - n * share for p, n in zip(pixels, noise)]  # every pixel is refined at once
    time.sleep(0.5)  # a short pause, so each step prints on its own
    show(f"step {step}:", pixels)

print(f"{STEPS} model calls, one per step, each over all {len(PICTURE)} pixels")
