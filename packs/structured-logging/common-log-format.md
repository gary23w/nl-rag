---
title: "Common Log Format"
source: https://en.wikipedia.org/wiki/Common_Log_Format
domain: structured-logging
license: CC-BY-SA-4.0
tags: structured logging, log event schema, json log lines, log correlation
fetched: 2026-07-02
---

# Common Log Format

For computer log management, the **Common Log Format**, also known as the **NCSA Common log format**, (after NCSA HTTPd) is a historically standardized text file format from 2004 that was used by web servers when generating server log files. Because the format was standardized, the files had been readily analyzed by a variety of web analysis programs, for example Webalizer and Analog.

Each line in a file stored in the Common Log Format has the following

The format is extended by the **Combined Log Format** with referer and user-agent fields.

## Example

```
127.0.0.1 ident alice [01/May/2025:07:20:10 +0000] "GET /index.html HTTP/1.1" 200 9481
```

A field set to dash (`-`) indicates missing data.

- `127.0.0.1` is the IP address of the client (remote host) which made the request to the server.
- `ident` is the RFC 1413 identity of the client, if supplied.
- `alice` is the userid of the person requesting the document. Missing unless HTTP authentication is used.
- `[01/May/2025:07:20:10 +0000]` is the request timestamp. Here in strftime format `%d/%b/%Y:%H:%M:%S %z`.
- `"GET /index.html HTTP/1.1"` is the request line from the client. The method `GET`, `/index.html` the resource requested, and `HTTP/1.1` the HTTP protocol version.
- `200` is the HTTP status code returned to the client.
- `9481` is the response size, in bytes.

## Usage

Log files are a standard tool for computer systems developers and administrators. They record the "what happened, when, by whom" of the system. This information can record faults and help their diagnosis. It can identify security breaches and other computer misuse. It can be used for auditing. It can be used for accounting purposes.

The information stored is only available for later analysis if it is stored in a form that can be analysed. This data can be structured in many ways for analysis. For example, storing it in a relational database would force the data into a query-able format. However, it would also make it more difficult to retrieve if the computer crashed, and logging would not be available unless the database was available. A plain text format minimises dependencies on other system processes, and assists logging at all phases of computer operation, including start-up and shut-down, where such processes might be unavailable.
