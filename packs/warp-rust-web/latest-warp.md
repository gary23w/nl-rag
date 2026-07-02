---
title: "warp"
source: https://docs.rs/warp/latest/warp/
domain: warp-rust-web
license: CC-BY-SA-4.0
tags: warp rust framework, rust filter composition, tokio rust web, warp reply rejection
fetched: 2026-07-02
---

# Crate warp

Source

Expand description

## §warp

warp is a super-easy, composable, web server framework for warp speeds.

Thanks to its `Filter` system, warp provides these out of the box:

- Path routing and parameter extraction
- Header requirements and extraction
- Query string deserialization
- JSON and Form bodies
- Multipart form data
- Static Files and Directories
- Websockets
- Access logging
- Etc

Since it builds on top of hyper, you automatically get:

- HTTP/1
- HTTP/2
- Asynchronous
- One of the fastest HTTP implementations
- Tested and **correct**

### §Filters

The main concept in warp is the `Filter`, which allows composition to describe various endpoints in your web service. Besides this powerful trait, warp comes with several built in filters, which can be combined for your specific needs.

As a small example, consider an endpoint that has path and header requirements:

```
use warp::Filter;

let hi = warp::path("hello")
    .and(warp::path::param())
    .and(warp::header("user-agent"))
    .map(|param: String, agent: String| {
        format!("Hello {}, whose agent is {}", param, agent)
    });
```

This example composes several `Filter`s together using `and`:

- A path prefix of “hello”
- A path parameter of a `String`
- The `user-agent` header parsed as a `String`

These specific filters will `reject` requests that don’t match their requirements.

This ends up matching requests like:

```notrust
GET /hello/sean HTTP/1.1
Host: hyper.rs
User-Agent: reqwest/v0.8.6
```

And it returns a response similar to this:

```notrust
HTTP/1.1 200 OK
Content-Length: 41
Date: ...

Hello sean, whose agent is reqwest/v0.8.6
```

Take a look at the full list of `filters` to see what you can build.

### §Testing

Testing your web services easily is extremely important, and warp provides a `test` module to help send mocked requests through your service.

## Modules

**filters**

Built-in Filters

**redirect**

Redirect requests to a new location.

**reject**

Rejections

**reply**

Reply to requests.

**test`test`**

Test utilities to test your filters.

## Macros

**path**

Convenient way to chain multiple path filters together.

## Structs

**Error**

Errors that can happen inside warp.

**Server`server` and `docsrs`**

A warp Server ready to filter requests.

## Traits

**Filter**

Composable request filters.

## Functions

**serve`server`**

Create a

Server

with the provided

Filter

.

**service**

Convert a

Filter

into a

Service

.

**wrap_fn**

Combines received filter with pre and after filters
