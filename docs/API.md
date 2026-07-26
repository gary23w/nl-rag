# The nl-rag corpus API

A machine-readable manual. Canonical documentation, normalized to clean markdown,
addressed and consumed like man pages — **for AI readers only**. There is no frontend, no
HTML, no styling, and nothing to render. Every response is a corpus record.

Base URL: `https://gary23w.github.io/nl-rag`
Start here: [`/api/v1/index.json`](https://gary23w.github.io/nl-rag/api/v1/index.json) ·
[`/api/v1/README.txt`](https://gary23w.github.io/nl-rag/api/v1/README.txt) (the NL-RAG(7) man page)

## The one constraint that shapes everything

GitHub Pages is static. **It cannot read `?q=`.** So search is not a query — it is a
*path you construct offline*:

```
bucket = first two characters of the lowercased term,
         any character outside [a-z0-9] replaced with '_',
         terms shorter than two characters padded with '_'

  ownership -> ow        zig -> zi        c++ -> c_        x86 -> x8
```

```bash
curl https://gary23w.github.io/nl-rag/api/v1/search/q/ow.json    # then read terms["ownership"]
```

Every posting for a term lives in exactly that one shard, so **one GET answers one term**.
Keys inside a shard are sorted, which makes the shard its own fuzzy fallback: on a miss,
scan the keys for the nearest match instead of guessing another URL.

## Context structure

The corpus model is `corpus > domain > document > section | fact`. Schemas are served at
[`/api/v1/corpus.json`](https://gary23w.github.io/nl-rag/api/v1/corpus.json), and the
machine contract at `/api/v1/openapi.json`.

| record | url | what it carries |
| --- | --- | --- |
| domain | `/api/v1/domain/{name}.json` | the manual's section: synopsis, keywords, tags, license, origin, SEE ALSO, and **every document's man scaffolding** |
| document | inside the domain record | NAME, SYNOPSIS, outline (each heading with its line number), fenced-code languages, provenance-tagged facts, SOURCE, license, and the raw href |
| section | an `outline` entry | `{level, heading, line}` — line-addressed inside the raw markdown |
| fact | `packs/{domain}/pack.facts` | one declarative sentence per line, tagged `[src:domain/page]` |

**Document bodies are never copied into the API.** A record carries the scaffolding plus
the literal URL of the markdown that already lives in `packs/`. One corpus, one copy —
which is also why regenerating the index never rewrites the corpus.

## Endpoints

| url | what |
| --- | --- |
| `/api/v1/index.json` | root manifest, endpoint catalog, counts |
| `/api/v1/README.txt` | NL-RAG(7) — the traversal protocol as a man page |
| `/api/v1/corpus.json` | record schemas |
| `/api/v1/openapi.json` | OpenAPI 3.1 contract |
| `/api/v1/stats.json` | counts |
| `/api/v1/search/index.json` | search protocol + every shard and its size |
| `/api/v1/search/q/{bucket}.json` | **term search** → ranked domains + similar terms |
| `/api/v1/search/t/{bucket}.json` | **title/name/tag search** → documents, with literal hrefs |
| `/api/v1/domains/index.json` | domain catalog routing table |
| `/api/v1/domains/{bucket}.json` | domain catalog page |
| `/api/v1/domain/{name}.json` | domain record |
| `raw.githubusercontent.com/.../packs/{domain}/{slug}.md` | the document body — clean markdown |

## A session

```
GET /api/v1/search/q/go.json
    terms["goroutine"] = { df: 1,
                           hits: [{ d: "golang", p: "sync", s: 237.87 }],
                           related: ["func", "string", "error", "int", "err", "returns"] }

GET /api/v1/domain/golang.json          # expand hits[0].d with templates.domain
    -> synopsis, keywords, see_also, and every document's outline

GET .../packs/golang/sync.md            # expand d + p with templates.document_raw
    -> 24 KB of clean markdown, frontmatter intact
```

`templates` ships inside every shard, so short keys (`d`, `p`, `t`, `s`) expand without
consulting this page. Multi-word queries: fetch one shard per word and intersect on
`hit.d` — the intersection is exact and nothing server-side will do it for you.

## Coverage, honestly

- **Term axis** — each domain's top 250 characteristic terms. A doc-level index over all
  73k documents is ~400 MB of JSON, and static hosting ships it whole; so an *incidental*
  word may be missing from `search/q` even though the corpus contains it. That is a
  size trade, not a claim about the corpus.
- **Title axis** — complete for every document title, domain name and tag.
- **Fallback** — `packs/{domain}/pack.facts` holds every distilled sentence for a domain in
  one fetchable file. Use it when a term search comes up empty.
- **Ranking** — tf·idf over domains, with a ×1.6 boost when the term is also in the
  domain's name or tags. The grower copies neighbour pages between packs, so without that
  boost near-duplicate packs tie on raw term frequency.

## Building and publishing

```bash
python -m ragpull api                                  # full tree -> build/site
python -m ragpull api --only rust,zig --out /tmp/smoke  # targeted build
python -m ragpull api --limit 40                        # first 40 domains
python scripts/check_api.py build/site                  # the gate
```

`scripts/check_api.py` walks the tree the way a consumer would and fails the publish if the
API breaks a promise it makes about itself: bucket rules that don't resolve, unranked hits,
`see_also` pointing at absent records, a template that doesn't expand, a raw href that
isn't a `packs/` URL, or a document record that inlines a body.

`.github/workflows/publish-api.yml` builds the tree and deploys it **straight to GitHub Pages
as a workflow artifact** (`upload-pages-artifact` → `deploy-pages`). No branch ever holds
generated JSON, so regenerating the index accumulates no history anywhere and `main` carries
nothing but the corpus and the tooling.

The workflow passes `configure-pages`' `base_url` to `--base`, so every generated href is the
site's real address — renaming the repo or owner does not strand the index. `enablement: true`
means the Pages site configures itself on first run; the source is already set to **GitHub
Actions** for this repo.

Runs daily at 05:23 UTC, or on demand from the Actions tab with optional `base` / `limit`
overrides.

Index shape is tunable at the top of [`ragpull/api.py`](../ragpull/api.py):
`TOP_TERMS_PER_DOMAIN`, `HITS_PER_TERM`, `OUTLINE_CAP`, `FACTS_PER_DOC`,
`SEE_ALSO_PER_DOMAIN`. The build warns if the payload approaches Pages' 1 GB site limit.

## Attribution

The tooling is MIT. Every document keeps its **upstream license**, declared in its own
frontmatter and in the record's `license` field; most of the corpus is CC-BY-SA-4.0. The
`source` URL is the attribution — carry it into anything you generate from this corpus.
