---
title: "Beacon API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Beacon_API
domain: real-user-monitoring
license: CC-BY-SA-4.0
tags: real user monitoring, beacon api reporting, website monitoring, field performance data, web analytics collection
fetched: 2026-07-02
---

# Beacon API

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2018.

- Learn more
- See full compatibility

The **`Beacon`** API is used to send an asynchronous and non-blocking request to a web server. The request does not expect a response. Unlike requests made using `XMLHttpRequest` or the Fetch API, the browser guarantees to initiate beacon requests before the page is unloaded and to run them to completion.

The main use case for the Beacon API is to send analytics such as client-side events or session data to the server. Historically, websites have used `XMLHttpRequest` for this, but browsers do not guarantee to send these asynchronous requests in some circumstances (for example, if the page is about to be unloaded). To combat this, websites have resorted to various techniques, such as making the request synchronous, that have a bad effect on responsiveness. Because beacon requests are both asynchronous and guaranteed to be sent, they combine good performance characteristics and reliability.

For more details about the motivation for and usage of this API, see the documentation for the `navigator.sendBeacon()` method.

**Note:** This API is *not available* in Web Workers (not exposed via `WorkerNavigator`).

## Interfaces

This API defines a single method: `navigator.sendBeacon()`.

The method takes two arguments, the URL and the data to send in the request. The data argument is optional and its type may be a string, an `ArrayBuffer`, a `TypedArray`, a `DataView`, a `ReadableStream`, a `Blob`, a `FormData` object, or a `URLSearchParams` object. If the browser successfully queues the request for delivery, the method returns `true`; otherwise, it returns `false`.

## Specifications

| Specification |
|---|
| Beacon # sendbeacon-method |

## Browser compatibility
