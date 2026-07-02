---
title: "reStructuredText"
source: https://en.wikipedia.org/wiki/ReStructuredText
domain: restructuredtext
license: CC-BY-SA-4.0
tags: restructuredtext markup, docutils parser, lightweight markup, sphinx source
fetched: 2026-07-02
---

# reStructuredText

**reStructuredText** (**RST**, **ReST**, or **reST**) is a plain-text markup language primarily used for technical documentation and other textual data. It serves a role similar to that of Markdown but includes additional semantic features for more complex document structuring. Prominent, large-scale, open-source projects that rely on reStructuredText include the Python programming language community for its official documentation, the Linux kernel docs, CMake, and the LLVM compiler project.

It is part of the Docutils project of the Python Doc-SIG (Documentation Special Interest Group), aimed at creating a set of tools for Python similar to Javadoc for Java or Plain Old Documentation (POD) for Perl. Docutils can extract comments and information from Python programs, and format them into various forms of program documentation.

In this sense, reStructuredText is a lightweight markup language designed to be both processable by documentation-processing software such as Docutils, and be easily readable by human programmers who are reading and writing Python source code.

## History

reStructuredText evolved from an earlier lightweight markup language called StructuredText (developed by Zope). There were a number of problems with StructuredText, and reST was developed to address them. The name reStructuredText was chosen to indicate that reST is a "revised, reworked, and reinterpreted StructuredText."

Parts of the reST syntax were inspired by the Setext language from the early 1990s. Elements of the common RFC822 Internet Message Format and Javadoc formats were also considered for inclusion in the design.

reStructuredText was first released in June 2001. It began to see significant use in the Python community in 2002.

## Reference implementation

The reference implementation of the reST parser is a component of the Docutils text processing framework in the Python programming language, but other parsers are available.

The Docutils project has not registered any MIME type for reStructuredText nor designated any unregistered MIME type as official, but documents the MIME type `text/x-rst` as in *de facto* use by, for example, the build system for the Python website. The same MIME type is used in the freedesktop.org file type database used by desktop environments on Linux. Another MIME type, `text/prs.fallenstein.rst`, was registered as a vanity MIME type by a third party in 2003 to represent reStructuredText, and remains the only IANA-registered MIME type for reStructuredText, although it is not acknowledged as such by the Docutils project.

## Applications

reStructuredText is commonly used for technical documentation, for example, in documentation of Python libraries. However, it is suitable for a wide range of texts.

Since 2008, reST has been a core component of Python's Sphinx document generation system.

Trac also supports reStructuredText, as do GitHub and Bitbucket.

In 2011, Distributed Proofreaders, which prepared texts for Project Gutenberg, was considering adoption of reST as a basic format from which other ebook formats could be generated.

In July 2016 the Linux kernel project decided to transition from DocBook based documentation to reStructuredText and the Sphinx toolchain.

The software build tool CMake switched from a custom markup language to reStructuredText in version 3.0 for its documentation.

The JetBrains IDE ecosystem supports reStructuredText editing through plugins such as reStructuredText Pro, which provides RST and Sphinx documentation support including live preview and syntax highlighting.

## Examples

| Text using rST syntax | Corresponding HTML produced by an rST processor | Text viewed in a browser |
|---|---|---|
| ================ Document Heading ================ Heading ======= Sub-heading ----------- Paragraphs are separated by a blank line. | <h1>Document Heading</h1> <h2>Heading</h2> <h3>Sub-heading</h3> <p>Paragraphs are separated by a blank line.</p> | Document Heading Heading Sub-heading Paragraphs are separated by a blank line. |
| Text attributes *emphasis*, **strong emphasis**, ``monospace``. Horizontal rule: ---- | <p>Text attributes <em>emphasis</em>, <strong>strong emphasis</strong>, <code>monospace</code>.</p> <p>Horizontal rule:</p> <hr /> | Text attributes *emphasis*, **strong emphasis**, `monospace`. Horizontal rule: |
| Bullet list: * apples * oranges * pears Numbered list: 1. lather 2. rinse 3. repeat Nested lists: 1. fruits * apple * banana 2. vegetables * carrot * broccoli | <p>Bullet list:</p> <ul> <li>apples</li> <li>oranges</li> <li>pears</li> </ul> <p>Numbered list:</p> <ol> <li>lather</li> <li>rinse</li> <li>repeat</li> </ol> <p>Nested lists:</p> <ol> <li>fruits <ul> <li>apple</li> <li>banana</li> </ul> </li> <li>vegetables <ul> <li>carrot</li> <li>broccoli</li> </ul> </li> </ol> | Bullet list: apples oranges pears Numbered list: lather rinse repeat Nested lists: fruits apple banana vegetables carrot broccoli |
| An `example <http://example.com>`_. .. image:: Icon-pictures.png :alt: Image If text is indented, it is treated as a block quotation, and the final attribution line is handled automatically: Should array indices start at 0 or 1? My suggested compromise of 0.5 was rejected without, I thought, proper consideration. -- Stan Kelly-Bootle reST uses :: at the end of the paragraph prior to a pre-formatted code block:: Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x))) \| Multi-line text can \| span in tables \| with a pipe character. | <p>An <a href="http://example.com">example</a>.</p> <p><img alt="Image" src="Icon-pictures.png" /></p> <p>If text is indented, it is treated as a block quotation, and the final attribution line is handled automatically:</p> <blockquote> Should array indices start at 0 or 1? My suggested compromise of 0.5 was rejected without, I thought, proper consideration. -- Stan Kelly-Bootle</blockquote> <p>reST uses :: at the end of the paragraph prior to a pre-formatted code block:</p> <pre class="literal-block"> Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x))) </pre> <p>Multi-line text can<br/>span in tables<br/>with a pipe character.</p> | An example. (Image) If text is indented, it is treated as a block quotation, and the final attribution line is handled automatically: Should array indices start at 0 or 1? My suggested compromise of 0.5 was rejected without, I thought, proper consideration. -- Stan Kelly-Bootle reST uses :: at the end of the paragraph prior to a pre-formatted code block: Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x))) Multi-line text can span in tables with a pipe character. |
