# One design, three families: which halves of the Transformer does each model keep? Read each model's own config file.
# Plain Python: nothing to install, no key, no sign-in, nothing saved. Only small JSON files, never the weights.
import json, time, urllib.request

MODELS = {  # the exact versions read (28 Nov 2026), so every run prints the same
    "google-bert/bert-base-uncased": "86b5e0934494bd15c9632b12f734a8a67f723594",  # BERT
    "google-t5/t5-small": "df1b051c49625cf57a3d0d8d3863ed4d13564fe4",             # T5
    "Qwen/Qwen3-8B": "b968826d9c46dd6066d109eabc6255188de91218",                  # Qwen3, a chat model
}

def config(repo):  # the model's configuration: one small JSON file from the Hugging Face Hub
    url = f"https://huggingface.co/{repo}/resolve/{MODELS[repo]}/config.json"
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

def layers(n):
    return f"{n} layers" if n else "none"

for repo in MODELS:
    c = config(repo)
    job = c["architectures"][0]  # the model's class: the job its last layer is trained for
    if c.get("is_encoder_decoder"):  # both halves; T5's decoder has as many layers unless the file says otherwise
        encoder, decoder = c["num_layers"], c.get("num_decoder_layers", c["num_layers"])
    elif job.endswith("ForCausalLM"):  # predicts the next token: the decoder half only
        encoder, decoder = 0, c["num_hidden_layers"]
    else:  # BERT fills in hidden words: the encoder half only
        encoder, decoder = c["num_hidden_layers"], 0
    heads = c.get("num_attention_heads") or c["num_heads"]  # T5 names its settings differently
    width = c.get("hidden_size") or c["d_model"]  # how many numbers stand for each token
    show(f"{repo}: {job}")
    show(f"  encoder: {layers(encoder)}   decoder: {layers(decoder)}")
    show(f"  {heads} attention heads, {width:,} numbers per token, vocabulary {c['vocab_size']:,}")
