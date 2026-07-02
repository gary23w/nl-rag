---
title: "Request - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Request
domain: fetch-api
license: CC-BY-SA-2.5
tags: fetch api, fetch request, http request browser, abortcontroller, fetch response
fetched: 2026-07-02
---

# Request

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`Request`** interface of the Fetch API represents a resource request.

You can create a new `Request` object using the `Request()` constructor, but you are more likely to encounter a `Request` object being returned as the result of another API operation, such as a service worker `FetchEvent.request`.

## Constructor

**`Request()`**

Creates a new `Request` object.

## Instance properties

**`Request.body` Read only**

A `ReadableStream` of the body contents.

**`Request.bodyUsed` Read only**

Stores `true` or `false` to indicate whether or not the body has been used in a request yet.

**`Request.cache` Read only**

Contains the cache mode of the request (e.g., `default`, `reload`, `no-cache`).

**`Request.credentials` Read only**

Contains a value controlling whether credentials should be included with the request (e.g., `omit`, `same-origin`, `include`). The default is `same-origin`.

**`Request.destination` Read only**

A string describing the type of content being requested.

**`Request.duplex` Read only**

The duplex mode of the request, which determines whether the browser must send the entire request before processing the response.

**`Request.headers` Read only**

Contains the associated `Headers` object of the request.

**`Request.integrity` Read only**

Contains the subresource integrity value of the request (e.g., `sha256-BpfBw7ivV8q2jLiT13fxDYAe2tJllusRSZ273h2nFSE=`).

**`Request.isHistoryNavigation` Read only**

A boolean indicating whether the request is a history navigation.

**`Request.isReloadNavigation` Read only**

A boolean indicating whether the request is a user-triggered reload.

**`Request.keepalive` Read only**

Contains the request's `keepalive` setting (`true` or `false`), which indicates whether the browser will keep the associated request alive if the page that initiated it is unloaded before the request is complete.

**`Request.method` Read only**

Contains the request's method (`GET`, `POST`, etc.)

**`Request.mode` Read only**

Contains the mode of the request (e.g., `cors`, `no-cors`, `same-origin`, `navigate`.)

**`Request.redirect` Read only**

Contains the mode for how redirects are handled. It may be one of `follow`, `error`, or `manual`.

**`Request.referrer` Read only**

Contains the referrer of the request (e.g., `client`).

**`Request.referrerPolicy` Read only**

Contains the referrer policy of the request (e.g., `no-referrer`).

**`Request.signal` Read only**

Returns the `AbortSignal` associated with the request.

**`Request.targetAddressSpace` Read only**

Returns the request's target address space, which indicates whether it is a loopback, local, or public request.

**`Request.url` Read only**

Contains the URL of the request.

## Instance methods

**`Request.arrayBuffer()`**

Returns a promise that resolves with an `ArrayBuffer` representation of the request body.

**`Request.blob()`**

Returns a promise that resolves with a `Blob` representation of the request body.

**`Request.bytes()`**

Returns a promise that resolves with a `Uint8Array` representation of the request body.

**`Request.clone()`**

Creates a copy of the current `Request` object.

**`Request.formData()`**

Returns a promise that resolves with a `FormData` representation of the request body.

**`Request.json()`**

Returns a promise that resolves with the result of parsing the request body as `JSON`.

**`Request.text()`**

Returns a promise that resolves with a text representation of the request body.

**Note:** The request body functions can be run only once; subsequent calls will reject with TypeError showing that the body stream has already used.

## Examples

In the following snippet, we create a new request using the `Request()` constructor (for an image file in the same directory as the script), then return some property values of the request:

```js
const request = new Request("https://www.mozilla.org/favicon.ico");

const url = request.url;
const method = request.method;
const credentials = request.credentials;
```

You could then fetch this request by passing the `Request` object in as a parameter to a `fetch()` call, for example:

```js
fetch(request)
  .then((response) => response.blob())
  .then((blob) => {
    image.src = URL.createObjectURL(blob);
  });
```

In the following snippet, we create a new request using the `Request()` constructor with some initial data and body content for an API request which needs a body payload:

```js
const request = new Request("https://example.com", {
  method: "POST",
  body: '{"foo": "bar"}',
});

const url = request.url;
const method = request.method;
const credentials = request.credentials;
const bodyUsed = request.bodyUsed;
```

**Note:** The body can only be a `Blob`, an `ArrayBuffer`, a `TypedArray`, a `DataView`, a `FormData`, a `URLSearchParams`, a `ReadableStream`, or a `String` object, as well as a string literal, so for adding a JSON object to the payload you need to stringify that object.

You could then fetch this API request by passing the `Request` object in as a parameter to a `fetch()` call, for example and get the response:

```js
fetch(request)
  .then((response) => {
    if (response.status !== 200) {
      throw new Error("Something went wrong on API server!");
    }
    return response.json();
  })
  .then((response) => {
    console.debug(response);
    // …
  })
  .catch((error) => {
    console.error(error);
  });
```

## Specifications

| Specification |
|---|
| Fetch # request-class |

## Browser compatibility
