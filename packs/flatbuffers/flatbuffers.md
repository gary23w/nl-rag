---
title: "FlatBuffers"
source: https://en.wikipedia.org/wiki/FlatBuffers
domain: flatbuffers
license: CC-BY-SA-4.0
tags: google flatbuffers, zero-copy serialization, flatbuffers schema, memory-efficient format
fetched: 2026-07-02
---

# FlatBuffers

**FlatBuffers** is a free software library implementing a serialization format similar to Protocol Buffers, Thrift, Apache Avro, SBE, and Cap'n Proto, primarily written by Wouter van Oortmerssen and open-sourced by Google. It supports “zero-copy” deserialization, so that accessing the serialized data does not require first copying it into a separate part of memory. This makes accessing data in these formats much faster than data in formats requiring more extensive processing, such as JSON, CSV, and in many cases Protocol Buffers. Compared to other serialization formats however, the handling of FlatBuffers usually requires more code, and some operations are not possible (like some mutation operations).

The serialized format allows random access to specific data elements (e.g. individual string or integer properties) without parsing all data. Unlike Protocol Buffers, which uses variable length integers, FlatBuffers encodes integers in their native size, which favors performance but leads to longer encoded representations.

FlatBuffers can be used in software written in C++, C#, C, Go, Java, JavaScript, Kotlin, Lobster, Lua, PHP, Python, Rust, Swift, and TypeScript. The schema compiler runs on Android, Microsoft Windows, macOS, and Linux, but games and other programs use FlatBuffers for serialization work on many other operating systems as well, including iOS, Amazon's Fire OS, and Windows Phone.

Van Oortmerssen originally developed FlatBuffers for game development and similar applications.

Although FlatBuffers has its own interface definition language to define the data to be serialized with it, it also supports schemas defined in the Protocol Buffers .proto format.

## Users

Some notable users of FlatBuffers:

- Cocos2d-x, the popular free-software 2-D game programming library, uses FlatBuffers to serialize all of its game data.
- Facebook Android Client uses FlatBuffers for disk storage and communication with Facebook servers. The previously used JSON format was performing poorly.
