---
title: "Age header - HTTP"
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Age
domain: http-caching-strategies
license: CC-BY-SA-4.0
tags: http caching strategies, cache-control header, etag validation, web cache freshness
fetched: 2026-07-02
---

# Age header

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The HTTP **`Age`** response header indicates the time in seconds for which an object was in a proxy cache.

The header value is usually close to zero. If the value is `0`, the object was probably fetched from the origin server; otherwise, the value is usually calculated as a difference between the proxy's current date and the `Date` general header included in the HTTP response.

| Header type | Response header |
|---|---|

## Syntax

```http
Age: <delta-seconds>
```

## Directives

**`<delta-seconds>`**

A non-negative integer that represents the time in seconds for which the object was in a proxy cache.

## Examples

```http
Age: 24
```

## Specifications

| Specification |
|---|
| HTTP Caching # field.age |

## Browser compatibility
