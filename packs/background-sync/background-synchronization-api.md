---
title: "Background Synchronization API - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API
domain: background-sync
license: CC-BY-SA-4.0
tags: background sync api, deferred network request, sync event retry, offline action queue
fetched: 2026-07-02
---

# Background Synchronization API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **Background Synchronization API** enables a web app to defer tasks so that they can be run in a service worker once the user has a stable network connection.

## Concepts and usage

The Background Synchronization API allows web applications to defer server synchronization work to their service worker to handle at a later time, if the device is offline. Uses may include sending requests in the background if they couldn't be sent while the application was being used.

For example, an email client application could let its users compose and send messages at any time, even when the device has no network connection. The application frontend just registers a sync request and the service worker gets alerted when the network is present again and handles the sync.

The `SyncManager` interface is available through `ServiceWorkerRegistration.sync`. A unique tag identifier is set to 'name' the sync event, which can then be listened for within the `ServiceWorker` script. Once the event is received you can then run any functionality available, such as sending requests to the server.

As this API relies on service workers, functionality provided by this API is only available in a secure context.

## Interfaces

**`SyncManager`**

Registers tasks to be run in a service worker at a later time with network connectivity. These tasks are referred to as *background sync requests*.

**`SyncEvent`**

Represents a synchronization event, sent to the global scope of a `ServiceWorker`. It provides a way to run tasks in the service worker once the device has network connectivity.

### Extensions to other interfaces

The following additions to the Service Worker API provide an entry point for setting up background synchronization.

**`ServiceWorkerRegistration.sync` Read only**

Returns a reference to the `SyncManager` interface for registering tasks to run once the device has network connectivity.

**`sync` event**

An event handler fired whenever a `sync` event occurs. This happens as soon as the network becomes available.

## Examples

The following examples show how to use the interface.

### Requesting a background sync

The following asynchronous function registers a background sync from a browsing context:

```js
async function syncMessagesLater() {
  const registration = await navigator.serviceWorker.ready;
  try {
    await registration.sync.register("sync-messages");
  } catch {
    console.log("Background Sync could not be registered!");
  }
}
```

### Verifying a background sync by Tag

This code checks to see if a background sync task with a given tag is registered.

```js
navigator.serviceWorker.ready.then((registration) => {
  registration.sync.getTags().then((tags) => {
    if (tags.includes("sync-messages")) {
      console.log("Messages sync already requested");
    }
  });
});
```

### Listening for a background sync within a Service Worker

The following example shows how to respond to a background sync event in the service worker.

```js
self.addEventListener("sync", (event) => {
  if (event.tag === "sync-messages") {
    event.waitUntil(sendOutboxMessages());
  }
});
```

## Specifications

| Specification |
|---|
| Web Background Synchronization |

## Browser compatibility

### api.SyncManager

### api.ServiceWorkerGlobalScope.sync_event
