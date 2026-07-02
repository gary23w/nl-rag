---
title: "AbortController - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/AbortController
domain: fetch-api
license: CC-BY-SA-2.5
tags: fetch api, fetch request, http request browser, abortcontroller, fetch response
fetched: 2026-07-02
---

# AbortController

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2019.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`AbortController`** interface represents a controller object that allows you to abort one or more Web requests as and when desired.

You can create a new `AbortController` object using the `AbortController()` constructor. Communicating with an asynchronous operation is done using an `AbortSignal` object.

## Constructor

**`AbortController()`**

Creates a new `AbortController` object instance.

## Instance properties

**`AbortController.signal` Read only**

Returns an `AbortSignal` object instance, which can be used to communicate with, or to abort, an asynchronous operation.

## Instance methods

**`AbortController.abort()`**

Aborts an asynchronous operation before it has completed. This is able to abort fetch requests, consumption of any response bodies, and streams.

## Examples

See the `AbortSignal` page for usage examples.

You can find a full working example on GitHub; you can also see it running live.

## Specifications

| Specification |
|---|
| DOM # interface-abortcontroller |

## Browser compatibility
