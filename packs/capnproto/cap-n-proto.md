---
title: "Cap'n Proto"
source: https://en.wikipedia.org/wiki/Cap%27n_Proto
domain: capnproto
license: CC-BY-SA-4.0
tags: capn proto, cap n proto, zero-copy format, capability-based rpc
fetched: 2026-07-02
---

# Cap'n Proto

**Cap’n Proto** is a data serialization format and Remote Procedure Call (RPC) framework for exchanging data between computer programs. The high-level design focuses on speed and security, making it suitable for network as well as inter-process communication. Cap'n Proto was created by the former maintainer of Google's popular Protocol Buffers framework Kenton Varda, and was designed to avoid some of its perceived shortcomings.

## Technical overview

### IDL Schema

Like most RPC frameworks dating as far back as Sun RPC and OSF DCE RPC (and their object-based descendants CORBA and DCOM), Cap'n Proto uses an Interface Description Language (IDL) to generate RPC libraries in a variety of programming languages - automating many low level details such as handling network requests, converting between data types, etc. The Cap'n Proto interface schema uses a C-like syntax and supports common primitives data types (booleans, integers, floats, etc.), compound types (structs, lists, enums), as well as generics and dynamic types. Cap'n Proto also supports object-oriented features such as multiple inheritance, which has been criticized for its complexity.

```mw
@0xa558ef006c0c123; # Unique identifiers are manually or automatically assigned to files and compound types

struct Date @0x5c5a558ef006c0c1 {
  year @0 :Int16; # @n marks order values were added to the schema
  month @1 :UInt8;
  day @2 :UInt8;
}

struct Contact @0xf032a54bcb3667e0 {
  name @0 :Text;
  birthday @2 :Date; # fields can be added anywhere in the definition, but their numbering must reflect the order in which they were added

  phones @1 :List(PhoneNumber);

  struct PhoneNumber { # Compound types without a static ID cannot be renamed, as automatic IDs are deterministically generated
    number @0 :Text;
    type @1 :PhoneType = mobile; # Default value

    enum PhoneType {
      mobile @0;
      landline @1;
    }
  }
}
```

Values in Cap'n Proto messages are represented in binary, as opposed to text encoding used by "human-readable" formats such as JSON or XML. Cap'n Proto tries to make the storage/network protocol appropriate as an in-memory format, so that no translation step is needed when reading data into memory or writing data out of memory. For example, the representation of numbers (endianness) was chosen to match the representation the most popular CPU architectures. When the in-memory and wire-protocol representations match, Cap'n Proto can avoid copying and encoding data when creating or reading a message and instead point to the location of the value in memory. Cap'n Proto also supports random access to data, meaning that any field can be read without having to read the entire message.

Unlike other binary serialization protocols such as XMI, Cap'n Proto considers fine-grained data validation at the RPC level an anti-feature that limits a protocol's ability to evolve. This was informed by experiences at Google where simply changing a field from *mandatory* to *optional* would cause complex operational failures. Cap'n Proto schemas are designed to be flexible as possible and pushes data validation to the application level, allowing arbitrary renaming of fields, adding new fields, and making concrete types generic. Cap'n Proto does, however, validate pointer bounds and type check individual values when they are first accessed.

Enforcing complex schema constraints would also incur significant overhead, negating the benefits of reusing in-memory data structures and preventing random access to data. Cap'n Proto protocol is *theoretically* suitable for very fast inter-process communication (IPC) via immutable shared memory, but as of October 2020 none of the implementations support data passing via shared memory. However, Cap'n Proto is still generally considered faster than Protocol Buffers and similar RPC libraries.

### Networking

Cap'n Proto RPC is network aware: supporting both handling of disconnects and promise pipelining, wherein a server pipes the output of one function into another function. This saves a client a round trip per successive call to the server without having to provide a dedicated API for every possible call graph. Cap'n Proto can be layered on top of TLS and support for the Noise Protocol Framework is on the roadmap. Cap'n Proto RPC is transport agnostic, with the mainline implementation supporting WebSockets, HTTP, TCP, and UDP.

### Capability security

The Cap'n Proto RPC standard has a rich capability security model based on the CapTP protocol used by the E programming language.

As of October 2020, the reference implementation only supports level 2.

## Comparison to other serialization formats

Cap'n Proto is often compared to other zero-copy serialization formats, such as Google's FlatBuffers and Simple Binary Encoding (SBE).

## Adoption

Cap'n Proto was originally created for Sandstorm.io, a startup offering a web application hosting platform with capability-based security. After Sandstorm.io failed commercially, the development team was acqui-hired by Cloudflare, which uses Cap'n Proto internally.
