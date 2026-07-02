"""Autonomous frontier discovery — find NEW, on-topic Wikipedia article titles that are not
yet in the registry, so the hourly grower always has fresh, usable candidates to admit.

Two complementary sources (Wikipedia has ~7M articles; the technical subgraph is hundreds of
thousands, so this never runs dry before the repo hits its size limit):
  1. CATEGORY WALK — enumerate article + subcategory members of broad technical categories
     (recursing one level into subcats), via the MediaWiki API.
  2. LINK EXPANSION — outbound namespace-0 links of already-accepted pages, so growth follows
     the real topic graph outward from what we already cover.

Stdlib only. Polite: a small delay between API calls, a descriptive User-Agent.
"""

import json
import time
import urllib.parse
import urllib.request

API = "https://en.wikipedia.org/w/api.php"
UA = "nl-rag-grower/1.0 (+https://github.com/gary23w/nl-rag; scheduled RAG builder)"
WIKI = "https://en.wikipedia.org/wiki/"

# broad, article-rich technical seed categories — the roots of the frontier walk
SEED_CATEGORIES = [
    "Algorithms", "Data structures", "Programming languages", "Software engineering",
    "Computer programming", "Areas of computer science", "Theory of computation",
    "Computational complexity theory", "Formal methods", "Compiler construction",
    "Operating systems", "Computer networking", "Network protocols", "Internet protocols",
    "Databases", "Distributed computing", "Concurrent computing", "Cryptography",
    "Computer security", "Machine learning", "Artificial intelligence", "Deep learning",
    "Natural language processing", "Computer vision", "Digital signal processing",
    "Numerical analysis", "Mathematical optimization", "Graph theory", "Combinatorics",
    "Number theory", "Abstract algebra", "Mathematical analysis", "Topology",
    "Probability theory", "Statistics", "Mathematical logic", "Control theory",
    "Electronic circuits", "Electrical engineering", "Digital electronics",
    "Microcontrollers", "Embedded systems", "Computer hardware", "Computer architecture",
    "Telecommunications", "Wireless networking", "Robotics", "Automation",
    "Computer graphics", "Rendering (computer graphics)", "Video game development",
    "Web development", "World Wide Web", "Software design patterns", "Software architecture",
    "Cloud computing", "Virtualization", "Version control", "Software testing",
    "Chemistry", "Physical chemistry", "Materials science", "Molecular biology",
    "Bioinformatics", "Genetics", "Neuroscience", "Physics", "Classical mechanics",
    "Quantum mechanics", "Electromagnetism", "Thermodynamics", "Optics", "Acoustics",
    "Signal processing", "Information theory", "Coding theory", "Systems theory",
    "Operations research", "Game theory", "Computational science", "Computational physics",
    "Data management", "Data mining", "Big data", "Functional programming",
    "Object-oriented programming", "Concurrency (computer science)", "Parallel computing",
    "Computer file formats", "Character encoding", "Markup languages", "Query languages",
]

# titles that gate poorly (nav / list / meta pages) — never admit these
_SKIP_PREFIXES = (
    "List of", "Lists of", "Index of", "Outline of", "Timeline of", "Comparison of",
    "Glossary of", "History of", "Bibliography of",
)
# citation-template + administrative link targets that ride outbound links but add no topical value
_SKIP_CONTAINS = ("(identifier)",)
_GENERIC = {
    "Academic journal", "Academic conference", "ArXiv", "Digital object identifier", "ISBN",
    "ISSN", "PubMed", "PubMed Central", "Bibcode", "Wayback Machine", "JSTOR", "OCLC",
    "Semantic Scholar", "Google Scholar", "Citation", "Wikidata", "Application software",
    "Software", "Computer", "Internet", "Website", "Encyclopedia", "Book", "Author",
}


def _api(params: dict, tries: int = 4) -> dict:
    params = {**params, "format": "json", "formatversion": "2"}
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    last = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:  # transient rate-limit / network — back off and retry
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"MediaWiki API failed: {last}")


def _is_admissible_title(title: str) -> bool:
    if not title or ":" in title:  # ":" ⇒ a namespace (Category:, Template:, Portal:, …)
        return False
    if "(disambiguation)" in title or title in _GENERIC:
        return False
    if any(s in title for s in _SKIP_CONTAINS):
        return False
    return not title.startswith(_SKIP_PREFIXES)


def category_members(category: str, want_subcats: bool = True):
    """(article_titles, subcategory_names) for a category, one API page (up to 500 each)."""
    r = _api({
        "action": "query", "list": "categorymembers",
        "cmtitle": f"Category:{category}",
        "cmtype": "page|subcat" if want_subcats else "page",
        "cmlimit": "500",
    })
    arts, subs = [], []
    for m in r.get("query", {}).get("categorymembers", []):
        t = m.get("title", "")
        if t.startswith("Category:"):
            subs.append(t[len("Category:"):])
        elif _is_admissible_title(t):
            arts.append(t)
    time.sleep(0.4)
    return arts, subs


def page_links(title: str, limit: int = 60):
    """Outbound namespace-0 (article) links from a page — the local topic graph."""
    r = _api({
        "action": "query", "prop": "links", "titles": title,
        "plnamespace": "0", "pllimit": str(limit),
    })
    out = []
    for pg in r.get("query", {}).get("pages", []):
        for l in pg.get("links", []):
            t = l.get("title", "")
            if _is_admissible_title(t):
                out.append(t)
    time.sleep(0.4)
    return out


def title_to_url(title: str) -> str:
    return WIKI + urllib.parse.quote(title.replace(" ", "_"), safe="_(),'!-./:%&")


def discover(rng, want: int, is_new, seed_titles=None):
    """Yield up to `want` candidate (title, url, hint) tuples that pass `is_new(url)`.
    `hint` is a coarse tag hint (the source category or 'linked'). Mixes a category walk
    with link-expansion from `seed_titles` (recently-accepted pages) for a durable frontier."""
    seen_titles = set()
    produced = 0

    def emit(title, hint):
        nonlocal produced
        if title in seen_titles:
            return False
        seen_titles.add(title)
        url = title_to_url(title)
        if not is_new(url):
            return False
        produced += 1
        return (title, url, hint)

    # 1) link-expansion from already-accepted pages (follows the real topic graph outward)
    for st in (seed_titles or [])[:12]:
        if produced >= want:
            break
        try:
            links = page_links(st)
        except Exception:
            continue
        rng.shuffle(links)
        for t in links:
            if produced >= want:
                break
            c = emit(t, "linked")
            if c:
                yield c

    # 2) category walk (root cats + one level of subcats), randomized for breadth over runs
    cats = list(SEED_CATEGORIES)
    rng.shuffle(cats)
    for cat in cats:
        if produced >= want:
            break
        try:
            arts, subs = category_members(cat)
        except Exception:
            continue
        rng.shuffle(subs)
        for sub in subs[:6]:  # descend one level for fresh frontier
            try:
                sub_arts, _ = category_members(sub, want_subcats=False)
                arts.extend(sub_arts)
            except Exception:
                pass
            if len(arts) > 1200:
                break
        rng.shuffle(arts)
        for t in arts:
            if produced >= want:
                break
            c = emit(t, cat.lower())
            if c:
                yield c
