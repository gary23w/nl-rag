---
title: "AsciiDoc"
source: https://en.wikipedia.org/wiki/AsciiDoc
domain: asciidoc
license: CC-BY-SA-4.0
tags: asciidoc markup, lightweight markup, asciidoctor docs, text markup
fetched: 2026-07-02
---

# AsciiDoc

**AsciiDoc** is a human-readable document format, semantically equivalent to DocBook XML, but using plain text mark-up conventions. AsciiDoc documents can be created using any text editor and read "as-is", or rendered to HTML or any other format supported by a DocBook tool-chain, i.e., PDF, TeX, Unix manpages, e-books, slide presentations, etc. Common file extensions for AsciiDoc files are `adoc` and historically `txt` (as encouraged by AsciiDoc's creator).

The AsciiDoc format is being standardized by the Eclipse Foundation.

## History

### Early history

AsciiDoc was created in 2002 by Stuart Rackham, who published tools (*asciidoc* and *a2x*), written in the programming language Python to convert plain text, *human readable* files to commonly used published document formats.

Implementations also exist in Ruby (named *Asciidoctor*, released in 2013), the Java ecosystem via JRuby, the JavaScript ecosystem via Opal.js, and in Haskell and Go.

### Standardizing and primacy of Asciidoctor (2019–present)

Since the start of the technical standardizing process in 2019, the Asciidoctor project has aimed to produce an independent, compatible implementation of the AsciiDoc specification in the making, with the support of Stuart Rackham, the original author of the language. The official website of the AsciiDoc language has since begun linking to Asciidoctor's documentation of the language.

The start of the standardizing process in 2019 coincided with the release of Asciidoctor 2.0 and several parts of syntax being deprecated, such as single quotation marks (`'`) to indicate italics. Legacy syntax remains available through a compatibility mode.

The original Python implementation by Stuart Rackham continues to be developed, and named *AsciiDoc.py*. Since 2021, its documentation describes it as legacy, and formally targets the older rendition of the language.

## Notable applications

Most of the Git project documentation is written in AsciiDoc.

Some of O'Reilly Media's books and e-books are authored using AsciiDoc mark-up.

Red Hat's product documentation is written in AsciiDoc.

Asciidoctor is usable within GitHub and GitLab.

The JetBrains IDE ecosystem supports AsciiDoc editing through plugins such as AsciiDoc and AsciiDoc Pro, which provide AsciiDoc documentation support including live preview, syntax highlighting and PDF export.

## Example

The following shows text using AsciiDoc mark-up, and a rendering similar to that produced by an AsciiDoc processor:

| AsciiDoc source text |
|---|
| = My Article J. Smith https://wikipedia.org[Wikipedia] is an on-line encyclopedia, available in English and *many* other languages. == Software You can install _package-name_ by using the `gem` command: gem install package-name == Hardware Metals commonly used include: * copper * tin * lead |

| HTML-rendered result |
|---|
| My Article **J. Smith** Wikipedia is an on-line encyclopedia, available in English and **many** other languages. Software You can install *package-name* by using the `gem` command: gem install package-name Hardware Metals commonly used include: copper tin lead |

## Tools

- Antora – multi-repository documentation site generator for tech writers using git
- AsciiBinder – (deprecated) documentation system built on Asciidoctor for people who have many docs to maintain and republish regularly
- awestruct – static site generator inspired by Jekyll
- Asciidoc FX – AsciiDoc Book Editor based on JavaFX 18
- AsciiDocLIVE – free online AsciiDoc editor
- DAPS – DocBook Authoring and Publishing Suite (DAPS) is command-line software to publish DocBook & AsciiDoc as HTML, PDF, and EPUB
