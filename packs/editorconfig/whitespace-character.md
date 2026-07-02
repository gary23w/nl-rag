---
title: "Whitespace character"
source: https://en.wikipedia.org/wiki/Whitespace_character
domain: editorconfig
license: CC-BY-SA-4.0
tags: editorconfig, editor coding style config, indentation style config, cross-editor formatting
fetched: 2026-07-02
---

# Whitespace character

A **whitespace character** is a character data element that represents white space when text is rendered for display by a computer.

For example, a *space* character (U+0020   SPACE, ASCII 32) represents blank space such as a word divider in a Western script.

A printable character results in output when rendered, but a whitespace character does not. Instead, whitespace characters define the layout of text to a limited degree, interrupting the normal sequence of rendering characters next to each other. The output of subsequent characters is typically shifted to the right (or to the left for right-to-left script) or to the start of the next line. The effect of multiple sequential whitespace characters is cumulative such that the next printable character is rendered at a location based on the accumulated effect of preceding whitespace characters.

The origin of the term *whitespace* is rooted in the common practice of rendering text on white paper. Normally, a whitespace character is *not* rendered as white. It affects rendering, but it is not itself rendered.

## Overview

A space character typically inserts horizontal space that is about as wide as a letter. For a monospaced font the width is the width of a letter, and for a variable-width font the width is font-specific. Some fonts support multiple space characters that have different widths.

A tab character typically inserts horizontal space that is based on tab stops which vary by application.

A newline character sequence typically moves the render output location to the beginning of the next line. If one follows text, it does not actually result in whitespace. But, two sequential newline sequences between text blocks results in a blank line between the blocks. The height of the blank line varies by application.

Using whitespace characters to lay out text is a convention. Applications sometimes render whitespace characters as visible markup so that a user can see what is normally not visible.

Typically, a user types a space character by pressing spacebar, a tab character by pressing Tab ↹ and newline by pressing ↵ Enter.

## Unicode

The table below lists the twenty-five characters defined as whitespace ("WSpace=Y", "WS") characters in the Unicode Character Database. Seventeen use a definition of whitespace consistent with the algorithm for bidirectional writing ("Bidirectional Character Type=WS") and are known as "Bidi-WS" characters. The remaining characters may also be used, but are not of this "Bidi" type.

*Note: Depending on the browser and fonts used to view the following table, not all spaces may be displayed properly.*

Name

Code point

Width box

May break

?

In

IDN

?

Script

Block

General

category

Notes

character tabulation

U+0009

9

Yes

No

Common

Basic Latin

Other,

control

HT,

Horizontal Tab

. HTML/XML

named entity

:

&

Tab;

,

LaTeX

:

\tab

,

C

escape:

\t

line feed

U+000A

10

Is a line-break

Common

Basic Latin

Other,

control

LF,

Line feed

. HTML/XML named entity:

&

NewLine;

, C escape:

\n

line tabulation

U+000B

11

Is a line-break

Common

Basic Latin

Other,

control

VT,

Vertical Tab

. C escape:

\v

form feed

U+000C

12

Is a line-break

Common

Basic Latin

Other,

control

FF,

Form feed

. C escape:

\f

carriage return

U+000D

13

Is a line-break

Common

Basic Latin

Other,

control

CR,

Carriage return

. C escape:

\r

space

U+0020

32

Yes

No

Common

Basic Latin

Separator,

space

Most common (normal ASCII space). LaTeX:

\

next line

U+0085

133

Is a line-break

Common

Latin-1

Supplement

Other,

control

NEL,

Next line

. LaTeX:

\\

no-break space

U+00A0

160

No

No

Common

Latin-1

Supplement

Separator,

space

Non-breaking space

: identical to U+0020, but not a point at which a line may be broken.

HTML/XML named entity:

&

nbsp;

,

&

NonBreakingSpace;

, LaTeX:

~

ogham space mark

U+1680

5760

Yes

No

Ogham

Ogham

Separator,

space

Used for

interword separation

in

Ogham

text. Normally a vertical line in vertical text or a horizontal line in horizontal text, but may also be a blank space in "stemless" fonts. Requires an Ogham font.

en quad

U+2000

8192

Yes

No

Common

General

Punctuation

Separator,

space

Width of one

en

. U+2002 is canonically equivalent to this character; U+2002 is preferred.

em quad

U+2001

8193

Yes

No

Common

General

Punctuation

Separator,

space

Also known as "mutton quad". Width of one

em

. U+2003 is canonically equivalent to this character; U+2003 is preferred.

en space

U+2002

8194

Yes

No

Common

General

Punctuation

Separator,

space

Also known as "nut". Width of one

en

. U+2000 En Quad is canonically equivalent to this character; U+2002 is preferred.

HTML/XML named entity:

&

ensp;

, LaTeX:

\enspace

(the LaTeX en space is a no-break space)

em space

U+2003

8195

Yes

No

Common

General

Punctuation

Separator,

space

Also known as "mutton". Width of one

em

. U+2001 Em Quad is canonically equivalent to this character; U+2003 is preferred.

HTML/XML named entity:

&

emsp;

, LaTeX:

\quad

three-per-em space

U+2004

8196

Yes

No

Common

General

Punctuation

Separator,

space

Also known as "thick space". One third of an em wide.

HTML/XML named entity:

&

emsp13;

, LaTeX:

\;

(the LaTeX thick space is a no-break space)

four-per-em space

U+2005

8197

Yes

No

Common

General

Punctuation

Separator,

space

Also known as "mid space". One fourth of an em wide.

HTML/XML named entity:

&

emsp14;

six-per-em space

U+2006

8198

Yes

No

Common

General

Punctuation

Separator,

space

One sixth of an em wide. In computer typography, sometimes equated to U+2009.

figure space

U+2007

8199

No

No

Common

General

Punctuation

Separator,

space

Figure space

. In fonts with monospaced digits, equal to the width of one digit.

HTML/XML named entity:

&

numsp;

punctuation space

U+2008

8200

Yes

No

Common

General

Punctuation

Separator,

space

As wide as the narrow punctuation in a font, i.e. the advance width of the period or comma.

HTML/XML named entity:

&

puncsp;

thin space

U+2009

8201

Yes

No

Common

General

Punctuation

Separator,

space

Thin space

; one-fifth (sometimes one-sixth) of an em wide. Recommended for use as a

thousands separator

for measures made with

SI units

. Unlike U+2002 to U+2008, its width may get adjusted in typesetting.

HTML/XML named entity:

&

thinsp;

,

&

ThinSpace;

, LaTeX:

\,

(the LaTeX thin space is a no-break space)

hair space

U+200A

8202

Yes

No

Common

General

Punctuation

Separator,

space

Thinner than a thin space. HTML/XML named entity:

&

hairsp;

,

&

VeryThinSpace;

line separator

U+2028

8232

Is a line-break

Common

General

Punctuation

Separator,

line

paragraph separator

U+2029

8233

Is a line-break

Common

General

Punctuation

Separator,

paragraph

narrow no-break space

U+202F

8239

No

No

Common

General

Punctuation

Separator,

space

Narrow no-break space

. Similar in function to U+00A0 No-Break Space. When used with Mongolian, its width is usually one third of the normal space; in other context, its width sometimes resembles that of the

Thin Space

(U+2009). LaTeX:

\,

medium mathematical space

U+205F

8287

Yes

No

Common

General

Punctuation

Separator,

space

MMSP. Used in mathematical formulae. Four-eighteenths of an em.

In mathematical typography, the widths of spaces are usually given in integral multiples of an eighteenth of an em, and 4/18 em may be used in several situations, for example between the

a

and the

+

and between the

+

and the

b

in the expression

a

+

b

.

HTML/XML named entity:

&

MediumSpace;

, LaTeX:

\:

(the LaTeX medium space is a no-break space)

ideographic space

U+3000

12288

Yes

No

Common

CJK Symbols

and

Punctuation

Separator,

space

As wide as a

CJK character

cell (

fullwidth

). Used, for example, in

tai tou

.

Name

Code point

Width box

May break

?

In

IDN

?

Script

Block

General

category

Notes

mongolian vowel separator

U+180E

6158

᠎

Yes

No

Mongolian

Mongolian

Other,

Format

MVS. A narrow space character, used in Mongolian to cause the final two characters of a word to take on different shapes.

It is no longer classified as space character (i.e. in Zs category) in Unicode 6.3.0, even though it was in previous versions of the standard.

zero width space

U+200B

8203

Yes

No

?

General

Punctuation

Other,

Format

ZWSP,

zero-width space

. Used to indicate word boundaries to text processing systems when using scripts that do not use explicit spacing. It is similar to the

soft hyphen

, with the difference that the latter is used to indicate syllable boundaries, and should display a visible hyphen when the line breaks at it.

HTML/XML

named entity

:

&

ZeroWidthSpace;

zero width non-joiner

U+200C

8204

‌

Yes

Context-dependent

?

General

Punctuation

Other,

Format

ZWNJ,

zero-width non-joiner

. When placed between two characters that would otherwise be connected, a ZWNJ causes them to be printed in their final and initial forms, respectively.

HTML/XML named entity:

&

zwnj;

zero width joiner

U+200D

8205

‍

Yes

Context-dependent

?

General

Punctuation

Other,

Format

ZWJ,

zero-width joiner

. When placed between two characters that would otherwise not be connected, a ZWJ causes them to be printed in their connected forms. Can also be used to display joining forms in isolation. Depending on whether a ligature or conjunct is expected by default, can either induce (as

in emoji

and

in Sinhala

) or suppress (as in

Devanagari

) substitution with a single glyph, whilst still permitting use of individual joining forms (unlike ZWNJ).

HTML/XML named entity:

&

zwj;

word joiner

U+2060

8288

⁠

No

No

?

General

Punctuation

Other,

Format

WJ,

word joiner

. Similar to U+200B, but not a point at which a line may be broken.

HTML/XML named entity:

&

NoBreak;

zero width non-breaking space

U+FEFF

65279

﻿

No

No

?

Arabic

Presentation

Forms-B

Other,

Format

Zero-width non-breaking space

. Used primarily as a

Byte Order Mark

. Use as an indication of non-breaking is deprecated as of Unicode 3.2; see U+2060 instead.

| White_Space is a binary Unicode property. *"Unicode PropList.txt". *Unicode*. 2025-06-30. Retrieved 2025-09-11.* Although `&ZeroWidthSpace;` is one HTML5 named entity for U+200B, the additional names `NegativeMediumSpace`, `NegativeThickSpace`, `NegativeThinSpace` and `NegativeVeryThinSpace` (which are names used in the Wolfram Language for negative-advance spaces, which it maps to the Private Use Area) are also defined by HTML5 as aliases for U+200B (e.g. `&NegativeMediumSpace;`). |
|---|

### Substitute images

Unicode also provides some visible characters that can be used to represent various whitespace characters, in contexts where a visible symbol must be displayed:

| Code | Decimal | Name | Block | Display | Description |
|---|---|---|---|---|---|
| U+00B7 | 183 | Middle dot | Latin-1 Supplement | · | Interpunct Named entity: `&middot;` |
| U+21A1 | 8609 | Downwards two headed arrow | Arrows | ↡ | ECMA-17 / ISO 2047 symbol for form feed (page break) |
| U+2261 | 8810 | Identical to | Mathematical Operators | ≡ | Amongst other uses, is the ECMA-17 / ISO 2047 symbol for line feed |
| U+237D | 9085 | Shouldered open box | Miscellaneous Technical | ⍽ | Used to indicate a NBSP |
| U+23CE | 9166 | Return symbol | Miscellaneous Technical | ⏎ | Symbol for a return key, which enters a line break |
| U+2409 | 9225 | Symbol for horizontal tabulation | Control Pictures | ␉ | Substitutes for a tab character |
| U+240A | 9226 | Symbol for line feed | Control Pictures | ␊ | Substitutes for a line feed |
| U+240B | 9227 | Symbol for vertical tabulation | Control Pictures | ␋ | Substitutes for a vertical tab (line tab) |
| U+240C | 9228 | Symbol for form feed | Control Pictures | ␌ | Substitutes for a form feed (page break) |
| U+240D | 9229 | Symbol for carriage return | Control Pictures | ␍ | Substitutes for a carriage return |
| U+2420 | 9248 | Symbol for space | Control Pictures | ␠ | Substitutes for an ASCII space |
| U+2422 | 9250 | Blank symbol | Control Pictures | ␢ | aka "substitute blank", used in BCDIC, EBCDIC, ASCII-1963 etc. as a symbol for the word separator |
| U+2423 | 9251 | Open box | Control Pictures | ␣ | Used in block letter handwriting at least since the 1980s when it is necessary to explicitly indicate the number of space characters (e.g. when programming with pen and paper). Used in a textbook (published 1982, 1984, 1985, 1988 by Springer-Verlag) on Modula-2, a programming language where space codes require explicit indication. Also used in the keypad of the Texas Instruments' TI-8*x* series of graphing calculators. Named entity: `&blank;` |
| U+2424 | 9252 | Symbol for newline | Control Pictures | ␤ | Substitutes for a line break |
| U+25B3 | 9651 | White up-pointing triangle | Geometric Shapes | △ | Amongst other uses, is the ECMA-17 / ISO 2047 symbol for the ASCII space |
| U+2A5B | 10843 | Logical Or with middle stem | Supplemental Mathematical Operators | ⩛ | Amongst other uses, is the ECMA-17 / ISO 2047 symbol for vertical tab (line tab) |
| U+2AAA | 10922 | Smaller than | Supplemental Mathematical Operators | ⪪ | Amongst other uses, is the ECMA-17 / ISO 2047 symbol for carriage return |
| U+2AAB | 10923 | Larger than | Supplemental Mathematical Operators | ⪫ | Amongst other uses, is the ECMA-17 / ISO 2047 symbol for the tab character |
| U+2B1A | 11034 | Dotted square | Miscellaneous Symbols and Arrows | ⬚ |   |
| U+3037 | 12343 | Ideographic Telegraph Line Feed Separator Symbol | CJK Symbols and Punctuation | 〷 | Graphic used for code 9999 in Chinese telegraph code, representing a line feed |

1. Above the zero "0" or negative "(‒)" key.

**Exact space**

- The Cambridge Z88 provided a special "exact space" (code point 160 aka 0xA0) (invokable by key shortcut ⌑+SPACE), displayed as "…" by the operating system's display driver. It was therefore also known as "dot space" in conjunction with BBC BASIC.
- Under code point 224 (0xE0) the computer also provided a special three-character-cells-wide SPACE symbol `"SPC"` (analogous to Unicode's single-cell-wide U+2420).

### Non-space blanks

- The Braille Patterns Unicode block contains U+2800 ⠀ BRAILLE PATTERN BLANK, a Braille pattern with no dots raised. Some fonts display the character as a fixed-width blank, however the Unicode standard explicitly states that it does not act as a space.
- Unicode's coverage of the Korean alphabet includes several code points which represent the absence of a written letter, and thus do not display a glyph:
  - Unicode includes a Hangul Filler character in the Hangul Compatibility Jamo block (U+3164 ㅤ HANGUL FILLER). This is classified as a letter, but displayed as an empty space, like a Hangul block containing no jamo. It is used in KS X 1001 Hangul combining sequences to introduce them or denote the absence of a letter in a position, but not in Unicode's combining jamo system.
  - Unicode's combining jamo system uses similar Hangul Choseong Filler and Hangul Jungseong Filler characters to denote the absence of a letter in initial or medial position within a syllable block, which are included in the Hangul Jamo block (U+115F ᅟ HANGUL CHOSEONG FILLER, U+1160 ᅠ HANGUL JUNGSEONG FILLER).
  - Additionally, a Halfwidth Hangul Filler is included in the Halfwidth and Fullwidth Forms (U+FFA0 ﾠ HALFWIDTH HANGUL FILLER), which is used when mapping from encodings which include characters from both Johab (or Wansung) and N-byte Hangul (or its EBCDIC counterpart), such as IBM-933, which includes both Johab and EBCDIC fillers.

## Whitespace and digital typography

### On-screen display

Text editors, word processors, and desktop publishing software differ in how they represent whitespace on the screen, and how they represent spaces at the ends of lines longer than the screen or column width. In some cases, spaces are shown simply as blank space; in other cases they may be represented by an interpunct or other symbols. Many different characters (described below) could be used to produce spaces, and non-character functions (such as margins and tab settings) can also affect whitespace.

Many of the Unicode space characters were created for compatibility with classic print typography.

Even if digital typography has algorithmic kerning and justification, those space characters can be used to supplement the electronic formatting when needed.

### Variable-width general-purpose space

In computer character encodings, there is a normal **general-purpose space** (Unicode character U+0020) whose width will vary according to the design of the typeface. Typical values range from 1/5 em to 1/3 em (in digital typography an em is equal to the nominal size of the font, so for a 10-point font the space will probably be between 2 and 3.3 points). Sophisticated fonts may have differently sized spaces for bold, italic, and small-caps faces, and often compositors will manually adjust the width of the space depending on the size and prominence of the text.

In addition to this general-purpose space, it is possible to encode a space of a specific width. See the table above for a complete list.

### Hair spaces around dashes

Em dashes used as parenthetical dividers, and en dashes when used as word joiners, are usually set continuous with the text. However, such a dash can optionally be surrounded with a **hair space**, U+200A, or **thin space**, U+2009. The hair space can be written in HTML by using the numeric character references `&#x200A;` or `&#8202;`, or the named entity `&hairsp;`. The thin space is named entity `&thinsp;` and numeric references `&#x2009;` or `&#8201;`. These spaces are much thinner than a normal space (except in a monospaced (non-proportional) font), with the hair space in particular being the thinnest of horizontal whitespace characters.

| Normal space with em dash | left — right |
|---|---|
| Thin space with em dash | left — right |
| Hair space with em dash | left — right |
| No space with em dash | left—right |

## Computing applications

### Programming languages

In most programming language syntax, whitespace characters can be used to separate tokens. For a free-form language, whitespace characters are ignored by code processors (i.e. compiler). Even when language syntax requires white space, often multiple whitespace characters are treated the same as a single. In an off-side rule language, indentation white space is syntactically significant. In the satirical and contrarian language called Whitespace, whitespace characters are the only significant characters and normal text is ignored.

Good use of white space in source code can group related logic and make the code easier to understand. Excessive use of whitespace, including at the end of a line where it provides no rendering behavior, is considered a nuisance.

Most languages only recognize whitespace characters that have an ASCII code. They disallow most or all of the Unicode codes listed above. The C language defines whitespace characters to be "space, horizontal tab, new-line, vertical tab, and form-feed". The HTTP network protocol requires different types of whitespace to be used in different parts of the protocol; it requires single space characters between items in the status line, a CR/LF pair at the end of a line, and "linear whitespace" in header values.

### Command-line parsing

Typical command-line parsers use the space character to delimit arguments. A value with an embedded space character is problematic since it causes the value to parse as multiple arguments. Typically, a parser allows for escaping the normal argument parsing by enclosing the text in quotes.

If, for example, a user wanted to view the contents of a directory named `foo bar` by using the `ls` (list) command, and they did so by entering the command as:

```mw
ls foo bar
```

the command would, instead, attempt to list files or directories named `foo` and `bar`. The correct syntax would specify only a single argument by enclosing it in double quotes:

```mw
ls "foo bar"
```

Or, alternatively, they could choose to leave out the double quotes and instead escape the space with a backslash:

```mw
ls foo\ bar
```

### Markup languages

Some markup languages, such as SGML, preserve whitespace as written.

Web markup languages such as XML and HTML treat whitespace characters specially, including space characters, for programmers' convenience. One or more space characters read by conforming display-time processors of those markup languages are collapsed to 0 or 1 space, depending on their semantic context. For example, double (or more) spaces within text are collapsed to a single space, and spaces which appear on either side of the "`=`" that separates an attribute name from its value have no effect on the interpretation of the document. Element end tags can contain trailing spaces, and empty-element tags in XML can contain spaces before the "`/>`". In these languages, unnecessary whitespace increases the file size, and so may slow network transfers. On the other hand, unnecessary whitespace can also incon­spicu­ously mark code for identification purposes, in a manner similar to but less overtly obvious than the way comments in code can. This can be of benefit in proving an infringement of license or copyright claim if the code was blatantly copied and pasted.

#### Preserving whitespace

In XML attribute values, sequences of whitespace characters are treated as a single space when the document is read by a parser. Whitespace in XML element content is not changed in this way by the parser, but an application receiving information from the parser may choose to apply similar rules to element content. An XML document author can use the `xml:space="preserve"` attribute on an element to instruct the parser to discourage the downstream application from altering whitespace in that element's content.

In most HTML elements, a sequence of whitespace characters is treated as a single *inter-word separator*, which may manifest as a single space character when rendering text in a language that normally inserts such space between words. Conforming HTML renderers apply literal whitespace behaviour to certain elements: those inside `<pre>...</pre>` tags, and those where CSS property `white-space` is set to pre or pre-wrap. In these elements, space characters will not be "collapsed" into inter-word separators.

In MediaWiki markup, as well as the `<pre>...</pre>` there is an optional `<poem>...</poem>` tag, which also preserves whitespace. It requires Extension:Poem.

In both XML and HTML, the non-breaking space character, along with other "non-standard" spaces, is not treated as collapsible whitespace.

### File names

Such usage is similar to multiword file names written for operating systems and applications that are confused by embedded space codes—such file names instead use an underscore (_) as a word separator, as_in_this_phrase.

Another such symbol is U+2422 ␢ BLANK SYMBOL, which was used on coding forms in the early years of computer programming. Keypunch operators interpreted it as an "explicit space". It was used in BCDIC, EBCDIC, and ASCII-1963.
