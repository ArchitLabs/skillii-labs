# Eight crawled web pages, filtered and deduplicated the way FineWeb does it, in miniature.
# Plain Python: nothing to install, no network, no key. The output is the same on every run.
# Rules from the FineWeb paper (arXiv 2406.17557), its dataset card and datatrove, read 27 Nov 2026; simplified.
import hashlib, time

def show(line):  # print one line after a short pause, so each line appears on its own
    time.sleep(0.5)
    print(line)

# eight crawled pages: (address, text). Made up for the lab, shaped like real web text.
crawl = [
    ("news.example/rain", "The city will get heavy rain this week, and the schools have closed."),
    ("mirror.example/rain", "the city will get heavy rain this week, and the schools have closed."),
    ("pills.example/buy", "Buy cheap pills now with free delivery to the door."),
    ("blog.example/menu", "Home | About | Contact | Login | Sign up"),
    ("shop.example/sale", "### The best deals of the year ### ### ###"),
    ("dev.example/draft", "Lorem ipsum dolor sit amet, and the page goes on."),
    ("wiki.example/tides", "Tides rise and fall twice a day because of the pull of the moon."),
    ("farm.example/river", "Please enable JavaScript to see the comments.\n"
                           "The river floods in the monsoon, and the farmers move to higher ground."),
]

BLOCKLIST = {"pills.example"}                                          # URL filtering
STOP_WORDS = {"the", "be", "to", "of", "and", "that", "have", "with"}  # Gopher's eight stop words

# the quality filters: the first rule a page breaks is why it is dropped
def why_dropped(url, text):
    if url.split("/")[0] in BLOCKLIST:
        return "url blocklist"
    words = text.split()
    if sum(w.lower() in STOP_WORDS for w in words) < 2:
        return "gopher: fewer than 2 stop words"
    if text.count("#") / len(words) > 0.1:
        return "gopher: too many # symbols"
    if "lorem ipsum" in text.lower() or "{" in text:
        return "c4: lorem ipsum or {"
    return None

show(f"crawled {len(crawl)} pages")
seen, kept = {}, []
for url, text in crawl:
    # C4's line rule: drop any line that mentions javascript, keep the rest of the page
    lines = text.split("\n")
    good = [line for line in lines if "javascript" not in line.lower()]
    if len(good) < len(lines):
        show(f"cut   {url:<20}c4: a line mentions javascript")
    text = "\n".join(good)
    reason = why_dropped(url, text)
    if reason:
        show(f"drop  {url:<20}{reason}")
        continue
    # exact deduplication: the same text, once spaces and case are evened out, has the same hash
    key = hashlib.sha1(" ".join(text.lower().split()).encode()).hexdigest()
    if key in seen:
        show(f"drop  {url:<20}duplicate of {seen[key]}")
        continue
    seen[key] = url
    kept.append(url)
show(f"kept {len(kept)} of {len(crawl)}: {' '.join(kept)}")
