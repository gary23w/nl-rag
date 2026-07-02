---
title: "Window: cancelIdleCallback() method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Window/cancelIdleCallback
domain: requestidlecallback
license: CC-BY-SA-4.0
tags: request idle callback, idle period scheduling, background task deadline, cooperative task chunking
fetched: 2026-07-02
---

# Window: cancelIdleCallback() method

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The **`window.cancelIdleCallback()`** method cancels a callback previously scheduled with `window.requestIdleCallback()`.

## Syntax

```js
cancelIdleCallback(handle)
```

### Parameters

**`handle`**

The ID value returned by `window.requestIdleCallback()` when the callback was established.

### Return value

None (`undefined`).

## Examples

See our complete example in the article Cooperative Scheduling of Background Tasks API.

## Specifications

| Specification |
|---|
| requestIdleCallback() # the-cancelidlecallback-method |

## Browser compatibility
