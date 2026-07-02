---
title: "Protocol Buffers Documentation"
source: https://protobuf.dev/
domain: protocol-buffers-idl
license: CC-BY-SA-4.0
tags: protocol buffers, protobuf idl, interface description language, binary serialization schema
fetched: 2026-07-02
---

# Protocol Buffers

Protocol Buffers are language-neutral, platform-neutral extensible mechanisms for serializing structured data.

## What Are Protocol Buffers?

Protocol buffers are Google’s language-neutral, platform-neutral, extensible mechanism for serializing structured data – think XML, but smaller, faster, and simpler. You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages.

## Pick Your Favorite Language

Protocol buffers support generated code in C++, C#, Dart, Go, Java, Kotlin, Objective-C, Python, Rust, and Ruby. With proto3, you can also work with PHP.

## Example Implementation

```proto
edition = "2024";

message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
```

**Figure 1.** A proto definition.

```java
// Java code
Person john = Person.newBuilder()
    .setId(1234)
    .setName("John Doe")
    .setEmail("jdoe@example.com")
    .build();
output = new FileOutputStream(args[0]);
john.writeTo(output);
```

**Figure 2.** Using a generated class to persist data.

```cpp
// C++ code
Person john;
fstream input(argv[1],
    ios::in | ios::binary);
john.ParseFromIstream(&input);
id = john.id();
name = john.name();
email = john.email();
```

**Figure 3.** Using a generated class to parse persisted data.

## How Do I Start?

1. Download and install the protocol buffer compiler.
2. Read the overview.
3. Try the tutorial for your chosen language.
