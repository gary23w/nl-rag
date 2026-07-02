---
title: "MessagePack"
source: https://en.wikipedia.org/wiki/MessagePack
domain: messagepack
license: CC-BY-SA-4.0
tags: messagepack format, binary json, compact serialization, binary encoding
fetched: 2026-07-02
---

# MessagePack

**MessagePack** is a computer data interchange format. It is a binary form for representing simple data structures like arrays and associative arrays. MessagePack aims to be as compact and simple as possible. The official implementation is available in a variety of languages such as C, C++, C#, D, Erlang, Go, Haskell, Java, JavaScript (NodeJS), Lua, OCaml, Perl, PHP, Python, Ruby, Rust, Scala, Smalltalk, and Swift.

## Data types and syntax

Data structures processed by MessagePack loosely correspond to those used in JSON format. They consist of the following element types:

- nil
- bool, Boolean (`true` and `false`)
- int, integer (up to 64 bits signed or unsigned)
- float, floating point numbers (IEEE single/double precision)
- str, UTF-8 string
- bin, binary data (up to 232 − 1 bytes)
- array
- map, an associative array
- ext (arbitrary data of an application-defined format, up to 232 − 1 bytes)
- timestamp (ext type = −1) (up to 64-bit seconds and 32-bit nanoseconds)

## Comparison to other formats

MessagePack is more compact than JSON, but imposes limitations on array and integer sizes. On the other hand, it allows binary data and non-UTF-8 strings. In JSON, map keys have to be strings, but MessagePack has no such limitation, and any type can be a map key, including types like maps and arrays, and, like YAML, numbers.

Compared to BSON, MessagePack is more space-efficient. BSON is designed for fast in-memory manipulation, whereas MessagePack is designed for efficient transmission over the wire. For example, BSON requires null terminators at the end of all strings and inserts string indexes for list elements, while MessagePack does not. BSON represents both arrays and maps internally as documents, which are maps, where an array is a map with keys as decimal strings counting up from 0. MessagePack on the other hand represents both maps and arrays as arrays, where each map key–value pair is contiguous, making odd items keys and even items values.

The Protocol Buffers format provides a significantly more compact transmission format than MessagePack because it does not transmit field names. However, while JSON and MessagePack aim to serialize arbitrary data structures with type tags, Protocol Buffers requires a schema to define the data types. Protocol Buffers compiler creates boilerplate code in the target language to facilitate integration of serialization into the application code; MessagePack returns only a dynamically typed data structure and provides no automatic structure checks.

MessagePack is referenced in RFC 7049 of CBOR.
