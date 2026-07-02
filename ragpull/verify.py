"""Clean-data gates. A page that fails any gate is rejected at pull time (and
`verify` re-audits the whole tree so regressions in the normalizer can't ship silently)."""

import re

from .emit import read_frontmatter, strip_fences

# a real renderer leak shows CLOSING tags or attributed opening tags; a bare "<style>" can be a
# legitimate CLI placeholder (git --conflict=<style>) and uppercase <A>/<P> are rustdoc generics
_TAG_RESIDUE = re.compile(r"</(?:div|span|p|a|td|tr|table|ul|li|script|style|img|h[1-6])>|<(?:div|span|td|tr|table|ul|li|script|style|img|h[1-6])\s+[a-z-]+=")
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_FORBIDDEN = (
    "enable javascript",
    "javascript is disabled",
    "accept cookies",
    "cookie settings",
    "was this page helpful",
    "browser does not support",
    "please enable js",
)
MIN_BODY = 400


def check_markdown(body: str) -> list[str]:
    """Gate a normalized body. Returns a list of failure reasons (empty = clean)."""
    problems = []
    prose = _INLINE_CODE.sub(" ", strip_fences(body))  # a page ABOUT html tags is not an html leak
    if len(body) < MIN_BODY:
        problems.append(f"too short ({len(body)}B < {MIN_BODY}B)")
        return problems
    # table cells legitimately hold literal tag examples (markdown/html syntax articles);
    # a real renderer leak shows up in paragraphs, so count residue on non-table lines only
    non_table = "\n".join(ln for ln in prose.splitlines() if not ln.lstrip().startswith("|"))
    residues = _TAG_RESIDUE.findall(non_table)
    if len(residues) > 3:
        problems.append(f"html residue ({len(residues)} tag-like fragments outside code fences)")
    low = prose.lower()
    for phrase in _FORBIDDEN:
        if phrase in low:
            problems.append(f"boilerplate phrase: {phrase!r}")
    sentences = len(re.findall(r"[.!?](?:\s|$)", prose))
    if sentences < 3:
        problems.append(f"not prose ({sentences} sentences)")
    letters = sum(c.isalpha() or c.isspace() for c in prose)
    if prose and letters / len(prose) < 0.55:
        problems.append(f"low prose ratio ({letters / len(prose):.2f})")
    return problems


def check_file(path) -> list[str]:
    meta = read_frontmatter(path)
    problems = []
    for key in ("title", "source", "domain", "license"):
        if not meta.get(key):
            problems.append(f"missing frontmatter: {key}")
    if meta.get("part"):
        # a split PART is an arbitrary slice of a page that already passed the full gate at pull
        # time — hold it to structural checks only (a synopsis/options part is legitimately terse)
        body = meta["_body"]
        prose = _INLINE_CODE.sub(" ", strip_fences(body))
        non_table = "\n".join(ln for ln in prose.splitlines() if not ln.lstrip().startswith("|"))
        if len(_TAG_RESIDUE.findall(non_table)) > 3:
            problems.append("html residue")
        low = prose.lower()
        problems.extend(f"boilerplate phrase: {p!r}" for p in _FORBIDDEN if p in low)
        if len(body) < 200:
            problems.append(f"fragment part ({len(body)}B)")
        return problems
    problems.extend(check_markdown(meta["_body"]))
    return problems
