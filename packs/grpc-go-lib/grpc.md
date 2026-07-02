---
title: "gRPC"
source: https://en.wikipedia.org/wiki/GRPC
domain: grpc-go-lib
license: CC-BY-SA-4.0
tags: grpc go, go rpc library, protobuf go, grpc streaming go
fetched: 2026-07-02
---

# gRPC

**gRPC** (recursive acronym for **gRPC Remote Procedure Calls**) is a cross-platform high-performance remote procedure call (RPC) framework. gRPC was initially created by Google, but is open source and is used in many organizations. Use cases range from microservices to the "last mile" of computing (mobile, web, and the Internet of things).

gRPC uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts. It generates cross-platform client and server bindings for many languages. The most common usage scenarios include connecting services in a microservices style architecture, or connecting mobile device clients to backend services.

gRPC's use of HTTP trailers makes it impossible to implement a gRPC client in a browser, instead requiring a proxy.

## History

From about 2001, Google created a general-purpose RPC infrastructure called Stubby to connect the large number of microservices running within and across its data centers. In March 2015, Google decided to build the next version of Stubby and make it open source. The result was gRPC.

## Authentication

gRPC supports the usage of Transport Layer Security (TLS) and token-based authentication. Connection to Google services must use TLS. There are two types of credentials: channel credentials and call credentials.

For token-based authorization, gRPC provides Server Interceptor and a Client Interceptor.

## Encoding

gRPC uses Protocol Buffers to encode data. Protocol buffers provide a serialization format and an interface definition language.

## Testing

Some of the software tools used for testing gRPC implementations include Postman, ezy, Insomnia, and Step CI.

## Adoption

Many organizations use gRPC, including Uber, Square, Netflix, IBM, CoreOS, Docker, CockroachDB, Arista Networks, Cisco, Juniper Networks, Spotify, Zalando, Dropbox, and Google as the original developer.

The open source project u-bmc uses gRPC to replace Intelligent Platform Management Interface (IPMI). On 8 January 2019, Dropbox announced that the next version of "Courier", their RPC framework at the core of their service-oriented architecture (SOA), would be migrated to be based on gRPC, primarily because it aligned well with their existing custom RPC frameworks.

## Alternatives

- Cap'n Proto
- Apache Thrift
- Apache Avro
- JSON-RPC
- XML-RPC
