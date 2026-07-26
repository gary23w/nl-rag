#!/usr/bin/env python3
"""Gate a generated API tree by walking it the way an AI consumer would.

    python scripts/check_api.py build/site           # sampled — the CI gate
    python scripts/check_api.py build/site --full    # every shard, term and record

Every check is a claim the API makes about itself: the bucket rule resolves, hrefs point
at files that exist, templates expand to real paths, and a search actually lands on a
document. A publish that fails here would teach a consumer a protocol that doesn't hold.

The default samples so the gate stays cheap on every publish. --full walks all 8k+ domain
records and all ~1,400 shards — slower, and the right thing to run after changing the
generator.
"""

import json
import os
import re
import sys
from pathlib import Path

FULL = "--full" in sys.argv
fails: list[str] = []
notes: list[str] = []


def cap(seq, n):
    """Sampling stride/limit — a no-op under --full."""
    return list(seq) if FULL else list(seq)[:n]


def bad(msg):
    fails.append(msg)


def longpath(p: Path) -> str:
    r"""Match the generator: some domain names are long enough that the record path passes
    Windows' 260-character limit, and \\?\ is the only way to open it."""
    s = str(p if p.is_absolute() else p.resolve())
    if sys.platform == "win32" and not s.startswith("\\\\?\\"):
        s = "\\\\?\\" + s.replace("/", "\\")
    return s


def exists(p: Path) -> bool:
    """Path.exists() silently answers False for a path over 260 characters on Windows —
    and one domain name lands the record at exactly 261. Checking the plain path would
    report a perfectly good record as missing (glob finds it; stat does not)."""
    return os.path.exists(longpath(p))


def load(p: Path):
    try:
        with open(longpath(p), "r", encoding="utf-8") as fh:
            return json.loads(fh.read())
    except FileNotFoundError:
        bad(f"missing file: {p}")
    except Exception as e:                      # a shard that won't parse is unusable
        bad(f"unparseable {p}: {e}")
    return None


def bucket_of(term: str) -> str:
    s = (term.lower() + "__")[:2]
    return "".join(c if c.isalnum() else "_" for c in s)


_records: dict[str, object] = {}


def record(domain_dir: Path, name: str):
    """Domain records are re-visited once per term hit — 72k+ loads under --full over
    files up to 46 KB. Cache them or the exhaustive pass is dominated by re-parsing."""
    if name not in _records:
        if len(_records) > 1500:       # bounded: all 8,343 parsed at once is ~0.5 GB of objects
            _records.clear()
        _records[name] = load(domain_dir / f"{name}.json")
    return _records[name]


def main(site: Path) -> int:
    api = site / "api" / "v1"
    if not api.is_dir():
        print(f"no api/v1 tree under {site}", file=sys.stderr)
        return 2

    if not exists(site / ".nojekyll"):
        bad(".nojekyll missing — Pages would run Jekyll over 8k+ JSON files")

    root = load(api / "index.json") or {}
    for key in ("nl_rag", "kind", "counts", "endpoints", "read_this_first", "license"):
        if key not in root:
            bad(f"root manifest missing '{key}'")
    if not exists(api / "README.txt"):
        bad("README.txt (NL-RAG(7)) missing")
    for name in ("corpus.json", "openapi.json", "stats.json"):
        load(api / name)

    stats = load(api / "stats.json") or {}
    si = load(api / "search" / "index.json") or {}
    ci = load(api / "domains" / "index.json") or {}

    # every routing-table entry must exist, and every bucket name must be self-consistent
    for kind, key in (("q", "term"), ("t", "title")):
        for row in (si.get("shards", {}) or {}).get(key, []):
            p = api / "search" / kind / f"{row['bucket']}.json"
            if not exists(p):
                bad(f"routing table lists {p.name} but it is not there")
    for row in ci.get("buckets", []):
        if not exists(api / "domains" / f"{row['bucket']}.json"):
            bad(f"catalog routing table lists bucket {row['bucket']} but the page is missing")

    domain_dir = api / "domain"
    domains = sorted(p.stem for p in domain_dir.glob("*.json"))
    if len(domains) != stats.get("domains"):
        bad(f"stats claim {stats.get('domains')} domains, tree has {len(domains)}")

    # --- the walk: term shard -> hit -> domain record -> document -> raw markdown
    checked_terms = walked = 0
    raw_re = re.compile(r"^https://raw\.githubusercontent\.com/[^/]+/[^/]+/[^/]+/packs/")
    for shard in cap(sorted((api / "search" / "q").glob("*.json")), 40):
        sh = load(shard)
        if not sh:
            continue
        if sh.get("bucket") != shard.stem:
            bad(f"{shard.name} declares bucket {sh.get('bucket')!r}")
        for key in ("templates", "how_to_read", "terms"):
            if key not in sh:
                bad(f"{shard.name} missing '{key}' — the shard must be self-describing")
        tmpl = sh.get("templates", {})
        terms = list(sh.get("terms", {}))
        if terms != sorted(terms):
            bad(f"{shard.name} terms are not sorted — documented fuzzy fallback breaks")
        for term in cap(terms, 4):
            checked_terms += 1
            if bucket_of(term) != shard.stem:
                bad(f"term {term!r} sits in shard {shard.stem} but routes to {bucket_of(term)}")
            entry = sh["terms"][term]
            if not entry.get("hits"):
                bad(f"term {term!r} has no hits")
                continue
            if entry["df"] < len(entry["hits"]):
                bad(f"term {term!r}: df {entry['df']} < {len(entry['hits'])} hits")
            scores = [h["s"] for h in entry["hits"]]
            if scores != sorted(scores, reverse=True):
                bad(f"term {term!r} hits are not ranked")
            hit = entry["hits"][0]
            # the top hit promises literal hrefs; they must agree with the templates
            # the same shard publishes, or the two paths disagree about the corpus
            for key in ("raw", "domain_href"):
                if key not in hit:
                    bad(f"term {term!r}: top hit has no literal '{key}'")
            if "raw" in hit:
                want = tmpl["document_raw"].replace("{d}", hit["d"]).replace("{p}", hit["p"])
                if hit["raw"] != want:
                    bad(f"term {term!r}: literal raw {hit['raw']} != template expansion {want}")
                if not raw_re.match(hit["raw"]):
                    bad(f"term {term!r}: literal raw is not a packs/ URL: {hit['raw']}")
            rec = record(domain_dir, hit["d"])
            if not rec:
                bad(f"term {term!r} hit domain {hit['d']!r} has no record")
                continue
            expect = tmpl["domain"].replace("{d}", hit["d"])
            if rec["hrefs"]["self"] != expect:
                bad(f"{hit['d']}: template expands to {expect} but record self-href is "
                    f"{rec['hrefs']['self']}")
            # a hit may name a document, or a specific part of a split document
            ids = {d["id"] for d in rec["documents"]}
            ids |= {f"{hit['d']}/{s}" for d in rec["documents"] for s in d.get("part_slugs", [])}
            if f"{hit['d']}/{hit['p']}" not in ids:
                bad(f"term {term!r} points at {hit['d']}/{hit['p']}, absent from the record")
            for rel in entry.get("related", []):
                if not exists(api / "search" / "q" / f"{bucket_of(rel)}.json"):
                    bad(f"related term {rel!r} routes to a shard that does not exist")
            walked += 1

    # --- document records must be complete and must never inline a body
    doc_checked = 0
    for name in (domains if FULL else domains[:: max(len(domains) // 60, 1)]):
        rec = load(domain_dir / f"{name}.json")
        if not rec:
            continue
        for key in ("name", "synopsis", "documents", "counts", "hrefs", "see_also", "keywords"):
            if key not in rec:
                bad(f"domain {name} missing '{key}'")
        for doc in rec.get("documents", []):
            doc_checked += 1
            for key in ("id", "title", "source", "license", "raw", "outline"):
                if key not in doc:
                    bad(f"{doc.get('id', name)} missing '{key}'")
            raws = doc["raw"] if isinstance(doc["raw"], list) else [doc["raw"]]
            for r in raws:
                if not raw_re.match(r):
                    bad(f"{doc['id']}: raw href is not a packs/ raw URL: {r}")
            if doc.get("parts") and len(raws) != doc["parts"]:
                bad(f"{doc['id']}: parts={doc['parts']} but {len(raws)} raw hrefs")
            if any(k in doc for k in ("body", "text", "content")):
                bad(f"{doc['id']} inlines a body — the API must reference, not copy")
        for s in rec.get("see_also", []):
            if not exists(domain_dir / f"{s['domain']}.json"):
                bad(f"domain {name}: see_also -> {s['domain']} which has no record")

    # --- title axis carries literal hrefs; they must be well-formed
    for shard in cap(sorted((api / "search" / "t").glob("*.json")), 20):
        sh = load(shard) or {}
        for term, entry in cap(sh.get("terms", {}).items(), 3):
            for hit in cap(entry["hits"], 3):
                if "raw" in hit and not raw_re.match(hit["raw"]):
                    bad(f"title shard {shard.name}: bad raw href {hit['raw']}")
                if not hit.get("domain_href", "").endswith(".json"):
                    bad(f"title shard {shard.name}: bad domain_href on {term!r}")

    notes.append(f"walked {walked} term->domain->document paths over {checked_terms} terms")
    notes.append(f"validated {doc_checked} document records across {len(domains)} domains")
    notes.append(f"api payload {stats.get('api_bytes', 0) / 1e6:.1f} MB")

    for n in notes:
        print(f"  {n}")
    if fails:
        print(f"\nFAIL — {len(fails)} problem(s):", file=sys.stderr)
        for f in fails[:40]:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("\nOK — the API keeps every promise it makes about itself")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(main(Path(args[0] if args else "build/site")))
