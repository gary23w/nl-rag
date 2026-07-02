---
title: "SyncManager - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/SyncManager
domain: background-sync
license: CC-BY-SA-4.0
tags: background sync api, deferred network request, sync event retry, offline action queue
fetched: 2026-07-02
---

# SyncManager

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`SyncManager`** interface of the Background Synchronization API provides an interface for registering and listing sync registrations.

## Instance properties

None.

## Instance methods

**`SyncManager.register()`**

Create a new sync registration and return a `Promise`.

**`SyncManager.getTags()`**

Return a list of developer-defined identifiers for `SyncManager` registrations.

## Specifications

| Specification |
|---|
| Web Background Synchronization # sync-manager-interface |

## Browser compatibility
