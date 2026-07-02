---
title: "tower"
source: https://docs.rs/tower/latest/tower/
domain: tower-middleware
license: CC-BY-SA-4.0
tags: tower rust middleware, rust service abstraction, tower layer stack, async service trait
fetched: 2026-07-02
---

# Crate tower

Source

Expand description

`async fn(Request) -> Result<Response, Error>`

## §Overview

Tower is a library of modular and reusable components for building robust networking clients and servers.

Tower provides a simple core abstraction, the `Service` trait, which represents an asynchronous function taking a request and returning either a response or an error. This abstraction can be used to model both clients and servers.

Generic components, like `timeout`, rate limiting, and load balancing, can be modeled as `Service`s that wrap some inner service and apply additional behavior before or after the inner service is called. This allows implementing these components in a protocol-agnostic, composable way. Typically, such services are referred to as *middleware*.

An additional abstraction, the `Layer` trait, is used to compose middleware with `Service`s. If a `Service` can be thought of as an asynchronous function from a request type to a response type, a `Layer` is a function taking a `Service` of one type and returning a `Service` of a different type. The `ServiceBuilder` type is used to add middleware to a service by composing it with multiple `Layer`s.

### §The Tower Ecosystem

Tower is made up of the following crates:

- `tower` (this crate)
- `tower-service`
- `tower-layer`
- `tower-test`

Since the `Service` and `Layer` traits are important integration points for all libraries using Tower, they are kept as stable as possible, and breaking changes are made rarely. Therefore, they are defined in separate crates, `tower-service` and `tower-layer`. This crate contains re-exports of those core traits, implementations of commonly-used middleware, and utilities for working with `Service`s and `Layer`s. Finally, the `tower-test` crate provides tools for testing programs using Tower.

## §Usage

Tower provides an abstraction layer, and generic implementations of various middleware. This means that the `tower` crate on its own does *not* provide a working implementation of a network client or server. Instead, Tower’s `Service` trait provides an integration point between application code, libraries providing middleware implementations, and libraries that implement servers and/or clients for various network protocols.

Depending on your particular use case, you might use Tower in several ways:

- **Implementing application logic** for a networked program. You might use the `Service` trait to model your application’s behavior, and use the middleware provided by this crate and by other libraries to add functionality to clients and servers provided by one or more protocol implementations.
- **Implementing middleware** to add custom behavior to network clients and servers in a reusable manner. This might be general-purpose middleware (and if it is, please consider releasing your middleware as a library for other Tower users!) or application-specific behavior that needs to be shared between multiple clients or servers.
- **Implementing a network protocol**. Libraries that implement network protocols (such as HTTP) can depend on `tower-service` to use the `Service` trait as an integration point between the protocol and user code. For example, a client for some protocol might implement `Service`, allowing users to add arbitrary Tower middleware to those clients. Similarly, a server might be created from a user-provided `Service`. Additionally, when a network protocol requires functionality already provided by existing Tower middleware, a protocol implementation might use Tower middleware internally, as well as as an integration point.

### §Library Support

A number of third-party libraries support Tower and the `Service` trait. The following is an incomplete list of such libraries:

- `hyper`: A fast and correct low-level HTTP implementation.
- `tonic`: A gRPC-over-HTTP/2 implementation built on top of `hyper`. See here for examples of using `tonic` with Tower.
- `warp`: A lightweight, composable web framework. See here for details on using `warp` with Tower.
- `tower-lsp`: implementations of the Language Server Protocol based on Tower.

If you’re the maintainer of a crate that supports Tower, we’d love to add your crate to this list! Please open a PR adding a brief description of your library!

### §Getting Started

If you’re brand new to Tower and want to start with the basics, we recommend you check out some of our guides.

The various middleware implementations provided by this crate are feature flagged, so that users can only compile the parts of Tower they need. By default, all the optional middleware are disabled.

To get started using all of Tower’s optional middleware, add this to your `Cargo.toml`:

```toml
tower = { version = "0.4", features = ["full"] }
```

Alternatively, you can only enable some features. For example, to enable only the `retry` and `timeout` middleware, write:

```toml
tower = { version = "0.4", features = ["retry", "timeout"] }
```

See here for a complete list of all middleware provided by Tower.

### §Supported Rust Versions

Tower will keep a rolling MSRV (minimum supported Rust version) policy of **at least** 6 months. When increasing the MSRV, the new Rust version must have been released at least six months ago. The current MSRV is 1.64.0.

## Modules

**balance`balance`**

Middleware that allows balancing load among multiple services.

**buffer`buffer`**

Middleware that provides a buffered mpsc channel to a service.

**builder**

Builder types to compose layers and services

**discover`discover`**

Service discovery

**filter`filter`**

Conditionally dispatch requests to the inner service based on the result of a predicate.

**hedge`hedge`**

Pre-emptively retry requests which have been outstanding for longer than a given latency percentile.

**layer**

A collection of

Layer

based tower services

**limit`limit`**

Tower middleware for limiting requests.

**load`load`**

Service load measurement

**load_shed`load-shed`**

Middleware for shedding load when inner services aren’t ready.

**make`make`**

Trait aliases for Services that produce specific types of Responses.

**ready_cache`ready-cache`**

A cache of services

**reconnect`reconnect`**

Reconnect services when they fail.

**retry`retry`**

Middleware for retrying “failed” requests.

**spawn_ready`spawn-ready`**

When an underlying service is not ready, drive it to readiness on a background task.

**steer`steer`**

This module provides functionality to aid managing routing requests between

Service

s.

**timeout`timeout`**

Middleware that applies a timeout to requests.

**util`util`**

Various utility types and functions that are generally used with Tower.

## Structs

**ServiceBuilder**

Declaratively construct

Service

values.

## Traits

**Layer**

Decorates a

Service

, transforming either the request or the response.

**MakeService`make`**

Creates new

Service

values.

**Service**

An asynchronous function from a

Request

to a

Response

.

**ServiceExt`util`**

An extension trait for

Service

s that provides a variety of convenient adapters

## Functions

**service_fn`util`**

Returns a new

ServiceFn

with the given closure.

## Type Aliases

**BoxError**

Alias for a type-erased error type.
