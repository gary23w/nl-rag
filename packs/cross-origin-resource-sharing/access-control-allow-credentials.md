---
title: "Access-Control-Allow-Credentials header - HTTP"
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Credentials
domain: cross-origin-resource-sharing
license: CC-BY-SA-4.0
tags: cross-origin resource sharing, cors preflight request, access-control-allow-origin header, credentialed cross-origin request
fetched: 2026-07-02
---

# Access-Control-Allow-Credentials header

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The HTTP **`Access-Control-Allow-Credentials`** response header tells browsers whether the server allows credentials to be included in cross-origin HTTP requests.

Credentials include cookies, Transport Layer Security (TLS) client certificates, or authentication headers containing a username and password. By default, these credentials are not sent in cross-origin requests, and doing so can make a site vulnerable to Cross-Site Request Forgery (CSRF) attacks.

A client can ask for credentials to be included in cross-site requests in several ways:

- Using `fetch()`, by setting the `credentials` option to `"include"`.
- Using `XMLHttpRequest`, by setting the `XMLHttpRequest.withCredentials` property to `true`.
- Using `EventSource()`, by setting the `EventSource.withCredentials` property to `true`.

When credentials are included:

- For preflighted requests: The preflight request does not include credentials. If the server's response to the preflight request sets the `Access-Control-Allow-Credentials` header to `true`, then the real request will include credentials; otherwise, the browser reports a network error.
- For non-preflighted requests: The request will include credentials, and if the server's response does not set the `Access-Control-Allow-Credentials` header to `true`, the browser reports a network error.

| Header type | Response header |
|---|---|

## Syntax

```http
Access-Control-Allow-Credentials: true
```

## Directives

**`true`**

The server allows credentials to be included in cross-origin HTTP requests. This is the only valid value for this header and is case-sensitive. If you don't need credentials, omit this header entirely rather than setting its value to `false`.

## Examples

Allow credentials:

```http
Access-Control-Allow-Credentials: true
```

Using `fetch()` with credentials:

```js
fetch(url, {
  credentials: "include",
});
```

Using `XMLHttpRequest` with credentials:

```js
const xhr = new XMLHttpRequest();
xhr.open("GET", "http://example.com/", true);
xhr.withCredentials = true;
xhr.send(null);
```

## Specifications

| Specification |
|---|
| Fetch # http-access-control-allow-credentials |

## Browser compatibility
