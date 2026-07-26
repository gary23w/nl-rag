"""The local corpus endpoint — the static API plus the live fallback it cannot host.

GitHub Pages serves files, so the published API can neither read `?q=` nor fetch anything
at request time. Running the same tree here closes both gaps at zero hosting cost, because
the compute is the consumer's own machine:

    python -m ragpull serve --site _site
    curl 'http://127.0.0.1:8077/api/v1/resolve?q=tail+latency+budgeting'

Every static path behaves exactly as it does on Pages — same shards, same records, same
bytes — so code written against the hosted API works here unchanged. The additions are:

    GET /api/v1/resolve?q=<query>     corpus first, live fallback on a genuine miss
    GET /api/v1/resolve/<query>       same, path-addressed (matches the static style)
    GET /api/v1/live/<url>            normalize ONE url on demand
    GET /api/v1/health                what this server can and cannot do

A resolution says which path answered it (`resolved_by`), and live documents inline their
body because nothing hosts them yet. Nothing is invented: if a page cannot be retrieved or
fails the clean-data gates, it is reported as unretrievable.
"""

import json
import urllib.parse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import live

API = "/api/v1"


class Handler(SimpleHTTPRequestHandler):
    root: Path = Path(".")
    allow_live: bool = True
    cache_dir: Path = Path(".cache")

    def log_message(self, fmt, *args):          # one tidy line per request
        print(f"  {self.address_string()} {fmt % args}")

    def _send(self, obj, code: int = 200):
        body = json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        # a local agent may well be driven from a browser page
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urllib.parse.urlsplit(self.path)
        path = urllib.parse.unquote(parsed.path)
        if path == f"{API}/health":
            return self._send(self._health())
        if path == f"{API}/resolve" or path.startswith(f"{API}/resolve/"):
            q = urllib.parse.parse_qs(parsed.query).get("q", [""])[0]
            if not q and path.startswith(f"{API}/resolve/"):
                q = path[len(f"{API}/resolve/"):]
            if not q.strip():
                return self._send({"error": "no query", "usage":
                                   f"{API}/resolve?q=<query> or {API}/resolve/<query>"}, 400)
            return self._resolve(q.strip())
        if path.startswith(f"{API}/live/"):
            url = path[len(f"{API}/live/"):]
            if parsed.query:                    # a url's own ?query survived the split
                url = f"{url}?{parsed.query}"
            if not url.startswith(("http://", "https://")):
                return self._send({"error": "not an absolute http(s) url", "got": url}, 400)
            return self._resolve(url)
        return super().do_GET()

    def _health(self):
        built = (self.root / "api" / "v1" / "index.json").exists()
        return {
            "nl_rag": "v1", "kind": "health",
            "static_tree": str(self.root) if built else None,
            "static_tree_built": built,
            "serves": [f"{API}/resolve?q=", f"{API}/resolve/<query>", f"{API}/live/<url>"]
                      + ([f"{API}/... (the full static API)"] if built else []),
            "live_fallback": self.allow_live,
            "can_read_query_strings": True,
            "note": ("this is the LOCAL endpoint. it mirrors the hosted static API byte for "
                     "byte and adds the two things static hosting cannot do: query strings "
                     "and fetching content the corpus lacks."
                     if built else
                     "no built tree found — /resolve still works (corpus lookup reads "
                     "atlas.json); run `ragpull api --out _site` to serve the full API."),
        }

    def _resolve(self, query: str):
        if not self.allow_live:
            idx = live.corpus_index(self.root_repo)
            hits = live.lookup_corpus(query, idx)
            return self._send({
                "nl_rag": "v1", "kind": "resolution", "query": query,
                "resolved_by": "corpus" if hits else "none",
                "corpus_hits": hits, "results": [],
                "note": "live fallback is disabled on this server (--no-live)",
            }, 200 if hits else 404)
        try:
            env = live.resolve(query, self.root_repo, cache_dir=self.cache_dir)
        except Exception as e:                  # a resolver crash must not kill the server
            return self._send({"error": f"{type(e).__name__}: {e}", "query": query}, 502)
        code = 200 if (env.get("corpus_hits") or env.get("results")) else 404
        return self._send(env, code)


def cmd_serve(args, repo_root: Path):
    site = Path(args.site) if args.site else repo_root / "_site"
    handler = Handler
    handler.root = site
    handler.root_repo = repo_root
    handler.allow_live = not args.no_live
    handler.cache_dir = repo_root / ".cache"
    built = (site / "api" / "v1" / "index.json").exists()

    print(f"nl-rag endpoint on http://{args.host}:{args.port}")
    print(f"  static tree : {site}{'' if built else '  (NOT BUILT — run `ragpull api --out _site`)'}")
    print(f"  live fallback: {'on' if handler.allow_live else 'off'}")
    print(f"  try: curl 'http://{args.host}:{args.port}{API}/health'")
    srv = ThreadingHTTPServer((args.host, args.port),
                              partial(handler, directory=str(site)))
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    return 0
