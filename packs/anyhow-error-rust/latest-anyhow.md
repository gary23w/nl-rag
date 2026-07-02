---
title: "anyhow"
source: https://docs.rs/anyhow/latest/anyhow/
domain: anyhow-error-rust
license: CC-BY-SA-4.0
tags: anyhow error handling, rust error library, anyhow context, rust error propagation
fetched: 2026-07-02
---

# Crate anyhow

Source

Expand description

(github) (crates-io) (docs-rs)

This library provides `anyhow::Error`, a trait object based error type for easy idiomatic error handling in Rust applications.

## §Details

- Use `Result<T, anyhow::Error>`, or equivalently `anyhow::Result<T>`, as the return type of any fallible function. Within the function, use `?` to easily propagate any error that implements the `std::error::Error` trait. `use anyhow::Result; fn get_cluster_info() -> Result<ClusterMap> { let config = std::fs::read_to_string("cluster.json")?; let map: ClusterMap = serde_json::from_str(&config)?; Ok(map) }`
- Attach context to help the person troubleshooting the error understand where things went wrong. A low-level error like “No such file or directory” can be annoying to debug without more context about what higher level step the application was in the middle of. `use anyhow::{Context, Result}; fn main() -> Result<()> { ... it.detach().context("Failed to detach the important thing")?; let content = std::fs::read(path) .with_context(|| format!("Failed to read instrs from {}", path))?; ... }``Error: Failed to read instrs from ./path/to/instrs.json Caused by: No such file or directory (os error 2)`
- Downcasting is supported and can be by value, by shared reference, or by mutable reference as needed. `match root_cause.downcast_ref::<DataStoreError>() { Some(DataStoreError::Censored(_)) => Ok(Poll::Ready(REDACTED_CONTENT)), None => Err(error), }`
- If using Rust ≥ 1.65, a backtrace is captured and printed with the error if the underlying error type does not already provide its own. In order to see backtraces, they must be enabled through the environment variables described in `std::backtrace`:
  - If you want panics and errors to both have backtraces, set `RUST_BACKTRACE=1`;
  - If you want only errors to have backtraces, set `RUST_LIB_BACKTRACE=1`;
  - If you want only panics to have backtraces, set `RUST_BACKTRACE=1` and `RUST_LIB_BACKTRACE=0`.
- Anyhow works with any error type that has an impl of `std::error::Error`, including ones defined in your crate. We do not bundle a `derive(Error)` macro but you can write the impls yourself or use a standalone macro like thiserror. `use thiserror::Error; #[derive(Error, Debug)] pub enum FormatError { #[error("Invalid header (expected {expected:?}, got {found:?})")] InvalidHeader { expected: String, found: String, }, #[error("Missing attribute: {0}")] MissingAttribute(String), }`
- One-off error messages can be constructed using the `anyhow!` macro, which supports string interpolation and produces an `anyhow::Error`. `return Err(anyhow!("Missing attribute: {}", missing));` A `bail!` macro is provided as a shorthand for the same early return. `bail!("Missing attribute: {}", missing);`

## §No-std support

In no_std mode, almost all of the same API is available and works the same way. To depend on Anyhow in no_std mode, disable our default enabled “std” feature in Cargo.toml. A global allocator is required.

```toml
[dependencies]
anyhow = { version = "1.0", default-features = false }
```

With versions of Rust older than 1.81, no_std mode may require an additional `.map_err(Error::msg)` when working with a non-Anyhow error type inside a function that returns Anyhow’s error type, as the trait that `?`-based error conversions are defined by is only available in std in those old versions.

## Re-exports

**`pub use anyhow as format_err;`**

## Macros

**anyhow**

Construct an ad-hoc error from a string or existing non-

anyhow

error value.

**bail**

Return early with an error.

**ensure**

Return early with an error if a condition is not satisfied.

## Structs

**Chain**

Iterator of a chain of source errors.

**Error**

The

Error

type, a wrapper around a dynamic error type.

## Traits

**Context**

Provides the

context

method for

Result

.

## Functions

**Ok**

Equivalent to

Ok::<_, anyhow::Error>(value)

.

## Type Aliases

**Result**

Result<T, Error>
