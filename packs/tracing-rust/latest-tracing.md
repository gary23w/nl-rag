---
title: "tracing"
source: https://docs.rs/tracing/latest/tracing/
domain: tracing-rust
license: CC-BY-SA-4.0
tags: tracing rust, rust structured logging, async instrumentation rust, tracing spans
fetched: 2026-07-02
---

# Crate tracing

Source

Expand description

A scoped, structured logging and diagnostics system.

## §Overview

`tracing` is a framework for instrumenting Rust programs to collect structured, event-based diagnostic information.

In asynchronous systems like Tokio, interpreting traditional log messages can often be quite challenging. Since individual tasks are multiplexed on the same thread, associated events and log lines are intermixed making it difficult to trace the logic flow. `tracing` expands upon logging-style diagnostics by allowing libraries and applications to record structured events with additional information about *temporality* and *causality* — unlike a log message, a span in `tracing` has a beginning and end time, may be entered and exited by the flow of execution, and may exist within a nested tree of similar spans. In addition, `tracing` spans are *structured*, with the ability to record typed data as well as textual messages.

The `tracing` crate provides the APIs necessary for instrumenting libraries and applications to emit trace data.

*Compiler support: requires `rustc` 1.65+*

## §Core Concepts

The core of `tracing`’s API is composed of *spans*, *events* and *subscribers*. We’ll cover these in turn.

### §Spans

To record the flow of execution through a program, `tracing` introduces the concept of spans. Unlike a log line that represents a *moment in time*, a span represents a *period of time* with a beginning and an end. When a program begins executing in a context or performing a unit of work, it *enters* that context’s span, and when it stops executing in that context, it *exits* the span. The span in which a thread is currently executing is referred to as that thread’s *current* span.

For example:

```
use tracing::{span, Level};
let span = span!(Level::TRACE, "my_span");
let _enter = span.enter();
```

The `span` module’s documentation provides further details on how to use spans.

```
Warning: In asynchronous code that uses async/await syntax,
Span::enter may produce incorrect traces if the returned drop
guard is held across an await point. See
the method documentation for details.
```

### §Events

An `Event` represents a *moment* in time. It signifies something that happened while a trace was being recorded. `Event`s are comparable to the log records emitted by unstructured logging code, but unlike a typical log line, an `Event` may occur within the context of a span.

For example:

```
use tracing::{event, span, Level};

event!(Level::INFO, "something happened");

let span = span!(Level::INFO, "my_span");
let _guard = span.enter();

event!(Level::DEBUG, "something happened inside my_span");
```

In general, events should be used to represent points in time *within* a span — a request returned with a given status code, *n* new items were taken from a queue, and so on.

The `Event` struct documentation provides further details on using events.

### §Subscribers

As `Span`s and `Event`s occur, they are recorded or aggregated by implementations of the `Subscriber` trait. `Subscriber`s are notified when an `Event` takes place and when a `Span` is entered or exited. These notifications are represented by the following `Subscriber` trait methods:

- `event`, called when an `Event` takes place,
- `enter`, called when execution enters a `Span`,
- `exit`, called when execution exits a `Span`

In addition, subscribers may implement the `enabled` function to *filter* the notifications they receive based on metadata describing each `Span` or `Event`. If a call to `Subscriber::enabled` returns `false` for a given set of metadata, that `Subscriber` will *not* be notified about the corresponding `Span` or `Event`. For performance reasons, if no currently active subscribers express interest in a given set of metadata by returning `true`, then the corresponding `Span` or `Event` will never be constructed.

## §Usage

First, add this to your `Cargo.toml`:

```toml
[dependencies]
tracing = "0.1"
```

### §Recording Spans and Events

Spans and events are recorded using macros.

#### §Spans

The `span!` macro expands to a `Span` struct which is used to record a span. The `Span::enter` method on that struct records that the span has been entered, and returns a RAII guard object, which will exit the span when dropped.

For example:

```
use tracing::{span, Level};
let span = span!(Level::TRACE, "my span");

let _enter = span.enter();
```

The `#[instrument]` attribute provides an easy way to add `tracing` spans to functions. A function annotated with `#[instrument]` will create and enter a span with that function’s name every time the function is called, with arguments to that function will be recorded as fields using `fmt::Debug`.

For example:

ⓘ

```
use tracing::{Level, event, instrument};

#[instrument]
pub fn my_function(my_arg: usize) {
    event!(Level::INFO, "inside my_function!");
    }
```

For functions which don’t have built-in tracing support and can’t have the `#[instrument]` attribute applied (such as from an external crate), the `Span` struct has a `in_scope()` method which can be used to easily wrap synchronous code in a span.

For example:

```
use tracing::info_span;

let json = info_span!("json.parse").in_scope(|| serde_json::from_slice(&buf))?;
```

You can find more examples showing how to use this crate here.

#### §Events

`Event`s are recorded using the `event!` macro:

```
use tracing::{event, Level};
event!(Level::INFO, "something has happened!");
```

### §Using the Macros

The `span!` and `event!` macros as well as the `#[instrument]` attribute use fairly similar syntax, with some exceptions.

#### §Configuring Attributes

Both macros require a `Level` specifying the verbosity of the span or event. Optionally, the, target and parent span may be overridden. If the target and parent span are not overridden, they will default to the module path where the macro was invoked and the current span (as determined by the subscriber), respectively.

For example:

```
span!(target: "app_spans", Level::TRACE, "my span");
event!(target: "app_events", Level::INFO, "something has happened!");
```

```
let span = span!(Level::TRACE, "my span");
event!(parent: &span, Level::INFO, "something has happened!");
```

The span macros also take a string literal after the level, to set the name of the span (as above). In the case of the event macros, the name of the event can be overridden (the default is `event file:line`) using the `name:` specifier.

```
span!(Level::TRACE, "my span");
event!(name: "some_info", Level::INFO, "something has happened!");
```

#### §Recording Fields

Structured fields on spans and events are specified using the syntax `field_name = field_value`. Fields are separated by commas.

```
event!(Level::INFO, answer = 42, question = "life, the universe, and everything");
```

As shorthand, local variables may be used as field values without an assignment, similar to struct initializers. For example:

```
let user = "ferris";

span!(Level::TRACE, "login", user);
span!(Level::TRACE, "login", user = user);
```

Field names can include dots, but should not be terminated by them:

```
let user = "ferris";
let email = "ferris@rust-lang.org";
span!(Level::TRACE, "login", user, user.email = email);
```

Since field names can include dots, fields on local structs can be used using the local variable shorthand:

```
let user = User {
    name: "ferris",
    email: "ferris@rust-lang.org",
};
span!(Level::TRACE, "login", user.name, user.email);
```

Fields with names that are not Rust identifiers, or with names that are Rust reserved words, may be created using quoted string literals. However, this may not be used with the local variable shorthand.

```
span!(Level::TRACE, "api", "guid:x-request-id" = "abcdef", "type" = "request");
```

Constant expressions can also be used as field names. Constants must be enclosed in curly braces (`{}`) to indicate that the *value* of the constant is to be used as the field name, rather than the constant’s name. For example:

```
const RESOURCE_NAME: &str = "foo";
span!(Level::TRACE, "get", { RESOURCE_NAME } = "some_id");
```

The `?` sigil is shorthand that specifies a field should be recorded using its `fmt::Debug` implementation:

```
#[derive(Debug)]
struct MyStruct {
    field: &'static str,
}

let my_struct = MyStruct {
    field: "Hello world!"
};

event!(Level::TRACE, greeting = ?my_struct);
event!(Level::TRACE, greeting = tracing::field::debug(&my_struct));
```

The `%` sigil operates similarly, but indicates that the value should be recorded using its `fmt::Display` implementation:

```
event!(Level::TRACE, greeting = %my_struct.field);
event!(Level::TRACE, greeting = tracing::field::display(&my_struct.field));
```

The `%` and `?` sigils may also be used with local variable shorthand:

```
event!(Level::TRACE, %my_struct.field);
```

Additionally, a span may declare fields with the special value `Empty`, which indicates that that the value for that field does not currently exist but may be recorded later. For example:

```
use tracing::{trace_span, field};

let span = trace_span!("my_span", greeting = "hello world", parting = field::Empty);

span.record("parting", &"goodbye world!");
```

Finally, events may also include human-readable messages, in the form of a format string and (optional) arguments, **after** the event’s key-value fields. If a format string and arguments are provided, they will implicitly create a new field named `message` whose value is the provided set of format arguments.

For example:

```
let question = "the ultimate question of life, the universe, and everything";
let answer = 42;
event!(
    Level::DEBUG,
    question.answer = answer,
    question.tricky = true,
    "the answer to {} is {}.", question, answer
);
```

Specifying a formatted message in this manner does not allocate by default.

#### §Shorthand Macros

`tracing` also offers a number of macros with preset verbosity levels. The `trace!`, `debug!`, `info!`, `warn!`, and `error!` behave similarly to the `event!` macro, but with the `Level` argument already specified, while the corresponding `trace_span!`, `debug_span!`, `info_span!`, `warn_span!`, and `error_span!` macros are the same, but for the `span!` macro.

These are intended both as a shorthand, and for compatibility with the `log` crate (see the next section).

#### §For `log` Users

Users of the `log` crate should note that `tracing` exposes a set of macros for creating `Event`s (`trace!`, `debug!`, `info!`, `warn!`, and `error!`) which may be invoked with the same syntax as the similarly-named macros from the `log` crate. Often, the process of converting a project to use `tracing` can begin with a simple drop-in replacement.

Let’s consider the `log` crate’s yak-shaving example:

ⓘ

```
use std::{error::Error, io};
use tracing::{debug, error, info, span, warn, Level};

#[tracing::instrument]
pub fn shave(yak: usize) -> Result<(), Box<dyn Error + 'static>> {
    debug!(excitement = "yay!", "hello! I'm gonna shave a yak.");
    if yak == 3 {
        warn!("could not locate yak!");
        return Err(io::Error::new(io::ErrorKind::Other, "shaving yak failed!").into());
    } else {
        debug!("yak shaved successfully");
    }
    Ok(())
}

pub fn shave_all(yaks: usize) -> usize {
    let _span = span!(Level::TRACE, "shaving_yaks", yaks).entered();

    info!("shaving yaks");

    let mut yaks_shaved = 0;
    for yak in 1..=yaks {
        let res = shave(yak);
        debug!(yak, shaved = res.is_ok());

        if let Err(ref error) = res {
            error!(yak, error = error.as_ref(), "failed to shave yak!");
        } else {
            yaks_shaved += 1;
        }
        debug!(yaks_shaved);
    }

    yaks_shaved
}
```

### §In libraries

Libraries should link only to the `tracing` crate, and use the provided macros to record whatever information will be useful to downstream consumers.

### §In executables

In order to record trace events, executables have to use a `Subscriber` implementation compatible with `tracing`. A `Subscriber` implements a way of collecting trace data, such as by logging it to standard output.

This library does not contain any `Subscriber` implementations; these are provided by other crates.

The simplest way to use a subscriber is to call the `set_global_default` function:

```
extern crate tracing;

let my_subscriber = FooSubscriber::new();
tracing::subscriber::set_global_default(my_subscriber)
    .expect("setting tracing default failed");
```

```
     Warning: In general, libraries should not call
     set_global_default()! Doing so will cause conflicts when
     executables that depend on the library try to set the default later.
 
```

This subscriber will be used as the default in all threads for the remainder of the duration of the program, similar to setting the logger in the `log` crate.

In addition, the default subscriber can be set through using the `with_default` function. This follows the `tokio` pattern of using closures to represent executing code in a context that is exited at the end of the closure. For example:

```
let my_subscriber = FooSubscriber::new();
tracing::subscriber::with_default(my_subscriber, || {
    })
```

This approach allows trace data to be collected by multiple subscribers within different contexts in the program. Note that the override only applies to the currently executing thread; other threads will not see the change from with_default.

Any trace events generated outside the context of a subscriber will not be collected.

Once a subscriber has been set, instrumentation points may be added to the executable using the `tracing` crate’s macros.

### §`log` Compatibility

The `log` crate provides a simple, lightweight logging facade for Rust. While `tracing` builds upon `log`’s foundation with richer structured diagnostic data, `log`’s simplicity and ubiquity make it the “lowest common denominator” for text-based logging in Rust — a vast majority of Rust libraries and applications either emit or consume `log` records. Therefore, `tracing` provides multiple forms of interoperability with `log`: `tracing` instrumentation can emit `log` records, and a compatibility layer enables `tracing` `Subscriber`s to consume `log` records as `tracing` `Event`s.

#### §Emitting `log` Records

This crate provides two feature flags, “log” and “log-always”, which will cause spans and events to emit `log` records. When the “log” feature is enabled, if no `tracing` `Subscriber` is active, invoking an event macro or creating a span with fields will emit a `log` record. This is intended primarily for use in libraries which wish to emit diagnostics that can be consumed by applications using `tracing` *or* `log`, without paying the additional overhead of emitting both forms of diagnostics when `tracing` is in use.

Enabling the “log-always” feature will cause `log` records to be emitted even if a `tracing` `Subscriber` *is* set. This is intended to be used in applications where a `log` `Logger` is being used to record a textual log, and `tracing` is used only to record other forms of diagnostics (such as metrics, profiling, or distributed tracing data). Unlike the “log” feature, libraries generally should **not** enable the “log-always” feature, as doing so will prevent applications from being able to opt out of the `log` records.

See here for more details on this crate’s feature flags.

The generated `log` records’ messages will be a string representation of the span or event’s fields, and all additional information recorded by `log` (target, verbosity level, module path, file, and line number) will also be populated. Additionally, `log` records are also generated when spans are entered, exited, and closed. Since these additional span lifecycle logs have the potential to be very verbose, and don’t include additional fields, they will always be emitted at the `Trace` level, rather than inheriting the level of the span that generated them. Furthermore, they are categorized under a separate `log` target, “tracing::span” (and its sub-target, “tracing::span::active”, for the logs on entering and exiting a span), which may be enabled or disabled separately from other `log` records emitted by `tracing`.

#### §Consuming `log` Records

The `tracing-log` crate provides a compatibility layer which allows a `tracing` `Subscriber` to consume `log` records as though they were `tracing` events. This allows applications using `tracing` to record the logs emitted by dependencies using `log` as events within the context of the application’s trace tree. See that crate’s documentation for details.

In addition to `tracing` and `tracing-core`, the `tokio-rs/tracing` repository contains several additional crates designed to be used with the `tracing` ecosystem. This includes a collection of `Subscriber` implementations, as well as utility and adapter crates to assist in writing `Subscriber`s and instrumenting applications.

In particular, the following crates are likely to be of interest:

- `tracing-futures` provides a compatibility layer with the `futures` crate, allowing spans to be attached to `Future`s, `Stream`s, and `Executor`s.
- `tracing-subscriber` provides `Subscriber` implementations and utilities for working with `Subscriber`s. This includes a `FmtSubscriber` `FmtSubscriber` for logging formatted trace data to stdout, with similar filtering and formatting to the `env_logger` crate.
- `tracing-log` provides a compatibility layer with the `log` crate, allowing log messages to be recorded as `tracing` `Event`s within the trace tree. This is useful when a project using `tracing` have dependencies which use `log`. Note that if you’re using `tracing-subscriber`’s `FmtSubscriber`, you don’t need to depend on `tracing-log` directly.
- `tracing-appender` provides utilities for outputting tracing data, including a file appender and non blocking writer.

Additionally, there are also several third-party crates which are not maintained by the `tokio` project. These include:

- `tracing-timing` implements inter-event timing metrics on top of `tracing`. It provides a subscriber that records the time elapsed between pairs of `tracing` events and generates histograms.
- `tracing-opentelemetry` provides a subscriber for emitting traces to OpenTelemetry-compatible distributed tracing systems.
- `tracing-honeycomb` Provides a layer that reports traces spanning multiple machines to honeycomb.io. Backed by `tracing-distributed`.
- `tracing-distributed` Provides a generic implementation of a layer that reports traces spanning multiple machines to some backend.
- `tracing-actix-web` provides `tracing` integration for the `actix-web` web framework.
- `tracing-actix` provides `tracing` integration for the `actix` actor framework.
- `axum-insights` provides `tracing` integration and Application insights export for the `axum` web framework.
- `tracing-gelf` implements a subscriber for exporting traces in Greylog GELF format.
- `tracing-coz` provides integration with the coz causal profiler (Linux-only).
- `tracing-bunyan-formatter` provides a layer implementation that reports events and spans in bunyan format, enriched with timing information.
- `tracing-wasm` provides a `Subscriber`/`Layer` implementation that reports events and spans via browser `console.log` and User Timing API (`window.performance`).
- `tracing-web` provides a layer implementation of level-aware logging of events to web browsers’ `console.*` and span events to the User Timing API (`window.performance`).
- `tide-tracing` provides a tide middleware to trace all incoming requests and responses.
- `test-log` takes care of initializing `tracing` for tests, based on environment variables with an `env_logger` compatible syntax.
- `tracing-unwrap` provides convenience methods to report failed unwraps on `Result` or `Option` types to a `Subscriber`.
- `diesel-tracing` provides integration with `diesel` database connections.
- `tracing-tracy` provides a way to collect Tracy profiles in instrumented applications.
- `tracing-elastic-apm` provides a layer for reporting traces to Elastic APM.
- `tracing-etw` provides a layer for emitting Windows ETW events.
- `tracing-fluent-assertions` provides a fluent assertions-style testing framework for validating the behavior of `tracing` spans.
- `sentry-tracing` provides a layer for reporting events and traces to Sentry.
- `tracing-forest` provides a subscriber that preserves contextual coherence by grouping together logs from the same spans during writing.
- `tracing-loki` provides a layer for shipping logs to Grafana Loki.
- `tracing-logfmt` provides a layer that formats events and spans into the logfmt format.
- `reqwest-tracing` provides a middleware to trace `reqwest` HTTP requests.
- `tracing-cloudwatch` provides a layer that sends events to AWS CloudWatch Logs.
- `clippy-tracing` provides a tool to add, remove and check for `tracing::instrument`.
- `json-subscriber` provides a subscriber for emitting JSON logs. The output can be customized much more than with `tracing-subscriber`’s JSON output.

If you’re the maintainer of a `tracing` ecosystem crate not listed above, please let us know! We’d love to add your project to the list!

```
     Note: Some of these ecosystem crates are currently
     unreleased and/or in earlier stages of development. They may be less stable
     than tracing and tracing-core.
 
```

### §Crate Feature Flags

The following crate feature flags are available:

- A set of features controlling the static verbosity level.
- `log`: causes trace instrumentation points to emit `log` records as well as trace events, if a default `tracing` subscriber has not been set. This is intended for use in libraries whose users may be using either `tracing` or `log`.
- `log-always`: Emit `log` records from all `tracing` spans and events, even if a `tracing` subscriber has been set. This should be set only by applications which intend to collect traces and logs separately; if an adapter is used to convert `log` records into `tracing` events, this will cause duplicate events to occur.
- `attributes`: Includes support for the `#[instrument]` attribute. This is on by default, but does bring in the `syn` crate as a dependency, which may add to the compile time of crates that do not already use it.
- `std`: Depend on the Rust standard library (enabled by default). `no_std` users may disable this feature with `default-features = false`: `[dependencies] tracing = { version = "0.1.38", default-features = false }`

```
     Note: tracing's no_std support
     requires liballoc.
 
```

#### §Unstable Features

These feature flags enable **unstable** features. The public API may break in 0.1.x releases. To enable these features, the `--cfg tracing_unstable` must be passed to `rustc` when compiling.

The following unstable feature flags are currently available:

- `valuable`: Enables support for recording field values using the `valuable` crate.

##### §Enabling Unstable Features

The easiest way to set the `tracing_unstable` cfg is to use the `RUSTFLAGS` env variable when running `cargo` commands:

```shell
RUSTFLAGS="--cfg tracing_unstable" cargo build
```

Alternatively, the following can be added to the `.cargo/config` file in a project to automatically enable the cfg flag for that project:

```toml
[build]
rustflags = ["--cfg", "tracing_unstable"]
```

### §Supported Rust Versions

Tracing is built against the latest stable release. The minimum supported version is 1.65. The current Tracing version is not guaranteed to build on Rust versions earlier than the minimum supported version.

Tracing follows the same compiler support policies as the rest of the Tokio project. The current stable Rust compiler and the three most recent minor versions before it will always be supported. For example, if the current stable compiler version is 1.69, the minimum supported version will not be increased past 1.66, three minor versions prior. Increasing the minimum supported compiler version is not considered a semver breaking change as long as doing so complies with this policy.

## Modules

**dispatcher**

Dispatches trace events to

Subscriber

s.

**event**

Events represent single points in time during the execution of a program.

**field**

Span

and

Event

key-value data.

**instrument**

Attach a span to a

std::future::Future

.

**level_filters**

Trace verbosity level filtering.

**span**

Spans represent periods of time in which a program was executing in a particular context.

**subscriber**

Collects and records trace data.

## Macros

**debug**

Constructs an event at the debug level.

**debug_span**

Constructs a span at the debug level.

**enabled**

Checks whether a span or event is

enabled

based on the provided

metadata

.

**error**

Constructs an event at the error level.

**error_span**

Constructs a span at the error level.

**event**

Constructs a new

Event

.

**event_enabled**

Tests whether an event with the specified level and target would be enabled.

**info**

Constructs an event at the info level.

**info_span**

Constructs a span at the info level.

**record_all**

Records multiple values on a span in a single call. As with recording individual values, all fields must be declared when the span is created.

**span**

Constructs a new span.

**span_enabled**

Tests whether a span with the specified level and target would be enabled.

**trace**

Constructs an event at the trace level.

**trace_span**

Constructs a span at the trace level.

**warn**

Constructs an event at the warn level.

**warn_span**

Constructs a span at the warn level.

## Structs

**Dispatch**

Dispatch

trace data to a

Subscriber

.

**Event**

Event

s represent single points in time where something occurred during the execution of a program.

**Level**

Describes the level of verbosity of a span or event.

**Metadata**

Metadata describing a

span

or

event

.

**Span**

A handle representing a span, with the capability to enter the span if it exists.

## Traits

**Instrument**

Attaches spans to a

std::future::Future

.

**Subscriber**

Trait representing the functions required to collect trace data.

**Value**

A field value of an erased type.

## Attribute Macros

**instrument`attributes`**

Instruments a function to create and enter a

tracing

span

every time the function is called.
