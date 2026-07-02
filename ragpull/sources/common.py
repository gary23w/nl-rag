"""Shared constants/helpers for the source registry modules."""

WIKI = "https://en.wikipedia.org/wiki/"
WIKIBOOKS = "https://en.wikibooks.org/wiki/"

# license identifiers used in frontmatter; full attribution lives in SOURCES.md
PSF = "PSF-2.0"
MIT_APACHE = "MIT OR Apache-2.0"
CC_BY_SA = "CC-BY-SA-4.0"
CC_BY_SA_25 = "CC-BY-SA-2.5"  # MDN prose
GFDL = "GFDL-1.3"  # GNU manuals
GPL2 = "GPL-2.0"  # git docs, linux man-pages (varies per page)
BSD = "BSD-3-Clause"
PD = "Public-Domain"
OWASP = "CC-BY-SA-4.0"  # OWASP cheat sheet series
APACHE = "Apache-2.0"
PG = "PostgreSQL"
MIT = "MIT"
GFDL12 = "GFDL-1.2"  # Rosetta Code
CC_BY = "CC-BY-3.0"


def mdn(path):
    return "https://developer.mozilla.org/en-US/docs/" + path


def man7(page):
    sec = page.rsplit(".", 1)[1]
    return f"https://man7.org/linux/man-pages/man{sec}/{page}.html"


def wiki(*titles):
    return [WIKI + t for t in titles]


def wikibooks(*titles):
    return [WIKIBOOKS + t for t in titles]
