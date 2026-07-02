---
title: "Unicode (part 1/2)"
source: https://en.wikipedia.org/wiki/Unicode
domain: encodings-serialization
license: CC-BY-SA-4.0
tags: unicode, utf-8, character encoding, protobuf, serialization, endianness
fetched: 2026-07-02
part: 1/2
---

# Unicode

**Unicode** (also known as ***The Unicode Standard*** and **TUS**) is a character encoding standard maintained by the Unicode Consortium designed to support the use of text in all of the world's writing systems that can be digitized. Version 17.0 defines 159,801 characters and 172 scripts used in various ordinary, literary, academic and technical contexts.

Unicode has largely supplanted the previous environment of myriad incompatible character sets used within different locales and on different computer architectures. The entire repertoire of these sets, plus many additional characters, were merged into the single Unicode set. Unicode is used to encode the vast majority of text on the Internet, including most web pages, and relevant Unicode support has become a common consideration in contemporary software development. Unicode is ultimately capable of encoding more than 1.1 million characters.

The Unicode character repertoire is synchronized with ISO/IEC 10646, each being code-for-code identical with one another. However, *The Unicode Standard* is more than just a repertoire within which characters are assigned. To aid developers and designers, the standard also provides charts and reference data, as well as annexes explaining concepts germane to various scripts, providing guidance for their implementation. Topics covered by these annexes include character normalization, character composition and decomposition, collation, and directionality.

Unicode encodes 3,790 emoji, with the continued development thereof conducted by the Consortium as a part of the standard. The widespread adoption of Unicode was in large part responsible for the initial popularization of emoji outside of Japan.

Unicode text is processed and stored as binary data using one of several encodings, which define how to translate the standard's abstracted codes for characters into sequences of bytes. *The Unicode Standard* itself defines three encodings: UTF-8, UTF-16, and UTF-32, though several others exist. UTF-8 is the most widely used by a large margin, in part due to its backwards-compatibility with ASCII.


## Origin and development

Unicode was originally designed with the intent of transcending limitations present in all text encodings designed up to that point: each encoding was relied upon for use in its own context, but with no particular expectation of compatibility with any other. Indeed, any two encodings chosen were often totally unworkable when used together, with text encoded in one interpreted as garbage characters by the other. Most encodings had only been designed to facilitate interoperation between a handful of scripts—often primarily between a given script and Latin characters—not between a large number of scripts, and not with all of the scripts supported being treated in a consistent manner.

The philosophy that underpins Unicode seeks to encode the underlying characters—graphemes and grapheme-like units—rather than graphical distinctions considered mere variant glyphs thereof, that are instead best handled by the typeface, through the use of markup, or by some other means. In particularly complex cases, such as the treatment of orthographical variants in Han characters, there is considerable disagreement regarding which differences justify their own encodings, and which are only graphical variants of other characters.

At the most abstract level, Unicode assigns a unique number called a *code point* to each character. Many issues of visual representation—including size, shape, and style—are intended to be up to the discretion of the software actually rendering the text, such as a web browser or word processor. However, partially with the intent of encouraging rapid adoption, the simplicity of this original model has become somewhat more elaborate over time, and various pragmatic concessions have been made over the course of the standard's development.

The first 256 code points mirror the ISO/IEC 8859-1 standard, with the intent of trivializing the conversion of text already written in Western European scripts. To preserve the distinctions made by different legacy encodings, therefore allowing for conversion between them and Unicode without any loss of information, many characters nearly identical to others, in both appearance and intended function, were given distinct code points. For example, the Halfwidth and Fullwidth Forms block encompasses a full semantic duplicate of the Latin alphabet, because legacy CJK encodings contained both "fullwidth" (matching the width of CJK characters) and "halfwidth" (matching ordinary Latin script) characters.

### History

The origins of Unicode can be traced back to the 1980s, to a group of individuals with connections to Xerox's Character Code Standard (XCCS). In 1987, Xerox employee Joe Becker, along with Apple employees Lee Collins and Mark Davis, started investigating the practicalities of creating a universal character set. With additional input from Peter Fenwick and Dave Opstad, Becker published a draft proposal for an "international/multilingual text character encoding system in August 1988, tentatively called Unicode". He explained that "the name 'Unicode' is intended to suggest a unique, unified, universal encoding".

In this document, entitled *Unicode 88*, Becker outlined a scheme using 16-bit characters:

> Unicode is intended to address the need for a workable, reliable world text encoding. Unicode could be roughly described as "wide-body ASCII" that has been stretched to 16 bits to encompass the characters of all the world's living languages. In a properly engineered design, 16 bits per character are more than sufficient for this purpose.

This design decision was made based on the assumption that only scripts and characters in "modern" use would require encoding:

> Unicode gives higher priority to ensuring utility for the future than to preserving past antiquities. Unicode aims in the first instance at the characters published in the modern text (e.g. in the union of all newspapers and magazines printed in the world in 1988), whose number is undoubtedly far below 214 = 16,384. Beyond those modern-use characters, all others may be defined to be obsolete or rare; these are better candidates for private use registration than for congesting the public list of generally useful Unicode.

In early 1989, the Unicode working group expanded to include Ken Whistler and Mike Kernaghan of Metaphor, Karen Smith-Yoshimura and Joan Aliprand of Research Libraries Group, and Glenn Wright of Sun Microsystems. The Research Libraries Group had an existing solution for East Asian character sets, which became one of the inputs to the Unicode character set. In 1990, Michel Suignard and Asmus Freytag of Microsoft and NeXT's Rick McGowan had also joined the group. By the end of 1990, most of the work of remapping existing standards had been completed, and a final review draft of Unicode was ready.

The Unicode Consortium was incorporated in California on 3 January 1991, and the first volume of *The Unicode Standard* was published that October. The second volume, now adding Han ideographs, was published in June 1992.

In 1996, a surrogate character mechanism was implemented in Unicode 2.0, so that Unicode was no longer restricted to 16 bits. This increased the Unicode codespace to over a million code points, which allowed for the encoding of many historic scripts, such as Egyptian hieroglyphs, and thousands of rarely used or obsolete characters that had not been anticipated for inclusion in the standard. Among these characters are various rarely used CJK characters—many mainly being used in proper names, making them far more necessary for a universal encoding than the original Unicode architecture envisioned.

### Unicode Consortium

The Unicode Consortium is a non-profit organization that coordinates Unicode's development. Full members include most of the main computer software and hardware companies (and few others) with any interest in text-processing standards, including Adobe, Apple, Google, IBM, Meta (previously as Facebook), Microsoft, Netflix, and SAP.

Over the years several countries or government agencies have been members of the Unicode Consortium.

The Consortium has the ambitious goal of eventually replacing existing character encoding schemes with Unicode and its standard Unicode Transformation Format (UTF) schemes, as many of the existing schemes are limited in size and scope and are incompatible with multilingual environments.

The **Unicode Bulldog Award** is given to people deemed to be influential in Unicode's development, with recipients including Tatsuo Kobayashi, Thomas Milo, Roozbeh Pournader, Ken Lunde, and Michael Everson.

### Scripts covered

As of September 2025, a total of 172 scripts (alphabets, abugidas and syllabaries) are included in Unicode, covering most major writing systems in use today. There are still scripts that are not yet encoded, particularly those mainly used in historical, liturgical, and academic contexts. Further additions of characters to the already encoded scripts, as well as symbols, in particular for mathematics and music also occur.

### Proposals for adding scripts

The Unicode Roadmap Committee (Michael Everson, Rick McGowan, Ken Whistler, V.S. Umamaheswaran) maintain the list of scripts that are candidates or potential candidates for encoding and their tentative code block assignments on the Unicode Roadmap page of the Unicode Consortium website. For some scripts on the Roadmap, such as Jurchen and Khitan large script, encoding proposals have been made and they are working their way through the approval process. For other scripts, such as Numidian and Rongorongo, no proposal has yet been made, and they await agreement on character repertoire and other details from the user communities involved.

Some modern invented scripts which have not yet been included in Unicode (e.g., Tengwar) or which do not qualify for inclusion in Unicode due to lack of real-world use (e.g., Klingon) are listed in the ConScript Unicode Registry, along with unofficial but widely used private use area code assignments.

There is also a Medieval Unicode Font Initiative focused on special Latin medieval characters. Part of these proposals has been already included in Unicode.

The Script Encoding Initiative (SEI), a project created by Deborah Anderson at the University of California, Berkeley, was founded in 2002 with the goal of funding proposals for scripts not yet encoded in the standard. Now run by Anushah Hossain, SEI has become a major source of proposed additions to the standard in recent years. Although SEI collaborates with the Unicode Consortium and the ISO/IEC 10646 standards process, it operates independently, supporting the technical, linguistic, and historical research needed to prepare formal proposals. SEI maintains a database of scripts that have yet to be encoded in the Unicode Standard on the project's website.

### Versions

The Unicode Consortium together with the ISO have developed a shared repertoire following the initial publication of *The Unicode Standard*: Unicode and the ISO's Universal Coded Character Set (UCS) use identical character names and code points. However, the Unicode versions do differ from their ISO equivalents in two significant ways.

While the UCS is a simple character map, Unicode specifies the rules, algorithms, and properties necessary to achieve interoperability between different platforms and languages. Thus, *The Unicode Standard* includes more information, covering in-depth topics such as bitwise encoding, collation, and rendering. It also provides a comprehensive catalog of character properties, including those needed for supporting bidirectional text, as well as visual charts and reference data sets to aid implementers. Previously, *The Unicode Standard* was sold as a print volume containing the complete core specification, standard annexes, and code charts. However, version 5.0, published in 2006, was the last version printed this way. Starting with version 5.2, only the core specification, published as a print-on-demand paperback, may be purchased. The full text, on the other hand, is published as a free PDF on the Unicode website.

A practical reason for this publication method highlights the second significant difference between the UCS and Unicode—the frequency with which updated versions are released and new characters added. *The Unicode Standard* has regularly released annual expanded versions, occasionally with more than one version released in a calendar year and with rare cases where the scheduled release had to be postponed. For instance, in April 2020, a month after version 13.0 was published, the Unicode Consortium announced they had changed the intended release date for version 14.0, pushing it back six months to September 2021 due to the COVID-19 pandemic.

Thus far, the following versions of *The Unicode Standard* have been published. Update versions, which do not include any changes to character repertoire, are signified by the third number (e.g., "version 4.0.1") and are omitted in the table below.

| Ver­sion | Date | Publication (book, text) | UCS edition | Total | Details |   |
|---|---|---|---|---|---|---|
| Scripts | Characters |   |   |   |   |   |
| 1.0.0 | October 1991 | ISBN 0-201-56788-1 (vol. 1) | —N/a | 24 | 7129 | Initial scripts covered: Arabic, Armenian, Bengali, Bopomofo, Cyrillic, Devanagari, Georgian, Greek and Coptic, Gujarati, Gurmukhi, Hangul, Hebrew, Hiragana, Kannada, Katakana, Lao, Latin, Malayalam, Odia, Tamil, Telugu, Thai, and Tibetan |
| 1.0.1 | June 1992 | ISBN 0-201-60845-6 (vol. 2) | 25 | 28327+21204 −6 | The initial 20,902 CJK Unified Ideographs |   |
| 1.1 | June 1993 | —N/a | ISO/IEC 10646-1:1993 | 24 | 34168+5963 −9 | 33 reclassified as control characters. 4,306 Hangul syllables, Tibetan removed |
| 2.0 | July 1996 | ISBN 0-201-48345-9 | 25 | 38885+11373 −6656 | Original set of Hangul syllables removed, new set of 11,172 Hangul syllables added at new location, Tibetan added back in a new location and with a different character repertoire, Surrogate character mechanism defined, Plane 15 and Plane 16 private use area allocated |   |
| 2.1 | May 1998 | —N/a | 38887+2 | U+20AC € EURO SIGN, U+FFFC ￼ OBJECT REPLACEMENT CHARACTER |   |   |
| 3.0 | September 1999 | ISBN 0-201-61633-5 | ISO/IEC 10646-1:2000 | 38 | 49194+10307 | Cherokee, Geʽez, Khmer, Mongolian, Burmese, Ogham, runes, Sinhala, Syriac, Thaana, Canadian Aboriginal syllabics, and Yi Syllables, Braille patterns |
| 3.1 | March 2001 | —N/a | ISO/IEC 10646-1:2000ISO/IEC 10646-2:2001 | 41 | 94140+44946 | Deseret, Gothic and Old Italic, sets of symbols for Western and Byzantine music, 42,711 additional CJK Unified Ideographs |
| 3.2 | March 2002 | 45 | 95156+1016 | Philippine scripts (Buhid, Hanunoo, Tagalog, and Tagbanwa), mathematical symbols |   |   |
| 4.0 | April 2003 | ISBN 0-321-18578-1 | ISO/IEC 10646:2003 | 52 | 96382+1226 | Cypriot syllabary, Limbu, Linear B, Osmanya, Shavian, Tai Le, and Ugaritic, Hexagram symbols |
| 4.1 | March 2005 | —N/a | 59 | 97655+1273 | Buginese, Glagolitic, Kharosthi, New Tai Lue, Old Persian, Sylheti Nagri, and Tifinagh, Coptic disunified from Greek, ancient Greek numbers and musical symbols, first named character sequences were introduced. |   |
| 5.0 | July 2006 | ISBN 0-321-48091-0 | 64 | 99024+1369 | Balinese, cuneiform, N'Ko, ʼPhags-pa, Phoenician |   |
| 5.1 | April 2008 | —N/a | 75 | 100648+1624 | Carian, Cham, Kayah Li, Lepcha, Lycian, Lydian, Ol Chiki, Rejang, Saurashtra, Sundanese, and Vai, sets of symbols for the Phaistos Disc, Mahjong tiles, Domino tiles, additions to Burmese, Scribal abbreviations, U+1E9E ẞ LATIN CAPITAL LETTER SHARP S |   |
| 5.2 | October 2009 | ISBN 978-1-936213-00-9 | 90 | 107296+6648 | Avestan, Bamum, Gardiner's sign list of Egyptian hieroglyphs, Imperial Aramaic, Inscriptional Pahlavi, Inscriptional Parthian, Javanese, Kaithi, Lisu, Meetei Mayek, Old South Arabian, Old Turkic, Samaritan, Tai Tham and Tai Viet, additional CJK Unified Ideographs, Jamo for Old Hangul, Vedic Sanskrit |   |
| 6.0 | October 2010 | ISBN 978-1-936213-01-6 | ISO/IEC 10646:2010 | 93 | 109384+2088 | Batak, Brahmi, Mandaic, playing card symbols, transport and map symbols, alchemical symbols, emoticons and emoji, additional CJK Unified Ideographs |
| 6.1 | January 2012 | ISBN 978-1-936213-02-3 | ISO/IEC 10646:2012 | 100 | 110116+732 | Chakma, Meroitic cursive, Meroitic hieroglyphs, Miao, Sharada, Sora Sompeng, and Takri |
| 6.2 | September 2012 | ISBN 978-1-936213-07-8 | 110117+1 | U+20BA ₺ TURKISH LIRA SIGN |   |   |
| 6.3 | September 2013 | ISBN 978-1-936213-08-5 | 110122+5 | 5 bidirectional formatting characters |   |   |
| 7.0 | June 2014 | ISBN 978-1-936213-09-2 | 123 | 112956+2834 | Bassa Vah, Caucasian Albanian, Duployan, Elbasan, Grantha, Khojki, Khudawadi, Linear A, Mahajani, Manichaean, Mende Kikakui, Modi, Mro, Nabataean, Old North Arabian, Old Permic, Pahawh Hmong, Palmyrene, Pau Cin Hau, Psalter Pahlavi, Siddham, Tirhuta, Warang Citi, and dingbats |   |
| 8.0 | June 2015 | ISBN 978-1-936213-10-8 | ISO/IEC 10646:2014 | 129 | 120672+7716 | Ahom, Anatolian hieroglyphs, Hatran, Multani, Old Hungarian, SignWriting, additional CJK Unified Ideographs, lowercase letters for Cherokee, 5 emoji skin tone modifiers |
| 9.0 | June 2016 | ISBN 978-1-936213-13-9 | 135 | 128172+7500 | Adlam, Bhaiksuki, Marchen, Newa, Osage, Tangut, 72 emoji |   |
| 10.0 | June 2017 | ISBN 978-1-936213-16-0 | ISO/IEC 10646:2017 | 139 | 136690+8518 | Zanabazar Square, Soyombo, Masaram Gondi, Nüshu, hentaigana, 7,494 CJK Unified Ideographs, 56 emoji, U+20BF ₿ BITCOIN SIGN |
| 11.0 | June 2018 | ISBN 978-1-936213-19-1 | 146 | 137374+684 | Dogra, Georgian Mtavruli capital letters, Gunjala Gondi, Hanifi Rohingya, Indic Siyaq Numbers, Makasar, Medefaidrin, Old Sogdian and Sogdian, Maya numerals, 5 CJK Unified Ideographs, symbols for xiangqi and star ratings, 145 emoji |   |
| 12.0 | March 2019 | ISBN 978-1-936213-22-1 | 150 | 137928+554 | Elymaic, Nandinagari, Nyiakeng Puachue Hmong, Wancho, Miao script, hiragana and katakana small letters, Tamil historic fractions and symbols, Lao letters for Pali, Latin letters for Egyptological and Ugaritic transliteration, hieroglyph format controls, 61 emoji |   |
| 12.1 | May 2019 | ISBN 978-1-936213-25-2 | 137929+1 | U+32FF ㋿ SQUARE ERA NAME REIWA |   |   |
| 13.0 | March 2020 | ISBN 978-1-936213-26-9 | ISO/IEC 10646:2020 | 154 | 143859+5930 | Chorasmian, Dhives Akuru, Khitan small script, Yezidi, 4,969 CJK ideographs, Arabic script additions used to write Hausa, Wolof, and other African languages, additions used to write Hindko and Punjabi in Pakistan, Bopomofo additions used for Cantonese, Creative Commons license symbols, graphic characters for compatibility with teletext and home computer systems, 55 emoji |
| 14.0 | September 2021 | ISBN 978-1-936213-29-0 | 159 | 144697+838 | Toto, Cypro-Minoan, Vithkuqi, Old Uyghur, Tangsa, extended IPA, Arabic script additions for use in languages across Africa and in Iran, Pakistan, Malaysia, Indonesia, Java, and Bosnia, additions for honorifics and Quranic use, additions to support languages in North America, the Philippines, India, and Mongolia, U+20C0 ⃀ SOM SIGN, Znamenny musical notation, 37 emoji |   |
| 15.0 | September 2022 | ISBN 978-1-936213-32-0 | 161 | 149186+4489 | Kawi and Mundari, 20 emoji, 4,192 CJK ideographs, control characters for Egyptian hieroglyphs |   |
| 15.1 | September 2023 | ISBN 978-1-936213-33-7 | 149813+627 | Additional CJK ideographs |   |   |
| 16.0 | September 2024 | ISBN 978-1-936213-34-4 |   | 168 | 154998+5185 | Garay, Gurung Khema, Kirat Rai, Ol Onal, Sunuwar, Todhri, Tulu-Tigalari, 7 emoji, 3,995 Egyptian Hieroglyphs |
| 17.0 | September 2025 | ISBN 978-1-936213-35-1 |   | 172 | 159801+4803 | Beria Erfe, Tai Yo, Sidetic, Tolong Siki, U+20C1 ⃁ SAUDI RIYAL SIGN, 7 emoji, 4,316 CJK unified ideographs |

1. A large amount of documentation for Windows incorrectly uses the term "Unicode" to mean *only* the UTF-16 encoding.
2. The total number of graphic and format characters, excluding private use characters, control characters, noncharacters, and surrogate code points).
3. 2.0 added Amendments 5, 6, and 72.1 added two characters from Amendment 18.
4. 3.2 added Amendment 1.
5. 4.1 added Amendment 15.0 added Amendment 2 as well as four characters from Amendment 35.1 added Amendment 45.2 added Amendments 5 and 6
6. Plus the Indian rupee sign
7. 6.2 added the Turkish lira sign6.3 added five additional characters7.0 added Amendments 1 and 2 as well as the ruble sign
8. Plus Amendment 1, as well as the Lari sign, nine CJK unified ideographs, and 41 emoji; 9.0 added Amendment 2, as well as Adlam, Newa, Japanese TV symbols, and 74 emoji and symbols.
9. Plus 56 emoji, 285 hentaigana characters, and 3 Zanabazar Square characters11.0 added 46 Mtavruli Georgian capital letters, 5 CJK unified ideographs, and 66 emoji12.0 added 62 additional characters.


## Architecture and terminology

### Codespace and code points

*The Unicode Standard* defines a *codespace*: a sequence of integers called *code points* in the range from 0 to 1114111, notated according to the standard as U+0000–U+10FFFF. The codespace is a systematic, architecture-independent representation of *The Unicode Standard*; actual text is processed as binary data via one of several Unicode encodings, such as UTF-8.

In this normative notation, the two-character prefix `U+` always precedes a written code point, and the code points themselves are written as hexadecimal numbers. At least four hexadecimal digits are always written, with leading zeros prepended as needed. For example, the code point U+00F7 ÷ DIVISION SIGN is padded with two leading zeros, but U+13254 𓉔 EGYPTIAN HIEROGLYPH O004 () is not padded.

There are a total of 1112064 valid code points within the codespace. This number arises from the limitations of the UTF-16 character encoding, which can encode the 216 code points in the range U+0000 through U+FFFF except for the 211 code points in the range U+D800 through U+DFFF, which are used as surrogate pairs to encode the 220 code points in the range U+10000 through U+10FFFF.

### Code planes and blocks

The Unicode codespace is divided into 17 *planes*, numbered 0 to 16. Plane 0 is the Basic Multilingual Plane (BMP), and contains the most commonly used characters. All code points in the BMP are accessed as a single code unit in UTF-16 encoding and can be encoded in one, two or three bytes in UTF-8. Code points in planes 1 through 16 (the *supplementary planes*) are accessed as surrogate pairs in UTF-16 and encoded in four bytes in UTF-8.

Within each plane, characters are allocated within named *blocks* of related characters. The size of a block is always a multiple of 16, and is often a multiple of 128, but is otherwise arbitrary. Characters required for a given script may be spread out over several different, potentially disjunct blocks within the codespace.

### General Category property

Each code point is assigned a classification, listed as the code point's General Category property. Here, at the uppermost level code points are categorized as one of Letter, Mark, Number, Punctuation, Symbol, Separator, or Other. Under each category, each code point is then further subcategorized. In most cases, other properties must be used to adequately describe all the characteristics of any given code point.

| General Category (Unicode Character Property) |   |   |   |   |   |
|---|---|---|---|---|---|
| Value | Category Major, minor | Basic type | Character assigned | Count (as of 17.0) | Remarks |
|   |   |   |   |   |   |
| L, Letter; LC, Cased Letter (Lu, Ll, and Lt only) |   |   |   |   |   |
| Lu | Letter, uppercase | Graphic | Character | 1,886 |   |
| Ll | Letter, lowercase | Graphic | Character | 2,283 |   |
| Lt | Letter, titlecase | Graphic | Character | 31 | Digraphs consisting of an uppercase letter followed by a lowercase letter (e.g., ǅ, ǈ, ǋ, and ǲ) |
| Lm | Letter, modifier | Graphic | Character | 410 | A modifier letter |
| Lo | Letter, other | Graphic | Character | 141,062 | An ideograph or a letter in a unicase alphabet |
| M, Mark |   |   |   |   |   |
| Mn | Mark, nonspacing | Graphic | Character | 2,059 |   |
| Mc | Mark, spacing combining | Graphic | Character | 471 |   |
| Me | Mark, enclosing | Graphic | Character | 13 |   |
| N, Number |   |   |   |   |   |
| Nd | Number, decimal digit | Graphic | Character | 770 | All these, and only these, have Numeric Type = De |
| Nl | Number, letter | Graphic | Character | 239 | Numerals composed of letters or letterlike symbols (e.g., Roman numerals) |
| No | Number, other | Graphic | Character | 915 | E.g., vulgar fractions, superscript and subscript digits, vigesimal digits |
| P, Punctuation |   |   |   |   |   |
| Pc | Punctuation, connector | Graphic | Character | 10 | Includes spacing underscore characters such as "_", and other spacing tie characters. Unlike other punctuation characters, these may be classified as "word" characters by regular expression libraries. |
| Pd | Punctuation, dash | Graphic | Character | 27 | Includes several hyphen characters |
| Ps | Punctuation, open | Graphic | Character | 79 | Opening bracket characters |
| Pe | Punctuation, close | Graphic | Character | 77 | Closing bracket characters |
| Pi | Punctuation, initial quote | Graphic | Character | 12 | Opening quotation mark. Does not include the ASCII "neutral" quotation mark. May behave like Ps or Pe depending on usage |
| Pf | Punctuation, final quote | Graphic | Character | 10 | Closing quotation mark. May behave like Ps or Pe depending on usage |
| Po | Punctuation, other | Graphic | Character | 641 |   |
| S, Symbol |   |   |   |   |   |
| Sm | Symbol, math | Graphic | Character | 960 | Mathematical symbols (e.g., +, −, =, ×, ÷, √, ∊, ≠). Does not include parentheses and brackets, which are in categories Ps and Pe. Also does not include !, *, -, or /, which despite frequent use as mathematical operators, are primarily considered to be "punctuation". |
| Sc | Symbol, currency | Graphic | Character | 64 | Currency symbols |
| Sk | Symbol, modifier | Graphic | Character | 125 |   |
| So | Symbol, other | Graphic | Character | 7,468 |   |
| Z, Separator |   |   |   |   |   |
| Zs | Separator, space | Graphic | Character | 17 | Includes the space, but not TAB, CR, or LF, which are Cc |
| Zl | Separator, line | Format | Character | 1 | Only U+2028 LINE SEPARATOR (LSEP) |
| Zp | Separator, paragraph | Format | Character | 1 | Only U+2029 PARAGRAPH SEPARATOR (PSEP) |
| C, Other |   |   |   |   |   |
| Cc | Other, control | Control | Character | 65 (will never change) | No name, <control> |
| Cf | Other, format | Format | Character | 170 | Includes the soft hyphen, joining control characters (ZWNJ and ZWJ), control characters to support bidirectional text, and language tag characters |
| Cs | Other, surrogate | Surrogate | Not (only used in UTF-16) | 2,048 (will never change) | No name, <surrogate> |
| Co | Other, private use | Private-use | Character (but no interpretation specified) | 137,468 total (will never change) (6,400 in BMP, 131,068 in Planes 15–16) | No name, <private-use> |
| Cn | Other, not assigned | Noncharacter | Not | 66 (will not change unless the range of Unicode code points is expanded) | No name, <noncharacter> |
| Reserved | Not | 814,664 | No name, <reserved> |   |   |
| *"Table 4-4: General Category". *The Unicode Standard*. Unicode Consortium. September 2025.* *"Table 2-3: Types of code points". *The Unicode Standard*. Unicode Consortium. September 2025.* *"DerivedGeneralCategory.txt". The Unicode Consortium. 2025-07-24.* *"5.7.1 General Category Values". *UTR #44: Unicode Character Database*. Unicode Consortium. 2024-08-27.* Unicode Character Encoding Stability Policies: Property Value Stability Stability policy: Some gc groups will never change. gc=Nd corresponds with Numeric Type=De (decimal). *"Annex C: Compatibility Properties (§ word)". *Unicode Regular Expressions*. Version 23. Unicode Consortium. 2022-02-08. Unicode Technical Standard #18.* *"Table 4-9: Construction of Code Point Labels". *The Unicode Standard*. Unicode Consortium. September 2025.* A *Code Point Label* may be used to identify a nameless code point. E.g. <control-*hhhh*>, <control-0088>. The Name remains blank, which can prevent inadvertently replacing, in documentation, a Control Name with a true Control code. Unicode also uses <not a character> for <noncharacter>. |   |   |   |   |   |

The 1024 points in the range U+D800–U+DBFF are known as *high-surrogate* code points, and code points in the range U+DC00–U+DFFF (1024 code points) are known as *low-surrogate* code points. A high-surrogate code point followed by a low-surrogate code point forms a *surrogate pair* in UTF-16 in order to represent code points greater than U+FFFF. In principle, these code points cannot otherwise be used, though in practice this rule is often ignored, especially when not using UTF-16.

A small set of code points are guaranteed never to be assigned to characters, although third-parties may make independent use of them at their discretion. There are 66 of these *noncharacters*: U+FDD0–U+FDEF and the last two code points in each of the 17 planes (e.g. U+FFFE, U+FFFF, U+1FFFE, U+1FFFF, ..., U+10FFFE, U+10FFFF). The set of noncharacters is stable, and no new noncharacters will ever be defined. Like surrogates, the rule that these cannot be used is often ignored, although the operation of the byte order mark assumes that U+FFFE will never be the first code point in a text. The exclusion of surrogates and noncharacters leaves 1111998 code points available for use.

*Private use* code points are considered to be assigned, but they intentionally have no interpretation specified by *The Unicode Standard* such that any interchange of such code points requires an independent agreement between the sender and receiver as to their interpretation. There are three private use areas in the Unicode codespace:

- Private Use Area: U+E000–U+F8FF (6400 characters),
- Supplementary Private Use Area-A: U+F0000–U+FFFFD (65534 characters),
- Supplementary Private Use Area-B: U+100000–U+10FFFD (65534 characters).

*Graphic* characters are those defined by *The Unicode Standard* to have particular semantics, either having a visible glyph shape or representing a visible space. As of Unicode 17.0, there are 159629 graphic characters.

*Format* characters are characters that do not have a visible appearance but may have an effect on the appearance or behavior of neighboring characters. For example, U+200C ZERO WIDTH NON-JOINER and U+200D ZERO WIDTH JOINER may be used to change the default shaping behavior of adjacent characters (e.g. to inhibit ligatures or request ligature formation). There are 172 format characters in Unicode 17.0.

65 code points, the ranges U+0000–U+001F and U+007F–U+009F, are reserved as *control codes*, corresponding to the C0 and C1 control codes as defined in ISO/IEC 6429. U+0009 TAB, U+000A LINE FEED, and U+000D CARRIAGE RETURN are widely used in texts using Unicode. In a phenomenon known as mojibake, the C1 code points are improperly decoded according to the Windows-1252 codepage, previously widely used in Western European contexts.

Together, graphic, format, control code, and private use characters are collectively referred to as *assigned characters*. *Reserved* code points are those code points that are valid and available for use, but have not yet been assigned. As of Unicode 17.0, there are 814664 reserved code points.

### Abstract characters

The set of graphic and format characters defined by Unicode does not correspond directly to the repertoire of *abstract characters* representable under Unicode. Unicode encodes characters by associating an abstract character with a particular code point. However, not all abstract characters are encoded as a single Unicode character, and some abstract characters may be represented in Unicode by a sequence of two or more characters. For example, a Latin small letter "i" with an ogonek, a dot above, and an acute accent, which is required in Lithuanian, is represented by the character sequence U+012F; U+0307; U+0301. Unicode maintains a list of uniquely named character sequences for abstract characters that are not directly encoded in Unicode.

All assigned characters have a unique and immutable name by which they are identified. This immutability has been guaranteed since version 2.0 of *The Unicode Standard* by its Name Stability policy. In cases where a name is seriously defective and misleading, or has a serious typographical error, a formal **alias** may be defined that applications are encouraged to use in place of the official character name. For example, U+A015 ꀕ YI SYLLABLE WU has the formal alias YI SYLLABLE ITERATION MARK, and U+FE18 ︘ PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET (sic) has the formal alias PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRA**CK**ET.

### Precomposed vis-à-vis composite characters

Unicode includes a mechanism for modifying characters that greatly extends the supported repertoire of glyphs. This covers the use of combining diacritical marks that may be added after the base character by the user. Multiple combining diacritics may be simultaneously applied to the same character. Unicode also contains precomposed versions of most letter/diacritic combinations in normal use. These make the conversion to and from legacy encodings simpler, and allow applications to use Unicode as an internal text format without having to implement combining characters. For example, `é` can be represented in Unicode as U+0065 e LATIN SMALL LETTER E followed by U+0301 ◌́ COMBINING ACUTE ACCENT, and equivalently as the precomposed character U+00E9 é LATIN SMALL LETTER E WITH ACUTE. Thus, users often have multiple equivalent ways of encoding the same character. The mechanism of canonical equivalence within *The Unicode Standard* ensures the practical interchangeability of these equivalent encodings.

An example of this arises with the Korean alphabet Hangul: Unicode provides a mechanism for composing Hangul syllables from their individual Hangul Jamo subcomponents. However, it also provides 11172 combinations of precomposed syllables made from the most common jamo.

CJK characters presently only have codes for uncomposable radicals and precomposed forms. Most Han characters have either been intentionally composed from, or reconstructed as compositions of, simpler orthographic elements called radicals, so in principle Unicode could have enabled their composition as it did with Hangul. While this could have greatly reduced the number of required code points, as well as allowing the algorithmic synthesis of many arbitrary new characters, the complexities of character etymologies and the post-hoc nature of radical systems add immense complexity to the proposal. Indeed, attempts to design CJK encodings on the basis of composing radicals have been met with difficulties resulting from the reality that Chinese characters do not decompose as simply or as regularly as Hangul does.

The CJK Radicals Supplement block is assigned to the range U+2E80–U+2EFF, and the Kangxi radicals are assigned to U+2F00–U+2FDF. The Ideographic Description Sequences block covers the range U+2FF0–U+2FFB, but *The Unicode Standard* warns against using its characters as an alternate representation for characters encoded elsewhere:

> This process is different from a formal *encoding* of an ideograph. There is no canonical description of unencoded ideographs; there is no semantic assigned to described ideographs; there is no equivalence defined for described ideographs. Conceptually, ideographic descriptions are more akin to the English phrase "an 'e' with an acute accent on it" than to the character sequence <U+0065, U+0301>.

### Ligatures

The

Devanāgarī

ddhrya

-ligature (द् + ध् + र् + य = द्ध्र्य) of JanaSanskritSans

The

Arabic

lām

-

alif

ligature (

ل

‎+‎

ا

‎=‎

لا

)

Many scripts, including Arabic and Devanāgarī, have special orthographic rules that require certain combinations of letterforms to be combined into special ligature forms. The rules governing ligature formation can be quite complex, requiring special script-shaping technologies such as ACE (Arabic Calligraphic Engine by DecoType in the 1980s and used to generate all the Arabic examples in the printed editions of *The Unicode Standard*), which became the proof of concept for OpenType (by Adobe and Microsoft), Graphite (by SIL International), or AAT (by Apple).

Instructions are also embedded in fonts to tell the operating system how to properly output different character sequences. A simple solution to the placement of combining marks or diacritics is assigning the marks a width of zero and placing the glyph itself to the left or right of the left sidebearing (depending on the direction of the script they are intended to be used with). A mark handled this way will appear over whatever character precedes it, but will not adjust its position relative to the width or height of the base glyph; it may be visually awkward and it may overlap some glyphs. Real stacking is impossible but can be approximated in limited cases (for example, Thai top-combining vowels and tone marks can just be at different heights to start with). Generally, this approach is only effective in monospaced fonts but may be used as a fallback rendering method when more complex methods fail.

### Standardized subsets

Several subsets of Unicode are standardized: Microsoft Windows since Windows NT 4.0 supports WGL-4 with 657 characters, which is considered to support all contemporary European languages using the Latin, Greek, or Cyrillic script. Other standardized subsets of Unicode include the Multilingual European Subsets: MES-1 (Latin scripts only; 335 characters), MES-2 (Latin, Greek, and Cyrillic; 1062 characters) and MES-3A & MES-3B (two larger subsets, not shown here). MES-2 includes every character in MES-1 and WGL-4.

The standard DIN 91379 specifies a subset of Unicode letters, special characters, and sequences of letters and diacritic signs to allow the correct representation of names and to simplify data exchange in Europe. This standard supports all of the official languages of all European Union countries, as well as the German minority languages and the official languages of Iceland, Liechtenstein, Norway, and Switzerland. To allow the transliteration of names in other writing systems to the Latin script according to the relevant ISO standards, all necessary combinations of base letters and diacritic signs are provided.

| Row | Cells | Range(s) |
|---|---|---|
| 00 | ***20–7E*** | Basic Latin (00–7F) |
| ***A0–FF*** | Latin-1 Supplement (80–FF) |   |
| 01 | ***00–13,* 14–15, *16–2B,* 2C–2D, *2E–4D,* 4E–4F, *50–7E,* 7F** | Latin Extended-A (00–7F) |
| 8F, **92,** B7, DE-EF, **FA–FF** | Latin Extended-B (80–FF ...) |   |
| 02 | 18–1B, 1E–1F | Latin Extended-B (... 00–4F) |
| 59, 7C, 92 | IPA Extensions (50–AF) |   |
| BB–BD, **C6, *C7,* C9,** D6, ***D8–DB,* DC, *DD,*** DF, EE | Spacing Modifier Letters (B0–FF) |   |
| 03 | 74–75, 7A, 7E, **84–8A, 8C, 8E–A1, A3–CE,** D7, DA–E1 | Greek (70–FF) |
| 04 | **00–5F, 90–91,** 92–C4, C7–C8, CB–CC, D0–EB, EE–F5, F8–F9 | Cyrillic (00–FF) |
| 1E | 02–03, 0A–0B, 1E–1F, 40–41, 56–57, 60–61, 6A–6B, **80–85,** 9B, **F2–F3** | Latin Extended Additional (00–FF) |
| 1F | 00–15, 18–1D, 20–45, 48–4D, 50–57, 59, 5B, 5D, 5F–7D, 80–B4, B6–C4, C6–D3, D6–DB, DD–EF, F2–F4, F6–FE | Greek Extended (00–FF) |
| 20 | **13–14, *15,* 17, *18–19,* 1A–1B, *1C–1D,* 1E, 20–22, 26, 30, 32–33, 39–3A, 3C, 3E, 44,** 4A | General Punctuation (00–6F) |
| **7F**, 82 | Superscripts and Subscripts (70–9F) |   |
| **A3–A4, A7, *AC,*** AF | Currency Symbols (A0–CF) |   |
| 21 | **05, 13, 16, *22, 26,* 2E** | Letterlike Symbols (00–4F) |
| ***5B–5E*** | Number Forms (50–8F) |   |
| ***90–93,* 94–95, A8** | Arrows (90–FF) |   |
| 22 | 00, **02,** 03, **06,** 08–09, **0F, 11–12, 15, 19–1A, 1E–1F,** 27–28, **29,** 2A, **2B, 48,** 59, **60–61, 64–65,** 82–83, 95, 97 | Mathematical Operators (00–FF) |
| 23 | **02, 0A, 20–21,** 29–2A | Miscellaneous Technical (00–FF) |
| 25 | **00, 02, 0C, 10, 14, 18, 1C, 24, 2C, 34, 3C, 50–6C** | Box Drawing (00–7F) |
| **80, 84, 88, 8C, 90–93** | Block Elements (80–9F) |   |
| **A0–A1, AA–AC, B2, BA, BC, C4, CA–CB, CF, D8–D9, E6** | Geometric Shapes (A0–FF) |   |
| 26 | **3A–3C, 40, 42, 60, 63, 65–66, *6A,* 6B** | Miscellaneous Symbols (00–FF) |
| F0 | (01–02) | Private Use Area (00–FF ...) |
| FB | **01–02** | Alphabetic Presentation Forms (00–4F) |
| FF | FD | Specials |

Rendering software that cannot process a Unicode character appropriately often displays it as an open rectangle, or as U+FFFD to indicate the position of the unrecognized character. Some systems have made attempts to provide more information about such characters. Apple's Last Resort font will display a substitute glyph indicating the Unicode range of the character, and the SIL International's Unicode fallback font will display a box showing the hexadecimal scalar value of the character.

### Mapping and encodings

Several mechanisms have been specified for storing a series of code points as a series of bytes.

Unicode defines two mapping methods: the **Unicode Transformation Format** (UTF) encodings, and the **Universal Coded Character Set** (UCS) encodings. An encoding maps (possibly a subset of) the range of Unicode *code points* to sequences of values in some fixed-size range, termed *code units*. All UTF encodings map code points to a unique sequence of bytes. The numbers in the names of the encodings indicate the number of bits per code unit (for UTF encodings) or the number of bytes per code unit (for UCS encodings and UTF-1). UTF-8 and UTF-16 are the most commonly used encodings. UCS-2 is an obsolete subset of UTF-16; UCS-4 and UTF-32 are functionally equivalent.

UTF encodings include:

- UTF-8, which uses one to four 8-bit units per code point, and has maximal compatibility with ASCII
- UTF-16, which uses one 16-bit unit per code point below U+010000, and a surrogate pair of two 16-bit units per code point in the range U+010000 to U+10FFFF
- UTF-32, which uses one 32-bit unit per code point
- UTF-EBCDIC, not specified as part of *The Unicode Standard*, which uses one to five 8-bit units per code point, intended to maximize compatibility with EBCDIC

UTF-8 uses one to four 8-bit units (*bytes*) per code point and, being compact for Latin scripts and ASCII-compatible, provides the de facto standard encoding for the interchange of Unicode text. It is used by FreeBSD and most recent Linux distributions as a direct replacement for legacy encodings in general text handling.

The UCS-2 and UTF-16 encodings specify the Unicode byte order mark (BOM) for use at the beginnings of text files, which may be used for byte-order detection (or byte endianness detection). The BOM, encoded as U+FEFF ZERO WIDTH NO-BREAK SPACE, has the important property of unambiguity on byte reorder, regardless of the Unicode encoding used; U+FFFE (the result of byte-swapping U+FEFF) does not equate to a legal character, and U+FEFF in places other than the beginning of text conveys the zero-width non-break space.

The same character converted to UTF-8 becomes the byte sequence `EF BB BF`. *The Unicode Standard* allows the BOM "can serve as a signature for UTF-8 encoded text where the character set is unmarked". Some software developers have adopted it for other encodings, including UTF-8, in an attempt to distinguish UTF-8 from local 8-bit code pages. However RFC 3629, the UTF-8 standard, recommends that byte order marks be forbidden in protocols using UTF-8, but discusses the cases where this may not be possible. In addition, the large restriction on possible patterns in UTF-8 (for instance there cannot be any lone bytes with the high bit set) means that it should be possible to distinguish UTF-8 from other character encodings without relying on the BOM.

In UTF-32 and UCS-4, one 32-bit code unit serves as a fairly direct representation of any character's code point (although the endianness, which varies across different platforms, affects how the code unit manifests as a byte sequence). In the other encodings, each code point may be represented by a variable number of code units. UTF-32 is widely used as an internal representation of text in programs (as opposed to stored or transmitted text), since every Unix operating system that uses the GCC compilers to generate software uses it as the standard "wide character" encoding. Recent versions of the Python programming language (beginning with 2.2) may also be configured to use UTF-32 as the representation for Unicode strings, effectively disseminating such encoding in high-level coded software.

Punycode, another encoding form, enables the encoding of Unicode strings into the limited character set supported by the ASCII-based Domain Name System (DNS). The encoding is used as part of IDNA, which is a system enabling the use of Internationalized Domain Names in all scripts that are supported by Unicode. Earlier and now historical proposals include UTF-5 and UTF-6.

GB18030 is another encoding form for Unicode, from the Standardization Administration of China. It is the official character set of the People's Republic of China (PRC). BOCU-1 and SCSU are Unicode compression schemes. The April Fools' Day RFC of 2005 specified two parody UTF encodings, UTF-9 and UTF-18.
