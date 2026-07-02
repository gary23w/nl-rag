---
title: "Comparison of data-serialization formats"
source: https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats
domain: save-game-serialization
license: CC-BY-SA-4.0
tags: save game serialization, saved game format, game state persistence, serialized save data
fetched: 2026-07-02
---

# Comparison of data-serialization formats

This is a **comparison of data serialization formats**, various ways to convert complex objects to sequences of bits. It does not include markup languages used exclusively as document file formats.

## Overview

Name

Creator-maintainer

Based on

Standardized?

Specification

Binary

?

Human-readable

?

Supports

references

?

e

Schema-

IDL

?

Standard

APIs

Supports

zero-copy

operations

Apache Arrow

Apache Software Foundation

—

N/a

De facto

Arrow Columnar Format

Yes

No

Yes

Built-in

C, C++, C#, Go, Java, JavaScript, Julia, Matlab, Python, R, Ruby, Rust, Swift

Yes

Apache Avro

Apache Software Foundation

—

N/a

No

Apache Avro™ Specification

Yes

Partial

g

—

N/a

Built-in

C, C#, C++, Java, PHP, Python, Ruby

—

N/a

Apache Parquet

Apache Software Foundation

—

N/a

No

Apache Parquet

Yes

No

No

—

N/a

Java, Python, C++

No

Apache Thrift

Facebook

(creator)

Apache

(maintainer)

—

N/a

No

Original whitepaper

Yes

Partial

c

No

Built-in

C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, JavaScript, Node.js, Smalltalk, OCaml, Delphi and other languages

—

N/a

ASN.1

ISO

,

IEC

,

ITU-T

—

N/a

Yes

ISO/IEC 8824 / ITU-T X.680 (syntax) and ISO/IEC 8825 / ITU-T X.690 (encoding rules) series. X.680, X.681, and X.683 define syntax and semantics.

BER

,

DER

,

PER

,

OER

, or custom via

ECN

XER

,

JER

,

GSER

, or custom via

ECN

Yes

f

Built-in

—

N/a

OER

Bencode

Bram Cohen

(creator)

BitTorrent, Inc.

(maintainer)

—

N/a

De facto

as

BEP

Part of

BitTorrent protocol specification

Except numbers and delimiters, being ASCII

No

No

No

No

No

BSON

MongoDB

JSON

No

BSON Specification

Yes

No

No

No

No

No

Cap'n Proto

Kenton Varda

—

N/a

No

Cap'n Proto Encoding Spec

Yes

Partial

h

No

Yes

No

Yes

CBOR

Carsten Bormann,

P. Hoffman

MessagePack

Yes

RFC 8949

Yes

No

Yes,

through tagging

CDDL

FIDO2

No

Comma-separated values

(CSV)

RFC author:

Yakov Shafranovich

—

N/a

Myriad informal variants

RFC 4180

(among others)

No

Yes

No

No

No

No

Common Data Representation

(CDR)

Object Management Group

—

N/a

Yes

General Inter-ORB Protocol

Yes

No

Yes

Yes

Ada, C, C++, Java, Cobol, Lisp, Python, Ruby, Smalltalk

—

N/a

D-Bus

Message Protocol

freedesktop.org

—

N/a

Yes

D-Bus Specification

Yes

No

No

Partial

(Signature strings)

Yes

—

N/a

Efficient XML Interchange

(EXI)

W3C

XML

, Efficient XML

Yes

Efficient XML Interchange (EXI) Format 1.0

Yes

XML

XPointer

,

XPath

XML Schema

DOM

,

SAX

,

StAX

,

XQuery

,

XPath

—

N/a

Extensible Data Notation

(edn)

Rich Hickey

/ Clojure community

Clojure

Yes

Official edn spec

No

Yes

No

No

Clojure, Ruby, Go, C++, Javascript, Java, CLR, ObjC, Python

No

FlatBuffers

Google

—

N/a

No

Flatbuffers GitHub

Yes

Apache Arrow

Partial

(internal to the buffer)

Yes

C++, Java, C#, Go, Python, Rust, JavaScript, PHP, C, Dart, Lua, TypeScript

Yes

Fast Infoset

ISO

,

IEC

,

ITU-T

XML

Yes

ITU-T X.891 and ISO/IEC 24824-1:2007

Yes

No

XPointer

,

XPath

XML schema

DOM

,

SAX

,

XQuery

,

XPath

—

N/a

FHIR

Health Level 7

REST

basics

Yes

Fast Healthcare Interoperability Resources

Yes

Yes

Yes

Yes

Hapi for FHIR

JSON

,

XML

,

Turtle

No

INI

Microsoft

?

No

Several different exists

No

Yes

?

?

?

?

Ion

Amazon

JSON

No

The Amazon Ion Specification

Yes

Yes

No

Ion schema

C, C#, Go, Java, JavaScript, Python, Rust

—

N/a

Java

serialization

Oracle Corporation

—

N/a

Yes

Java Object Serialization

Yes

No

Yes

No

Yes

—

N/a

JSON

Douglas Crockford

JavaScript syntax

Yes

STD 90

/RFC 8259

(ancillary:

RFC 6901,

RFC 6902),

ECMA-404

,

ISO/IEC 21778:2017

No, but see

BSON

,

Smile

,

UBJSON

Yes

JSON Pointer (RFC

6901)

, or alternately,

JSONPath

,

JPath

,

JSPON

,

json:select()

; and

JSON-LD

Partial

(

JSON Schema Proposal

,

ASN.1

with

JER

,

Kwalify

Archived

2021-08-12 at the

Wayback Machine

,

Rx

,

JSON-LD

Partial

(

Clarinet

,

JSONQuery

/

RQL

,

JSONPath

),

JSON-LD

No

MessagePack

Sadayuki Furuhashi

JSON

(loosely)

No

MessagePack format specification

Yes

No

No

No

No

Yes

Netstrings

Dan Bernstein

—

N/a

No

netstrings.txt

Except ASCII delimiters

Yes

No

No

No

Yes

OGDL

Rolf Veen

?

No

Specification

Binary specification

Yes

Path specification

Schema WD

—

N/a

OPC-UA Binary

OPC Foundation

—

N/a

No

opcfoundation.org

Yes

No

Yes

No

No

—

N/a

OpenDDL

Eric Lengyel

C

,

PHP

No

OpenDDL.org

No

Yes

Yes

No

OpenDDL library

—

N/a

PHP serialization format

PHP Group

—

N/a

Yes

No

Yes

Yes

Yes

No

Yes

—

N/a

Pickle (Python)

Guido van Rossum

Python

De facto

as

PEPs

PEP 3154 – Pickle protocol version 4

Yes

No

Yes

No

Yes

No

Property list

NeXT

(creator)

Apple

(maintainer)

?

Partial

Public DTD for XML format

Yes

a

Yes

b

No

?

Cocoa

,

CoreFoundation

,

OpenStep

,

GnuStep

No

Protocol Buffers

(protobuf)

Google

—

N/a

No

Developer Guide: Encoding

,

proto2 specification

, and

proto3 specification

Yes

Yes

d

No

Built-in

C++, Java, C#, Python, Go, Ruby, Objective-C, C, Dart, Perl, PHP, R, Rust, Scala, Swift, Julia, D, ActionScript, Delphi, Elixir, Elm, Erlang, GopherJS, Haskell, Haxe, JavaScript, Kotlin, Lua, Matlab, Mercurt, OCaml, Prolog, Solidity, TypeScript, Vala, Visual Basic

No

S-expressions

John McCarthy

(original)

Ron Rivest

(internet draft)

Lisp

,

Netstrings

Largely

de facto

"S-Expressions"

Archived

2013-10-07 at the

Wayback Machine

Internet Draft

Yes,

canonical representation

Yes,

advanced transport representation

No

No

—

N/a

Smile

Tatu Saloranta

JSON

No

Smile Format Specification

Yes

No

Yes

Partial

(

JSON Schema Proposal

, other JSON schemas/IDLs)

Partial

(via JSON APIs implemented with Smile backend, on Jackson, Python)

—

N/a

SOAP

W3C

XML

Yes

W3C Recommendations

:

SOAP/1.1

SOAP/1.2

Partial

(

Efficient XML Interchange

,

Binary XML

,

Fast Infoset

,

MTOM

,

XSD

base64 data

)

Yes

Built-in id/ref,

XPointer

,

XPath

WSDL

,

XML schema

DOM

,

SAX

,

XQuery

,

XPath

—

N/a

Structured Data eXchange Formats

Max Wildgrube

—

N/a

Yes

RFC 3072

Yes

No

No

No

—

N/a

TOML

Tom Preston-Werner

INI file

format

Yes

Version 1.1.0

Latest version

No

Yes

?

?

?

?

UBJSON

The Buzz Media, LLC

JSON

,

BSON

No

ubjson.org

Yes

No

No

No

No

—

N/a

eXternal Data Representation

(XDR)

Sun Microsystems

(creator)

IETF

(maintainer)

—

N/a

Yes

STD 67

/RFC 4506

Yes

No

Yes

Yes

Yes

—

N/a

XML

W3C

SGML

Yes

W3C Recommendations

:

1.0 (Fifth Edition)

1.1 (Second Edition)

Partial

(

Efficient XML Interchange

,

Binary XML

,

Fast Infoset

,

XSD

base64 data

)

Yes

XPointer

,

XPath

XML schema

,

RELAX NG

DOM

,

SAX

,

XQuery

,

XPath

—

N/a

XML-RPC

Dave Winer

XML

No

XML-RPC Specification

No

Yes

No

No

No

No

YAML

Clark Evans,

Ingy döt Net,

and Oren Ben-Kiki

C

,

Java

,

Perl

,

Python

,

Ruby

,

Email

,

HTML

,

MIME

,

URI

,

XML

,

SAX

,

SOAP

,

JSON

No

Version 1.2

No

Yes

Yes

Partial

(

Kwalify

Archived

2021-08-12 at the

Wayback Machine

,

Rx

, built-in language type-defs)

No

No

Name

Creator-maintainer

Based on

Standardized?

Specification

Binary

?

Human-readable

?

Supports

references

?

e

Schema-

IDL

?

Standard

APIs

Supports

zero-copy

operations

1. **^**The current default format is binary.
2. **^**The "classic" format is plain text, and an XML format is also supported.
3. **^**Theoretically possible due to abstraction, but no implementation is included.
4. **^**The primary format is binary, but text and JSON formats are available.
5. **^**Means that generic tools/libraries know how to encode, decode, and dereference a reference to another piece of data in the same document. A tool may require the IDL file, but no more. Excludes custom, non-standardized referencing techniques.
6. **^**ASN.1 has X.681 (Information Object System), X.682 (Constraints), and X.683 (Parameterization) that allow for the precise specification of open types where the types of values can be identified by integers, by OIDs, etc. OIDs are a standard format for globally unique identifiers, as well as a standard notation ("absolute reference") for referencing a component of a value. For example, PKIX uses such notation in RFC 5912. With such notation (constraints on parameterized types using information object sets), generic ASN.1 tools/libraries can automatically encode/decode/resolve references within a document.
7. **^**The primary format is binary, a json encoder is available.
8. **^**The primary format is binary, but a text format is available.

## Syntax comparison of human-readable formats

Format

Null

Boolean

true

Boolean

false

Integer

Floating-point

String

Array

Associative array

/

Object

ASN.1

(XML Encoding Rules)

<foo />

<foo>true</foo>

<foo>false</foo>

<foo>685230</foo>

<foo>6.8523015e+5</foo>

<foo>A to Z</foo>

```mw
<SeqOfUnrelatedDatatypes>
    <isMarried>true</isMarried>
    <hobby />
    <velocity>-42.1e7</velocity>
    <bookname>A to Z</bookname>
    <bookname>We said, "no".</bookname>
</SeqOfUnrelatedDatatypes>
```

An object (the key is a field name):

```mw
<person>
    <isMarried>true</isMarried>
    <hobby />
    <height>1.85</height>
    <name>Bob Peterson</name>
</person>
```

A data mapping (the key is a data value):

```mw
<competition>
    <measurement>
        <name>John</name>
        <height>3.14</height>
    </measurement>
    <measurement>
        <name>Jane</name>
        <height>2.718</height>
    </measurement>
</competition>
```

a

CSV

b

null

a

(or an empty element in the row)

a

1

a

true

a

0

a

false

a

685230

-685230

a

6.8523015e+5

a

A to Z

"We said, ""no""."

true,,-42.1e7,"A to Z"

```
42,1
A to Z,1,2,3
```

edn

nil

true

false

685230

-685230

6.8523015e+5

"A to Z"

,

"A \"up to\" Z"

[true nil -42.1e7 "A to Z"]

{:kw 1, "42" true, "A to Z" [1 2 3]}

Ion

`null` `null.null` `null.bool` `null.int` `null.float` `null.decimal` `null.timestamp` `null.string` `null.symbol` `null.blob` `null.clob` `null.struct` `null.list` `null.sexp`

true

false

685230

-685230

0xA74AE

0b111010010101110

6.8523015e5

"A to Z"

'''

A

to

Z

'''

```mw
[true, null, -42.1e7, "A to Z"]
```

```mw
{'42': true, 'A to Z': [1, 2, 3]}
```

Netstrings

c

0:,

a

4:null,

a

1:1,

a

4:true,

a

1:0,

a

5:false,

a

6:685230,

a

9:6.8523e+5,

a

6:A to Z,

29:4:true,0:,7:-42.1e7,6:A to Z,,

41:9:2:42,1:1,,25:6:A to Z,12:1:1,1:2,1:3,,,,

a

JSON

null

true

false

685230

-685230

6.8523015e+5

"A to Z"

```mw
[true, null, -42.1e7, "A to Z"]
```

```mw
{"42": true, "A to Z": [1, 2, 3]}
```

OGDL

null

a

true

a

false

a

685230

a

6.8523015e+5

a

"A to Z"

'A to Z'

NoSpaces

```
true
null
-42.1e7
"A to Z"
```

`(true, null, -42.1e7, "A to Z")`

```
42
  true
"A to Z"
  1
  2
  3
```

```
42
  true
"A to Z", (1, 2, 3)
```

OpenDDL

ref {null}

bool {true}

bool {false}

int32 {685230}

int32 {0x74AE}

int32 {0b111010010101110}

float {6.8523015e+5}

string {"A to Z"}

Homogeneous array:

```
int32 {1, 2, 3, 4, 5}
```

Heterogeneous array:

```
array
{
    bool {true}
    ref {null}
    float {-42.1e7}
    string {"A to Z"}
}
```

```
dict
{
    value (key = "42") {bool {true}}
    value (key = "A to Z") {int32 {1, 2, 3}}
}
```

PHP serialization format

N;

b:1;

b:0;

i:685230;

i:-685230;

d:685230.15;

d

d:INF;

d:-INF;

d:NAN;

s:6:"A to Z";

a:4:{i:0;b:1;i:1;N;i:2;d:-421000000;i:3;s:6:"A to Z";}

Associative array:

a:2:{i:42;b:1;s:6:"A to Z";a:3:{i:0;i:1;i:1;i:2;i:2;i:3;}}

Object:

O:8:"stdClass":2:{s:4:"John";d:3.14;s:4:"Jane";d:2.718;}

d

Pickle (Python)

N.

I01\n.

I00\n.

I685230\n.

F685230.15\n.

S'A to Z'\n.

(lI01\na(laF-421000000.0\naS'A to Z'\na.

(dI42\nI01\nsS'A to Z'\n(lI1\naI2\naI3\nas.

Property list

(plain text format)

—

N/a

<*BY>

<*BN>

<*I685230>

<*R6.8523015e+5>

"A to Z"

( <*BY>, <*R-42.1e7>, "A to Z" )

```
{
    "42" = <*BY>;
    "A to Z" = ( <*I1>, <*I2>, <*I3> );
}
```

Property list

(XML format)

—

N/a

<true />

<false />

<integer>685230</integer>

<real>6.8523015e+5</real>

<string>A to Z</string>

```mw
<array>
    <true />
    <real>-42.1e7</real>
    <string>A to Z</string>
</array>
```

```mw
<dict>
    <key>42</key>
    <true />
    <key>A to Z</key>
    <array>
        <integer>1</integer>
        <integer>2</integer>
        <integer>3</integer>
    </array>
</dict>
```

Protocol Buffers

—

N/a

true

false

685230

-685230

20.0855369

"A to Z"

"sdfff2 \000\001\002\377\376\375"

"q\tqq<>q2&\001\377"

```
field1: "value1"
field1: "value2"
field1: "value3
```

```
anotherfield {
  foo: 123
  bar: 456
}
anotherfield {
  foo: 222
  bar: 333
}
```

```mw
thing1: "blahblah"
thing2: 18923743
thing3: -44
thing4 {
  submessage_field1: "foo"
  submessage_field2: false
}
enumeratedThing: SomeEnumeratedValue
thing5: 123.456
[extensionFieldFoo]: "etc"
[extensionFieldThatIsAnEnum]: EnumValue
```

S-expressions

NIL

nil

T

#t

f

true

NIL

#f

f

false

685230

6.8523015e+5

abc

"abc"

#616263#

3:abc

{MzphYmM=}

|YWJj|

(T NIL -42.1e7 "A to Z")

((42 T) ("A to Z" (1 2 3)))

TOML

—

N/a

true

false

685230

+685_230

-685230

0x_0A_74_AE

0b1010_0111_0100_1010_1110

6.8523015e+5

685.230_15e+03

685_230.15

inf

-inf

nan

"A to Z"

'A to Z'

["y", -42.1e7, "A to Z"]

```
[
    "y",
    -42.1e7,
    "A to Z"
]
```

{ John = 3.14, Jane = 2.718 }

```
42 = y
"A to Z" = [1, 2, 3]
```

YAML

~

null

Null

NULL

y

Y

yes

Yes

YES

on

On

ON

true

True

TRUE

n

N

no

No

NO

off

Off

OFF

false

False

FALSE

685230

+685_230

-685230

02472256

0x_0A_74_AE

0b1010_0111_0100_1010_1110

190:20:30

6.8523015e+5

685.230_15e+03

685_230.15

190:20:30.15

.inf

-.inf

.Inf

.INF

.NaN

.nan

.NAN

A to Z

"A to Z"

'A to Z'

[y, ~, -42.1e7, "A to Z"]

```
- y
-
- -42.1e7
- A to Z
```

{"John":3.14, "Jane":2.718}

```
42: y
A to Z: [1, 2, 3]
```

XML

e

and

SOAP

<null />

a

true

false

685230

6.8523015e+5

A to Z

```mw
<item>true</item>
<item xsi:nil="true"/>
<item>-42.1e7</item>
<item>A to Z<item>
```

```mw
<map>
  <entry key="42">true</entry>
  <entry key="A to Z">
    <item val="1"/>
    <item val="2"/>
    <item val="3"/>
  </entry>
</map>
```

XML-RPC

<value><boolean>1</boolean></value>

<value><boolean>0</boolean></value>

<value><int>685230</int></value>

<value><double>6.8523015e+5</double></value>

<value><string>A to Z</string></value>

```mw
<value><array>
  <data>
  <value><boolean>1</boolean></value>
  <value><double>-42.1e7</double></value>
  <value><string>A to Z</string></value>
  </data>
  </array></value>
```

```mw
<value><struct>
  <member>
    <name>42</name>
    <value><boolean>1</boolean></value>
    </member>
  <member>
    <name>A to Z</name>
    <value>
      <array>
        <data>
          <value><int>1</int></value>
          <value><int>2</int></value>
          <value><int>3</int></value>
          </data>
        </array>
      </value>
    </member>
</struct>
```

1. **^**Omitted XML elements are commonly decoded by XML data binding tools as NULLs. Shown here is another possible encoding; XML schema does not define an encoding for this datatype.
2. **^**The RFC CSV specification only deals with delimiters, newlines, and quote characters; it does not directly deal with serializing programming data structures.
3. **^**The netstrings specification only deals with nested byte strings; anything else is outside the scope of the specification.
4. **^**PHP will unserialize any floating-point number correctly, but will serialize them to their full decimal expansion. For example, 3.14 will be serialized to 3.140000000000000124344978758017532527446746826171875.
5. **^**XML data bindings and SOAP serialization tools provide type-safe XML serialization of programming data structures into XML. Shown are XML values that can be placed in XML elements and attributes.
6. **^**This syntax is not compatible with the Internet-Draft, but is used by some dialects of Lisp.

## Comparison of binary formats

| Format | Null | Booleans | Integer | Floating-point | String | Array | Associative array/object |
|---|---|---|---|---|---|---|---|
| ASN.1 (BER, PER or OER encoding) | NULL type | BOOLEAN: BER: as 1 byte in binary form;PER: as 1 bit;OER: as 1 byte | INTEGER: BER: variable-length big-endian binary representation (up to 221024 bits);PER Unaligned: a fixed number of bits if the integer type has a finite range; a variable number of bits otherwise;PER Aligned: a fixed number of bits if the integer type has a finite range and the size of the range is less than 65536; a variable number of octets otherwise;OER: 1, 2, or 4 octets (either signed or unsigned) if the integer type has a finite range that fits in that number of octets; a variable number of octets otherwise | REAL:base-10 real values are represented as character strings in ISO 6093 format;binary real values are represented in a binary format that includes the mantissa, the base (2, 8, or 16), and the exponent;the special values NaN, -INF, +INF, and negative zero are also supported | Multiple valid types (VisibleString, PrintableString, GeneralString, UniversalString, UTF8String) | Data specifications SET OF (unordered) and SEQUENCE OF (guaranteed order) | User definable type |
| BSON | `\x0A` (1 byte) | True: `\x08\x01` False: `\x08\x00` (2 bytes) | int32: 32-bit little-endian 2's complement or int64: 64-bit little-endian 2's complement | Double: little-endian binary64 | UTF-8-encoded, preceded by int32-encoded string length in bytes | BSON embedded document with numeric keys | BSON embedded document |
| Concise Binary Object Representation (CBOR) | `\xf6` (1 byte) | True: `\xf5`False: `\xf4` (1 byte) | Small positive/negative `\x00`–`\x17` & `\x20`–`\x37` (1 byte)8-bit: positive `\x18`, negative `\x38` (+ 1 byte)16-bit: positive `\x19`, negative `\x39` (+ 2 bytes)32-bit: positive `\x1A`, negative `\x3A` (+ 4 bytes)64-bit: positive `\x1B`, negative `\x3B` (+ 8 bytes)Negative x encoded as (−x − 1) | IEEE half/single/double `\xf9`–`\xfb` (+ 2–8 bytes)Decimals and bigfloats (4+ bytes) encoded as `\xc4` tag + 2-item array of integer mantissa & exponent | Length and content (1–9 bytes overhead)Bytestring `\x40`–`\x5f`UTF-8 `\x60`–`\x7f`Indefinite partial strings `\x5f` and `\x7f` stitched together until `\xff`. | Length and items `\x80`–`\x9e`Indefinite list `\x9f` terminated by `\xff` entry. | Length (in pairs) and items `\xa0`–`\xbe`Indefinite map `\xbf` terminated by `\xff` key. |
| Efficient XML Interchange (EXI) (Unpreserved lexical values format) | xsi:nil is not allowed in binary context. | 1–2 bit integer interpreted as boolean. | Boolean sign, plus arbitrary length 7-bit octets, parsed until most-significant bit is 0, in little-endian. The schema can set the zero-point to any arbitrary number. Unsigned skips the boolean flag. | Float: integer mantissa and integer exponent.Decimal: boolean sign, integer whole value, integer fractional. | Length prefixed integer-encoded Unicode. Integers may represent enumerations or string table entries instead. | Length prefixed set of items. | Not in protocol. |
| FlatBuffers | Encoded as absence of field in parent object | True: `\x01`False: `\x00` (1 byte) | Little-endian 2's complement signed and unsigned 8/16/32/64 bits | Floats: little-endian binary32Doubles: little-endian binary64 | UTF-8-encoded, preceded by 32-bit integer length of string in bytes | Vectors of any other type, preceded by 32-bit integer length of number of elements | Tables (schema defined types) or Vectors sorted by key (maps / dictionaries) |
| Ion | `\x0f` | True: `\x11`False: `\x10` | Positive `\x2x`, negative `\x3x`Zero is always encoded in tag byte.BigInts over 13 bytes (104 bits) have 1+ byte overhead for length | `\x44` (32-bit float)`\x48` (64-bit float)Zero is always encoded in tag byte. | UTF-8: `\x8x`Other strings: `\x9x`Arbitrary length and overhead | `\xbx` Arbitrary length and overhead. Length in octets. | Structs (numbered fields): `\xdx`Annotations (named fields): `\xex` |
| MessagePack | `\xc0` | True: `\xc3`False: `\xc2` | Single byte "fixnum" (values −32 – 127)*or* typecode (1 byte) + big-endian (u)int8/16/32/64 | Typecode (1 byte) + IEEE single/double | Typecode + up to 15 bytes*or* typecode + length as uint8/16/32 + bytes; encoding is unspecified | As "fixarray" (single-byte prefix + up to 15 array items)*or* typecode (1 byte) + 2–4 bytes length + array items | As "fixmap" (single-byte prefix + up to 15 key-value pairs)*or* typecode (1 byte) + 2–4 bytes length + key-value pairs |
| Netstrings | Not in protocol. | Not in protocol. | Not in protocol. | Not in protocol. | Length-encoded as an ASCII string + ':' + data + ',' Length counts only octets between ':' and ',' | Not in protocol. | Not in protocol. |
| OGDL Binary |   |   |   |   |   |   |   |
| Property list (binary format) |   |   |   |   |   |   |   |
| Protocol Buffers |   |   | Variable encoding length signed 32-bit: varint encoding of "ZigZag"-encoded value `(n << 1) XOR (n >> 31)`Variable encoding length signed 64-bit: varint encoding of "ZigZag"-encoded `(n << 1) XOR (n >> 63)`Constant encoding length 32-bit: 32 bits in little-endian 2's complementConstant encoding length 64-bit: 64 bits in little-endian 2's complement | Floats: little-endian binary32Doubles: little-endian binary64 | UTF-8-encoded, preceded by varint-encoded integer length of string in bytes | Repeated value with the same tag or, for varint-encoded integers only, values packed contiguously and prefixed by tag and total byte length | —N/a |
| Smile | `\x21` | True: `\x23`False: `\x22` | Single byte "small" (values −16 – 15 encoded as `\xc0`–`\xdf`),zigzag-encoded `varint`s (1–11 data bytes), or `BigInteger` | IEEE single/double, `BigDecimal` | Length-prefixed "short" Strings (up to 64 bytes), marker-terminated "long" Strings and (optional) back-references | Arbitrary-length heterogenous arrays with end-marker | Arbitrary-length key/value pairs with end-marker |
| Structured Data eXchange Formats (SDXF) |   |   | Big-endian signed 24-bit or 32-bit integer | Big-endian IEEE double | Either UTF-8 or ISO 8859-1 encoded | List of elements with identical ID and size, preceded by array header with int16 length | Chunks can contain other chunks to arbitrary depth. |
| Thrift |   |   |   |   |   |   |   |

1. Any XML based representation can be compressed, or generated as, using EXI – *"Efficient XML Interchange (EXI) Format 1.0 (Second Edition)".* – which is a "Schema Informed" (as opposed to schema-required, or schema-less) binary compression standard for XML.
2. All basic Ion types have a null variant, as its 0xXf tag. Any tag beginning with 0x0X other than 0x0f defines ignored padding.
3. Interpretation of Netstrings is entirely application- or schema-dependent.
