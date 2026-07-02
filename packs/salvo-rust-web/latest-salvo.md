---
title: "salvo"
source: https://docs.rs/salvo/latest/salvo/
domain: salvo-rust-web
license: CC-BY-SA-4.0
tags: salvo rust framework, rust web server framework, rust handler tree, salvo flexible middleware
fetched: 2026-07-02
---

# Crate salvo

Source

Expand description

Salvo is a powerful web framework that can make your work easier.

`salvo` uses a set of [feature flags] to reduce the amount of compiled and optional dependencies.

## §Feature flags

| Feature | Description | Default? |
|---|---|---|
| `cookie` | Support for Cookie | ✔️ |
| `server` | Built-in Server implementation | ✔️ |
| `http1` | Support for HTTP 1.1 protocol | ✔️ |
| `http2` | Support for HTTP 2 protocol | ✔️ |
| `http2-cleartext` | Support for HTTP 2 over cleartext TCP | ❌ |
| `quinn` | Use quinn to support HTTP 3 protocol | ❌ |
| `test` | Utilities for testing application | ✔️ |
| `acme` | Automatically obtain certificates through ACME | ❌ |
| `rustls` | TLS built on `rustls` | ❌ |
| `openssl` | TLS built on `openssl-tls` | ❌ |
| `native-tls` | TLS built on `native-tls` | ❌ |
| `unix` | Listener based on Unix socket | ❌ |
| `tower-compat` | Adapters for `tower::Layer` and `tower::Service` | ❌ |
| `anyhow` | Integrate with the `anyhow` crate | ❌ |
| `eyre` | Integrate with the `eyre` crate | ❌ |
| `affix-state` | Middleware for adding shared application state to the request context | ❌ |
| `craft` | Generate handlers or endpoints with shared data | ❌ |
| `basic-auth` | Middleware for basic authentication | ❌ |
| `caching-headers` | Middleware for setting caching headers | ❌ |
| `catch-panic` | Middleware for catching panics | ❌ |
| `concurrency-limiter` | Middleware for limiting concurrency | ❌ |
| `force-https` | Middleware for forcing HTTPS | ❌ |
| `logging` | Middleware for logging requests and responses | ❌ |
| `request-id` | Middleware for setting a request ID | ❌ |
| `size-limiter` | Middleware for limiting request size | ❌ |
| `sse` | Server-Sent Events (SSE) middleware | ❌ |
| `timeout` | Middleware for setting a timeout | ❌ |
| `trailing-slash` | Middleware for handling trailing slashes | ❌ |
| `websocket` | WebSocket implementation | ❌ |

## Re-exports

**`pub use salvo_cache as cache;``cache`**

**`pub use salvo_compression as compression;``compression`**

**`pub use salvo_cors as cors;``cors`**

**`pub use salvo_csrf as csrf;``csrf`**

**`pub use salvo_flash as flash;``flash`**

**`pub use salvo_jwt_auth as jwt_auth;``jwt-auth`**

**`pub use salvo_proxy as proxy;``proxy`**

**`pub use salvo_rate_limiter as rate_limiter;``rate-limiter`**

**`pub use salvo_session as session;``session`**

**`pub use salvo_serve_static as serve_static;``serve-static`**

**`pub use salvo_otel as otel;``otel`**

**`pub use salvo_acme as acme;``acme`**

**`pub use salvo_oapi as oapi;``oapi`**

**`pub use salvo_tus as tus;``tus`**

**`pub use salvo_core as core;`**

**`pub use salvo_craft as craft;``craft`**

## Modules

**affix_state`affix-state`**

Middleware for adding shared application state to the request context.

**basic_auth`basic-auth`**

Middleware for HTTP Basic Authentication.

**caching_headers`caching-headers`**

Middleware for handling ETag and Last-Modified headers.

**catch_panic`catch-panic`**

Middleware for catch panic in handlers.

**catcher**

Error catching and custom error page handling.

**concurrency_limiter`concurrency-limiter`**

Middleware for limiting concurrency.

**conn**

Connection and listener implementations for handling HTTP connections.

**extract**

Extract is a feature to let you deserialize request to custom type.

**force_https`force-https`**

Middleware force redirect to https.

**fs**

Filesystem utilities for serving files in HTTP responses.

**fuse**

Protection mechanisms against slow HTTP attacks and connection abuse.

**handler**

Handler module for handle

Request

.

**http**

HTTP types, request/response handling, and protocol utilities.

**hyper**

hyper

**logging`logging`**

A simple logging middleware.

**macros**

The macros lib of Salvo web framework.

**prelude**

A list of things that automatically imports into application use salvo.

**proto**

Http protocol supports.

**request_id`request-id`**

Request id middleware.

**routing**

Routing and filters.

**rt**

Runtime module.

**server`server`**

Server module

**size_limiter`size-limiter`**

Middleware for limiting request size.

**sse`sse`**

Middleware for Server-Sent Events (SSE)

**test`test`**

Utilities for testing application.

**timeout`timeout`**

Middleware for controlling requests timeout.

**trailing_slash`trailing-slash`**

Trailing slash middleware.

**websocket`websocket`**

WebSocket implementation.

**writing**

Writer trait and it’s implements.

## Structs

**Depot**

Store temp data for current request.

**FlowCtrl**

Control the flow of execute handlers.

**Request**

Represents an HTTP request.

**Response**

Represents an HTTP response.

**Router**

Route request to different handlers.

**Server**

HTTP Server.

**Service**

Service http request.

## Enums

**Error**

The main error type used throughout Salvo.

## Traits

**Extractible**

If a type implements this trait, it will give a metadata, this will help request to extracts data to this type.

**Handler**

Handler

is used for handle

Request

.

**Listener**

A trait for types that can bind to an address and create an acceptor.

**Scribe**

Scribe

is used to write data to

Response

.

**Writer**

Writer

is used to write data to

Response

.

## Type Aliases

**BoxedError**

A boxed error type for dynamic error handling.

**Result**

Result type which has

salvo::Error

as its error type.

## Attribute Macros

**async_trait**

**handler**

handler

is a macro to help create

Handler

from function or impl block easily.
