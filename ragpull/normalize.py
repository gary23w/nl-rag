"""HTML -> clean AI markdown. Stdlib only.

Three stages:
  1. parse   — tolerant tree build (html.parser), kill-list tags dropped at parse time
  2. select  — find the CONTENT ROOT (main/article/known doc-site containers), prune chrome
               (nav/toc/sidebar/footer/edit-links/citation markers) by class/id heuristics
  3. render  — headings/paragraphs/fenced code/GFM tables/lists/blockquotes; inline links keep
               their TEXT only (the frontmatter carries the source URL — hrefs are token noise
               for ingestion)

The output is meant to be chunked by sentence (the veil's ingestCorpus) or distilled to
one-line .facts, so prose fidelity beats layout fidelity everywhere.
"""

import re
from html.parser import HTMLParser

VOID = {"br", "hr", "img", "meta", "link", "input", "area", "base", "col", "embed", "source", "track", "wbr", "param"}
KILL = {"script", "style", "noscript", "nav", "footer", "aside", "form", "svg", "iframe", "button", "select", "option", "label", "dialog", "template", "video", "audio", "canvas", "object", "map", "figcaption"}
# junk containers by class/id fragment (word-ish bounded via regex)
JUNK_RE = re.compile(
    r"(?:^|[\s_-])(?:nav|navbar|menu|sidebar|sphinxsidebar|breadcrumbs?|footer|banner|cookie|announce(?:ment)?|edit|search|share|social|comments?|advert|ads|promo|skip|pagination|pager|feedback|toc|contents|mw-editsection|mw-jump|catlinks|interlanguage|navbox|infobox|vertical-navbox|hatnote|shortdescription|noprint|metadata|ambox|sistersitebox|headerlink|toolbar|related|prevnext|prev-next|page-nav|docs-nav|version-?switcher|language-?switcher|survey|newsletter|midpage|bottom-of-page|watermark|site-header|top-nav|example-header|language-name)(?:$|[\s_-])",
    re.I,
)
# wikipedia sections dropped wholesale at render time (heading text match)
DROP_SECTIONS = {"references", "external links", "see also", "further reading", "notes", "bibliography", "citations", "sources", "footnotes"}

_WS_RE = re.compile(r"[ \t\r\n\f]+")
_LANG_RE = re.compile(r"(?:language|lang|highlight|brush)[-: ]+([A-Za-z0-9+#]+)", re.I)


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.children = []
        self.parent = parent

    def cls_id(self):
        return (self.attrs.get("class", "") + " " + self.attrs.get("id", "")).strip()

    def text(self):
        out = []
        stack = [self]
        while stack:
            n = stack.pop()
            if isinstance(n, str):
                out.append(n)
            else:
                stack.extend(reversed(n.children))
        return "".join(out)


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("_root")
        self.cur = self.root
        self.kill_depth = 0
        self.kill_tag = None
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title" and not self.title:
            self._in_title = True
        if self.kill_depth:
            if tag == self.kill_tag and tag not in VOID:
                self.kill_depth += 1
            return
        if tag in KILL:
            if tag not in VOID:
                self.kill_depth = 1
                self.kill_tag = tag
            return
        node = Node(tag, attrs, self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        if self.kill_depth or tag in KILL:
            return
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if self.kill_depth:
            if tag == self.kill_tag:
                self.kill_depth -= 1
                if self.kill_depth == 0:
                    self.kill_tag = None
            return
        # pop to the nearest matching open tag (tolerates misnesting)
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if self.kill_depth or not data:
            return
        self.cur.children.append(data)


CONTENT_IDS = {"content", "bodycontent", "mw-content-text", "main-content", "maincontent", "main", "docs-content", "article"}
CONTENT_CLASSES = ("markdown-body", "md-content", "body", "document", "article-content", "post-content", "content", "book")


def _find_content_root(root: Node) -> Node:
    by_tag = {"main": None, "article": None, "body": None}
    by_id = None
    by_class = None
    stack = [root]
    while stack:
        n = stack.pop()
        if isinstance(n, str):
            continue
        if n.tag in by_tag and by_tag[n.tag] is None:
            by_tag[n.tag] = n
        if n.attrs.get("role", "") == "main" and by_id is None:
            by_id = n
        nid = n.attrs.get("id", "").lower()
        if nid in CONTENT_IDS and by_id is None:
            by_id = n
        if by_class is None:
            classes = n.attrs.get("class", "").lower().split()
            for c in CONTENT_CLASSES:
                if c in classes:
                    by_class = n
                    break
        stack.extend(n.children)
    return by_tag["main"] or by_tag["article"] or by_id or by_class or by_tag["body"] or root


def _prune(node: Node):
    kept = []
    for c in node.children:
        if isinstance(c, str):
            kept.append(c)
            continue
        ci = c.cls_id()
        if ci and JUNK_RE.search(ci):
            continue
        if c.tag == "sup" and "reference" in c.attrs.get("class", ""):
            continue  # wikipedia [n] citation markers
        if c.tag == "span" and "mw-cite-backlink" in ci:
            continue
        _prune(c)
        kept.append(c)
    node.children = kept


class Renderer:
    def __init__(self):
        self.blocks = []
        self.drop_section_level = 0  # >0: currently inside a dropped wikipedia-style section

    # ---- inline -------------------------------------------------------------
    def inline(self, node) -> str:
        if isinstance(node, str):
            return _WS_RE.sub(" ", node)
        t = node.tag
        inner = "".join(self.inline(c) for c in node.children)
        if t == "code":
            txt = inner.strip()
            return f"`{txt}`" if txt and "`" not in txt else txt
        if t in ("strong", "b"):
            return f"**{inner.strip()}**" if inner.strip() else ""
        if t in ("em", "i", "var", "cite", "dfn"):
            return f"*{inner.strip()}*" if inner.strip() else ""
        if t == "br":
            return " "
        if t == "img":
            alt = node.attrs.get("alt", "").strip()
            return f"({alt})" if alt else ""
        return inner  # a, span, abbr, sub, sup, ... -> text only

    def inline_block(self, node) -> str:
        s = "".join(self.inline(c) for c in node.children)
        return _WS_RE.sub(" ", s).strip()

    # ---- blocks -------------------------------------------------------------
    def emit(self, text):
        if text:
            self.blocks.append(text)

    def code_lang(self, node) -> str:
        probe = node
        for _ in range(3):
            if probe is None or isinstance(probe, str):
                break
            m = _LANG_RE.search(probe.attrs.get("class", ""))
            if m:
                lang = m.group(1).lower()
                if lang not in ("text", "plain", "default", "none", "output"):
                    return lang
            for c in probe.children:
                if not isinstance(c, str) and c.tag == "code":
                    m = _LANG_RE.search(c.attrs.get("class", ""))
                    if m:
                        return m.group(1).lower()
                    break
            probe = probe.parent
        return ""

    def pre_text(self, node) -> str:
        out = []

        def walk(n):
            if isinstance(n, str):
                out.append(n)
                return
            if n.tag == "br":
                out.append("\n")
                return
            for c in n.children:
                walk(c)
            if n.tag in ("div", "p", "tr"):  # line-per-div highlighters
                if out and not out[-1].endswith("\n"):
                    out.append("\n")

        walk(node)
        return "".join(out).strip("\n")

    def table(self, node) -> str:
        rows = []

        def collect(n):
            if isinstance(n, str):
                return
            if n.tag == "tr":
                cells = []
                for c in n.children:
                    if not isinstance(c, str) and c.tag in ("td", "th"):
                        cells.append(self.inline_block(c).replace("|", "\\|") or " ")
                if cells:
                    rows.append(cells)
                return
            for c in n.children:
                collect(c)

        collect(node)
        if not rows or len(rows) > 200:
            return ""
        width = max(len(r) for r in rows)
        if width > 8:  # layout table, not data — flatten to text
            return ""
        lines = []
        for i, r in enumerate(rows):
            r = r + [" "] * (width - len(r))
            lines.append("| " + " | ".join(r) + " |")
            if i == 0:
                lines.append("|" + "---|" * width)
        return "\n".join(lines)

    def list_block(self, node, ordered, depth=0) -> str:
        lines = []
        idx = 0
        for c in node.children:
            if isinstance(c, str) or c.tag != "li":
                continue
            idx += 1
            sub = []
            inline_parts = []
            for cc in c.children:
                if not isinstance(cc, str) and cc.tag in ("ul", "ol"):
                    sub.append(self.list_block(cc, cc.tag == "ol", depth + 1))
                elif not isinstance(cc, str) and cc.tag == "pre":
                    txt = self.pre_text(cc)
                    if txt:
                        sub.append("  " * (depth + 1) + "```\n" + txt + "\n" + "  " * (depth + 1) + "```")
                else:
                    inline_parts.append(self.inline(cc))
            text = _WS_RE.sub(" ", "".join(inline_parts)).strip()
            marker = f"{idx}." if ordered else "-"
            if text:
                lines.append("  " * depth + f"{marker} {text}")
            lines.extend(s for s in sub if s)
        return "\n".join(lines)

    def heading(self, node, level):
        text = self.inline_block(node)
        text = re.sub(r"[#¶§]+\s*$", "", text).strip()  # sphinx/mkdocs permalink glyphs
        if not text:
            return
        if text.lower().strip(":") in DROP_SECTIONS:
            self.drop_section_level = level
            return
        if self.drop_section_level and level <= self.drop_section_level:
            self.drop_section_level = 0
        if self.drop_section_level:
            return
        self.emit("#" * min(level, 6) + " " + text)

    def block(self, node):
        if isinstance(node, str):
            s = node.strip()
            if s and not self.drop_section_level:
                self.emit(_WS_RE.sub(" ", s))
            return
        t = node.tag
        if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heading(node, int(t[1]))
            return
        if self.drop_section_level:
            return
        if t == "p":
            txt = self.inline_block(node)
            if txt:
                self.emit(txt)
            return
        if t == "pre":
            txt = self.pre_text(node)
            if txt:
                fence = "````" if "```" in txt else "```"
                self.emit(f"{fence}{self.code_lang(node)}\n{txt}\n{fence}")
            return
        if t in ("ul", "ol"):
            txt = self.list_block(node, t == "ol")
            if txt:
                self.emit(txt)
            return
        if t == "dl":
            parts = []
            for c in node.children:
                if isinstance(c, str):
                    continue
                if c.tag == "dt":
                    txt = self.inline_block(c)
                    if txt:
                        parts.append(f"**{txt}**")
                elif c.tag == "dd":
                    saved, self.blocks = self.blocks, []
                    for cc in c.children:
                        self.block(cc)
                    dd = "\n\n".join(self.blocks)
                    self.blocks = saved
                    if dd:
                        parts.append(dd)
            if parts:
                self.emit("\n\n".join(parts))
            return
        if t == "table":
            txt = self.table(node)
            if txt:
                self.emit(txt)
            else:  # fall through: render cell contents as blocks
                for c in node.children:
                    self.block(c)
            return
        if t == "blockquote":
            saved, self.blocks = self.blocks, []
            for c in node.children:
                self.block(c)
            inner = "\n\n".join(self.blocks)
            self.blocks = saved
            if inner:
                self.emit("\n".join("> " + ln for ln in inner.splitlines()))
            return
        if t == "hr":
            return
        # transparent containers
        for c in node.children:
            self.block(c)


_MD_MAN_HEAD = re.compile(r"^#{2,3} +([A-Z][A-Z0-9 /()-]{2,40}?)(?: +top)? *$")
_MAN_DROP = {"COLOPHON", "REPORTING BUGS", "AVAILABILITY"}
_MAN_SUBHEAD = re.compile(r"^ {2,4}([A-Z][A-Za-z0-9 '/-]{4,60})$")


def unwrap_manpage(body: str) -> str:
    """A man page (man7.org et al.) renders as ## SECTION headings whose CONTENT sits in <pre>
    fences — prose trapped in code blocks. When the document is man-shaped (>=2 of NAME/
    SYNOPSIS/DESCRIPTION headings), unwrap every fence: drop the fence markers and the standard
    7-space man indent, promote 3-space Title-Case subsection lines to ###, drop boilerplate
    sections (COLOPHON...) and the top link-nav table. No-op for everything else."""
    heads = {m.group(1).strip() for ln in body.splitlines() if (m := _MD_MAN_HEAD.match(ln))}
    if len(heads & {"NAME", "SYNOPSIS", "DESCRIPTION"}) < 2:
        return body
    out = []
    dropping = False
    in_fence = False
    seen_section = False
    for ln in body.splitlines():
        m = _MD_MAN_HEAD.match(ln)
        if m and not in_fence:
            name = m.group(1).strip()
            seen_section = True
            dropping = name in _MAN_DROP
            if not dropping:
                out.extend(["", "## " + name, ""])
            continue
        if ln.startswith("```"):
            in_fence = not in_fence
            continue
        if dropping:
            continue
        if not seen_section and ln.startswith("|"):
            continue  # the NAME|SYNOPSIS|... link-nav table above the first section
        if in_fence:
            sub = _MAN_SUBHEAD.match(ln)
            if sub and not sub.group(1).rstrip().endswith("."):
                out.extend(["", "### " + sub.group(1).strip(), ""])
            else:
                out.append(ln[7:] if ln.startswith("       ") else ln)
        else:
            out.append(ln)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def normalize(html: str) -> tuple[str, str]:
    """Return (title, markdown_body)."""
    tb = TreeBuilder()
    try:
        tb.feed(html)
        tb.close()
    except Exception:
        pass  # render whatever was built before the parser choked
    root = _find_content_root(tb.root)
    _prune(root)
    r = Renderer()
    r.block(root)
    body = "\n\n".join(r.blocks)
    body = body.replace("\xa0", " ").replace("​", "")
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    body = unwrap_manpage(body)
    title = _WS_RE.sub(" ", tb.title.replace("\xa0", " ")).strip()
    # strip site suffixes: "json — Python 3.13 documentation" keeps the meaningful head
    for sep in (" — ", " | ", " - ", " – "):
        if sep in title and len(title.split(sep)[0]) >= 4:
            title = title.split(sep)[0].strip()
            break
    if not title:
        m = re.match(r"#\s+(.+)", body)
        title = m.group(1).strip() if m else "Untitled"
    return title, body


def split_markdown(body: str, max_bytes: int = 48_000) -> list[str]:
    """Split an oversized body at heading boundaries (## first, then #) into parts
    each <= ~max_bytes. Small remainders merge into the previous part."""
    if len(body.encode("utf-8", "replace")) <= max_bytes:
        return [body]
    for level in ("\n## ", "\n# ", "\n### "):
        chunks = body.split(level)
        if len(chunks) > 1:
            sections = [chunks[0]] + [level.lstrip("\n") + c for c in chunks[1:]]
            parts, cur, cur_len = [], [], 0
            for s in sections:
                sl = len(s.encode("utf-8", "replace"))
                if cur and cur_len + sl > max_bytes:
                    parts.append("\n\n".join(cur))
                    cur, cur_len = [], 0
                # an oversized single section gets hard-split by paragraphs
                while sl > max_bytes:
                    paras = s.split("\n\n")
                    half = len(paras) // 2 or 1
                    head, s = "\n\n".join(paras[:half]), "\n\n".join(paras[half:])
                    parts.append(head)
                    sl = len(s.encode("utf-8", "replace"))
                cur.append(s)
                cur_len += sl
            if cur:
                parts.append("\n\n".join(cur))
            return _coalesce([p.strip() for p in parts if p.strip()])
    # no headings at all: paragraph windows
    paras = body.split("\n\n")
    parts, cur, cur_len = [], [], 0
    for p in paras:
        pl = len(p.encode("utf-8", "replace")) + 2
        if cur and cur_len + pl > max_bytes:
            parts.append("\n\n".join(cur))
            cur, cur_len = [], 0
        cur.append(p)
        cur_len += pl
    if cur:
        parts.append("\n\n".join(cur))
    return _coalesce(parts)


def _coalesce(parts: list[str], min_bytes: int = 2000) -> list[str]:
    """No fragment parts: anything under min_bytes merges into a neighbor (a page's tiny
    pre-heading preamble would otherwise ship as a useless 300-byte file)."""
    out = []
    for p in parts:
        if out and (len(out[-1].encode()) < min_bytes or len(p.encode()) < min_bytes):
            out[-1] = out[-1] + "\n\n" + p
        else:
            out.append(p)
    return out
