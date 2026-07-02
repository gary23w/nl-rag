---
title: "Unicode (part 2/2)"
source: https://en.wikipedia.org/wiki/Unicode
domain: unicode-bidi-web
license: CC-BY-SA-4.0
tags: bidirectional text, unicode bidi property, right-to-left script, writing mode direction
fetched: 2026-07-02
part: 2/2
---

## Adoption

Unicode, in the form of UTF-8, has been the most common encoding for the World Wide Web since 2008. It has near-universal adoption, and much of the non-UTF-8 content is found in other Unicode encodings, e.g. UTF-16. As of 2024, UTF-8 accounts for on average 98.3% of all web pages (and 983 of the top 1,000 highest-ranked web pages). Although many pages only use ASCII characters to display content, UTF-8 was designed with 8-bit ASCII as a subset and almost no websites now declare their encoding to only be ASCII instead of UTF-8. Over a third of the languages tracked have 100% UTF-8 use.

All internet protocols maintained by Internet Engineering Task Force, e.g. File Transfer Protocol (FTP), have required support for UTF-8 since the publication of RFC 2277 in 1998, which specified that all IETF protocols "MUST be able to use the UTF-8 charset".

### Operating systems

Unicode has become the dominant scheme for the internal processing and storage of text. Although a great deal of text is still stored in legacy encodings, Unicode is used almost exclusively for building new information processing systems. Early adopters tended to use UCS-2 (the fixed-length two-byte obsolete precursor to UTF-16) and later moved to UTF-16 (the variable-length current standard), as this was the least disruptive way to add support for non-BMP characters. The best known such system is Windows NT (and its descendants, 2000, XP, Vista, 7, 8, 10, and 11), which uses UTF-16 as the sole internal character encoding. The Java and .NET bytecode environments, macOS, and KDE also use it for internal representation. Partial support for Unicode can be installed on Windows 9x through the Microsoft Layer for Unicode.

UTF-8 (originally developed for Plan 9) has become the main storage encoding on most Unix-like operating systems (though others are also used by some libraries) because it is a relatively easy replacement for traditional extended ASCII character sets. UTF-8 is also the most common Unicode encoding used in HTML documents on the World Wide Web.

Multilingual text-rendering engines which use Unicode include Uniscribe and DirectWrite for Microsoft Windows, ATSUI and Core Text for macOS, and Pango for GTK+ and the GNOME desktop.

### Input methods

Because keyboard layouts cannot have simple key combinations for all characters, several operating systems provide alternative input methods that allow access to the entire repertoire.

ISO/IEC 14755, which standardises methods for entering Unicode characters from their code points, specifies several methods. There is the *Basic method*, where a *beginning sequence* is followed by the hexadecimal representation of the code point and the *ending sequence*. There is also a *screen-selection entry method* specified, where the characters are listed in a table on a screen, such as with a character map program.

Online tools for finding the code point for a known character include Unicode Lookup by Jonathan Hedley and Shapecatcher by Benjamin Milde. In Unicode Lookup, one enters a search key (e.g. "fractions"), and a list of corresponding characters with their code points is returned. In Shapecatcher, based on Shape context, one draws the character in a box and a list of characters approximating the drawing, with their code points, is returned.

### Email

MIME defines two different mechanisms for encoding non-ASCII characters in email, depending on whether the characters are in email headers (such as the "Subject:"), or in the text body of the message; in both cases, the original character set is identified as well as a transfer encoding. For email transmission of Unicode, the UTF-8 character set and the Base64 or the Quoted-printable transfer encoding are recommended, depending on whether much of the message consists of ASCII characters. The details of the two different mechanisms are specified in the MIME standards and generally are hidden from users of email software.

The IETF has defined a framework for internationalized email using UTF-8, and has updated several protocols in accordance with that framework.

The adoption of Unicode in email has been very slow. Some East Asian text is still encoded in encodings such as ISO-2022, and some devices, such as mobile phones, still cannot correctly handle Unicode data. Support has been improving, however. Many major free mail providers such as Yahoo! Mail, Gmail, and Outlook.com support it.

### Web

All W3C recommendations have used Unicode as their *document character set* since HTML 4.0. Web browsers have supported Unicode, especially UTF-8, for many years. There used to be display problems resulting primarily from font related issues; e.g. v6 and older of Microsoft Internet Explorer did not render many code points unless explicitly told to use a font that contains them.

Although syntax rules may affect the order in which characters are allowed to appear, XML (including XHTML) documents, by definition, comprise characters from most of the Unicode code points, with the exception of:

- FFFE or FFFF.
- most of the C0 control codes,
- the permanently unassigned code points D800–DFFF,

HTML characters manifest either directly as bytes according to the document's encoding, if the encoding supports them, or users may write them as numeric character references based on the character's Unicode code point. For example, the references `&#916;`, `&#1049;`, `&#1511;`, `&#1605;`, `&#3671;`, `&#12354;`, `&#21494;`, `&#33865;`, and `&#47568;` (or the same numeric values expressed in hexadecimal, with `&#x` as the prefix) should display on all browsers as Δ, Й, ק ,م, ๗, あ, 叶, 葉, and 말.

When specifying URIs, for example as URLs in HTTP requests, non-ASCII characters must be percent-encoded.

### Fonts

Unicode is not in principle concerned with fonts *per se*, seeing them as implementation choices. Any given character may have many allographs, from the more common bold, italic and base letterforms to complex decorative styles. A font is "Unicode compliant" if the glyphs in the font can be accessed using code points defined in *The Unicode Standard*. The standard does not specify a minimum number of characters that must be included in the font; some fonts have quite a small repertoire.

Free and retail fonts based on Unicode are widely available, since TrueType and OpenType support Unicode (and Web Open Font Format (WOFF and WOFF2) is based on those). These font formats map Unicode code points to glyphs, but OpenType and TrueType font files are restricted to 65,535 glyphs. Collection files provide a "gap mode" mechanism for overcoming this limit in a single font file. (Each font within the collection still has the 65,535 limit, however.) A TrueType Collection file would typically have a file extension of ".ttc".

Thousands of fonts exist on the market, but fewer than a dozen fonts—sometimes described as "pan-Unicode" fonts—attempt to support the majority of Unicode's character repertoire. Instead, Unicode-based fonts typically focus on supporting only basic ASCII and particular scripts or sets of characters or symbols. Several reasons justify this approach: applications and documents rarely need to render characters from more than one or two writing systems; fonts tend to demand resources in computing environments; and operating systems and applications show increasing intelligence in regard to obtaining glyph information from separate font files as needed, i.e., font substitution. Furthermore, designing a consistent set of rendering instructions for tens of thousands of glyphs constitutes a monumental task; such a venture passes the point of diminishing returns for most typefaces.

### Newlines

Unicode partially addresses the newline problem that occurs when trying to read a text file on different platforms. Unicode defines a large number of characters that conforming applications should recognize as line terminators.

In terms of the newline, Unicode introduced U+2028 LINE SEPARATOR and U+2029 PARAGRAPH SEPARATOR. This was an attempt to provide a Unicode solution to encoding paragraphs and lines semantically, potentially replacing all of the various platform solutions. In doing so, Unicode does provide a way around the historical platform-dependent solutions. Nonetheless, few if any Unicode solutions have adopted these Unicode line and paragraph separators as the sole canonical line ending characters. However, a common approach to solving this issue is through newline normalization. This is achieved with the Cocoa text system in macOS and also with W3C XML and HTML recommendations. In this approach, every possible newline character is converted internally to a common newline (which one does not really matter since it is an internal operation just for rendering). In other words, the text system can correctly treat the character as a newline, regardless of the input's actual encoding.


## Issues

### Character unification

#### Han unification

The Ideographic Research Group (IRG) is tasked with advising the Consortium and ISO regarding Han unification, or Unihan, especially the further addition of CJK unified and compatibility ideographs to the repertoire. The IRG is composed of experts from each region that has historically used Chinese characters. However, despite the deliberation within the committee, Han unification has consistently been one of the most contested aspects of *The Unicode Standard* since the genesis of the project.

Existing character set standards such as the Japanese JIS X 0208 (encoded by Shift JIS) defined unification criteria, meaning rules for determining when a variant Chinese character is to be considered a handwriting/font difference (and thus unified), versus a spelling difference (to be encoded separately). Unicode's character model for CJK characters was based on the unification criteria used by JIS X 0208, as well as those developed by the Association for a Common Chinese Code in China.

Due to the standard's principle of encoding semantic instead of stylistic variants, Unicode has received criticism for not assigning code points to certain rare and archaic kanji variants, possibly complicating processing of ancient and uncommon Japanese names. Since it places particular emphasis on Chinese, Japanese and Korean sharing many characters in common, Han unification is also sometimes perceived as treating the three as the same thing. Regional differences in the expected forms of characters, in terms of typographical conventions and curricula for handwriting, do not always fall along language boundaries: although Hong Kong and Taiwan both write Chinese languages using Traditional Chinese characters, the preferred forms of characters differ between Hong Kong and Taiwan in some cases.

Less-frequently-used alternative encodings exist, often predating Unicode, with character models differing from this paradigm, aimed at preserving the various stylistic differences between regional and/or nonstandard character forms. One example is the TRON Code favored by some users for handling historical Japanese text, though not widely adopted among the Japanese public. Another is the CCCII encoding adopted by library systems in Hong Kong, Taiwan and the United States. These have their own drawbacks in general use, leading to the Big5 encoding (introduced in 1984, four years after CCCII) having become more common than CCCII outside of library systems. Although work at Apple based on Research Libraries Group's CJK Thesaurus, which was used to maintain the EACC variant of CCCII, was one of the direct predecessors of Unicode's Unihan set, Unicode adopted the JIS-style unification model.

The earliest version of Unicode had a repertoire of fewer than 21,000 Han characters, largely limited to those in relatively common modern usage. As of version 17.0, the standard now encodes more than 101,000 Han characters, and work is continuing to add thousands more—largely historical and dialectal variant characters used throughout the Sinosphere.

Modern typefaces provide a means to address some of the practical issues in depicting unified Han characters with various regional graphical representations. The 'locl' OpenType table allows a renderer to select a different glyph for each code point based on the text locale. The Unicode variation sequences can also provide in-text annotations for a desired glyph selection; this requires registration of the specific variant in the Ideographic Variation Database.

#### Italic or cursive characters in Cyrillic

If the appropriate glyphs for characters in the same script differ only in the italic, Unicode has generally unified them, as can be seen in the comparison among a set of seven characters' italic glyphs as typically appearing in Russian, traditional Bulgarian, Macedonian, and Serbian texts at right, meaning that the differences are displayed through smart font technology or manually changing fonts. The same OpenType 'locl' technique is used.

#### Localised case pairs

For use in the Turkish alphabet and Azeri alphabet, Unicode includes a separate dotless lowercase I (ı) and a dotted uppercase I (İ). However, the usual ASCII letters are used for the lowercase dotted i and the uppercase dotless I, matching how they are handled in the earlier ISO 8859-9. As such, case-insensitive comparisons for those languages have to use different rules than case-insensitive comparisons for other languages using the Latin script. This can have security implications if, for example, sanitization code or access control relies on case-insensitive comparison.

By contrast, the Icelandic eth (ð), the barred D (đ) and the retroflex D (ɖ), which usually look the same in uppercase (Đ), are given the opposite treatment, and encoded separately in both letter-cases (in contrast to the earlier ISO 6937, which unifies the uppercase forms). Although it allows for case-insensitive comparison without needing to know the language of the text, this approach also has issues, requiring security measures relating to homoglyph attacks.

#### Diacritics on lowercase I

Whether the lowercase letter I is expected to retain its tittle when a diacritic applies also depends on local conventions.

### Security

Unicode has a large number of homoglyphs, many of which look very similar or identical to ASCII letters. Substitution of these can make an identifier or URL that looks correct, but directs to a different location than expected. Additionally, homoglyphs can also be used for manipulating the output of natural language processing (NLP) systems. Mitigation requires disallowing these characters, displaying them differently, or requiring that they resolve to the same identifier; all of this is complicated due to the huge and constantly changing set of characters.

A security advisory was released in 2021 by two researchers, one from the University of Cambridge and the other from the University of Edinburgh, in which they assert that the BiDi marks can be used to make large sections of code do something different from what they appear to do. The problem was named "Trojan Source". In response, code editors started highlighting marks to indicate forced text-direction changes.

The UTF-8 and UTF-16 encodings do not accept all possible sequences of code units. Implementations vary in what they do when reading an invalid sequence, which has led to security bugs.

### Mapping to legacy character sets

Unicode was designed to provide code-point-by-code-point round-trip format conversion to and from any preexisting character encodings, so that text files in older character sets can be converted to Unicode and then back and get back the same file, without employing context-dependent interpretation. That has meant that inconsistent legacy architectures, such as combining diacritics and precomposed characters, both exist in Unicode, giving more than one method of representing some text. This is most pronounced in the three different encoding forms for Korean Hangul. Since version 3.0, any precomposed characters that can be represented by a combined sequence of already existing characters can no longer be added to the standard to preserve interoperability between software using different versions of Unicode.

Injective mappings must be provided between characters in existing legacy character sets and characters in Unicode to facilitate conversion to Unicode and allow interoperability with legacy software. Lack of consistency in various mappings between earlier Japanese encodings such as Shift-JIS or EUC-JP and Unicode led to round-trip format conversion mismatches, particularly the mapping of the character JIS X 0208 '～' (1-33, WAVE DASH), heavily used in legacy database data, to either U+FF5E ～ FULLWIDTH TILDE (in Microsoft Windows) or U+301C 〜 WAVE DASH (other vendors).

Some Japanese computer programmers objected to Unicode because it requires them to separate the use of U+005C \ REVERSE SOLIDUS (backslash) and U+00A5 ¥ YEN SIGN, which was mapped to 0x5C in JIS X 0201, and a lot of legacy code exists with this usage. (This encoding also replaces tilde '~' 0x7E with macron '¯', now 0xAF.) The separation of these characters exists in ISO 8859-1, from long before Unicode.

### Indic scripts

Indic scripts such as Tamil and Devanagari are each allocated only 128 code points, matching the ISCII standard. The correct rendering of Unicode Indic text requires transforming the stored logical order characters into visual order and the forming of ligatures (also known as conjuncts) out of components. Some local scholars argued in favor of assignments of Unicode code points to these ligatures, going against the practice for other writing systems, though Unicode contains some Arabic and other ligatures for backward compatibility purposes only. Encoding of any new ligatures in Unicode will not happen, in part, because the set of ligatures is font-dependent, and Unicode is an encoding independent of font variations. The same kind of issue arose for the Tibetan script in 2003 when the Standardization Administration of China proposed encoding 956 precomposed Tibetan syllables, but these were rejected for encoding by the relevant ISO committee (ISO/IEC JTC 1/SC 2).

Thai alphabet support has been criticized for its ordering of Thai characters. The vowels เ, แ, โ, ใ, ไ that are written to the left of the preceding consonant are in visual order instead of phonetic order, unlike the Unicode representations of other Indic scripts. This complication is due to Unicode inheriting the Thai Industrial Standard 620, which worked in the same way, and was the way in which Thai had always been written on keyboards. This ordering problem complicates the Unicode collation process slightly, requiring table lookups to reorder Thai characters for collation. Even if Unicode had adopted encoding according to spoken order, it would still be problematic to collate words in dictionary order. E.g., the word แสดง [sa dɛːŋ] "perform" starts with a consonant cluster "สด" (with an inherent vowel for the consonant "ส"), the vowel แ-, in spoken order would come after the ด, but in a dictionary, the word is collated as it is written, with the vowel following the ส.

### Combining characters

Characters with diacritical marks can generally be represented either as a single precomposed character or as a decomposed sequence of a base letter plus one or more non-spacing marks. For example, ḗ (precomposed e with macron and acute above) and ḗ (e followed by the combining macron above and combining acute above) should be rendered identically, both appearing as an e with a macron (◌̄) and acute accent (◌́), but in practice, their appearance may vary depending upon what rendering engine and fonts are being used to display the characters. Similarly, underdots, as needed in the romanization of Indic languages, will often be placed incorrectly. Unicode characters that map to precomposed glyphs can be used in many cases, thus avoiding the problem, but where no precomposed character has been encoded, the problem can often be solved by using a specialist Unicode font such as Charis SIL that uses Graphite, OpenType ('gsub'), or AAT technologies for advanced rendering features.

### Anomalies

*The Unicode Standard* has imposed rules intended to guarantee stability. Depending on the strictness of a rule, a change can be prohibited or allowed. For example, a "name" given to a code point cannot and will not change. But a "script" property is more flexible, by Unicode's own rules. In version 2.0, Unicode changed many code point "names" from version 1. At the same moment, Unicode stated that, thenceforth, an assigned name to a code point would never change. This implies that when mistakes are published, these mistakes cannot be corrected, even if they are trivial (as happened in one instance with the spelling BRAKCET for BRACKET in a character name). In 2006 a list of anomalies in character names was first published, and, as of June 2021, there were 104 characters with identified issues, for example:

- U+034F ͏ COMBINING GRAPHEME JOINER: Does not join graphemes.
- U+2118 ℘ SCRIPT CAPITAL P: This is a small letter. The capital is U+1D4AB 𝒫 MATHEMATICAL SCRIPT CAPITAL P.
- U+A015 ꀕ YI SYLLABLE WU: This is not a Yi syllable, but a Yi iteration mark.
- U+FE18 ︘ PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET: *bracket* is spelled incorrectly. (Spelling errors are resolved by using Unicode alias names.)

While Unicode defines the script designator (name) to be "Phags_Pa", in that script's character names, a hyphen is added: U+A840 ꡀ PHAGS-PA LETTER KA. This, however, is not an anomaly, but the rule: hyphens are replaced by underscores in script designators.
