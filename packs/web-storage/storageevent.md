---
title: "StorageEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/StorageEvent
domain: web-storage
license: CC-BY-SA-2.5
tags: web storage, localstorage, sessionstorage, browser key-value storage
fetched: 2026-07-02
---

# StorageEvent

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`StorageEvent`** interface is implemented by the `storage` event, which is sent to a window when a storage area the window has access to is changed within the context of another document.

## Constructor

**`StorageEvent()`**

Returns a newly constructed `StorageEvent` object.

## Instance properties

*In addition to the properties listed below, this interface inherits the properties of its parent interface, `Event`.*

**`key` Read only**

Returns a string with the key for the storage item that was changed. The `key` attribute is `null` when the change is caused by the storage `clear()` method.

**`newValue` Read only**

Returns a string with the new value of the storage item that was changed. This value is `null` when the change has been invoked by storage `clear()` method, or the storage item has been removed from the storage.

**`oldValue` Read only**

Returns a string with the original value of the storage item that was changed. This value is `null` when the storage item has been newly added and therefore doesn't have any previous value.

**`storageArea` Read only**

Returns a `Storage` object that represents the storage object that was affected.

**`url` Read only**

Returns string with the URL of the document whose storage changed.

## Instance methods

*In addition to the methods listed below, this interface inherits the methods of its parent interface, `Event`.*

**`initStorageEvent()`**

Initializes the event in a manner analogous to the similarly-named `initEvent()` method in the DOM Events interfaces. Use the constructor instead.

## Specifications

| Specification |
|---|
| HTML # the-storageevent-interface |

## Browser compatibility
