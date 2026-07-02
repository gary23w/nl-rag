---
title: "Window: origin property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Window/origin
domain: same-origin-policy
license: CC-BY-SA-4.0
tags: same-origin policy, web origin model, cross-origin isolation, document domain property
fetched: 2026-07-02
---

# Window: origin property

The **`origin`** read-only property of the `Window` interface returns the origin of the global scope, serialized as a string.

## Value

A string.

## Examples

Executed from inside window scope, the following snippet will log the document's global scope's origin to the console.

```js
console.log(window.origin); // On this page returns 'https://developer.mozilla.org'
```

If the origin is not a scheme/host/port tuple (say you are trying to run it locally, i.e., via `file://` URL), `origin` will return the string `"null"`.

## Specifications

| Specification |
|---|
| HTML # dom-origin-dev |

## Browser compatibility
