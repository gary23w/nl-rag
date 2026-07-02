---
title: "LockManager - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/LockManager
domain: web-locks-api
license: CC-BY-SA-4.0
tags: web locks api, mutual exclusion resource, cross-tab lock coordination, exclusive shared lock mode
fetched: 2026-07-02
---

# LockManager

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The **`LockManager`** interface of the Web Locks API provides methods for requesting a new `Lock` object and querying for an existing `Lock` object. To get an instance of `LockManager`, call `navigator.locks`.

## Instance methods

**`LockManager.request()`**

Requests a `Lock` object with parameters specifying its name and characteristics.

**`LockManager.query()`**

Returns a `Promise` that resolves with an object that contains information about held and pending locks.

## Specifications

| Specification |
|---|
| Web Locks API # api-lock-manager |

## Browser compatibility
