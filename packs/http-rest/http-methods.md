---
title: "HTTP request methods - HTTP"
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
domain: http-rest
license: CC-BY-SA-2.5 / IETF-Trust (RFC)
tags: http, rest api, endpoint, cookie, cors, websocket
fetched: 2026-07-02
---

# HTTP request methods

HTTP defines a set of **request methods** to indicate the purpose of the request and what is expected if the request is successful. Although they can also be nouns, these request methods are sometimes referred to as *HTTP verbs*. Each request method has its own semantics, but some characteristics are shared across multiple methods, specifically request methods can be safe, idempotent, or cacheable.

**`GET`**

The `GET` method requests a representation of the specified resource. Requests using `GET` should only retrieve data and should not contain a request content.

**`HEAD`**

The `HEAD` method asks for a response identical to a `GET` request, but without a response body.

**`POST`**

The `POST` method submits an entity to the specified resource, often causing a change in state or side effects on the server.

**`PUT`**

The `PUT` method replaces all current representations of the target resource with the request content.

**`DELETE`**

The `DELETE` method deletes the specified resource.

**`CONNECT`**

The `CONNECT` method establishes a tunnel to the server identified by the target resource.

**`OPTIONS`**

The `OPTIONS` method describes the communication options for the target resource.

**`TRACE`**

The `TRACE` method performs a message loop-back test along the path to the target resource.

**`PATCH`**

The `PATCH` method applies partial modifications to a resource.

## Safe, idempotent, and cacheable request methods

The following table lists HTTP request methods and their categorization in terms of safety, cacheability, and idempotency.

| Method | Safe | Idempotent | Cacheable |
|---|---|---|---|
| `GET` | Yes | Yes | Yes |
| `HEAD` | Yes | Yes | Yes |
| `OPTIONS` | Yes | Yes | No |
| `TRACE` | Yes | Yes | No |
| `PUT` | No | Yes | No |
| `DELETE` | No | Yes | No |
| `POST` | No | No | Conditional* |
| `PATCH` | No | No | Conditional* |
| `CONNECT` | No | No | No |

* `POST` and `PATCH` are cacheable when responses explicitly include freshness information and a matching `Content-Location` header.

## Specifications

| Specification |
|---|
| HTTP Semantics # GET |
| HTTP Semantics # DELETE |
| HTTP Semantics # HEAD |
| HTTP Semantics # CONNECT |
| HTTP Semantics # PUT |
| HTTP Semantics # POST |
| HTTP Semantics # OPTIONS |

## Browser compatibility
