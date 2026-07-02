---
title: "PeriodicSyncManager - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PeriodicSyncManager
domain: periodic-background-sync
license: CC-BY-SA-4.0
tags: periodic background sync, periodic sync registration, scheduled content refresh, minimum sync interval
fetched: 2026-07-02
---

# PeriodicSyncManager

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Note:** This feature is available in Web Workers.

The **`PeriodicSyncManager`** interface of the Web Periodic Background Synchronization API provides a way to register tasks to be run in a service worker at periodic intervals with network connectivity. These tasks are referred to as periodic background sync requests. Access `PeriodicSyncManager` through the `ServiceWorkerRegistration.periodicSync`.

## Instance properties

None.

## Instance methods

**`PeriodicSyncManager.register()`**

Registers a periodic sync request with the browser with the specified tag and options. Returns a `Promise` that resolves when the registration completes.

**`PeriodicSyncManager.getTags()`**

Returns a `Promise` that resolves with a list of `strings` representing the tags that are currently registered for periodic syncing.

**`PeriodicSyncManager.unregister()`**

Unregisters the periodic sync request corresponding to the specified tag and returns a `Promise` that resolves when unregistration completes.

## Examples

The following examples show how to use the interface.

### Requesting a Periodic Background Sync

The following asynchronous function registers a periodic background sync at a minimum interval of one day from a browsing context:

```js
async function registerPeriodicNewsCheck() {
  const registration = await navigator.serviceWorker.ready;
  try {
    await registration.periodicSync.register("get-latest-news", {
      minInterval: 24 * 60 * 60 * 1000,
    });
  } catch {
    console.log("Periodic Sync could not be registered!");
  }
}
```

### Verifying a Background Periodic Sync by Tag

This code checks to see if a Periodic Background Sync task with a given tag is registered.

```js
navigator.serviceWorker.ready.then((registration) => {
  registration.periodicSync.getTags().then((tags) => {
    if (tags.includes("get-latest-news")) skipDownloadingLatestNewsOnPageLoad();
  });
});
```

### Removing a Periodic Background Sync Task

The following code removes a Periodic Background Sync task to stop articles syncing in the background.

```js
navigator.serviceWorker.ready.then((registration) => {
  registration.periodicSync.unregister("get-latest-news");
});
```

## Specifications

| Specification |
|---|
| Web Periodic Background Synchronization # periodicsyncmanager-interface |

## Browser compatibility
