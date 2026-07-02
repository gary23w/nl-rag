---
title: "PeriodicSyncEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PeriodicSyncEvent
domain: periodic-background-sync
license: CC-BY-SA-4.0
tags: periodic background sync, periodic sync registration, scheduled content refresh, minimum sync interval
fetched: 2026-07-02
---

# PeriodicSyncEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Note:** This feature is only available in Service Workers.

The **`PeriodicSyncEvent`** interface of the Web Periodic Background Synchronization API provides a way to run tasks in the service worker with network connectivity.

An instance of this event is passed to the `periodicsync` handler. This happens periodically, at an interval greater than or equal to that set in the `PeriodicSyncManager.register()` method. Other implementation-specific factors such as the user's engagement with the site decide the actual interval.

## Constructor

**`PeriodicSyncEvent()`**

Creates a new `PeriodicSyncEvent` object. This constructor is not typically used. The browser creates these objects itself and provides them to `onperiodicsync` callback.

## Instance properties

*Inherits properties from its parent, `ExtendableEvent`.*

**`PeriodicSyncEvent.tag` Read only**

Returns the developer-defined identifier for this `PeriodicSyncEvent`. Multiple tags can be used by the web app to run different periodic tasks at different frequencies.

## Instance methods

*Inherits methods from its parent, `ExtendableEvent`.*

## Examples

The following example shows how to respond to a periodic sync event in the service worker.

```js
self.addEventListener("periodicsync", (event) => {
  if (event.tag === "get-latest-news") {
    event.waitUntil(fetchAndCacheLatestNews());
  }
});
```

`fetchAndCacheLatestNews` is a developer defined function.

## Specifications

| Specification |
|---|
| Web Periodic Background Synchronization # periodicsync-event |

## Browser compatibility
