# Count GPT-3's parameters from the shapes its paper lists (Table 2.1),
# with the rule in "Scaling Laws for Neural Language Models", section 2.1:
# each layer holds about 12 x width x width weights (embeddings left out).

# (name, layers, width d_model, the parameter count the paper lists)
MODELS = [
    ("GPT-3 Small", 12, 768, "125M"),
    ("GPT-3 13B", 40, 5140, "13.0B"),
    ("GPT-3 175B", 96, 12288, "175.0B"),
]


def layer_weights(layers, width):
    return 12 * layers * width * width


for name, layers, width, listed in MODELS:
    counted = layer_weights(layers, width)
    print(f"{name}: {layers} layers, width {width}")
    print(f"  counted: {counted:,}  paper: {listed}")
