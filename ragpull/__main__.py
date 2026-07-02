"""nl-rag CLI.

  python -m ragpull list                     # registry overview
  python -m ragpull pull [domain ...]        # fetch + normalize + gate + index (all domains when none named)
  python -m ragpull verify [domain ...]      # re-audit the committed packs
  python -m ragpull index [domain ...]       # regenerate INDEX.md / pack.facts / atlas.json from packs on disk
"""

import argparse
import sys
from datetime import date
from pathlib import Path

from . import emit, verify
from .fetch import FetchError, fetch
from .normalize import normalize, split_markdown
from .sources import DOMAINS, slug_for

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
CACHE = ROOT / ".cache"


def pick(names):
    if not names:
        return list(DOMAINS)
    bad = [n for n in names if n not in DOMAINS]
    if bad:
        sys.exit(f"unknown domain(s): {', '.join(bad)} — see `python -m ragpull list`")
    return names


def cmd_list(_args):
    total = 0
    for name, d in DOMAINS.items():
        total += len(d["pages"])
        print(f"{name:20} {len(d['pages']):3} pages  tags: {', '.join(d['tags'])}")
    print(f"{'TOTAL':20} {total:3} pages across {len(DOMAINS)} domains")


def cmd_pull(args):
    domains = pick(args.domains)
    ok = failed = rejected = cached = 0
    rejects = []
    for name in domains:
        d = DOMAINS[name]
        pack_dir = PACKS / name
        print(f"== {name} ({len(d['pages'])} pages)")
        for url in d["pages"]:
            slug = slug_for(url)
            try:
                html, from_cache = fetch(url, CACHE, force=args.force)
            except FetchError as e:
                print(f"   FETCH-FAIL {slug}: {e}")
                failed += 1
                continue
            cached += from_cache
            title, body = normalize(html)
            problems = verify.check_markdown(body)
            if problems:
                print(f"   REJECT {slug}: {'; '.join(problems)}")
                rejects.append((name, url, problems))
                rejected += 1
                continue
            parts = split_markdown(body)
            files = emit.write_page(pack_dir, slug, title, url, name, d["license"], d["tags"], parts)
            ok += 1
            note = f" ({len(files)} parts)" if len(files) > 1 else ""
            print(f"   ok {slug}{note}")
        _reindex(name)
    print(f"\npulled {ok} pages ({cached} from cache), {failed} fetch failures, {rejected} rejected by clean gates")
    if rejects:
        print("rejected:")
        for name, url, problems in rejects:
            print(f"  {name}: {url} — {'; '.join(problems)}")
    _write_atlas()
    return 1 if (failed + rejected) and args.strict else 0


def _reindex(name):
    d = DOMAINS[name]
    pack_dir = PACKS / name
    if not pack_dir.exists():
        return None
    facts = emit.distill_facts(name, pack_dir)
    rows = emit.write_index(name, pack_dir, d["tags"], d["license"])
    print(f"   index: {len(rows)} files, {facts} distilled facts")
    return rows


def _write_atlas():
    manifest = {"name": "nl-rag", "generated": date.today().isoformat(), "domains": []}
    for name, d in DOMAINS.items():
        pack_dir = PACKS / name
        if not pack_dir.exists():
            continue
        files = [p.name for p in sorted(pack_dir.glob("*.md")) if p.name != "INDEX.md"]
        manifest["domains"].append({
            "name": name,
            "tags": d["tags"],
            "license": d["license"],
            "files": files,
            "facts": (pack_dir / "pack.facts").exists(),
        })
    emit.write_atlas(ROOT, manifest)
    print(f"atlas.json: {len(manifest['domains'])} domains")


def cmd_index(args):
    for name in pick(args.domains):
        _reindex(name)
    _write_atlas()
    return 0


def cmd_verify(args):
    bad = 0
    checked = 0
    for name in pick(args.domains):
        pack_dir = PACKS / name
        if not pack_dir.exists():
            continue
        for md in sorted(pack_dir.glob("*.md")):
            if md.name == "INDEX.md":
                continue
            checked += 1
            problems = verify.check_file(md)
            if problems:
                bad += 1
                print(f"FAIL {md.relative_to(ROOT)}: {'; '.join(problems)}")
    print(f"verified {checked} pack files, {bad} failures")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(prog="ragpull")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    p = sub.add_parser("pull")
    p.add_argument("domains", nargs="*")
    p.add_argument("--force", action="store_true", help="bypass the fetch cache")
    p.add_argument("--strict", action="store_true", help="nonzero exit on any failure/reject")
    p = sub.add_parser("verify")
    p.add_argument("domains", nargs="*")
    p = sub.add_parser("index")
    p.add_argument("domains", nargs="*")
    args = ap.parse_args()
    fn = {"list": cmd_list, "pull": cmd_pull, "verify": cmd_verify, "index": cmd_index}[args.cmd]
    sys.exit(fn(args) or 0)


if __name__ == "__main__":
    main()
