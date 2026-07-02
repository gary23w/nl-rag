# nl-rag

**The mega RAG repository** — canonical documentation pulled, normalized into clean AI
markdown, and served as fetchable packs. Built as the knowledge substrate for
[nl-veil](https://github.com/gary23w/nl-veil): the veil's source atlas points scouts at these
packs first, so a small model reads pre-cleaned markdown instead of fighting HTML.

## What's here

- `packs/<domain>/` — one directory per knowledge domain (121 domains, ~1100 upstream
  pages): every language paradigm and problem-solving method, the full embedded/IoT stack
  (microcontrollers, RTOS, buses, IoT protocols, electronics, control theory, DSP, FPGA,
  PLC/SCADA, robotics), mathematics from linear algebra to category theory, CS systems
  (OS, compilers, automata, distributed systems, formal methods), the complete GoF pattern
  catalog plus architecture/concurrency patterns, AI/ML, graphics and game development,
  cloud, the canonical books of the craft, and Rosetta Code polyglot tasks. Every file is:
  - **clean markdown** — no HTML, no nav/chrome/cookie banners, fenced code with language
    tags, GFM tables, citation markers stripped
  - **frontmattered** — `title`, `source` (upstream URL), `domain`, `license`, `tags`,
    `fetched`
  - **fetch-sized** — oversized pages (the Zig langref, the bash manual, RFC 9110) are split
    at heading boundaries into parts a model can pull one at a time
- `packs/<domain>/INDEX.md` — the pack's table of contents with absolute raw URLs: fetch the
  index, then fetch any page it lists, straight over `raw.githubusercontent.com`
- `packs/<domain>/pack.facts` — the pack distilled to one declarative sentence per line with
  `[src:domain/page]` provenance tags; bulk-loads into
  [neuron-db](https://github.com/gary23w/neuron-db) via `neuron import pack.facts --scope knowledge`
- `atlas.json` — machine-readable manifest: every domain, its tags, license, and file list

## Domains

Languages (python, rust, ruby, golang, javascript, typescript, zig, c-cpp, java, kotlin,
scala, clojure, csharp-dotnet, haskell, ocaml, elixir, erlang, racket, common-lisp,
perl, lua, php, swift, dart, r, julia, x86/arm/risc-v assembly, the legacy canon) ·
paradigms & problem-solving · embedded & IoT (embedded-systems, iot-protocols,
hardware-interfaces, electronics, control-systems, dsp, fpga-hdl, plc-scada, robotics,
real-time-systems, freertos, esp32, arduino, raspberry-pi, computer-architecture) ·
mathematics (linear-algebra, calculus, discrete-mathematics, number-theory,
numerical-methods, floating-point, statistics, logic, lambda/type theory, category-theory,
information-theory, computational-geometry, optimization) · CS systems (operating-systems,
compilers, automata, distributed-systems, consensus, complexity, formal-methods,
performance, compression, debugging) · patterns & practice (full GoF catalog,
architecture-patterns, concurrency-patterns, code-quality, agile-devops,
sre-observability, canonical-books) · data & AI (machine-learning, classic-ai,
data-engineering, databases, caching) · web & cloud (react, vue, svelte, graphql, grpc,
kubernetes, cloud-computing, graphics, game-dev) · security & crypto · tooling & ops ·
rosetta-code (the same task in dozens of languages)

## The tool

`ragpull/` is the puller/normalizer — Python stdlib only, no dependencies.

```
python -m ragpull list              # registry overview
python -m ragpull pull              # fetch + normalize + clean-gate + index everything
python -m ragpull pull rust zig     # just those domains
python -m ragpull verify            # re-audit every committed pack file
python -m ragpull index             # regenerate INDEX.md / pack.facts / atlas.json
```

The pipeline per page: polite cached fetch (per-host rate limit, charset sniffing) →
content-root detection (main/article/known doc-site containers) → chrome pruning →
markdown rendering (headings, fenced code, GFM tables, lists; man pages unwrapped from
`<pre>` into real sections) → **clean-data gates** (HTML-residue, boilerplate-phrase,
prose-ratio, sentence-count checks — a page that fails is rejected, never shipped) →
frontmattered emit with heading-boundary splitting.

To add a domain: add an entry to `ragpull/sources.py` (tags, license, curated page URLs)
and run `python -m ragpull pull <name>`.

## Wiring into the veil

nl-veil's compiled-in source atlas (`src/worker/locs/atlas.zig`) carries a `pack` pointer
for every domain covered here. When a goal/gap matches a domain, the research directive
lists `PACK <raw INDEX url>` ahead of the live doc-site seeds — the scout fetches
pre-normalized markdown first (and the veil's fetch cache makes every pack page a
once-ever GET), with the origin sites still listed for freshness-critical topics.

## Licenses

The tool is MIT. Pack content keeps its **upstream license**, declared per-file in
frontmatter and per-domain in [SOURCES.md](SOURCES.md), with the `source:` URL as
attribution.
