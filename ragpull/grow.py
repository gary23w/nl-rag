"""AUTONOMOUS GROWER — the engine behind the hourly GitHub Action.

Each run: (1) check the repo's size against the limit and no-op if we've reached it; (2) discover
NEW technical topics not yet in the pack tree; (3) fetch + normalize each candidate and admit it
ONLY if it clears the same clean-data gates every hand-curated pack passed; (4) write the packs and
append the admitted domains to `ragpull/sources/auto_domains.json` (the `auto` registry module reads
it, so growth is permanent); (5) regenerate `atlas.json`. The workflow then commits + pushes.

"New" = a slug not already on disk and not previously rejected. "Usable" = passes normalize +
verify.check_markdown (rejects JS shells, boilerplate, non-prose) AND yields >= min-pages real pages,
so no thin or junk domains are ever committed. Stdlib only; runs headless on a CI runner.
"""

import argparse
import json
import os
import time
import urllib.request
from datetime import date
from pathlib import Path

from . import emit, verify
from .discover import discover, page_links
from .fetch import FetchError, fetch
from .normalize import normalize, split_markdown
from .sources import slug_for

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
CACHE = ROOT / ".cache"
AUTO_JSON = ROOT / "ragpull" / "sources" / "auto_domains.json"
AUTO_REJECTED = ROOT / "ragpull" / "sources" / "auto_rejected.txt"
LICENSE = "CC-BY-SA-4.0"  # every auto domain is Wikipedia prose

_COMMON = set(
    "the a an and or of to in for with on at is are be as by from data system model "
    "method process type value function computer science".split()
)


# ---------------------------------------------------------------- size governor
def repo_size_kb():
    """Authoritative server-side repo size (KB) from the GitHub API — what GitHub's 1GB soft
    limit is actually measured against. None if unavailable (then we fall back to local size)."""
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        return None
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"User-Agent": "nl-rag-grower", "Accept": "application/vnd.github+json"},
    )
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return int(json.loads(r.read().decode()).get("size", 0))
    except Exception:
        return None


def local_packs_mb():
    total = 0
    for p in PACKS.rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total / (1024 * 1024)


def at_limit(max_repo_mb: float, max_packs_mb: float):
    kb = repo_size_kb()
    if kb is not None and kb / 1024 >= max_repo_mb:
        return True, f"GitHub repo size {kb/1024:.0f}MB >= {max_repo_mb:.0f}MB limit"
    mb = local_packs_mb()
    if mb >= max_packs_mb:
        return True, f"local packs {mb:.0f}MB >= {max_packs_mb:.0f}MB limit"
    return False, f"repo {'%.0fMB' % (kb/1024) if kb else '?'} / packs {mb:.0f}MB — under limit"


# ---------------------------------------------------------------- admission
def _tags(title: str, hint: str):
    tl = " ".join(title.lower().replace("(", " ").replace(")", " ").split())
    tags = [tl] if (" " in tl or (len(tl) >= 5 and tl not in _COMMON)) else []
    h = " ".join(hint.lower().split())
    if h and h != "linked" and h not in tags and " " in h:
        tags.append(h)
    if not tags:  # last resort so every pack has a tag
        tags = [tl or "reference"]
    return tags[:6]


def _usable_page(url: str, force: bool):
    """Fetch+normalize+gate one page. Return (slug, title, parts) or None."""
    try:
        html, _ = fetch(url, CACHE, force=force)
    except FetchError:
        return None
    except Exception:
        return None
    try:
        title, body = normalize(html)
        if verify.check_markdown(body):  # non-empty ⇒ failed a clean-data gate
            return None
        return slug_for(url), (title or url), split_markdown(body)
    except Exception:
        return None


def build_domain(title, url, hint, min_pages, max_pages, taken_slugs, force):
    """Assemble a multi-page domain around a candidate article. None if not usable enough."""
    domain = slug_for(url)
    if domain in taken_slugs:
        return None
    main = _usable_page(url, force)
    if main is None:
        return None
    pages, page_slugs, srcs = [], {main[0]}, [url]
    pages.append(main)
    # follow the article's own outbound links to build a real multi-page pack
    try:
        from .discover import title_to_url
        related = page_links(title)
    except Exception:
        related = []
    for rt in related:
        if len(pages) >= max_pages:
            break
        rurl = title_to_url(rt)
        rslug = slug_for(rurl)
        if rslug in page_slugs or rslug == domain:
            continue
        pg = _usable_page(rurl, force)
        if pg is None:
            continue
        page_slugs.add(rslug)
        pages.append(pg)
        srcs.append(rurl)
    if len(pages) < min_pages:
        return None
    return {"name": domain, "tags": _tags(title, hint), "license": LICENSE,
            "pages": srcs, "_pagedata": pages, "_srcmap": dict(zip([p[0] for p in pages], srcs))}


def write_domain(dom):
    pack_dir = PACKS / dom["name"]
    for slug, title, parts in dom["_pagedata"]:
        emit.write_page(pack_dir, slug, title, dom["_srcmap"][slug], dom["name"],
                        dom["license"], dom["tags"], parts)
    emit.distill_facts(dom["name"], pack_dir)
    emit.write_index(dom["name"], pack_dir, dom["tags"], dom["license"])


def rebuild_atlas():
    """Regenerate atlas.json from what's on disk — self-contained, no registry reload."""
    domains = []
    for d in sorted(p for p in PACKS.iterdir() if p.is_dir()):
        mds = [p.name for p in sorted(d.glob("*.md")) if p.name != "INDEX.md"]
        if not mds:
            continue
        meta = emit.read_frontmatter(d / mds[0])
        tags = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
        domains.append({"name": d.name, "tags": tags, "license": meta.get("license", ""),
                        "files": mds, "facts": (d / "pack.facts").exists()})
    emit.write_atlas(ROOT, {"name": "nl-rag", "generated": date.today().isoformat(),
                            "domains": domains})


def _load_json_list(path: Path):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def cmd_grow(args):
    stop, why = at_limit(args.max_repo_mb, args.max_packs_mb)
    print(f"[grow] size check: {why}")
    if stop:
        print("[grow] AT LIMIT — nothing to do.")
        return 0

    existing = {p.name for p in PACKS.iterdir() if p.is_dir()} if PACKS.exists() else set()
    rejected = set()
    if AUTO_REJECTED.exists():
        rejected = {ln.strip() for ln in AUTO_REJECTED.read_text(encoding="utf-8").splitlines() if ln.strip()}
    auto = _load_json_list(AUTO_JSON)
    taken = set(existing)
    added_slugs = set()

    def is_new(url):
        s = slug_for(url)
        return s not in taken and s not in rejected and s not in added_slugs

    # seed link-expansion from the most-recently accepted auto domains (follow the frontier)
    seed_titles = []
    for d in auto[-40:]:
        pg = d.get("pages") or []
        if pg:
            t = pg[0].rsplit("/", 1)[-1].replace("_", " ")
            seed_titles.append(t)

    import random
    rng = random.Random(int(time.time()))
    rng.shuffle(seed_titles)

    added = new_rejects = 0
    t0 = time.time()
    for title, url, hint in discover(rng, want=args.budget * 5, is_new=is_new, seed_titles=seed_titles):
        if added >= args.budget:
            break
        if time.time() - t0 > args.max_seconds:
            print("[grow] time budget reached")
            break
        dom = build_domain(title, url, hint, args.min_pages, args.max_pages, taken, args.force)
        if dom is None:
            new_rejects += 1
            rejected.add(slug_for(url))
            continue
        write_domain(dom)
        auto.append({"name": dom["name"], "tags": dom["tags"], "license": dom["license"], "pages": dom["pages"]})
        taken.add(dom["name"])
        added_slugs.add(dom["name"])
        added += 1
        print(f"[grow] + {dom['name']} ({len(dom['_pagedata'])} pages) — {title}")
        if added % 8 == 0:  # re-check size mid-run so a big run can't overshoot
            stop, _ = at_limit(args.max_repo_mb, args.max_packs_mb)
            if stop:
                print("[grow] hit size limit mid-run")
                break

    if added:
        AUTO_JSON.write_text(json.dumps(auto, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        rebuild_atlas()
    if new_rejects:
        AUTO_REJECTED.write_text("\n".join(sorted(rejected)) + "\n", encoding="utf-8", newline="\n")

    print(f"[grow] DONE: +{added} new usable domains, {new_rejects} candidates rejected, "
          f"{len(auto)} auto-domains total, packs {local_packs_mb():.0f}MB")
    return 0


def add_parser(sub):
    p = sub.add_parser("grow", help="autonomously discover + admit new usable domains (CI grower)")
    p.add_argument("--budget", type=int, default=40, help="max new domains to admit this run")
    p.add_argument("--min-pages", dest="min_pages", type=int, default=3, help="min usable pages per domain")
    p.add_argument("--max-pages", dest="max_pages", type=int, default=8, help="max pages per domain")
    p.add_argument("--max-repo-mb", dest="max_repo_mb", type=float, default=950.0,
                   help="stop when the GitHub repo size reaches this many MB")
    p.add_argument("--max-packs-mb", dest="max_packs_mb", type=float, default=3000.0,
                   help="local-size safety ceiling on packs/ (MB)")
    p.add_argument("--max-seconds", dest="max_seconds", type=int, default=1500, help="per-run wall-clock budget")
    p.add_argument("--force", action="store_true", help="bypass the fetch cache")
    return p
