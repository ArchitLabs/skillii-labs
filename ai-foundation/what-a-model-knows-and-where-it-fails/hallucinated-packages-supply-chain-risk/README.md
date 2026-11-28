# When AI Invents a Package Name: A Supply-Chain Risk

Course: AI Foundation · Section: What a model knows, and where it fails

The lab from the SKILLii lesson video *When AI Invents a Package Name: A Supply-Chain Risk*. It follows Spracklen et
al., [We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating
LLMs](https://arxiv.org/abs/2406.10279) (2025), and OWASP's
[LLM09:2025 Misinformation](https://genai.owasp.org/llmrisk/llm092025-misinformation/).

| Script | What it shows | Cost to run |
|---|---|---|
| `check.py` | **Check a suggested dependency before you install it.** It looks up four package names, as if an AI assistant had suggested them, in PyPI's public [JSON API](https://docs.pypi.org/api/json/) (`GET /pypi/<project>/json`). A name PyPI knows returns its metadata, and the script prints the latest version and the date of the first upload. A name PyPI does not know returns 404. The last two names were made up for this lab | free |

Do not install the two made-up names. A missing name is exactly what an attacker can register later, so "it
exists" is not enough on its own: look at who publishes a package, how long it has been on PyPI, and whether it is
the project you meant.

The script only reads public data: it publishes nothing, registers nothing, installs nothing and leaves nothing to
tidy up. It uses only Python itself, and needs no key.

## Run it

```
python check.py
```

The versions and dates printed for the real packages change as they publish new releases.

## Recorded run

<!-- skillii-kit:run check -->
Recorded run of `python check.py` (28 Nov 2026):

```text
requests                      on PyPI  latest 2.34.2  first upload 2011-02-14
flask                         on PyPI  latest 3.1.3  first upload 2010-04-16
skillii-made-up-csv-helper    not on PyPI (404)
skillii-made-up-json-cleaner  not on PyPI (404)
2 of 4 names are not on PyPI: skillii-made-up-csv-helper, skillii-made-up-json-cleaner
```

This lab makes no paid request.
<!-- /skillii-kit:run check -->
