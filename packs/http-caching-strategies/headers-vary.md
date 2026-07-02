---
title: "Vary header - HTTP"
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary
domain: http-caching-strategies
license: CC-BY-SA-4.0
tags: http caching strategies, cache-control header, etag validation, web cache freshness
fetched: 2026-07-02
---

# Vary header

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The HTTP **`Vary`** response header describes the parts of the request message (aside from the method and URL) that influenced the content of the response it occurs in. Including a `Vary` header ensures that responses are separately cached based on the headers listed in the `Vary` field. Most often, this is used to create a cache key when content negotiation is in use.

The same `Vary` header value should be used on all responses for a given URL, including `304` `Not Modified` responses and the "default" response.

| Header type | Response header |
|---|---|

## Syntax

```http
Vary: *
Vary: <header-name>, …, <header-nameN>
```

## Directives

**`*` (wildcard)**

Factors other than request headers influenced the generation of this response. Implies that the response is uncacheable.

**`<header-name>`**

A request header name that could have influenced the generation of this response.

## Specifications

| Specification |
|---|
| HTTP Semantics # field.vary |

## Browser compatibility
