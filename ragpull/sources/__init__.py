"""THE SOURCE REGISTRY — every knowledge domain a coding swarm might need to ground itself in.

Curation rules (mirrors the nl-veil atlas):
  1. official documentation first; encyclopedic (Wikipedia/Wikibooks) for concepts with no single owner
  2. every URL must serve real HTML to a plain GET (no JS-walled apps)
  3. concrete content pages over homepages — the normalizer turns ONE page into ONE clean pack file
  4. tags must survive word-bounded matching (never a bare common English word)

Thematic modules aggregate into one DOMAINS dict; names match nl-veil's atlas entries wherever
an atlas entry exists, so pack wiring stays mechanical (many atlas entries may map onto one pack).
"""

from . import (
    base,
    books_rosetta,
    cs_systems,
    data_ai,
    embedded_iot,
    languages,
    mathematics,
    paradigms_problem,
    patterns_practice,
    web_cloud,
)

_MODULES = [
    base, languages, paradigms_problem, embedded_iot, mathematics,
    cs_systems, patterns_practice, data_ai, web_cloud, books_rosetta,
]

DOMAINS = {}
for _m in _MODULES:
    for _name, _d in _m.DOMAINS.items():
        if _name in DOMAINS:
            raise SystemExit(f"duplicate domain across modules: {_name} ({_m.__name__})")
        DOMAINS[_name] = _d


def slug_for(url: str) -> str:
    """Stable filesystem slug for a page URL: last meaningful path segments, lowercased,
    [a-z0-9-] only. Distinct URLs in one domain never collide (verified at registry load)."""
    from urllib.parse import urlparse, unquote

    p = urlparse(url)
    path = unquote(p.path).strip("/")
    if not path:
        path = p.netloc.replace(".", "-")
    segs = [s for s in path.split("/") if s not in ("", "en-US", "en", "docs", "wiki", "w", "stable", "current", "master", "3")]
    tail = segs[-2:] if len(segs) >= 2 and len(segs[-1]) < 12 else segs[-1:]
    raw = "-".join(tail)
    for suf in (".html", ".xhtml", ".php", ".1", ".2", ".5", ".7", ".8"):
        if raw.endswith(suf):
            raw = raw[: -len(suf)]
    out = []
    for c in raw.lower():
        out.append(c if c.isalnum() else "-")
    s = "".join(out)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")[:80] or "page"


def check_registry():
    """Fail fast on slug collisions inside a domain."""
    for name, d in DOMAINS.items():
        seen = {}
        for url in d["pages"]:
            s = slug_for(url)
            if s in seen:
                raise SystemExit(f"slug collision in {name}: {seen[s]} vs {url} -> {s}")
            seen[s] = url


check_registry()
