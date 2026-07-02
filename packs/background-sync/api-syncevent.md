---
title: "SyncEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/SyncEvent
domain: background-sync
license: CC-BY-SA-4.0
tags: background sync api, deferred network request, sync event retry, offline action queue
fetched: 2026-07-02
---

# SyncEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Note:** This feature is only available in Service Workers.

The **`SyncEvent`** interface of the Background Synchronization API represents a sync action that is dispatched on the `ServiceWorkerGlobalScope` of a ServiceWorker.

This interface inherits from the `ExtendableEvent` interface.

## Constructor

**`SyncEvent()`**

Creates a new `SyncEvent` object.

## Instance properties

*Inherits properties from its parent, `ExtendableEvent` and `Event`*.

**`SyncEvent.tag` Read only**

Returns the developer-defined identifier for this `SyncEvent`.

**`SyncEvent.lastChance` Read only**

Returns `true` if the user agent will not make further synchronization attempts after the current attempt.

## Instance methods

*Inherits methods from its parent, `ExtendableEvent` and `Event`*.

None.

## Specifications

| Specification |
|---|
| Web Background Synchronization # sync-event |

## Browser compatibility
