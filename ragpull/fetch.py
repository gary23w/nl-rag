"""Polite cached fetcher — stdlib only.

Every successful body is cached on disk (keyed by URL) so re-runs and normalizer
iterations never re-hit the origin. One global per-host rate limit; identity or
gzip bodies handled; charset from the Content-Type header with utf-8 fallback.
"""

import gzip
import hashlib
import io
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

_META_CHARSET = re.compile(rb"""charset\s*=\s*["']?([A-Za-z0-9_.:-]+)""", re.I)


def _decode(raw: bytes, header_charset: str | None) -> str:
    """Header charset, then <meta charset> sniff, then strict utf-8, then latin-1.
    Blind utf-8/replace mangles latin-1 doc sites (man7) into U+FFFD."""
    for enc in (header_charset,):
        if enc:
            try:
                return raw.decode(enc)
            except (LookupError, UnicodeDecodeError):
                pass
    m = _META_CHARSET.search(raw[:4096])
    if m:
        try:
            return raw.decode(m.group(1).decode("ascii", "replace"))
        except (LookupError, UnicodeDecodeError):
            pass
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("latin-1")

UA = "nl-rag/0.1 (+https://github.com/gary23w/nl-rag; doc pack builder)"
MAX_BYTES = 8 << 20
HOST_DELAY_S = 0.8

_last_hit: dict[str, float] = {}


class FetchError(Exception):
    pass


def _cache_path(cache_dir: Path, url: str) -> Path:
    h = hashlib.sha1(url.encode()).hexdigest()
    return cache_dir / f"{h}.html"


def fetch(url: str, cache_dir: Path, force: bool = False, timeout: int = 40) -> tuple[str, bool]:
    """Return (decoded_html, from_cache). Raises FetchError on permanent failure."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    cp = _cache_path(cache_dir, url)
    if cp.exists() and not force:
        return cp.read_text(encoding="utf-8", errors="replace"), True

    # percent-encode any literal non-ASCII in the URL (a Wikipedia title like "Nosé–Hoover"
    # would otherwise blow up http.client's latin-1 request-line encoding)
    if not url.isascii():
        from urllib.parse import quote, urlsplit, urlunsplit

        sp = urlsplit(url)
        url = urlunsplit(sp._replace(path=quote(sp.path), query=quote(sp.query, safe="=&")))

    host = urlparse(url).netloc
    wait = _last_hit.get(host, 0) + HOST_DELAY_S - time.monotonic()
    if wait > 0:
        time.sleep(wait)

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en",
        },
    )
    last_err = None
    for attempt in range(3):
        _last_hit[host] = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                # chunked read under a WALL-CLOCK deadline: socket timeouts never fire on a
                # server that drips bytes, and one dripping host must not wedge the whole pull
                deadline = time.monotonic() + max(timeout, 90)
                chunks: list[bytes] = []
                got = 0
                while got < MAX_BYTES:
                    if time.monotonic() > deadline:
                        raise FetchError(f"wall-clock deadline exceeded: {url}")
                    # read1 = at most one socket recv: a dripping server can't trap us inside
                    # a full read(n) (which loops recv until n bytes and defeats the deadline)
                    chunk = resp.read1(min(1 << 16, MAX_BYTES - got))
                    if not chunk:
                        break
                    chunks.append(chunk)
                    got += len(chunk)
                raw = b"".join(chunks)
                if resp.headers.get("Content-Encoding", "").lower() == "gzip":
                    raw = gzip.GzipFile(fileobj=io.BytesIO(raw)).read(MAX_BYTES)
                text = _decode(raw, resp.headers.get_content_charset())
                cp.write_text(text, encoding="utf-8", errors="replace")
                return text, False
        except urllib.error.HTTPError as e:
            if e.code in (403, 404, 410):
                raise FetchError(f"HTTP {e.code} for {url}") from e
            last_err = e
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = e
        time.sleep(2.0 * (attempt + 1))
    raise FetchError(f"failed after retries: {url} ({last_err})")
