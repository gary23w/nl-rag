---
title: "Base64"
source: https://en.wikipedia.org/wiki/Base64
domain: data-formats
license: CC-BY-SA-4.0
tags: json, yaml, toml, xml, csv, base64, markdown
fetched: 2026-07-02
---

# Base64

**Base64** is a binary-to-text encoding that uses 64 printable characters to represent each 6-bit segment of a sequence of byte values. As for all binary-to-text encodings, Base64 encoding enables transmitting binary data on a communication channel that only supports text.

When comparing the original data to the resulting encoded data, Base64 encoding increases the size by 33% plus about 4% additional if inserting line breaks for typical line length.

The earliest uses of this encoding were for dial-up communication between systems running the same operating system – for example, uuencode for UNIX and BinHex for the TRS-80 (later adapted for the Macintosh) – and could therefore make more assumptions about what characters were safe to use. For instance, uuencode uses uppercase letters, digits, and many punctuation characters, but no lowercase.

## Applications

Notable applications of Base64:

**Web pages**

Base64 encoding is prevalent on the

World Wide Web

where it is often used to embed binary data such as a digital image in text such as

HTML

and

CSS

.

**E-mail attachments**

Base64 is widely used for sending

e-mail

attachments, because

SMTP

– in its original form – was designed to transport

7-bit ASCII

characters only. Encoding an attachment as Base64 before sending, and then decoding when received, assures older SMTP servers correctly transmit messages with attached binary information.

**Embed binary data in a text file**

For example, to include the data of an image in a script to avoid depending on external files.

**Embed binary data in XML**

To embed binary data in an

XML

file, using a syntax similar to

<data encoding="base64">...</data>

e.g.

favicons

in

Firefox

's exported

bookmarks.html

.

**PDF files**

To embed a

PDF

file in an HTML page.

**Embedded elements**

Although not part of the official specification for the

SVG

format, some viewers can interpret Base64 when used for embedded elements, such as raster images inside SVG files.

**Preventing delimiter collisions**

To transmit and store text that might otherwise cause

delimiter collision

.

**LDAP Data Interchange Format**

To encode character strings in

LDAP Data Interchange Format

files.

**Data URI schemes**

The

data URI scheme

can use Base64 to represent file contents. For instance, background images and fonts can be specified in a

CSS

stylesheet file as

data:

URIs, instead of being supplied in separate files.

**Leverage clipboard**

To store/transmit relatively small amounts of binary data via a computer's text

clipboard

functionality, especially in cases where the information doesn't warrant being permanently saved or when information must be quickly sent between a wide variety of different, potentially incompatible programs. An example is the representation of the public keys of

cryptocurrency

recipients as Base64 encoded text strings, which can be easily copied and pasted into users'

wallet software

.

**Support human verification**

Binary data that must be quickly verified by humans as a safety mechanism, such as

file checksums

or

key fingerprints

, is often represented in Base64 for easy checking, sometimes with additional formatting, such as separating each group of four characters in the representation of a

PGP

key fingerprint with a space.

**QR code encoding**

A

QR code

, which contains binary data, is sometimes stored as Base64 since it is more likely that a QR code reader accurately decodes text than binary data. Also, some devices more readily save text from a QR code than potentially malicious binary data.

## Alphabet

The set of characters used to represent the values for each base-64 digit (value from 0 to 63) differs slightly between the variations of Base64. The general strategy is to use printable characters that are common to most character encodings. This tends to result in data remaining unchanged as it moves through information systems, such as email, that were traditionally not 8-bit clean. Typically, an encoding uses `A`–`Z`, `a`–`z`, and `0`–`9` for the first 62 values. Many variants use `+` and `/` for the last two.

Per RFC 4648 §4, the following table lists the characters used for each numeric value. To indicate padding, `=` is used.

Base64 alphabet

Value

char

Value

char

value

char

value

char

0

A

16

Q

32

g

48

w

1

B

17

R

33

h

49

x

2

C

18

S

34

i

50

y

3

D

19

T

35

j

51

z

4

E

20

U

36

k

52

0

5

F

21

V

37

l

53

1

6

G

22

W

38

m

54

2

7

H

23

X

39

n

55

3

8

I

24

Y

40

o

56

4

9

J

25

Z

41

p

57

5

10

K

26

a

42

q

58

6

11

L

27

b

43

r

59

7

12

M

28

c

44

s

60

8

13

N

29

d

45

t

61

9

14

O

30

e

46

u

62

+

15

P

31

f

47

v

63

/

Base64URL encoding replaces `+` with `-` and `/` with `_` to make the encoded string HTTP-safe and avoid the need for escaping.

## Examples

To simplify explanation, the example below uses plain text for input. While this is done in practice, a much more common use is encoding images and other data that are normally not representable with plain text, and the result then represents the data in a printable text format.

For the input data:

```
Many hands make light work.
```

The typical Base64 representation is:

```
TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu
```

### Encoding when no padding needed

Each input sequence of 6 bits (which can encode 26 = 64 values) is mapped to a Base64 alphabet letter. Therefore, Base64 encoding results in four characters for each three input bytes. Assuming the input is ASCII or similar, the byte-data for the first three characters 'M', 'a', 'n' are values `77`, `97`, and `110` which in 8-bit binary representation are `01001101`, `01100001`, and `01101110`. Joining these representations and splitting into 6-bit groups gives:

```
010011 010110 000101 101110
```

Which encodes the string `TWFu` (per ASCII or similar).

The following table shows how input is encoded. For example, the letter 'M' has the value `77` (per ASCII and similar). The first 6 bits of the value is `010011` or 19 decimal which maps to Base64 letter 'T' which has a value `84` (per ASCII and similar).

Encoding 'M', 'a', 'n' as Base64

Input

(ASCII)

Letter (ASCII)

M

a

n

8-bit

decimal value

77

97

110

Hexadecimal

value

4

D

6

1

6

E

Bits

0

1

0

0

1

1

0

1

0

1

1

0

0

0

0

1

0

1

1

0

1

1

1

0

Encoded

(Base64)

6-bit

decimal value

19

22

5

46

Letter

(Base64 alphabet)

T

W

F

u

Byte

84

87

70

117

### Encoding with one padding character

If the input consists of a number of bytes that is 2 more than a multiple of 3 (e.g. 'M', 'a'), then the last 2 bytes (16 bits) are encoded in 3 Base64 digits (18 bits). The two least significant bits of the last content-bearing 6-bit block are treated as zero for encoding and discarded for decoding (along with the trailing `=` padding character).

Input

(ASCII)

Letter (ASCII)

M

a

8-bit

decimal value

77

97

Hexadecimal

value

4

D

6

1

Bits

0

1

0

0

1

1

0

1

0

1

1

0

0

0

0

1

0

0

Encoded

(Base64)

6-bit

decimal value

19

22

4

Padding

Letter

(Base64 alphabet)

T

W

E

=

Byte

84

87

69

61

### Encoding with two padding characters

If the input consists of a number of bytes that is 1 more than a multiple of 3 (e.g. 'M'), then the last 8 bits are represented in 2 Base64 digits (12 bits). The four least significant bits of the last content-bearing 6-bit block are treated as zero for encoding and discarded for decoding (along with the trailing two `=` padding characters):

Input

(ASCII)

Letter (ASCII)

M

8-bit

decimal value

77

Hexadecimal

value

4

D

Bits

0

1

0

0

1

1

0

1

0

0

0

0

Encoded

(Base64)

6-bit

decimal value

19

16

Padding

Padding

Letter

(Base64 alphabet)

T

Q

=

=

byte

84

81

61

61

### Decoding with padding

When decoding, each sequence of four encoded characters is converted to three output bytes, but with a single padding character the final 4 characters decode to only two bytes, or with two padding characters, the final 4 characters decode to a single byte. For example:

| Encoded | Padding | Length | Decoded |
|---|---|---|---|
| bGlnaHQgdw== | `==` | 1 | *light w* |
| bGlnaHQgd28= | `=` | 2 | *light wo* |
| bGlnaHQgd29y | None | 3 | *light wor* |

Another way to interpret the padding character is to consider it as an instruction to discard 2 trailing bits from the bit string each time a `=` is encountered. For example, when bGlnaHQgdw== is decoded, we convert each character (except the trailing occurrences of `=`) into their corresponding 6-bit representation, and then discard 2 trailing bits for the first `=` and another 2 trailing bits for the other `=`. In this instance, we would get 6 bits from the `d`, and another 6 bits from the `w` for a bit string of length 12, but since we remove 2 bits for each `=` (for a total of 4 bits), the `dw==` ends up producing 8 bits (1 byte) when decoded.

### Decoding without padding

Use of the padding character in encoded text is not essential for decoding. The number of missing bytes can be inferred from the length of the encoded text. In some variants, the padding character is mandatory, while for others it is not used. Notably, when concatenating Base64 encoded strings, then use of padding characters is *required* during encoding to avoid ambiguity when decoding.

Without padding, after decoding each sequence of 4 encoded characters, there may be 2 or 3 encoded characters left over. A single remaining encoded character is not possible because a single Base64 character only contains 6 bits, and 8 bits are required to create a byte. The first Base64 character contributes 6 bits, and the second Base64 character contributes its first 2 bits to finish filling the byte. The following table demonstrates decoding encoded strings that have 2, 3 or no left-over characters.

| Encoded | Length of last group | Decoded | Decoded length of last group |
|---|---|---|---|
| bGlnaHQgdw | 2 | *light w* | 1 |
| bGlnaHQgd28 | 3 | *light wo* | 2 |
| bGlnaHQgd29y | 4 | *light wor* | 3 |

Decoding without padding is not performed consistently among decoders - some decoders require padding while other decoders infer the correct amount of padding from the encoded input string. In addition, allowing padless decoding by definition allows one list of strings written in some particular order to decode into several possible different output strings rather than only one possible output string, which can be a security risk due to the unpredictable and/or unexpected decoding.

## Variants

Variations of Base64 differ in the alphabet used and structural aspects like maximum line length. The most commonly used alphabet is that described by RFC 4648 and most variations only differ in the last two letters used. The following table describes more commonly used encodings that are specified by an RFC.

| Encoding | Specification | Alphabet | Lines |   |   |   |   |
|---|---|---|---|---|---|---|---|
| 62nd | 63rd | pad | Separators | Length | Checksum |   |   |
| Base 64 Encoding | RFC 4648 §4 | `+` | `/` | `=` | No |   | No |
| Base 64 Encoding with URL and Filename Safe Alphabet | RFC 4648 §5 | `-` | `_` | `=` optional | No |   | No |
| for MIME | RFC 2045 | `+` | `/` | `=` | Yes | 76 | No |
| for Privacy-Enhanced Mail (deprecated) | RFC 1421 | `+` | `/` | `=` | Yes | 64 | Yes, in PEM CRC |
| for UTF-7 | RFC 2152 | `+` | `/` |   | No |   | No |
| for IMAP mailbox names | RFC 3501 | `+` | `,` |   | No |   | No |
| Textual Encodings of PKIX, PKCS, and CMS Structures | RFC 7468 | `+` | `/` | `=` | Yes | 64 | No |
| ASCII armor for OpenPGP | RFC 9580 | `+` | `/` | `=` | Yes | 76 | Yes, (CRC24) |

### RFC 4648

RFC 4648 describes a various encodings including Base64, and it discusses the use of line feeds in encoded data, the use of padding in encoded data, the use of non-alphabet characters in encoded data, use of different encoding alphabets, and canonical encodings. The variant that it calls *Base 64 Encoding* and *base64* is intended for general-use.

The RFC also specifies a second Base64 encoding that it calls *Base 64 Encoding with URL and Filename Safe Alphabet* that is intended for representing relatively long identifying information. For example, a database persistence framework for Java objects might use Base64 encoding to encode a relatively large unique id (generally 128-bit UUIDs) as a string for use as an HTTP parameter in an HTTP form or an HTTP GET URL. Also, many applications need to encode binary data in a way that is convenient for inclusion in a URL, including in hidden web form fields, and Base64 is a convenient encoding to render them in a compact way.

Using standard Base64 in a URL requires encoding the `+`, `/` and `=` characters as special percent-encoded hexadecimal sequences (`+` becomes `%2B`, `/` becomes `%2F` and `=` becomes `%3D`), which makes the string longer and harder to read. Using a different alphabet allows for encoding as Base64 without requiring this extra markup. Typically, `+` and `/` are replaced by `-` and `_`, respectively, so that using URL encoders/decoders is no longer necessary and has no effect on the length of the encoded value, leaving the same encoded form intact for use in relational databases, web forms, and object identifiers in general. A popular site to make use of such is YouTube. Some variants allow or require omitting the padding `=` signs to avoid them being confused with field separators, or require that any such padding be percent-encoded. Some libraries encode `=` as `.`, potentially exposing applications to relative path attacks when a folder name is encoded from user data.

### RFC 3548

RFC 3548, entitled *The Base16, Base32, and Base64 Data Encodings*, is an informational (non-normative) memo that attempts to unify the RFC 1421 and RFC 2045 specifications of Base64 encodings, alternative-alphabet encodings, and the Base32 (which is seldom used) and Base16 encodings. RFC 4648 obsoletes RFC 3548.

Unless an encoder is written to a specification that refers to RFC 3548 and specifically requires otherwise, RFC 3548 forbids an encoder from generating messages containing characters outside the encoding alphabet or without padding, and it also declares that a decoder must reject data that contain characters other than the encoding alphabet.

### MIME

The MIME (Multipurpose Internet Mail Extensions) specification lists Base64 as one of two binary-to-text encoding schemes (the other being quoted-printable). MIME's Base64 encoding is based on that of the RFC 1421 version of PEM: it uses the same 64-character alphabet and encoding mechanism as PEM and uses the `=` symbol for output padding in the same way, as described at RFC 2045.

MIME does not specify a fixed length for Base64-encoded lines, but it does specify a maximum line length of 76 characters. Additionally, it specifies that any character outside the standard set of 64 encoding characters (for example CRLF sequences), must be ignored by a compliant decoder, although most implementations use a CR/LF newline pair to delimit encoded lines.

Thus, the actual length of MIME-compliant Base64-encoded binary data is usually about 137% of the original data length (4⁄3×78⁄76), though for very short messages the overhead can be much higher due to the overhead of the headers. Very roughly, the final size of Base64-encoded binary data is equal to 1.37 times the original data size + 814 bytes (for headers). The size of the decoded data can be approximated with this formula:

```
bytes = (string_length(encoded_string) − 814) / 1.37
```

### Privacy-enhanced mail

The first known standardized use of the encoding now called MIME Base64 was in the Privacy-Enhanced Mail (PEM) protocol, proposed by RFC 989 in 1987. PEM defines a "printable encoding" scheme that uses Base64 encoding to transform an arbitrary sequence of bytes to a format that can be expressed in short lines of 6-bit characters, as required by transfer protocols such as SMTP.

The current version of PEM (specified in RFC 1421) uses a 64-character alphabet consisting of upper- and lower-case Roman letters (`A`–`Z`, `a`–`z`), the numerals (`0`–`9`), and the `+` and `/` symbols. The `=` symbol is also used as a padding suffix. The original specification, RFC 989, additionally used the `*` symbol to delimit encoded but unencrypted data within the output stream.

To convert data to PEM printable encoding, the first byte is placed in the most significant eight bits of a 24-bit buffer, the next in the middle eight, and the third in the least significant eight bits. If there are fewer than three bytes left to encode (or in total), the remaining buffer bits will be zero. The buffer is then used, six bits at a time, most significant first, as indices into the string: "`ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`", and the indicated character is output.

The process is repeated on the remaining data until fewer than four bytes remain. If three bytes remain, they are processed normally. If fewer than three bytes (24 bits) are remaining to encode, the input data is right-padded with zero bits to form an integral multiple of six bits.

After encoding the non-padded data, if two bytes of the 24-bit buffer are padded-zeros, two `=` characters are appended to the output; if one byte of the 24-bit buffer is filled with padded-zeros, one `=` character is appended. This signals the decoder that the zero bits added due to padding should be excluded from the reconstructed data. This also guarantees that the encoded output length is a multiple of 4 bytes.

PEM requires that all encoded lines consist of exactly 64 printable characters, with the exception of the last line, which may contain fewer printable characters. Lines are delimited by whitespace characters according to local (platform-specific) conventions.

### UTF-7

UTF-7, described first in RFC 1642, which was later superseded by RFC 2152, introduced a system called *modified Base64*. This data encoding scheme is used to encode UTF-16 as ASCII characters for use in 7-bit transports such as SMTP. It is a variant of the Base64 encoding used in MIME.

The "Modified Base64" alphabet consists of the MIME Base64 alphabet, but does not use the "`=`" padding character. UTF-7 is intended for use in mail headers (defined in RFC 2047), and the "`=`" character is reserved in that context as the escape character for "quoted-printable" encoding. Modified Base64 simply omits the padding and ends immediately after the last Base64 digit containing useful bits leaving up to three unused bits in the last Base64 digit.

### OpenPGP

OpenPGP, described in RFC 9580, specifies "ASCII armor", which is identical to the "Base64" encoding described by MIME, with the addition of an optional 24-bit CRC. The checksum is calculated on the input data before encoding; the checksum is then encoded with the same Base64 algorithm and, prefixed by the "`=`" symbol as the separator, appended to the encoded output data.

### Javascript (DOM Web API)

The `atob()` and `btoa()` JavaScript methods, defined in the HTML5 draft specification, provide Base64 encoding and decoding functionality to web pages. The `btoa()` method outputs padding characters, but these are optional in the input of the `atob()` method. Example: Encoding of the beginning of a GIF file: `btoa("GIF89a")` ↦ `"R0lGODlh"`.

### With atypical alphabet order

Several variants use alphabets similar to the common variants, but in a different order.

**Unix password**

Unix stores password hashes computed with

crypt

in the

/etc/passwd

file

using an encoding called

B64

. crypt's alphabet puts the punctuation

.

and

/

before the alphanumeric characters. crypt uses the alphabet "

./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz

" without padding. An advantage over RFC 4648 is that sorting encoded ASCII data results in the same order as sorting the plain ASCII data.

**GEDCOM**

The

GEDCOM

5.5 standard for genealogical data interchange encodes multimedia files in its text-line hierarchical file format. GEDCOM uses the same alphabet as crypt, which is

"

./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz

"

.

**bcrypt**

bcrypt

hashes are designed to be used in the same way as traditional crypt(3) hashes, but bcrypt's alphabet is in a different order than crypt's. bcrypt uses the alphabet

"

./ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789

"

.

**Xxencoding**

Xxencoding

uses a mostly-alphanumeric character set similar to crypt, but using

+

and

-

rather than

.

and

/

. Xxencoding uses the alphabet

"

+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz

"

.

**6PACK**

Used with some

terminal node controllers

, uses an alphabet from 0x00 to 0x3f.

**Bash**

Bash

supports numeric literals in Base64. Bash uses the alphabet

"

0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@_

"

.

### With atypical alphabet

Some variants use a Base64 alphabet that is significantly different from the alphabets used in the most common Base64 variants (like RFC 4648).

**Uuencoding**

The

Uuencoding

alphabet includes no lowercase characters, instead using ASCII codes 32 ("

" (space)) through 95 ("

_

"), consecutively. Uuencoding uses the alphabet

"

!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_

"

. Avoiding all lower-case letters was helpful, because many older printers only printed uppercase. Using consecutive ASCII characters saved computing power, because it was only necessary to add 32, without requiring a lookup table. Its use of most punctuation characters and the space character may limit its usefulness in some applications, such as those that use these characters as syntax.

**BinHex**

BinHex 4

(HQX), which was used within the

classic Mac OS

, excludes some visually confusable characters like '

7

', '

O

', '

g

' and '

o

'. Its alphabet includes additional punctuation characters. It uses the alphabet

"

!"#$%&'()*+,-012345689@ABCDEFGHIJKLMNPQRSTUVXYZ[`abcdefhijklmpqr

"

.

**UTF-8**

A

UTF-8

environment can use non-synchronized continuation bytes as base64:

0b10

xxxxxx

. See

UTF-8#Self-synchronization

.
