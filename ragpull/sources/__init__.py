"""THE SOURCE REGISTRY — every knowledge domain a coding swarm might need to ground itself in.

Curation rules (mirrors the nl-veil atlas):
  1. official documentation first; encyclopedic (Wikipedia/Wikibooks) for concepts with no single owner
  2. every URL must serve real HTML to a plain GET (no JS-walled apps)
  3. concrete content pages over homepages — the normalizer turns ONE page into ONE clean pack file
  4. tags must survive word-bounded matching (never a bare common English word)

Thematic modules aggregate into one DOMAINS dict; names match nl-veil's atlas entries wherever
an atlas entry exists, so pack wiring stays mechanical (many atlas entries may map onto one pack).
"""

import importlib
import pkgutil

# Auto-discover every submodule that exposes a DOMAINS dict (base + thematic + ext_* expansion
# packs). `common` is helpers-only, so it's skipped naturally (no DOMAINS). base loads first so
# a cross-module domain-name collision names the newer module as the offender.
_DOMAIN_OWNER: dict[str, str] = {}
DOMAINS = {}


def _load():
    names = [m.name for m in pkgutil.iter_modules(__path__) if m.name != "common"]
    names.sort(key=lambda n: (n != "base", n))  # base first, then alphabetical
    for modname in names:
        mod = importlib.import_module(f"{__name__}.{modname}")
        table = getattr(mod, "DOMAINS", None)
        if not table:
            continue
        for name, d in table.items():
            if name in DOMAINS:
                raise SystemExit(
                    f"duplicate domain '{name}': in both {_DOMAIN_OWNER[name]} and {modname}"
                )
            DOMAINS[name] = d
            _DOMAIN_OWNER[name] = modname


_load()


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
    s = s.strip("-")[:80] or "page"
    # "index" collides with the pack's INDEX.md on a case-insensitive filesystem (Windows),
    # where index.md and INDEX.md are the same file — reserve it
    return "index-page" if s == "index" else s


def dedupe_slugs():
    """Two URLs in one domain can slug to the same filename (a Wikipedia article and a doc page
    both ending .../graph-database). Keep the FIRST (agents list Wikipedia first — the reliable
    floor) and drop the rest so one page never silently overwrites another at emit time. Returns
    the number dropped. Idempotent."""
    dropped = 0
    for d in DOMAINS.values():
        seen = set()
        kept = []
        for url in d["pages"]:
            s = slug_for(url)
            if s in seen:
                dropped += 1
                continue
            seen.add(s)
            kept.append(url)
        d["pages"] = kept
    return dropped


_SLUG_DROPPED = dedupe_slugs()
