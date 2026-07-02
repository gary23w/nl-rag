---
title: "BSON"
source: https://en.wikipedia.org/wiki/BSON
domain: aws-documentdb
license: CC-BY-SA-4.0
tags: aws documentdb, amazon documentdb, managed document database, mongodb-compatible database
fetched: 2026-07-02
---

# BSON

**BSON** (/ˈbiːsən/; **Binary JSON**) is a computer data interchange format extending JSON. It is a binary form for representing simple or complex data structures including associative arrays (also known as name-value pairs), integer indexed arrays, and a suite of fundamental scalar types. BSON originated in 2009 at MongoDB. Several scalar data types are of specific interest to MongoDB and the format is used both as a data storage and network transfer format for the MongoDB database, but it can be used independently outside of MongoDB. Implementations are available in a variety of languages such as C, C++, C#, D, Delphi, Erlang, Go, Haskell, Java, JavaScript, Julia, Lua, OCaml, Perl, PHP, Python, Ruby, Rust, Scala, Smalltalk, and Swift.

## Data types and syntax

BSON has a published specification. The topmost element in the structure must be of type BSON object and contains 1 or more elements, where an element consists of a field name, a type, and a value. Field names are strings. Types include:

- Unicode string (using the UTF-8 encoding)
- 32-bit integer
- 64-bit integer
- double (64-bit IEEE 754 floating point number, including NaN/Inf)
- decimal128 (128-bit IEEE 754-2008 floating point number; binary integer decimal (BID) variant), suitable as a carrier for decimal-place sensitive financial data and arbitrary precision numerics with 34 decimal digits of precision, a max value of approximately 106145
- datetime in UTC (signed 64-bit integer number of milliseconds since the Unix epoch)
- byte array (for arbitrary binary data)
- Boolean (`true` and `false`)
- null
- BSON object
- BSON array
- JavaScript code
- MD5 binary data
- Regular expression (Perl compatible regular expressions ("PCRE") version 8.41 with UTF-8 support)

An important differentiator to JSON is that BSON contains types not present in JSON (e.g. datetime, byte array, and proper IEEE 754 floats) and offers type-strict handling for several numeric types instead of a universal "number" type. For situations where these additional types need to be represented in a textual way, MongoDB's Extended JSON format can be used.

## Efficiency

Compared to JSON, BSON is designed to be efficient both in storage space and scan-speed. Large elements in a BSON document are prefixed with a length field to facilitate scanning. In some cases, BSON will use more space than JSON due to the length prefixes and explicit array indices.

## Example

A document such as `{"hello": "world"}` will be stored as:

```mw
\x16\x00\x00\x00          // total document size
\x02                      // 0x02 = type String
hello\x00                 // field name
\x06\x00\x00\x00world\x00 // field value (size of value, value, null terminator)
\x00                      // 0x00 = type EOO ('end of object')
```
