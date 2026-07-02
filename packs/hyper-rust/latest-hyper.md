---
title: "hyper"
source: https://docs.rs/hyper/latest/hyper/
domain: hyper-rust
license: CC-BY-SA-4.0
tags: hyper http rust, rust web server library, http2 rust, hyper http library
fetched: 2026-07-02
---

# Crate hyper

Source

Expand description

## §hyper

hyper is a **fast** and **correct** HTTP implementation written in and for Rust.

### §Features

- HTTP/1 and HTTP/2
- Asynchronous design
- Leading in performance
- Tested and **correct**
- Extensive production use
- Client and Server APIs

If just starting out, **check out the Guides first.**

### §“Low-level”

hyper is a lower-level HTTP library, meant to be a building block for libraries and applications.

If looking for just a convenient HTTP client, consider the reqwest crate.

## §Cancel safety

Futures returned by hyper are cancel safe: dropping a future before it completes is the supported way to cancel the operation. See the documentation on individual futures — for example `SendRequest::send_request` in `client::conn::http1` and `client::conn::http2` — for the protocol- specific behavior on cancellation.

## §Optional Features

hyper uses a set of feature flags to reduce the amount of compiled code. It is possible to just enable certain features over others. By default, hyper does not enable any features but allows one to enable a subset for their use case. Below is a list of the available feature flags. You may also notice above each function, struct and trait there is listed one or more feature flags that are required for that item to be used.

If you are new to hyper it is possible to enable the `full` feature flag which will enable all public APIs. Beware though that this will pull in many extra dependencies that you may not need.

The following optional features are available:

- `http1`: Enables HTTP/1 support.
- `http2`: Enables HTTP/2 support.
- `client`: Enables the HTTP `client`.
- `server`: Enables the HTTP `server`.

### §Unstable Features

hyper includes a set of unstable optional features that can be enabled through the use of a feature flag and a configuration flag.

The following is a list of feature flags and their corresponding `RUSTFLAG`:

- `ffi`: Enables C API for hyper `hyper_unstable_ffi`.
- `tracing`: Enables debug logging with `hyper_unstable_tracing`.

For example:

```notrust
RUSTFLAGS="--cfg hyper_unstable_tracing" cargo build
```

## §Stability

It’s worth talking a bit about the stability of hyper. hyper’s API follows SemVer. Breaking changes will only be introduced in major versions, if ever. New additions to the API, such as new types, methods, or traits will only be added in minor versions.

Some parts of hyper are documented as NOT being part of the stable API. The following is a brief list, you can read more about each one in the relevant part of the documentation.

- Downcasting error types from `Error::source()` is not considered stable.
- Private dependencies use of global variables is not considered stable. So, if a dependency uses `log` or `tracing`, hyper doesn’t promise it will continue to do so.
- Behavior from default options is not stable. hyper reserves the right to add new options that are enabled by default which might alter the behavior, for the purposes of protection. It is also possible to *change* what the default options are set to, also in efforts to protect the most people possible.

## Re-exports

**`pub use http::header;`**

**`pub use http::HeaderMap;`**

**`pub use http::Method;`**

**`pub use http::Request;`**

**`pub use http::Response;`**

**`pub use http::StatusCode;`**

**`pub use http::Uri;`**

**`pub use http::Version;`**

## Modules

**body**

Streaming bodies for Requests and Responses.

**client`client`**

HTTP Client.

**ext**

Extensions for HTTP messages in Hyper.

**ffi`hyper_unstable_ffi` and `ffi`**

hyper C API

**rt**

Runtime components.

**server`server`**

HTTP Server.

**service**

Asynchronous Services.

**upgrade**

HTTP Upgrades.

## Structs

**Error**

Represents errors that can occur handling HTTP streams.

## Type Aliases

**Result**

Result type often returned from methods that can have hyper

Error

s.
