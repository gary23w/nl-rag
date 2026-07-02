---
title: "Comparison of documentation generators"
source: https://en.wikipedia.org/wiki/Comparison_of_documentation_generators
domain: sphinx-docs
license: CC-BY-SA-4.0
tags: sphinx docs, documentation generator, restructuredtext source, read the docs
fetched: 2026-07-02
---

# Comparison of documentation generators

The following tables compare general and technical information for a number of documentation generators. Please see the individual products' articles for further information. Unless otherwise specified in footnotes, comparisons are based on the stable versions without any add-ons, extensions or external programs. Note that many of the generators listed are no longer maintained.

## General information

Basic general information about the generators, including: creator or company, license, and price.

| Name | Creator | Input format | Languages (alphabet order) | OS support | First public release date | Latest stable version | Software license |
|---|---|---|---|---|---|---|---|
| Ddoc | Walter Bright | Text | D | Windows, OS X, Linux and BSD | 2005/09/19 | DMD 2.078.3 | Boost (opensource) |
| docToolchain | Ralph D. Müller | Text | Java | Windows, OS X, Linux and BSD | 2018/08/31 | v3.4.2 | MIT license |
| Document! X | Innovasys | Text, Binary | C++/CLI only, C#, IDL, Java, VB, VBScript, PL/SQL | Windows only | 1998 | 2014.1 | Proprietary |
| Doxygen | Dimitri van Heesch | Text | C/C++, C#, D, IDL, Fortran, Java, PHP, Python | Any | 1997/10/26 | 1.16.1 | GPL |
| Epydoc | Edward Loper | Text | Python | Any | 2002/01/— | 3.0 (2008) | MIT |
| fpdoc (Free Pascal Documentation Generator) | Sebastian Guenther and Free Pascal Core | Text | (Object)Pascal/Delphi | FPC tier 1 targets | 2005 | 3.2.2 | GPL reusable parts are GPL with static linking exception |
| Haddock | Simon Marlow | Text | Haskell | Any | 2002 | 2.15.0 (2014) | BSD |
| HeaderDoc | Apple Inc. | Text | AppleScript, Bash, Csh, C, C++, Delphi, IDL, Java, JavaScript, MIG, Pascal, Perl, PHP, Python, Ruby, Tcl | Any Unix-like | 2000/09/— | 8.9.28 (2013) | APSL |
| Imagix 4D | Imagix Corp. | Text | C, C++, Java | Windows, Linux, Unix | 1995 | 7.3 | Proprietary |
| Javadoc | Sun Microsystems | Text | Java | Any | 1995 | 1.6 | GPL |
| JSDoc | Michael Mathews | Text | JavaScript | Any | 2024/10/19 | 4.0.4 | Apache |
| mkd | Jean-Paul Louyot | Text | Any with comments | Unix, Linux, Windows | 1989 | 2015 | EUPL GPL |
| MkDocs | Tom Christie | Text | Python | Any | 2014/10/29 | 1.5.3 | BSD |
| Natural Docs | Greg Valure | Text | Any with comments | Any | 2003/05/26 | 2.0.2 | GPL |
| NDoc | Jason Diamond, Jean-Claude Manoli, Kral Ferch | Binary | C# | Windows only | 2003/07/27 | 1.3.1 | GPL |
| pdoc | Andrew Gallant | Text | Python | Any | 2013 | 1.0.1 (2021) | Unlicense (PD) |
| perldoc | Larry Wall | Text | Perl | Any | 1994 | 5.16.3 | Artistic, GPL |
| phpDocumentor | Joshua Eichorn | Text | PHP | Any | 2000 | 3.0.0 | LGPL for 1.x, MIT for 2+ |
| pydoc | Ka-Ping Yee | Text | Python | Any | 2000 | in Python core | Python |
| RDoc | Dave Thomas | Text | C, C++, Ruby | Any | 2001/12/14 | in Ruby core | Ruby |
| ROBODoc | Frans Slothouber | Text | Any with comments | Any | 1995/01/19 | 4.99.36 (2015) | GPL |
| Sandcastle | Microsoft | Text | .NET | Windows only | 2008/05/— | 2.4.10520 (2016) | Ms-PL |
| Sphinx | Georg Brandl | Text | Ada, C, C++, Chapel, CMake, Fortran, GraphQL, JavaScript, Matlab, PHP, Python, reStructuredText, Ruby, Rust, VB | Any | 2008/03/21 | 8.2.1 | BSD |
| Visual Expert | Novalys | Text, Binary | C#, PL/SQL, Transact-SQL, PowerBuilder | Windows only | 1995 | 2017 | Proprietary |
| VSdocman | Helixoft | Text | VB, VBScript, C# | Windows only | 2003 Oct 2 | 9.0 | Proprietary |
| YARD | Loren Segal | Text | Ruby | Any | 2007/02/24 | 0.7.3 | MIT |
| Name | Creator | Input format | Languages (alphabet order) | OS support | First public release date | Latest stable version | Software license |

## Supported formats

The output formats the generators can write.

Generator name

HTML

CHM

RTF

PDF

LaTeX

PostScript

man pages

DocBook

XML

EPUB

Ddoc

Yes

Yes

No

Yes

Yes

Yes

Yes

No

Yes

No

docToolchain

Yes

No

No

Yes

No

No

No

Yes

No

Yes

Document! X

Yes

Yes

No

No

No

No

No

No

No

No

Epydoc

Yes

No

No

Yes

Indirectly

Indirectly

No

No

No

No

fpdoc

Yes

Native

Yes

Indirectly

Indirectly

Yes

No

No

No

No

Haddock

Yes

Yes

No

No

No

No

No

Partial

No

No

HeaderDoc

Yes

No

No

No

No

No

Yes

No

Yes

No

Imagix 4D

Yes

No

Yes

No

No

No

No

No

No

No

Javadoc

Yes

Indirectly

Indirectly

Indirectly

Indirectly

Indirectly

Indirectly

Indirectly

Indirectly

No

JSDoc

Yes

No

No

No

No

No

No

No

No

No

MkDocs

Yes

No

No

No

No

No

No

No

No

No

Natural Docs

Yes

No

No

No

No

No

No

No

No

No

NDoc

Yes

Yes

No

No

No

No

No

No

No

No

pdoc

Yes

No

No

No

No

No

No

No

No

No

phpDocumentor

Yes

Yes (1.x only)

No

Yes (1.x only)

No

No

No

Yes (1.x only)

Yes (1.x only)

No

pydoc

Yes

No

No

No

No

No

No

No

No

No

RDoc

Yes

Yes

No

No

No

No

Indirectly

No

Yes

No

ROBODoc

Yes

Indirectly

Yes

Indirectly

Yes

Indirectly

Yes

Yes

No

No

Sandcastle

Yes

Yes

No

No

No

No

No

No

No

No

Sphinx

Yes

Yes

No

Indirectly

Yes

No

Yes

No

Yes

Yes

Visual Expert

Yes

No

No

No

No

No

No

No

No

No

VSdocman

Yes

Yes

No

Yes

No

No

No

No

Yes

No

YARD

Yes

No

No

No

No

No

No

No

No

No

Generator name

HTML

CHM

RTF

PDF

LaTeX

PostScript

man pages

DocBook

XML

EPUB

## Other features

|   | possibility of extended customization | generated diagrams | highlighting and linking of generated doc | parameter types extracted |
|---|---|---|---|---|
| Ddoc | with macros |   |   |   |
| docToolchain | customizable themes, custom tasks | many diagram plugins (plantUML, mermaid, ...) | automatic and manual references, table of contents, bibliography, ... |   |
| Document! X | customizable HTML based templates, custom comment tags | linked graphical object relationship diagrams | internal links and links to .NET framework documentation | types extracted and linked |
| Doxygen | with XSLT | caller and callee graphs, dependency graphs, inheritance diagrams, collaboration diagrams |   |   |
| Epydoc |   |   |   |   |
| Haddock |   |   | Yes | Yes |
| HeaderDoc | Custom headers, footers, code coloring, and other CSS styles in individual pages. Project-wide TOC is generated from a user-defined template. |   | Configurable syntax highlighting/coloring with automatic linking to symbols in declaration, ability to manually link to symbols in discussion, etc. | Provides warnings if tagged parameters do not match code, parsed parameters included in XML output and Doxygen-style tagfile (-D flag in 8.7). Partial C preprocessor support with -p flag. Support for #if/#ifdef control over documentation inclusion using the -D and -U command-line flags. |
| Imagix 4D | customizable through style sheets and CSS | linked hierarchy and dependency graphs for function calls, variable sets and reads, class inheritance and interface, and file includes and interface, intra-function flow charts | fully cross-linked project-wide, including all hierarchy and dependency graphs, metrics tables, source code snippets, and source files | full semantic analysis of source code, including parameter types, conditional compilation directives, macro expansions |
| Javadoc |   |   |   |   |
| JSDoc |   |   |   | Yes |
| mkd | Customisable for all type of comments | 'as-is' in comments | all general documentation; references, manual, organigrams, ... Including the binary codes included in the comments. | all coded comments |
| MkDocs |   |   |   |   |
| Natural Docs |   |   |   |   |
| NDoc |   |   |   |   |
| perldoc | Extend the generator classes through Perl programming. |   | Only linking |   |
| pdoc | overridable Jinja2 templates |   | source code syntax highlighting, automatic cross-linking to symbol declarations | Yes |
| phpDocumentor | Smarty-based templates (1.x), Twig-based templates (2+) | class inheritance diagrams | cross reference to generated documentation, and to php.net function reference | Yes |
| pydoc |   |   |   |   |
| RDoc |   |   |   |   |
| ROBODoc |   |   |   |   |
| Sphinx | Customizable themes (10 first-party); Jinja templating; Python plugins | class inheritance diagrams, graphviz, third party (e.g. using aafigure, actdiag, Google Chart, gnuplot, mermaid) | Automatic cross-referencing (including between projects), Index; Table of Contents, Syntax highlighting with Pygments | custom objects (such as functions and classes) |
| Visual Expert | documentation content and styles customizable | Class inheritance, call trees, dependencies (impact analysis) | internal links between classes, methods, variables, tables, columns... | all types extracted |
| VSdocman | full customization for all output formats, templates for MSDN-like output, custom XML comment tags | linked graphical class diagrams, class inheritance tree | internal links and links to .NET framework documentation | types extracted and linked |
| YARD | customizable Ruby templates | class diagrams with extra tool | internal classes/modules cross-referenced and Ruby source highlighted |   |
