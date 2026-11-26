# Base model or instruct model? Read how each version of SmolLM2-135M expects its text, from its own files.
# Plain Python: nothing to install, no key, no sign-in, nothing saved. Both are open weights (Apache 2.0).
import json, re, time, urllib.request

VERSIONS = {  # the exact versions read (27 Nov 2026), so every run prints the same
    "SmolLM2-135M": "93efa2f097d58c2a74874c7e644dbc9b0cee75a2",           # the base model
    "SmolLM2-135M-Instruct": "12fd25f77366fa6b3b4b768ec3050bf629380bac",  # the instruct model
}

def settings(name):  # the model's tokenizer settings: one small JSON file from the Hugging Face Hub
    url = f"https://huggingface.co/HuggingFaceTB/{name}/resolve/{VERSIONS[name]}/tokenizer_config.json"
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# 1. does each version have a chat template, and which token ends its text?
base, instruct = settings("SmolLM2-135M"), settings("SmolLM2-135M-Instruct")
for name, s in [("SmolLM2-135M", base), ("SmolLM2-135M-Instruct", instruct)]:
    template = "yes" if "chat_template" in s else "none"
    show(f"{name:<23} chat template: {template:<5} text ends with: {s['eos_token']}")

# 2. a base model reads plain text, and continues it
question = "how do i make tea?"
show(f"base model reads:     {question}")

# 3. the instruct model reads the same question in its own format, laid out as its chat template says
t, start, end = instruct["chat_template"], instruct["bos_token"], instruct["eos_token"]
system = re.search(re.escape(start) + r"system(?:\\n|\n)(.*?)" + re.escape(end), t).group(1)
prompt = (f"{start}system\n{system}{end}\n"   # the default system message, taken from the template
          f"{start}user\n{question}{end}\n"   # the question, as a user message
          f"{start}assistant\n")              # where the model's reply starts
show("instruct model reads:")
for line in prompt.splitlines():
    show(line)
