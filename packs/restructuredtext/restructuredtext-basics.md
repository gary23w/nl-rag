---
title: "reStructuredText Primer"
source: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
domain: restructuredtext
license: CC-BY-SA-4.0
tags: restructuredtext markup, docutils parser, lightweight markup, sphinx source
fetched: 2026-07-02
---

# reStructuredText Primer

reStructuredText is the default plaintext markup language used by Sphinx. This section is a brief introduction to reStructuredText (reST) concepts and syntax, intended to provide authors with enough information to author documents productively. Since reStructuredText was designed to be a simple, unobtrusive markup language, this will not take too long.

See also

The authoritative reStructuredText User Documentation. The “ref” links in this document link to the description of the individual constructs in the reStructuredText reference.

## Paragraphs

The paragraph (ref) is the most basic block in a reStructuredText document. Paragraphs are simply chunks of text separated by one or more blank lines. As in Python, indentation is significant in reStructuredText, so all lines of the same paragraph must be left-aligned to the same level of indentation.

## Inline markup

The standard reStructuredText inline markup is quite simple: use

- one asterisk: `*text*` for emphasis (italics),
- two asterisks: `**text**` for strong emphasis (boldface), and
- backquotes: ``text`` for code samples.

If asterisks or backquotes appear in running text and could be confused with inline markup delimiters, they have to be escaped with a backslash.

Be aware of some restrictions of this markup:

- it may not be nested,
- content may not start or end with whitespace: `* text*` is wrong,
- it must be separated from surrounding text by non-word characters. Use a backslash escaped space to work around that: `thisis\ *one*\ word`.

These restrictions may be lifted in future versions of the docutils.

It is also possible to replace or expand upon some of this inline markup with roles. Refer to Roles for more information.

## Lists and Quote-like blocks

List markup (ref) is natural: just place an asterisk at the start of a paragraph and indent properly. The same goes for numbered lists; they can also be autonumbered using a `#` sign:

```rst
* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.
```

Nested lists are possible, but be aware that they must be separated from the parent list items by blank lines:

```rst
* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues
```

Definition lists (ref) are created as follows:

```rst
term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.
```

Note that the term cannot have more than one line of text.

Quoted paragraphs (ref) are created by just indenting them more than the surrounding paragraphs.

Line blocks (ref) are a way of preserving line breaks:

```rst
| These lines are
| broken exactly like in
| the source file.
```

There are also several more special blocks available:

- field lists (ref, with caveats noted in Field Lists)
- option lists (ref)
- quoted literal blocks (ref)
- doctest blocks (ref)

## Literal blocks

Literal code blocks (ref) are introduced by ending a paragraph with the special marker `::`. The literal block must be indented (and, like all paragraphs, separated from the surrounding ones by blank lines):

```rst
This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.
```

The handling of the `::` marker is smart:

- If it occurs as a paragraph of its own, that paragraph is completely left out of the document.
- If it is preceded by whitespace, the marker is removed.
- If it is preceded by non-whitespace, the marker is replaced by a single colon.

That way, the second sentence in the above example’s first paragraph would be rendered as “The next paragraph is a code sample:”.

Code highlighting can be enabled for these literal blocks on a document-wide basis using the `highlight` directive and on a project-wide basis using the `highlight_language` configuration option. The `code-block` directive can be used to set highlighting on a block-by-block basis. These directives are discussed later.

## Doctest blocks

Doctest blocks (ref) are interactive Python sessions cut-and-pasted into docstrings. They do not require the literal blocks syntax. The doctest block must end with a blank line and should *not* end with an unused prompt:

```rst
>>> 1 + 1
2
```

## Tables

For *grid tables* (ref), you have to “paint” the cell grid yourself. They look like this:

```rst
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+
```

*Simple tables* (ref) are easier to write, but limited: they must contain more than one row, and the first column cells cannot contain multiple lines. They look like this:

```rst
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======
```

Two more syntaxes are supported: *CSV tables* and *List tables*. They use an *explicit markup block*. Refer to Tables for more information.

## Hyperlinks
