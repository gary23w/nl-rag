---
title: "Combining grapheme joiner"
source: https://en.wikipedia.org/wiki/Combining_Grapheme_Joiner
domain: combining-diacritical-marks
license: CC-BY-SA-4.0
tags: combining diacritical marks
fetched: 2026-07-03
---

# Combining grapheme joiner

(Redirected from

Combining Grapheme Joiner

)

The **combining grapheme joiner** (CGJ), U+034F ͏ COMBINING GRAPHEME JOINER (&#847;) is a Unicode character that has no visible glyph and is "default ignorable" by applications. Its name is a misnomer and does not describe its function: the character does not join graphemes. Its purpose is to semantically *separate* characters that should *not* be considered digraphs as well as to block canonical reordering of combining marks during normalization.

For example, in a Hungarian language context, adjoining letters *c* and *s* would normally be considered equivalent to the cs digraph. If they are separated by the CGJ, they will be considered as two separate graphemes. However, in contrast to the zero-width joiner and similar characters, the CGJ does not affect whether the two letters are *rendered* separately or as a ligature or cursively joined—the default behavior for this is determined by the font.

The CGJ is also needed for complex scripts. For example, in most cases the Hebrew cantillation accent metheg is supposed to appear to the left of the vowel point and by default most display systems will render it like this even if it is typed before the vowel. But in some words in Biblical Hebrew the metheg appears to the right of the vowel, and to tell the display engine to render it properly on the right, CGJ must be typed between the metheg and the vowel. Compare:

| he | ה |
|---|---|
| pathah (vowel) | *ַ* |
| metheg | *ֽ* |
| he + pathah + metheg | הַֽ |
| he + metheg + pathah | הַֽ |
| he + metheg + CGJ + pathah | הֽ͏ַ |

In the case of several consecutive combining diacritics, an intervening CGJ indicates that they should not be subject to canonical reordering.

In contrast, the "zero-width non-joiner" (at U+200C in the General Punctuation range) prevents two adjacent characters from turning into a ligature.
