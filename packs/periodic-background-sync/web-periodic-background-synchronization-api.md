---
title: "Web Periodic Background Synchronization API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Web_Periodic_Background_Synchronization_API
domain: periodic-background-sync
license: CC-BY-SA-4.0
tags: periodic background sync, periodic sync registration, scheduled content refresh, minimum sync interval
fetched: 2026-07-02
---

# Web Periodic Background Synchronization API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Note:** This feature is available in Web Workers.

The **Web Periodic Background Synchronization API** provides a way to register tasks to be run in a service worker at periodic intervals with network connectivity. These tasks are referred to as periodic background sync requests.

## Concepts and Usage

The Periodic Background Sync API allows web applications to alert their service worker to make any updates, at a periodic time interval. Uses may include fetching latest content whilst a device is connected to Wi-Fi, or allowing background updates to an application.

The minimum time interval is set when the API is invoked; however the user agent might also take into account other factors which affect when the service worker receives the event. For instance previous website engagement, or connection to a known network.

The `PeriodicSyncManager` interface is available through `ServiceWorkerRegistration.periodicSync`. A unique tag identifier is set to 'name' the sync event, which can then be listened for within the `ServiceWorker` script. Once the event is received you can then run any functionality available, such as updating caches or fetching new resources.

As this API relies on service workers, functionality provided by this API is only available in a secure context.

## Interfaces

**`PeriodicSyncManager`**

Registers tasks to be run in a service worker at periodic intervals with network connectivity. These tasks are referred to as periodic background sync requests.

**`PeriodicSyncEvent`**

Represents a synchronization event, sent to the global scope of a ServiceWorker. It provides a way to run tasks in the service worker with network connectivity.

### Extensions to other interfaces

The following additions to the Service Worker API are specified in the Periodic Background Sync specification to provide an entry point for using Periodic Background Sync.

**`ServiceWorkerRegistration.periodicSync` Read only**

Returns a reference to the `PeriodicSyncManager` interface for registering tasks to run at specific intervals.

**`periodicsync` event**

Occurs at periodic intervals, which were specified when registering a `PeriodicSyncManager`.

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

### Listening for a Periodic Background Sync within a Service Worker

The following example shows how to respond to a periodic sync event in the service worker.

```js
self.addEventListener("periodicsync", (event) => {
  if (event.tag === "get-latest-news") {
    event.waitUntil(fetchAndCacheLatestNews());
  }
});
```

## Specifications

| Specification |
|---|
| Web Periodic Background Synchronization |

## Browser compatibility

### api.PeriodicSyncManager

### api.ServiceWorkerGlobalScope.periodicsync_event
