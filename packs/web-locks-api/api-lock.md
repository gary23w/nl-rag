---
title: "Lock - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Lock
domain: web-locks-api
license: CC-BY-SA-4.0
tags: web locks api, mutual exclusion resource, cross-tab lock coordination, exclusive shared lock mode
fetched: 2026-07-02
---

# Lock

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`Lock`** interface of the Web Locks API provides the name and mode of a lock. This may be a newly requested lock that is received in the callback to `LockManager.request()`, or a record of an active or queued lock returned by `LockManager.query()`.

## Instance properties

**`Lock.mode` Read only**

Returns the access mode passed to `LockManager.request()` when the lock was requested. The mode is either `"exclusive"` (the default) or `"shared"`.

**`Lock.name` Read only**

Returns the name passed to `LockManager.request()` when the lock was requested.

## Examples

The following examples show how the mode and name properties are passed in the call to `LockManager.request()`. `LockManager` is the object returned by `navigator.locks`.

```js
navigator.locks.request("net_db_sync", showLockProperties);
navigator.locks.request("another_lock", { mode: "shared" }, showLockProperties);

function showLockProperties(lock) {
  console.log(`The lock name is: ${lock.name}`);
  console.log(`The lock mode is: ${lock.mode}`);
}
```

## Specifications

| Specification |
|---|
| Web Locks API # api-lock |

## Browser compatibility
