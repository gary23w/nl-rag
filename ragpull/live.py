"""LIVE FALLBACK — answer a query the corpus does not cover, normalized the same way.

The published API is static files: it cannot fetch anything at request time. So when a
lookup misses, resolution happens where compute is free — on the consumer's machine
(`ragpull resolve` / `ragpull serve`) or on a CI runner. This module is that path.

WHY THE FETCHER IS HAND-ROLLED
------------------------------
The escalation methodology here is ported from curl_cffi / curl-impersonate rather than
imported: `ragpull` is stdlib-only on purpose, and a bundled libcurl binary is exactly the
kind of thing an endpoint-protection product shoots on sight. What ports cleanly:

  * complete browser header SETS in the order a real browser sends them, including the
    sec-ch-ua client hints and Sec-Fetch-* metadata that naive clients omit entirely
  * a cookie jar, so a wall that sets a cookie and redirects is satisfied by round two
  * Referer chains and a real navigation shape (document request, then same-origin subs)
  * TLS knobs the ssl module does expose: cipher-suite ORDER, protocol floor/ceiling,
    ALPN, and session-ticket behaviour

WHAT DOES NOT PORT — stated plainly so nobody mistakes this for full impersonation:
curl-impersonate's real leverage is the exact TLS ClientHello fingerprint (JA3: GREASE
values, extension count and ordering, supported-groups and signature-algorithm lists) and
the HTTP/2 SETTINGS/priority frames. `http.client` speaks HTTP/1.1 and gives no hook for
extension ordering, so the JA3 hash is still Python's. This beats a bare urllib
User-Agent on documentation sites and soft walls; it will not beat a check that matches
JA3 or requires HTTP/2. When a site needs that, the honest answer is that the page is not
retrievable here — and the resolver reports the failure rather than inventing content.

Everything admitted goes through the SAME fetch -> normalize -> clean-data gates as every
hand-curated pack, so a live answer is shaped exactly like a corpus answer.
"""

import gzip
import http.cookiejar
import io
import json
import random
import ssl
import time
import urllib.error
import urllib.request
import zlib
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from . import verify
from .fetch import FetchError, HOST_DELAY_S, MAX_BYTES, _decode, fetch
from .normalize import normalize, split_markdown
from .sources import slug_for

# ---------------------------------------------------------------- content encodings
# Only advertise what we can actually decode: claiming br/zstd and then failing to inflate
# turns a working fetch into garbage. Chrome sends "gzip, deflate, br, zstd"; we send the
# prefix we can honour, which is itself a small fingerprint difference we accept.


def _encodings() -> tuple[str, dict]:
    decoders = {
        "gzip": lambda b: gzip.GzipFile(fileobj=io.BytesIO(b)).read(MAX_BYTES),
        "deflate": lambda b: zlib.decompressobj(-zlib.MAX_WBITS).decompress(b, MAX_BYTES),
        "identity": lambda b: b,
    }
    names = ["gzip", "deflate"]
    for mod, name in (("brotli", "br"), ("brotlicffi", "br")):
        try:
            m = __import__(mod)
        except ImportError:
            continue
        decoders["br"] = lambda b, _m=m: _m.decompress(b)
        names.append("br")
        break
    try:                                        # stdlib zstd landed in 3.14
        from compression import zstd as _zstd
        decoders["zstd"] = lambda b: _zstd.decompress(b)
        names.append("zstd")
    except Exception:
        pass
    return ", ".join(names), decoders


ACCEPT_ENCODING, _DECODERS = _encodings()

# ---------------------------------------------------------------- browser profiles
# Header ORDER matters — it is part of what a fingerprinter looks at — and dicts preserve
# insertion order, so these are written in the order the browser actually emits them.
# Cipher strings are OpenSSL names in the browser's preference order.

_CHROME_CIPHERS = (
    "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:"
    "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:"
    "ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:"
    "ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:"
    "AES256-GCM-SHA384:AES128-SHA:AES256-SHA"
)
_FIREFOX_CIPHERS = (
    "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:"
    "ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:"
    "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:"
    "ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:"
    "ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA:AES256-SHA"
)

PROFILES: dict[str, dict] = {
    "chrome": {
        "ciphers": _CHROME_CIPHERS,
        "headers": {
            "sec-ch-ua": '"Chromium";v="126", "Not:A-Brand";v="24", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"),
            "Accept": ("text/html,application/xhtml+xml,application/xml;q=0.9,"
                       "image/avif,image/webp,image/apng,*/*;q=0.8,"
                       "application/signed-exchange;v=b3;q=0.7"),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": ACCEPT_ENCODING,
            "Accept-Language": "en-US,en;q=0.9",
            "Priority": "u=0, i",
        },
    },
    "firefox": {
        "ciphers": _FIREFOX_CIPHERS,
        "headers": {
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) "
                           "Gecko/20100101 Firefox/127.0"),
            "Accept": ("text/html,application/xhtml+xml,application/xml;q=0.9,"
                       "image/avif,image/webp,*/*;q=0.8"),
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": ACCEPT_ENCODING,
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Priority": "u=0, i",
            "TE": "trailers",
        },
    },
    "safari": {
        "ciphers": _CHROME_CIPHERS,
        "headers": {
            "Accept": ("text/html,application/xhtml+xml,application/xml;q=0.9,"
                       "*/*;q=0.8"),
            "Accept-Encoding": ACCEPT_ENCODING,
            "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                           "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 "
                           "Safari/605.1.15"),
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1",
        },
    },
}
ESCALATION = ("chrome", "firefox", "safari")

_last_hit: dict[str, float] = {}


def _context(profile: str) -> ssl.SSLContext:
    """TLS shaped as far as the ssl module allows: the browser's cipher ORDER, a TLS 1.2
    floor, and ALPN advertising only http/1.1 — because http.client only speaks 1.1 and
    negotiating h2 we cannot talk would break the fetch outright."""
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    try:
        ctx.set_ciphers(PROFILES[profile]["ciphers"])
    except ssl.SSLError:
        pass                                    # an OpenSSL build without one of the names
    try:
        ctx.set_alpn_protocols(["http/1.1"])
    except NotImplementedError:
        pass
    return ctx


class _Redirect(urllib.request.HTTPRedirectHandler):
    """Browsers send a Referer as they follow a redirect chain and keep the navigation
    metadata coherent; urllib drops both, which is a tell."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is not None:
            new.add_unredirected_header("Referer", req.full_url)
            origin = urlparse(req.full_url).netloc
            same = urlparse(newurl).netloc == origin
            new.add_unredirected_header("Sec-Fetch-Site", "same-origin" if same else "cross-site")
        return new


def _read_body(resp, timeout: int) -> bytes:
    """Chunked read under a wall-clock deadline — same discipline as fetch.py: a server that
    drips bytes never trips a socket timeout and must not be able to wedge a run."""
    deadline = time.monotonic() + max(timeout, 90)
    chunks, got = [], 0
    while got < MAX_BYTES:
        if time.monotonic() > deadline:
            raise FetchError("wall-clock deadline exceeded")
        chunk = resp.read1(min(1 << 16, MAX_BYTES - got))
        if not chunk:
            break
        chunks.append(chunk)
        got += len(chunk)
    return b"".join(chunks)


def fetch_impersonated(url: str, profile: str = "chrome", timeout: int = 40,
                       referer: str | None = None) -> str:
    """One GET dressed as `profile`. Raises FetchError; never touches the pack cache (the
    caller decides whether an escalated body is worth caching)."""
    if profile not in PROFILES:
        raise FetchError(f"unknown browser profile: {profile}")
    if not url.isascii():
        from urllib.parse import quote, urlsplit, urlunsplit
        sp = urlsplit(url)
        url = urlunsplit(sp._replace(path=quote(sp.path), query=quote(sp.query, safe="=&")))

    host = urlparse(url).netloc
    wait = _last_hit.get(host, 0) + HOST_DELAY_S - time.monotonic()
    if wait > 0:
        time.sleep(wait)

    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=_context(profile)),
        urllib.request.HTTPCookieProcessor(jar),
        _Redirect(),
    )
    headers = dict(PROFILES[profile]["headers"])
    if referer:
        headers["Referer"] = referer
        headers["Sec-Fetch-Site"] = (
            "same-origin" if urlparse(referer).netloc == host else "cross-site")

    last = None
    for attempt in range(3):
        _last_hit[host] = time.monotonic()
        req = urllib.request.Request(url, headers=headers)
        try:
            with opener.open(req, timeout=timeout) as resp:
                raw = _read_body(resp, timeout)
                enc = (resp.headers.get("Content-Encoding") or "identity").lower().strip()
                dec = _DECODERS.get(enc)
                if dec is None:
                    raise FetchError(f"cannot decode Content-Encoding {enc!r}")
                try:
                    raw = dec(raw)
                except Exception as e:
                    raise FetchError(f"{enc} decode failed: {e}") from e
                return _decode(raw, resp.headers.get_content_charset())
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):            # permanent: escalating cannot help
                raise FetchError(f"HTTP {e.code} for {url}") from e
            last = e
        except FetchError:
            raise
        except (urllib.error.URLError, TimeoutError, OSError, ssl.SSLError) as e:
            last = e
        # jittered backoff: a fixed cadence is itself a bot signal
        time.sleep(1.5 * (attempt + 1) + random.random())
    raise FetchError(f"impersonated fetch failed ({profile}): {url} ({last})")


def fetch_escalating(url: str, cache_dir: Path, force: bool = False,
                     timeout: int = 40) -> tuple[str, str]:
    """The corpus fetcher first — it is cached, polite and honest about who it is — then
    browser profiles in turn. Returns (html, how) where `how` names what worked, so a
    record can tell a consumer how its content was obtained."""
    try:
        html, cached = fetch(url, cache_dir, force=force, timeout=timeout)
        return html, "cache" if cached else "stdlib"
    except FetchError:
        pass
    except Exception:
        pass
    errors = []
    for profile in ESCALATION:
        try:
            return fetch_impersonated(url, profile=profile, timeout=timeout), profile
        except FetchError as e:
            errors.append(f"{profile}: {e}")
    raise FetchError(f"every fetch strategy failed for {url} — " + " | ".join(errors))


# ---------------------------------------------------------------- admission (live)

def usable_page_live(url: str, cache_dir: Path, force: bool = False):
    """fetch -> normalize -> clean-data gates, escalating on a fetch failure OR a gate
    failure. The gate case is the one that matters: a JS-shell page returns HTTP 200 and
    then dies at the gates, and that is exactly what a browser-shaped request can fix.
    Mirrors grow._usable_page's contract. Returns (slug, title, parts, how) or None."""
    for strategy in ("corpus", *ESCALATION):
        try:
            if strategy == "corpus":
                html, from_cache = fetch(url, cache_dir, force=force)
                how = "cache" if from_cache else "stdlib"
            else:
                html, how = fetch_impersonated(url, profile=strategy), strategy
        except FetchError:
            continue
        except Exception:
            continue
        try:
            title, body = normalize(html)
        except Exception:
            continue
        if verify.check_markdown(body):
            continue                            # failed a gate — escalate, never ship it
        return slug_for(url), (title or url), split_markdown(body), how
    return None


# ---------------------------------------------------------------- corpus lookup

def corpus_index(root: Path) -> dict:
    """Domain names, tags and page slugs straight from atlas.json — enough to answer "do we
    already have this?" without needing a built API tree on disk."""
    atlas = root / "atlas.json"
    if not atlas.exists():
        return {"domains": {}, "slugs": {}, "tags": {}}
    data = json.loads(atlas.read_text(encoding="utf-8"))
    domains, slugs, tags = {}, {}, {}
    for d in data.get("domains", []):
        name = d["name"]
        domains[name] = d
        for t in d.get("tags", []):
            tags.setdefault(t.lower().strip(), []).append(name)
        for f in d.get("files", []):
            slugs.setdefault(f[:-3] if f.endswith(".md") else f, []).append(name)
    return {"domains": domains, "slugs": slugs, "tags": tags}


def _query_slug(query: str) -> str:
    out = [c if c.isalnum() else "-" for c in query.lower()]
    s = "".join(out)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")


def _segments(slug: str) -> set[str]:
    return set(slug.split("-"))


def lookup_corpus(query: str, idx: dict, limit: int = 8) -> list[dict]:
    """Corpus hits for a query, best first: exact domain, exact page slug, tag, then a
    SEGMENT match on domain names and page slugs. Cheap on purpose — this runs before
    anything touches the network, and a false miss means fetching what we already have.

    Segments, not substrings: bare substring matching put "1911-boston-rustlers-season" on
    a query for "rust", while a query for "ownership" missed rust's
    ch04-01-what-is-ownership entirely — wrong in both directions at once."""
    q = _query_slug(query)
    words = [w for w in q.split("-") if len(w) > 2]
    hits: list[dict] = []
    seen: set[str] = set()

    def add(domain: str, why: str, page: str | None = None):
        key = f"{domain}/{page or ''}"
        if key in seen or domain not in idx["domains"]:
            return
        seen.add(key)
        hit = {"domain": domain, "matched": why,
               "index_md": f"https://raw.githubusercontent.com/gary23w/nl-rag/main/"
                           f"packs/{domain}/INDEX.md"}
        if page:
            hit["page"] = page
            hit["raw"] = (f"https://raw.githubusercontent.com/gary23w/nl-rag/main/"
                          f"packs/{domain}/{page}.md")
        hits.append(hit)

    if q in idx["domains"]:
        add(q, "domain name")
    for d in idx["slugs"].get(q, []):
        add(d, "page slug", q)
    for d in idx["tags"].get(query.lower().strip(), []):
        add(d, "tag")
    if not words:
        return hits[:limit]
    want = set(words)
    for name in idx["domains"]:                 # every query word is a name segment
        if len(hits) >= limit:
            return hits[:limit]
        if want <= _segments(name):
            add(name, "domain name segments")
    # ...or a page-slug segment. Fewest segments first: the query is a larger share of a
    # tight slug, so "ch04-01-what-is-ownership" beats a page that merely mentions the word.
    slug_hits = [(slug, owners) for slug, owners in idx["slugs"].items()
                 if want <= _segments(slug)]
    for slug, owners in sorted(slug_hits, key=lambda s: (len(_segments(s[0])), s[0])):
        if len(hits) >= limit:
            break
        for d in owners:
            add(d, "page slug segments", slug)
    return hits[:limit]


# ---------------------------------------------------------------- the resolver

def _record(url: str, slug: str, title: str, parts: list[str], how: str) -> dict:
    """A live document in the SAME shape the API uses for a corpus document — with one
    deliberate difference: `body` is inlined. A corpus record can point at packs/ because
    the markdown is already hosted; a live result has no home yet, so it must carry its
    content or the consumer gets a pointer to nothing."""
    from .api import OUTLINE_CAP, parse_body, plain

    body = "\n\n".join(parts)
    outline, langs, lead, blocks = parse_body(body)
    rec = {
        "kind": "live_document",
        "origin": "live",
        "fetched_via": how,
        "id": f"live/{slug}",
        "title": title,
        "synopsis": plain(lead)[:280],
        "outline": outline[:OUTLINE_CAP],
        "source": url,
        "license": "upstream — see 'source'; attribute it in anything you generate",
        "fetched": date.today().isoformat(),
        "lines": body.count("\n") + 1,
        "bytes": len(body.encode("utf-8")),
        "gates": "passed — same clean-data gates as every committed pack",
        "body": body,
    }
    if blocks:
        rec["code"] = {"blocks": blocks, "languages": langs}
    if len(outline) > OUTLINE_CAP:
        rec["outline_truncated"] = True
    if len(parts) > 1:
        rec["parts"] = len(parts)
    return rec


def resolve(query: str, root: Path, cache_dir: Path | None = None, want: int = 3,
            max_candidates: int = 8, force: bool = False, progress=lambda *_: None) -> dict:
    """Answer a query. Corpus first — a live fetch is a fallback, not the default path.

    Returns a self-describing envelope: what was asked, whether the corpus covered it, and
    either corpus pointers or normalized live documents. `resolved_by` says which."""
    cache_dir = cache_dir or (root / ".cache")
    idx = corpus_index(root)
    covered = lookup_corpus(query, idx)
    envelope = {
        "nl_rag": "v1",
        "kind": "resolution",
        "query": query,
        "generated": date.today().isoformat(),
        "corpus_hits": covered,
    }
    if covered:
        envelope["resolved_by"] = "corpus"
        envelope["note"] = ("the corpus already covers this — fetch index_md or raw above. "
                            "no network request was made for content.")
        return envelope

    envelope["resolved_by"] = "live"
    envelope["note"] = ("the corpus does not cover this query. these documents were fetched "
                        "live, normalized and gated exactly like committed packs, but they "
                        "are NOT yet part of the corpus — 'body' is inlined because nothing "
                        "hosts them yet.")
    if query.startswith(("http://", "https://")):
        candidates = [(query.rsplit("/", 1)[-1] or query, query)]
    else:
        from .discover import search_titles, title_to_url
        try:
            titles = search_titles(query, limit=max_candidates)
        except Exception as e:
            envelope["error"] = f"discovery failed: {e}"
            envelope["results"] = []
            return envelope
        candidates = [(t, title_to_url(t)) for t in titles]

    envelope["candidates_considered"] = [u for _, u in candidates]
    results, failures = [], []
    for title, url in candidates:
        if len(results) >= want:
            break
        progress(f"  live: {url}")
        page = usable_page_live(url, cache_dir, force=force)
        if page is None:
            failures.append(url)
            continue
        slug, real_title, parts, how = page
        results.append(_record(url, slug, real_title or title, parts, how))
    envelope["results"] = results
    if failures:
        # never silently drop: a consumer must be able to tell "nothing exists" from
        # "we could not retrieve it", because those call for different next moves
        envelope["unretrievable"] = failures
    if not results:
        envelope["note"] += (" NOTHING was retrievable — every candidate failed to fetch or "
                             "failed the clean-data gates. no content is being invented.")
    return envelope


def admit(envelope: dict, root: Path, tags: list[str] | None = None) -> dict:
    """Fold a live resolution into the corpus using the SAME writer the autonomous grower
    uses, so an on-demand admission is indistinguishable from a scheduled one. Only pages
    that already passed the gates reach here."""
    from . import grow

    results = envelope.get("results") or []
    if not results:
        return {"admitted": None, "why": "nothing retrievable to admit"}
    domain = _query_slug(envelope["query"])[:80] or results[0]["id"].split("/", 1)[1]
    if (root / "packs" / domain).exists():
        return {"admitted": None, "why": f"pack {domain} already exists"}
    if len(results) < 3:
        # the grower's floor: a pack under 3 usable pages is a thin pack, and the corpus
        # does not carry thin packs just because someone asked
        return {"admitted": None, "why": f"only {len(results)} usable page(s); floor is 3"}

    pagedata, srcmap, srcs = [], {}, []
    for r in results:
        slug = r["id"].split("/", 1)[1]
        pagedata.append((slug, r["title"], split_markdown(r["body"])))
        srcmap[slug] = r["source"]
        srcs.append(r["source"])
    dom = {"name": domain, "tags": (tags or [envelope["query"].lower()])[:6],
           "license": grow.LICENSE, "pages": srcs,
           "_pagedata": pagedata, "_srcmap": srcmap}
    grow.write_domain(dom)
    grow.rebuild_atlas()
    return {"admitted": domain, "pages": len(pagedata),
            "why": "written with the grower's own writer; atlas.json regenerated"}
