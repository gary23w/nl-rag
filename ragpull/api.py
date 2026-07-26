"""The static REST API generator — nl-rag as a machine-readable manual.

No frontend, no server, no query strings: GitHub Pages serves plain files, so every
lookup is a *path*. The generated tree is the whole API surface —

    /api/v1/index.json              root manifest: endpoint catalog + protocol
    /api/v1/README.txt              NL-RAG(7): how an AI traverses this corpus
    /api/v1/corpus.json             record schemas (corpus/domain/document/section/fact)
    /api/v1/openapi.json            machine contract
    /api/v1/stats.json              counts
    /api/v1/domains/index.json      catalog routing table
    /api/v1/domains/<bucket>.json   domain catalog page
    /api/v1/domain/<name>.json      DOMAIN RECORD (man-shaped; every document's outline)
    /api/v1/search/index.json       search protocol + bucket rule
    /api/v1/search/q/<bucket>.json  full-text term  -> ranked domains  + related terms
    /api/v1/search/t/<bucket>.json  title/name/tag  -> documents

Document *bodies* are never copied: a record carries the man-page scaffolding (NAME,
SYNOPSIS, outline, SEE ALSO, SOURCE, a couple of provenance-tagged fact sentences) plus
a literal raw URL for the markdown that already lives in packs/. One corpus, one copy.

Search size, honestly: a doc-level global index over 73k documents is ~400 MB of JSON,
so the term axis indexes each domain's TOP_TERMS_PER_DOMAIN characteristic terms and
resolves to *domains* (with the best-matching document named on each hit). Landing on a
domain record then gives literal hrefs for everything in it. Two GETs, ~100 KB each.
"""

import json
import math
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from .emit import RAW_BASE, auto_domain_names, read_frontmatter

API_VERSION = "v1"
DEFAULT_BASE = "https://gary23w.github.io/nl-rag"

# --- index shape knobs (every one of these is a size/recall trade; see module docstring)
TOP_TERMS_PER_DOMAIN = 250   # characteristic terms indexed per domain
HITS_PER_TERM = 10           # domains returned per term
RELATED_PER_TERM = 6         # "similar searches" offered on a term
DOCS_PER_TITLE_TOKEN = 25    # documents returned per title/name/tag token
NAME_MATCH_BOOST = 1.6       # a term that is also in the domain's name/tags is about that
                             # domain — the grower copies neighbour pages between packs, so
                             # without this every near-duplicate pack ties on raw tf
OUTLINE_CAP = 20             # headings kept per document
FACTS_PER_DOC = 2            # provenance-tagged sentences quoted per document
SEE_ALSO_PER_DOMAIN = 8      # related domains on a domain record
DOMAIN_TOP_TERMS = 24        # per-domain fingerprint used for relatedness
FINGERPRINT_DF_CAP = 200     # a fingerprint term shared by more domains than this is
                             # too generic to imply relatedness — skipped when linking

_TOKEN_RE = re.compile(r"[a-z][a-z0-9_+#.\-]{1,30}")
_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})\s*([a-zA-Z0-9_+#-]*)")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_FACT_RE = re.compile(r"^\[src:([^/\]]+)/([^\]]+)\]\s+(.*)$")
_PART_RE = re.compile(r"^(\d+)\s*/\s*(\d+)$")
# names Windows cannot create as files, whatever the extension
_RESERVED = frozenset(("con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)),
                       *(f"lpt{i}" for i in range(1, 10))))

STOP = frozenset("""
a about above after again against all also am an and any are aren as at be because been
before being below between both but by can cannot could couldn did didn do does doesn doing
don down during each few for from further had hadn has hasn have haven having he her here
hers herself him himself his how i if in into is isn it its itself just let me more most
must mustn my myself no nor not now of off on once only or other ought our ours ourselves
out over own same shan she should shouldn so some such than that the their theirs them
themselves then there these they this those through to too under until up very was wasn we
were weren what when where which while who whom why will with won would wouldn you your
yours yourself yourselves via etc ie eg vs per may might shall upon within without along
among across whether either neither however therefore thus hence although though since
while whereas one two three four five six seven eight nine ten first second third new
using used use uses like many much often several various given whose above below following
note see also example examples section chapter page pages figure table tables list lists
value values name names type types set sets get gets make makes made take takes taken
based called known called said says show shows shown want need needs way ways time times
case cases part parts number numbers form forms line lines point points end ends
""".split())


# ---------------------------------------------------------------- tokenizing & buckets

def tokenize(text: str) -> list[str]:
    """Lowercase word tokens, code identifiers included (`memcpy`, `c++`, `std.mem`).
    Trailing punctuation is shaved so `ownership.` and `ownership` are one term."""
    out = []
    for raw in _TOKEN_RE.findall(text.lower()):
        t = raw.strip(".-_+#")
        if len(t) < 3 or t in STOP:
            continue
        out.append(t)
    return out


def bucket_of(term: str) -> str:
    """THE routing rule an AI must reproduce to search: first two characters of the
    lowercased term, anything outside [a-z0-9] folded to '_', short terms padded.
      ownership -> ow      c++ -> c_      zig -> zi      x86 -> x8
    Every posting for a term lands in exactly one bucket, so one GET answers one term."""
    s = (term.lower() + "__")[:2]
    return "".join(c if c.isalnum() else "_" for c in s)


def safe_name(domain: str) -> str:
    """Filesystem-safe stem for a domain (Windows reserves con/aux/nul/...)."""
    return f"{domain}_" if domain.lower() in _RESERVED else domain


# ---------------------------------------------------------------- markdown structure

def parse_body(body: str) -> tuple[list[dict], list[str], str, int]:
    """Outline (headings + line numbers), fenced-code languages, first prose line,
    and a code-block count — the man-page scaffolding of one document."""
    outline, langs, blocks = [], [], 0
    lead = ""
    in_fence = False
    fence_tok = ""
    for i, line in enumerate(body.splitlines(), 1):
        m = _FENCE_RE.match(line)
        if m and (not in_fence or line.strip().startswith(fence_tok)):
            if in_fence:
                in_fence = False
            else:
                in_fence, fence_tok, blocks = True, m.group(1), blocks + 1
                if m.group(2):
                    langs.append(m.group(2).lower())
            continue
        if in_fence:
            continue
        h = _HEADING_RE.match(line)
        if h:
            outline.append({"level": len(h.group(1)), "heading": h.group(2).strip(), "line": i})
        elif not lead:
            s = line.strip()
            if len(s) > 40 and not s.startswith(("|", ">", "-", "*", "<", "!", "[")):
                lead = s
    seen, uniq = set(), []
    for l in langs:
        if l not in seen:
            seen.add(l)
            uniq.append(l)
    return outline, uniq[:6], lead, blocks


def load_facts(pack_dir: Path) -> dict[str, list[str]]:
    """pack.facts is already one provenance-tagged declarative sentence per line —
    the corpus's own abstract layer. Group it by document slug."""
    p = pack_dir / "pack.facts"
    if not p.exists():
        return {}
    by_doc: dict[str, list[str]] = defaultdict(list)
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        m = _FACT_RE.match(line)
        if m and len(by_doc[m.group(2)]) < FACTS_PER_DOC:
            by_doc[m.group(2)].append(m.group(3).strip())
    return dict(by_doc)


# ---------------------------------------------------------------- phase 1: scan packs

def scan_domain(domain: str, pack_dir: Path, meta: dict, base: str) -> dict | None:
    """One domain -> its document records + the term counts that feed the search axes."""
    facts = load_facts(pack_dir)
    tf: Counter[str] = Counter()
    best_doc: dict[str, tuple[int, str]] = {}   # term -> (tf in doc, doc slug)
    groups: dict[str, dict] = {}                # logical document (parts folded together)
    order: list[str] = []
    total_bytes = 0

    for md in sorted(pack_dir.glob("*.md")):
        if md.name == "INDEX.md":
            continue
        fm = read_frontmatter(md)
        body = fm.pop("_body", "")
        slug = md.stem
        total_bytes += md.stat().st_size
        outline, langs, lead, blocks = parse_body(body)

        counts = Counter(tokenize(fm.get("title", "") + "\n" + body))
        tf.update(counts)
        for term, n in counts.items():
            if term not in best_doc or n > best_doc[term][0]:
                best_doc[term] = (n, slug)

        title = fm.get("title", slug)
        part = None
        pm = _PART_RE.match(fm.get("part", "") or "")
        if pm:
            part = (int(pm.group(1)), int(pm.group(2)))
            title = re.sub(r"\s*\(part \d+/\d+\)\s*$", "", title)
        key = title if part else slug

        page = {
            "part": part[0] if part else 1,
            "slug": slug,
            "raw": f"{RAW_BASE}/packs/{domain}/{md.name}",
            "lines": body.count("\n") + 1,
            "bytes": md.stat().st_size,
        }
        g = groups.get(key)
        if g is None:
            g = groups[key] = {
                "id": f"{domain}/{slug}",
                "title": title,
                "source": fm.get("source", ""),
                "license": fm.get("license", meta.get("license", "")),
                "fetched": fm.get("fetched", ""),
                "synopsis": plain((facts.get(slug) or [lead or ""])[0])[:280],
                "code": {"blocks": blocks, "languages": langs} if blocks else None,
                "outline": outline[:OUTLINE_CAP],
                "outline_truncated": len(outline) > OUTLINE_CAP,
                "facts": facts.get(slug, []),
                "pages": [],
            }
            order.append(key)
        else:
            g["outline"] = (g["outline"] + outline)[:OUTLINE_CAP]
            g["outline_truncated"] = g["outline_truncated"] or len(outline) > OUTLINE_CAP
            for f in facts.get(slug, []):
                if len(g["facts"]) < FACTS_PER_DOC and f not in g["facts"]:
                    g["facts"].append(f)
            g["code"] = g["code"] or ({"blocks": blocks, "languages": langs} if blocks else None)
        g["pages"].append(page)

    if not groups:
        return None

    documents = []
    for key in order:
        g = groups[key]
        g["pages"].sort(key=lambda p: p["part"])
        if len(g["pages"]) == 1:
            p = g["pages"][0]
            g["raw"] = p["raw"]
            g["lines"], g["bytes"] = p["lines"], p["bytes"]
            del g["pages"]
        else:
            # a split upstream page is ONE document with addressable parts: search hits
            # name the part a term is densest in, so every part slug must resolve here
            g["parts"] = len(g["pages"])
            g["part_slugs"] = [p["slug"] for p in g["pages"]]
            g["raw"] = [p["raw"] for p in g["pages"]]
            g["lines"] = sum(p["lines"] for p in g["pages"])
            g["bytes"] = sum(p["bytes"] for p in g["pages"])
            del g["pages"]
        if not g["code"]:
            del g["code"]
        if not g["facts"]:
            del g["facts"]
        if not g["outline_truncated"]:
            del g["outline_truncated"]
        documents.append(g)

    top = [t for t, _ in tf.most_common(TOP_TERMS_PER_DOMAIN) if tf[t] >= 2] \
        or [t for t, _ in tf.most_common(TOP_TERMS_PER_DOMAIN)]
    return {
        "kind": "domain",
        "name": domain,
        "title": f"{domain} — nl-rag domain",
        "tags": meta.get("tags", []),
        "license": meta.get("license", ""),
        "origin": meta.get("origin", "curated"),
        "documents": documents,
        "counts": {"documents": len(documents),
                   "files": sum(1 for _ in pack_dir.glob("*.md")) - 1,
                   "bytes": total_bytes,
                   "facts": sum(len(v) for v in facts.values())},
        "hrefs": {
            "self": f"{base}/api/{API_VERSION}/domain/{safe_name(domain)}.json",
            "index_md": f"{RAW_BASE}/packs/{domain}/INDEX.md",
            **({"facts": f"{RAW_BASE}/packs/{domain}/pack.facts"} if facts else {}),
        },
        "_top": [(t, tf[t], best_doc[t][1]) for t in top],
    }


_DANGLING = re.compile(
    r"^(as (mentioned|well as|noted|described|above)|however|therefore|this|that|these|"
    r"those|it |its |they |he |she |let[' ]|here |there |such |instead|then |also |but |"
    r"and |for example|in addition|in this|in the (above|previous|next|following))", re.I)
_EMPHASIS = re.compile(r"(\*\*|\*|__)(?=\S)(.+?)(?<=\S)\1")
# chrome that survived the fetch gate and reached pack.facts — never a domain's one-liner
_CHROME = re.compile(
    r"(opens a new window|click here|javascript (is )?(disabled|must be)|enable javascript|"
    r"cookie|sign in|log in to|edit this page|report a (bug|problem)|table of contents|"
    r"skip to (main|content)|browser (does not|doesn't) support|subscribe|newsletter)", re.I)


def plain(s: str) -> str:
    """Man pages don't do bold. Backticks stay — code spans carry meaning."""
    return _EMPHASIS.sub(r"\2", s).strip()


def domain_synopsis(domain: str, documents: list[dict]) -> str:
    """The domain's one-liner, chosen not invented. A pack carries its topic page plus
    neighbours, so prefer the document that IS the domain; failing that, prefer a sentence
    that names the domain and doesn't open mid-argument ("As mentioned above, ...")."""
    words = {w for w in tokenize(domain.replace("-", " ")) if len(w) > 2}
    wanted = domain.replace("-", "")
    best, best_score = "", -99
    for i, doc in enumerate(documents):
        syn = (doc.get("synopsis") or "").strip()
        if not syn:
            continue
        slug = doc["id"].split("/", 1)[1]
        score = -i * 0.01
        if slug == domain or slug.replace("-", "") == wanted:
            score += 10
        low = syn.lower()
        if any(w in low for w in words):
            score += 2
        if _DANGLING.match(syn):
            score -= 3
        if _CHROME.search(syn):
            score -= 8
        if score > best_score:
            best, best_score = syn, score
    return best[:280]


# ---------------------------------------------------------------- writers

def longpath(p: Path) -> str:
    r"""Windows caps a path at 260 characters, and the corpus has domain names 79 characters
    long ("alliance-of-liberals-and-democrats-for-europe-in-the-..."). Under any moderately
    deep output directory that overflows, and the write fails late in the build. The \\?\
    prefix lifts the limit to 32k. A no-op everywhere else."""
    s = str(p if p.is_absolute() else p.resolve())
    if sys.platform == "win32" and not s.startswith("\\\\?\\"):
        s = "\\\\?\\" + s.replace("/", "\\")
    return s


def read_text(path: Path) -> str:
    with open(longpath(path), "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def write_text(path: Path, text: str) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(longpath(path), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return len(text)


def write_json(path: Path, obj) -> int:
    data = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=False)
    return write_text(path, data + "\n")


def _stamp(base: str, kind: str) -> dict:
    return {"nl_rag": API_VERSION, "kind": kind, "generated": date.today().isoformat(),
            "root": f"{base}/api/{API_VERSION}/index.json"}


# ---------------------------------------------------------------- the build

def build(root: Path, out: Path, base: str, limit: int | None = None,
          only: list[str] | None = None, progress=print) -> dict:
    packs = root / "packs"
    atlas_meta: dict[str, dict] = {}
    atlas_path = root / "atlas.json"
    if atlas_path.exists():
        for d in json.loads(read_text(atlas_path)).get("domains", []):
            atlas_meta[d["name"]] = d
    auto = auto_domain_names(root)

    api = out / "api" / API_VERSION
    work = out / ".work"
    for stale in (api, work):
        if stale.exists():
            shutil.rmtree(longpath(stale), ignore_errors=True)
    write_text(out / ".nojekyll", "")

    names = sorted(p.name for p in packs.iterdir() if p.is_dir())
    if only:
        missing = [n for n in only if n not in set(names)]
        if missing:
            raise SystemExit(f"no such pack(s): {', '.join(missing)}")
        names = [n for n in names if n in set(only)]
    if limit:
        names = names[:limit]

    # phase 1 — scan every pack once: domain records to scratch, postings to bucket files
    q_files: dict[str, list[str]] = {}
    t_files: dict[str, list[str]] = {}
    fingerprint: dict[str, list[str]] = {}
    namewords: dict[str, set[str]] = {}
    scanned: list[str] = []
    stats = Counter()

    # Postings are buffered per bucket and flushed in batches rather than held open:
    # there are ~2,000 buckets across both axes, and a default Linux fd limit of 1024
    # would kill the run partway through phase 1.
    started: set[tuple[str, str]] = set()

    def flush(store: dict[str, list[str]], kind: str):
        for b, lines in store.items():
            if not lines:
                continue
            p = work / kind / f"{b}.tsv"
            p.parent.mkdir(parents=True, exist_ok=True)
            mode = "a" if (kind, b) in started else "w"
            started.add((kind, b))
            with open(longpath(p), mode, encoding="utf-8", newline="\n") as fh:
                fh.write("".join(lines))
            lines.clear()

    for i, domain in enumerate(names, 1):
        meta = dict(atlas_meta.get(domain) or {})
        meta.setdefault("origin", "auto" if domain in auto else "curated")
        rec = scan_domain(domain, packs / domain, meta, base)
        if rec is None:
            stats["empty_domains"] += 1
            continue
        top = rec.pop("_top")
        write_json(work / "dom" / f"{safe_name(domain)}.json", rec)
        scanned.append(domain)
        stats["documents"] += len(rec["documents"])
        stats["files"] += rec["counts"]["files"]
        stats["bytes"] += rec["counts"]["bytes"]

        for term, n, slug in top:
            q_files.setdefault(bucket_of(term), []).append(f"{term}\t{domain}\t{n}\t{slug}\n")
            stats["term_postings"] += 1
        fingerprint[domain] = [t for t, _, _ in top[:DOMAIN_TOP_TERMS]]

        seen_tok = set()
        for doc in rec["documents"]:
            for term in tokenize(doc["title"]):
                if (term, doc["id"]) in seen_tok:
                    continue
                seen_tok.add((term, doc["id"]))
                safe_title = doc["title"][:90].replace("\t", " ")
                t_files.setdefault(bucket_of(term), []).append(
                    f"{term}\t{domain}\t{doc['id'].split('/', 1)[1]}\t{safe_title}\n")
                stats["title_postings"] += 1
        name_tokens = tokenize(domain.replace("-", " ") + " " + " ".join(rec["tags"]))
        for term in name_tokens:
            t_files.setdefault(bucket_of(term), []).append(f"{term}\t{domain}\t\t{domain}\n")
            stats["title_postings"] += 1
        namewords[domain] = set(name_tokens)

        if i % 250 == 0 or i == len(names):
            flush(q_files, "q")
            flush(t_files, "t")
            progress(f"  scan {i}/{len(names)} domains — {stats['documents']} docs, "
                     f"{stats['term_postings']} term postings")

    flush(q_files, "q")
    flush(t_files, "t")

    # the fingerprint inversion drives both "similar searches" and a domain's SEE ALSO
    inv: dict[str, list[str]] = defaultdict(list)
    for domain, terms in fingerprint.items():
        for t in terms:
            inv[t].append(domain)

    def related_terms(term: str, hits: list[str]) -> list[str]:
        pool: Counter[str] = Counter()
        for d in hits[:3]:
            pool.update(fingerprint.get(d, ()))
        pool.pop(term, None)
        return [t for t, _ in pool.most_common(RELATED_PER_TERM)]

    n_domains = max(len(scanned), 1)

    # phase 2 — term axis: df is computable inside a bucket (all of a term's postings
    # land there by construction), so scoring never needs a global pass
    progress("  phase 2: term shards")
    q_buckets = []
    for tsv in sorted((work / "q").glob("*.tsv")) if (work / "q").exists() else []:
        rows: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
        for line in read_text(tsv).splitlines():
            term, domain, n, slug = line.split("\t", 3)
            rows[term].append((domain, int(n), slug))
        terms = {}
        for term in sorted(rows):
            posts = rows[term]
            df = len(posts)
            idf = math.log(1 + n_domains / df)

            def score(post, _idf=idf, _term=term):
                d, n, _ = post
                boost = NAME_MATCH_BOOST if _term in namewords.get(d, ()) else 1.0
                return n * _idf * boost

            ranked = sorted(posts, key=lambda p: (-score(p), p[0]))[:HITS_PER_TERM]
            hits = [{"d": d, "s": round(score((d, n, slug)), 2), "p": slug}
                    for d, n, slug in ranked]
            # The best answer is handed over as literal URLs — nothing to assemble. The tail
            # stays template-only on purpose: hrefs on all ten would put ~115 MB into the
            # term axis and push the biggest shard past 4 MB for a single search fetch.
            if hits:
                top = hits[0]
                top["raw"] = f"{RAW_BASE}/packs/{top['d']}/{top['p']}.md"
                top["domain_href"] = (f"{base}/api/{API_VERSION}/domain/"
                                      f"{safe_name(top['d'])}.json")
            terms[term] = {
                "df": df,
                "hits": hits,
                "related": related_terms(term, [d for d, _, _ in ranked]),
            }
        size = write_json(api / "search" / "q" / f"{tsv.stem}.json", {
            **_stamp(base, "search_shard"), "axis": "term", "bucket": tsv.stem,
            "terms_in_shard": len(terms),
            "how_to_read": (
                "terms are sorted keys; a miss is answered by scanning them for the nearest "
                "match. hit.d=domain, hit.p=page slug, hit.s=tf-idf score. THE TOP HIT "
                "CARRIES LITERAL HREFS ('raw' = the page, 'domain_href' = its domain record); "
                "for the rest, expand d and p with the templates below. when a page was split, p "
                "names the PART the term is densest in — it appears in the domain record's "
                "part_slugs, under the document whose id is part 1. 'related' lists similar "
                "searches — each is another term; its shard is search/q/<first two chars>.json."),
            "templates": {
                "domain": f"{base}/api/{API_VERSION}/domain/{{d}}.json",
                "document_raw": RAW_BASE + "/packs/{d}/{p}.md",
                "term": f"{base}/api/{API_VERSION}/search/q/{{bucket}}.json",
            },
            "terms": terms,
        })
        q_buckets.append({"bucket": tsv.stem, "terms": len(terms), "bytes": size})
        stats["terms"] += len(terms)

    # phase 3 — title axis: titles, domain names and tags, with literal hrefs (small
    # enough to afford them here, unlike the term axis)
    progress("  phase 3: title shards")
    t_buckets = []
    for tsv in sorted((work / "t").glob("*.tsv")) if (work / "t").exists() else []:
        rows: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
        for line in read_text(tsv).splitlines():
            # maxsplit: the title is last, so a tab inside it cannot shift the other fields
            term, domain, slug, title = line.split("\t", 3)
            rows[term].append((domain, slug, title))
        terms = {}
        for term in sorted(rows):
            # round-robin across domains before capping: 25 pages from one near-duplicate
            # pack is a useless answer, 25 pages from 25 domains is a real one
            by_domain: dict[str, list] = defaultdict(list)
            for post in rows[term]:
                by_domain[post[0]].append(post)
            order, lane = [], 0
            while len(order) < len(rows[term]):
                added = False
                for d in sorted(by_domain):
                    if lane < len(by_domain[d]):
                        order.append(by_domain[d][lane])
                        added = True
                if not added:
                    break
                lane += 1
            hits = []
            for domain, slug, title in order[:DOCS_PER_TITLE_TOKEN]:
                h = {"d": domain, "t": title,
                     "domain_href": f"{base}/api/{API_VERSION}/domain/{safe_name(domain)}.json"}
                if slug:
                    h["p"] = slug
                    h["raw"] = f"{RAW_BASE}/packs/{domain}/{slug}.md"
                else:
                    h["is_domain_name"] = True
                hits.append(h)
            terms[term] = {"df": len(rows[term]), "hits": hits}
        size = write_json(api / "search" / "t" / f"{tsv.stem}.json", {
            **_stamp(base, "search_shard"), "axis": "title", "bucket": tsv.stem,
            "terms_in_shard": len(terms),
            "how_to_read": (
                "tokens from document titles, domain names and tags. every hit carries a "
                "literal href: 'raw' is the man page itself, 'domain_href' its domain record. "
                "hits are capped per token — df is the true count."),
            "terms": terms,
        })
        t_buckets.append({"bucket": tsv.stem, "terms": len(terms), "bytes": size})

    # phase 4 — domain records: inject SEE ALSO, then publish
    progress("  phase 4: domain records")
    catalog: dict[str, list[dict]] = defaultdict(list)
    for domain in scanned:
        rec = json.loads(read_text(work / "dom" / f"{safe_name(domain)}.json"))
        near: Counter[str] = Counter()
        for t in fingerprint.get(domain, ()):
            peers = inv.get(t, ())
            if len(peers) > FINGERPRINT_DF_CAP:
                continue
            near.update(peers)
        near.pop(domain, None)
        rec["see_also"] = [
            {"domain": d, "shared_terms": c,
             "href": f"{base}/api/{API_VERSION}/domain/{safe_name(d)}.json"}
            for d, c in near.most_common(SEE_ALSO_PER_DOMAIN)
        ]
        rec["keywords"] = fingerprint.get(domain, [])[:12]
        rec["synopsis"] = domain_synopsis(domain, rec["documents"])
        rec["search"] = {
            "in_this_domain": "grep the document titles and outlines in this record",
            "term_shard_rule": f"{base}/api/{API_VERSION}/search/q/<first two chars of term>.json",
        }
        ordered = {**_stamp(base, "domain"), **rec}
        size = write_json(api / "domain" / f"{safe_name(domain)}.json", ordered)
        stats["domain_bytes"] += size
        catalog[bucket_of(domain)].append({
            "name": domain, "tags": rec["tags"], "license": rec["license"],
            "origin": rec["origin"], "documents": rec["counts"]["documents"],
            "href": rec["hrefs"]["self"],
        })

    # phase 5 — catalog + manifests
    progress("  phase 5: manifests")
    cat_buckets = []
    for b in sorted(catalog):
        size = write_json(api / "domains" / f"{b}.json", {
            **_stamp(base, "domain_catalog"), "bucket": b,
            "count": len(catalog[b]), "domains": sorted(catalog[b], key=lambda d: d["name"]),
        })
        cat_buckets.append({"bucket": b, "count": len(catalog[b]), "bytes": size,
                            "href": f"{base}/api/{API_VERSION}/domains/{b}.json"})

    write_json(api / "domains" / "index.json", {
        **_stamp(base, "domain_catalog_index"),
        "count": len(scanned),
        "bucket_rule": "first two characters of the domain name, [^a-z0-9] -> '_'",
        "buckets": cat_buckets,
    })

    write_json(api / "search" / "index.json", {
        **_stamp(base, "search_index"),
        "axes": {
            "term": {
                "what": "full-text: each domain's characteristic terms -> ranked domains",
                "url": f"{base}/api/{API_VERSION}/search/q/{{bucket}}.json",
                "terms": stats["terms"], "shards": len(q_buckets),
            },
            "title": {
                "what": "document titles, domain names and tags -> documents, with hrefs",
                "url": f"{base}/api/{API_VERSION}/search/t/{{bucket}}.json",
                "shards": len(t_buckets),
            },
        },
        "bucket_rule": {
            "rule": "lowercase the term; bucket = first two characters, each character "
                    "outside [a-z0-9] replaced with '_'; terms shorter than two characters "
                    "are padded with '_'",
            "examples": {"ownership": "ow", "zig": "zi", "c++": "c_", "x86": "x8", "b": "b_"},
        },
        "multi_word": "fetch one shard per word and intersect on hit.d — the shards are "
                      "small and the intersection is exact; there is no server to do it for you",
        "coverage": {
            "term_axis": f"each domain's top {TOP_TERMS_PER_DOMAIN} characteristic terms. a "
                         "word that appears only incidentally may not be indexed — that is a "
                         "deliberate size trade, not a claim the corpus lacks it",
            "title_axis": "complete for every document title, domain name and tag",
            "fallback": "packs/<domain>/pack.facts holds every distilled sentence in a domain; "
                        "fetch it when the term axis comes up empty",
        },
        "shards": {"term": q_buckets, "title": t_buckets},
    })

    write_json(api / "corpus.json", corpus_schema(base))
    write_json(api / "openapi.json", openapi(base, stats, len(scanned)))
    stats_obj = {
        **_stamp(base, "stats"),
        "domains": len(scanned), "documents": stats["documents"], "files": stats["files"],
        "corpus_bytes": stats["bytes"], "indexed_terms": stats["terms"],
        "term_postings": stats["term_postings"], "title_postings": stats["title_postings"],
        "term_shards": len(q_buckets), "title_shards": len(t_buckets),
        "api_bytes": stats["domain_bytes"] + sum(b["bytes"] for b in q_buckets)
                     + sum(b["bytes"] for b in t_buckets),
    }
    write_json(api / "stats.json", stats_obj)
    write_json(api / "index.json", root_manifest(base, stats_obj))
    man = manpage(base, stats_obj)
    write_text(api / "README.txt", man)
    write_text(out / "llms.txt", man)
    write_json(out / "index.json", {
        **_stamp(base, "site"),
        "name": "nl-rag", "what": "AI-only corpus API — no frontend, path-addressed",
        "start_here": [f"{base}/api/{API_VERSION}/index.json", f"{base}/api/{API_VERSION}/README.txt"],
    })

    shutil.rmtree(longpath(work), ignore_errors=True)
    return stats_obj


# ---------------------------------------------------------------- self-describing docs

def corpus_schema(base: str) -> dict:
    a = f"{base}/api/{API_VERSION}"
    return {
        **_stamp(base, "corpus_schema"),
        "model": "corpus > domain > document > section | fact",
        "records": {
            "corpus": {"what": "this whole repository", "fields": {
                "domains": "int", "documents": "int", "license": "per-document, upstream"}},
            "domain": {
                "what": "one knowledge domain — the manual's section",
                "url": f"{a}/domain/{{name}}.json",
                "fields": {
                    "name": "stable slug, also the path segment",
                    "title": "display title",
                    "synopsis": "one-line abstract, taken from the first document's facts",
                    "keywords": "the domain's characteristic terms (its fingerprint)",
                    "tags": "curated topic tags",
                    "license": "upstream license of the pack content",
                    "origin": "'curated' (hand-registered) | 'auto' (admitted by the grower)",
                    "documents": "array of document records",
                    "see_also": "related domains, ranked by shared fingerprint terms",
                    "hrefs": "self, the pack INDEX.md, the pack.facts sentence store",
                },
            },
            "document": {
                "what": "one man page. the BODY IS NOT COPIED — 'raw' is its only home",
                "fields": {
                    "id": "'<domain>/<slug>' — the corpus-wide document identifier",
                    "title": "NAME",
                    "synopsis": "SYNOPSIS — one declarative sentence about the document",
                    "code": "{blocks, languages} when the page carries fenced code",
                    "outline": "[{level, heading, line}] — the section table, line-addressed",
                    "outline_truncated": f"true when more than {OUTLINE_CAP} headings exist",
                    "facts": f"up to {FACTS_PER_DOC} provenance-tagged sentences from pack.facts",
                    "raw": "literal URL of the clean markdown (string, or array when split "
                           "into parts); frontmatter at the top of that file repeats "
                           "title/source/domain/license/tags/fetched",
                    "parts": "present when one upstream page was split at heading boundaries",
                    "part_slugs": "the addressable slug of each part, parallel to 'raw' — a "
                                  "term-search hit may name any of them",
                    "source": "SOURCE — the upstream URL (this is the attribution)",
                    "license": "upstream license of this page",
                    "lines": "int", "bytes": "int",
                },
            },
            "section": {"what": "an outline entry; 'line' addresses it inside the raw markdown"},
            "fact": {"what": "one declarative sentence with a [src:domain/page] tag",
                     "bulk": "packs/<domain>/pack.facts, one per line"},
        },
        "conventions": {
            "no_query_strings": "static hosting cannot read '?q='. every lookup is a path.",
            "short_keys": "search hits use d=domain, p=document slug, t=title, s=score — "
                          "expanded with the 'templates' block carried by every shard",
            "bodies": "fetch raw markdown from raw.githubusercontent.com; it is already "
                      "normalized (no HTML, fenced code, GFM tables) and frontmattered",
        },
    }


def root_manifest(base: str, st: dict) -> dict:
    a = f"{base}/api/{API_VERSION}"
    return {
        **_stamp(base, "root"),
        "name": "nl-rag",
        "what": "A machine-readable manual: canonical documentation, normalized to clean "
                "markdown, addressed like man pages. Built for AI consumption only — there "
                "is no frontend and no HTML.",
        "counts": {k: st[k] for k in ("domains", "documents", "files", "indexed_terms")},
        "read_this_first": f"{a}/README.txt",
        "endpoints": [
            {"url": f"{a}/README.txt", "what": "NL-RAG(7) — the traversal protocol, as a man page"},
            {"url": f"{a}/corpus.json", "what": "record schemas: corpus > domain > document"},
            {"url": f"{a}/openapi.json", "what": "machine contract"},
            {"url": f"{a}/stats.json", "what": "counts"},
            {"url": f"{a}/search/index.json", "what": "search protocol + shard routing table"},
            {"url": f"{a}/search/q/{{bucket}}.json", "what": "TERM search -> ranked domains + similar terms"},
            {"url": f"{a}/search/t/{{bucket}}.json", "what": "TITLE/name/tag search -> documents + hrefs"},
            {"url": f"{a}/domains/index.json", "what": "domain catalog routing table"},
            {"url": f"{a}/domains/{{bucket}}.json", "what": "domain catalog page"},
            {"url": f"{a}/domain/{{name}}.json", "what": "domain record: every document's man scaffolding"},
            {"url": RAW_BASE + "/packs/{domain}/{slug}.md", "what": "the document body — clean markdown"},
        ],
        "search_in_one_line": "bucket = first two chars of the lowercased term ('_' for "
                              "non-alphanumerics); GET search/q/<bucket>.json; read terms[<term>].",
        "license": "tooling MIT; every document keeps its upstream license, declared in its "
                   "own frontmatter and in the record's 'license' field. attribution is the "
                   "'source' URL — carry it into anything you generate.",
    }


def openapi(base: str, stats: Counter, n_domains: int) -> dict:
    a = f"/api/{API_VERSION}"
    def op(sid, summary, params=()):
        o = {"operationId": sid, "summary": summary,
             "responses": {"200": {"description": "record",
                                   "content": {"application/json": {}}}}}
        if params:
            o["parameters"] = [{"name": p, "in": "path", "required": True,
                                "schema": {"type": "string"}, "description": d}
                               for p, d in params]
        return {"get": o}
    return {
        "openapi": "3.1.0",
        "info": {"title": "nl-rag corpus API", "version": API_VERSION,
                 "description": "Static, path-addressed corpus API for AI consumers. No "
                                "query strings: hosting is static, so search is a path. "
                                f"{n_domains} domains, {stats['documents']} documents.",
                 "license": {"name": "MIT (tooling); documents keep upstream licenses"}},
        "servers": [{"url": base}],
        "paths": {
            f"{a}/index.json": op("root", "Root manifest and endpoint catalog"),
            f"{a}/README.txt": op("manual", "NL-RAG(7) traversal protocol (text/plain)"),
            f"{a}/corpus.json": op("schema", "Record schemas"),
            f"{a}/stats.json": op("stats", "Corpus counts"),
            f"{a}/search/index.json": op("searchIndex", "Search protocol and shard routing table"),
            f"{a}/search/q/{{bucket}}.json": op(
                "searchTerm", "Full-text term shard: term -> ranked domains + similar terms",
                (("bucket", "first two characters of the lowercased term, non-alphanumerics as '_'"),)),
            f"{a}/search/t/{{bucket}}.json": op(
                "searchTitle", "Title/name/tag shard: token -> documents with hrefs",
                (("bucket", "first two characters of the lowercased token"),)),
            f"{a}/domains/index.json": op("catalogIndex", "Domain catalog routing table"),
            f"{a}/domains/{{bucket}}.json": op("catalogPage", "Domain catalog page",
                                               (("bucket", "first two characters of the domain name"),)),
            f"{a}/domain/{{name}}.json": op("domain", "Domain record with every document's man scaffolding",
                                            (("name", "domain slug"),)),
        },
    }


def manpage(base: str, st: dict) -> str:
    a = f"{base}/api/{API_VERSION}"
    return f"""\
NL-RAG(7)                     nl-rag corpus manual                    NL-RAG(7)

NAME
       nl-rag - a machine-readable manual of canonical technical documentation,
       addressed and consumed like man pages. For AI readers. No frontend.

SYNOPSIS
       GET {a}/index.json
       GET {a}/search/q/<bucket>.json          # term search
       GET {a}/search/t/<bucket>.json          # title / name / tag search
       GET {a}/domain/<name>.json              # domain record
       GET {RAW_BASE}/packs/<domain>/<slug>.md
                                               # the document body

DESCRIPTION
       {st['domains']} domains, {st['documents']} documents, {st['indexed_terms']} indexed terms.
       Every document was pulled from upstream documentation, stripped of HTML,
       nav and boilerplate, rendered to clean markdown with fenced code and GFM
       tables, gated for content quality, and frontmattered with title, source,
       domain, license, tags and fetch date.

       The API is a set of static files. There is no server: query strings cannot
       be read, so every lookup is a PATH you can construct offline. Document
       bodies are never duplicated into the API - a record carries the man-page
       scaffolding and the literal URL of the markdown.

THE BUCKET RULE
       Lowercase the term. Take its first two characters. Replace any character
       outside [a-z0-9] with '_'. Pad terms shorter than two characters with '_'.

           ownership -> ow      zig -> zi      c++ -> c_      x86 -> x8

       Every posting for a term lives in exactly that one shard, so one GET
       answers one term. Keys inside a shard are sorted: on a miss, scan them for
       the nearest match instead of guessing another URL.

SEARCHING
       1. Term search  - GET {a}/search/q/<bucket>.json
          terms[<term>] = {{ df, hits[{{d, p, s}}], related[] }}
              d  domain          p  page slug            s  tf-idf score
              df how many domains carry the term
              related  similar searches: more terms, each with its own shard
          hits[0] also carries literal hrefs - 'raw' is the page itself and
          'domain_href' its domain record, so the best answer needs no assembly.
          For the rest, expand d and p with the 'templates' block in the same
          response.

       2. Title search - GET {a}/search/t/<bucket>.json
          Tokens from document titles, domain names and tags. Every hit carries
          literal hrefs already: 'raw' (the page) and 'domain_href' (its domain).

       3. Multi-word   - fetch one shard per word, intersect on hit.d. The shards
          are small; the intersection is exact. Nothing server-side will do it.

COVERAGE, HONESTLY
       The term axis indexes each domain's top {TOP_TERMS_PER_DOMAIN} characteristic terms, not every
       word of every page: a doc-level index over the whole corpus is ~400 MB of
       JSON and static hosting has to ship it whole. So an incidental word may
       be missing from search/q even though the corpus contains it. The title
       axis IS complete for titles, domain names and tags. When a term search
       comes up empty, fall back to packs/<domain>/pack.facts, which holds every
       distilled sentence for a domain in one fetchable file.

READING
       A domain record lists every document with: title, one-line synopsis, the
       outline (each heading with its line number in the raw markdown), fenced-
       code languages, up to two provenance-tagged fact sentences, the upstream
       source URL, the license, and the raw href. Read the outline to decide
       whether to spend a fetch on the body.

       SEE ALSO on a record ranks related domains by shared fingerprint terms.

       packs/<domain>/pack.facts is the same corpus distilled to one declarative
       sentence per line, each tagged [src:domain/page] - bulk context, no
       markdown to parse.

FILES
       {a}/index.json        root manifest, endpoint catalog
       {a}/corpus.json       record schemas
       {a}/openapi.json      machine contract
       {a}/search/index.json shard routing table, every bucket and its size
       {a}/domains/index.json  domain catalog routing table

CONVENTIONS
       Short keys in search hits (d, p, t, s) keep shards small enough to fetch
       in one hop; every shard carries the templates that expand them.

ATTRIBUTION
       The tooling is MIT. Every document keeps its upstream license, declared in
       its own frontmatter and in the record's 'license' field; most of the
       corpus is CC-BY-SA-4.0. The 'source' URL is the attribution - carry it
       into anything you generate from this corpus.

SEE ALSO
       neuron-db(1) for loading pack.facts as memory, nl-veil(1) for the scout
       that reads these packs.

nl-rag {st['generated']}                                              NL-RAG(7)
"""


def cmd_api(args, root: Path):
    out = Path(args.out) if args.out else root / "build" / "site"
    out.mkdir(parents=True, exist_ok=True)
    print(f"building nl-rag API -> {out}  (base {args.base})")
    only = [s for s in (args.only or "").split(",") if s] or None
    st = build(root, out, args.base.rstrip("/"), limit=args.limit, only=only)
    mb = st["api_bytes"] / 1e6
    print(f"\n{st['domains']} domains · {st['documents']} documents · "
          f"{st['indexed_terms']} terms · {st['term_shards']}+{st['title_shards']} shards")
    print(f"api payload {mb:.1f} MB  (corpus bodies not copied: "
          f"{st['corpus_bytes'] / 1e6:.0f} MB stays in packs/)")
    if mb > 900:
        print("WARNING: over GitHub Pages' 1 GB site limit — lower TOP_TERMS_PER_DOMAIN "
              "or OUTLINE_CAP in ragpull/api.py", file=sys.stderr)
    return 0
