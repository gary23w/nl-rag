---
title: "Pandoc"
source: https://en.wikipedia.org/wiki/Pandoc
domain: pandoc
license: CC-BY-SA-4.0
tags: pandoc converter, document conversion, markup converter, markdown to pdf
fetched: 2026-07-02
---

# Pandoc

**Pandoc** is a free-software document converter, widely used as a writing tool (especially by scholars) and as a basis for publishing workflows. It was created by John MacFarlane, a philosophy professor at the University of California, Berkeley.

## Functionality

Pandoc dubs itself a "markup format" converter. It can take a document in one of the supported formats and convert only its markup to another format. Maintaining the look and feel of the document is not a priority.

Plug-ins for custom formats can also be written in Lua, which has been used to create an exporting tool for the Journal Article Tag Suite, for example.

### CiteProc

An included CiteProc option allows pandoc to use bibliographic data from reference management software in any of five formats: BibTeX, BibLaTeX, CSL JSON or CSL YAML, or RIS. The information is automatically transformed into a citation in various styles (such as APA, Chicago, or MLA) using an implementation of the Citation Style Language. This allows the program to serve as a simpler alternative to LaTeX for producing academic writing in Markdown with inline citation keys. Or the program can be used to convert any bibliographic data stream in the accepted formats into a list of citations in a chosen style.

## Supported file formats

### Input formats

The input format with the most support is Pandoc's extended version of Markdown. Notwithstanding, pandoc can also read in the following formats:

- AsciiDoc
- Bibliography data formats: BibTeX, BibLaTeX, CSL JSON or CSL YAML, RIS, or EndNote XML
- Creole
- CSV and TSV tables
- DocBook
- EPUB
- FictionBook (FB2)
- Haddock
- HTML
- Jira wiki markup
- Journal Article Tag Suite (JATS) and Book Interchange Tag Set (BITS)
- JSON
- Jupyter Notebook
- LaTeX
- man (roff) and mdoc
- Markdown: Strict, CommonMark, Djot, GitHub Flavored Markdown (GFM), MultiMarkdown (MMD) and Markdown Extra (PHP Extra) variants
- OpenDocument (ODT)
- OPML
- Office Open XML: Microsoft Word variant
- Org-mode
- pod
- reStructuredText
- Rich Text Format (RTF)
- Textile
- txt2tags (t2t)
- Typst (typ)
- Wiki markup: MediaWiki, Muse, TikiWiki, TWiki and Vimwiki variants

### Output formats

Pandoc can create files in the following output formats, the set of which is not the same as the set of input formats:

- AsciiDoc
- Bibliography data formats: BibTeX, BibLaTeX, CSL JSON or CSL YAML
- ConTeXt
- DocBook: Versions 4 and 5
- EPUB: Versions 2 and 3
- FictionBook (FB2)
- Haddock
- HTML: HTML4 and HTML5 variants, respectively compliant with XHTML 1.0 Transitional and XHTML Strict
- InDesign ICML
- Jira wiki markup
- Journal Article Tag Suite (JATS)
- JSON
- Jupyter Notebook
- LaTeX
- man (roff)
- Markdown: Strict, CommonMark, Djot, GitHub Flavored Markdown (GFM), MultiMarkdown (MMD) and Markdown Extra (PHP Extra) variants
- OpenDocument (ODT/ODF) and OpenDocument XML
- OPML
- Office Open XML: Microsoft Word and Microsoft PowerPoint variants
- Org-mode
- PDF (needs a third-party add-on like ConTeXt, `pdfroff`, `wkhtmltopdf`, `weasyprint` or `prince`)
- Plain text
- reStructuredText
- Rich Text Format (RTF)
- TEI
- Texinfo
- Textile
- Typst (typ)
- Web-based slideshows: LaTeX Beamer, Slideous, Slidy, DZSlides, reveal.js and S5 variants
- Wiki markup: DokuWiki, MediaWiki, Muse, TikiWiki, TWiki and Vimwiki variants
