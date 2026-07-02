---
title: "JSON streaming"
source: https://en.wikipedia.org/wiki/JSON_streaming
domain: jq-json
license: CC-BY-SA-4.0
tags: jq json, json processor, command-line json, json filter
fetched: 2026-07-02
---

# JSON streaming

**JSON streaming** comprises communications protocols to delimit JSON objects built upon lower-level stream-oriented protocols (such as TCP), that ensures individual JSON objects are recognized, when the server and clients use the same one (e.g. implicitly coded in). This is necessary as JSON is a non-concatenative protocol (the concatenation of two JSON objects does not produce a valid JSON object).

## Introduction

JSON is a popular format for exchanging object data between systems. Frequently there's a need for a stream of objects to be sent over a single connection, such as a stock ticker or application log records. In these cases there's a need to identify where one JSON encoded object ends and the next begins. Technically this is known as framing.

There are four common ways to achieve this:

- Send the JSON objects *formatted without newlines* and use a newline as the delimiter.
- Send the JSON objects concatenated with a record separator control character as the delimiter.
- Send the JSON objects concatenated with no delimiters and rely on a streaming parser to extract them.
- Send the JSON objects prefixed with their length and rely on a streaming parser to extract them.

### Comparison

Line-delimited JSON works very well with traditional line-oriented tools.

Concatenated JSON works with pretty-printed JSON but requires more effort and complexity to parse. It doesn't work well with traditional line-oriented tools. Concatenated JSON streaming is a superset of line-delimited JSON streaming.

Length-prefixed JSON works with pretty-printed JSON. It doesn't work well with traditional line-oriented tools, but may offer performance advantages over line-delimited or concatenated streaming. It can also be simpler to parse.

## Approaches

### Newline-delimited JSON

Two terms for equivalent formats of line-delimited JSON are:

- Newline delimited (NDJSON) - The old name was Line delimited JSON (LDJSON).
- JSON lines (JSONL), that is the current (2025) and most used standard, in Big Data and other applications.

Streaming makes use of the fact that the JSON format does not allow return and newline characters within primitive values (in strings those must be escaped as `\r` and `\n`, respectively) and that most JSON formatters default to not including any whitespace, including returns and newlines. These features allow the newline character or return and newline character sequence to be used as a delimiter.

This example shows two JSON objects (the implicit newline characters at the end of each line are not shown):

```mw
{"some":"thing\n"}
{"may":{"include":"nested","objects":["and","arrays"]}}
```

The use of a newline as a delimiter enables this format to work very well with traditional line-oriented Unix tools.

A log file, for example, might look like:

```mw
{"ts":"2020-06-18T10:44:12","started":{"pid":45678}}
{"ts":"2020-06-18T10:44:13","logged_in":{"username":"foo"},"connection":{"addr":"1.2.3.4","port":5678}}
{"ts":"2020-06-18T10:44:15","registered":{"username":"bar","email":"bar@example.com"},"connection":{"addr":"2.3.4.5","port":6789}}
{"ts":"2020-06-18T10:44:16","logged_out":{"username":"foo"},"connection":{"addr":"1.2.3.4","port":5678}}
```

which is very easy to sort by date, grep for usernames, actions, IP addresses, etc.

#### Compatibility

Line-delimited JSON can be read by a parser that can handle concatenated JSON. Concatenated JSON that contains newlines *within* a JSON object can't be read by a line-delimited JSON parser.

The terms "line-delimited JSON" and "newline-delimited JSON" are often used without clarifying if embedded newlines are supported.

In the past the newline delimited JSON specification allowed comments to be embedded if the first two characters of a given line were "//". This could not be used with standard JSON parsers if comments were included. Current version of the specification ("NDJSON - Newline delimited JSON ") no longer includes comments.

Concatenated JSON can be converted into line-delimited JSON by a suitable JSON utility such as jq. For example

```mw
jq --compact-output . < concatenated.json > lines.json
```

### Record separator-delimited JSON

Record separator-delimited JSON streaming allows JSON text sequences to be delimited without the requirement that the JSON formatter exclude whitespace. Since JSON text sequences cannot contain control characters, a record separator character can be used to delimit the sequences. In addition, it is suggested that each JSON text sequence be followed by a line feed character to allow proper handling of top-level JSON objects that are not self delimiting (numbers, true, false, and null).

This format is also known as JSON Text Sequences or MIME type `application/json-seq`, and is formally described in IETF RFC 7464.

The example below shows two JSON objects with ␞ representing the record separator control character and ␊ representing the line feed character:

```mw
␞{"some":"thing\n"}␊
␞{
  "may": {
    "include": "nested",
    "objects": [
      "and",
      "arrays"
    ]
  }
}␊
```

### Concatenated JSON

Concatenated JSON streaming allows the sender to simply write each JSON object into the stream with no delimiters. It relies on the receiver using a parser that can recognize and *emit* each JSON object as the terminating character is parsed. Concatenated JSON isn't a new format, it's simply a name for streaming multiple JSON objects without any delimiters.

The advantage of this format is that it can handle JSON objects that have been formatted with embedded newline characters, e.g., pretty-printed for human readability. For example, these two inputs are both valid and produce the same output:

```mw
{"some":"thing\n"}{"may":{"include":"nested","objects":["and","arrays"]}}
```

```mw
{
  "some": "thing\n"
}
{
  "may": {
    "include": "nested",
    "objects": [
      "and",
      "arrays"
    ]
  }
}
```

Implementations that rely on line-based input may require a newline character after each JSON object in order for the object to be emitted by the parser in a timely manner. (Otherwise the line may remain in the input buffer without being passed to the parser.) This is rarely recognised as an issue because terminating JSON objects with a newline character is very common.

### Length-prefixed JSON

Length-prefixed or framed JSON streaming allows the sender to explicitly state the length of each message. It relies on the receiver using a parser that can recognize each length *n* and then read the following *n* bytes to parse as JSON.

The advantage of this format is that it can speed up parsing due to the fact that the exact length of each message is explicitly stated, rather than forcing the parser to search for delimiters. Length-prefixed JSON is also well-suited for TCP applications, where a single "message" may be divided into arbitrary chunks, because the prefixed length tells the parser exactly how many bytes to expect before attempting to parse a JSON string.

This example shows two length-prefixed JSON objects (with each length being the byte-length of the following JSON string):

```mw
18{"some":"thing\n"}55{"may":{"include":"nested","objects":["and","arrays"]}}
```

## Applications and tools

### Newline-delimited JSON

- jq can both create and read line-delimited JSON texts.
- Jackson (API) can read and write line-delimited JSON texts.
- logstash includes a json_lines codec.
- ldjson-stream module for Node.js
- ld-jsonstream dependency free module for Node.js
- json-stream-es is a JavaScript/TypeScript library (frontend and backend) that can create and read newline-delimited JSON documents.
- ArduinoJson is a C++ library that supports line-delimited JSON.
- RecordStream A set of tools to manipulate line delimited JSON (generate, transform, collect statistics, and format results).
- The Go standard library's encoding/json package can be used to read and write line-delimited JSON.
- RDF4J and Ontotext GraphDB support NDJSON for JSON-LD (called NDJSONLD) since February 2021.

### Record separator-delimited JSON

- jq can both create and read record separator-delimited JSON texts.
- json-stream-es is a JavaScript/TypeScript library (frontend and backend) that can create and read record separator-delimited JSON documents.

### Concatenated JSON

- concatjson concatenated JSON streaming parser/serializer module for Node.js
- json-stream-es is a JavaScript/TypeScript library (frontend and backend) that can create and read concatenated JSON documents.
- Jackson (API) can read and write concatenated JSON content.
- jq lightweight flexible command-line JSON processor
- Noggit Solr's streaming JSON parser for Java
- Yajl – Yet Another JSON Library. YAJL is a small event-driven (SAX-style) JSON parser written in ANSI C, and a small validating JSON generator.
- ArduinoJson is a C++ library that supports concatenated JSON.
- GSON JsonStreamParser.java can read concatenated JSON.
- json-stream is a streaming JSON parser for python.

### Length-prefixed JSON

- missive Fast, lightweight library for encoding and decoding length-prefixed JSON messages over streams
- Native messaging WebExtensions Native Messaging
