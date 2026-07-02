---
title: "thiserror"
source: https://docs.rs/thiserror/latest/thiserror/
domain: thiserror-rust
license: CC-BY-SA-4.0
tags: thiserror derive, rust custom errors, error enum rust, thiserror macro
fetched: 2026-07-02
---

# Crate thiserror

Source

Expand description

(github) (crates-io) (docs-rs)

This library provides a convenient derive macro for the standard library’s `std::error::Error` trait.

## §Example

```
use thiserror::Error;

#[derive(Error, Debug)]
pub enum DataStoreError {
    #[error("data store disconnected")]
    Disconnect(#[from] io::Error),
    #[error("the data for key `{0}` is not available")]
    Redaction(String),
    #[error("invalid header (expected {expected:?}, found {found:?})")]
    InvalidHeader {
        expected: String,
        found: String,
    },
    #[error("unknown data store error")]
    Unknown,
}
```

## §Details

- Thiserror deliberately does not appear in your public API. You get the same thing as if you had written an implementation of `std::error::Error` by hand, and switching from handwritten impls to thiserror or vice versa is not a breaking change.
- Errors may be enums, structs with named fields, tuple structs, or unit structs.
- A `Display` impl is generated for your error if you provide `#[error("...")]` messages on the struct or each variant of your enum, as shown above in the example. The messages support a shorthand for interpolating fields from the error. These shorthands can be used together with any additional format args, which may be arbitrary expressions. For example: `#[derive(Error, Debug)] pub enum Error { #[error("invalid rdo_lookahead_frames {0} (expected < {max})", max = i32::MAX)] InvalidLookahead(u32), }` If one of the additional expression arguments needs to refer to a field of the struct or enum, then refer to named fields as `.var` and tuple fields as `.0`. `#[derive(Error, Debug)] pub enum Error { #[error("first letter must be lowercase but was {:?}", first_char(.0))] WrongCase(String), #[error("invalid index {idx}, expected at least {} and at most {}", .limits.lo, .limits.hi)] OutOfBounds { idx: usize, limits: Limits }, }`
  - `#[error("{var}")]` ⟶ `write!("{}", self.var)`
  - `#[error("{0}")]` ⟶ `write!("{}", self.0)`
  - `#[error("{var:?}")]` ⟶ `write!("{:?}", self.var)`
  - `#[error("{0:?}")]` ⟶ `write!("{:?}", self.0)`
- A `From` impl is generated for each variant that contains a `#[from]` attribute. The variant using `#[from]` must not contain any other fields beyond the source error (and possibly a backtrace — see below). Usually `#[from]` fields are unnamed, but `#[from]` is allowed on a named field too. `#[derive(Error, Debug)] pub enum MyError { Io(#[from] io::Error), Glob(#[from] globset::Error), }`
- The Error trait’s `source()` method is implemented to return whichever field has a `#[source]` attribute or is named `source`, if any. This is for identifying the underlying lower level error that caused your error. The `#[from]` attribute always implies that the same field is `#[source]`, so you don’t ever need to specify both attributes. Any error type that implements `std::error::Error` or dereferences to `dyn std::error::Error` will work as a source. `#[derive(Error, Debug)] pub struct MyError { msg: String, #[source] source: anyhow::Error, }`
- The Error trait’s `provide()` method is implemented to provide whichever field has a type named `Backtrace`, if any, as a `std::backtrace::Backtrace`. Using `Backtrace` in errors requires a nightly compiler with Rust version 1.73 or newer. `use std::backtrace::Backtrace; #[derive(Error, Debug)] pub struct MyError { msg: String, backtrace: Backtrace, }`
- If a field is both a source (named `source`, or has `#[source]` or `#[from]` attribute) *and* is marked `#[backtrace]`, then the Error trait’s `provide()` method is forwarded to the source’s `provide` so that both layers of the error share the same backtrace. The `#[backtrace]` attribute requires a nightly compiler with Rust version 1.73 or newer. `#[derive(Error, Debug)] pub enum MyError { Io { #[backtrace] source: io::Error, }, }`
- For variants that use `#[from]` and also contain a `Backtrace` field, a backtrace is captured from within the `From` impl. `#[derive(Error, Debug)] pub enum MyError { Io { #[from] source: io::Error, backtrace: Backtrace, }, }`
- Errors may use `error(transparent)` to forward the source and `Display` methods straight through to an underlying error without adding an additional message. This would be appropriate for enums that need an “anything else” variant. `#[derive(Error, Debug)] pub enum MyError { ... #[error(transparent)] Other(#[from] anyhow::Error), }` Another use case is hiding implementation details of an error representation behind an opaque error type, so that the representation is able to evolve without breaking the crate’s public API. `#[derive(Error, Debug)] #[error(transparent)] pub struct PublicError(#[from] ErrorRepr); impl PublicError { } #[derive(Error, Debug)] enum ErrorRepr { ... }`
- See also the `anyhow` library for a convenient single error type to use in application code.

## Derive Macros

**Error**
