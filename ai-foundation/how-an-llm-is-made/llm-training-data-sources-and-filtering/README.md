# LLM Training Data Explained: Where It Comes From

Course: AI Foundation · Section: How an LLM is made

The lab from the SKILLii lesson video *LLM Training Data Explained: Where It Comes From*. Most of the text an LLM is
pre-trained on is crawled from the web, and raw crawl data is noisy: menus, spam, placeholder text and copies of the
same page. [The FineWeb paper](https://arxiv.org/abs/2406.17557) (June 2024) documents how one open dataset was
cleaned: a URL blocklist, text extraction, a language filter, quality and repetition filters (from Gopher's MassiveText
and from C4), and deduplication. This lab runs a few of those rules over eight made-up pages so you can see each one
remove something.

| Script | What it shows | Cost to run |
|---|---|---|
| `clean.py` | Eight crawled pages go through a URL blocklist, two of Gopher's quality rules (at least 2 of its eight stop words; at most 0.1 `#` symbols per word), two of C4's rules (drop a line that mentions javascript; drop a page with "lorem ipsum" or a curly bracket), and exact deduplication by hash. It prints why each page or line was removed and which pages are kept | free |

The script uses only Python itself: nothing to install, no network, no key. It creates nothing and leaves nothing to
tidy up. It is a simplified miniature, not FineWeb's pipeline: the real one runs on billions of pages with
[datatrove](https://github.com/huggingface/datatrove), extracts text from raw HTML with trafilatura, keeps only text a
fastText classifier scores as English, applies more rules (Gopher's also needs 50 to 100,000 words per page), and finds
near-duplicates with MinHash rather than exact copies. The rule thresholds used here are the defaults in datatrove's
[`gopher_quality_filter.py`](https://github.com/huggingface/datatrove/blob/main/src/datatrove/pipeline/filters/gopher_quality_filter.py)
and the C4 rules named in the paper. It pauses half a second before each line, so you can read the output one line at
a time.

## Run it

```bash
python clean.py
```

Nothing is random, so the output is the same every time.

## Recorded run

<!-- skillii-kit:run clean -->
Recorded run of `python clean.py` (27 Nov 2026):

```text
crawled 8 pages
drop  mirror.example/rain duplicate of news.example/rain
drop  pills.example/buy   url blocklist
drop  blog.example/menu   gopher: fewer than 2 stop words
drop  shop.example/sale   gopher: too many # symbols
drop  dev.example/draft   c4: lorem ipsum or {
cut   farm.example/river  c4: a line mentions javascript
kept 3 of 8: news.example/rain wiki.example/tides farm.example/river
```

This lab makes no paid request.
<!-- /skillii-kit:run clean -->
