---
title: "Punycode"
source: https://en.wikipedia.org/wiki/Punycode
domain: encodings-serialization
license: CC-BY-SA-4.0
tags: unicode, utf-8, character encoding, protobuf, serialization, endianness
fetched: 2026-07-02
---

# Punycode

**Punycode** is a representation of Unicode with the limited ASCII character subset used for Internet hostnames. Using Punycode, host names containing Unicode characters are transcoded to a subset of ASCII consisting of letters, digits, and hyphens, which is called the letter–digit–hyphen (LDH) subset. For example, the German *München* (English: Munich) is encoded as *Mnchen-3ya*.

While the Domain Name System (DNS) technically supports arbitrary sequences of octets in domain name labels, the DNS standards recommend the use of the LDH subset of ASCII conventionally used for host names, and require that string comparisons between DNS domain names should be case-insensitive. The Punycode syntax is a method of encoding strings containing Unicode characters, such as internationalized domain names (IDNA), into the LDH subset of ASCII favored by DNS. It is specified in IETF Request for Comments 3492.

## Origin of the name

The RFC author, Adam Costello, is reported to have written:

> Why “Punycode”? It rhymes with Unicode and is intended to encode Unicode strings. It is “puny” in three senses: The repertoire of characters used in the encoded strings is small, the encoded strings are short, and the implementation is small.

## Description

As stated in RFC 3492, "Punycode is an instance of a more general algorithm called *Bootstring*, which allows strings composed from a small set of 'basic' code points to uniquely represent any string of code points drawn from a larger set." Punycode defines parameters for the general Bootstring algorithm to match the characteristics of Unicode text. This section demonstrates the procedure for Punycode encoding, using as an example the German string "bücher" (English: *books*), which is translated into the label "bcher-kva".

To make the encoding and decoding algorithms simple, no attempt has been made to prevent some encoded values from encoding inadmissible Unicode values: however, these should be checked for and detected during decoding.

Punycode is designed to work across all scripts, and to be self-optimizing by attempting to adapt to the character set ranges within the string as it operates. It is optimized for the case where the string is composed of zero or more ASCII characters and in addition characters from only one other script system, but will cope with any arbitrary Unicode string. Note that for DNS use, the domain name string is assumed to have been normalized using nameprep and (for top-level domains) filtered against an officially registered language table before being punycoded, and that the DNS protocol sets limits on the acceptable lengths of the output Punycode string.

### Separation of ASCII characters

First, all ASCII characters in the string are copied from input to output, skipping over any other characters. For example, "bücher" is copied to "bcher". If any characters were copied, i.e. if there was at least one ASCII character in the input, an ASCII hyphen is appended to the output (e.g., "bücher" → "bcher-", but "ü" → "").

Note that hyphens are themselves ASCII characters. Thus, they can be present in the input and, if so, they will be copied to the output. This causes no ambiguity: if the output contains hyphens, the one that got added is always the last one. It marks the end of the ASCII characters.

### Encoding the non-ASCII characters

The non-ASCII characters are sorted by Unicode value, lowest first (if a character occurs more than once, they are sorted by position). Each is then encoded as a single number. This single number defines both the location to insert the character at and which character to insert.

- An index into the result to insert the code at, starting at 0 (for insertion at the start).
- The number of insertionPoints (current length of the result plus one).
- The reducedCodepoint is the Unicode code point to insert minus 128.

The encoded number is *insertionPoints* × *reducedCodepoint* + *index*. By dividing by insertionPoints and also getting the remainder, a decoder can determine reducedCodepoint and index.

There are 6 possible insertion points for a character in the string "bcher" (including before the first character and after the last one). ü is Unicode code point 0xFC or 252 (see Latin-1 Supplement), and the reduced code point is 252 − 128, or 124. The ü is inserted at position 1, after the b. Thus the encoder will add the number 6 × 124 + 1 = 745, and the decoder can retrieve these by ⌊745 / 6⌋ = 124 and 745 mod 6 = 1.

These numbers are strictly increasing. For the second and subsequent inserted characters, the difference between the number and the previous one is written.

### Variable-length number encoding

The number is encoded using the letters a through z and the digits 0 through 9. It is not base-36 but a more complex scheme, generalized variable-length integers, which allows the numbers to be concatenated with nothing separating them.

This is how "kva" is used to represent the code number 745:

> A number system with little-endian ordering is used which allows variable-length codes without separate delimiters: a digit lower than a threshold value marks that it is the most-significant digit, hence the end of the number. The threshold value depends on the position in the number and also on previous insertions, to increase efficiency. Correspondingly the weights of the digits vary.
> 
> In this case a number system with 36 symbols is used, with the case-insensitive 'a' through 'z' equal to the decimal numbers 0 through 25, and '0' through '9' equal to the decimal numbers 26 through 35. Thus "kva", corresponds to the decimal number string "10 21 0".

To decode this string of symbols, a sequence of thresholds will be needed, in this case it is (1, 1, 26, 26, ...). The weight (or place value) of the least-significant digit is always 1: 'k' (=10) with a weight of 1 equals 10. After this, the weight of the next digit depends on the first threshold: generally, for any *n*, the weight of the (*n*+1)-th digit is *w* × (36 − *t*), where *w* is the previous weight and *t* is the threshold of the *n*-th digit. So in this case, the second symbol has a place value of 36 minus the previous threshold value of 1, which equals 35. Therefore, the sum of the first two symbols 'k' (=10) and 'v' (=21) is 10 × 1 + 21 × 35. Since the second symbol is not less than its threshold value of 1, there is more to come. However, since the third symbol in this example is 'a' (=0), we may ignore calculating its weight. Therefore, "kva" represents the decimal number (10 × 1) + (21 × 35) = 745.

Number 745 will be encoded as 10 + 21 × 35 + 0 (base 35 used for second digit, the most significant digit 0 needed as terminator), 10 → 'k', 21 → 'v', 0 → 'a', so "bücher" → "bcher-kva".

The thresholds themselves are determined for each successive encoded character by an algorithm keeping them between 1 and 26 inclusive. The case can then be used to provide information about the original case of the string.

Because special characters are sorted by their code points by encoding algorithm, for the insertion of a second special character in "bücher", the first possibility is "büücher" with code "bcher-kvaa", the second "bücüher" with code "bcher-kvab", etc. After "bücherü" with code "bcher-kvae" comes codes representing insertion of ý, the Unicode character following ü, starting with "ýbücher" with code "bcher-kvaf" (different from "übücher" coded "bcher-jvab"), etc.

### ACE prefix for internationalized domain names

To prevent hyphens in non-international domain names from triggering a Punycode decoding, the string `xn--` is prepended to Punycode sequences in internationalized domain names. This is called ACE (ASCII Compatible Encoding).

Thus the domain name "bücher.tld" would be represented in a URL as "xn--bcher-kva.tld".

## Examples

The following table shows examples of Punycode encodings for different types of input.

| Input | Punycode | Description |
|---|---|---|
|   |   | The empty string. |
| a | a- | Only ASCII characters, one, lowercase. |
| A | A- | Only ASCII characters, one, uppercase. |
| 3 | 3- | Only ASCII characters, one, a digit. |
| - | -- | Only ASCII characters, one, a hyphen. |
| -- | --- | Only ASCII characters, two hyphens. |
| London | London- | Only ASCII characters, more than one, no hyphens. |
| Lloyd-Atkinson | Lloyd-Atkinson- | Only ASCII characters, one hyphen. |
| This has spaces | This has spaces- | Only ASCII characters, with spaces. |
| -> $1.00 <- | -> $1.00 <-- | Only ASCII characters, mixed symbols. |
| Б | d0a | No ASCII characters, one Cyrillic character. |
| ü | tda | No ASCII characters, one Latin-1 Supplement character. |
| α | mxa | No ASCII characters, one Greek character. |
| 例 | fsq | No ASCII characters, one CJK character. |
| 😉 | n28h | No ASCII characters, one emoji character. |
| αβγ | mxacd | No ASCII characters, more than one character. |
| München | Mnchen-3ya | Mixed string, with one character that is not an ASCII character. |
| Mnchen-3ya | Mnchen-3ya- | Double-encoded Punycode of "München". |
| München-Ost | Mnchen-Ost-9db | Mixed string, with one character that is not ASCII, and a hyphen. |
| Bahnhof München-Ost | Bahnhof Mnchen-Ost-u6b | Mixed string, with one space, one hyphen, and one character that is not ASCII. |
| abæcdöef | abcdef-qua4k | Mixed string, two non-ASCII characters. |
| Αθήνα | jxafb0a0a | Greek (monotonic), without ASCII. |
| правда | 80aafi6cg | Russian, without ASCII. |
| ยจฆฟคฏข | 22cdfh1b8fsa | Thai, without ASCII. |
| 도메인 | hq1bm8jm9l | Korean, without ASCII. |
| ドメイン名例 | eckwd4c7cu47r2wf | Japanese, without ASCII. |
| MajiでKoiする5秒前 | MajiKoi5-783gue6qz075azm5e | Japanese with ASCII. |
| 「bücher」 | bcher-kva8445foa | Mixed non-ASCII scripts (Latin-1 Supplement and CJK). |
