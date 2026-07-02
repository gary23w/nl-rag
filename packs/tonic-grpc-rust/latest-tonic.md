---
title: "tonic"
source: https://docs.rs/tonic/latest/tonic/
domain: tonic-grpc-rust
license: CC-BY-SA-4.0
tags: tonic grpc, rust grpc library, protobuf rust, tonic service
fetched: 2026-07-02
---

# Crate tonic

Source

Expand description

A Rust implementation of gRPC, a high performance, open source, general RPC framework that puts mobile and HTTP/2 first.

`tonic` is a gRPC over HTTP/2 implementation focused on **high performance**, **interoperability**, and **flexibility**. This library was created to have first class support of async/await and to act as a core building block for production systems written in Rust.

## §Examples

Examples can be found in the `tonic-examples` crate.

## §Getting Started

Follow the instructions in the `tonic-build` crate documentation.

## §Feature Flags

- `transport`: Enables the fully featured, batteries included client and server implementation based on `hyper`, `tower` and `tokio`. This enables `server` and `channel` features. Enabled by default.
- `server`: Enables just the full featured server portion of the `transport` feature.
- `channel`: Enables just the full featured channel portion of the `transport` feature.
- `router`: Enables the `axum` based service router. Enabled by default.
- `codegen`: Enables all the required exports and optional dependencies required for `tonic-build`. Enabled by default.
- `tls-ring`: Enables the `rustls` based TLS options for the `transport` feature using the `ring` libcrypto provider. Not enabled by default.
- `tls-aws-lc`: Enables the `rustls` based TLS options for the `transport` feature using the `aws-lc-rs` libcrypto provider. Not enabled by default.
- `tls-native-roots`: Adds system trust roots to `rustls`-based gRPC clients using the `rustls-native-certs` crate. Not enabled by default.
- `tls-webpki-roots`: Add the standard trust roots from the `webpki-roots` crate to `rustls`-based gRPC clients. Not enabled by default.
- `tls-connect-info`: Adds additional implementations of `Connected` on common TLS connectors. Not enabled by default, unless any of the other `tls-*` features are enabled. This feature is useful for when trying to use a custom TLS connector with `connect_with_connector` without enabling any `tls-*` features.
- `gzip`: Enables compressing requests, responses, and streams. Depends on `flate2`. Not enabled by default.
- `deflate`: Enables compressing requests, responses, and streams. Depends on `flate2`. Not enabled by default.
- `zstd`: Enables compressing requests, responses, and streams. Depends on `zstd`. Not enabled by default.

## §Structure

### §Generic implementation

The main goal of `tonic` is to provide a generic gRPC implementation over HTTP/2 framing. This means at the lowest level this library provides the ability to use a generic HTTP/2 implementation with different types of gRPC encodings formats. Generally, some form of codegen should be used instead of interacting directly with the items in `client` and `server`.

### §Transport

The `transport` module contains a fully featured HTTP/2.0 `Channel` (gRPC terminology) and `Server`. These implementations are built on top of `tokio`, `hyper` and `tower`. It also provides many of the features that the core gRPC libraries provide such as load balancing, tls, timeouts, and many more. This implementation can also be used as a reference implementation to build even more feature rich clients and servers. This module also provides the ability to enable TLS using `rustls`, via the `tls` feature flag.

## §Code generated client/server configuration

### §Max Message Size

Currently, both servers and clients can be configured to set the max message encoding and decoding size. This will ensure that an incoming gRPC message will not exhaust the systems memory. By default, the decoding message limit is `4MB` and the encoding limit is `usize::MAX`.

## Modules

**body**

HTTP specific body utilities.

**client**

Generic client implementation.

**codec**

Generic encoding and decoding.

**metadata**

Contains data structures and utilities for handling gRPC custom metadata.

**server**

Generic server implementation.

**service**

Utilities for using Tower services with Tonic.

**transport`server` or `channel`**

Batteries included server and client.

## Macros

**include_file_descriptor_set**

Include an encoded

prost_types::FileDescriptorSet

as a

&'static [u8]

. The parameter must be the stem of the filename passed to

file_descriptor_set_path

for the

tonic-build::Builder

, excluding the

.bin

extension.

**include_proto**

Include generated proto server and client items.

## Structs

**ConnectError**

Wrapper type to indicate that an error occurs during the connection process, so that the appropriate gRPC Status can be inferred.

**Extensions**

A type map of protocol extensions.

**GrpcMethod**

A gRPC Method info extension.

**Request**

A gRPC request and metadata from an RPC call.

**Response**

A gRPC response and metadata from an RPC call.

**Status**

A gRPC status describing the result of an RPC call.

**Streaming**

Streaming requests and responses.

**TimeoutExpired**

Error returned if a request didn’t complete within the configured timeout.

## Enums

**Code**

gRPC status codes used by

Status

.

## Traits

**IntoRequest**

Trait implemented by RPC request types.

**IntoStreamingRequest**

Trait implemented by RPC streaming request types.

## Type Aliases

**Result**

Result

is a type that represents either success (

Ok

) or failure (

Err

). By default, the Err value is of type

Status

but this can be overridden if desired.

## Attribute Macros

**async_trait`codegen`**

A re-export of

async-trait

for use with codegen.
