---
title: "Stream (abstract data type)"
source: https://en.wikipedia.org/wiki/Stream_(abstract_data_type)
domain: coinduction
license: CC-BY-SA-4.0
tags: coinduction principle, corecursion scheme, coinductive definition, infinite data structure
fetched: 2026-07-02
---

# Stream (abstract data type)

In type theory and functional programming, a **stream** is a potentially infinite analog of a list, given by the coinductive definition:

```mw
data Stream α = Nil | Cons α (Stream α)
```

Generating and computing with streams requires lazy evaluation, either implicitly in a lazily evaluated language or by creating and forcing thunks in an eager language. In total languages they must be defined as codata and can be iterated over using (guarded) corecursion.

Java provides the Stream interface under the java.util.stream namespace.

JavaScript provides the ReadableStream, WritableStream and TransformStream interfaces.

Python have the StreamReader and StreamWriter classes in the asyncio module.

.NET provides the abstract class Stream which is implemented by classes such as FileStream and MemoryStream.

In Rust a struct can implement the Read trait. There is also the Cursor struct wraps an in-memory buffer.
