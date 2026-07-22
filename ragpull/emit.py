"""Emitters: frontmattered pack pages, per-domain INDEX.md, distilled pack.facts,
and the machine-readable atlas.json manifest."""

import json
import re
from datetime import date
from pathlib import Path

RAW_BASE = "https://raw.githubusercontent.com/gary23w/nl-rag/main"

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
_FENCE_RE = re.compile(r"^(`{3,4})[^\n]*\n.*?^\1\s*$", re.S | re.M)
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9`*\"'(])")


def frontmatter(title: str, source: str, domain: str, license_id: str, tags: list[str], part=None) -> str:
    t = title.replace('"', "'")
    lines = [
        "---",
        f'title: "{t}"',
        f"source: {source}",
        f"domain: {domain}",
        f"license: {license_id}",
        f"tags: {', '.join(tags)}",
        f"fetched: {date.today().isoformat()}",
    ]
    if part:
        lines.append(f"part: {part[0]}/{part[1]}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def write_page(pack_dir: Path, slug: str, title: str, source: str, domain: str,
               license_id: str, tags: list[str], parts: list[str]) -> list[Path]:
    pack_dir.mkdir(parents=True, exist_ok=True)
    out = []
    multi = len(parts) > 1
    for i, body in enumerate(parts, 1):
        name = f"{slug}-p{i:02d}.md" if multi else f"{slug}.md"
        fm = frontmatter(title if not multi else f"{title} (part {i}/{len(parts)})",
                         source, domain, license_id, tags,
                         part=(i, len(parts)) if multi else None)
        head = f"# {title}\n\n" if not body.lstrip().startswith("#") else ""
        p = pack_dir / name
        p.write_text(fm + head + body + "\n", encoding="utf-8", newline="\n")
        out.append(p)
    return out


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = _FM_RE.match(text)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    meta["_body"] = text[m.end():] if m else text
    return meta


def strip_fences(body: str) -> str:
    return _FENCE_RE.sub(" ", body)


def distill_facts(domain: str, pack_dir: Path, cap_per_domain: int = 1200) -> int:
    """One clean declarative sentence per line, provenance-tagged, deduped.
    Format matches the neuron CLI `.facts` import (plain lines; caller sets scope)."""
    seen = set()
    lines = []
    for md in sorted(pack_dir.glob("*.md")):
        if md.name == "INDEX.md":
            continue
        meta = read_frontmatter(md)
        stem = md.stem
        prose = strip_fences(meta["_body"])
        for raw_line in prose.splitlines():
            line = raw_line.strip()
            if not line or line.startswith(("#", "|", ">", "-", "*", "```", "1.")):
                continue
            for sent in _SENT_SPLIT.split(line):
                s = " ".join(sent.split()).strip()
                if not (40 <= len(s) <= 300) or not s.endswith((".", "!", "?")):
                    continue
                letters = sum(c.isalpha() or c == " " for c in s)
                if letters / len(s) < 0.72:
                    continue
                key = s.lower()
                if key in seen:
                    continue
                seen.add(key)
                lines.append(f"[src:{domain}/{stem}] {s}")
                if len(lines) >= cap_per_domain:
                    break
            if len(lines) >= cap_per_domain:
                break
        if len(lines) >= cap_per_domain:
            break
    if not lines:
        return 0
    out = pack_dir / "pack.facts"
    header = (f"# nl-rag distilled facts — domain: {domain}\n"
              f"# one declarative sentence per line; load with:  neuron --db app.db import pack.facts --scope knowledge\n")
    out.write_text(header + "\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def write_index(domain: str, pack_dir: Path, tags: list[str], license_id: str) -> list[dict]:
    """INDEX.md: the fetchable table of contents for a pack (full raw URLs so a scout
    can go straight from the index to any page with one GET). Returns manifest rows."""
    rows = []
    for md in sorted(pack_dir.glob("*.md")):
        if md.name == "INDEX.md":
            continue
        meta = read_frontmatter(md)
        rows.append({
            "file": md.name,
            "title": meta.get("title", md.stem),
            "source": meta.get("source", ""),
            "bytes": md.stat().st_size,
        })
    lines = [
        f"# {domain} — nl-rag pack",
        "",
        f"Pre-normalized AI markdown. tags: {', '.join(tags)}. license: {license_id} (see SOURCES.md).",
        "Fetch any page below as raw markdown — no HTML, no chrome, ready to ingest.",
        "",
    ]
    for r in rows:
        lines.append(f"- [{r['title']}]({RAW_BASE}/packs/{domain}/{r['file']}) — upstream: {r['source']}")
    facts = pack_dir / "pack.facts"
    if facts.exists():
        lines.append(f"- [pack.facts]({RAW_BASE}/packs/{domain}/pack.facts) — distilled one-line facts (neuron CLI import)")
    (pack_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return rows


def auto_domain_names(root: Path) -> set[str]:
    """Names the grower appended to auto_domains.json — every other pack is hand-curated.
    Both atlas writers stamp `origin` from this one rule so a consumer can tier on it
    (e.g. vendor only curated packs) without loading the Python registry."""
    p = root / "ragpull" / "sources" / "auto_domains.json"
    try:
        return {d["name"] for d in json.loads(p.read_text(encoding="utf-8")) if d.get("name")}
    except Exception:
        return set()


def write_atlas(root: Path, manifest: dict):
    manifest = dict(manifest)
    manifest["raw_base"] = RAW_BASE
    manifest["index_url_template"] = RAW_BASE + "/packs/{domain}/INDEX.md"
    (root / "atlas.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
