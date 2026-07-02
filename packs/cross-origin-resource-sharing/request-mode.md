---
title: "Request: mode property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Request/mode
domain: cross-origin-resource-sharing
license: CC-BY-SA-4.0
tags: cross-origin resource sharing, cors preflight request, access-control-allow-origin header, credentialed cross-origin request
fetched: 2026-07-02
---

# Request: mode property

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`mode`** read-only property of the `Request` interface contains the mode of the request (e.g., `cors`, `no-cors`, `same-origin`, or `navigate`.) This is used to determine if cross-origin requests lead to valid responses, and which properties of the response are readable.

To construct a request with a specific mode, pass the desired value as the `RequestInit.mode` option to the `Request.Request()` constructor.

Note that setting particular modes, especially `no-cors`, places restrictions on the request methods and headers that may be used, and prevents JavaScript from accessing the response headers or body. See the documentation for `RequestInit.mode` for more details.

## Value

One of the following values:

**`same-origin`**

Disallows cross-origin requests. If a request is made to another origin with this mode set, the result is an error.

**`no-cors`**

Disables CORS for cross-origin requests. The response is *opaque*, meaning that its headers and body are not available to JavaScript.

**`cors`**

If the request is cross-origin then it will use the Cross-Origin Resource Sharing (CORS) mechanism.

**`navigate`**

A mode for supporting navigation. The `navigate` value is intended to be used only by HTML navigation. A navigate request is created only while navigating between documents.

### Default mode

Requests can be initiated in a variety of ways, and the mode for a request depends on the particular means by which it was initiated.

For example, when a `Request` object is created using the `Request()` constructor, the value of the `mode` property for that `Request` is set to `cors`.

However, for requests created other than by the `Request()` constructor, `no-cors` is typically used as the mode; for example, for embedded resources where the request is initiated from markup, unless the `crossorigin` attribute is present, the request is in most cases made using the `no-cors` mode — that is, for the `<link>` or `<script>` elements (except when used with modules), or `<img>`, `<audio>`, `<video>`, `<object>`, `<embed>`, or `<iframe>` elements.

## Examples

In the following snippet, we create a new request using the `Request()` constructor (for an image file in the same directory as the script), then save the request mode in a variable:

```js
const myRequest = new Request("flowers.jpg");
const myMode = myRequest.mode; // returns "cors" by default
```

## Specifications

| Specification |
|---|
| Fetch # ref-for-dom-request-mode② |

## Browser compatibility
