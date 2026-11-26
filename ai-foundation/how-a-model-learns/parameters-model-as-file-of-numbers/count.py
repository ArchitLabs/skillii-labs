# What does the "8B" in Qwen3-8B count? Read the model's own files on Hugging Face, without downloading its weights.
# Plain Python: nothing to install, no key, no sign-in, nothing saved. Qwen3-8B is open weights (Apache 2.0).
import json, time, urllib.request

REPO = "Qwen/Qwen3-8B"
REV = "b968826d9c46dd6066d109eabc6255188de91218"  # the exact version read (26 Nov 2026): every run prints the same

def get(path):  # one small JSON file from the Hugging Face Hub
    with urllib.request.urlopen(f"https://huggingface.co/{path}", timeout=30) as r:
        return json.load(r)

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# file 1, the configuration: a few numbers that fix the shape of every part of the model
c = get(f"{REPO}/resolve/{REV}/config.json")
h, layers, vocab = c["hidden_size"], c["num_hidden_layers"], c["vocab_size"]
q, kv = c["num_attention_heads"] * c["head_dim"], c["num_key_value_heads"] * c["head_dim"]
show(f"model: {REPO}")
show(f"config.json: {layers} layers, hidden size {h:,}, vocabulary {vocab:,}")

# count the numbers: a weight matrix with r rows and k columns holds r x k numbers
attention = h * q + h * kv + h * kv + q * h        # the query, key, value and output matrices
mlp = 3 * h * c["intermediate_size"]               # the gate, up and down matrices
norms = 2 * h + 2 * c["head_dim"]                  # four small scaling vectors
layer = attention + mlp + norms
outside = 2 * vocab * h + h  # a token table in, a token table out (Qwen3-8B keeps two), a final scaling vector
total = layers * layer + outside
show(f"one layer:         {layer:>13,} numbers")
show(f"{layers} layers:         {layers * layer:>13,} numbers")
show(f"outside layers:    {outside:>13,} numbers")
show(f"total:             {total:>13,} numbers = {total / 1e9:.1f}B")

# file 2, the weights: how many bytes the numbers fill, and the files on disk
size = get(f"{REPO}/resolve/{REV}/model.safetensors.index.json")["metadata"]["total_size"]
files = [f for f in get(f"api/models/{REPO}/tree/{REV}") if f["path"].endswith(".safetensors")]
show(f"weights: {size:,} bytes = {size / total:g} bytes a number ({c['torch_dtype']})")
show(f"on disk: {len(files)} files, {sum(f['size'] for f in files) / 1e9:.1f} GB")

# the memory just to hold the numbers: 2 bytes each as shipped, 1 byte each at 8 bits
show(f"to load: {total * 2 / 1e9:.1f} GB at 2 bytes a number, {total / 1e9:.1f} GB at 1 byte")
