---
title: "Lightweight markup language"
source: https://en.wikipedia.org/wiki/Lightweight_markup_language
domain: restructuredtext
license: CC-BY-SA-4.0
tags: restructuredtext markup, docutils parser, lightweight markup, sphinx source
fetched: 2026-07-02
---

# Lightweight markup language

A **lightweight markup language** (**LML**), also termed a **simple** or **humane markup language**, is a markup language with simple, unobtrusive syntax. It is designed to be easy to write using any generic text editor and easy to read in its raw form. It is used in applications where it may be necessary to read the raw document and the final rendered output.

For instance, a person downloading a software library might prefer to read the documentation in a text editor rather than a web browser. Another use for such languages is to provide for data entry in web-based publishing, as in blogs and wikis, where the input interface is a simple text box. The server software then converts the input into a common document markup language like HTML.

## History

Lightweight markup languages were originally used on text-only displays which could not display characters in italics or bold, so informal methods to convey this information had to be developed. This formatting choice was naturally carried forth to plain-text email communications. Console browsers may also resort to similar display conventions.

In 1986 international standard SGML provided facilities to define and parse lightweight markup languages using grammars and tag implication. The 1998 W3C XML is a profile of SGML that omits these facilities. However, no SGML document type definition (DTD) for any of the languages listed below is known.

## Types

Lightweight markup languages can be categorized by their tag types. Like HTML (`<b>**bold**</b>`), some languages use named elements that share a common format for start and end tags (e.g., BBCode `[b]**bold**[/b]`), whereas proper lightweight markup languages are restricted to ASCII-only punctuation marks and other non-letter symbols for tags, but some also mix both styles (e.g., Textile `bq.`) or allow embedded HTML (e.g., Markdown), possibly extended with custom elements (e.g., MediaWiki `<ref>'''source'''</ref>`).

Most languages distinguish between markup for lines or blocks and for shorter spans of texts, but some only support inline markup.

Some markup languages are tailored for a specific purpose, such as documenting computer code (e.g., POD, reST, RD) or being converted to a certain output format (usually HTML or LaTeX) and nothing else, others are more general in application. This includes whether they are oriented on textual presentation or on data serialization.

Presentation oriented languages include AsciiDoc, atx, BBCode, Creole, Crossmark, Djot, Epytext, Haml, JsonML, MakeDoc, Markdown, Org-mode, POD (Perl), reST (Python), RD (Ruby), Setext, SiSU, SPIP, Xupl, Texy!, Textile, txt2tags, UDO and Wikitext.

Data serialization oriented languages include Curl (homoiconic, but also reads JSON; every object serializes), JSON, and YAML.

## Comparison of language features

| Language | HTML export tool | HTML import tool | Tables | Link titles | `class` attribute | `id` attribute | Release date |
|---|---|---|---|---|---|---|---|
| AsciiDoc | Yes | Yes | Yes | Yes | Yes | Yes | 2002-11-25 |
| BBCode | No | No | Yes | No | No | No | 1998 |
| Creole | No | No | Yes | No | No | No | 2007-07-04 |
| Djot | Yes | Yes | Yes | Yes | Yes | Yes | 2022-07-30 |
| DokuWiki | Yes | Yes/No | Yes | Yes | Yes/No | Yes/No | 2004-07-04 |
| Gemtext | Yes | Yes | No | Yes | No | No | 2020 |
| GitHub Flavored Markdown | Yes | No | Yes | Yes | No | No | 2011-04-28+ |
| Jira Formatting Notation | Yes | No | Yes | Yes | No | No | 2002+ |
| Markdown | Yes | Yes | No | Yes | Yes/No | Yes/No | 2004-03-19 |
| Markdown Extra | Yes | Yes | Yes | Yes | Yes | Yes | 2013-04-11 |
| MediaWiki | Yes | Yes | Yes | Yes | Yes | Yes | 2002 |
| MultiMarkdown | Yes | No | Yes | Yes | No | No | 2009-07-13 |
| Org-mode | Yes | Yes | Yes | Yes | Yes | Yes | 2003 |
| PmWiki | Yes | Yes | Yes | Yes | Yes | Yes | 2002-01 |
| POD | Yes | ? | No | Yes | ? | ? | 1994 |
| reStructuredText | Yes | Yes | Yes | Yes | Yes | auto | 2002-04-02 |
| setext | Yes | Yes | No | Yes | No | No | 1992 |
| Slack | No | No | No | Yes | No | No | 2013+ |
| Textile | Yes | No | Yes | Yes | Yes | Yes | 2002-12-26 |
| Texy | Yes | Yes | Yes | Yes | Yes | Yes | 2004 |
| TiddlyWiki | Yes | No | Yes | Yes | Yes | No | 2004-09 |
| txt2tags | Yes | Yes | Yes | Yes | Yes/No | Yes/No | 2001-07-26 |
| WhatsApp | No | No | No | No | No | No | 2016-03-16 |

Markdown's own syntax does not support class attributes or id attributes; however, since Markdown supports the inclusion of native HTML code, these features can be implemented using direct HTML. (Some extensions may support these features.)

txt2tags' own syntax does not support class attributes or id attributes; however, since txt2tags supports inclusion of native HTML code in tagged areas, these features can be implemented using direct HTML when saving to an HTML target.

DokuWiki does not support HTML import natively, but HTML to DokuWiki converters and importers exist and are mentioned in the official documentation. DokuWiki does not support class or id attributes, but can be set up to support HTML code, which does support both features. HTML code support was built-in before release 2023-04-04. In later versions, HTML code support can be achieved through plug-ins, though it is discouraged.

## Comparison of implementation features

Comparing implementations, especially output formats

Language

Implementations

X

HTML

Con

/

La

TeX

PDF

DocBook

ODF

EPUB

DOC

(X)

LMLs

Other

License

AsciiDoc

Python

,

Ruby

,

JavaScript

,

Java

XHTML

LaTeX

PDF

DocBook

ODF

EPUB

No

—

N/a

Man page

, etc.

GNU GPL, MIT

BBCode

Perl

,

PHP

,

C#

,

Python

,

Ruby

(X)HTML

No

No

No

No

No

No

—

N/a

—

N/a

Public Domain

Creole

PHP

,

Python

,

Ruby

,

JavaScript

Depends on implementation

CC BY-SA

1.0

Djot

Lua

(originally),

JavaScript

,

PHP

,

Prolog

,

Rust

HTML

LaTeX, ConTeXt

PDF

DocBook

ODF

EPUB

RTF

MediaWiki, reST

Man page, S5 etc.

MIT

GitHub Flavored Markdown

Haskell (

Pandoc

)

HTML

LaTeX, ConTeXt

PDF

DocBook

ODF

EPUB

DOC

AsciiDoc

,

reST

OPML

GPL

Java

,

JavaScript

,

PHP

,

Python

,

Ruby

HTML

No

No

No

No

No

No

—

N/a

—

N/a

Proprietary

Markdown

Perl

(originally),

C

,

Python

,

JavaScript

,

Haskell

,

Ruby

,

C#

,

Java

,

PHP

HTML

LaTeX, ConTeXt

PDF

DocBook

ODF

EPUB

RTF

MediaWiki

,

reST

Man page

,

S5

etc.

BSD-style & GPL (both)

Markdown Extra

PHP

(originally),

Python

,

Ruby

XHTML

No

No

No

No

No

No

—

N/a

—

N/a

BSD-style & GPL (both)

MediaWiki

Perl

,

PHP

,

Haskell

,

Python

XHTML

No

No

No

No

No

No

—

N/a

—

N/a

GNU GPL

MultiMarkdown

C

,

Perl

(X)HTML

LaTeX

PDF

No

ODF

No

DOC, RTF

—

N/a

OPML

GPL

,

MIT

Org-mode

Emacs Lisp

,

Ruby

(parser only),

Perl

,

OCaml

XHTML

LaTeX

PDF

DocBook

ODF

EPUB

DOCX

Markdown

TXT

,

XOXO

,

iCalendar

,

Texinfo

,

man

, contrib:

groff

,

s5

, deck.js, Confluence Wiki Markup,

TaskJuggler

,

RSS

,

FreeMind

GPL

PmWiki

PHP

XHTML 1.0 Transitional, HTML5

No

PDF export addons

No

No

EPUB export addon

No

—

N/a

—

N/a

GNU GPL

POD

Perl

(X)HTML, XML

LaTeX

PDF

DocBook

No

No

RTF

—

N/a

Man page

,

plain text

Artistic License

, Perl's license

reStructuredText

Python

,

Haskell

(

Pandoc

),

Java

HTML, XML

LaTeX

PDF

DocBook

ODF

EPUB

DOC

—

N/a

man

,

S5

,

Devhelp

,

Qt Help

,

CHM

,

JSON

Public Domain

Textile

PHP

,

JavaScript

,

Java

,

Perl

,

Python

,

Ruby

,

ASP

,

C#

,

Haskell

XHTML

No

No

No

No

No

No

—

N/a

—

N/a

Textile License

Texy!

PHP

,

C#

,

Java

(X)HTML

No

No

No

No

No

No

—

N/a

—

N/a

GNU GPL v2 License

txt2tags

Python

,

PHP

(X)HTML, SGML

LaTeX

PDF

DocBook

ODF

EPUB

DOC

Creole

,

AsciiDoc

,

MediaWiki

,

MoinMoin

,

PmWiki

,

DokuWiki

,

Google Code

Wiki

roff

,

man

,

MagicPoint

, Lout,

PageMaker

,

ASCII Art

,

TXT

GPL

## Comparison of lightweight markup language syntax

### Inline span syntax

Although usually documented as yielding italic and bold text, most lightweight markup processors output semantic HTML elements `em` and `strong` instead. Monospaced text may either result in semantic `code` or presentational `tt` elements. Few languages make a distinction, e.g., Textile, or allow the user to configure the output easily, e.g., Texy.

LMLs sometimes differ for multi-word markup where some require the markup characters to replace the inter-word spaces (*infix*). Some languages require one character as prefix and suffix, others need two or even three, or support both with slightly different meaning, e.g., different levels of emphasis.

| HTML output | `<strong>strongly emphasized</strong>` | `<em>emphasized text</em>` | `<code>code</code>` | semantic |
|---|---|---|---|---|
| `<b>bold text</b>` | `<i>italic text</i>` | `<tt>monospace text</tt>` | presentational |   |
| AsciiDoc | `*bold text*` | `_italic text_` | `monospace text` | Can double operators to apply formatting where there is no word boundary (for example `**b**old t**ex**t` yields **b**old t**ex**t). |
| `'italic text'` | `+monospace text+` |   |   |   |
| BBCode | `[b]bold text[/b]` | `[i]italic text[/i]` | `[code]monospace text[/code]` | Formatting works across line breaks. |
| Creole | `**bold text**` | `//italic text//` | `{{{monospace text}}}` | Triple curly braces are for *nowiki* which is optionally monospace. |
| Djot | `*bold text*` | `_italic text_` | `monospace text` |   |
| DokuWiki | `**bold text**` | `//italic text//` | `<code>code</code>` |   |
| `''monospace text''` |   |   |   |   |
| Gemtext | —N/a | —N/a | ```alt text monospace text ``` | Text immediately following the first three backticks is alt-text. |
| Jira Formatting Notation | `*bold text*` | `_italic text_` | `{{monospace text}}` |   |
| Markdown | `**bold text**` | `*italic text*` | `monospace text` | semantic HTML tags |
| `__bold text__` | `_italic text_` |   |   |   |
| MediaWiki | `'''bold text'''` | `''italic text''` | `<code>monospace text</code>` | mostly resorts to inline HTML |
| Org-mode | `*bold text*` | `/italic text/` | `=code=` |   |
| `~verbatim~` |   |   |   |   |
| PmWiki | `'''bold text'''` | `''italic text''` | `@@monospace text@@` |   |
| POD | `B<bold text>` | `I<italic text>` | `C<monospace text>` | Indented text is also shown as monospaced code. |
| reStructuredText | `**bold text**` | `*italic text*` | ``monospace text`` |   |
| Setext | `**bold text**` | `~italic text~` | `monospace text` |   |
| Slack | `*bold text*` | `_italic text_` | `monospace text` | ```block of monospaced text``` |
| Textile | `*strong*` | `_emphasis_` | `@monospace text@` | semantic HTML tags |
| `**bold text**` | `__italic text__` | presentational HTML tags |   |   |
| Texy! | `**bold text**` | `*italic text*` | `monospace text` | semantic HTML tags by default, optional support for presentational tags |
| `//italic text//` |   |   |   |   |
| TiddlyWiki | `''bold text''` | `//italic text//` | `monospace text` |   |
| ``monospace text`` |   |   |   |   |
| txt2tags | `**bold text**` | `//italic text//` | ``monospace text`` |   |
| WhatsApp | `*bold text*` | `_italic text_` | ```monospace text``` |   |

Gemtext does not have any inline formatting, monospaced text (called preformatted text in the context of Gemtext) must have the opening and closing ``` on their own lines.

#### Emphasis syntax

In HTML, text is emphasized with the `<em>` and `<strong>` element types, whereas `<i>` and `<b>` traditionally mark up text to be italicized or bold-faced, respectively.

Microsoft Word and Outlook, and accordingly other word processors and mail clients that strive for a similar user experience, support the basic convention of using asterisks for boldface and underscores for italic style. While Word removes the characters, Outlook retains them.

Italic type or normal emphasis

Code

AsciiDoc

ATX

Creole,

DokuWiki

Jira

Markdown

MediaWiki

Org-mode

PmWiki

reST

Setext

Slack

Textile

Texy!

TiddlyWiki

txt2tags

WhatsApp

*italic*

No

No

No

No

Yes

No

No

No

Yes

No

No

No

Yes

No

No

No

**italic**

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

_italic_

Yes

Yes

No

Yes

Yes

No

No

No

No

No

Yes

Yes

No

No

No

Yes

__italic__

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

No

Yes

No

No

No

No

'italic'

Yes/No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

''italic''

Yes/No

No

No

No

No

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

No

/italic/

No

No

No

No

No

No

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

//italic//

No

No

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

Yes

Yes

Yes

No

~italic~

No

No

No

No

No

No

No

No

No

Yes

No

No

No

No

No

No

Bold face or strong emphasis

Code

AsciiDoc

ATX

Creole,

DokuWiki

Jira

Markdown

MediaWiki

Org-mode

PmWiki

reST

Setext

Slack

Textile

Texy!

TiddlyWiki

txt2tags

WhatsApp

*bold*

Yes

Yes

No

Yes

No

No

Yes

No

No

No

Yes

Yes

No

No

No

Yes

**bold**

Yes

No

Yes

No

Yes

No

No

No

Yes

Yes

No

Yes

Yes

No

Yes

No

__bold__

No

No

No

No

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

No

No

''bold''

No

No

No

No

No

No

No

No

No

No

No

No

No

Yes

No

No

'''bold'''

No

No

No

No

No

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

No

#### Editorial syntax

In HTML, removed or deleted and inserted text is marked up with the `<del>` and `<ins>` element types, respectively. However, legacy element types `<s>` or `<strike>` and `<u>` are still also available for stricken and underlined spans of text.

Underlined or inserted text

Language

Code

DokuWiki

Jira

Markdown

Org-mode

Setext

Texy!

TiddlyWiki

txt2tags

_underline_

No

No

Optional

Yes

Yes

No

No

No

__underline__

Yes

No

Optional

No

No

No

Yes

Yes

+underline+

No

Yes

No

No

No

No

No

No

++underline++

No

No

No

No

No

Yes

No

No

AsciiDoc, ATX, Creole, MediaWiki, PmWiki, reST, Slack, Textile and WhatsApp do not support dedicated markup for underlining text. Textile does, however, support insertion via the `+inserted+` syntax.

Strike-through or deleted text

Language

Code

Jira

Markdown

Org-mode

Slack

Textile

Texy

TiddlyWiki

txt2tags

WhatsApp

~stricken~

No

No

No

Yes

No

No

No

No

Yes

~~stricken~~

No

GFM

No

No

No

No

Yes

No

No

+stricken+

No

No

Yes

No

No

No

No

No

No

-stricken-

Yes

No

No

No

Yes

No

No

No

No

--stricken--

No

No

No

No

No

Yes

No

Yes

No

ATX, Creole, MediaWiki, PmWiki, reST and Setext do not support dedicated markup for striking through text.

DokuWiki supports HTML-like `<del>stricken</del>` syntax, even with embedded HTML disabled.

AsciiDoc supports stricken text through a built-in *text span* prefix: `[.line-through]#stricken#`.

#### Programming syntax

Quoted computer code is traditionally presented in typewriter-like fonts where each character occupies the same fixed width. HTML offers the semantic `<code>` and the deprecated, presentational `<tt>` element types for this task.

Monospaced font, teletype text or code

Code

AsciiDoc

ATX

Creole

Gemtext

Jira

Markdown

Org-mode

PmWiki

reST

Slack

Textile

Texy!

TiddlyWiki

txt2tags

WhatsApp

@code@

No

No

No

No

No

No

No

No

No

No

Yes

No

No

No

No

@@code@@

No

No

No

No

No

No

No

Yes

No

No

No

No

No

No

No

`code`

Yes

No

No

No

No

Yes

No

No

No

Yes

No

Yes

Yes

No

Yes

``code``

Yes

No

No

No

No

Yes

No

No

Yes

No

No

No

Yes

Yes

No

```code```

No

No

No

Yes

No

Yes

No

No

No

Yes/No

No

No

Yes

No

No

=code=

No

No

No

No

No

No

Yes

No

No

No

No

No

No

No

No

~code~

No

No

No

No

No

No

Yes

No

No

No

No

No

No

No

No

+code+

Yes/No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

++code++

Yes/No

No

No

No

No

No

No

No

No

No

No

No

No

No

No

{{code}}

No

No

No

No

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

No

{{{code}}}

No

No

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

No

No

No

|code|

No

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

No

No

No

No

;;code;;

Mediawiki and Gemtext do not provide lightweight markup for inline code spans.

### Heading syntax

Headings are usually available in up to six levels, but the top one is often reserved to contain the same as the document title, which may be set externally. Some documentation may associate levels with divisional types, e.g., part, chapter, section, article or paragraph. This article uses *1* as the top level, but index of heading levels may begin at *1* or *0* in official documentation.

Most LMLs follow one of two styles for headings, either Setext-like underlines or atx-like line markers, or they support both.

#### Underlined headings

```
Level 1 Heading
===============

Level 2 Heading
---------------

Level 3 Heading
~~~~~~~~~~~~~~~
```

The first style uses underlines, i.e., repeated characters (e.g., equals `=`, hyphen `-` or tilde `~`, usually at least two or four times) in the line below the heading text.

Underlined heading levels

Character

Language

=

-

~

*

#

+

^

_

:

"

'

`

.

Min. length

AsciiDoc

1

2

3

No

No

5

4

No

No

No

No

No

No

2

Markdown

1

2

No

No

No

No

No

No

No

No

No

No

No

1

reStructuredText

Heading structure is determined dynamically from the succession of headings

heading width

Setext

1

2

No

No

No

No

No

No

No

No

No

No

No

?

Texy!

3

4

No

2

1

No

No

No

No

No

No

No

No

3

Headings may optionally be overline in reStructuredText, in addition to being underlined.

#### Prefixed headings

```
# Level 1 Heading
## Level 2 Heading ##
### Level 3 Heading ###
```

The second style is based on repeated markers (e.g., hash `#`, equals `=` or asterisk `*`) at the start of the heading itself, where the number of repetitions indicates the (sometimes inverse) heading level. Most languages also support the reduplication of the markers at the end of the line, but whereas some make them mandatory, others do not even expect their numbers to match.

Line prefix (and suffix) headings

Character

Language

=

#

*

!

+

Suffix

Levels

Indentation

AsciiDoc

Yes

No

No

No

No

Optional

1–6

No

Creole

Yes

No

No

No

No

Optional

1–6

No

DokuWiki

Yes

No

No

No

No

Yes

6-1

No

Gemtext

No

Yes

No

No

No

?

1–3

No

Markdown

No

Yes

No

No

No

Optional

1–6

No

MediaWiki

Yes

No

No

No

No

Yes

1–6

No

Org-mode

No

No

Yes

No

No

No

1– +∞

alternative

PmWiki

No

No

No

Yes

No

Optional

1–6

No

Texy!

Yes

Yes

No

No

No

Optional

6–1, dynamic

No

TiddlyWiki

No

No

No

Yes

No

No

1–6

No

txt2tags

Yes

No

No

No

Yes

Yes

1–6

No

Org-mode supports indentation as a means of indicating the level.

BBCode does not support section headings at all.

POD and Textile choose the HTML convention of numbered heading levels instead.

| Language | Format |
|---|---|
| POD | =head1 Level 1 Heading =head2 Level 2 Heading |
| Jira, Textile | h1. Level 1 Heading h2. Level 2 Heading h3. Level 3 Heading h4. Level 4 Heading h5. Level 5 Heading h6. Level 6 Heading |

Microsoft Word supports auto-formatting paragraphs as headings if they do not contain more than a handful of words, no period at the end and the user hits the enter key twice. For lower levels, the user may press the tabulator key the according number of times before entering the text, i.e., one through eight tabs for heading levels two through nine.

### Link syntax

Hyperlinks can either be added inline, which may clutter the code because of long URLs, or with named `alias` or numbered `id` references to lines containing nothing but the address and related attributes and often may be located anywhere in the document. Most languages allow the author to specify text `Text` to be displayed instead of the plain address `http://example.com` and some also provide methods to set a different link title `Title` which may contain more information about the destination.

LMLs that are tailored for special setups, e.g., wikis or code documentation, may automatically generate named anchors (for headings, functions etc.) inside the document, link to related pages (possibly in a different namespace) or provide a textual search for linked keywords.

Most languages employ (double) square or angular brackets to surround links, but hardly any two languages are completely compatible. Many can automatically recognize and parse absolute URLs inside the text without further markup.

| Languages | Basic syntax | Text syntax | Title syntax |
|---|---|---|---|
| AsciiDoc | `http://example.com[Text]` | `http://example.com` |   |
| BBCode, Creole, MediaWiki, PmWiki |   |   |   |
| Slack | `<http://example.com\|Text>` |   |   |
| Textile | `"Text":http://example.com` | `"Text (Title)":http://example.com` |   |
| Texy! | `"Text .(Title)":http://example.com` |   |   |
| Jira | `[http://example.com]` | `[Text\|http://example.com]` |   |
| MediaWiki | `[http://example.com Text]` |   |   |
| txt2tags | `[Text http://example.com]` |   |   |
| Creole, MediaWiki, PmWiki, DokuWiki | `[[Name]]` | `[[Name\|Text]]` |   |
| Org-mode | `[[Name][Text]]` |   |   |
| TiddlyWiki | `[[Text\|Name]]` |   |   |
| Creole | `[[Namespace:Name]]` | `[[Namespace:Name\|Text]]` |   |
| Org-mode | `[[Namespace:Name][Text]]` |   |   |
| Creole, PmWiki | `[[http://example.com]]` | `[[http://example.com\|Text]]` |   |
| BBCode | `[url]http://example.com[/url]` | `[url=http://example.com]Text[/url]` |   |
| Markdown | `<http://example.com>` | `[Text](http://example.com)` | `[Text](http://example.com "Title")` |
| reStructuredText | `Text <http://example.com/>`_ |   |   |
| Gemtext | `=> gemini://example.com` | `=> gemini://example.com Text` |   |
| POD | `L<http://example.com/>` | `L</Name>` |   |
| setext |   | `^.. _Link_name URL` |   |

Gemtext and setext links must be on a line by themselves, they cannot be used inline.

| Languages | Text syntax | Title syntax |
|---|---|---|
| AsciiDoc | … [[id]] … <<id>> | … [[id]] … <<id,Text>> |
| … anchor:id … xref:id | … anchor:id … xref:id[Text] |   |
| Markdown | … [Text][id] … [id]: http://example.com | … [Text][id] … [id]: http://example.com "Title" |
| … [Text][] … [Text]: http://example.com | … [Text][] … [Text]: http://example.com "Title" |   |
| … [Text] … [Text]: http://example.com | … [Text] … [Text]: http://example.com "Title" |   |
| reStructuredText | … Name_ … .. _Name: http://example.com |   |
| setext | … Link_name_ … ^.. _Link_name URL |   |
| Textile | … "Text":alias … [alias]http://example.com | … "Text":alias … [alias (Title)]http://example.com |
| Texy! | … "Text":alias … [alias]: http://example.com | … "Text":alias … [alias]: http://example.com .(Title) |

Org-mode's normal link syntax does a text search of the file. You can also put in dedicated targets with `<<id>>`.

### Media and external resource syntax

### List syntax

HTML requires an explicit element for the list, specifying its type, and one for each list item, but most lightweight markup languages need only different line prefixes for the bullet points or enumerated items. Some languages rely on indentation for nested lists, others use repeated parent list markers.

Unordered, bullet list items

Character

Language

*

-

+

#

.

·

•

_

:

–

—

indent

skip

nest

AsciiDoc

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

No

0

?

repeat

or

alternate the marker

DokuWiki

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

No

2+

0+

indent

Gemtext

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

No

0

1+

—

N/a

Jira

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

No

0

1+

repeat

Markdown

Yes

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

0–3

1–3

indent

MediaWiki

,

TiddlyWiki

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

No

0

1+

repeat

Org-mode

Yes

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

0+

indent

Textile

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

No

0

1+

repeat

Texy!

Yes

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

2+

?

indent

Microsoft Word automatically converts paragraphs that start with an asterisk `*`, hyphen-minus `-` or greater-than bracket `>` followed by a space or horizontal tabulator as bullet list items. It will also start an enumerated list for the digit *1* and the case-insensitive letters *a* (for alphabetic lists) or *i* (for roman numerals), if they are followed by a period `.`, a closing round parenthesis `)`, a greater-than sign `>` or a hyphen-minus `-` and a space or tab; in case of the round parenthesis an optional opening one `(` before the list marker is also supported.

Languages differ on whether they support optional or mandatory digits in numbered list items, which kinds of enumerators they understand (e.g., decimal digit *1*, roman numerals *i* or *I*, alphabetic letters *a* or *A*) and whether they support to keep explicit values in the output format. Some Markdown dialects, for instance, will respect a start value other than 1, but ignore any other explicit value.

Ordered, enumerated list items

Character

Language

+

#

-

.

#1

1.

1)

1]

1}

(1)

[1]

{1}

a.

A.

i.

I.

indent

skip

nest

AsciiDoc

No

No

No

Yes

No

Yes

No

No

No

No

No

No

Yes

0

?

repeat

or

alternate the marker

DokuWiki

No

No

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

No

No

No

No

2+

0+

indent

Jira

,

MediaWiki

,

Textile

,

TiddlyWiki

No

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

No

No

No

No

No

0

1+

repeat

Markdown

No

No

No

No

No

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

No

0–3

1–3

indent

Org-mode

No

No

No

No

No

Yes

Yes

No

No

No

No

No

Optional

No

No

0+

indent

Texy!

No

No

No

No

No

Yes

Yes

No

No

No

No

No

Only with

)

delimiter

No

Only with

)

delimiter

2+

?

indent

Slack assists the user in entering enumerated and bullet lists, but does not actually format them as such, i.e., it just includes a leading digit followed by a period and a space or a bullet character `•` in front of a line.

| Languages | Term being defined | Definition of the term |
|---|---|---|
| AsciiDoc | `Term::` | No specific requirements; may be mixed with ordered or unordered lists, with nesting optional |
| `Term::::` |   |   |
| `Term;;` |   |   |
| MediaWiki | `; Term` | `: Definition` |
| Textile |   |   |
| TiddlyWiki |   |   |
| Texy! | Term: - Definition |   |
| Org-mode | `- Term :: Definition` |   |

### Quotation syntax

### Table syntax

## Historical formats

The following lightweight markup languages, while similar to some of those already mentioned, have not yet been added to the comparison tables in this article:

- EtText: circa 2000.
- Grutatext: circa 2002.
