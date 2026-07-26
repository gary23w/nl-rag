"""nl-rag CLI.

  python -m ragpull list                     # registry overview
  python -m ragpull pull [domain ...]        # fetch + normalize + gate + index (all domains when none named)
  python -m ragpull verify [domain ...]      # re-audit the committed packs
  python -m ragpull index [domain ...]       # regenerate INDEX.md / pack.facts / atlas.json from packs on disk
  python -m ragpull atlas                    # regenerate atlas.json only (no pack churn)
  python -m ragpull grow [--budget N]        # autonomously discover + admit new usable domains (CI grower)
  python -m ragpull api [--out DIR]          # generate the static AI-facing REST API (GitHub Pages tree)
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

# Force UTF-8 stdout/stderr at IMPORT time (before any print): a redirected pipe on Windows —
# or Git Bash — defaults to cp1252/ascii, and a single en-dash in a page title or URL crashes
# the whole run with UnicodeEncodeError. Doing this in main() was too late for early output.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

from . import api, emit, verify
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
            except Exception as e:  # a malformed URL (literal non-ascii, bad scheme) must not kill the chunk
                print(f"   FETCH-FAIL {slug}: {type(e).__name__}: {e}")
                failed += 1
                continue
            try:
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
            except Exception as e:  # one bad page never aborts the run
                print(f"   ERROR {slug}: {type(e).__name__}: {e}")
                failed += 1
                continue
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
    # sorted by domain name so atlas.json diffs stay minimal as the hourly grower appends
    # (the grower's rebuild_atlas uses the same order)
    manifest = {"name": "nl-rag", "generated": date.today().isoformat(), "domains": []}
    auto = emit.auto_domain_names(ROOT)
    for name in sorted(DOMAINS):
        d = DOMAINS[name]
        pack_dir = PACKS / name
        if not pack_dir.exists():
            continue
        files = [p.name for p in sorted(pack_dir.glob("*.md")) if p.name != "INDEX.md"]
        manifest["domains"].append({
            "name": name,
            "tags": d["tags"],
            "license": d["license"],
            "origin": "auto" if name in auto else "curated",
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


def cmd_atlas(_args):
    # atlas.json alone — no pack churn; used after registry/metadata changes
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


def cmd_resolve(args):
    """Corpus first, live fallback on a genuine miss. Prints one self-describing JSON
    envelope on stdout so it pipes straight into whatever asked."""
    from . import live

    env = live.resolve(args.query, ROOT, cache_dir=CACHE, want=args.want,
                       max_candidates=args.candidates, force=args.force,
                       progress=(lambda *_: None) if args.quiet else
                                (lambda m: print(m, file=sys.stderr)))
    if args.admit:
        tags = [t.strip() for t in (args.tags or "").split(",") if t.strip()] or None
        env["admission"] = live.admit(env, ROOT, tags=tags)
    print(json.dumps(env, ensure_ascii=False, indent=1))
    # a miss that retrieved nothing is not a success — let a caller branch on the exit code
    return 0 if (env.get("corpus_hits") or env.get("results")) else 3


def _serve(args):
    from .serve import cmd_serve

    return cmd_serve(args, ROOT)


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
    sub.add_parser("atlas")
    p = sub.add_parser("api", help="generate the static AI-facing REST API (GitHub Pages tree)")
    p.add_argument("--out", help="output directory (default build/site)")
    p.add_argument("--base", default=api.DEFAULT_BASE,
                   help=f"public base URL of the published site (default {api.DEFAULT_BASE})")
    p.add_argument("--limit", type=int, help="only the first N domains — for a smoke build")
    p.add_argument("--only", help="comma-separated domain names — for a targeted build")
    p = sub.add_parser("resolve", help="answer a query: corpus first, live fallback on a miss")
    p.add_argument("query", help="a search phrase, or an absolute http(s) url")
    p.add_argument("--want", type=int, default=3, help="usable documents to gather (default 3)")
    p.add_argument("--candidates", type=int, default=8, help="urls to consider (default 8)")
    p.add_argument("--admit", action="store_true",
                   help="fold the result into packs/ with the grower's own writer")
    p.add_argument("--tags", help="comma-separated tags to use when admitting")
    p.add_argument("--force", action="store_true", help="bypass the fetch cache")
    p.add_argument("--quiet", action="store_true", help="JSON only, no progress lines")
    p = sub.add_parser("serve", help="serve the static API locally, with the live fallback")
    p.add_argument("--site", help="built API tree to serve (default _site)")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=8077)
    p.add_argument("--no-live", action="store_true", help="corpus only; never fetch")
    from .grow import add_parser as _grow_parser, cmd_grow
    _grow_parser(sub)
    args = ap.parse_args()
    fn = {"list": cmd_list, "pull": cmd_pull, "verify": cmd_verify, "index": cmd_index,
          "atlas": cmd_atlas, "grow": cmd_grow,
          "api": lambda a: api.cmd_api(a, ROOT),
          "resolve": cmd_resolve,
          "serve": lambda a: _serve(a)}[args.cmd]

    # big-stack worker thread because the normalizer recurses to DOM depth and a raised
    # recursionlimit past the native stack is a silent process kill, not a Python exception
    # (utf-8 stdout is already forced at module import above)
    import threading

    rc: list[int] = [0]

    def run():
        try:
            rc[0] = fn(args) or 0
        except SystemExit as e:
            # sys.exit("message") carries a str, not a status — CPython prints it and exits 1.
            # int()-ing it blindly turned every argument-error message into a ValueError
            # traceback from inside the worker thread.
            if e.code is None or isinstance(e.code, int):
                rc[0] = e.code or 0
            else:
                print(e.code, file=sys.stderr)
                rc[0] = 1
        except BaseException:
            import traceback

            traceback.print_exc()
            rc[0] = 70  # a thread death must NOT read as success

    threading.stack_size(64 << 20)
    t = threading.Thread(target=run)
    t.start()
    t.join()
    sys.exit(rc[0])


if __name__ == "__main__":
    main()
