---
title: "Apache Avro"
source: https://en.wikipedia.org/wiki/Apache_Avro
domain: apache-avro
license: CC-BY-SA-4.0
tags: apache avro, row oriented serialization, schema registry, compact binary format, remote procedure call
fetched: 2026-07-02
---

# Apache Avro

**Avro** is a row-oriented remote procedure call and data serialization framework developed within Apache's Hadoop project. It uses JSON for defining data types and protocols, and serializes data in a compact binary format. Its primary use is in Apache Hadoop, where it can provide both a serialization format for persistent data, and a wire format for communication between Hadoop nodes, and from client programs to the Hadoop services. Avro uses a schema to structure the data that is being encoded. It has two different types of schema languages: one for human editing (Avro IDL) and another which is more machine-readable based on JSON.

It is similar to Thrift and Protocol Buffers, but does not require running a code-generation program when a schema changes (unless desired for statically-typed languages).

Apache Spark SQL can access Avro as a data source.

## Avro Object Container File

An Avro Object Container File consists of:

- A file header, followed by
- one or more file data blocks.

A file header consists of:

- Four bytes, ASCII 'O', 'b', 'j', followed by the Avro version number which is 1 (0x01) (Binary values 0x4F 0x62 0x6A 0x01).
- File metadata, including the schema definition.
- The 16-byte, randomly-generated sync marker for this file.

For data blocks Avro specifies two serialization encodings: binary and JSON. Most applications will use the binary encoding, as it is smaller and faster. For debugging and web-based applications, the JSON encoding may sometimes be appropriate.

## Schema definition

Avro schemas are defined using JSON. Schemas are composed of primitive types (null, boolean, int, long, float, double, bytes, and string) and complex types (record, enum, array, map, union, and fixed).

Simple schema example:

```mw
 {
   "namespace": "example.avro",
   "type": "record",
   "name": "User",
   "fields": [
      {"name": "name", "type": "string"},
      {"name": "favorite_number",  "type": ["null", "int"]},
      {"name": "favorite_color", "type": ["null", "string"]}
   ] 
 }
```

## Serializing and deserializing

Data in Avro might be stored with its corresponding schema, meaning a serialized item can be read without knowing the schema ahead of time.

### Example serialization and deserialization code in Python

Serialization:

```mw
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

# Need to know the schema to write. According to 1.8.2 of Apache Avro
schema = avro.schema.parse(open("user.avsc", "rb").read())

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 8, "favorite_color": "red"})
writer.close()
```

File "users.avro" will contain the schema in JSON and a compact binary representation of the data:

```mw
$ od -v -t x1z users.avro 
0000000 4f 62 6a 01 04 14 61 76 72 6f 2e 63 6f 64 65 63  >Obj...avro.codec<
0000020 08 6e 75 6c 6c 16 61 76 72 6f 2e 73 63 68 65 6d  >.null.avro.schem<
0000040 61 ba 03 7b 22 74 79 70 65 22 3a 20 22 72 65 63  >a..{"type": "rec<
0000060 6f 72 64 22 2c 20 22 6e 61 6d 65 22 3a 20 22 55  >ord", "name": "U<
0000100 73 65 72 22 2c 20 22 6e 61 6d 65 73 70 61 63 65  >ser", "namespace<
0000120 22 3a 20 22 65 78 61 6d 70 6c 65 2e 61 76 72 6f  >": "example.avro<
0000140 22 2c 20 22 66 69 65 6c 64 73 22 3a 20 5b 7b 22  >", "fields": [{"<
0000160 74 79 70 65 22 3a 20 22 73 74 72 69 6e 67 22 2c  >type": "string",<
0000200 20 22 6e 61 6d 65 22 3a 20 22 6e 61 6d 65 22 7d  > "name": "name"}<
0000220 2c 20 7b 22 74 79 70 65 22 3a 20 5b 22 69 6e 74  >, {"type": ["int<
0000240 22 2c 20 22 6e 75 6c 6c 22 5d 2c 20 22 6e 61 6d  >", "null"], "nam<
0000260 65 22 3a 20 22 66 61 76 6f 72 69 74 65 5f 6e 75  >e": "favorite_nu<
0000300 6d 62 65 72 22 7d 2c 20 7b 22 74 79 70 65 22 3a  >mber"}, {"type":<
0000320 20 5b 22 73 74 72 69 6e 67 22 2c 20 22 6e 75 6c  > ["string", "nul<
0000340 6c 22 5d 2c 20 22 6e 61 6d 65 22 3a 20 22 66 61  >l"], "name": "fa<
0000360 76 6f 72 69 74 65 5f 63 6f 6c 6f 72 22 7d 5d 7d  >vorite_color"}]}<
0000400 00 05 f9 a3 80 98 47 54 62 bf 68 95 a2 ab 42 ef  >......GTb.h...B.<
0000420 24 04 2c 0c 41 6c 79 73 73 61 00 80 04 02 06 42  >$.,.Alyssa.....B<
0000440 65 6e 00 10 00 06 72 65 64 05 f9 a3 80 98 47 54  >en....red.....GT<
0000460 62 bf 68 95 a2 ab 42 ef 24                       >b.h...B.$<
0000471
```

Deserialization:

```mw
# The schema is embedded in the data file
reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)
reader.close()
```

This outputs:

```mw
{'name': 'Alyssa', 'favorite_number': 256, 'favorite_color': None}
{'name': 'Ben', 'favorite_number': 8, 'favorite_color': 'red'}
```

## Languages with APIs

Though theoretically any language could use Avro, the following languages have APIs written for them:

- C
- C++
- C#
- Elixir
- Go
- Haskell
- Java
- JavaScript
- Perl
- PHP
- Python
- Ruby
- Rust
- Scala

## Avro IDL

In addition to supporting JSON for type and protocol definitions, Avro includes experimental support for an alternative interface description language (IDL) syntax known as Avro IDL. Previously known as GenAvro, this format is designed to ease adoption by users familiar with more traditional IDLs and programming languages, with a syntax similar to C/C++, Protocol Buffers and others.

## Logo

The original Apache Avro logo was from the defunct British aircraft manufacturer Avro (originally A.V. Roe and Company).

The Apache Avro logo was updated to an original design in late 2023.
