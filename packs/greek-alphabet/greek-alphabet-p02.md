---
title: "Greek alphabet (part 2/2)"
source: https://en.wikipedia.org/wiki/Greek_alphabet
domain: greek-alphabet
license: CC-BY-SA-4.0
tags: greek alphabet
fetched: 2026-07-05
part: 2/2
---

## Computer encodings

For computer usage, a variety of encodings have been used for Greek online, many of them documented in RFC 1947.

The two principal ones still used today are ISO/IEC 8859-7 and Unicode. ISO 8859-7 supports only the monotonic orthography; Unicode supports both the monotonic and polytonic orthographies.

### ISO/IEC 8859-7

For the range A0–FF (hex), it follows the Unicode range 370–3CF (see below) except that some symbols, like ©, ½, § etc. are used where Unicode has unused locations. Like all ISO-8859 encodings, it is equal to ASCII for 00–7F (hex).

### Greek in Unicode

Unicode supports polytonic orthography well enough for ordinary continuous text in modern and ancient Greek, and even many archaic forms for epigraphy. With the use of combining characters, Unicode also supports Greek philology and dialectology and various other specialized requirements. Most current text rendering engines do not render diacritics well, so, though alpha with macron and acute can be *represented* as U+03B1 U+0304 U+0301, this rarely renders well: ᾱ́.

There are two main blocks of Greek characters in Unicode. The first is "Greek and Coptic" (U+0370 to U+03FF). This block is based on ISO 8859-7 and is sufficient to write Modern Greek. There are also some archaic letters and Greek-based technical symbols.

This block also supports the Coptic alphabet. Formerly, most Coptic letters shared codepoints with similar-looking Greek letters; but in many scholarly works, both scripts occur, with quite different letter shapes, so as of Unicode 4.1, Coptic and Greek were disunified. Those Coptic letters with no Greek equivalents still remain in this block (U+03E2 to U+03EF).

To write polytonic Greek, one may use combining diacritical marks or the precomposed characters in the "Greek Extended" block (U+1F00 to U+1FFF).

Greek and Coptic

[1]

[2]

Official Unicode Consortium code chart

(PDF)

0

1

2

3

4

5

6

7

8

9

A

B

C

D

E

F

U+037x

Ͱ

ͱ

Ͳ

ͳ

ʹ

͵

Ͷ

ͷ

ͺ

ͻ

ͼ

ͽ

;

Ϳ

U+038x

΄

΅

Ά

·

Έ

Ή

Ί

Ό

Ύ

Ώ

U+039x

ΐ

Α

Β

Γ

Δ

Ε

Ζ

Η

Θ

Ι

Κ

Λ

Μ

Ν

Ξ

Ο

U+03Ax

Π

Ρ

Σ

Τ

Υ

Φ

Χ

Ψ

Ω

Ϊ

Ϋ

ά

έ

ή

ί

U+03Bx

ΰ

α

β

γ

δ

ε

ζ

η

θ

ι

κ

λ

μ

ν

ξ

ο

U+03Cx

π

ρ

ς

σ

τ

υ

φ

χ

ψ

ω

ϊ

ϋ

ό

ύ

ώ

Ϗ

U+03Dx

ϐ

ϑ

ϒ

ϓ

ϔ

ϕ

ϖ

ϗ

Ϙ

ϙ

Ϛ

ϛ

Ϝ

ϝ

Ϟ

ϟ

U+03Ex

Ϡ

ϡ

Ϣ

ϣ

Ϥ

ϥ

Ϧ

ϧ

Ϩ

ϩ

Ϫ

ϫ

Ϭ

ϭ

Ϯ

ϯ

U+03Fx

ϰ

ϱ

ϲ

ϳ

ϴ

ϵ

϶

Ϸ

ϸ

Ϲ

Ϻ

ϻ

ϼ

Ͻ

Ͼ

Ͽ

Notes

1.

^

As of Unicode version 17.0

2.

^

Grey areas indicate non-assigned code points

Greek Extended

[1]

[2]

Official Unicode Consortium code chart

(PDF)

0

1

2

3

4

5

6

7

8

9

A

B

C

D

E

F

U+1F0x

ἀ

ἁ

ἂ

ἃ

ἄ

ἅ

ἆ

ἇ

Ἀ

Ἁ

Ἂ

Ἃ

Ἄ

Ἅ

Ἆ

Ἇ

U+1F1x

ἐ

ἑ

ἒ

ἓ

ἔ

ἕ

Ἐ

Ἑ

Ἒ

Ἓ

Ἔ

Ἕ

U+1F2x

ἠ

ἡ

ἢ

ἣ

ἤ

ἥ

ἦ

ἧ

Ἠ

Ἡ

Ἢ

Ἣ

Ἤ

Ἥ

Ἦ

Ἧ

U+1F3x

ἰ

ἱ

ἲ

ἳ

ἴ

ἵ

ἶ

ἷ

Ἰ

Ἱ

Ἲ

Ἳ

Ἴ

Ἵ

Ἶ

Ἷ

U+1F4x

ὀ

ὁ

ὂ

ὃ

ὄ

ὅ

Ὀ

Ὁ

Ὂ

Ὃ

Ὄ

Ὅ

U+1F5x

ὐ

ὑ

ὒ

ὓ

ὔ

ὕ

ὖ

ὗ

Ὑ

Ὓ

Ὕ

Ὗ

U+1F6x

ὠ

ὡ

ὢ

ὣ

ὤ

ὥ

ὦ

ὧ

Ὠ

Ὡ

Ὢ

Ὣ

Ὤ

Ὥ

Ὦ

Ὧ

U+1F7x

ὰ

ά

ὲ

έ

ὴ

ή

ὶ

ί

ὸ

ό

ὺ

ύ

ὼ

ώ

U+1F8x

ᾀ

ᾁ

ᾂ

ᾃ

ᾄ

ᾅ

ᾆ

ᾇ

ᾈ

ᾉ

ᾊ

ᾋ

ᾌ

ᾍ

ᾎ

ᾏ

U+1F9x

ᾐ

ᾑ

ᾒ

ᾓ

ᾔ

ᾕ

ᾖ

ᾗ

ᾘ

ᾙ

ᾚ

ᾛ

ᾜ

ᾝ

ᾞ

ᾟ

U+1FAx

ᾠ

ᾡ

ᾢ

ᾣ

ᾤ

ᾥ

ᾦ

ᾧ

ᾨ

ᾩ

ᾪ

ᾫ

ᾬ

ᾭ

ᾮ

ᾯ

U+1FBx

ᾰ

ᾱ

ᾲ

ᾳ

ᾴ

ᾶ

ᾷ

Ᾰ

Ᾱ

Ὰ

Ά

ᾼ

᾽

ι

᾿

U+1FCx

῀

῁

ῂ

ῃ

ῄ

ῆ

ῇ

Ὲ

Έ

Ὴ

Ή

ῌ

῍

῎

῏

U+1FDx

ῐ

ῑ

ῒ

ΐ

ῖ

ῗ

Ῐ

Ῑ

Ὶ

Ί

῝

῞

῟

U+1FEx

ῠ

ῡ

ῢ

ΰ

ῤ

ῥ

ῦ

ῧ

Ῠ

Ῡ

Ὺ

Ύ

Ῥ

῭

΅

`

U+1FFx

ῲ

ῳ

ῴ

ῶ

ῷ

Ὸ

Ό

Ὼ

Ώ

ῼ

´

῾

Notes

1.

^

As of Unicode version 17.0

2.

^

Grey areas indicate non-assigned code points

#### Combining and letter-free diacritics

Combining and spacing (letter-free) diacritical marks pertaining to Greek language:

| Combining | Spacing | Sample | Description |
|---|---|---|---|
| U+0300 | U+0060 | ( *̀*) | "varia / grave accent" |
| U+0301 | U+00B4, U+0384 | ( *́*) | "oxia / tonos / acute accent" |
| U+0304 | U+00AF | ( ̄ ) | "macron" |
| U+0306 | U+02D8 | ( ̆ ) | "vrachy / breve" |
| U+0308 | U+00A8 | ( ̈ ) | "dialytika / diaeresis" |
| U+0313 | U+02BC | ( ̓ ) | "psili / comma above" (spiritus lenis) |
| U+0314 | U+02BD | ( ̔ ) | "dasia / reversed comma above" (spiritus asper) |
| U+0342 |   | ( ͂ ) | "perispomeni" (circumflex) |
| U+0343 |   | ( ̓ ) | "koronis" (= U+0313) |
| U+0344 | U+0385 | ( ̈́ ) | "dialytika tonos" (deprecated, = U+0308 U+0301) |
| U+0345 | U+037A | ( ͅ ) | "ypogegrammeni / iota subscript". |

### Encodings with a subset of the Greek alphabet

IBM code pages 437, 860, 861, 862, 863, and 865 contain the letters ΓΘΣΦΩαδεπστφ (plus β as an alternative interpretation for ß).
