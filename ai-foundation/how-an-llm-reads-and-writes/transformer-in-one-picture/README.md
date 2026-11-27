# The Transformer Explained in One Picture

Course: AI Foundation · Section: How an LLM reads and writes

The lab from the SKILLii lesson video *The Transformer Explained in One Picture*. The Transformer of 2017 has two
halves: an encoder that reads the input and a decoder that writes the output one token at a time. Models since then
keep both halves or only one. This lab reads the configuration file of three open models on the Hugging Face Hub and
prints which halves each keeps, how many layers each half has, and the sizes that tie the picture together: attention
heads, how many numbers stand for each token, and how many tokens the vocabulary holds.

| Script | What it shows | Cost to run |
|---|---|---|
| `halves.py` | Reads `config.json` of BERT (`google-bert/bert-base-uncased`), T5 (`google-t5/t5-small`) and Qwen3 (`Qwen/Qwen3-8B`), each pinned to an exact version, and prints each model's class, its encoder and decoder layers, its attention heads, its numbers per token and its vocabulary | free |

The script uses only Python itself: nothing to install, no key, no sign-in. It reads three small JSON files from
huggingface.co, never the weights, and saves nothing, so there is nothing to tidy up. It pauses half a second before
each line, so you can read the output one line at a time.

## Run it

```bash
python halves.py
```

## Recorded run

<!-- skillii-kit:run halves -->
Recorded run of `python halves.py` (28 Nov 2026):

```text
google-bert/bert-base-uncased: BertForMaskedLM
  encoder: 12 layers   decoder: none
  12 attention heads, 768 numbers per token, vocabulary 30,522
google-t5/t5-small: T5ForConditionalGeneration
  encoder: 6 layers   decoder: 6 layers
  8 attention heads, 512 numbers per token, vocabulary 32,128
Qwen/Qwen3-8B: Qwen3ForCausalLM
  encoder: none   decoder: 36 layers
  32 attention heads, 4,096 numbers per token, vocabulary 151,936
```

This lab makes no paid request.
<!-- /skillii-kit:run halves -->
