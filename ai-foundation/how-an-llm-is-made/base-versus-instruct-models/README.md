# Base Model vs Instruct Model: What's the Difference?

Course: AI Foundation · Section: How an LLM is made

The lab from the SKILLii lesson video *Base Model vs Instruct Model: What's the Difference?*. Many models come in two
versions. As the [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter11/2) puts it, "A base model
is trained on raw text data to predict the next token, while an instruct model is fine-tuned specifically to follow
instructions and engage in conversations". An instruct model also expects its text in its own format, written down in
the chat template of its tokenizer settings. This lab reads those settings for both versions of
[SmolLM2-135M](https://huggingface.co/HuggingFaceTB/SmolLM2-135M) and
[SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct), open-weights models (Apache 2.0)
that anyone can read without signing in.

| Script | What it shows | Cost to run |
|---|---|---|
| `template.py` | Reads each version's `tokenizer_config.json` and prints whether it has a chat template and which token ends its text. Then it shows one question as the base model reads it (plain text, to be continued) and as the instruct model reads it: wrapped in the `<\|im_start\|>` and `<\|im_end\|>` markers its chat template uses, with the default system message taken from that template, and ending where the model's reply starts | free |

The script uses only Python itself: nothing to install, no key, no sign-in. It reads two small JSON files from
huggingface.co, never the model weights, and saves nothing, so there is nothing to tidy up. It reads one fixed version
of each repository, so the output is the same on every run. It pauses half a second before each line, so you can read
the output one line at a time.

The script lays the question out by following the template's own pattern in Python. In your own code, let the
tokenizer do it: the `transformers` library's `apply_chat_template` reads the same template and runs it, and its `add_generation_prompt=True` adds the last line, where the reply
starts.

## Run it

```bash
python template.py
```

## Recorded run

<!-- skillii-kit:run template -->
Recorded run of `python template.py` (27 Nov 2026):

```text
SmolLM2-135M            chat template: none  text ends with: <|endoftext|>
SmolLM2-135M-Instruct   chat template: yes   text ends with: <|im_end|>
base model reads:     how do i make tea?
instruct model reads:
<|im_start|>system
You are a helpful AI assistant named SmolLM, trained by Hugging Face<|im_end|>
<|im_start|>user
how do i make tea?<|im_end|>
<|im_start|>assistant
```

This lab makes no paid request.
<!-- /skillii-kit:run template -->
