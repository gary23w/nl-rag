---
title: "Pandoc (part 3/4)"
source: https://pandoc.org/MANUAL.html
domain: pandoc
license: CC-BY-SA-4.0
tags: pandoc converter, document conversion, markup converter, markdown to pdf
fetched: 2026-07-02
part: 3/4
---

## Variables

### Language variables

**`lang`**

identifies the main language of the document using IETF language tags (following the

BCP 47

standard), such as

en

or

en-GB

. The

Language subtag lookup

tool can look up or verify these tags. This affects most formats, and controls hyphenation in PDF output when using LaTeX (through

babel

and

polyglossia

) or ConTeXt. Use native pandoc

Divs and Spans

with the

lang

attribute to switch the language:

```
---
lang: en-GB
...

Text in the main document language (British English).

::: {lang=fr-CA}
> Cette citation est écrite en français canadien.
:::

More text in English. ['Zitat auf Deutsch.']{lang=de}
```

**`dir`**

the base script direction, either

rtl

(right-to-left) or

ltr

(left-to-right). For bidirectional documents, native pandoc

span

s and

div

s with the

dir

attribute (value

rtl

or

ltr

) can be used to override the base direction in some output formats. This may not always be necessary if the final renderer (e.g. the browser, when generating HTML) supports the

Unicode Bidirectional Algorithm

. When using LaTeX for bidirectional documents, only the

xelatex

engine is fully supported (use

--pdf-engine=xelatex

).

### Variables for HTML

**`document-css`**

Enables inclusion of most of the

CSS

in the

styles.html

partial

(have a look with

pandoc --print-default-data-file=templates/styles.html

). Unless you use

--css

, this variable is set to

true

by default. You can disable it with e.g.

pandoc -M document-css=false

.

**`mainfont`**

sets the CSS

font-family

property on the

html

element.

**`fontsize`**

sets the base CSS

font-size

, which you’d usually set to e.g.

20px

, but it also accepts

pt

(12pt = 16px in most browsers).

**`fontcolor`**

sets the CSS

color

property on the

html

element.

**`linkcolor`**

sets the CSS

color

property on all links.

**`monofont`**

sets the CSS

font-family

property on

code

elements.

**`monobackgroundcolor`**

sets the CSS

background-color

property on

code

elements and adds extra padding.

**`linestretch`**

sets the CSS

line-height

property on the

html

element, which is preferred to be unitless.

**`maxwidth`**

sets the CSS

max-width

property (default is 36em).

**`backgroundcolor`**

sets the CSS

background-color

property on the

html

element.

**`margin-left`, `margin-right`, `margin-top`, `margin-bottom`**

sets the corresponding CSS

padding

properties on the

body

element.

To override or extend some CSS for just one document, include for example:

```
---
header-includes: |
  <style>
  blockquote {
    font-style: italic;
  }
  tr.even {
    background-color: #f0f0f0;
  }
  td, th {
    padding: 0.5em 2em 0.5em 0.5em;
  }
  tbody {
    border-bottom: none;
  }
  </style>
---
```

### Variables for HTML math

**`classoption`**

when using

--katex

, you can render display math equations flush left using

YAML metadata

or with

-M classoption=fleqn

.

### Variables for HTML slides

These affect HTML output when producing slide shows with pandoc.

**`institute`**

author affiliations: can be a list when there are multiple authors

**`revealjs-url`**

base URL for reveal.js documents (defaults to

https://unpkg.com/reveal.js@^5

)

**`s5-url`**

base URL for S5 documents (defaults to

s5/default

)

**`slidy-url`**

base URL for Slidy documents (defaults to

https://www.w3.org/Talks/Tools/Slidy2

)

**`slideous-url`**

base URL for Slideous documents (defaults to

slideous

)

**`title-slide-attributes`**

additional attributes for the title slide of reveal.js slide shows. See

background in reveal.js, beamer, and pptx

for an example.

**`highlightjs-theme`**

highlight.js theme for code highlighting when using

--syntax-highlighting=idiomatic

with reveal.js (defaults to

monokai

). See the

highlight.js demo page

for available themes.

All reveal.js configuration options are available as variables. To turn off boolean flags that default to true in reveal.js, use `0`.

### Variables for Beamer slides

These variables change the appearance of PDF slides using `beamer`.

**`aspectratio`**

slide aspect ratio (

43

for 4:3 [default],

169

for 16:9,

1610

for 16:10,

149

for 14:9,

141

for 1.41:1,

54

for 5:4,

32

for 3:2)

**`beameroption`**

add extra beamer option with

\setbeameroption{}

**`institute`**

author affiliations: can be a list when there are multiple authors

**`logo`**

logo image for slides

**`logooptions`**

options for logo image (e.g.,

width

,

height

)

**`navigation`**

controls navigation symbols (default is

empty

for no navigation symbols; other valid values are

frame

,

vertical

, and

horizontal

)

**`section-titles`**

enables “title pages” for new sections (default is true)

**`theme`, `colortheme`, `fonttheme`, `innertheme`, `outertheme`**

beamer themes

**`themeoptions`, `colorthemeoptions`, `fontthemeoptions`, `innerthemeoptions`, `outerthemeoptions`**

options for LaTeX beamer themes (lists)

**`titlegraphic`**

image for title slide: can be a list

**`titlegraphicoptions`**

options for title slide image (e.g.,

width

,

height

)

**`shorttitle`, `shortsubtitle`, `shortauthor`, `shortinstitute`, `shortdate`**

some beamer themes use short versions of the title, subtitle, author, institute, date

### Variables for PowerPoint

These variables control the visual aspects of a slide show that are not easily controlled via templates.

**`monofont`**

font to use for code.

### Variables for LaTeX

Pandoc uses these variables when creating a PDF with a LaTeX engine.

#### Layout

**`block-headings`**

make

\paragraph

and

\subparagraph

(fourth- and fifth-level headings, or fifth- and sixth-level with book classes) free-standing rather than run-in; requires further formatting to distinguish from

\subsubsection

(third- or fourth-level headings). Instead of using this option,

KOMA-Script

can adjust headings more extensively:

```
---
documentclass: scrartcl
header-includes: |
  \RedeclareSectionCommand[
    beforeskip=-10pt plus -2pt minus -1pt,
    afterskip=1sp plus -1sp minus 1sp,
    font=\normalfont\itshape]{paragraph}
  \RedeclareSectionCommand[
    beforeskip=-10pt plus -2pt minus -1pt,
    afterskip=1sp plus -1sp minus 1sp,
    font=\normalfont\scshape,
    indent=0pt]{subparagraph}
...
```

**`classoption`**

option for document class, e.g.

oneside

; repeat for multiple options:

```
---
classoption:
- twocolumn
- landscape
...
```

**`documentclass`**

document class: usually one of the standard classes,

article

,

book

, and

report

; the

KOMA-Script

equivalents,

scrartcl

,

scrbook

, and

scrreprt

, which default to smaller margins; or

memoir

**`geometry`**

option for

geometry

package, e.g.

margin=1in

; repeat for multiple options:

```
---
geometry:
- top=30mm
- left=20mm
- heightrounded
...
```

**`shorthands`**

Enable language-specific shorthands when loading

babel

. (By default, pandoc includes

shorthands=off

when loading

babel

, disabling language-specific shorthands.)

**`hyperrefoptions`**

option for

hyperref

package, e.g.

linktoc=all

; repeat for multiple options:

```
---
hyperrefoptions:
- linktoc=all
- pdfwindowui
- pdfpagemode=FullScreen
...
```

**`indent`**

if true, pandoc will use document class settings for indentation (the default LaTeX template otherwise removes indentation and adds space between paragraphs)

**`linestretch`**

adjusts line spacing using the

setspace

package, e.g.

1.25

,

1.5

**`margin-left`, `margin-right`, `margin-top`, `margin-bottom`**

sets margins if

geometry

is not used (otherwise

geometry

overrides these)

**`pagestyle`**

control

\pagestyle{}

: the default article class supports

plain

(default),

empty

(no running heads or page numbers), and

headings

(section titles in running heads)

**`papersize`**

paper size, e.g.

letter

,

a4

**`secnumdepth`**

numbering depth for sections (with

--number-sections

option or

numbersections

variable)

**`beamerarticle`**

produce an article from Beamer slides. Note: if you set this variable, you must specify the beamer writer but use the default

LaTeX

template: for example,

pandoc -Vbeamerarticle -t beamer --template default.latex

.

**`handout`**

produce a handout version of Beamer slides (with overlays condensed into single slides)

**`csquotes`**

load

csquotes

package and use

\enquote

or

\enquote*

for quoted text.

**`csquotesoptions`**

options to use for

csquotes

package (repeat for multiple options).

**`babeloptions`**

options to pass to the babel package (may be repeated for multiple options). This defaults to

provide=*

if the main language isn’t a European language written with Latin or Cyrillic script or Vietnamese. Most users will not need to adjust the default setting.

#### Fonts

**`fontenc`**

allows font encoding to be specified through

fontenc

package (with

pdflatex

); default is

T1

(see

LaTeX font encodings guide

)

**`fontfamily`**

font package for use with

pdflatex

:

TeX Live

includes many options, documented in the

LaTeX Font Catalogue

. The default is

Latin Modern

.

**`fontfamilyoptions`**

options for package used as

fontfamily

; repeat for multiple options. For example, to use the Libertine font with proportional lowercase (old-style) figures through the

libertinus

package:

```
---
fontfamily: libertinus
fontfamilyoptions:
- osf
- p
...
```

**`fontsize`**

font size for body text. The standard classes allow 10pt, 11pt, and 12pt. To use another size, set

documentclass

to one of the

KOMA-Script

classes, such as

scrartcl

or

scrbook

.

**`mainfont`, `sansfont`, `monofont`, `mathfont`, `CJKmainfont`, `CJKsansfont`, `CJKmonofont`**

font families for use with

xelatex

or

lualatex

: take the name of any system font, using the

fontspec

package.

CJKmainfont

uses the

xecjk

package if

xelatex

is used, or the

luatexja

package if

lualatex

is used.

**`mainfontoptions`, `sansfontoptions`, `monofontoptions`, `mathfontoptions`, `CJKoptions`, `luatexjapresetoptions`**

options to use with

mainfont

,

sansfont

,

monofont

,

mathfont

,

CJKmainfont

in

xelatex

and

lualatex

. Allow for any choices available through

fontspec

; repeat for multiple options. For example, to use the

TeX Gyre

version of Palatino with lowercase figures:

```
---
mainfont: TeX Gyre Pagella
mainfontoptions:
- Numbers=Lowercase
- Numbers=Proportional
...
```

**`mainfontfallback`, `sansfontfallback`, `monofontfallback`**

fonts to try if a glyph isn’t found in

mainfont

,

sansfont

, or

monofont

respectively. These are lists. The font name must be followed by a colon and optionally a set of options, for example:

```
---
mainfontfallback:
  - "FreeSans:"
  - "NotoColorEmoji:mode=harf"
...
```

Font fallbacks currently only work with

lualatex

.

**`babelfonts`**

a map of Babel language names (e.g.

chinese

) to the font to be used with the language:

```
---
babelfonts:
  chinese-hant: "Noto Serif CJK TC"
  russian: "Noto Serif"
...
```

**`microtypeoptions`**

options to pass to the microtype package

#### Links

**`colorlinks`**

add color to link text; automatically enabled if any of

linkcolor

,

filecolor

,

citecolor

,

urlcolor

, or

toccolor

are set

**`boxlinks`**

add visible box around links (has no effect if

colorlinks

is set)

**`linkcolor`, `filecolor`, `citecolor`, `urlcolor`, `toccolor`**

color for internal links, external links, citation links, linked URLs, and links in table of contents, respectively: uses options allowed by

xcolor

, including the

dvipsnames

,

svgnames

, and

x11names

lists

**`links-as-notes`**

causes links to be printed as footnotes

**`urlstyle`**

style for URLs (e.g.,

tt

,

rm

,

sf

, and, the default,

same

)

#### Front matter

**`lof`, `lot`**

include list of figures, list of tables (can also be set using

--lof/--list-of-figures

,

--lot/--list-of-tables

)

**`thanks`**

contents of acknowledgments footnote after document title

**`toc`**

include table of contents (can also be set using

--toc/--table-of-contents

)

**`toc-depth`**

level of section to include in table of contents

#### BibLaTeX Bibliographies

These variables function when using BibLaTeX for citation rendering.

**`biblatexoptions`**

list of options for biblatex

**`biblio-style`**

bibliography style, when used with

--natbib

and

--biblatex

**`biblio-title`**

bibliography title, when used with

--natbib

and

--biblatex

**`bibliography`**

bibliography to use for resolving references

**`natbiboptions`**

list of options for natbib

#### Other

**`pdf-trailer-id`**

the PDF trailer ID; must be two PDF byte strings if set, conventionally with 16 bytes each. E.g.,

<00112233445566778899aabbccddeeff> <00112233445566778899aabbccddeeff>

. See the section on

reproducible builds

.

**`pdfstandard`**

PDF standard(s) for the document, e.g.

ua-2

,

a-4f

. Supports PDF/A, PDF/X, and PDF/UA variants. Requires LuaLaTeX and LaTeX 2023+. Repeat for multiple standards:

```
---
pdfstandard:
- ua-2
- a-4f
...
```

### Variables for ConTeXt

Pandoc uses these variables when creating a PDF with ConTeXt.

**`fontsize`**

font size for body text (e.g.

10pt

,

12pt

)

**`headertext`, `footertext`**

text to be placed in running header or footer (see

ConTeXt Headers and Footers

); repeat up to four times for different placement

**`indenting`**

controls indentation of paragraphs, e.g.

yes,small,next

(see

ConTeXt Indentation

); repeat for multiple options

**`interlinespace`**

adjusts line spacing, e.g.

4ex

(using

setupinterlinespace

); repeat for multiple options

**`layout`**

options for page margins and text arrangement (see

ConTeXt Layout

); repeat for multiple options

**`linkcolor`, `contrastcolor`**

color for links outside and inside a page, e.g.

red

,

blue

(see

ConTeXt Color

)

**`linkstyle`**

typeface style for links, e.g.

normal

,

bold

,

slanted

,

boldslanted

,

type

,

cap

,

small

**`lof`, `lot`**

include list of figures, list of tables

**`mainfont`, `sansfont`, `monofont`, `mathfont`**

font families: take the name of any system font (see

ConTeXt Font Switching

)

**`mainfontfallback`, `sansfontfallback`, `monofontfallback`**

list of fonts to try, in order, if a glyph is not found in the main font. Use

\definefallbackfamily

-compatible font name syntax. Emoji fonts are unsupported.

**`margin-left`, `margin-right`, `margin-top`, `margin-bottom`**

sets margins, if

layout

is not used (otherwise

layout

overrides these)

**`pagenumbering`**

page number style and location (using

setuppagenumbering

); repeat for multiple options

**`papersize`**

paper size, e.g.

letter

,

A4

,

landscape

(see

ConTeXt Paper Setup

); repeat for multiple options

**`pdfa`**

adds to the preamble the setup necessary to generate PDF/A of the type specified, e.g.

1a:2005

,

2a

. If no type is specified (i.e. the value is set to True, by e.g.

--metadata=pdfa

or

pdfa: true

in a YAML metadata block),

1b:2005

will be used as default, for reasons of backwards compatibility. Using

--variable=pdfa

without specified value is not supported. To successfully generate PDF/A the required ICC color profiles have to be available and the content and all included files (such as images) have to be standard-conforming. The ICC profiles and output intent may be specified using the variables

pdfaiccprofile

and

pdfaintent

. See also

ConTeXt PDFA

for more details.

**`pdfaiccprofile`**

when used in conjunction with

pdfa

, specifies the ICC profile to use in the PDF, e.g.

default.cmyk

. If left unspecified,

sRGB.icc

is used as default. May be repeated to include multiple profiles. Note that the profiles have to be available on the system. They can be obtained from

ConTeXt ICC Profiles

.

**`pdfaintent`**

when used in conjunction with

pdfa

, specifies the output intent for the colors, e.g.

ISO coated v2 300\letterpercent\space (ECI)

If left unspecified,

sRGB IEC61966-2.1

is used as default.

**`toc`**

include table of contents (can also be set using

--toc/--table-of-contents

)

**`urlstyle`**

typeface style for links without link text, e.g.

normal

,

bold

,

slanted

,

boldslanted

,

type

,

cap

,

small

**`whitespace`**

spacing between paragraphs, e.g.

none

,

small

(using

setupwhitespace

)

**`includesource`**

include all source documents as file attachments in the PDF file

### Variables for `wkhtmltopdf`

Pandoc uses these variables when creating a PDF with `wkhtmltopdf`. The `--css` option also affects the output.

**`footer-html`, `header-html`**

add information to the header and footer

**`margin-left`, `margin-right`, `margin-top`, `margin-bottom`**

set the page margins

**`papersize`**

sets the PDF paper size

### Variables for man pages

**`adjusting`**

adjusts text to left (

l

), right (

r

), center (

c

), or both (

b

) margins

**`footer`**

footer in man pages

**`header`**

header in man pages

**`section`**

section number in man pages

### Variables for Texinfo

**`version`**

version of software (used in title and title page)

**`filename`**

name of info file to be generated (defaults to a name based on the texi filename)

### Variables for Typst

**`template`**

Typst template to use (relative path only).

**`margin`**

A dictionary with the fields defined in the Typst documentation:

x

,

y

,

top

,

bottom

,

left

,

right

.

**`papersize`**

Paper size:

a4

,

us-letter

, etc.

**`mainfont`**

Name of system font to use for the main font.

**`fontsize`**

Font size (e.g.,

12pt

).

**`section-numbering`**

Schema to use for numbering sections, e.g.

1.A.1

.

**`page-numbering`**

Schema to use for numbering pages, e.g.

1

or

i

, or an empty string to omit page numbering.

**`columns`**

Number of columns for body text.

**`thanks`**

contents of acknowledgments footnote after document title

**`mathfont`, `codefont`**

Name of system font to use for math and code, respectively.

**`linestretch`**

adjusts line spacing, e.g.

1.25

,

1.5

**`linkcolor`, `filecolor`, `citecolor`**

color for external links, internal links, and citation links, respectively: expects a hexadecimal color code

### Variables for ms

**`fontfamily`**

A

(Avant Garde),

B

(Bookman),

C

(Helvetica),

HN

(Helvetica Narrow),

P

(Palatino), or

T

(Times New Roman). This setting does not affect source code, which is always displayed using monospace Courier. These built-in fonts are limited in their coverage of characters. Additional fonts may be installed using the script

install-font.sh

provided by Peter Schaffter and documented in detail on

his web site

.

**`indent`**

paragraph indent (e.g.

2m

)

**`lineheight`**

line height (e.g.

12p

)

**`pointsize`**

point size (e.g.

10p

)

### Variables set automatically

Pandoc sets these variables automatically in response to options or document contents; users can also modify them. These vary depending on the output format, and include the following:

**`body`**

body of document

**`date-meta`**

the

date

variable converted to ISO 8601 YYYY-MM-DD, included in all HTML based formats (dzslides, epub, html, html4, html5, revealjs, s5, slideous, slidy). The recognized formats for

date

are:

mm/dd/yyyy

,

mm/dd/yy

,

yyyy-mm-dd

(ISO 8601),

dd MM yyyy

(e.g. either

02 Apr 2018

or

02 April 2018

),

MM dd, yyyy

(e.g.

Apr. 02, 2018

or

April 02, 2018),

yyyy[mm[dd]]

(e.g.

20180402,

201804

or

2018

).

**`header-includes`**

contents specified by

-H/--include-in-header

(may have multiple values)

**`include-before`**

contents specified by

-B/--include-before-body

(may have multiple values)

**`include-after`**

contents specified by

-A/--include-after-body

(may have multiple values)

**`meta-json`**

JSON representation of all of the document’s metadata. Field values are transformed to the selected output format.

**`numbersections`**

non-null value if

-N/--number-sections

was specified

**`sourcefile`, `outputfile`**

source and destination filenames, as given on the command line.

sourcefile

can also be a list if input comes from multiple files, or empty if input is from stdin. You can use the following snippet in your template to distinguish them:

```
$if(sourcefile)$
$for(sourcefile)$
$sourcefile$
$endfor$
$else$
(stdin)
$endif$
```

Similarly,

outputfile

can be

-

if output goes to the terminal. If you need absolute paths, use e.g.

$curdir$/$sourcefile$

.

**`pdf-engine`**

name of PDF engine if provided using

--pdf-engine

, or the default engine for the format if PDF output is requested.

**`curdir`**

working directory from which pandoc is run.

**`pandoc-version`**

pandoc version.

**`toc`**

non-null value if

--toc/--table-of-contents

was specified

**`toc-title`**

title of table of contents (works only with EPUB, HTML, revealjs, opendocument, odt, docx, pptx, beamer, LaTeX). Note that in docx and pptx a custom

toc-title

will be picked up from metadata, but cannot be set as a variable.

# Extensions

The behavior of some of the readers and writers can be adjusted by enabling or disabling various extensions.

An extension can be enabled by adding `+EXTENSION` to the format name and disabled by adding `-EXTENSION`. For example, `--from markdown_strict+footnotes` is strict Markdown with footnotes enabled, while `--from markdown-footnotes-pipe_tables` is pandoc’s Markdown without footnotes or pipe tables.

The Markdown reader and writer make by far the most use of extensions. Extensions only used by them are therefore covered in the section Pandoc’s Markdown below (see Markdown variants for `commonmark` and `gfm`). In the following, extensions that also work for other formats are covered.

Note that Markdown extensions added to the `ipynb` format affect Markdown cells in Jupyter notebooks (as do command-line options like `--markdown-headings`).


## Typography

### Extension: `smart` ±

Interpret straight quotes as curly quotes, `---` as em-dashes, `--` as en-dashes, and `...` as ellipses. Nonbreaking spaces are inserted after certain abbreviations, such as “Mr.”

This extension can be enabled/disabled for the following formats:

**input formats**

markdown

,

commonmark

,

latex

,

mediawiki

,

org

,

rst

,

twiki

,

html

**output formats**

markdown

,

latex

,

context

,

org

,

rst

**enabled by default in**

markdown

,

latex

,

context

(both input and output)

Note: If you are *writing* Markdown, then the `smart` extension has the reverse effect: what would have been curly quotes comes out straight.

In LaTeX, `smart` means to use the standard TeX ligatures for quotation marks (`` and `''` for double quotes, ` and `'` for single quotes) and dashes (`--` for en-dash and `---` for em-dash). If `smart` is disabled, then in reading LaTeX pandoc will parse these characters literally. In writing LaTeX, enabling `smart` tells pandoc to use the ligatures when possible; if `smart` is disabled pandoc will use unicode quotation mark and dash characters.


## Headings and sections

### Extension: `auto_identifiers` ±

A heading without an explicitly specified identifier will be automatically assigned a unique identifier based on the heading text.

This extension can be enabled/disabled for the following formats:

**input formats**

markdown

,

latex

,

rst

,

mediawiki

,

textile

,

man

**output formats**

markdown

,

muse

**enabled by default in**

markdown

,

muse

,

man

The default algorithm used to derive the identifier from the heading text is:

- Remove all formatting, links, etc.
- Remove all footnotes.
- Remove all non-alphanumeric characters, except underscores, hyphens, and periods.
- Replace all spaces and newlines with hyphens.
- Convert all alphabetic characters to lowercase.
- Remove everything up to the first letter (identifiers may not begin with a number or punctuation mark).
- If nothing is left after this, use the identifier `section`.

Thus, for example,

| Heading | Identifier |
|---|---|
| `Heading identifiers in HTML` | `heading-identifiers-in-html` |
| `Maître d'hôtel` | `maître-dhôtel` |
| `*Dogs*?--in *my* house?` | `dogs--in-my-house` |
| `[HTML], [S5], or [RTF]?` | `html-s5-or-rtf` |
| `3. Applications` | `applications` |
| `33` | `section` |

These rules should, in most cases, allow one to determine the identifier from the heading text. The exception is when several headings have the same text; in this case, the first will get an identifier as described above; the second will get the same identifier with `-1` appended; the third with `-2`; and so on.

(However, a different algorithm is used if `gfm_auto_identifiers` is enabled; see below.)

These identifiers are used to provide link targets in the table of contents generated by the `--toc|--table-of-contents` option. They also make it easy to provide links from one section of a document to another. A link to this section, for example, might look like this:

```
See the section on
[heading identifiers](#heading-identifiers-in-html-latex-and-context).
```

Note, however, that this method of providing links to sections works only in HTML, LaTeX, and ConTeXt formats.

If the `--section-divs` option is specified, then each section will be wrapped in a `section` (or a `div`, if `html4` was specified), and the identifier will be attached to the enclosing `<section>` (or `<div>`) tag rather than the heading itself. This allows entire sections to be manipulated using JavaScript or treated differently in CSS.

### Extension: `ascii_identifiers` ±

Causes the identifiers produced by `auto_identifiers` to be pure ASCII. Accents are stripped off of accented Latin letters, and non-Latin letters are omitted.

### Extension: `gfm_auto_identifiers` ±

Changes the algorithm used by `auto_identifiers` to conform to GitHub’s method. Spaces are converted to dashes (`-`), uppercase characters to lowercase characters, and punctuation characters other than `-` and `_` are removed. Emojis are replaced by their names.


## Math Input

The extensions `tex_math_dollars`, `tex_math_gfm`, `tex_math_single_backslash`, and `tex_math_double_backslash` are described in the section about Pandoc’s Markdown.

However, they can also be used with HTML input. This is handy for reading web pages formatted using MathJax, for example.


## Raw HTML/TeX

The following extensions are described in more detail in their respective sections of Pandoc’s Markdown:

- `raw_html` allows HTML elements which are not representable in pandoc’s AST to be parsed as raw HTML. By default, this is disabled for HTML input.
- `raw_tex` allows raw LaTeX, TeX, and ConTeXt to be included in a document. This extension can be enabled/disabled for the following formats (in addition to `markdown`): input formats `latex`, `textile`, `html` (environments, `\ref`, and `\eqref` only), `ipynb` output formats `textile`, `commonmark` Note: as applied to `ipynb`, `raw_html` and `raw_tex` affect not only raw TeX in Markdown cells, but data with mime type `text/html` in output cells. Since the `ipynb` reader attempts to preserve the richest possible outputs when several options are given, you will get best results if you disable `raw_html` and `raw_tex` when converting to formats like `docx` which don’t allow raw `html` or `tex`.
- `native_divs` causes HTML `div` elements to be parsed as native pandoc Div blocks. If you want them to be parsed as raw HTML, use `-f html-native_divs+raw_html`.
- `native_spans` causes HTML `span` elements to be parsed as native pandoc Span inlines. If you want them to be parsed as raw HTML, use `-f html-native_spans+raw_html`. If you want to drop all `div`s and `span`s when converting HTML to Markdown, you can use `pandoc -f html-native_divs-native_spans -t markdown`.


## Literate Haskell support

### Extension: `literate_haskell` ±

Treat the document as literate Haskell source.

This extension can be enabled/disabled for the following formats:

**input formats**

markdown

,

rst

,

latex

**output formats**

markdown

,

rst

,

latex

,

html

If you append `+lhs` (or `+literate_haskell`) to one of the formats above, pandoc will treat the document as literate Haskell source. This means that

- In Markdown input, “bird track” sections will be parsed as Haskell code rather than block quotations. Text between `\begin{code}` and `\end{code}` will also be treated as Haskell code. For ATX-style headings the character ‘=’ will be used instead of ‘#’.
- In Markdown output, code blocks with classes `haskell` and `literate` will be rendered using bird tracks, and block quotations will be indented one space, so they will not be treated as Haskell code. In addition, headings will be rendered setext-style (with underlines) rather than ATX-style (with ‘#’ characters). (This is because ghc treats ‘#’ characters in column 1 as introducing line numbers.)
- In restructured text input, “bird track” sections will be parsed as Haskell code.
- In restructured text output, code blocks with class `haskell` will be rendered using bird tracks.
- In LaTeX input, text in `code` environments will be parsed as Haskell code.
- In LaTeX output, code blocks with class `haskell` will be rendered inside `code` environments.
- In HTML output, code blocks with class `haskell` will be rendered with class `literatehaskell` and bird tracks.

Examples:

```
pandoc -f markdown+lhs -t html
```

reads literate Haskell source formatted with Markdown conventions and writes ordinary HTML (without bird tracks).

```
pandoc -f markdown+lhs -t html+lhs
```

writes HTML with the Haskell code in bird tracks, so it can be copied and pasted as literate Haskell source.

Note that GHC expects the bird tracks in the first column, so indented literate code blocks (e.g. inside an itemized environment) will not be picked up by the Haskell compiler.


## Other extensions

### Extension: `empty_paragraphs` ±

Allows empty paragraphs. By default empty paragraphs are omitted.

This extension can be enabled/disabled for the following formats:

**input formats**

docx

,

html

**output formats**

docx

,

odt

,

opendocument

,

html

,

latex

### Extension: `native_numbering` ±

Enables native numbering of figures and tables. Enumeration starts at 1.

This extension can be enabled/disabled for the following formats:

**output formats**

odt

,

opendocument

,

docx

### Extension: `xrefs_name` ±

Links to headings, figures and tables inside the document are substituted with cross-references that will use the name or caption of the referenced item. The original link text is replaced once the generated document is refreshed. This extension can be combined with `xrefs_number` in which case numbers will appear before the name.

Text in cross-references is only made consistent with the referenced item once the document has been refreshed.

This extension can be enabled/disabled for the following formats:

**output formats**

odt

,

opendocument

### Extension: `xrefs_number` ±

Links to headings, figures and tables inside the document are substituted with cross-references that will use the number of the referenced item. The original link text is discarded. This extension can be combined with `xrefs_name` in which case the name or caption numbers will appear after the number.

For the `xrefs_number` to be useful heading numbers must be enabled in the generated document, also table and figure captions must be enabled using for example the `native_numbering` extension.

Numbers in cross-references are only visible in the final document once it has been refreshed.

This extension can be enabled/disabled for the following formats:

**output formats**

odt

,

opendocument

### Extension: `styles` ±

When converting from docx, add `custom-styles` attributes for all docx styles, regardless of whether pandoc understands the meanings of these styles. Because attributes cannot be added directly to paragraphs or text in the pandoc AST, paragraph styles will cause Divs to be created and character styles will cause Spans to be created to hold the attributes. (Table styles will be added to the Table elements directly.) This extension can be used with docx custom styles.

**input formats**

docx

### Extension: `amuse` ±

In the `muse` input format, this enables Text::Amuse extensions to Emacs Muse markup.

### Extension: `raw_markdown` ±

In the `ipynb` input format, this causes Markdown cells to be included as raw Markdown blocks (allowing lossless round-tripping) rather than being parsed. Use this only when you are targeting `ipynb` or a Markdown-based output format.

### Extension: `citations` (typst) ±

When the `citations` extension is enabled in `typst` (as it is by default), `typst` citations will be parsed as native pandoc citations, and native pandoc citations will be rendered as `typst` citations.

### Extension: `citations` (org) ±

When the `citations` extension is enabled in `org`, org-cite and org-ref style citations will be parsed as native pandoc citations, and org-cite citations will be used to render native pandoc citations.

### Extension: `citations` (docx) ±

When `citations` is enabled in `docx`, citations inserted by Zotero or Mendeley or EndNote plugins will be parsed as native pandoc citations. (Otherwise, the formatted citations generated by the bibliographic software will be parsed as regular text.)

### Extension: `fancy_lists` (org) ±

Some aspects of Pandoc’s Markdown fancy lists are also accepted in `org` input, mimicking the option `org-list-allow-alphabetical` in Emacs. As in Org Mode, enabling this extension allows lowercase and uppercase alphabetical markers for ordered lists to be parsed in addition to arabic ones. Note that for Org, this does not include roman numerals or the `#` placeholder that are enabled by the extension in Pandoc’s Markdown.

### Extension: `element_citations` ±

In the `jats` output formats, this causes reference items to be replaced with `<element-citation>` elements. These elements are not influenced by CSL styles, but all information on the item is included in tags.

### Extension: `ntb` ±

In the `context` output format this enables the use of Natural Tables (TABLE) instead of the default Extreme Tables (xtables). Natural tables allow more fine-grained global customization but come at a performance penalty compared to extreme tables.

### Extension: `smart_quotes` (org) ±

Interpret straight quotes as curly quotes during parsing. When *writing* Org, then the `smart_quotes` extension has the reverse effect: what would have been curly quotes comes out straight.

This extension is implied if `smart` is enabled.

### Extension: `special_strings` (org) ±

Interpret `---` as em-dashes, `--` as en-dashes, `\-` as shy hyphen, and `...` as ellipses.

This extension is implied if `smart` is enabled.

### Extension: `tagging` ±

Enabling this extension with `context` output will produce markup suitable for the production of tagged PDFs. This includes additional markers for paragraphs and alternative markup for emphasized text. The `emphasis-command` template variable is set if the extension is enabled.

# Pandoc’s Markdown

Pandoc understands an extended and slightly revised version of John Gruber’s Markdown syntax. This document explains the syntax, noting differences from original Markdown. Except where noted, these differences can be suppressed by using the `markdown_strict` format instead of `markdown`. Extensions can be enabled or disabled to specify the behavior more granularly. They are described in the following. See also Extensions above, for extensions that work also on other formats.


## Philosophy

Markdown is designed to be easy to write, and, even more importantly, easy to read:

> A Markdown-formatted document should be publishable as-is, as plain text, without looking like it’s been marked up with tags or formatting instructions. – John Gruber

This principle has guided pandoc’s decisions in finding syntax for tables, footnotes, and other extensions.

There is, however, one respect in which pandoc’s aims are different from the original aims of Markdown. Whereas Markdown was originally designed with HTML generation in mind, pandoc is designed for multiple output formats. Thus, while pandoc allows the embedding of raw HTML, it discourages it, and provides other, non-HTMLish ways of representing important document elements like definition lists, tables, mathematics, and footnotes.


## Paragraphs

A paragraph is one or more lines of text followed by one or more blank lines. Newlines are treated as spaces, so you can reflow your paragraphs as you like. If you need a hard line break, put two or more spaces at the end of a line.

### Extension: `escaped_line_breaks` ±

A backslash followed by a newline is also a hard line break. Note: in multiline and grid table cells, this is the only way to create a hard line break, since trailing spaces in the cells are ignored.


## Headings

There are two kinds of headings: Setext and ATX.

### Setext-style headings

A setext-style heading is a line of text “underlined” with a row of `=` signs (for a level-one heading) or `-` signs (for a level-two heading):

```
A level-one heading
===================

A level-two heading
-------------------
```

The heading text can contain inline formatting, such as emphasis (see Inline formatting, below).

### ATX-style headings

An ATX-style heading consists of one to six `#` signs and a line of text, optionally followed by any number of `#` signs. The number of `#` signs at the beginning of the line is the heading level:

```

## A level-two heading

### A level-three heading ###
```

As with setext-style headings, the heading text can contain formatting:

```
# A level-one heading with a [link](/url) and *emphasis*
```

### Extension: `blank_before_header` ±

Original Markdown syntax does not require a blank line before a heading. Pandoc does require this (except, of course, at the beginning of the document). The reason for the requirement is that it is all too easy for a `#` to end up at the beginning of a line by accident (perhaps through line wrapping). Consider, for example:

```
I like several of their flavors of ice cream:
#22, for example, and #5.
```

### Extension: `space_in_atx_header` ±

Many Markdown implementations do not require a space between the opening `#`s of an ATX heading and the heading text, so that `#5 bolt` and `#hashtag` count as headings. With this extension, pandoc does require the space.

### Heading identifiers

See also the `auto_identifiers` extension above.

### Extension: `header_attributes` ±

Headings can be assigned attributes using this syntax at the end of the line containing the heading text:

```
{#identifier .class .class key=value key=value}
```

Thus, for example, the following headings will all be assigned the identifier `foo`:

```
# My heading {#foo}


## My heading ##    {#foo}

My other heading   {#foo}
---------------
```

(This syntax is compatible with PHP Markdown Extra.)

Note that although this syntax allows assignment of classes and key/value attributes, writers generally don’t use all of this information. Identifiers, classes, and key/value attributes are used in HTML and HTML-based formats such as EPUB and slidy. Identifiers are used for labels and link anchors in the LaTeX, ConTeXt, Textile, Jira markup, and AsciiDoc writers.

Headings with the class `unnumbered` will not be numbered, even if `--number-sections` is specified. A single hyphen (`-`) in an attribute context is equivalent to `.unnumbered`, and preferable in non-English documents. So,

```
# My heading {-}
```

is just the same as

```
# My heading {.unnumbered}
```

If the `unlisted` class is present in addition to `unnumbered`, the heading will not be included in a table of contents. (Currently this feature is only implemented for certain formats: those based on LaTeX and HTML, PowerPoint, and RTF.)

### Extension: `implicit_header_references` ±

Pandoc behaves as if reference links have been defined for each heading. So, to link to a heading

```
# Heading identifiers in HTML
```

you can simply write

```
[Heading identifiers in HTML]
```

or

```
[Heading identifiers in HTML][]
```

or

```
[the section on heading identifiers][heading identifiers in
HTML]
```

instead of giving the identifier explicitly:

```
[Heading identifiers in HTML](#heading-identifiers-in-html)
```

If there are multiple headings with identical text, the corresponding reference will link to the first one only, and you will need to use explicit links to link to the others, as described above.

Like regular reference links, these references are case-insensitive.

Explicit link reference definitions always take priority over implicit heading references. So, in the following example, the link will point to `bar`, not to `#foo`:

```
# Foo

[foo]: bar

See [foo]
```


## Block quotations

Markdown uses email conventions for quoting blocks of text. A block quotation is one or more paragraphs or other block elements (such as lists or headings), with each line preceded by a `>` character and an optional space. (The `>` need not start at the left margin, but it should not be indented more than three spaces.)

```
> This is a block quote. This
> paragraph has two lines.
>
> 1. This is a list inside a block quote.
> 2. Second item.
```

A “lazy” form, which requires the `>` character only on the first line of each block, is also allowed:

```
> This is a block quote. This
paragraph has two lines.

> 1. This is a list inside a block quote.
2. Second item.
```

Among the block elements that can be contained in a block quote are other block quotes. That is, block quotes can be nested:

```
> This is a block quote.
>
> > A block quote within a block quote.
```

If the `>` character is followed by an optional space, that space will be considered part of the block quote marker and not part of the indentation of the contents. Thus, to put an indented code block in a block quote, you need five spaces after the `>`:

```
>     code
```

### Extension: `blank_before_blockquote` ±

Original Markdown syntax does not require a blank line before a block quote. Pandoc does require this (except, of course, at the beginning of the document). The reason for the requirement is that it is all too easy for a `>` to end up at the beginning of a line by accident (perhaps through line wrapping). So, unless the `markdown_strict` format is used, the following does not produce a nested block quote in pandoc:

```
> This is a block quote.
>> Not nested, since `blank_before_blockquote` is enabled by default
```


## Verbatim (code) blocks

### Indented code blocks

A block of text indented four spaces (or one tab) is treated as verbatim text: that is, special characters do not trigger special formatting, and all spaces and line breaks are preserved. For example,

```
    if (a > 3) {
      moveShip(5 * gravity, DOWN);
    }
```

The initial (four space or one tab) indentation is not considered part of the verbatim text, and is removed in the output.

Note: blank lines in the verbatim text need not begin with four spaces.

### Fenced code blocks

### Extension: `fenced_code_blocks` ±

In addition to standard indented code blocks, pandoc supports *fenced* code blocks. These begin with a row of three or more tildes (`~`) and end with a row of tildes that must be at least as long as the starting row. Everything between these lines is treated as code. No indentation is necessary:

```
~~~~~~~
if (a > 3) {
  moveShip(5 * gravity, DOWN);
}
~~~~~~~
```

Like regular code blocks, fenced code blocks must be separated from surrounding text by blank lines.

If the code itself contains a row of tildes or backticks, just use a longer row of tildes or backticks at the start and end:

```
~~~~~~~~~~~~~~~~
~~~~~~~~~~
code including tildes
~~~~~~~~~~
~~~~~~~~~~~~~~~~
```

### Extension: `backtick_code_blocks` ±

Same as `fenced_code_blocks`, but uses backticks (`) instead of tildes (`~`).

### Extension: `fenced_code_attributes` ±

Optionally, you may attach attributes to fenced or backtick code block using this syntax:

```
~~~~ {#mycode .haskell .numberLines startFrom="100"}
qsort []     = []
qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++
               qsort (filter (>= x) xs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Here `mycode` is an identifier, `haskell` and `numberLines` are classes, and `startFrom` is an attribute with value `100`. Some output formats can use this information to do syntax highlighting. Currently, the only output formats that use this information are HTML, LaTeX, Docx, Ms, and PowerPoint. If highlighting is supported for your output format and language, then the code block above will appear highlighted, with numbered lines. (To see which languages are supported, type `pandoc --list-highlight-languages`.) Otherwise, the code block above will appear as follows:

```
<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
  ...
  </code>
</pre>
```

The `numberLines` (or `number-lines`) class will cause the lines of the code block to be numbered, starting with `1` or the value of the `startFrom` attribute. The `lineAnchors` (or `line-anchors`) class will cause the lines to be clickable anchors in HTML output.

A shortcut form can also be used for specifying the language of the code block:

````
```haskell
qsort [] = []
```
````

This is equivalent to:

````
``` {.haskell}
qsort [] = []
```
````

This shortcut form may be combined with attributes:

````
```haskell {.numberLines}
qsort [] = []
```
````

Which is equivalent to:

````
``` {.haskell .numberLines}
qsort [] = []
```
````

If the `fenced_code_attributes` extension is disabled, but input contains class attribute(s) for the code block, the first class attribute will be printed after the opening fence as a bare word.

To prevent all highlighting, use the `--syntax-highlighting=none` option. To set the highlighting style or method, use `--syntax-highlighting`. For more information on highlighting, see Syntax highlighting, below.


## Line blocks

### Extension: `line_blocks` ±

A line block is a sequence of lines beginning with a vertical bar (`|`) followed by a space. The division into lines will be preserved in the output, as will any leading spaces; otherwise, the lines will be formatted as Markdown. This is useful for verse and addresses:

```
| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical

| 200 Main St.
| Berkeley, CA 94718
```

The lines can be hard-wrapped if needed, but the continuation line must begin with a space.

```
| The Right Honorable Most Venerable and Righteous Samuel L.
  Constable, Jr.
| 200 Main St.
| Berkeley, CA 94718
```

Inline formatting (such as emphasis) is allowed in the content (though it can’t cross line boundaries). Block-level formatting (such as block quotes or lists) is not recognized.

This syntax is borrowed from reStructuredText.
