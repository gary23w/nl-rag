---
title: "ServiceWorkerRegistration: periodicSync property - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/periodicSync
domain: periodic-background-sync
license: CC-BY-SA-4.0
tags: periodic background sync, periodic sync registration, scheduled content refresh, minimum sync interval
fetched: 2026-07-02
---

# ServiceWorkerRegistration: periodicSync property

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`periodicSync`** read-only property of the `ServiceWorkerRegistration` interface returns a reference to the `PeriodicSyncManager` interface, which allows for registering of tasks to run at specific intervals.

## Value

A `PeriodicSyncManager` object.

## Examples

You can access the property from either your main script or the registered service worker.

Here is an example from the main script:

```js
// reference registration
const registration = await navigator.serviceWorker.ready;

// feature detection
if ("periodicSync" in registration) {
  // Background Periodic Sync functionality
  const periodicSync = registration.periodicSync;
}
```

From the service worker:

```js
// service worker script

const periodicSync = self.registration.periodicSync;
```

## Specifications

| Specification |
|---|
| Web Periodic Background Synchronization # dom-serviceworkerregistration-periodicsync |

## Browser compatibility
