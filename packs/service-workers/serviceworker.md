---
title: "Navigator: serviceWorker property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Navigator/serviceWorker
domain: service-workers
license: CC-BY-SA-2.5
tags: service worker, offline caching, cache storage api, background sync
fetched: 2026-07-02
---

# Navigator: serviceWorker property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2018.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The **`serviceWorker`** read-only property of the `Navigator` interface returns the `ServiceWorkerContainer` object for the associated document, which provides access to registration, removal, upgrade, and communication with the `ServiceWorker`.

The feature may not be available in private mode.

Note that a worker can similarly access the `ServiceWorkerContainer` for a document using `WorkerNavigator.serviceWorker`.

## Value

`ServiceWorkerContainer`.

## Examples

This code checks if the browser supports service workers.

```js
if ("serviceWorker" in navigator) {
  // Supported!
}
```

## Specifications

| Specification |
|---|
| Service Workers Nightly # navigator-service-worker-attribute |

## Browser compatibility
