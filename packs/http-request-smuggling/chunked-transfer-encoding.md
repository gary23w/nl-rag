---
title: "Chunked transfer encoding"
source: https://en.wikipedia.org/wiki/Chunked_transfer_encoding
domain: http-request-smuggling
license: CC-BY-SA-4.0
tags: http request smuggling, content length transfer encoding, proxy desynchronization, request boundary parsing
fetched: 2026-07-02
---

# Chunked transfer encoding

**Chunked transfer encoding** is a streaming data transfer mechanism available in Hypertext Transfer Protocol (HTTP) version 1.1, defined in RFC 9112 §7.1. In chunked transfer encoding, the data stream is divided into a series of non-overlapping "chunks". The chunks are sent out and received independently of one another. At any given time, no knowledge of the data stream outside the currently-being-processed chunk is necessary for either the sender or the receiver.

Each chunk is preceded by its size in bytes and transmission ends when a zero-length chunk is received. The *chunked* keyword in the Transfer-Encoding header is used to indicate chunked transfer.

Chunked transfer encoding is not supported in HTTP/2, which provides its own mechanisms for data streaming.

## Rationale

The introduction of chunked encoding provided various benefits:

- Chunked transfer encoding allows a server to maintain an HTTP persistent connection for dynamically generated content. In this case, the HTTP Content-Length header cannot be used to delimit the content and the next HTTP request/response, as the content size is not yet known. Chunked encoding has the benefit that it is not necessary to generate the full content before writing the header, as it allows streaming of content as chunks and explicitly signaling the end of the content, making the connection available for the next HTTP request/response.
- Chunked encoding allows the sender to send additional header fields after the message body. This is important in cases where values of a field cannot be known until the content has been produced, such as when the content of the message must be digitally signed. Without chunked encoding, the sender would have to buffer the content until it was complete in order to calculate a field value and send it before the content.

## Applicability

For version 1.1 of the HTTP protocol, the chunked transfer mechanism is considered to be always and anyway acceptable, even if not listed in the Transfer-Encoding (TE) request header field, and when used with other transfer mechanisms, should always be applied last to the transferred data and never more than one time. This transfer encoding method also allows additional entity header fields to be sent after the last chunk if the client specified the "trailers" parameter as an argument of the TE request field. The origin server of the response can also decide to send additional entity trailers even if the client did not specify the "trailers" parameter, but only if the metadata is optional (i.e. the client can use the received entity without them). Whenever the trailers are used, the server should list their names in the Trailer header field; three header field types are specifically prohibited from appearing as a trailer field: Content-Length, Trailer, and Transfer-Encoding.

## Format

If a Transfer-Encoding field with a value of "chunked" is specified in an HTTP message (either a request sent by a client or the response from the server), the body of the message consists of one or more chunks and one terminating chunk with an optional trailer before the final ␍␊ sequence (i.e. carriage return followed by line feed).

Each chunk starts with the number of octets of the data it embeds expressed as a hexadecimal number in ASCII followed by optional parameters (*chunk extension*) and a terminating ␍␊ sequence, followed by the chunk data. The chunk is terminated by ␍␊.

If chunk extensions are provided, the chunk size is terminated by a semicolon and followed by the parameters, each also delimited by semicolons. Each parameter is encoded as an extension name followed by an optional equal sign and value. These parameters could be used for a running message digest or digital signature, or to indicate an estimated transfer progress, for instance.

The terminating chunk is a special chunk of zero length. It may contain a trailer, which consists of a (possibly empty) sequence of entity header fields. Normally, such header fields would be sent in the message's header; however, it may be more efficient to determine them after processing the entire message entity. In that case, it is useful to send those headers in the trailer.

Header fields that regulate the use of trailers are *Transfer-Encoding* with the "trailers" parameter (used in requests) and *Trailer* (used in responses).

## Use with compression

HTTP servers often use compression to optimize transmission, for example with Content-Encoding: gzip or Content-Encoding: deflate. If both compression and chunked encoding are enabled, then the content stream is first compressed, then chunked; so the chunk encoding itself is not compressed, and the data in each chunk is compressed holistically (i.e. based on the whole content). The remote endpoint then decodes the stream by concatenating the chunks and decompressing the result.

## Example

### Encoded data

The following example contains three chunks of size 4, 7, and 11 (hexadecimal "B") octets of data.

```
4␍␊Wiki␍␊7␍␊pedia i␍␊B␍␊n ␍␊chunks.␍␊0␍␊␍␊
```

Below is an annotated version of the encoded data.

```
4␍␊            (chunk size is four octets)
Wiki           (four octets of data)
␍␊             (end of chunk)

7␍␊            (chunk size is seven octets)
pedia i        (seven octets of data)
␍␊             (end of chunk)

B␍␊            (chunk size is eleven octets)
n ␍␊chunks.    (eleven octets of data)
␍␊             (end of chunk)

0␍␊            (chunk size is zero octets, no more chunks)
␍␊             (end of final chunk with zero data octets)
```

Note: Each chunk's size excludes the two ␍␊ bytes that terminate the data of each chunk.

### Decoded data

Decoding the above example produces the following octets:

```
Wikipedia in ␍␊chunks.
```

The bytes above are typically displayed as

```
Wikipedia in 
chunks. 
```
